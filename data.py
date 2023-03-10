# Data Sanitizer
# ----
# Version 1.0

import json
import re


def sanitizer_title(value):
    # if(valeue[le])
    try:
        title = re.sub('[^a-zA-Z0-9ÁÉÍÓÚáéíóúñÑ \n\.]',
                       '', value["leyenda"][0])
        return title.lower()
    except (KeyError):
        print("No Key")
        return ("")
    except (IndexError):
        print("No Index")
        return ("")


def sanitizer_author(value):
    try:
        if (value["author"]):
            return value["author"].lower()
        else:
            return ("")
    except (KeyError):
        print("Author Error")
        return ("")


def sanitizer_location(value):
    try:
        if (value["location"]):
            return value["location"].lower()
        else:
            return ("")
    except (KeyError):
        print("location Error")
        return ("")


def sanitizer_characters(value):
    try:
        characters = value["personajes"]
        if (characters):
            characters = re.sub('[\.]', '', value["personajes"])
            chars = characters.split(",")
        else:
            chars = ""
        return (chars)

    except (KeyError):
        print("Error in characters")
        return ("")


def sanitizer_text(value):
    result = ""
    for sentence in value["leyenda"][1:]:
        if sentence != "\r\n\r\n":
            result += " ".join(sentence.split()) + " "
        else:
            result += '\n' + '\n'
    # Function
    return result


def sanitizer_img(value, id):
    try:
        image_unique = value["img"][0][17:]
        return (str(id)+"_"+image_unique)
    except (IndexError):
        print("No Image")
        return ("")


def sanitizer_category():
    # Function
    return True


data_test = {"title": "El lazo negro y el lazo blanco", "author": "Balaguer i Cirera, Víctor", "acontecimientos": None, "personajes": "Señor de Cardona", "publicacion": "\r\n", "enlaces": [], "leyenda": ["El lazo negro y el lazo blanco", "\r\n\r\n", " ", "\r\n\r\n", "En otro tiempo, cuando aún recorrían los trovadores las comarcas, y deteniéndose en cada castillo cantaban una trova de amor o de guerra a la familia reunida junto al hogar del castellano, no era extraño oír repetir esta o una parecida balada:", "\r\n\r\n", "El señor de Cardona ha partido para la caza. ", "¡Dios le dé buena caza al señor de Cardona!!", "\r\n\r\n", "Es valiente y es noble, es aguerrido y osado.", "\r\n\r\n", "Caballero en un corcel fogoso que desafía al viento en la carrera, atraviesa bosques y valles seguido de una numerosa comitiva.", "\r\n\r\n", "¡Halalí! ¡halalí! ¡apretad los ijares, jinetes! ¡lanzaos a la carrera! ¡la pieza se escapa! ¡cercadla en el soto! ¡Halalí! ¡halalí!", "\r\n\r\n", "Es que el señor de Cardona está de caza, y cuando el señor de Cardona está de caza parece que la guerra está en el valle.", "\r\n\r\n", "Los bosques se estremecen, la tierra resuena herida por los cascos de los corceles, los montes repiten por todos sus ecos los gritos de los cazadores y los sones de las bocinas.... ¡hasta los árboles tiemblan!", "\r\n\r\n", "¡Buena caza, señor de Cardona, buena caza!", "\r\n\r\n", "Mientras vos corréis tras del jabalí que os huye aguzando sus colmillos, vuestra dulce esposa, revolcándose en el lecho del dolor, espera la hora en que podrá hacer gritar desde lo alto de las murallas del castillo por los servidores que arrojen a puñados las monedas al pueblo: ¡regocijaos, vasallos; al señor de Cardona le ha nacido un hijo; regocijaos!", "\r\n\r\n", "¡Buena caza, señor de Cardona! buena caza! ¡Halalí! ¡halalí! La pieza se os escapa, cazadores ¡Cercadla en el valle! ¡matadla en el soto! ¡Halalí!", "\r\n\r\n", "—Paje, paje mío...", "\r\n\r\n", "Y esto lo dice la vizcondesa entre sollozos, mientras su noble esposo atraviesa el valle y el bosque Tras el fugitivo jabalí.", "\r\n\r\n", "—Paje, paje mío, mi buen paje, por Dios te ruego que bajes a la capilla y que veas si arden ante el altar las lámparas, como tengo encargado.", "\r\n\r\n", "Ya está de vuelta el paje.", "\r\n\r\n", "Dobla una rodilla ante el lecho donde gime su señora, y la dice:", "\r\n\r\n", "—Señora mía, doce son las lámparas que arden ante el altar en memoria de los doce santos compañeros de Cristo Señor nuestro. Todas son de plata fina y ricamente labradas, y de cada una, señora, se escapa una lengua de fuego entre oleadas de perfumes que embalsaman el aire.", "\r\n\r\n", "—Paje mío, mi buen paje, mi señor y el tuyo está en la caza. Así Dios te dé ventura en lides y así la hermosa a quien ames premie tu amoroso afecto, como vayas a reunirte con mi señor y el tuyo en la caza, tan pronto como haya yo dado a luz el hijo que se mueve en mis entrañas. Si es varón, paje mío, atarás a tu brazo derecho un lazo blanco, y deteniendo a tu señor aun en medio de la más desenfrenada carrera, le dirás: “Señor, la vizcondesa os aguarda”. Si es hembra, mi buen paje, atarás a tu brazo izquierdo un lazo negro, e irás también a reunirte con el vizconde en la caza, pero entonces no lo dirás nada. Te pondrás a su lado para que te vea el color del lazo y nada más.", "\r\n\r\n", "Y la condesa ha caído sollozando y entre gemidos sobre el lecho en que se había incorporado.", "\r\n\r\n", "—¡Dadme un varón, Señor, y yo os juro que eternamente arderán entre perfumes las lámparas de plata que se han encendido junto al ara!", "\r\n\r\n", "El puente levadizo se ha bajado. Un paje lo atraviesa a caballo.", "\r\n\r\n", "¡Cómo corre! ¡ay! cómo corre. La cuesta del castillo la ha bajado volando. Ya apenas se le ve. Ya es solo un punto negro en el valle.", "\r\n\r\n", "El paje se ha reunido con su señor, el señor de Cardona que está cazando, en el momento en que pone mano al cuchillo de caza que cuelga a su lado para arrojárselo al montero que debe rematar al jabalí ya rendido.", "\r\n\r\n", "El señor de Cardona ha visto el paje, pero ha visto también atado a su brazo izquierdo un lazo negro.", "\r\n\r\n", "El señor de Cardona ha pasado una mano por su frente, ha mirado al cielo con aire de reproche, ha exhalado un hondo suspiro, y acabando el movimiento que había empezado a la llegada del paje, ha sacado de su vaina de plata su cuchillo de monte y se lo ha arrojado al montero para que degüelle al jabalí.", "\r\n\r\n", "Un año ha pasado.", "\r\n\r\n", "Las doce lámparas de plata vuelven a arder ante el altar, la vizcondesa vuelve a revolcarse entre gemidos por el lecho del dolor, el vizconde vuelve a estar de caza.", "\r\n\r\n", "Como el año anterior, el paje, el mismo paje, vuela a reunirse con el vizconde. También lleva atado un lazo negro a su brazo izquierdo.", "\r\n\r\n", "El señor de Cardona al verlo, hunde con furia el acicate", "[1]", " en el vientre de su caballo y se arroja a lo más fragoso de la selva, sin salir de ella hasta que las sombras han caído sobre el valle.", "\r\n\r\n", "Otro año se ha pasado.", "\r\n\r\n", "Tercera vez vuelven a arder las lámparas, tercera vez vuelve a sentir la vizcondesa un hijo en sus entrañas, tercera vez se ha ido a la caza el señor de Cardona, tercera vez se le ha presentado el paje con un lazo negro.", "\r\n\r\n", "¡Dios te niega un hijo, Ramón Folch, vizconde de Cardona! Dios no quiere darte un varón para que sea espejo de la caballería como su padre! ¡Tres hembras ya y ningún varón! Verdaderamente Dios te castiga. ¿Qué le has hecho a Dios, señor de Cardona?", "\r\n\r\n", "Otro año ha pasado.",
                                                                                                                                                                                                            "Esta vez, al salir para la caza, el señor de Cardona se detiene en el umbral de la estancia donde solloza y gime la vizcondesa.", "\r\n\r\n", "—Despedíos de mí, señora, — dice el señor de Cardona.—Si otra vez se me presenta el paje con el lazo negro, es que la cólera de Dios me persigue, y ya sin volver al castillo, me voy en peregrinación a la Tierra Santa. Adiós, señora.", "\r\n\r\n", "Y la condesa no contesta porque la ahogan las lágrimas.", "\r\n\r\n", "El señor de Cardona ha partido para la caza.", "\r\n\r\n", "¡Dios le dé buena caza al señor de Cardona!", "\r\n\r\n", "¡Halalí! ¡halalí! ¡la pieza se escapa! ¡corred tras ella cazadores! ¡cerradla en el valle! ¡matadla en el soto!¡Halalí! El paje llega montado en un caballo cubierto de espuma. El señor de Cardona le divisa y clava en él los ojos. Pero esta vez, ¡ay! esta vez lleva envuelto a su brazo derecho un lazo blanco. El vizconde arroja un grito de júbilo.", "\r\n\r\n", " —Señores, —exclama volviéndose a los suyos, —un hijo me ha nacido. ¡Bendigamos a Dios que me da un hijo! Y todos se descubren, y la plegaria entreabre todos los labios. El jabalí se ha escapado, la caza se ha concluido. El señor de Cardona vuelve su caballo y se lanza a escape hacia el castillo. Atraviesa el puente levadizo, sube la escalera, cruza el salón de armas, llega a la estancia de su esposa. La madre sonriendo le presenta al hijo llorando. ¡Oh! qué hermoso es y qué bello! De pronto..... ¿qué es eso?.... el recién nacido deja de llorar, sus ojos brillan con un rayo de inteligencia, sus labios se entreabren, su cabeza se alza erguida.....¡Señor! ¡señor! ¿qué es eso? El recién nacido habla. Ahora oiréis lo que ha hablado. ", "\r\n\r\n", "—Treinta días pasarán sobre mí, más allá no viviré. Cerraréis mi cuerpo en un arca y pondréis el arca sobre un caballo al cual daréis libertad. Correrá el caballo a su albedrío y a su albedrío detendrá su curso. Allá dó parare será edificado un monasterio y dedicado al Señor Dios y a San Pedro, porque esta es la voluntad del Señor en cuyo nombre os hablo.", "\r\n\r\n", "El vizconde y su esposa le han escuchado; en sí no pueden volver de su sorpresa. Y fue verdad lo que dijo el niño recién nacido. A los treinta días murió el hijo del señor de Cardona, y fue encerrado su cuerpo en un arca, y el arca puesta sobre un caballo el cual corrió a su albedrío, y cruzó montes y selvas y llanuras, y atravesó el Ter, y ascendió a una de las cumbres de Tirabourg, en el término de Castro-serras, donde fue edificado un monasterio y dedicado al señor Dios y a San Pedro. Y en el mismo monasterio se conservaron las reliquias del niño inocente veneradas todavía por los fieles de Jesucristo... ", "\r\n\r\n", "Tal es la tradición de los siglos.", "\r\n\r\n", "Esta es la balada que cantaba el errante trovador a la familia del castellano reunida junto al hogar para escuchar los cuentos o las trovas del bardo. A esto añadiremos nosotros que aún existen ahora las ruinas del  ", "monasterio de S. Pedro de Caserras", ", fundado en el punto donde, según la tradición, se detuvo el caballo con el arca. Este monasterio hubo de pertenecer más tarde a la ", "orden del Temple", " y luego a los benedictinos cluniacenses", "[2]", ". El señor de Cardona a quien suponemos que la balada se refiere, no tuvo ningún otro varón. La esposa pertenecía a la casa de Urgel, y por este enlace los Cardonas se reunieron con aquella tan ilustre como desgraciada familia. A la muerte del vizconde, volvió a extinguirse la línea varonil de los Cardonas. El vizcondado pasó su primera hija casada con Ramón Roger conde de Pallars. -258- ", "\r\n\r\n", "El hijo segundo de este matrimonio, pues que el primero se quedó con el condado de Pallars, fue el que a la muerte de su madre se tituló vizconde de Cardona bajo el nombre de Guillen Folch.", "\r\n\r\n", " ", "\r\n\r\n", " ", "\r\n\r\n", "FUENTE", "\r\n\r\n", "Balaguer, Víctor. ", "Manresa y Cardona: historia y tradiciones", ". Editorial: [S.l.][s.n.] 1851, pp. 257 y 258", "\r\n\r\n", " ", "\r\n\r\n", "Edición: Pilar Vega Rodríguez.", "\r\n\r\n", "NOTAS", "\r\n\r\n", "\r\n", "[1]", " ", "Acicate", ": ", "1. ", "m. Espuela para picar al caballo provista de una punta aguda con un tope para que no penetre demasiado. (RAE, ", "Diccionario de la lengua española", ")", "\r\n\r\n", "\r\n", "[2]", " La ", "Orden de San Benito", " (en latín: ", "Ordo Sancti Benedicti", "), (O.S.B.) es la orden religiosa fundada por Benito de Nursia, que sigue la Regla dictada por éste a principios del siglo VI para la abadía de Montecassino. Benito de Nursia contribuyó decididamente a evangelización cristiana de Europa por lo que se lo ha declarado Patrono de Europa. Actualmente la Orden está extendida por todo el mundo, con monasterios masculinos y femeninos. Siguiendo su ejemplo e inspiración, diversos fundadores de órdenes religiosas han basado la normativa de sus monasterios en la Regla dejada por Benito, cuyo principio fundamental es", " Ora et labora", ", es decir, reza y trabaja. Los monasterios benedictinos están siempre dirigidos por un superior que, dependiendo de la categoría del monasterio, puede llamarse prior o abad; éste es escogido por el resto de la comunidad. El ritmo de vida benedictino tiene como eje principal el Oficio Divino, también llamado Liturgia de las Horas, que se reza siete veces al día, tal como San Benito lo ordenó. Junto con la intensa vida de oración en cada monasterio, se trabaja arduamente en diversas actividades manuales, agrícolas, etc., para el sustento y el autoabastecimiento de la comunidad. http://monasteriopaular.com/historia2.html", "\r\n", "\r\n", "\r\n"], "img": ["../Adjuntos/Imag/330px-Castell_de_Cardona_2.jpg"]}


# Test
# print(sanitizer_title(data_test))
# print(sanitizer_text(data_test))
