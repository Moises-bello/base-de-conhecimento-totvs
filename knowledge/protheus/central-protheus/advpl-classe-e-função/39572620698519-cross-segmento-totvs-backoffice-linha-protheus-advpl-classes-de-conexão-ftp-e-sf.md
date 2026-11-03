---
article_id: 39572620698519
category: ADVPL - Classe e Função
content_hash: 0218749631cada3074ae7e3b3e2f7c0c3fdef244f535b4666955f64c103b0de7
fetched_at: '2026-06-28T22:40:20.580682+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Classes de conexão
  FTP e SFTP
type: support-article
updated_at: '2026-04-16T13:58:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39572620698519-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classes-de-conex%C3%A3o-FTP-e-SFTP
---

As classes TFtpClient e tSFTPClient em ADVPL diferem pelo protocolo e segurança: - TFtpClient usa FTP padrão (porta 21) sem criptografia, indicado para redes internas seguras; - tSFTPClient usa SFTP (porta 22) com criptografia SSH, recomendado para integrações seguras externas.

![time.png](https://totvssuporte.zendesk.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**   
Qual é a diferença entre as classes tSFTPClient e TFtpClient em ADVPL e por que utilizar uma em vez da outra?

**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões

**Solução**   
A diferença principal entre as classes está no protocolo de comunicação e na segurança aplicada durante a transferência de arquivos e envio de credenciais.

* **TFtpClient (FTP Padrão):** Utiliza o protocolo FTP (porta padrão 21). Toda a comunicação, incluindo usuário e senha, trafega em texto puro sem criptografia.   
  **Quando usar:** Recomendado apenas em redes internas seguras ou em integrações específicas com sistemas legados que não suportam protocolos criptografados.
* **tSFTPClient (SFTP):** Utiliza o protocolo SFTP baseado em SSH (porta padrão 22). Garante que a autenticação e a transferência de arquivos sejam totalmente criptografadas.   
  **Quando usar:** Recomendado como padrão para qualquer nova integração e obrigatório em comunicações externas (via internet) ou entre empresas diferentes, garantindo a integridade e o sigilo dos dados da operação.

**Passos**

Abaixo estão os exemplos focados na passagem correta de parâmetros para o método `Connect` (responsável pela autenticação) e no uso dos métodos de envio e recebimento.

**1. Exemplo de uso: TFtpClient (FTP Padrão)**

```
User Function ExemploFTP()
    Local oFTP      := TFtpClient():New()
    Local cServer   := "ftp.servidor.com"
    Local nPort     := 21
    Local cUser     := "usuario_ftp"
    Local cPassword := "senha_ftp"

    // O metodo Connect realiza a conexao e a autenticacao no servidor.
    If oFTP:Connect(cServer, nPort, cUser, cPassword)
        ConOut("Autenticacao FTP realizada com sucesso.")
        
        // SendFile: Envia um arquivo local para o servidor
        // Parametros: (1) Caminho Local, (2) Caminho no Servidor
        If oFTP:SendFile("C:\temp\arquivo.txt", "/destino/arquivo.txt")
            ConOut("Arquivo enviado com sucesso!")
        Else
            ConOut("Erro ao enviar o arquivo.")
        EndIf
        
        // ReceiveFile: Baixa um arquivo do servidor para o disco local
        // Parametros: (1) Caminho no Servidor, (2) Caminho Local
        If oFTP:ReceiveFile("/origem/download.txt", "C:\temp\download.txt")
            ConOut("Arquivo recebido com sucesso!")
        EndIf
        
        // Encerra a conexao com o servidor
        oFTP:Disconnect()
    Else
        ConOut("Falha na conexao ou autenticacao FTP.")
    EndIf
Return
```

**2. Exemplo de uso: tSFTPClient (SFTP Seguro)**

```
User Function ExemploSFTP()
    Local oSFTP     := tSFTPClient():New()
    Local cServer   := "sftp.servidor.com"
    Local cPort     := "22" // A classe tSFTPClient recebe a porta como caracter
    Local cUser     := "usuario_sftp"
    Local cPassword := "senha_sftp"
    
    // O metodo Connect no tSFTPClient autentica usando SSH (criptografia).
    If oSFTP:Connect(cServer, cPort, cUser, cPassword)
        ConOut("Autenticacao SFTP segura realizada com sucesso.")
        
        // ReceiveFile: Baixa o arquivo de forma criptografada
        // Parametros: (1) Caminho no Servidor, (2) Caminho Local
        If oSFTP:ReceiveFile("/origem/dados.txt", "C:\temp\dados.txt")
            ConOut("Arquivo seguro recebido com sucesso!")
        Else
            ConOut("Falha na recepcao do arquivo.")
        EndIf
        
        // SendFile: Envia o arquivo de forma criptografada
        // Parametros: (1) Caminho Local, (2) Caminho no Servidor
        If oSFTP:SendFile("C:\temp\envio.txt", "/destino/envio.txt")
            ConOut("Arquivo seguro enviado com sucesso!")
        EndIf
        
        // Encerra a conexao segura
        oSFTP:Disconnect()
    Else
        ConOut("Falha na conexao ou autenticacao SFTP.")
    EndIf
Return
```

**Resumo dos Métodos Utilizados:**

* **New():** Instancia o objeto da respectiva classe.
* **Connect(Servidor, Porta, Usuario, Senha):** Abre a conexão com o servidor e realiza a autenticação simultaneamente com as credenciais informadas.
* **SendFile(OrigemLocal, DestinoRemoto):** Realiza o upload (envio) do arquivo da sua máquina/servidor para o FTP/SFTP.
* **ReceiveFile(OrigemRemota, DestinoLocal):** Realiza o download (recebimento) do arquivo do FTP/SFTP para a sua máquina/servidor.
* **Disconnect():** Encerra a sessão atual e libera a conexão de rede com o servidor.

**Saiba Mais**   
[tSFTPClient](https://tdn.totvs.com/display/tec/tSFTPClient)   
[Classe TFtpClient](https://tdn.totvs.com/display/tec/Classe+TFtpClient)  
[TFtpClient em host compartilhado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039692874-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TFtpClient-n%C3%A3o-conecta)  
[Conexão em protocolo SFTP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004969447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Conex%C3%A3o-em-protocolo-SFTP)
