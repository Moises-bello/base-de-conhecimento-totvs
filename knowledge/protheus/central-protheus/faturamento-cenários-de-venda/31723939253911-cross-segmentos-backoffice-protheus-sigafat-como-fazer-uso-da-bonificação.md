---
article_id: 31723939253911
category: Faturamento - Cenários de Venda
content_hash: 99d09ffae6ff01d7f59ccf026566cbd34787691842168e69cda850b6d80db41f
fetched_at: '2026-06-28T22:38:34.011801+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como fazer uso da bonificação
type: support-article
updated_at: '2025-04-29T19:09:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31723939253911-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-fazer-uso-da-bonifica%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31723906567063) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual o conceito e como usar a bonificação?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Para utilização do processo de bonificação deve ser informado o parâmetro MV\_BONUSTS, no qual deve ser informado o código da TES utilizado pelas regras de bonificação.

Paralelamente existe também o parâmetro MV\_TESBONS, este não é obrigatório para o processo e recebe a TES que não deve ser considerada nas regras de bonificação.

**Importante:**

O TES informado no parâmetro deve ser utilizado exclusivamente para o tratamento do bônus, não podendo ser usado em outro processo do sistema e não deve ser informado pelo usuário no pedido de venda, pois neste caso o sistema entenderá que se trata de um item bonificado.Não é possível utilizar mais de uma TES (Tipo de Entrada/Saída) para os Itens bonificados. Por padrão a Regra de Bonificação utiliza uma única TES, que é configurada através do parâmetro MV\_BONUSTS

**Etapas:**  
1. Inclusão da Regra de Bonificação:

* Menu > Atualizações > Cenários de Vendas > Regra de Bonificação

1° Passo: Selecione a opção “Incluir” e o sistema apresentará a janela de inclusão para incluir o registro;

2. Preencher os campos ([FAT0092\_Regras\_De\_Bonificação](https://tdn.totvs.com/x/AA5dDg))

Campos cruciais:

|  |  |  |
| --- | --- | --- |
| Produto | ACQ\_CODPRO | Código da produto que será bonificado. |

|  |  |  |
| --- | --- | --- |
| Produto | ACR\_CODPRO | Indica o produto a ser vendido para que a bonificação seja realizada. |

|  |  |  |
| --- | --- | --- |
| Lote | ACR\_LOTE | Quantidade a ser vendida para que a bonificação seja realizada. |
| Lote | ACQ\_LOTE | Lote de quantidade, campo do cabeçalho |

3. Conhecer o conceito dos parâmetros:

MV\_TPBONUS - Indica se as quantidades a serem bonificadas serão acumulativas (.T), ou se serão calculadas pela maior quantidade (.F).

MV\_BONUSTD – Indica se todas as regras de bonificação serão consideradas na análise ou somente a primeira regra a ser encontrada.

**Exemplos:**

* Cenário: Tenho mais de uma regra que envolve o produto X
* Regra 1: Se o cliente comprar 2 quantidades do produto X ganha o produto Z
* Regra 2: Se o cliente comprar 5 quantidades do produto X ganha o produto Y

Supondo que inclua um pedido de venda que contém o produto X e informo 8 quantidades e o meu parâmetro "MV\_BONUSTD = 1", o sistema inclui os dois produtos como bonificação, produtos Z e Y.

Caso o parâmetro "MV\_BONUSTD = 2" o sistema considera a primeira regra de bonificação incluída para o produto X.
