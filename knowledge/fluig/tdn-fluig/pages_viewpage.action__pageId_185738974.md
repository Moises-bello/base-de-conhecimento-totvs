---
content_hash: 97c36e7745fb34439d10c1ad9343f9c10d31d22e2f8f2c5b34ba4827ba0e62d9
fetched_at: '2026-06-28T21:35:18.804685+00:00'
page_id: '185738974'
product: fluig
source: tdn-fluig
title: Integrando widget com serviços SOAP - utilizando o ERP RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185738974
version: 15
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar a forma de integração de *widgets* com serviços SOAP.

# Pré-requisitos

Antes de tudo, é necessário desenvolver o *widget* para, então, realizar a integração com o ERP RM utilizando o protocolo SOAP.

# Criando os arquivos para utilização SOAP

Primeiramente precisamos gerar os arquivos que serão utilizados para consultar o serviço. Neste exemplo, utilizaremos os serviços do ERP RM para obter os dados de aniversariantes.

Para gerar os arquivos, basta executar o comando no console:

bash

Onde:

* **"servidor-rm":** deve ser substituído pelo endereço do servidor onde se encontra o ERP RM;
* **"com.fluig.kitintranet.proxy.soap":** deve ser substituído pelo pacote onde desejamos que o código seja gerado.

Após a execução deste comando, os arquivos são gerados na estrutura de pastas conforme o pacote informado.

Conforme apresentado na imagem, foram gerados vários arquivos que são necessários para a consulta de aniversariantes no ERP RM.

Neste caso, utilizaremos apenas uma classe chamada "WsGlbSSL", conforme exemplificado a seguir:

java" + month + "" + day + "";
String resultSQL = wsGlbSSL.getWsGlbSSLSoap().getResultSQL(user, password, 0, "V", "INTEGR\_FLG.02", param, false);
return buildJSONResponse(resultSQL);
}
}
]]>

Esta classe BirthdayProxy*.*java deve ser chamada via JavaScript utilizando REST. Para saber como criar um serviço REST dentro de um *widget*, acesse .

O resultado será o seguinte:

js
