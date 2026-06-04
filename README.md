# Segmentation clients par analyse RFM

## Contexte

Un retailer e-commerce souhaite mieux cibler ses actions
marketing. Plutôt qu'une communication uniforme, l'objectif
est d'identifier des groupes de clients homogènes selon
leur comportement d'achat réel à partir de transactions brutes.

## Dataset

- **Source** : [Online Retail UCI](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci)
- **Période** : décembre 2009 → décembre 2011
- **Volume brut** : 1 067 371 transactions, 43 pays
- **Après nettoyage** : 805 549 transactions, 5 878 clients

## Méthodologie

1. Nettoyage des données
   - Suppression des transactions anonymes
   - Suppression des retours et annulations
   - Conversion des types

2. Feature engineering
   - Création des variables RFM par client
   - Récence : jours depuis le dernier achat
   - Fréquence : nombre de commandes distinctes
   - Montant : chiffre d'affaires total généré

3. Préparation pour le clustering
   - Transformation logarithmique (distributions asymétriques)
   - Normalisation StandardScaler

4. Clustering KMeans
   - Courbe du coude → k=4
   - Silhouette Score : 0.365

5. Visualisations
   - Distribution des segments
   - Heatmap RFM
   - Visualisation PCA (variance expliquée : 95.14%)

## Résultats

| Segment | Clients | Récence moy. | Fréquence moy. | Montant moy. |
|---|---|---|---|---|
| Champions | 1 188 (20.2%) | 27 jours | 19 commandes | 11 014€ |
| Perdus | 1 974 (33.6%) | 396 jours | 1 commande | 326€ |
| A risque | 1 465 (24.9%) | 228 jours | 5 commandes | 2 002€ |
| Nouveaux prometteurs | 1 251 (21.3%) | 28 jours | 3 commandes | 865€ |

## Recommandations marketing

- **Champions** → programme VIP, parrainage, accès anticipé produits
- **Perdus** → campagne réactivation, offre exceptionnelle, retrait si non-réponse
- **A risque** → intervention urgente, offre personnalisée sur historique
- **Nouveaux prometteurs** → séquence onboarding, offre 2ème achat

## Points clés

- 58.5% des clients sont perdus ou à risque → enjeu de rétention majeur
- Les Champions génèrent en moyenne 34x plus que les Perdus
- La transformation logarithmique était indispensable sur ce dataset réel

## Limites

- Segmentation statique → à recalculer régulièrement en production
- Le pays n'a pas été pris en compte
- Silhouette Score de 0.365 → chevauchements normaux sur données réelles

## Stack technique

- Python 3
- pandas, numpy
- scikit-learn
- matplotlib, seaborn

## Lancer le projet

```bash
pip install pandas scikit-learn matplotlib seaborn
```

Ouvrir `notebook/rfm_segmentation.ipynb`

## Auteur

[Ton nom] — [Lien LinkedIn]
