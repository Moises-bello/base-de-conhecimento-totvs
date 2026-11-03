---
article_id: 4417442157719
category: Faturamento - Integrações
content_hash: 4813b5d5fd61683fb5f19f3ed356ec04fd16053bd0db8f738e6358f2f51a2ba0
fetched_at: '2026-06-28T22:38:26.485579+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Help A410NATCLI e A410NATPED
  na integração do pedido de venda via rotina MATA411
type: support-article
updated_at: '2024-12-10T12:45:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417442157719-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-A410NATCLI-e-A410NATPED-na-integra%C3%A7%C3%A3o-do-pedido-de-venda-via-rotina-MATA411
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28339649333399) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao efetuar a importação do XML pelo Importador XML ou TOTVS Colaboração é gerado o registro no arquivo "**deliveryxml\_salesorder**" o help **A410NATCLI** ou **A410NATPED.**

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - a partir da release 12.

**Causa**O problema ocorre quando o campo **A1\_NATUREZ** não está com a natureza informada no cadastro do cliente no momento da integração do pedido de venda por job **MATA411**.

* Caso o parâmetro (**MV\_1DUPNAT = SA1->A1\_NATUREZ**) será apresentado o Help **A410NATCLI**.

|  |
| --- |
|  |

* Caso o parâmetro (**MV\_1DUPNAT = SC5->C5\_NATUREZ**) será apresentado o Help **A410NATPED**.

|  |
| --- |
|  |

**Obs.:** As divergências de integração do pedido serão geradas nos arquivos "**order**" e "**deliveryxml\_salesorder**" dentro da pasta **XML**, criada na pasta **System**.

**Solução**

* **Help** **A410NATCLI (MV\_1DUPNAT = SA1->A1\_NATUREZ)**

Altere o cadastro do cliente utilizado para a integração e selecione via consulta **[F3]**, a natureza que deverá ser utilizada no campo **A1\_NATUREZ**;

Salve a alteração e posteriormente efetue a atualização da tarefa schedule para que o sistema processe o XML para integração do pedido de venda (**MATA411**).

* **Help A410NATPED (MV\_1DUPNAT = SC5->C5\_NATUREZ)**

Por padrão na integração do pedido de venda (**MATA411**), o sistema sempre utilizará a natureza que está cadastrada no cadastro do cliente (**A1\_NATUREZ**).

**Nesse caso temos duas opções:**

**1 -** Altere o cadastro do cliente utilizado para a integração e informe uma natureza válida que deverá ser utilizada no campo **A1\_NATUREZ**.

Salve a alteração e posteriormente efetue a atualização da tarefa schedule para que o sistema processe o XML para integração do pedido de venda (**MATA411**).

**2 -** Caso não queira utilizar a natureza no cadastro do cliente, poderá customizar por meio do ponto de entrada **MA411GRV** e informar a natureza no campo **C5\_NATUREZ**:  
  
[MA411GRV - Manipula os dados do pedido de vendas gerado através do EDI de Vendas (TOTVS Colaboração)](https://tdn.totvs.com/x/oxc-Dg)
