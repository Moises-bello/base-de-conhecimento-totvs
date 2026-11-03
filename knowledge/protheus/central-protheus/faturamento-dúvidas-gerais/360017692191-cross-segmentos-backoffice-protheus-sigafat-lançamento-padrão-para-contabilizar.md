---
article_id: 360017692191
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 8b54bb02df6c9175414652824abeb342c6ea6da85fda06099b2566621d0aac9a
fetched_at: '2026-06-28T22:38:33.055338+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Lançamento Padrão para contabilizar
  no Faturamento
type: support-article
updated_at: '2026-04-27T18:13:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017692191-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Lan%C3%A7amento-Padr%C3%A3o-para-contabilizar-no-Faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31493665432855) Tempo aproximado para leitura: **00:03:00 min**

Dúvida

Quais são as LPs para contabilizar pedido, notas fiscais de saída e notas fiscais de complemento no módulo Faturamento?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - todas as versões.  
  
**Solução**

***Importante: O Lançamento Padrão é desenvolvida com o departamento contábil de sua empresa juntamente com o analista programador, o suporte não auxilia.***

O cadastramento e manutenção é realizado no **Módulo Faturamento** > **Atualizações > Cadastros > Lançamentos Padronizados**

Abaixo, exemplos de uso dos lançamentos mais usados do módulo Faturamento:

|  |  |  |
| --- | --- | --- |
| **LP** | **Nome/Objetivo** | **Exemplo de Sintaxe do LP para testes (preenchimento do campo CT5\_VLR01)** |
| 610 | Documento de Saída - Itens | SD2->D2\_TOTAL |

|  |  |  |
| --- | --- | --- |
| 612 | Pedido de Vendas - Itens | SC6->C6\_VALOR |
| 613 | Documento de Saída - Rateio de Itens | AGH->AGH\_PERC  Outro exemplo  AGH->AGH\_CUSTO1 (Contabilizar valor do rateio da nota de saída, onde o valor da AGH\_CUSTO será SD2->D2\_CUSTO1 \* (AGG→AGG\_PERC/100))    * Importante : Somente é possível contabilizar a tabela AGH   <https://tdn.totvs.com.br/pages/releaseview.action?pageId=220891208> |
| 614 | Pedido de Vendas - Eliminação de Resíduo - Itens | SC6->C6\_VALOR  Documentação no link abaixo  [721327 DSERFAT-441 DT Pedido de Venda - Eliminação de Resíduos](https://tdn.totvs.com/pages/viewpage.action?pageId=286021726) |

|  |  |  |
| --- | --- | --- |
| 620 | Documento de Saída - Total | SF2->F2\_VALMERC |
| 621 | Pedido de Vendas - Total | SC5->C5\_FRETE |
| 630 | Documento de Saída - Exclusão Itens | SD2->D2\_TOTAL |
| 632 | Pedido de Vendas - Exclusão Itens | SC6->C6\_VALOR |
| 633 | Documento de Saída - Exclusão de rateio de Itens | AGH->AGH\_PERC  Outro exemplo  AGH->AGH\_CUSTO1 (Contabilizar valor do rateio da nota de saída, onde o valor da AGH\_CUSTO será SD2->D2\_CUSTO1 \* (AGG→AGG\_PERC/100))    * Importante : Somente é possível contabilizar a tabela AGH   <https://tdn.totvs.com.br/pages/releaseview.action?pageId=220891208> |

|  |  |  |
| --- | --- | --- |
| 635 | Documento de Saída - Exclusão Total | SF2->F2\_VALMERC |
| 636 | Pedido de Vendas - Exclusão Total | SC5->C5\_FRETE |

**Importante**:  
Para notas de complemento ou devolução de compras, não existem lançamentos padronizados específicos. No módulo Faturamento, serão utilizados os LPs 610 ou 620, sendo que a query configurada será responsável por definir quais informações serão consideradas na contabilização.

---

A contabilização dos registros ocorrerá somente para documentos cuja origem seja o módulo Faturamento. Caso o documento não esteja sendo contabilizado, é necessário verificar se o campo **D2\_ORIGLAN** está preenchido com alguma das seguintes origens:

* **LF** = Livros Fiscais
* **LO** = Loja
* **VD** = Venda Direta

Se o campo estiver preenchido com uma dessas opções, orientamos entrar em contato com a equipe responsável pela origem do documento, para que sejam validadas as LPs utilizadas na contabilização do registro.

**Saiba mais:**

[**Contabilização (LPs) no Faturamento (SIGAFAT)**](https://tdn.totvs.com/x/Yn6ZDg)

[**Integração Faturamento X SigaCtb (SIGAFAT)**](https://tdn.totvs.com/x/W2nXIQ)
