<?php
// Informations de connexion à la base de données
$host = "mysql";
$user = "toto"; // Nom d'utilisateur de la base
$password = "toto"; // Mot de passe de la base
$dbname = "bdd"; // Nom de la base

// Connexion à la base
$conn = new mysqli($host, $user, $password, $dbname);

// Vérification de la connexion
if ($conn->connect_error) {
    die("Erreur de connexion : " . $conn->connect_error);
}
?>
