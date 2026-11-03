---
content_hash: 6cdea7ed3a0adc3568f68915d301876c0aa94bb9ea2cf2f40dfa0e41300e4704
fetched_at: '2026-06-29T00:12:15.792824+00:00'
page_id: '981794544'
product: rm
source: tdn-rm
title: informações da Tributação IBS/CBS - CT-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=981794544
version: 23
---

# IBSCBS -  Grupo de informações da Tributação IBS/CBS

| **Campo** | **Grupo Pai** | **Ocorrência** | **Ele** | **Descrição** |
| --- | --- | --- | --- | --- |
| **IBSCBS** | **[imp](https://tdn.totvs.com/pages/viewpage.action?pageId=981002580)** | **0-1** | **Grupo** | **Grupo de informações da Tributação IBS/CBS**  Este Grupo será gerado sempre que os tributos IBS e CBS estiverem preenchidos no Movimento e o valor da TTRBMOV.BASEDECALCULO do CBS for maior que 0. Caso o cliente não queira gerar estes tributos, basta deixar configurado para que a base de cálculo fique 0 (este é o gatilho que definirá a entrada em produção deste tributo na reforma tributária. |
| CST | IBSCBS | 1-1 | Elemento | TTRBMOV.SITTRIBUTARIA do CBS  Definido no Movimento |
| cClassTrib | IBSCBS | 1-1 | Elemento | TTRBMOV.CLASSTRIB do CBS  Definido no Movimento |
| indDoacao | IBSCBS | 0-1 | Elemento | Não será gerado |
| **gIBSCBS** | **IBSCBS** | **0-1** | **Grupo** | **Grupo de informações específicas do IBS/CBS.**  **Será gerado de acordo com a [tabela de CSTs](https://dfe-portal.svrs.rs.gov.br/Cff/ClassificacaoTributaria), seguindo o índice IndIBSCBS. Para que essa tabela seja importada no TOTVS Gestão Fiscal e seus valores sejam utilizados na geração dos grupos da CT-e, veja [Tabela CST e Classificação Tributária (IBS e CBS)](https://tdn.totvs.com/pages/viewpage.action?pageId=1011567535).** |
| vBC | gIBSCBS | 1-1 | Elemento | TTRBMOV.BASEDECALCULO do CBS |
| **gIBSUF** | **gIBSCBS** | **1-1** | **Grupo** |  |
| **gIBSMun** | **gIBSCBS** | **1-1** | **Grupo** |  |
| vIBS | gIBSCBS | 1-1 | Elemento | Valor do IBS (soma de vIBSUF e vIBSMun) |
| **gCBS** | **gIBSCBS** | **1-1** | **Grupo** |  |
| **gTribRegular** | **gIBSCBS** | **0-1** | **Grupo** |  |
| **gTribCompraGov** | **gIBSCBS** | **0-1** | **Grupo** | **Não será gerado** |
| **gEstornoCred** | **IBSCBS** | **0-1** | **Grupo** | **Grupo de informações de estorno de crédito. Informado conforme indicador no cClassTrib**  **Não será gerado** |
| vIBSEstCred | gEstornoCred | 1-1 | Elemento | Não será gerado |
| vCBSEstCred | gEstornoCred | 1-1 | Elemento | Não será gerado |
