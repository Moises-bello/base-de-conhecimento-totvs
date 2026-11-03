---
article_id: 360039002034
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: 2f82c503cbde2cd1eec87cba6b941dbf0dfd2768ca9fb2a01af3283c929435e7
fetched_at: '2026-06-28T22:39:52.200276+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Error log na amarração
  produto x fornecedor
type: support-article
updated_at: '2021-10-29T12:07:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039002034-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Error-log-na-amarra%C3%A7%C3%A3o-produto-x-fornecedor
---

**Dúvida**Como corrigir o error log:   
**variable is not an object on FWFLDGET**(PROTHEUSFUNCTIONMVC.PRX) 15/02/2019 09:11:02 line : 4499

[TOTVS build: 7.00.170117A-20190212]  
Called from A060VFLOJA(**MATA060**.PRX) 04/09/2018 15:31:48 line : 1576  
Called from {|x,lResValid,o| o := Self:aEntryCtrls[7],(lResValid := If(o:lModified .or. (o:Cargo <> NIL .and. o:Cargo <> M->A5\_FALOJA),(A060VFLoja() ),.T.)),(If(Type('lRefresh') == 'L' .and. lRefresh,Self:EnchRefreshAll(),)),lResValid}(MSMGETPR.PRW) 15/02/2019 09:10:59 line : 1586  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – Easy Import Control – A partir da versão 12.1.017.  
  
**Solução**Através do configurador, altere a chamada no menu de MATA060 para o MATA061, rotina atual.  
  
**Saiba mais**  
[MATA060: Amarração Produto X Fornecedor](http://tdn.totvs.com/pages/releaseview.action?pageId=372558651)
