---
article_id: 360004583891
category: eSocial - Tabelas/Não Periódicos
content_hash: e4b7179d5862a97c65f46866d85c0b7a76cdc1f69defac7b792d0ba41165395d
fetched_at: '2026-06-28T22:47:10.498672+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Quantidade de dias anterior ao período do gozo de
  férias para envio do S-2230
type: support-article
updated_at: '2024-07-30T20:39:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004583891-RH-RM-FOP-eSocial-Quantidade-de-dias-anterior-ao-per%C3%ADodo-do-gozo-de-f%C3%A9rias-para-envio-do-S-2230
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24441897619479) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Qual a função do novo campo **Quantidade de dias anterior ao período do gozo de férias para envio do S-2230 (Máx. 60 dias**) e como utilizá-lo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial  - Todas as versões  
  
**Solução**O campo **Quantidade de dias anterior ao período de gozo de férias para envio do S-2230 (Máx. 60 dias),**localizado no menu **Configurações | Parametrizador | eSocial | Configurações Gerais 4/7**, foi criado com o intuito de que as empresas que trabalham com o planejamento de férias anual possam reduzir seu número de retificações, pois ao planejar as férias para todo um ano, integrar com o TAF e enviar ao governo, existe a possibilidade de que alterações no cadastro das férias sejam efetuados, e com isto se faz necessário retificar estas férias. Além disso, o próprio eSocial limita o envio de afastamento futuros, restringindo o envio de afastamento pelo motivo de férias com data de início não superior à 60 dias do envio do evento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25287894690327)

Com o uso deste parâmetro, as férias serão barradas para integração com TAF de acordo com o número de dias preenchido pelo usuário. Desta forma, o usuário poderá alinhar em seu processo, um determinado número de dias máximo anterior à data de final de gozo de férias para modificações nos cadastros de férias, estabelecendo assim maior integridade de seus dados e um menor retrabalho.  
  
Ao tentar efetuar a integração de um evento S-2230 relacionado a férias, o sistema irá subtrair a data atual da data final do afastamento. Se esta operação ultrapassar a quantidade de dias informada no parâmetro o sistema não irá enviar o evento e irá retornar um aviso no log do processo.

Exemplo:Ao cadastrar férias que terminam dia 30/05/2019 para um determinado funcionário e parametrizar o campo em questão com o número de 10 dias, só será possível integrar as férias a partir do dia 20/05/2019 (30/05/2019 - 10 dias = 20/05/2019).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028717831)

**Importante**Caso este campo seja preenchido com o valor 0, o sistema não realizará nenhuma validação e por consequência irá integrar os eventos de férias em qualquer data, independente do cadastro de férias.  
Ao integrar com o TAF ou Governo o registro S-2230 onde a coluna Afastamento de Férias =SIM o sistema irá preencher a coluna Fora do prazo de envio conforme parametrização feita no parâmetro **“Quantidade de dias anterior ao período de gozo de férias para envio do S-2230 (Máx. 60 dias)"**

**Saiba mais**  
Para mais informações acesse:  
[S-2230 - Como utilizar o parâmetro "Quantidade de dias anterior ao período do gozo de férias para envio do S-2230"?](https://tdn.totvs.com/pages/releaseview.action?pageId=403735177)
