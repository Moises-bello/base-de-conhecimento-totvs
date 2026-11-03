---
article_id: 115001428228
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 5ab2be2fc4b9f53aa8e48928b77f2ef64b05df85bb064769b9d9d4c193c87fdf
fetched_at: '2026-06-28T22:38:39.924400+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Pedido de Venda com status
  indevido de bloqueado (ou indevidamente liberado) por Crédito
type: support-article
updated_at: '2026-01-23T17:43:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115001428228-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pedido-de-Venda-com-status-indevido-de-bloqueado-ou-indevidamente-liberado-por-Cr%C3%A9dito
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37345390872471) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**  
Por que meu Pedido de Venda foi bloqueado (ou liberado) indevidamente por Crédito e como posso verificar a causa?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

O status de bloqueio ou liberação de um Pedido de Venda por Crédito é regido por algumas validações de parâmetros, limite de crédito e configurações da operação. As principais para identificar a causa, podem ser verificadas a partir das seguintes etapas:

Confirmação do Bloqueio:

|  |  |  |
| --- | --- | --- |
| **Item** | **Verificação** | **Observação** |
| **Tabela SC9** | Campo **C9\_BLCRED** | Se houver conteúdo, o sistema identificou uma restrição de crédito aplicada ao pedido. |

**Pedido** **LIBERADO indevidamente:**

|  |  |  |
| --- | --- | --- |
| **Parâmetro / Processo** | **Verificação** | **Motivo da Liberação Indevida** |
| **MV\_BLOQUEI** | Deve estar configurado como `.T.` | Se estiver `.F.`, a avaliação de crédito é ignorada no momento da liberação do pedido. |
| **MV\_LIMINCR** | Valor mínimo para análise de crédito | Se o valor do pedido for inferior a esse parâmetro, o crédito não é avaliado. |
| **MV\_CREDCLI** | Configuração `"C"` (Cliente) | O sistema soma o limite de todas as lojas do cliente. Se outra loja possuir saldo de crédito, o pedido pode ser liberado. |
| **E1\_STATUS** | Status dos títulos no Financeiro | Apenas títulos com status `"A"` (Aberto) entram no cálculo. Títulos baixados ou com status diferente não geram bloqueio. |
| **MV\_RISCO(X)** | Prazo de carência por risco | Verifique se o atraso do título é superior ao prazo definido conforme o risco do cliente (**A1\_RISCO**). |

**Pedido** **BLOQUEADO indevidamente:**

|  |  |  |
| --- | --- | --- |
| **Parâmetro / Processo** | **Verificação** | **Motivo do Bloqueio Indevido** |
| **MV\_BLQCRED** | Configurado como `"T"` | O sistema bloqueia propositalmente o crédito quando não há estoque, evitando “prender” o limite do cliente. |
| **MV\_PERMAX** | Percentual máximo de uso do limite | Se o cliente já atingiu o percentual configurado (ex.: 80%), novos pedidos serão bloqueados. |
| **MV\_LIBNODP** | Avaliação de pedidos sem duplicata | Se estiver `"T"`, o crédito é avaliado mesmo que o TES não gere duplicata (**F4\_DUPLIC = N**). |
| **A1\_MSBLQL** | Status do cliente ou da loja | Se estiver igual a `1` (Inativo), o sistema bloqueará o pedido independentemente do limite disponível |

**Observação:** O módulo **Financeiro** (**SIGAFIN**) tem disponível a rotina “**Refaz Dados Cliente / Fornecedor**” (**FINA410**), esta rotina **atualiza os dados** dos campos do **Cadastro de Clientes** (**CRMA980**), caso identifique alguma inconsistência nas informações dos campos, execute esta rotina e verifique se ela é corrigida.

**Saiba mais:**

* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como identificar e liberar bloqueios do Pedido de Vendas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014207291-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-identificar-e-liberar-bloqueios-do-Pedido-de-Vendas)
* [Liberação OU Bloqueio "indevido" de Crédito](https://tdn.totvs.com/x/z2k-Dg)
* [Refaz dados cliente/fornecedor (FINA410)](https://tdn.totvs.com/x/4wEtDw)
