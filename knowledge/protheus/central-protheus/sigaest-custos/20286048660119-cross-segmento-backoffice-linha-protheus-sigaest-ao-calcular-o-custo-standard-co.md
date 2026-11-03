---
article_id: 20286048660119
category: SIGAEST - CUSTOS
content_hash: 85e62fffa011838a52f351f239d62f557f2fa224e4575ad3f8a9143cc65ac4db
fetched_at: '2026-06-28T22:39:00.587032+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao calcular o Custo
  Standard com mais de uma filial, qual valor deverá ser considerado?
type: support-article
updated_at: '2025-03-12T12:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20286048660119-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-calcular-o-Custo-Standard-com-mais-de-uma-filial-qual-valor-dever%C3%A1-ser-considerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20286074683159) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual valor que será calculado no campo B1\_CUSTD na rotina de Custo de Reposição ao selecionar mais de uma filial?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Observando o seguinte cenário onde tem um produto que foi dado entrada em uma nota fiscal de compra em uma filial no dia 06/12 com um custo de 5 reais e feito uma outra nota fiscal no dia 14/12 em outra filial com custo de 3 reais, qual valor que o sistema irá considerar para calcular o campo B1\_CUSTD ao executar a rotina Custo Standard com data de processamento 20/12?

**O sistema irá fazer o processamento filial por filial** e não é feito o processamento de todas as filiais ao mesmo tempo, mesmo que tenha selecionado as filiais para executar.

Logo o sistema irá considerar o maior valor entre o custo das notas fiscais, sendo nesse caso acima o valor de 5 reais, desconsiderando a entrada que foi feita no dia 14/12.

Uma sugestão é validar o parametro MV\_ARQPROD e colocar no parametro "SBZ" que permitirá o tratamento das informações dos indicadores de produto de forma individual por filial, em vez de compartilhada.

Outra alternativa é a validação dos pontos de entrada da rotina Custo Standard:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA320 - Pontos de Entrada da rotina Custo Standard (Custo de Reposição)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004367962-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA320-Pontos-de-Entrada-da-rotina-Custo-Standard-Custo-de-Reposi%C3%A7%C3%A3o-#:~:text=Este%20ponto%20de%20entrada%20permite,para%20a%20moeda%20do%20PA.)

**Saiba mais:**

[Cross Segmentos - Backoffice (Linha Protheus) - SIGAEST - Conceito de utilização da rotina Custo Standard/Custo de Reposição MATA320 - B1\_CUSTD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013572791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAEST-Conceito-de-utiliza%C3%A7%C3%A3o-da-rotina-Custo-Standard-Custo-de-Reposi%C3%A7%C3%A3o-MATA320-B1-CUSTD)

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013572791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAEST-Conceito-de-utiliza%C3%A7%C3%A3o-da-rotina-Custo-Standard-Custo-de-Reposi%C3%A7%C3%A3o-MATA320-B1-CUSTD)

#
