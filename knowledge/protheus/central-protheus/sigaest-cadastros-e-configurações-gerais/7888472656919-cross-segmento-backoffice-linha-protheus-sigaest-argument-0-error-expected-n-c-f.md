---
article_id: 7888472656919
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 2575357af7234b8e24597a0f41bd6290533255b26c7d98f8d5fe6a5871eb5b9a
fetched_at: '2026-06-28T22:39:08.033787+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - argument #0 error,
  expected N->C,  function str on ESTPGONL(ESTPGONL.PRW)'
type: support-article
updated_at: '2022-08-02T14:29:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7888472656919-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-argument-0-error-expected-N-C-function-str-on-ESTPGONL-ESTPGONL-PRW
---

**Ocorrência**Ao alterar o cadastro de usuários pelo módulo configurador exibe o error.log.

***argument #0 error, expected N->C, function str on ESTPGONL(ESTPGONL.PRW) 09/11/2020 15:05:04 line : 67***

*[TOTVS build: 7.00.210324P-20220312]*  
*Called from {|| ESTPGOnl(oPGOnline) }(CFGPGONLINE.PRW) 08/06/2022 16:53:22 line : 139*  
*Called from LOADPGONL(CFGPGONLINE.PRW) 08/06/2022 16:53:22 line : 139*  
*Called from PGLONLINE(CFGA510.PRX) 08/06/2022 16:53:24 line : 1298*  
*Called from {|OOWNER| PGLONLINE(OOWNER,OVIEW,@APGONLINE)}(CFGA510.PRX) 08/06/2022 16:53:24 line : 520*  
*Called from FWOTHEROBJECTVIEW:ACTIVATE(FWOTHEROBJECTVIEW.PRW) 08/06/2022 16:53:24 line : 59*  
*Called from FWFORMVIEW:ACTIVATE(FWFORMVIEW.PRW) 08/06/2022 16:53:24 line : 1597*  
*Called from FWMVCWINDOW:SHOW(FWMVCWINDOW.PRW) 08/06/2022 16:53:24 line : 179*  
*Called from FWMVCWINDOW:ACTIVATE(FWMVCWINDOW.PRW) 08/06/2022 16:53:24 line : 215*  
*Called from FWVIEWEXEC:OPENVIEW(FWVIEWEXEC.PRW) 08/06/2022 16:53:24 line : 488*  
*Called from CFA510DBM(CFGA510DB.PRW) 08/06/2022 16:53:24 line : 322*  
*Called from FWFORMBROWSE:EXECUTE(FWFORMBROWSE.PRW) 08/06/2022 16:53:24 line : 1147*  
*Called from {|| OSELF:EXECUTE("CFA510DBM", 4, 0,"ALTERAR", 0,"","","", 0) }(FWFORMBROWSE.PRW) 08/06/2022 16:53:24 line : 579*  
*Called from ::MSDIALOG:ACTIVATE*  
*Called from CFGA510DB(CFGA510DB.PRW) 08/06/2022 16:53:24 line : 141*  
*Called from CFGA510(CFGA510.PRX) 08/06/2022 16:53:24 line : 89*  
*Called from \_\_EXECUTE(APLIB090.PRW) 08/06/2022 16:53:22 line : 721*  
*Called from FWPREEXECUTE(FWPREEXECUTE.PRW) 08/06/2022 16:53:24 line : 86*  
*Called from {|| FWPreExecute('Usuários', 'CFGA510()', 1, '99', 'xxxxxxxxxx') }(FWUIMENUL.PRW) 08/06/2022 16:53:24 line : 197*  
*Called from ::TWINDOW:ACTIVATE*  
*Called from MSAPP:ACTIVATE(FWAPP.PRW) 08/06/2022 16:53:24 line : 755*  
*Called from SIGACFG(APLIB000.PRW) 08/06/2022 16:53:22 line : 1010*

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Estoque Custos - à partir do release P12.33  
  
**Causa**Esse incidente ocorre no momento que esta efetuando a alteração do cadastro  
  
**Solução**Para solucionar essa ocorrência, abaixo pacote com atualização:

12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1066605> ;

Para acessar a documentação da solicitação acesse o link: <https://tdn.totvs.com/pages/viewpage.action?pageId=682436324>

Saiba Mais:  
[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001533821-Estoque-e-Custos-SIGAEST-)
