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

        // Initialisation des filtres
        $marque_filter = isset($_GET['marque']) ? $_GET['marque'] : '';
        $site_filter = isset($_GET['site']) ? $_GET['site'] : '';
        $recherche = isset($_GET['recherche']) ? $_GET['recherche'] : '';

        // Filtre de la requête SQL
        $sql = "SELECT marque, titre, prix, nom_site, lien FROM clavier WHERE 1=1";

        if ($marque_filter != '') {
            $sql .= " AND marque = '$marque_filter'";
        }
        if ($site_filter != '') {
            $sql .= " AND nom_site = '$site_filter'";
        }
        if ($recherche != '') {
            $sql .= " AND titre LIKE '%$recherche%'";
        }

        // Exécuter la requête SQL
        $result = $conn->query($sql);

        // Récupérer les marques et sites disponibles pour les filtres
        $marques_result = $conn->query("SELECT DISTINCT marque FROM clavier");
        $sites_result = $conn->query("SELECT DISTINCT nom_site FROM clavier");
        ?>

        <!-- Formulaire de filtres -->
        <form method="GET" action="">
            <label for="marque">Marque:</label>
            <select name="marque" id="marque">
                <option value="">Toutes</option>
                <?php while ($marque = $marques_result->fetch_assoc()): ?>
                    <option value="<?= htmlspecialchars($marque['marque']) ?>" <?= $marque_filter == $marque['marque'] ? 'selected' : '' ?>>
                        <?= htmlspecialchars($marque['marque']) ?>
                    </option>
                <?php endwhile; ?>
            </select>

            <label for="site">Site:</label>
            <select name="site" id="site">
                <option value="">Tous</option>
                <option value="ldlc" <?= $site_filter == 'ldlc' ? 'selected' : '' ?>>LDLC</option>
                <option value="topachat" <?= $site_filter == 'topachat' ? 'selected' : '' ?>>TopAchat</option>
            </select>

            <label for="recherche">Recherche:</label>
            <input type="text" name="recherche" id="recherche" value="<?= htmlspecialchars($recherche) ?>" placeholder="Rechercher un produit">

            <button type="submit">Filtrer</button>
        </form>

        <!-- Affichage des produits -->
        <?php if ($result->num_rows > 0): ?>
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
                            <td><?= htmlspecialchars($row['prix']) ?></td>
                            <td><?= htmlspecialchars($row['nom_site']) ?></td>
                            <td><a href="<?= htmlspecialchars($row['lien']) ?>" target="_blank">Voir le produit</a></td>
                        </tr>
                    <?php endwhile; ?>
                </tbody>
            </table>
        <?php else: ?>
            <p>Aucun produit trouvé selon vos critères.</p>
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
