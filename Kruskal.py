#RODRIGUEZ JAUREGUI JARED

import matplotlib.pyplot as plt  # Para crear gráficos
import networkx as nx  # Para trabajar con grafos

# Función para graficar el grafo completo
def graficar_grafo_completo(eje, grafo, titulo):
    # Generar las posiciones de los nodos usando el algoritmo spring layout
    posiciones = nx.spring_layout(grafo)
    
    # Dibujar el grafo con las posiciones calculadas, incluyendo etiquetas de los nodos
    nx.draw(grafo, posiciones, with_labels=True, node_color='lightblue', node_size=3000, font_size=15, font_weight='bold', edge_color='gray', ax=eje)
    
    # Obtener las etiquetas de las aristas (pesos de las aristas) y dibujarlas
    etiquetas = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, posiciones, edge_labels=etiquetas, font_size=12, ax=eje)
    
    # Establecer el título del gráfico
    eje.set_title(titulo)

# Función para graficar un Árbol de Mínimo Coste con aristas resaltadas
def graficar_Arbol_con_aristas_resaltadas(eje, grafo, aristas_mst, titulo):
    # Generar las posiciones de los nodos usando el algoritmo spring layout
    posiciones = nx.spring_layout(grafo)
    
    # Dibujar el grafo completo con las posiciones calculadas
    nx.draw(grafo, posiciones, with_labels=True, node_color='lightblue', node_size=3000, font_size=15, font_weight='bold', edge_color='gray', ax=eje)
    
    # Crear un subgrafo solo con las aristas seleccionadas para el árbol
    arbol = nx.Graph()
    arbol.add_weighted_edges_from(aristas_mst)
    
    # Dibujar las aristas seleccionadas en el árbol con un color verde y mayor grosor
    nx.draw_networkx_edges(arbol, posiciones, edge_color='green', width=3, ax=eje)
    
    # Obtener las etiquetas de las aristas (pesos de las aristas) y dibujarlas
    etiquetas = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, posiciones, edge_labels=etiquetas, font_size=12, ax=eje)
    
    # Establecer el título del gráfico
    eje.set_title(titulo)

# Función para realizar el algoritmo de Kruskal (Árbol de Mínimo Coste y Máximo Coste)
def kruskal_paso_a_paso(grafo):
    # Obtener todas las aristas del grafo y ordenarlas de acuerdo a su peso (en orden ascendente)
    aristas = list(grafo.edges(data=True))
    aristas.sort(key=lambda x: x[2]['weight'])  # Ordenar por peso para el árbol de mínimo coste
    
    print("Paso a paso para el Árbol de Mínimo Coste (MST):")
    
    # Inicializar los diccionarios para gestionar los componentes disjuntos (conjuntos de nodos conectados)
    padre = {}
    rango = {}
    
    # Función para encontrar el padre de un nodo en el conjunto disjunto (conjuntos de nodos conectados)
    def encontrar(u):
        if padre[u] != u:
            padre[u] = encontrar(padre[u])  # Recursivamente encontrar el representante del conjunto
        return padre[u]

    # Función para unir dos conjuntos disjuntos
    def unir(u, v):
        raiz_u = encontrar(u)
        raiz_v = encontrar(v)
        
        # Si las raíces son diferentes, unir los conjuntos
        if raiz_u != raiz_v:
            if rango[raiz_u] > rango[raiz_v]:
                padre[raiz_v] = raiz_u  # Hacer el conjunto de u la raíz
            elif rango[raiz_u] < rango[raiz_v]:
                padre[raiz_u] = raiz_v  # Hacer el conjunto de v la raíz
            else:
                padre[raiz_v] = raiz_u  # Si tienen el mismo rango, hacer u la raíz
                rango[raiz_u] += 1  # Aumentar el rango de la raíz

    # Inicializar cada nodo como su propio padre (cada nodo es su propio conjunto)
    for nodo in grafo.nodes():
        padre[nodo] = nodo
        rango[nodo] = 0  # Inicializar el rango a 0

    aristas_mínimas = []  # Lista para almacenar las aristas del Árbol de Mínimo Coste
    
    # Ejecutar el algoritmo de Kruskal para encontrar el Árbol de Mínimo Coste
    for u, v, datos in aristas:
        print("Considerando la arista entre ", u, " y ", v, " con peso ", datos['weight'])
        
        # Si las aristas no forman un ciclo (es decir, si pertenecen a componentes disjuntos)
        if encontrar(u) != encontrar(v):
            aristas_mínimas.append((u, v, datos['weight']))  # Añadir la arista al árbol
            unir(u, v)  # Unir los conjuntos disjuntos
            print("Arista agregada: ", u, " - ", v, " con peso ", datos['weight'])
        else:
            print("Arista omitida: ", u, " - ", v, " - Forma un ciclo")
    
    print("\nÁrbol de Mínimo Coste:")
    print(aristas_mínimas)  # Imprimir el Árbol de Mínimo Coste
    
    # Repetir el proceso para el Árbol de Máximo Coste
    print("\nPaso a paso para el Árbol de Máximo Coste (MST):")
    
    aristas.sort(key=lambda x: x[2]['weight'], reverse=True)  # Ordenar las aristas en orden descendente para el árbol de máximo coste
    
    # Reiniciar los diccionarios de padres y rangos para el nuevo cálculo
    for nodo in grafo.nodes():
        padre[nodo] = nodo
        rango[nodo] = 0

    aristas_máximas = []  # Lista para almacenar las aristas del Árbol de Máximo Coste
    
    # Ejecutar el algoritmo de Kruskal para encontrar el Árbol de Máximo Coste
    for u, v, datos in aristas:
        print("Considerando la arista entre ", u, " y ", v, " con peso ", datos['weight'])
        
        # Si las aristas no forman un ciclo
        if encontrar(u) != encontrar(v):
            aristas_máximas.append((u, v, datos['weight']))  # Añadir la arista al árbol
            unir(u, v)  # Unir los conjuntos disjuntos
            print("Arista agregada: ", u, " - ", v, " con peso ", datos['weight'])
        else:
            print("Arista omitida: ", u, " - ", v, " - Forma un ciclo")
    
    print("\nÁrbol de Máximo Coste:")
    print(aristas_máximas)  # Imprimir el Árbol de Máximo Coste
    
    return aristas_mínimas, aristas_máximas  # Devolver las aristas del Árbol de Mínimo y Máximo Coste

# Definir el grafo con vértices y aristas
grafo = {
    'vertices': ['A', 'B', 'C', 'D', 'E'],
    'aristas': [
        ('A', 'B', 1),
        ('A', 'C', 2),
        ('B', 'C', 2),
        ('B', 'D', 3),
        ('C', 'D', 3)
    ]
}

# Crear un grafo de NetworkX y agregar las aristas del grafo definido
G = nx.Graph()
G.add_weighted_edges_from(grafo['aristas'])

# Ejecutar el algoritmo de Kruskal paso a paso y obtener las aristas de los árboles de mínimo y máximo coste
aristas_mínimas, aristas_máximas = kruskal_paso_a_paso(G)

# Crear la figura con 3 subgráficas para mostrar los resultados
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Graficar el grafo original en la primera subgráfica
graficar_grafo_completo(axs[0], G, "Grafo Original")

# Graficar el Árbol de Mínimo Coste en la segunda subgráfica
graficar_Arbol_con_aristas_resaltadas(axs[1], G, aristas_mínimas, "Árbol de Mínimo Coste")

# Graficar el Árbol de Máximo Coste en la tercera subgráfica
graficar_Arbol_con_aristas_resaltadas(axs[2], G, aristas_máximas, "Árbol de Máximo Coste")

# Ajustar la disposición de los gráficos
plt.tight_layout()

# Mostrar los gráficos
plt.show()