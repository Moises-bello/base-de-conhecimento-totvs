---
article_id: 23774216137751
category: SIGAEST - MOVIMENTAÇÕES
content_hash: ef891f9d1c7c19045329b853d08e8cc1f99abd0082b2e8b433d0227b657206b8
fetched_at: '2026-06-28T22:38:55.507496+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Estorno de Movimentos
  de produtos com controle de Localização qual o comportamento do Saldo?
type: support-article
updated_at: '2025-03-12T12:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23774216137751-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Estorno-de-Movimentos-de-produtos-com-controle-de-Localiza%C3%A7%C3%A3o-qual-o-comportamento-do-Saldo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23774201433751) Tempo aproximado para leitura: **00:03:20 min**

**Dúvida**

Ao estornar de Movimentos de produtos que utilizam controle de **Localização Física (B1\_LOCALIZ=S)**, qual o comportamento do Saldo? É possível parametrizar?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

No padrão, ao estornar movimentos de produtos que controlam Localização Física, o Saldo estornado gera um novo movimento na tabela SDA aguardando que seja endereçado novamente pela rotina ENDEREÇAMENTO DE PRODUTOS (MATA265). Esse comportamento pode ser ajustado com o **parâmetro MV\_PDEVLOC** com as opções abaixo:

**- 0 - Padrão**, **redistribuir o saldo;**

**- 1 - Localização Original,** **devolve o saldo na Localização que foi requisitado pela movimentação;**

**- 2 - Pergunta,** **se deseja Redistribuir ou Devolver ao Endereço Origem;**

***Observações*:** Com a opção **2** também pode complementar com o **parâmetro MV\_PERGDLT** para determinar o tempo de apresentação da mensagem de tratamento de estorno. No exemplo abaixo definido 9 segundos.

![mv_pergdlt.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/23774521062935)

***Saiba Mais:***

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
