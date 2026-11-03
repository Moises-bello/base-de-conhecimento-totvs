---
article_id: 36074198847639
category: 'Financeiro - Borderô contas a Pagar '
content_hash: 9631e954a92f3cda9c7a3303073fb81448f92ce3a32803f58c4f4592305cd0ff
fetched_at: '2026-06-28T22:37:34.991852+00:00'
product: protheus
section_id: 35057529029143
source: central-protheus
title: Cross Segmentos Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Qual lançamento
  padrão utilizar para contabilizar o borderô na baixa automática?
type: support-article
updated_at: '2025-11-03T19:46:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36074198847639-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Qual-lan%C3%A7amento-padr%C3%A3o-utilizar-para-contabilizar-o-border%C3%B4-na-baixa-autom%C3%A1tica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36074198828311) Tempo aproximado para leitura: 00:05**min**  
  
**Dúvida**  
Qual lançamento padrão utilizar para contabilizar o borderô na baixa automática?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução:**

O  lançamento padrão 532 (Contas a pagar - baixas de títulos por borderô) é utilizado para contabilizarmos todos os pagamentos efetuados ao(s) título(s) que foram colocado(s) em borderô(s), neste documento iremos exemplificar sua utilização e seus principais conceitos:

**CTBAFIN:**

**Cenário 1 - partida dobrada:**

|  |  |
| --- | --- |
|  | **Sequencia 001** |
| Conta Credito | SE2->E2\_CREDIT |
| Conta Debito | SE2->E2\_DEBITO |
| Histórico | "Pagamento do titulo "+ SE2→E2\_NUM+SE2→E2\_PREFIXO+ " no borderô" + SE2→E2\_NUMBOR |
| Origem | "532-001" |
| Tipo de lançamento | 3 - partida dobrada |
| Valor do lançamento | SE5->E5\_VALOR |

**Cenário 2 - partida simples com totalizador do borderô:**

|  |  |
| --- | --- |
|  | **Sequencia 001** |
| Descrição | LP532 - BAIXA DE BORDERO - TITULO A TITULO |
| Tipo de lançamento | 1 - Debito |
| Conta Debito | SA2->A2\_CONTA |
| Conta Credito |  |
| Valor do lançamento | SE2->E2\_VALLIQ |
| Histórico | "BAIXA TIT "+SE2->E2\_NUM+" REF BORDERO "+SE2->E2\_NUMBOR+" DT "+DTOC(SE2->E2\_DTBORDE) |

|  |  |
| --- | --- |
|  | **Sequencia 002** |
| Descrição | LP532 - BAIXA DE BORDERO - TOTAL BORDERO |
| Tipo de lançamento | 2 - Crédito |
| Conta Debito |  |
| Conta Credito | SA6->A6\_CONTA |
| Valor do lançamento | VALOR |
| Histórico | "BAIXA REF BORDERO "+SEA->EA\_NUMBOR+" DT "+DTOC(SEA->EA\_DATABOR) |

**FINA090:**

|  | **Sequencia 001** |
| --- | --- |
| Conta Credito | IIF(SE5->E5\_MULTNAT =='1',SA6->A6\_CONTA,SE2->E2\_CREDIT) |
| Conta Debito | IIF(SE5->E5\_MULTNAT =='1',SA2->A2\_CONTA,SE2->E2\_DEBITO) |
| Histórico | "Pagamento do titulo "+ SE5->(E5\_NUMERO+E5\_PREFIXO)+ " no bordero" + SEA->EA\_NUMBOR |
| Origem | "532-001" |
| Tipo de lançamento | 3 - partida dobrada |
| Valor do lançamento | IIF(SE5->E5\_MULTNAT =='1',SEV->EV\_VALOR,SE5->E5\_VALOR) |

Variáveis contábeis disponíveis:

* VALOR - Variável totalizadora dos valores de pagamentos efetuados sobre os títulos do borderô - disponível na contabilização online e offline;
* VALOR2 - Variável totalizadora dos descontos aplicados sobre o pagamento do(s) borderô(s) - disponível na contabilização offline;
* VALOR3 - Variável totalizadora dos juros aplicados sobre o pagamento do(s) borderô(s) - disponível na contabilização offline;
* VALOR4 - Variável totalizadora das multas aplicadas sobre o pagamento do(s) borderô(s) - disponível na contabilização offline;
* VALOR5 - Variável totalizadora da correção monetária aplicada sobre o pagamento do(s) borderô(s) - disponível na contabilização offline;
* STRLCTPAD - Contém o(s) número(s) do(s) borderô(s) - disponível na contabilização offline;
  + Na contabilização offline (CTBAFIN), caso o lançamento contábil seja o aglutinador de vários borderôs, essa variável será disponibilizada com uma lista de todos eles (separados por ponto e virgula);

#### **Demais informações:**

* [Contabilização CNAB LP530 e LP532](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027015252-MP-SIGAFIN-CNAB-FINA430-Os-lan%C3%A7amentos-padr%C3%B5es-530-e-532-contabiliza-o-Retorno-de-Pagamento)
* [Diferença entre os LP's 521 e 532](https://tdn.totvs.com/x/XFkMEQ)
* [FIN0010\_LPAD\_Como\_utilizar\_rateio\_de\_múltiplas\_naturezas\_por\_Centro\_de\_Custo?](https://tdn.totvs.com/pages/viewpage.action?pageId=229147656)

Saiba mais

[532 Baixas de Titulos por Bordero de Pagamento](https://tdn.totvs.com/display/public/PROT/532+Baixas+de+Titulos+por+Bordero+de+Pagamento)
