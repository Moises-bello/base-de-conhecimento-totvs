---
content_hash: c9ec9a5caa5755d5e6b3bbb87229f7e0fbda279b4b3b9085022754782c20dd19
fetched_at: '2026-06-29T00:09:24.434309+00:00'
page_id: '423937903'
product: rm
source: tdn-rm
title: Monitor de Arquivos
type: documentation
url: https://tdn.totvs.com/display/LRM/Monitor+de+Arquivos
version: 19
---

# Conteúdo

Conteúdo

# 1. Introdução

O **Monitor de Arquivos** é uma ferramenta utilizada para gerenciar o recebimento de arquivos XML relacionados a Documentos Fiscais Eletrônicos. Estes documentos podem ser retornados pelos parceiros homologados com o Backoffice Linha RM ou por terceiros. Cada XML recebido pode ter a resposta de algum processo iniciado no RM ou trazer o recebimento de um novo documento. Seu principal objetivo é garantir que cada arquivo recebido seja direcionado ao processo correto dentro do Módulo. Exemplo: No caso de um arquivo de NF-e, o Monitor irá direcionar este arquivo para que o processo de NF-e faça os devidos tratamentos; se for um XML de CT-e, o Monitor fara o direcionamento para o processo de CT-e.

A gestão dos arquivos realizadas pelo Monitor pode ser automatizada conforme a necessidade do usuário.

Para acessar o Monitor de Arquivos, vá ao módulo *TOTVS Gestão de Estoque, Compras e Faturamento > Integrações > Monitor de Arquivos*.

Clique para expandir

# 2. Parceiros Homologados

Os parceiros homologados atualmente para o envio e processamento de documentos fiscais eletrônicos são:

* **TOTVS Processos Fiscais (TPF)**: Responsável pela integração fiscal e envio de documentos à SEFAZ e prefeituras.
* **TOTVS Transmite**: Ferramenta intermediária para a transmissão e recebimento de Documentos Fiscais Eletrônicos.

Para os documentos de **NF-e** e **CT-e**, também é possível receber o XML oficial diretamente da SEFAZ, sem a necessidade de intermediários.

# 3. Tipos de Documentos Suportados

O **Monitor de Arquivos** permite gerenciar os seguintes tipos de documentos eletrônicos:

* [Nota Fiscal Eletrônica (NF-e)](https://tdn.totvs.com/pages/viewpage.action?pageId=422546178)
* [Nota Fiscal de Consumidor Eletrônica (NFC-e)](https://tdn.totvs.com/pages/viewpage.action?pageId=422546024)
* [Nota Fiscal Eletrônica de Serviços (NFS-e)](https://tdn.totvs.com/pages/viewpage.action?pageId=422546027)
* [Conhecimento de Transporte Eletrônico (CT-e)](https://tdn.totvs.com/pages/viewpage.action?pageId=772807458)
* [Conhecimento de Transporte Eletrônico para Outros Serviços (CT-e OS)](https://tdn.totvs.com/pages/viewpage.action?pageId=773489041)
* [Manifesto Eletrônico Documentos Fiscais (MDF-e)](https://tdn.totvs.com/pages/viewpage.action?pageId=423938051)

# 4. Processos

* [Alterar Status do Arquivo](https://tdn.totvs.com/pages/viewpage.action?pageId=423938372)
* [Importação de Arquivos XML](https://tdn.totvs.com/pages/viewpage.action?pageId=423938146)
* [Serviço de Consulta de Arquivos XML](https://tdn.totvs.com/pages/viewpage.action?pageId=423938181)

# 5. Outras Informações

* O sistema é compatível com **automatizações** para reduzir a intervenção manual nos processos de importação e consulta.
* FAQ's e Resolução de problemas: <https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000837921-Integra%C3%A7%C3%A3o-Com-Totvs-Colabora%C3%A7%C3%A3o>
