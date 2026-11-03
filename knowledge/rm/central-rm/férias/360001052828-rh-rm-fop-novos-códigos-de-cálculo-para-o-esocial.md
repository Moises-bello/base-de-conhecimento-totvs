---
article_id: 360001052828
category: Férias
content_hash: 68dfb39ae7d8d4516c5bb37b4748c10ef2d0410e8c5ac2f0251076bb93dd4b67
fetched_at: '2026-06-28T22:46:56.519486+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Novos códigos de cálculo para o eSocial
type: support-article
updated_at: '2025-02-27T18:24:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001052828-RH-RM-FOP-Novos-c%C3%B3digos-de-c%C3%A1lculo-para-o-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:09:30 min  
  
Dúvida**Devido a necessidade de adaptação de algumas verbas rescisórias às novas regras do eSocial, quais serão os novos códigos de cálculo que deverão ser utilizados no processo de rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Os novos códigos de cálculo foram divididos em três partes: **férias vencidas e proporcionais**; **férias em dobro**; e **13º salário e licença maternidade**. Veja abaixo os comentários sobre cada um destes códigos de cálculo:

* **Férias Vencidas X Férias****Proporcionais**No processo de rescisão temos os códigos de cálculo 24 e 25, que representam os valores de férias dos períodos vencido e proporcional, respectivamente. Porém, no caso do adicional de 1/3 de férias é lançado um evento único, de código de cálculo 63, com o valor total de todos os períodos aquisitivos.  
    
  O eSocial possui rubricas distintas para os valores do período proporcional e do período vencido de férias. Por esse motivo, houve a necessidade de separar o valor do adicional de 1/3 para ser lançado em eventos diferentes com os valores de férias vencidas e proporcionais.  
    
  Os novos códigos de cálculo para o adicional de 1/3 de férias na rescisão, serão:  
    
  **367 - ADICIONAL 1/3 FÉRIAS VENCIDAS RESCISÃO****368 - DIFERENÇA 1/3 FÉRIAS VENCIDAS RESCISÃO****369 - ADICIONAL 1/3 FÉRIAS PROPORCIONAIS RESCISÃO****370 - DIFERENÇA 1/3 FÉRIAS PROPORCIONAIS RESCISÃO**Após atualização do patch será necessária a criação de novos eventos com os códigos de cálculo acima. Estes eventos deverão ser criados com as mesmas parametrizações dos eventos com os códigos de cálculo 63 (adicional de 1/3 de férias rescisão) e 95 (diferença de 1/3 de férias na rescisão).  
    
  Os eventos com código de cálculo 367 e 369 serão lançados no processo de Rescisão e os eventos com códigos 368 e 370 serão lançados no processo da Rescisão Complementar.  
    
  Observação:  
    
  No Parametrizador, pasta **Rescisão | Férias**, caso o parâmetro **"Separar médias de férias vencidas e proporcionais na rescisão"** esteja desmarcado, não será possível separar o valor do adicional de 1/3. Neste caso, o processo de rescisão continuará a lançar o antigo evento de código de cálculo 63 (adicional de 1/3 de férias rescisão). Ou seja, para separar o valor do 1/3, será necessário separar também os valores de média.  
    
  Portanto, para atender as novas regras estabelecidas pelo eSocial, aconselhamos a marcar o parâmetro na pasta **Rescisão | Férias** do Parametrizador.

* **Férias em dobro**Quando ocorre o término do período aquisitivo de férias sem o devido pagamento, o funcionário passa a ter direito ao dobro de férias. Nesse caso são utilizados os eventos com códigos de cálculo 309 (férias em dobro) e 310 (adicional 1/3 de férias em dobro). Esses eventos são lançados tanto no Recibo de Férias, no cálculo de férias normais, quanto no cálculo de rescisão.  
    
  Entretanto, no eSocial existem rubricas distintas para os valores de férias em dobro pagos nas férias normais e para os pagos na rescisão. Para essa separação foram criados os novos códigos de cálculo abaixo:  
    
  **365 - FÉRIAS EM DOBRO RESCISÃO****366 - ADICIONAL 1/3 FÉRIAS EM DOBRO RESCISÃO**Após a atualização do patch, será necessária a criação de novos eventos com os códigos de cálculo acima, com a mesma parametrização dos eventos com os códigos de cálculo 309 (férias em dobro) e 310 (adicional 1/3 de férias em dobro).  
    
  Os antigos códigos 309 e 310 passarão a ser lançados somente no cálculo de férias normais. E os novos códigos 365 e 366 serão utilizados para os lançamentos no processo de rescisão.
* **13º salário X Licença Maternidade**Quando ocorre afastamento por Licença Maternidade durante o ano é lançado o evento de código de cálculo 48 (13º salário rescisão), no processo da rescisão, com valor total de 13º salário, incluindo o valor referente ao período da licença, que será deduzido na Guia de INSS.  
    
  Na rescisão também é lançado um evento do tipo base de cálculo com o código de cálculo 324 (13º salário rescisão licença maternidade), que tem por finalidade apenas demonstrar o valor a ser deduzido na guia.  
    
  Entretanto, o eSocial exige que sejam informados os proventos separados de 13º salário pago pela Empresa na rescisão e o 13º salário referente ao Salário Maternidade.  
    
  Isto também acontece com o pagamento da segunda parcela do 13º salário, quando paga em dezembro, no evento de código de cálculo 102 (segunda parcela 13º salário) e no evento do tipo base de cálculo com código de cálculo 322 (segunda parcela 13º salário licença maternidade).  
    
  Sendo assim, foram criados os códigos de cálculo abaixo:  
    
  **371 - SEGUNDA PARCELA 13º LICENÇA MATERNIDADE PROVENTO****372 - DIFERENÇA 13º SALÁRIO LICENÇA MATERNIDADE PROVENTO****373 - 13º RESCISÃO LICENÇA MATERNIDADE PROVENTO****374 - DIFERENÇA 13º RESCISÃO LIC. MATERNIDADE PROVENTO**Após a atualização do patch será necessária a criação de novos eventos com os códigos de cálculo acima, com a mesma parametrização dos eventos com os códigos de cálculo 322, 323, 324 e 325, respectivamente.  
    
  Os novos códigos de cálculo irão substituir os eventos do tipo base lançados na rescisão e na segunda parcela de 13º salário, com códigos de cálculo 322 e 324. E também os lançados na Rescisão Complementar e Diferença de 13º, com códigos de cálculo 323 e 325.  
    
  Como os novos eventos para o 13º referente à licença maternidade serão proventos, os seus respectivos valores serão abatidos nos valores dos eventos de 13º salário a ser pago pela Empresa, com códigos de cálculo 48 (13º salário rescisão) e 102 (segunda parcela 13º salário).  
    
  Observação:  
    
  Os códigos de cálculo 371 e 372 só serão utilizados no processo da segunda parcela a ser calculada em dezembro. Os devidos tratamentos no cálculo estão em desenvolvimento no sistema e serão disponibilizados em patchs ainda a serem definidos.

**Saiba mais**Para mais informações sobre cada código de cálculo, veja abaixo:  
  
[365 - Férias em Dobro Rescisão](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.FeriasDobroRescisao.aspx)[366 - Adicional 1/3 de Férias em Dobro Rescisão](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.AdicionalUmTercoFeriasDobroRescisao.aspx)[367 - Adicional 1/3 Férias Vencidas Rescisão](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.AdicionalUmTercoFeriasVencidasRescisao.aspx)[368 - Diferença 1/3 de Férias Vencidas Rescisão](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.DiferencaUmTercoFeriasVencidasRescisao.aspx)[369 - Adicional 1/3 Férias Proporcionais Rescisão](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.AdicionalUmTercoFeriasProporcionaisRescisao.aspx)[370 - Diferença 1/3 de Férias Proporcionais Rescisão](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.DiferencaUmTercoFeriasProporcionaisRescisao.aspx)[371 - Segunda Parcela 13º Licença Maternidade Provento](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.SegundaParcela13LicencaMaternidadeProvento.aspx)[372 - Diferença 13º Salário Licença Maternidade Provento](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.Diferenca13SalarioLicencaMaternidadeProvento.aspx)[373 - 13º Rescisão Licença Maternidade Provento](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.RescisaoLicencaMaternidadeProvento.aspx)  
[374 - Diferença 13º Rescisão Lic. Maternidade Provento  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009475912/mceclip1.png)](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.DiferencaRescisaoLicencaMaternidadeProvento.aspx)
