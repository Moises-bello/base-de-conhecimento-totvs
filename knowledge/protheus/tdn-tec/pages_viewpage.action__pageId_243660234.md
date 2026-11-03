---
content_hash: ccc075e30e75ff5521b35e0d5eb1ffffa137b9d248ef7d8b95672c404332517f
fetched_at: '2026-07-02T19:24:19.719184+00:00'
page_id: '243660234'
product: protheus
source: tdn-tec
title: Múltiplas instalações do SmartClient HTML (Tomcat) no Windows
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243660234
version: 5
---

Para instalar vários SmartClient HTML na mesma máquina:

1. Realizar a instalação através do instalador disponível no *suporte.totvs.com.br*.
2. Desinstalar o serviço através do prompt de comando:
   1. entrar na pasta server\bin.
   2. rodar o comando "*totvswebserver.bat REMOVE*".
3. Copiar a pasta inteira do SmartClient HTML.
4. Acessar a pasta copiada e alterar os seguintes arquivos:
   1. pasta server\bin, arquivo *totvswebserver.bat*:
      1. Alterar as variáveis ***JRE\_HOME*** e ***CATALINA\_HOME*** informando o caminho da nova pasta.
      2. Forneça um novo nome do serviço: ***SERVICE\_NAME*** e ***SERVICE\_DISPLAY***
   2. pasta server\bin, arquivo *setenv.bat*, alterar a variável ***JRE\_HOME***informando o caminho da nova pasta.
   3. pasta server\conf, arquivo *server.xml*, alterar as portas do Apache Tomcat:
      1. No nó ***server***, forneça um novo valor para o atributo ***port*** (padrão 8005).
      2. No nó ***connector*** de atributo ***protocol*** cujo valor é HTTP/1.1, forneça um novo valor para o atributo ***port***.
5. Instalar os SmartClient HTML através do prompt de comando:  
   1. entrar na pasta server\bin.
   2. rodar o comando "*totvswebserver.bat INSTALL*".
6. Subir os serviços através do gerenciador de serviços do Windows
