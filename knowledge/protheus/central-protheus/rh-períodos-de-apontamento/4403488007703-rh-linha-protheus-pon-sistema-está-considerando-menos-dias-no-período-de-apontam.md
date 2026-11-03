---
article_id: 4403488007703
category: RH - Períodos de Apontamento
content_hash: 8ccdbc8988ea235e036772b291743c54db42480b3b3ea6901a1b064a5364124f
fetched_at: '2026-06-28T22:44:45.136332+00:00'
product: protheus
section_id: 32419304439959
source: central-protheus
title: RH - Linha Protheus - PON - Sistema está considerando menos dias no Período
  de Apontamento
type: support-article
updated_at: '2025-10-13T17:08:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403488007703-RH-Linha-Protheus-PON-Sistema-est%C3%A1-considerando-menos-dias-no-Per%C3%ADodo-de-Apontamento
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31942072021271) Tempo aproximado para leitura: 00:02:00 min******Dúvida**Após o Fechamento Mensal do período, o sistema está considerando menos dias no novo período aberto.  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O cenário ocorre nos casos onde o Período de Apontamento utilizado é de 01 à 31/30/29/28 do mês e o conteúdo do parâmetro **MV\_PAPONTA** está como **01/30, 01/29 ou 01/28.**  
  
O **MV\_PAPONTA** é utilizado pelo sistema para sinalização de quais datas deverão ser utilizadas no próximo período, independente da quantidade de dias que os meses tenham, portanto, o correto é que o conteúdo do parâmetro esteja **01/31**, indicando que o período utilizado sempre será do primeiro ao último dia do mês cheio, independente de qual seja o mês de atuação.  
  
Para ajustar o conteúdo do parâmetro, acesse **Atualizações > Cadastro do Ponto > Período de Apontamento > Outras Ações > Modificar Período de Apontamento > Dia Inicial/Final >** Preencha como **01/31** e clique em Confirmar **>** Informe o **último dia** do Período de Apontamento que será utilizado, neste exemplo, foi informado o dia 30.06.2021:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19463589052183)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19463563201431)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19463563206167)  
  
  
Após clicar em OK, o período será criado de forma correta. Para consultar, acesse novamente **Outras ações > Modificar Período > Apenas Visualizar:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19463563209239)

**Importante:** Caso seja necessário trabalhar com um período **maior ou menor que 30 dias,** será necessário efetuar a configuração conforme documentação abaixo:  
[RH - Linha Protheus - Como trabalhar com um período de apontamento menor ou maior que 30 dias no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011060231-MP-PON-Como-trabalhar-com-um-per%C3%ADodo-de-apontamento-menor-ou-maior-que-30-dias-no-Ponto-Eletr%C3%B4nico?source=search) **Saiba mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Rotina Período de Apontamento - PONA290](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059188733-RH-Linha-Protheus-PON-Rotina-Per%C3%ADodo-de-Apontamento-PONA290)
