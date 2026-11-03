---
article_id: 28659387607319
category: Originação de Grãos (OG)
content_hash: d2553e067c0cfc9e95dfa3b54bff85a8c090f89db5dc797557319bc62610b4b6
fetched_at: '2026-06-28T22:45:37.671938+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Complemento de Quantidade de Fardão
type: support-article
updated_at: '2025-08-11T13:23:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28659387607319-Agro-Linha-Protheus-AGR-Complemento-de-Quantidade-de-Fard%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28659383022359) Tempo aproximado para leitura: **00:02:40 min** **Dúvida**Como funciona um **Complemento de Quantidade de Fardão Serviços**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**Atualmente, no processo que precede o beneficiamento de algodão, o fardão realiza a entrada no Sistema com um peso estimado, sabendo-se seu peso exato apenas no processo de romaneio de entrada, em que ocorre a pesagem. Dessa forma, é preciso informar ao Sistema esse transbordo ou diferença de quantidade, em função de adequar a informação anteriormente informada. 

Para atender essa demanda, foi desenvolvida uma rotina de complemento de fardão, que efetua as movimentações pertinentes a nível de produção, estoque e faturamento, equalizando as informações do Sistema com o disposto no estoque físico. A rotina também contempla o estorno dessas movimentações.

O diagrama abaixo exemplifica a nova tela **AGRA610 - Compl Fardão**:

![](https://tdn.totvs.com/download/attachments/856944698/sequencia_1.PNG?version=1&modificationDate=1721200268377&api=v2)

O processo de geração de complemento contempla os processos de geração de **OP**, apontamento de produção, geração de pedido de venda e de documento de saída. O diagrama abaixo exemplifica o processo de complemento:

![](https://tdn.totvs.com/download/attachments/856944698/sequencia_2.PNG?version=1&modificationDate=1721200268297&api=v2)

É importante salientar que se o processo for interrompido após a geração do pedido de venda, independente de este já ter estoque e/ou crédito liberados, o processo será armazenado até esse ponto e pode ser retomado a partir daí. Caso o processo seja interrompido antes da geração do pedido de venda, todo o processo será desfeito.

Já o processo de estorno contempla o estorno/eliminação de toda a movimentação gerada no processo de complemento, porém, oferece a flexibilidade de permitir que a nota fiscal e o pedido de venda sejam eliminados/estornados pelo módulo **SIGAFAT**, porém, o resto dos movimentos, impreterivelmente, precisam ser desfeitos pelo **AGRA610**. Abaixo, o diagrama exemplifica as movimentações efetuadas pelo processo de estorno:

![](https://tdn.totvs.com/download/attachments/856944698/sequencia_3.PNG?version=1&modificationDate=1721200268153&api=v2)Demais Informações:

|  |  |
| --- | --- |
| **Rotina** | **Nome Técnico** |
| Complemento de Fardão | AGRA610 |
| Produção X Fardão | AGRA605 |
| Romaneio de Entrada | AGRA600 |
| Cadastro de Fardão | AGRA601 |
| **Ponto de Entrada** | [AG610OPR](https://tdn.totvs.com/pages/viewpage.action?pageId=244716215) |
| **Tabelas Utilizadas:** | DXB, DXL, SC5, SC6, SC2, SD3, SF2 |
