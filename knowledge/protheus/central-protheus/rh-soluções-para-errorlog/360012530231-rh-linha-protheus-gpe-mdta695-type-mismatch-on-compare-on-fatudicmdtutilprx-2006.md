---
article_id: 360012530231
category: RH - Soluções para error.log
content_hash: 46d4ce581ab88b5962ecf93ef2f0da439d26c5a8a9487f4f24893ff9f469fdd6
fetched_at: '2026-06-28T22:44:09.121982+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - MDTA695 - type mismatch on compare on FATUDIC(MDTUTIL.PRX)
  20/06/2018 10:53:01 line : 1887'
type: support-article
updated_at: '2021-08-16T19:55:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012530231-RH-Linha-Protheus-GPE-MDTA695-type-mismatch-on-compare-on-FATUDIC-MDTUTIL-PRX-20-06-2018-10-53-01-line-1887
---

**Ocorrência***Type mismatch on compare on* FATUDIC(MDTUTIL.PRX) 20/06/2018 10:53:01 *line* : 1887  
  
**Causa**THREAD ERROR  
type mismatch on compare on FATUDIC(MDTUTIL.PRX) 20/06/2018 10:53:01 line : 1887  
[TOTVS build: 7.00.131227A-20180425 NG]  
Called from FATUDIC(MDTUTIL.PRX) 20/06/2018 10:53:01 line : 1887  
Called from MDTLOAD(MDTUTIL.PRX) 20/06/2018 10:53:01 line : 824  
Called from \_\_EXECUTE(APLIB090.PRW) 13/07/2018 17:01:01 line : 603  
Called from {|| \_\_Execute('MDTLoad()','xxxxxxxxxx','Medicina e Segurança do Trabalho',' 35',,,.T.)}(APLIB090.PRW) 13/07/2018 17:01:01 line : 603  
Called from ONLOADEXECUTE(APLIB090.PRW) 13/07/2018 17:01:01 line : 3505  
Called from FWSETENVIRONMENT(FWAPP.PRW) 13/07/2018 17:01:04 line : 2032  
Called from APPSETENVCHILD(FWAPP.PRW) 13/07/2018 17:01:04 line : 2131  
Called from MDIEXECUTE(APLIB260.PRW) 13/07/2018 17:01:01 line : 765  
Called from STATICCALL(APLIB260.PRW) 13/07/2018 17:01:01 line : 765  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Verifique o conteúdo do parâmetro **MV\_NG2AUSE** e se o mesmo está com o tipo numérico, conforme imagem abaixo:  
![](https://totvssuporte.zendesk.com/attachments/token/OZ1NtUESjsSfXqtAXgtrZIgh6/?name=inline-1155431767.png)  
![](https://totvssuporte.zendesk.com/attachments/token/hYBpclGWcoEvF8TV7HSKdU58L/?name=inline1395746199.png)  
  
**Saiba Mais**Para adquirir mais informações acesse: [MP - ERRORLOG - MDTA695 - type mismatch on compare on FATUDIC(MDTUTIL.PRX) 20/06/2018 10:53:01 line : 1887](http://tdn.totvs.com/pages/viewpage.action?pageId=388236801)
