Feature: US_002 Modifier la durée du film

  En tant que Administrateur
  Je veux modifier la durée d'un film
  Afin de corriger une erreur de saisie ou mettre à jour la fiche technique

  Scenario Outline: Mise à jour de la durée
    Given un film existant avec une durée de 0
    When je modifie la durée pour <nouvelle_duree>
    Then la durée du film doit être égale à <nouvelle_duree>

    Examples:
      | nouvelle_duree |
      | 90             |
      | 120            |
      | 154            |