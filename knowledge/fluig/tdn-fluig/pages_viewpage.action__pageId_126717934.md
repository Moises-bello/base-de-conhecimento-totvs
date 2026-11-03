---
content_hash: 03b1e46abc265fdcf2163051e30da11a2ea4450b6ad0c235d6af0ceb4644304b
fetched_at: '2026-06-28T21:35:17.770379+00:00'
page_id: '126717934'
product: fluig
source: tdn-fluig
title: Enviando dados e fatos do formulário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=126717934
version: 18
---

# Índice

true.\*ndicenone

# Objetivo

Esse guia visa apresentar os passos necessários de configuração para que dados e fatos de **formulários de processos** sejam enviados para o Analytics.

Atenção

Os números de acessos (hits) de registros de formulários não são enviados ao analytics.

# Pré-requisitos

* Conhecimento prévio em determinados pontos, principalmente uma visão geral sobre o TOTVS Fluig Plataforma e o card
* Para configurar é necessário o código do processo e os campos do formulário que serão enviados.

Atenção

O Analytics permite o envio de até 10 campos customizados para cada solicitação workflow.

# Preparando a importação de dados de formulários de processos

1. Na pasta onde está o *analytics-import.jar* crie o diretório "conf"
2. Crie o arquivo descritor (formato txt) com o código do processo dentro da pasta "conf"  
   Ex.: RH.txt
3. Edite o arquivo descritor e inclua os campos desejados (conforme o atributo *name* do formulário) que deverão ser enviados ao Analytics

Exemplo:

html/xmlFormulário do processo workflow
