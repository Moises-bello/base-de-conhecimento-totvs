---
content_hash: 94a213b478a18a478cbc0acbc72194e27002336f90752953573bd0579e0ec985
fetched_at: '2026-06-29T00:11:55.802385+00:00'
page_id: '864332998'
product: rm
source: tdn-rm
title: FISCAL01-23580 - Cadastro de Municípios | Anexo Dados Fiscais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864332998
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Fiscal |
| Processo | NFS-e e Dados Fiscais dos Município |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-23580 |

## **02. SITUAÇÃO/REQUISITO**

Adicionar um novo campo do tipo *checkbox list* no "Cadastro de Municípios | Anexo Dados Fiscais". Esse campo permitirá ao usuário configurar se os itens da NFS-e devem ser agrupados ou não durante a emissão. O campo deve utilizar o conceito de binário para facilitar futuras evoluções.

Também deverá ser criado um campo para indicar se a mascara da inscrição municipal do prestador deverá ser removida durante a geração do xml da NFS-e.

Regra: O Default desse campo deve ser remover mascara

## **03. SOLUÇÃO**

Foi adicionado 2 novos campos no Dados Fiscais do Município:

NFS-e Agrupar por Itens e Máscara IM Prestador no cadastro do Município.

Ao selecionar o campo Máscara do IM Prestador a mascara Inscrição Municipal do Prestador deixa de ser exibida na NFS-e do layout único e nacional.

Disponível à partir da biblioteca 12.1.2310
