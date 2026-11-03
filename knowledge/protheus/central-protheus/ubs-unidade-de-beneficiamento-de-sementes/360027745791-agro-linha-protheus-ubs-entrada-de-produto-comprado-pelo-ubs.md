---
article_id: 360027745791
category: UBS - Unidade de Beneficiamento de Sementes
content_hash: 33761c384593e88de89e497b596ccace6d24a1f36132a1d7b9af31bf0fbe3e3a
fetched_at: '2026-06-28T22:45:34.798299+00:00'
product: protheus
section_id: 360005696194
source: central-protheus
title: Agro - Linha Protheus - UBS - Entrada de produto comprado pelo UBS
type: support-article
updated_at: '2025-06-24T19:59:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027745791-Agro-Linha-Protheus-UBS-Entrada-de-produto-comprado-pelo-UBS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22238576695831)***Tempo aproximado para leitura: **00:01:25 min****Dúvida**Como é efetuada a entrada de um produto comprado pelo processo de **UBS - Unidade de Beneficiamento de Sementes**?  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBS - Unidade de Beneficiamento de Sementes - Versão 12  
  
**Solução**Quando é efetuada a compra de um produto, para que ele seja manipulado pelo Sistema de **UBS** é necessário, primeiramente, que o parâmetro **MV\_AGRUBS - Cliente utiliza o UBS da SIGAAGR** esteja ativo, pois este parâmetro indica que o Sistema utiliza o processo de **UBS**, e além disso o produto necessita ser semente e também controlado por lote.  
  
Para que a entrada seja efetuada é necessário lançar o produto em um documento de entrada, por meio da rotina **MATA103 - Documento de Entrada**. Ao clicar para salvar o registro será aberta a tela abaixo, que é onde devem ser inseridas as informações que serão levadas para a tabela **NP9 - Lote de Sementes**.

![COMPR.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6934652093079)

Ao salvar, o lote é gerado automaticamente na rotina **AGRA840 - Lote de Sementes**, e a partir desse momento o processo é efetuado normalmente.  
  
O lote pode ser gerado com o nome disponibilizado pelo Sistema.

![COMPR1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6934737269655)

Mas o nome do lote também pode ser alterado conforme as necessidades da empresa.

![COMPR2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6934739232535)  
  
![COMPR3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6934741081495)
