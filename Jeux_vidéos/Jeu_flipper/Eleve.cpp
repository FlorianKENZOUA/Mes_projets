#pragma warning( disable : 4996 ) 

#include <cstdlib>
#include <vector>
#include <iostream>
#include <string>
#include "G2D.h"
using namespace std;

struct Cible {
    V2 A, B; // Les deux points qui permettent de définir la cible
    bool active; // Statu de la cible
    int rangee;  // Numéro de rangée de la cible

    Cible(V2 a, V2 b, int r) : A(a), B(b), active(true), rangee(r) {} // Construction de la cible avec itialisation à active
};

struct Bumper {
    V2 position;  // Position du bumper
    float rayon;  // Rayon du bumper
    float lastCollisionTime; // Horodatage du dernier rebond

    Bumper(V2 pos, float r) : position(pos), rayon(r), lastCollisionTime(-1) {} // Construction du bumper
};

struct GameData {
    int idFrame = 0;
    int HeightPix = 800; // Nombre pixel jeu sur verticale
    int WidthPix = 600; // Nombre pixel jeu sur horizontale
    V2 BallPos = V2(300, 400); // Position initiale de la balle
    V2 BallMove; // Vecteur de mouvement de la balle
    int BallRadius = 15; // Rayon de la balle
    int score = 0; // Score, initialisé à 0

    vector<V2> PreviousPos;
    vector<V2> LP{
        V2(595, 550), V2(585, 596), V2(542, 638), V2(476, 671),
        V2(392, 692), V2(300, 700), V2(207, 692), V2(123, 671),
        V2(57, 638), V2(14, 596), V2(5, 550), V2(5,5), V2(595,5), V2(595,550)
    }; // Contours du flipper

    vector<Cible> Cibles;
    vector<Bumper> Bumpers; // Liste des bumpers

    GameData() {
        PreviousPos.resize(50);
        BallMove = V2(10, 20); // Initialisation du vecteur de mouvement de la balle

        // Création des bumpers
        Bumpers.push_back(Bumper(V2(170, 200), 60)); // Bumper en bas à gauche
        Bumpers.push_back(Bumper(V2(430, 200), 60)); // Bumper en bas à droite
        Bumpers.push_back(Bumper(V2(300, 550), 60)); // Bumper en haut

        // Création des cibles
        for (int i = 0; i < 4; i++) {
            Cibles.emplace_back(V2(100, 500 - i * 50), V2(160, 530 - i * 50), 0); // Cible de gauche
            Cibles.emplace_back(V2(500, 500 - i * 50), V2(440, 530 - i * 50), 1); // Cible de droite
        }
    }
};

// Rebond de la balle
V2 Rebond(V2 V, V2 N) {
    N.normalize(); // Normalisation
    V2 T = { N.y, -N.x }; // Vecteur tangent
    double vt = V.x * T.x + V.y * T.y; // Produit scalaire (V.T)
    double vn = V.x * N.x + V.y * N.y; // Produit scalaire (V.N)
    return (T * vt) - (N * vn); // Actualise le vecteur de mouvement de la balle
}

// Détection de collision entre segment et cercle
int CollisionSegCir(V2 A, V2 B, float r, V2 C) {
    V2 AB = B - A;
    V2 T = AB;
    T.normalize();
    float d = prodScal(T, C - A);
    if (d > 0 && d < AB.norm()) { // Condition de collision
        V2 P = A + d * T;
        V2 PC = C - P;
        if (PC.norm() < r) return 2;
    }
    return 0;
}

// Détection de collision entre deux cercles (bille et bumper)
bool CollisionCircleCircle(V2 ballPos, float ballRadius, V2 bumperPos, float bumperRadius) {
    float distance = (ballPos - bumperPos).norm(); // Norme du vecteur centre du bumper/centre de la balle
    return distance < (ballRadius + bumperRadius); // Condition de collision
}

// Fonction pour dessiner un flash de bumper
void DrawBumperFlash(const Bumper& bumper) {
    float elapsedTime = G2D::elapsedTimeFromStartSeconds() - bumper.lastCollisionTime; // temps écoulé depuis la dernière collision avec le bumper
    if (elapsedTime < 1.0f) { // Condition de flash = moins de 1 seconde
        float radius = bumper.rayon + (15 * (1.0f - elapsedTime)); // Calcul du rayon du flash = effet d'animation
        G2D::drawCircle(bumper.position, radius, Color::Yellow, true); // Affichage effet d'animation
    }
}

// Fonction de mise à jour du score
void updateScore(GameData& G, bool bumperCollision, bool targetCollision, bool rowComplete) {
    if (bumperCollision) {
        G.score += 100; // 100 points pour le bumper
    }

    if (targetCollision) {
        G.score += 500; // 500 points pour la cible
    }

    if (rowComplete) {
        G.score += 1111; // Bonus de 1111 points pour une rangée complète
    }
}

void render(const GameData& G) {
    G2D::clearScreen(Color::Black); // Fond
    G2D::drawStringFontMono(V2(10, 10), "Score: " + to_string(G.score), 30, 5, Color::Yellow); // Affichage du score
    G2D::drawCircle(G.BallPos, G.BallRadius, Color::Red, true); // Affichage balle

    for (auto& cible : G.Cibles) {
        Color col = cible.active ? Color::Green : Color::Red;
        G2D::drawLine(cible.A, cible.B, col); // Affichage cible 
    }

    for (int i = 0; i < G.LP.size() - 1; i++)
        G2D::drawLine(G.LP[i], G.LP[i + 1], Color::Green); // Affichage des bords

    for (V2 P : G.PreviousPos)
        G2D::setPixel(P, Color::Green); // Affichage de la trajectoire

    // Dessiner les bumpers et leur flash
    for (auto& bumper : G.Bumpers) {
        Color bumperColor = Color::Blue; // Couleur des bumpers
        G2D::drawCircle(bumper.position, bumper.rayon, bumperColor, true); // Affichage des bumpers
        DrawBumperFlash(bumper); // Dessiner le flash jaune si collision
    }

    if (G2D::isOnPause())
        G2D::drawStringFontMono(V2(100, G.HeightPix / 2), "Pause...", 50, 5, Color::Yellow); // Fonctionnalité de pause

    G2D::Show();
}

void Logic(GameData& G) {
    G.idFrame += 1;
    G.BallPos = G.BallPos + G.BallMove; // Déplacement
    bool rebondEffectue = false; // Initialisation des collisions
    bool bumperCollision = false;
    bool targetCollision = false;
    bool rowComplete = false;

    // Vérification des collisions avec les bumpers
    for (auto& bumper : G.Bumpers) {
        if (CollisionCircleCircle(G.BallPos, G.BallRadius, bumper.position, bumper.rayon)) {
            // Calcul du vecteur normal
            V2 normal = G.BallPos - bumper.position;
            normal.normalize();

            G.BallMove = Rebond(G.BallMove, normal); // Appliquer le rebond

            bumper.lastCollisionTime = G2D::elapsedTimeFromStartSeconds(); // Mise à jour de la dernière collision

            bumperCollision = true;  // Collision avec un bumper
            rebondEffectue = true; // Collision bords
            break; // Sortir de la boucle après le premier rebond
        }
    }

    // Vérification des collisions avec les cibles
    for (auto& cible : G.Cibles) {
        if (cible.active && CollisionSegCir(cible.A, cible.B, G.BallRadius, G.BallPos) == 2) {
            // Calcul du vecteur direction du segment de la cible
            V2 direction = cible.B - cible.A;

            // Calcul du vecteur normal (perpendiculaire au segment de la cible)
            V2 normal = V2(direction.y, -direction.x); // Normal au segment
            normal.normalize();

            // Appliquer le rebond en utilisant la normale
            G.BallMove = Rebond(G.BallMove, normal);

            // Désactiver la cible après collision
            cible.active = false;

            targetCollision = true; // Collision avec une cible

            // Vérifier si c'est la dernière cible active d'une rangée
            bool lastActiveInRangee = true;
            for (const auto& c : G.Cibles) {
                if (c.rangee == cible.rangee && c.active) {
                    lastActiveInRangee = false;
                    break;
                }
            }

            // Si c'est la dernière cible active d'une rangée, réactiver toutes les cibles de cette rangée
            if (lastActiveInRangee) {
                for (auto& c : G.Cibles) {
                    if (c.rangee == cible.rangee) {
                        c.active = true;
                    }
                }

                rowComplete = true; // Rangée complète
            }

            rebondEffectue = true;
            break; // Sortie de la boucle après collision
        }
    }

    // Gestion des rebonds contre les bords de la fenêtre (si aucune collision avec un bumper ou une cible)
    if (!rebondEffectue) {
        if (G.BallPos.x - G.BallRadius < 0) {
            G.BallMove = Rebond(G.BallMove, V2(1, 0));
            rebondEffectue = true;
        }
        else if (G.BallPos.x + G.BallRadius > G.WidthPix) {
            G.BallMove = Rebond(G.BallMove, V2(-1, 0));
            rebondEffectue = true;
        }
        if (G.BallPos.y - G.BallRadius < 0) {
            G.BallMove = Rebond(G.BallMove, V2(0, 1));
            rebondEffectue = true;
        }
        else if (G.BallPos.y + G.BallRadius > G.HeightPix) {
            G.BallMove = Rebond(G.BallMove, V2(0, -1));
            rebondEffectue = true;
        }
    }

    // Vérification des collisions avec les bordures du flipper
    if (!rebondEffectue) {
        for (size_t i = 0; i < G.LP.size() - 1; i++) {
            V2 A = G.LP[i];
            V2 B = G.LP[i + 1];
            int collisionType = CollisionSegCir(A, B, G.BallRadius, G.BallPos);

            if (collisionType == 2) {
                V2 direction = B - A;
                V2 normal = V2(direction.y, -direction.x); // Perpendiculaire au segment
                normal.normalize();
                G.BallMove = Rebond(G.BallMove, normal);
                rebondEffectue = true;
                break; // Sortie de la boucle après rebond
            }
        }
    }

    // Mise à jour des positions précédentes
    G.PreviousPos.push_back(G.BallPos);
    if (G.PreviousPos.size() > 50)
        G.PreviousPos.erase(G.PreviousPos.begin());

    // Mise à jour du score
    updateScore(G, bumperCollision, targetCollision, rowComplete);
}

int main(int argc, char* argv[]) {
    GameData G;
    G2D::initWindow(V2(G.WidthPix, G.HeightPix), V2(200, 200), "Super Flipper 600 !!");
    G2D::Run(Logic, render, G, 50, true);
}
