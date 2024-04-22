import pydicom

# Cargar la imagen DICOM
ds = pydicom.dcmread('./1-001.dcm')

# Obtener información de la imagen
print('Tipo de imagen: ', ds.Modality)
print('Fecha de adquisición: ', ds.AcquisitionDate)
print('Hora de adquisición: ', ds.AcquisitionTime)
print('Tamaño de la imagen: ', ds.Rows, 'x', ds.Columns)
print('Nombre del paciente: ', ds.PatientName)
print('Edad del paciente: ', ds.PatientAge)