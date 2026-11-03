---
article_id: 12130658501015
category: SIGAEST - CUSTOS
content_hash: 266017459f6dc081df60c27c939641674cda7a6c38c35b5e996e882ef15582c6
fetched_at: '2026-06-28T22:39:02.018860+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA038 - array out
  of bounds ( 2 of 1 )  on FWGETADJSIZE(FWRESADJSIZE.PRW) 13/12/2022 14:23:45 line
  : 24'
type: support-article
updated_at: '2023-02-02T19:43:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12130658501015-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-array-out-of-bounds-2-of-1-on-FWGETADJSIZE-FWRESADJSIZE-PRW-13-12-2022-14-23-45-line-24
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao acessar a nova rotina Acompanha Custos (MATA038) apresenta o error.log abaixo.

***array out of bounds ( 2 of 1 )  on FWGETADJSIZE(FWRESADJSIZE.PRW) 13/12/2022 14:23:45 line : 24***

***[TOTVS build: 7.00.210324P-20221215]***

***Called from FWRESADJSIZE(FWRESADJSIZE.PRW) 13/12/2022 14:23:45 line : 3***

***Called from FWUIWIZARD:CREATESTRUCT(FWUIWIZARD.PRW) 13/12/2022 14:23:45 line : 142***

***Called from FWUIWIZARD:SETOWNER(FWUIWIZARD.PRW) 13/12/2022 14:23:45 line : 112***

***Called from FWWIZARDCONTROL:ACTIVATE(FWWIZARDCONTROL.PRW) 13/12/2022 14:23:45 line : 146***

***Called from MATA038(MATA038.PRW) 16/12/2022 11:52:56 line : 60***

***Called from \_\_EXECUTE(APLIB090.PRW) 13/12/2022 14:23:45 line : 721***

***Called from MDIEXECUTE(APLIB260.PRW) 13/12/2022 14:23:45 line : 924***

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Causa**Esse incidente ocorre apenas em versões do ***Windows Server, ambiente não homologado*** para uso do SmartClient. Ocorre também em outras rotinas, podemos afirmar por exemplo no Cadastro de Produtos  (MATA010).

**Solução**

Repetir o procedimento acessando um ***Sistema Operacional homologado*** pela TOTVS, conforme indicado na documentação do link abaixo:

***<https://tdn.totvs.com/display/tec/SmartClient+-+Sistemas+operacionais>***

***Saiba Mais:***  
*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
