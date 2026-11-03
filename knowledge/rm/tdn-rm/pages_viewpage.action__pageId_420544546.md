---
content_hash: 31ef6d42fd7d6925622a520aa3b53b9e176b040fea3a9fa1b4841947649accf0
fetched_at: '2026-06-29T00:09:13.431026+00:00'
page_id: '420544546'
product: rm
source: tdn-rm
title: 3996324 FISCAL01-6740 DT - EFD - Parâmetro de Geração do Bloco P.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=420544546
version: 1
---

Tempo aproximado para leitura:**02 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | EFD - Contribuições |

**02. SITUAÇÃO/REQUISITO**

O Bloco P do EFD Contribuições não está sendo gerado para empresas do Grupo 2 da REINF.

Verificado no layout de gerador de saídas não gera o Bloco P para períodos posteriores a 01/07/2018.

De acordo com a Nota técnica 07/2018 o Bloco P foi migrado para a REINF para empresas do grupo 1.

<http://sped.rfb.gov.br/arquivo/show/2676>.

**03. SOLUÇÃO**

Foi criado parâmetro na tela de geração da rotina onde o Cliente poderá escolher se deseja gerar o Bloco P ou não.
