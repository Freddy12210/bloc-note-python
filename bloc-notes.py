"""class Note:
    def __init__(self, titre, contenu):
        self.__titre = titre
        self.__contenu = contenu

    def lire_note(self):
        print("Titre : " + self.__titre)
        print("Contenu : " + self.__contenu)



class Bloc_note(Note):
    def __init__(self, nom):
       self.notes = []

    def ajout_note(self, titre, contenu):
        #on crée une nouvelle note de la classe Notes
        note = Note(titre= titre, contenu= contenu)
        self.notes.append(note)


    def lire_notes(self):
        pass

"""

import os

class Bloc_note:
    def __init__(self,filename="bloc-note.txt" ):
        self.filename = filename
        self.note_list = self.charger_bloc()

    def ajout_note(self):
        choix_note = int(input("Choisissez un type de note : \n"
                               "0 - Note classique\n"
                               "1 - Note de rappel\n"))

        new_titre = input("Choisissez un titre : ")
        new_contenu = input("Choisissez un contenu : ")

        match choix_note:
            case 0: #Note classique
                note = Note(new_titre, new_contenu)

            case 1: #Note de rappel
                new_rappel = input("Ajouter une date de rappel : ")
                note = Note_Rappel(new_titre, new_contenu, new_rappel)

        self.note_list.append(note)
        print("Note ajoutée avec succès")


    def lire_bloc(self):
        if not self.note_list:
            print("le bloc est vide")
        else:
            for index, note in enumerate(self.note_list, start=1):
                print(f"{index}, Titre: {note.titre}, Contenu: {note.contenu}")

    def sauvegarder_bloc(self):
        with open(self.filename, "w") as file:
            for note in self.note_list:
                file.write(note.titre + ' / ' + note.contenu + '\n')
        print("Le bloc note a été sauvegardé")

    def charger_bloc(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                return [Note(line.strip()) for line in file.readline()]
        else:
            return []

class Note:
    def __init__(self, titre, contenu):
        self.titre = titre
        self.contenu = contenu

class Note_Rappel(Note):
    def __init__(self, titre, contenu, date_rappel):
        super().__init__(titre, contenu)
        self.date_rappel = date_rappel

if __name__ == "__main__":

    b = Bloc_note()

    while True:
        choix = int(input("Bloc-note\n"
              "1 - Ajouter note\n"
              "2 - Lire les notes\n"
              "3 - Sauvegarder\n"
              "4 - Quitter\n"))

        match choix:
            case 1:
                b.ajout_note()
            case 2:
                b.lire_bloc()
            case 3:
                b.sauvegarder_bloc()
            case 4:
                break

