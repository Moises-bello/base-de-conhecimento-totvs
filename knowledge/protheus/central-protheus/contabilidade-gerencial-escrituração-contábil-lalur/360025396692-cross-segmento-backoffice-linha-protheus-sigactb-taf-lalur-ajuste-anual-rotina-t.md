---
article_id: 360025396692
category: Contabilidade Gerencial - Escrituração-Contábil-Lalur
content_hash: a55d4591febf4de44cbfe0d1272608c01b7f425290e6dee12dc569c47c3e9f50
fetched_at: '2026-06-28T22:40:40.304912+00:00'
product: protheus
section_id: 1500001548842
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB-TAF LALUR AJUSTE ANUAL
  ROTINA TAFA444  NÃO EXISTE UMA VIGÊNCIA CADASTRADA ABRANGENDO ESTE PERIODO
type: support-article
updated_at: '2024-06-05T14:54:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025396692-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-TAF-LALUR-AJUSTE-ANUAL-ROTINA-TAFA444-N%C3%83O-EXISTE-UMA-VIG%C3%8ANCIA-CADASTRADA-ABRANGENDO-ESTE-PERIODO
---

**Dúvida**Ao realizar a apuração de ajuste anual é gerado a mensagem: "Não existe uma vigência cadastrada abrangendo este período"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024410091/mceclip0.png)

* Realize algum testes na rotina seguindo o conceito de apuração anual com recolhimento mensal, onde os períodos devem estar cadastrados da seguinte forma:
* [TAF433(evento tributário)](https://tdn.totvs.com/pages/releaseview.action?pageId=248578386) será necessário efetuar :   
  -12 períodos mensais de janeiro a dezembro -13º de jan a dez
* [TAFA444 :](https://tdn.totvs.com/display/public/TAF/Cadastro+de+Eventos+Especiais+-+TAFA443+-+TAF+-+P12) Apuração com recolhimento mensal será uma para cada período   
  -12 períodos mensais de janeiro a dezembro - “Campo Per.Anual – não flegado” -13º de jan a dez “Campo Per.Anual - flegado”
* [TAFA438 – amarra](https://tdn.totvs.com/pages/releaseview.action?pageId=245170511) vigência Cadastrar 13 sendo 12 mensal e 1 anual ambos os tributos, amarrando cada um ao evento tributário respectivo

Caso o erro persista, verifique também:

* Verifique se as tabelas abaixo possuem o mesmo compartilhamento: T0J, CWV, T50, T0N, T0O, T0R, LEC, CHC, CH6, T0P, LED, C1G, T5L ,LEL,T0S, LE9, T0T, T0U, CEN, CEO, CEP, CEQ, CES, CER, CET, CEU, CEV, CFR
* Essas tabelas são utilizadas no processo do IR pelas rotinas e devem possui o mesmo compartilhamento, caso tenha alguma diferença realize o ajuste conforme a sua necessidade e tente novamente.

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
  
**Solução**

Na Apuração Anual de Ajuste (01/01/20XX ate 31/12/20XX) a rotina TAFA438 (Vigência do evento tributário) deve estar relacionada a um cadastro de Evento tributário (TAFA444) com o campo "código tributo" igual a 00001 (Lucro Real)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024454392/mceclip2.png)

Saiba mais:

[MP\_SIGACTB LALUR E LACS: LUCRO PRESUMIDO REGIME DE CAIXA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018333372-MP-SIGACTB-LALUR-E-LACS-LUCRO-PRESUMIDO-REGIME-DE-CAIXA-?source=search)

[MP - SIGACTB - ECF – Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)

[MP-SIGACTB - ECF Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)

[MP\_SIGACTB LALUR/LACS: CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF?source=search)

[MP-SIGACTB - ECF LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)

[MP\_SIGACTB - CTBS300 ONDE CADASTRAR FILTRO LALUR?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015738232-MP-SIGACTB-CTBS300-ONDE-CADASTRAR-FILTRO-LALUR-?source=search)

[MP - SIGACTB - ECF - Bloco M - Apuração IRPJ/CSLL para Lucro Real (TAFA322)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004874591-MP-SIGACTB-ECF-Bloco-M-Apura%C3%A7%C3%A3o-IRPJ-CSLL-para-Lucro-Real-TAFA322-?source=search)

[MP - SIGACTB - ECF - Geração do BLOCO M no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008506768-MP-SIGACTB-ECF-Gera%C3%A7%C3%A3o-do-BLOCO-M-no-TAF?source=search)

[MP-SIGACTB - ECF Tabelas Relacionadas a Apuração IRPJ CSLL no TAF (Lalur)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034815894-MP-SIGACTB-ECF-Tabelas-Relacionadas-a-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-Lalur-?source=search)
