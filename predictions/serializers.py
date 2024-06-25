from rest_framework import serializers

# Lista completa de características
feature_names = [
    'feature_0', 'feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5', 
    'feature_6', 'feature_7', 'feature_8', 'feature_9', 'feature_10', 'feature_11', 
    'feature_12', 'feature_13', 'NumeroDescargas', 'PrecioPromedio', 'DuracionPromedio', 
    'VecesCompartida', 'VecesGuardada', 'VecesRecomendada', 'VecesEscuchada', 
    'PuntuacionMedia', 'NumeroComentarios', 'NumeroLikes', 'NumeroDislikes', 
    'NumeroReproducciones', 'VecesReportada', 'NumeroListas', 'VecesComprada', 
    'VecesRegalada', 'VecesDescartada', 'NumeroArtistas', 'NumeroAlbumes', 
    'VecesFavorita', 'NumeroFormatos', 'NumeroVersiones', 'NumeroCategorias', 
    'NumeroGeneros', 'NumeroInstrumentos', 'NumeroColaboraciones', 'NumeroEventos', 
    'NumeroVentas', 'NumeroVisualizaciones', 'NumeroDescargasAlbum', 'PrecioTotal', 
    'NumeroDiasDisponibles', 'NumeroSemanasDisponibles', 'NumeroMesesDisponibles', 
    'NumeroAñosDisponibles', 'NumeroDiasUltimaDescarga'
]

# Crear un serializador automáticamente con las nuevas características
fields = {name: serializers.FloatField() for name in feature_names}
PredictGenreSerializer = type('PredictGenreSerializer', (serializers.Serializer,), fields)
