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
2. Feature engineering — création des variables RFM
3. Transformation logarithmique
4. Normalisation et clustering KMeans
5. Visualisation PCA et profilage des segments
6. Recommandations marketing

## Distribution des variables RFM

<img src="images/distribution_rfm.png" width="600"/>

## Courbe du coude

<img src="images/courbe_coude.png" width="500"/>

## Résultats

| Segment | Clients | Récence moy. | Fréquence moy. | Montant moy. |
|---|---|---|---|---|
| Champions | 1 188 (20.2%) | 27 jours | 19 commandes | 11 014€ |
| Perdus | 1 974 (33.6%) | 396 jours | 1 commande | 326€ |
| A risque | 1 465 (24.9%) | 228 jours | 5 commandes | 2 002€ |
| Nouveaux prometteurs | 1 251 (21.3%) | 28 jours | 3 commandes | 865€ |

## Répartition des segments

<img src="images/repartition_segments.png" width="600"/>

## Profil des segments

<img src="images/profil_segments.png" width="600"/>

## Heatmap RFM

<img src="images/heatmap_rfm.png" width="500"/>

## Visualisation PCA

<img src="images/pca_clusters.png" width="600"/>

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

GUEYE khadim — www.linkedin.com/in/khadimgueye1
