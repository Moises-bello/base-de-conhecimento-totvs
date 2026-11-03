---
article_id: 360017779011
category: RH - Folha de Pagamento
content_hash: 995ef128f013da2f1ee9a6baa2fd3074efb2366545ce36fa87290ad932dbd5e8
fetched_at: '2026-06-28T22:44:16.110458+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - O sistema está lançando a dedução de 1/12 avos
  de 13° salário no cálculo da licença maternidade
type: support-article
updated_at: '2024-09-10T18:43:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017779011-RH-Linha-Protheus-GPE-O-sistema-est%C3%A1-lan%C3%A7ando-a-dedu%C3%A7%C3%A3o-de-1-12-avos-de-13-sal%C3%A1rio-no-c%C3%A1lculo-da-licen%C3%A7a-maternidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26277736187415) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**Ao efetuar o cálculo da folha de pagamento (**GPEM020)**o sistema apresenta para funcionária afastada por licença maternidade a verba com identificador de cálculo **0670** - Dedução de 1/12 avos de 13° salário.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Solução**O parâmetro responsável por apresentar a verba de **id 0670** no cálculo da folha ou no cálculo de 13º salário é o **MV\_SALMGRP**.  
Com o parâmetro configurado com **S** a verba é lançada a dedução de 1/12 avos de 13° salário no cálculo da folha de licença maternidade.

A configuração com **S** foi desenvolvida para empresas que ganharam **Liminar na Justiça para tal dedução mensal**, sem a liminar não cabe a empresa optar por essa dedução, visto que por lei sempre será deduzido no próprio cálculo do 13º salário da funcionária.

![TOTVS_Varejo__Microsiga__02.9.0007.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360013076611)  
  
**Resumo do cálculo:**Verba 627= 1.500,00 (verba 131) / 12 = 125,00

Para que tal dedução ocorra apenas no **mês de rescisão e no período da folha 13º Salário**, deverá ser informado **N** para o parâmetro **MV\_SALMGRP -**Acrescenta 1/12 Avos de Dedução Salário Maternidade e na GRPS**.**O correto é levar esta informação sempre no cálculo de 13º salário, portanto, o parâmetro deverá estar desabilitado.  
Caso tenha uma rescisão, a informação será apresentada na mesma.

![TOTVS_Varejo__Microsiga__02.9.0099.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360013076871)  
  
Perceba que a verba 627 - com identificador de cálculo 0670 não é mais apresentada.  
![TOTVS_Varejo__Microsiga__02.9.0007_2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360013069212)  
  
Agora ela passará a ser deduzida no cálculo da rescisão ou na folha de 13º salário.

![TOTVS_Varejo__Microsiga__02.9.0007_3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360013069712)

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
