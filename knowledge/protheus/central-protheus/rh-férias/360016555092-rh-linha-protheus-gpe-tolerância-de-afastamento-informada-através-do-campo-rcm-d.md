---
article_id: 360016555092
category: RH - Férias
content_hash: 33e094a568a7c77cad54a6d521c76f90e87c96aa0296a7b4ee04b0e073dbe891
fetched_at: '2026-06-28T22:43:59.246755+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Tolerância de afastamento informada através do
  campo RCM_DIASFE
type: support-article
updated_at: '2025-08-29T11:56:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016555092-RH-Linha-Protheus-GPE-Toler%C3%A2ncia-de-afastamento-informada-atrav%C3%A9s-do-campo-RCM-DIASFE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26667939968663)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como funciona a tolerância de afastamento informada através do campo RCM\_DIASFE?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quando o funcionário entrega um atestado de **X dias de afastamento**, o sistema irá buscar dentro do cadastro de ausência o campo **Dias Afastamento Férias (RCM\_DIASFE),** quantos dias serão toleráveis **até que a contagem para perca dos avos** (informada no campo Tipo Ausência Férias- RCM\_FERIAS) **seja iniciada.**  
  
**Exemplo**Foi definido no campo **Tipo Ausência Férias** que o funcionário perderá o período aquisitivo quando o afastamento **ultrapassar 30 dias**, porém existe uma **tolerância** de **20 dias** através do campo **Dias Afastamento Férias.**  
Caso o funcionário fique afastado por **31 dias dentro do período aquisitivo**, o sistema irá utilizar **primeiramente os 20 dias de tolerância** para que a partir do 21º dia comece a contagem da perca dos avos.   
Então, após a tolerância o funcionário tem **11 dias de afastamento** e como esse restante é menor que 30 dias o período **não é prescrito**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26667894328855)

**Observação:**Caso os dias de afastamos após a tolerância ultrapassar os dias de perda definido no **campo Tipo Ausência Férias**, o status desse período fica "**prescrito**" no Controle de Dias de Direito (GPEA050) e se inicia um **novo período a partir do retorno do afastamento**.  
  
**IMPORTANTE:**Além do campo interferir na perda de avos de férias, também poderá **interferir no cálculo de férias** **em dobro** pois, uma vez que os dias informados no campo não serão utilizados na contagem dos dias de afastamento, também não serão utilizados na contagem de aumento do período concessivo, no caso do parâmetro **MV\_SUSPCON** estiver ativo.  
  
**Exemplo**: Considerando um tipo de ausência padrão na qual o direito as férias é perdido após 180 dias. Se no campo **RCM\_DIASFE** for informado **100 dias**, o funcionário **perderá o direito as férias** apenas se ficar afastado durante **280 dias, pois os 180 primeiros entram na tolerância** e serão ignorados.   
Da mesma forma, esses 180 dias de tolerância não irão contar na suspensão do período concessivo, sendo somados apenas os dias que ultrapassarem a tolerância.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26667939975063)  
Logo, se o período concessivo for de 20/07/2018 até 19/07/2019 e o funcionário estiver afastado por 200 dias, por exemplo, apenas 20 dias serão somados, deixando o final do período concessivo no dia 08/08/2019 .

**Saiba Mais**

[RH - Férias](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597291-RH-F%C3%A9rias)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
