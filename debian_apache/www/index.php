<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comparateur de Claviers</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Comparateur de Claviers</h1>
    </header>

    <main>
        <?php
        ini_set('display_errors', 1);
        ini_set('display_startup_errors', 1);
        error_reporting(E_ALL);        
        // Inclure le fichier de connexion à la base
        include('db.php');

        // Requête SQL pour récupérer les données
        $sql = "SELECT marque, titre, prix, nom_site, lien FROM clavier";
        $result = $conn->query($sql);

        // Vérifier si des données sont disponibles
        if ($result->num_rows > 0): ?>
            <table>
                <thead>
                    <tr>
                        <th>Marque</th>
                        <th>Produit</th>
                        <th>Prix (€)</th>
                        <th>Site</th>
                        <th>Lien</th>
                    </tr>
                </thead>
                <tbody>
                <?php while ($row = $result->fetch_assoc()): ?>
                    <tr>
                        <td><?= htmlspecialchars($row['marque']) ?></td>
                        <td><?= htmlspecialchars($row['titre']) ?></td>
                        <td><?= number_format($row['prix'], 2) ?> €</td>
                        <td><?= htmlspecialchars($row['nom_site']) ?></td>
                        <td><a href="<?= htmlspecialchars($row['lien']) ?>" target="_blank">Voir le produit</a></td>
                    </tr>
                <?php endwhile; ?>
                </tbody>
            </table>
        <?php else: ?>
            <p>Aucun produit trouvé dans la base de données.</p>
        <?php endif;

        // Fermer la connexion
        $conn->close();
        ?>
    </main>

    <footer>
        <p>&copy; <?= date("Y") ?> Comparateur de Claviers</p>
    </footer>
</body>
</html>
