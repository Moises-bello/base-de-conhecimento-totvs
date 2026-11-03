---
article_id: 360050634994
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: eb8bdcbbc50ffd07a116425d1832293a0cb75c50d759348cdcfe909c9358f713
fetched_at: '2026-06-28T22:40:47.457492+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF : Reg 0010 COMO
  GERAR OS REGISTRO'
type: support-article
updated_at: '2026-06-23T17:57:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634994-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Reg-0010-COMO-GERAR-OS-REGISTRO
---

**Dúvida**Como gerar o registro 0010 da ECF ?  
  
**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
**Solução**

Gerar a revisão conforme regime tributário

* [Como gerar o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Real-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
* [ECF – IMUNE OU ISENTA COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search)

Registro    Tabela/CTB     TAFST1/TAFST2  
Reg 0010      CSZ                      T127  
Verifique se o registro foi gerado na tabela da contabilidade

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079025733)

* Através do registro da conta verifique T0127 – Tabela TAFST1 e TAFST2:
  + Posicione o Mouse no "TAFKEY" na Conta que possui amarração
  + Editar > Alterar - Verifique se a conta referencial está sendo apresentada  
      
    Ex: |T127|20160101|20161231|0|0|00000||0||2|2|5|1|01|PPPP||2||||||1|000|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2||2|1|
* Verifique o TAFSTATUS = 3

**[Blocos/Registros](http://tdn.totvs.com/pages/viewpage.action?pageId=192094180)****– geração no TAF ou na integração : [MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077879194)

* Através do [Layout do TAF](https://tdn.totvs.com/pages/releaseview.action?pageId=187534666) veja se os dados foram gerados corretamente

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079026073)

Através da rotina abaixo [TAFA372](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512) verifique se o registro foi gerado

[**Registro 0010 - Parâmetros de Tributação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)

* Tabela - CHD (Parâmetros de abertura ECF)
* Registro do Layout TOTVS - T127
* Rotina - TAFA372 (Cadastro de Parâmetros de Abertura ECF)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079026153)
