---
article_id: 360016512051
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: b795b2e04ee6205badc0e80e221b581769611347ae741f67f932183ad1e6d3e7
fetched_at: '2026-06-28T22:40:48.824724+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Reg 0020  ECF - Erro
  apresentado no validador IND_ALIQ_CSLL
type: support-article
updated_at: '2022-07-28T18:34:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016512051-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Reg-0020-ECF-Erro-apresentado-no-validador-IND-ALIQ-CSLL
---

**Dúvida**

Erro ao validar arquivo ECF no Validador da Receita

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012421471/mceclip0.png)  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 1  
  
**Solução**

Gerar a revisão conforme regime tributário

* [Como gerar o Regime tributário Lucro Real /Apuração anual?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004875431-MP-SIGACTB-ECF-Como-gerar-o-Regime-tribut%C3%A1rio-Lucro-Real-Apura%C3%A7%C3%A3o-anual-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Real com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006950711-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Real-com-Apura%C3%A7%C3%A3o-trimestral-?source=search)
* [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
* [ECF – IMUNE OU ISENTA COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search)

Solicito que realize a analise   
  
Registro    Tabela/CTB     TAFST1/TAFST2  
Reg **0020**     CSZ                      T127

Verifique se o registro foi gerado na tabela da contabilidade

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012415912/mceclip4.png)

Verifique se na tabela CSZ “IND\_ALIQ\_CSLL” foi alimentado corretamente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012415932/mceclip5.png)

**[Blocos/Registros](http://tdn.totvs.com/pages/viewpage.action?pageId=192094180)****– geração no TAF ou na integração : [MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)**

- Através registro verifique T0127 – Tabela TAFST1  
\*posicione o Mouse no "TAFKEY" na Conta que possui amarração   
\* Editar > Alterar - Verifique se a conta referencial está sendo apresentada   
Ex:

|T127|20170101|20171231|0|0|00000||0||2|2|5|1|00|PPPP||2||||||**1**|000|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2||0|2|

- Verifique o TAFSTATUS = 3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012423131/mceclip6.png)

* [Layout do TAF](https://tdn.totvs.com/pages/releaseview.action?pageId=187534666)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012423171/mceclip7.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012423211/mceclip8.png)

-Verifique  Também se a tabela TAFST2 foi alimentada:

- no registro da conta verifique T0127

  \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração

     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada

   Ex: |T127|20160101|20161231|0|0|00000||0||2|2|5|1|01|PPPP||2||||||1|000|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2|2||2|1|

- Verifique o TAFSTATUS = 3

Através da rotina abaixo TAFA372 verifique se o registro foi gerado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012416052/mceclip9.png)

**Registro 0020 - Parâmetros Complementares**

* Tabela - CHD (Parâmetros de abertura ECF)
* Registro do Layout TOTVS - T127
* Rotina - TAFA372 (Cadastro de Parâmetros de Abertura ECF)

Verifique se na rotina do TAF o campo Existe e foi alimentado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012416072/mceclip10.png)
