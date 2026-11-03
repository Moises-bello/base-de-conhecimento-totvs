---
article_id: 360019522952
category: Faturamento - Cenários de Venda
content_hash: 93a062ca6192a4c32d5691b4f5bc9439860842d2dd089a165cf566d466a233b1
fetched_at: '2026-06-28T22:38:33.980069+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Qual a funcionalidade
  do parâmetro MV_PVRECAL
type: support-article
updated_at: '2025-11-13T15:03:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019522952-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Qual-a-funcionalidade-do-par%C3%A2metro-MV-PVRECAL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**O sistema está recalculando o preço dos itens ao alterar a tabela de preço do Pedido de Venda.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões  
  
**Solução**O parâmetro **MV\_PVRECAL** é utilizado para desabilitar (.T.) ou habilitar(.F.) o recálculo do preço dos itens do pedido de venda ao alterar o código da tabela de preço.

**Exemplo de uso - Pré-Condições**

| Código Tabela | Produto | Preço |
| --- | --- | --- |
| 001 | PRODUTO\_A | R$100,00 |
| 002 | PRODUTO\_A | R$200,00 |

**Situação 1:** Parâmetro **MV\_PVRECAL** configurado como .F. (Habilita o recálculo de preço do produto).

Digitar um pedido de venda utilizando a tabela de preço 001 e incluir o produto **PRODUTO\_A**:

Alterar o código de tabela para 002. O preço do produto será alterado para R$200,00.

Para mais exemplos, acesse: **[FAT0278 Utilização do parâmetro MV\_PVRECAL](http://tdn.totvs.com/pages/viewpage.action?pageId=433236058)**
