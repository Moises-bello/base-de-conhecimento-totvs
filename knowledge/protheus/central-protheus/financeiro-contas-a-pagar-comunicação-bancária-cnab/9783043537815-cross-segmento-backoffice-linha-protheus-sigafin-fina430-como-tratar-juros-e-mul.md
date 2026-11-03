---
article_id: 9783043537815
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: d0af373ee09b7beff90ff6ac7c9af4d3cadbf34831e14b837157b8a6a2ae0dc9
fetched_at: '2026-06-28T22:37:55.210517+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA430 Como tratar
  juros e multas na rotina FINA430 Retorno CNAB a pagar?  E como considerar juros
  e multa na base do IRRF para a rotina FINA080 - Baixas a pagar manual?
type: support-article
updated_at: '2023-09-13T21:07:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9783043537815-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA430-Como-tratar-juros-e-multas-na-rotina-FINA430-Retorno-CNAB-a-pagar-E-como-considerar-juros-e-multa-na-base-do-IRRF-para-a-rotina-FINA080-Baixas-a-pagar-manual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17508365805591) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como tratar juros e multas na rotina FINA430 Retorno CNAB a pagar ?  
E como considerar juros e multa na base do IRRF para a rotina FINA080 - Baixas a pagar manual?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Cenário 1**:  Ao ter um título no contas a pagar que tenha juros/multa e esteja parametrizado o IRPF para gerar o imposto de baixa do título.   
E como considerar juros e multa na base do IRRF para a rotina FINA080 - Baixas a pagar manual?

Exemplo: Assim que digitar o valor de juros/multa seja alterado o valor do IRPF no momento da baixa?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17508402242199)

**Solução 1:**

Altere o parâmetro para

MV\_IMPBAIX = 1 = Considera valores de juros, multa ou desconto.

**Cenário 2:**

Segue abaixo o conceito do sistema, quanto ao tratamento de juros:

- Taxa de Permanência é um valor fixo cobrado por dia de atraso no pagamento do titulo   
 - Juros é um percentual calculado sobre o valor baixado por dia de atraso   
  
Quando da baixa do título, a taxa de permanência, por ser um valor fixo, será multiplicado pelo número de dias de atraso, obtendo-se assim o valor total da taxa de permanência a ser cobrada, independente do valor baixado.  
  
Quanto aos Juros, é aplicado o percentual, multiplicado pelo número de dias em atraso (se Juros Simples) sobre o valor baixado.  
[Cálculo de juros - MV\_JURTIPO](http://tdn.totvs.com/pages/releaseview.action?pageId=39682457)  
  
No Financeiro para calcular taxa de permanência utilize o parâmetro: MV\_TXPER  
**MV\_LJJUROS** Igual ao parâmetro **MV\_TXPER** e maior que zero  
**MV\_TXPER** Igual ao parâmetro **MV\_LJJURO**S e maior que zero  
**MV\_LJMULTA** Maior que zero  
**MV\_JURTIPO** -> L (CONSIDERA CALCULO DE MULTA DA LOJA)  
**MV\_LJJUFIN** .F.  
**MV\_FINJRTP** 3 - Ambos (calcula juros e taxa de permanência)  
**MV\_TOLER** 0  
**MV\_LJFSEMA** 0 - não calcula no sábado e domingo  
  
**Parâmetro MV\_IMPBAIX**O parâmetro **MV\_IMPBAIX** considera os juros, multa ou desconto na base do imposto  
[Conceito parâmetro MV\_IMPBAIX](https://tdn.totvs.com/pages/releaseview.action?pageId=73084336)   
  
**Para o processo que trabalha com CNAB**   
A multa não tem como enviar na remessa, porém existe como enviar na remessa uma mensagem para cobrar x de multa após o vencimento.

- O banco retorna o valor de multa, e terá como tratar no retorno   
- Os juros somente é possível informar no campo de **PORCENTAGEM** de juros ou na taxa de permanência , devendo ser tratado em seu leiaute de configuração

A função **SOMAVALOR** poderá sanar a duvida da soma da multa de juros ou multa  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - FINA420 - Existem variáveis e funções que possam ser utilizadas na configuração de CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004894128-MP-SIGAFIN-CNAB-SISPAG-Existem-vari%C3%A1veis-e-fun%C3%A7%C3%B5es-que-possam-ser-utilizadas-na-configura%C3%A7%C3%A3o-de-CNAB-SISPAG?source=search)

Temos documentações que poderão apoiá-lo nos principais processos.  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Principais configurações para uso do CNAB - Modelos 1 e 2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7778595184407-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Principais-configura%C3%A7%C3%B5es-para-uso-do-CNAB-Modelos-1-e-2?source=search)

###
