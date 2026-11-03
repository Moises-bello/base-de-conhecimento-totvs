---
content_hash: 134c107b9951305de0687c8a77bb2c7429e65d946e60bee8f360b79ac299e4c4
fetched_at: '2026-07-02T19:24:19.723868+00:00'
page_id: '243661258'
product: protheus
source: tdn-tec
title: Múltiplas instalações do SmartClient HTML (Tomcat) no Linux
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243661258
version: 2
---

Para instalar vários SmartClient HTML na mesma máquina:

1. Realizar a instalação através do instalador disponível no *suporte.totvs.com.br*.
2. Parar o SmartClient HTML através do Terminal:
   1. executar o comando "*ps -aux*" para listar os processos em execução e procurar o PID do SmartClient HTML.
   2. executar o comando "*kill PID*".
3. Copiar a pasta inteira do SmartClient HTML.
4. Acessar a pasta copiada e alterar os seguintes arquivos:
   1. pasta server\bin, arquivo *service.sh*:
      1. Alterar as variáveis ***JAVA\_HOME*** e ***CATALINA\_HOME*** informando o caminho da nova pasta.
   2. pasta server\bin, arquivo *setenv.bat*, alterar a variável ***JRE\_HOME***informando o caminho da nova pasta.
   3. pasta server\conf, arquivo *server.xml*, alterar as portas do Apache Tomcat:
      1. No nó ***server***, forneça um novo valor para o atributo ***port*** (padrão 8005).
      2. No nó ***connector*** de atributo ***protocol*** cujo valor é HTTP/1.1, forneça um novo valor para o atributo ***port***.
5. Subir os processos através do Terminal:
   1. acessar a pasta server\bin
   2. executar o ".*/startup.sh*"
