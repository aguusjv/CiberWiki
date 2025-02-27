from transformers import pipeline

# Usamos el modelo de lenguaje de Hugging Face
modelo_hf = pipeline("text-generation", model="mistralai/Mistral-7B-Instruct-v0.1")

def generar_contenido(tema):
    prompt = f"Escribe un artículo detallado sobre {tema} en ciberseguridad, con ejemplos y código si aplica."

    respuesta = modelo_hf(prompt, max_length=500)[0]['generated_text']
    
    return respuesta

tema = input("Introduce el tema del artículo: ")
contenido = generar_contenido(tema)

with open(f"docs/{tema.replace(' ', '_')}.md", "w", encoding="utf-8") as file:
    file.write(f"# {tema}\n\n{contenido}")

print(f"✅ Artículo generado y guardado en docs/{tema.replace(' ', '_')}.md")
