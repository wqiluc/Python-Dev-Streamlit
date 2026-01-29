# Passo a Passo:
# 1 - Título;
# 2 - Input do usuário no chat (campo de mensagem);
# 3 - A cada mensagem que o usuário enviar:
#     mostrar a mensagem do usuário no chat; 
#     pegar a pergunta; e
#     enviar para uma terceira IA analisar e responder.
# 4 - Exibir a resposta da IA.

# Resolução:
import streamlit as st #framework que permite desenvolver front e backending com python! 
from openai import OpenAI as IA

modelo_ia = IA(api_key="SUA CHAVE AQUI")

st.write("CHATBOT COM IA (PYTHON + STREAMLIT 🤖🐍)")

if "lista_mensagens_histórico" not in (st.session_state):
    st.session_state["lista_mensagens_histórico"] = [{"role": "system", "content": " "}]
else:
    pass

texto_usuario = st.chat_input("Digite algo: 🤖🐍")
arquivo_envio = st.file_uploader("Anexe abaixo seu arquivo: 👇📁")

# MOSTRA TODO O HISTÓRICO NA TELA (isso que mantém as mensagens acumuladas)
for msg in st.session_state["lista_mensagens_histórico"]:
    if msg["role"] != ("system"):
        st.chat_message(msg["role"]).write(msg["content"])

if (texto_usuario):
    print(f"\n {texto_usuario}")

    # Mostra mensagem do usuário na tela
    st.chat_message("user").write(texto_usuario)

    mensagem_usuario = {
        "role": "user",
        "content": texto_usuario}
    
    st.session_state["lista_mensagens_histórico"].append(mensagem_usuario)

    # Modelos de icon📸:
        # nome do usuário; (primeira letra) (🅰🅱️...)
        # 'user'; (primeira letra salva no navegador do usuário)
        # 'assistant' (icon de um robôzinho 🤖)

    # IA respondendo:
    resposta_ia = modelo_ia.chat.completions.create(
        messages= st.session_state["lista_mensagens_histórico"],
        model = "gpt-4o")
    print(resposta_ia.choices[0].message.content)

    texto_resposta_ia = resposta_ia.choices[0].message.content
    st.chat_message("assistant").write(texto_resposta_ia)

    mensagem_IA = {
        "role": "assistant",
        "content": resposta_ia}
    
    st.session_state["lista_mensagens_histórico"].append(mensagem_IA)
else:
    pass

print("\n", st.session_state["lista_mensagens_histórico"])