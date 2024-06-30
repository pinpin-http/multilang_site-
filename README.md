
# MultiLang Site

Une application web faite dans le cadre d'un test technique simulant un forum avec des articles, construite avec Django.

## Fonctionnalités

- Support multilingue 
- Gestion des utilisateurs
- Gestion de contenu

## Structure du Projet

- `multilang_site/` : Répertoire principal de l'application Django.
  - `settings.py` : Configuration du projet Django.
  - `urls.py` : Définition des routes de l'application.
  - `wsgi.py` : Point d'entrée de l'application pour les serveurs web compatibles WSGI.
- `app/` : Répertoire contenant les applications Django spécifiques.
  - `models.py` : Définition des modèles de données.
  - `views.py` : Logique de traitement des requêtes et des réponses.
  - `templates/` : Répertoire contenant les templates HTML.
  - `static/` : Répertoire pour les fichiers statiques (CSS, JavaScript).
- `manage.py` : Script utilitaire pour gérer le projet.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/pinpin-http/multilang_site-.git
   cd multilang_site-
   ```

2. Créez un environnement virtuel et activez-le :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sous Windows utilisez `venv\Scripts\activate`
   ```

3. Installez les dépendances requises :
   ```bash
   pip install -r requirements.txt
   ```

4. Exécutez les migrations :
   ```bash
   python manage.py migrate
   ```

5. Lancez le serveur de développement :
   ```bash
   python manage.py runserver
   ```

## Utilisation

- Accédez à `http://localhost:8000` dans votre navigateur.
- Gérez le contenu et les utilisateurs via l'interface d'administration Django.

## État du Projet

Ce projet est non fini en raison d'un manque de temps et a été réalisé en 3 jours. Il manque les fonctionnalitées basé sur l'IA et la traduction des articles dans la bdd.

## Contribution

1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commitez vos modifications (`git commit -m 'Add some AmazingFeature'`)
4. Pushez votre branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request


