---
content_hash: f57fc4568471c3defdb3061c6cfecc837a563104abe8b1842972cab02203b564
fetched_at: '2026-06-29T00:12:15.251103+00:00'
page_id: '974806567'
product: rm
source: tdn-rm
title: eSocial - Salário Maternidade Vinculado à Lei nº 15.156/2025
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=974806567
version: 38
---

---

Este documento tem como objetivo esclarecer que o produto **TOTVS Folha de Pagamento RM** esta em conformidade com nova **FAQ** (pergunta frequente) de código **10.45**, publicada no portal do eSocial em **17/07/2025.** A referida FAQ trata dos códigos de incidência tributária e trabalhista que devem ser utilizadas nas rubricas relativas ao salário-maternidade vinculado à [Lei nº 15.156/2025](https://www.totvs.com/blog/uncategorized/licenca-maternidade-e-paternidade-ampliadas-pela-lei-no-15-156-2025-entenda-o-que-muda/). Essa lei garante licença-maternidade diferenciada nos casos de nascimento ou adoção de crianças com deficiência permanente associada ao vírus Zika. 

---

**Incidências nos eventos do eSocial**

O afastamento deve ser informado no evento S-2230 com o motivo 43, específico para essa situação. A depender de quem realiza o pagamento do benefício – empresa ou INSS –, devem ser aplicados códigos distintos para a contribuição previdenciária, Imposto de Renda e FGTS, conforme a seguir:

1true1Salário Maternidade EMPRESASalário Maternidade EMPRESA

Quando o salário-maternidade é pago pela empresa as incidência deverá ser conforme abaixo:

* INSS ({codIncCP}): 21 – Salário maternidade mensal pago pelo Empregador
* IRRF ({codIncIRRF}): 11 – Remuneração mensal
* FGTS ({codIncFGTS}): 11 – Remuneração mensal

Salário Maternidade EMPRESAtrue2-1ParametrizaçãoParametrização

No menu Cadastros | Eventos

Deverá cadastrar eventos com o código de cálculo  ou código de cálculo

2-2Salário Maternidade MensalSalário Maternidade Mensal

1) No menu Cadastros | Eventos, deverá existir evento com código de cálculo 17:

2) Gerar XML do evento S-1200:

2-3Salário Maternidade 13o. SalárioSalário Maternidade 13o. Salário

1) No menu Cadastros | Eventos, deverá existir evento com código de cálculo 371:

2) Gerar XML do evento S-1200:

2Salário Maternidade INSSSalário Maternidade INSS

Quando o salário maternidade é pago diretamente pelo INSS os códigos deverão ser:

* INSS ({codIncCP}): 25 – Salário maternidade mensal pago pelo INSS
* IRRF ({codIncIRRF}): 9 – Verba transitada pela folha de pagamento de natureza diversa de rendimento ou retenção/isenção/dedução de IR
* FGTS ({codIncFGTS}): 11 – Remuneração mensal

Integraçãotrue2-1ParametrizaçãoParametrização

No menu Configurações | Parametrizador | Folha Normal | Salário Maternidade 1/2, deverá esta parametrizado os eventos de base de cálculo:

2-2Salário Maternidade MensalSalário Maternidade Mensal

1) No meu Cadastros | Eventos:

2) Gerar XML do evento S-1200:

2-3Salário Maternidade MédiaSalário Maternidade Média

1) No meu Cadastros | Eventos:

2) Na geração do XML do evento S-1200:

3-6Salário Maternidade 13o. SalárioSalário Maternidade 13o. Salário

1) No meu Cadastros | Eventos:

2) Gerar XML do evento S-1200:

3-6Salario Maternidade 13o. RescisãoSalario Maternidade 13o. Rescisão

1) No meu Cadastros | Eventos:

2) Na geração do XML do evento S-1200:

---

**OUTROS LINKS**

[eSocial – publica FAQ sobre incidência de encargos no salário-maternidade referente à Lei 15.156/2025](https://www.totvs.com/blog/fiscal-clientes/esocial-publica-faq-sobre-incidencia-de-encargos-no-salario-maternidade-referente-a-lei-15-156-2025/)
