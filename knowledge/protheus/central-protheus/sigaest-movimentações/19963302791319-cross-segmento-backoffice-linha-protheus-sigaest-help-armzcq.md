---
article_id: 19963302791319
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 455e883dddd1c5ec1075c276f92cb6d99485d0212afcceb3cbc67260f8fa0140
fetched_at: '2026-06-28T22:38:55.566435+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP ARMZCQ
type: support-article
updated_at: '2025-03-12T11:40:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19963302791319-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-ARMZCQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19963302780183) Tempo aproximado para leitura: **00:03:15 min** **Dúvida**Porque ocorre o HELP ARMZCQ ao faturar um pedido de venda? Porque nao ocorre o HELP ARMZCQ quando efetua um pedido de venda?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Mensagem de Ajuda (HELP ARMZCQ)**

A mensagem de ajuda "HELP ARMZCQ" é gerada no contexto de um pedido de venda, especificamente quando são utilizadas configurações específicas para o pedido de venda e TES (Tipo de Entrada e Saída), observando as seguintes premissas:

**ETAPA 1 (exibe o HELP)**  
1. O campo C5\_TIPO estiver configurado como "N" ou "B".  
2. O campo F4\_PODER3 for diferente de configurado como "D".  
3. O campo MV\_CQ deve indicar o armazém no qual o faturamento será realizado.

A condição para a exibição da mensagem, ocorre em casos os campos a seguir sejam iguais das configurações mencionadas acima, a mensagem "HELP ARMZCQ" será exibida.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19963365905047)

**ETAPA 2 (não exibe o HELP)**  
1. F4\_TRANFIL estiver configurado como "1".  
2. F4\_TRANCQ estiver configurado como "1".

É importante ressaltar que, ao atender às condições da primeira etapa(ETAPA 1) mencionada, o faturamento do pedido não será efetuado. No entanto, será permitido o pedido de venda, desde que seja considerado como uma nota de transferência nas configurações da TES. Essa abordagem visa proporcionar uma compreensão clara das condições sob as quais a mensagem "HELP ARMZCQ" é gerada e as implicações associadas ao processo de faturamento de pedidos.

Caso queira efetuar o bloqueio mesmo sendo tratado como uma transferencia, existe a possibilidade de efetuar um controle e validação mediante a customizações no fonte.

Para mais detalhes sobre os pontos de entradas disponiveis na rotina (Pedido de venda) consulte o boletim abaixo:

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de Entrada na rotina "Pedidos de Venda (MATA410)"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7381576110871-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-Entrada-na-rotina-Pedidos-de-Venda-MATA410-)

**Saiba mais:**

[Para informações sobre como efetuar a Baixa de C.Q (MATA175) clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011962151-MP-SIGAEST-Como-efetuar-Baixa-do-C-Q-MATA175-)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração do Controle de Qualidade de Materiais no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011947711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-do-Controle-de-Qualidade-de-Materiais-no-Protheus)

*[Clique aqui e veja mais artigos sobre Movimentações em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
