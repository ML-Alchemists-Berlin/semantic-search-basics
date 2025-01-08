# NER-German-News-Organizations

Este proyecto tiene como objetivo crear un dataset colaborativo para fine-tuning de modelos de Reconocimiento de Entidades Nombradas (NER) enfocado en identificar organizaciones de noticias (tipo `ORG`) en idioma alemán.

## Cómo contribuir

1. Clona este repositorio.
2. Descarga artículos de noticias usando `fetch_articles.py`.
3. Limpia y preprocesa los datos con `preprocess_data.py`.
4. Etiqueta las entidades y contribuye con tu dataset a la carpeta `data/processed/`.

## Instalación

1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
