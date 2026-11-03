---
article_id: 360019761431
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: b762b80135b5007a2eb3175d85b94012f8890906ae93492bcb013a6bdeb68b6f
fetched_at: '2026-06-28T22:41:43.257371+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA050 - Não processa
  o calculo de depreciação mensal
type: support-article
updated_at: '2025-04-10T16:52:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019761431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA050-N%C3%A3o-processa-o-calculo-de-deprecia%C3%A7%C3%A3o-mensal
---

**Dúvida**Rotina ATFA050 não gera movimentos no calculo de depreciação mensal?  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Ativo Fixo – A partir da versão 12.  
  
  
**Solução**Além do Valor original (N3\_VORIG1) e da taxa de depreciação (N3\_TXDEPR1) é necessário o preenchimento das contas contábeis no cadastro do ativo (ATFA012):

* Necessário cadastro da [MOEDAS que serão depreciadas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021847812-MP-MATA090-MOEDAS-Valor-padr%C3%A3o-ao-iniciar-o-sistema?source=search)
* Informar o valor original da Moeda 1 (N3\_VORIG1)
* o sistema engatilhará para as outras moedas os valores baseando-se na regra de conversão do dia. Mas se a taxa do dia estiver zerado para as outras moedas, os campos N3\_VORIG2, N3\_VORIG3, N3\_VORIG4 e N3\_VORIG5 não receberão valor. ([Gatilhos para valor original do bem em outras moedas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018851491-MP-SIGAATF-ATFA012-Gatilhos-para-valor-original-do-bem-em-outras-moedas?source=search))
* Configuração [dos parâmetros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007812091-MP-SIGAATF-ATFA050-Deprecia%C3%A7%C3%A3o-de-Ativo?source=search)
* Imobilização: N3\_CCONTAB
* Despesa: N3\_CDEPREC
* Depreciação acumulada: N3\_CCDEPR
* Taxa de depreciação  : N3\_TXDEPR1, N3\_TXDEPR2, N3\_TXDEPR3, N3\_TXDEPR4 (Informar a taxa para a moeda que será depreciada)

Essa validação é importante para mantermos o histórico e integridade nos relatórios do ativo fixo. Mantendo assim o relacionamento entre movimentos/saldos e contas contábeis.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360015369911)

**Importante**

[N1\_PATRIM](https://tdn.totvs.com/pages/releaseview.action?pageId=555852609)  
    \* "N" -> Ativo Imobilizado  
    \* "S" -> Patrimônio Líquido  
    \* "A" -> Amortização  
    \* "C" -> Capital Social

    \* "E" -> Custos de Empréstimos

    \* "P" -> Patrimônio (Prejuízo)  
    \* "I" -> Ativo Intangível  
    \* "D" -> Ativo Diferido  
    \* "O" -> Orçamento  
    \* "V" -> Provisão de Despesa  
    \* "T" -> Custos de Transação

**Depreciam = "|N|D|I|O|T|E"**  
**Não depreciam = "S|A|C|P|V"**

**Saiba Mais**:

[MP\_SIGAATF - O QUE TRATA O CAMPO N4\_OCORR ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018328552-MP-SIGAATF-O-QUE-TRATA-O-CAMPO-N4-OCORR-?source=search)

[MP - SIGAATF: Quais as opções que existem de preenchimento do campo N5\_TIPO.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017722312-MP-SIGAATF-Quais-as-op%C3%A7%C3%B5es-que-existem-de-preenchimento-do-campo-N5-TIPO-?source=search)

[MP - SIGAATF - Cálculo Mensal não calcula para todos os bens e preenche o campo N3\_FIMDEPR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000465528-MP-SIGAATF-C%C3%A1lculo-Mensal-n%C3%A3o-calcula-para-todos-os-bens-e-preenche-o-campo-N3-FIMDEPR-?source=search)

[MP - SIGAATF - Utilização de procedure no cálculo de depreciação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021716291-MP-SIGAATF-Utiliza%C3%A7%C3%A3o-de-procedure-no-c%C3%A1lculo-de-deprecia%C3%A7%C3%A3o?source=search)

[MP-SIGAATF - ATFA050 QUAL O VALOR MÍNIMO PARA CALCULO DE DEPRECIAÇÃO?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016041211-MP-SIGAATF-ATFA050-QUAL-O-VALOR-M%C3%8DNIMO-PARA-CALCULO-DE-DEPRECIA%C3%87%C3%83O-?source=search)
