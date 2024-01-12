# Importar as bibliotecas speedtest e tkinter uma simples intrerface gráfica
import speedtest
import tkinter

# Criar o objeto speedtest e passando o parametro sectre=true para evitar algum erro do tipo forbidden 404
st = speedtest.Speedtest(secure=True)

# Criando a janela, título da janela e resolução da window
window = tkinter.Tk()
window.title("Teste de velocidade da internet")
window.geometry("640x480")

# Criar uma função para testar a velocidade e atualizar os labels e obter os valores em megabites 
def test_speed():
    download = st.download() / 1000000
    upload = st.upload() / 1000000
    ping = st.results.ping

    # Atualizar os labels e exibir os valores formatados com f strings
    download_label.config(text=f"Download: {download:.2f} Mbps")
    upload_label.config(text=f"Upload: {upload:.2f} Mbps")
    ping_label.config(text=f"Ping: {ping:.2f} ms")

# Criar um simples button para iniciar o teste
button = tkinter.Button(window, text="Testar velocidade", command=test_speed)
button.pack(pady=10)

# Criar labels para mostrar os resultados em Mbps 
download_label = tkinter.Label(window, text="Download: 0.00 Mbps")
download_label.pack()
upload_label = tkinter.Label(window, text="Upload: 0.00 Mbps")
upload_label.pack()
ping_label = tkinter.Label(window, text="Ping: 0.00 ms")
ping_label.pack()

# Iniciar o loop da janela, regra basica 
window.mainloop()