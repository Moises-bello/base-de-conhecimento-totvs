---
content_hash: 0aba06cc6ec3ef32a28be873689101b0a9fd1a363d905ee1d1189afd89b522e0
fetched_at: '2026-06-29T00:11:03.388570+00:00'
page_id: '621599683'
product: rm
source: tdn-rm
title: FISCAL01-15523 DT Autenticação TSS - Criar campos de autenticação - REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=621599683
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Autenticação TSS |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15523 |

## **02. SITUAÇÃO/REQUISITO**

Adicionar os novos campos em:

Ambiente | Parâmetros | Gestão Fiscal

03.05 - Integração  
03.05.06 - TSS  
Parametrizar Filial -> Gerais

Campos:  
● CLIENT\_ID - Alfanumérico - Tamanho 40  
● CLIENT\_SECRET - Alfanumérico - Tamanho 256

## **03. SOLUÇÃO**

Foi criado os dois novos campos para autenticação com o TSS.

Na tabela DPARAMETROSEMPRESA foi adicionado dois novos campos:

CLIENTIDTSS VARCHAR(40)

CLIENTSECRETTSS VARCHAR(256)

Caminho: Gestão Fiscal | Ambiente | Parâmetros | Gestão Fiscal | Integração | TSS, parametrizar a Filial.

Marcação do SCRIPT: LI.2021.06\_02

Disponível a partir da versão 12.1.33.
