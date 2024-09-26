from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def instructores(request):
    data = {
        'tipodato' : 'Descripción',
        'titulo' : 'Instructores',
        'nombre1' : 'Jorge Jaramillo',
        'nombre2' : 'Zack Zuñiga',
        'nombre3' : 'Hector Huaiquipan',
        'dato1' : 'Especialidad: Desarrollo de Software para Dispositivos Móviles',
        'dato2' : 'Especialidad: Inteligencia Artificial Aplicada',
        'dato3' : 'Especialidad: Ciberseguridad y Protección de Datos',
        'descripcion1' : 'Mi especialidad es el desarrollo de software para dispositivos móviles, centrada en la creación de aplicaciones nativas y multiplataforma para Android e iOS. Manejo tecnologías como Kotlin, Swift y frameworks como React Native para diseñar soluciones eficientes y de alto rendimiento. Además, me enfoco en la optimización de interfaces, integración con APIs y garantizar una experiencia de usuario fluida, desde el diseño inicial hasta el despliegue en tiendas de aplicaciones.',
        'descripcion2' : 'Especialista en Inteligencia Artificial Aplicada, con experiencia en el desarrollo e implementación de soluciones basadas en machine learning, redes neuronales y procesamiento de lenguaje natural. Mi enfoque está en crear modelos predictivos, optimizar sistemas inteligentes y aplicar técnicas avanzadas de IA en diversas industrias como la salud, finanzas y automatización. Utilizo herramientas como TensorFlow y PyTorch para entrenar modelos de alto rendimiento, siempre buscando soluciones innovadoras y escalables en entornos empresariales.',
        'descripcion3' : 'Especialista en Ciberseguridad y Protección de Datos, con un sólido conocimiento en la identificación y mitigación de amenazas cibernéticas. Mi enfoque está en proteger la infraestructura digital de las organizaciones, implementando medidas de seguridad avanzadas y gestionando incidentes para minimizar riesgos. Tengo experiencia en auditorías de seguridad, análisis forense digital y cumplimiento de normativas internacionales de protección de datos, garantizando la confidencialidad e integridad de la información sensible en entornos complejos.',
        'imagen1' : 'Jorgeuno.jpg',
        'imagen2' : 'Jorgedos.jpg',
        'imagen3' : 'Zackuno.jpg',
        'imagen4' : 'Zackdos.jpg',
        'imagen5' : 'Hectorunoo.jpg',
        'imagen6' : 'Hectordoss.jpg'
    }
    return render(request, 'informacion.html', data)

def cursos(request):
    data = {
        'tipodato' : 'Reseña',
        'titulo' : 'Cursos',
        'nombre1' : 'Programación Orientada a Objetos',
        'nombre2' : 'Programación de Sistemas IoT para el Hogar Inteligente',
        'nombre3' : 'Desarrollo de Aplicaciones Web con React',
        'descripcion1' : 'Este curso está orientado a quienes deseen comprender los principios fundamentales de la Programación Orientada a Objetos (POO). Durante 25 horas, los estudiantes aprenderán a estructurar software utilizando clases, objetos, herencia, polimorfismo y encapsulamiento. Se trabajará con lenguajes como Java y Python para desarrollar proyectos que simulen escenarios del mundo real, facilitando la creación de código más modular, reutilizable y fácil de mantener. Al final del curso, los participantes estarán capacitados para aplicar los conceptos de POO en el desarrollo de aplicaciones robustas.',
        'descripcion2' : 'Este curso está diseñado para introducir a los estudiantes en el mundo de la programación aplicada a dispositivos del Internet de las Cosas (IoT). A lo largo de 10 semanas, los participantes aprenderán a conectar sensores y actuadores a una red doméstica, desarrollar software para el control remoto de electrodomésticos y optimizar sistemas de automatización del hogar. Al finalizar el curso, los estudiantes tendrán las habilidades necesarias para diseñar su propio ecosistema de hogar inteligente utilizando plataformas como Arduino, Raspberry Pi y tecnologías de red.',
        'descripcion3' : 'En este curso, los estudiantes aprenderán a desarrollar aplicaciones web modernas y dinámicas utilizando React, una de las bibliotecas más populares de JavaScript. Durante 30 horas, se explorarán conceptos clave como componentes, hooks, manejo de estado y enrutamiento. Los participantes crearán interfaces interactivas y optimizadas, mientras adquieren buenas prácticas para organizar y escalar proyectos. Al finalizar, los estudiantes estarán preparados para construir aplicaciones web responsivas y altamente interactivas, listas para el despliegue en producción.',
        'dato1' : 'Duración: 25 horas',
        'dato2' : 'Duración: 20 horas',
        'dato3' : 'Duración: 30 horas',
        'imagen1' : 'Poouno.jpg',
        'imagen2' : 'Poodos.jpg',
        'imagen3' : 'Iotuno.jpg',
        'imagen4' : 'Iotdos.jpg',
        'imagen5' : 'Reactuno.jpg',
        'imagen6' : 'Reactdos.png'
    }
    return render(request, 'informacion.html', data)

def egresados(request):
    data = {
        'tipodato' : 'Opinión',
        'titulo' : 'Egresados',
        'nombre1' : 'Laura Martínez',
        'nombre2' : 'Javier Torres',
        'nombre3' : 'Sofía Reyes',
        'dato1' : 'Empresa: TechSolutions AI',
        'dato2' : 'Empresa: SecureNet Corp.',
        'dato3' : 'Empresa: MobileDev Innovations',
        'descripcion1' : 'Estudiar Inteligencia Artificial aplicada me ha permitido dar un salto en mi carrera profesional. Ahora en TechSolutions AI, trabajo con algoritmos de machine learning que mejoran la eficiencia de nuestros sistemas de recomendación. Las herramientas y conocimientos adquiridos durante mi especialización me han permitido desarrollar soluciones innovadoras que están marcando una diferencia en el mercado. Estoy orgullosa de los proyectos que hemos logrado implementar.',
        'descripcion2' : 'Trabajar en SecureNet Corp. como especialista en ciberseguridad ha sido un desafío constante, pero también una experiencia gratificante. Gracias a mi formación, he podido liderar proyectos para mejorar la seguridad de nuestros sistemas y proteger datos confidenciales. La ciberseguridad es un campo en continuo cambio, y es emocionante estar a la vanguardia de las tecnologías que mantendrán seguras a las empresas del futuro.',
        'descripcion3' : 'Como desarrolladora de software para dispositivos móviles en MobileDev Innovations, he podido aplicar directamente las habilidades aprendidas durante mi especialización. Desde la creación de interfaces atractivas hasta la optimización de aplicaciones para el rendimiento, cada proyecto es un nuevo reto. Me encanta ver cómo nuestras aplicaciones se lanzan al mercado y reciben tan buena aceptación de los usuarios, sabiendo que formé parte del proceso desde el inicio.',
        'imagen1' : 'Laurauno.webp',
        'imagen2' : 'Laurados.jpg',
        'imagen3' : 'Javieruno.jpg',
        'imagen4' : 'Javierdos.jpg',
        'imagen5' : 'Sofiauno.avif',
        'imagen6' : 'Sofiados.jpg'
    }
    return render(request, 'informacion.html', data)