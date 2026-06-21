import sys
import argparse

def sort_words(words_list, order='asc'):
    """
    Ordena una lista de palabras.
    
    Args:
        words_list: Lista de palabras a ordenar
        order: 'asc' para ascendente, 'desc' para descendente
    
    Returns:
        Lista ordenada
    """
    if order == 'asc':
        return sorted(words_list)
    elif order == 'desc':
        return sorted(words_list, reverse=True)
    else:
        print(f"Error: Orden '{order}' no válido. Use 'asc' o 'desc'")
        return words_list

def main():
    # Configurar el parser de argumentos
    parser = argparse.ArgumentParser(description='Ordena una lista de palabras')
    parser.add_argument('palabras', nargs='*', 
                       help='Lista de palabras a ordenar (ej: perro gato casa)')
    parser.add_argument('-o', '--orden', choices=['asc', 'desc'], 
                       default='asc', help='Orden: asc (ascendente) o desc (descendente)')
    parser.add_argument('-a', '--archivo', 
                       help='Archivo con palabras (una por línea)')
    
    args = parser.parse_args()
    
    # Obtener las palabras
    palabras = []
    
    if args.archivo:
        # Leer desde archivo
        try:
            with open(args.archivo, 'r', encoding='utf-8') as f:
                palabras = [linea.strip() for linea in f if linea.strip()]
            print(f"📖 Palabras leídas desde {args.archivo}: {len(palabras)} palabras")
        except FileNotFoundError:
            print(f"❌ Error: No se encontró el archivo '{args.archivo}'")
            return
    elif args.palabras:
        # Usar palabras de la línea de comandos
        palabras = args.palabras
    else:
        # Lista de ejemplo por defecto
        palabras = ["perro", "gato", "elefante", "abeja", "delfin", "cocodrilo"]
        print("📝 Usando lista de ejemplo por defecto")
    
    # Mostrar lista original
    print(f"\n📋 Lista original ({len(palabras)} palabras):")
    print(f"   {', '.join(palabras)}")
    
    # Ordenar
    palabras_ordenadas = sort_words(palabras, args.orden)
    
    # Mostrar resultado
    orden_texto = "ascendente 📈" if args.orden == 'asc' else "descendente 📉"
    print(f"\n✅ Lista ordenada ({orden_texto}):")
    print(f"   {', '.join(palabras_ordenadas)}")

if __name__ == "__main__":
    main()