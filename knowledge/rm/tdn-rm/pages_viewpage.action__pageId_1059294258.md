---
content_hash: 163c465ce520b5da5ea454b7839acce1eac306e8529e9e481160c00b04d86af7
fetched_at: '2026-06-29T00:05:52.695634+00:00'
page_id: '1059294258'
product: rm
source: tdn-rm
title: PI - Comissão 2.0 - Configuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1059294258
version: 32
---

Esta página tem como objetivo de orientar a configuração da Comissão 2.0 dentro do portal de imóveis.

A comissão 2.0 está sendo construída utilizando o [PO UI](https://po-ui.io/) Biblioteca de componentes baseado em Angular e é hospedado de forma nativa no RM.Host, neste documento vamos abordar os procedimentos necessários para a configuração.

Importante!

A comissão 2.0 está disponível para versão TOTVS RM Portal - a partir da versão 12.1.2205 apenas para cliente piloto.

Para utilizar deverá estar com as configurações de API Port do RM devidamente configuradas:

---

Para configurar o Portal para comissão 2.0 será necessário configurar os itens:

* config.json
* API REST TOTVS: URL
* web.config

# **Passo 1:**

**Configurando config.json do Portal que acessa o Serviço de API do Host**

No diretório de instalação da biblioteca RM "C:\TOTVS\CorporeRM\RM.Net\wwwroot\config\" abra o arquivo de configuração do Portal "config.json". Nele serão possíveis de se efetuar as seguintes configurações:

1config.jsontrue

---

"**apiServer**": endereço da API do serviço do Host do RM

* A porta da API deve estar preenchida com a **mesma porta** informada na **configuração do Host:  "ApiPort".**
* O endereço localhost limita o acesso no portal somente para ambiente de desenvolvimento. Para acessos externos o endereço deve ser alterado para o nome completo do computador (Exemplo: [http://NOME\_DA\_MAQUINA\_COM\_SERVICO:8052)](http://bhn050102752.bh01.local:8051)) onde ***NOME\_DA\_MAQUINA\_COM\_SERVICO*** é o nome da máquina, ou o IP.

Importante

Após configurar o arquivo config.json, é necessário limpar o cache do navegador, caso contrário, o arquivo de configuração antigo será mantido por um tempo.  
A Tag **rmApiServer** deve obrigatoriamente **terminar com barra "/"**.

---

**Importante: Até a versão 12.1.2602 e seus patchs, é possível compartilhar a mesma porta para os serviços HTTP e API.****Nas versões superiores a 12.1.2602 deverá ser revisitado a configuração de portas quando host em uma mesma instalação.**

**HTTPPORT: 8051 (permanece igual)**  
**APIPORT   : 8052 (nova porta padrão)**

Caso a porta **8052**não esteja disponível, será exibida uma mensagem no console do **RM.Host.Exe** informando o problema. Nesse caso, será necessário reservar a porta configurada utilizando o comando:

Atenção

**As portas devem estar devidamente reservadas na rede. Mais informações sobre essa configuração,**

---

# **Passo 2:**

**Configurando parâmetro:** **API REST TOTVS: URL no Portal**

Acesse o Portal de Imóveis - Backend - Parâmetros - TOTVS  
- Informe no campo **"API REST TOTVS: URL"** URL base para acessar as APIS da TOTVS --> como configurar: **[S](https://tdn.totvs.com/pages/viewpage.action?pageId=1059294258#Configuracoes-comissaoconfigpi:~:text=8051%20(permanece%20igual)-,APIPORT,-%3A%208052%20(nova%20porta)iga as intruções do** "*passo 1*"

# **Passo 3:**

**Configurando *web.config* **do Portal de Imóveis****

Certifique a existência do arquivo ***web.config***  em seu ambiente de instalação do portal.    
Geralmente, é adotado o caminho fisico,  (C:\TOTVS\CorporeRM\FrameHTML\Web\App\Imb\PVI\API\ Segue o padrão do Web.config

xmlEclipseWeb.config



























]]>#FF9000Notas

* Vale lembrar que, por padrão o compartilhamento de recursos com origens diferentes ([CORS](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/CORS))  vai liberado.  
  Caso seja necessário bloquear algumas destas configurações, o Web.config do portal de imóveis na pasta /PVI/api, deverá ser alterado. as tag's responsáveis são:

  xmlCors




  ]]>
