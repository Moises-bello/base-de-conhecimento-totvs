---
article_id: 360018333372
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: a87fcb199e70576b816a80326c27368054defcd0824fda884474d088364654a3
fetched_at: '2026-06-28T22:40:48.819032+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - LALUR E LACS: LUCRO
  PRESUMIDO REGIME DE CAIXA'
type: support-article
updated_at: '2025-05-14T18:03:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018333372-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-LALUR-E-LACS-LUCRO-PRESUMIDO-REGIME-DE-CAIXA
---

*LALUR E LACS: LUCRO PRESUMIDO REGIME DE CAIXA***Dúvida**Apuração do Lucro Presumido por Regime de caixa, como devemos proceder com os cadastros no TAF?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice - Microsiga Protheus - Todas as versões

**Solução**

**Veja : [Cálculo de CSLL e IRPJ - Empresa Lucro Presumido trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035133373-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-C%C3%A1lculo-de-CSLL-e-IRPJ-Empresa-Lucro-Presumido-trimestral)**1. Cadastro Lalur- CTBS300 (Caso possua os lançamentos no módulo contábil).

Sabemos que atualmente o Regime Caixa não precisa ter contabilidade escriturada.

Caso não tenha os lançamentos na contabilidade gerencial, deverá ser feito os lançamentos direto (Manualmente) no TAF.   [Rotina - TAFA331( Lançamento contabeis)](https://tdn.totvs.com/pages/releaseview.action?pageId=269067209) e [Rotina TAFA311](https://tdn.totvs.com/pages/viewpage.action?pageId=497457208) (Saldos contábeis Bloco [K155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055863753-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-K155-COMO-GERAR?source=search), [K156](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-K156-COMO-GERAR?source=search), [K355](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033656274-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-K355-COMO-GERAR?source=search)).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013944592)

* Será necessário incluir os lançamento manualmente no TAF , pois ao informar o parâmetro [TIP\_ESP\_PRE = L](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007125451-MP-SIGACTB-ECF-Bloco-Q?source=search) o sistema não integra para o TAF os bloco K e P .

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16830651587863)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16830606796823)

* Necessário verificar no no manual da receita o conceito e conseguencias ao preencher a perguntas abaixo, ao gerar a ECF

IND\_REC\_RECEITA

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32103346777367)

2. Cadastro de tributo- TAFA430

Os campos: Alíquota Presunção 1/ Alíquota Presunção 2/ Alíquota Presunção 3

São destinados a Lucro Presumido, deve ser informado alíquota referente cada tipo de receita.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16830608044055)

Os passos a seguir devem ser conforme os de mais regimes tributários, conforme documentação:

[MP\_SIGACTB LALUR/LACS: CADASTRO, APURAÇÃO E INTEGRAÇÃO COM ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018585831-MP-SIGACTB-LALUR-LACS-CADASTRO-APURA%C3%87%C3%83O-E-INTEGRA%C3%87%C3%83O-COM-ECF)

Veja mais :

[MP - Cálculo de CSLL e IRPJ - Empresa Lucro Presumido - Trimestral - SIGACTB X SIGATAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035133373-MP-C%C3%A1lculo-de-CSLL-e-IRPJ-Empresa-Lucro-Presumido-Trimestral-SIGACTB-X-SIGATAF?source=search)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - ERRO PVA -TIP\_ESC\_PRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006982951-MP-SIGACTB-ECF-ERRO-PVA-TIP-ESC-PRE?source=search)

[MP-SIGACTB - ECF Simulação Apuração IRPJ CSLL no TAF (TAFA433)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035319633-MP-SIGACTB-ECF-Simula%C3%A7%C3%A3o-Apura%C3%A7%C3%A3o-IRPJ-CSLL-no-TAF-TAFA433-?source=search)

[MP - SIGACTB - COMO CONFIGURAR O LUCRO PRESUMIDO NO TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010318251-MP-SIGACTB-COMO-CONFIGURAR-O-LUCRO-PRESUMIDO-NO-TAF-?source=search)

[MP-SIGACTB - ECF LALUR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006910571-MP-SIGACTB-ECF-LALUR-?source=search)
