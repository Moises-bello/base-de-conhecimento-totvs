---
article_id: 360018584472
category: Financeiro - Contas a Pagar
content_hash: 3a7a39ea30f5d1a42b8ddf531842cb36bff8321b96524e54a42ce25500405120
fetched_at: '2026-06-28T22:38:09.899388+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: MP - SIGAFIN - FINA340 - Compensação contas a pagar MOVIMENTO MOEDA ESTRANGEIRA
type: support-article
updated_at: '2025-10-13T21:27:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018584472-MP-SIGAFIN-FINA340-Compensa%C3%A7%C3%A3o-contas-a-pagar-MOVIMENTO-MOEDA-ESTRANGEIRA
---

**Dúvida**Erro gravação **SE5** - Compensação contas a pagar quando MOVIMENTO MOEDA ESTRANGEIRA.

**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.1.17  
  
  
**Solução**1 - Para os processos que não consideram **banco,**Liquidação, Fatura e Compensação CP, a gravação respeita a moeda do título.  
**E5\_MOEDA** → Moeda do título envolvido na compensação  
**E5\_VALOR** → Valor do movimento na moeda do Título  
**E5\_VLMOED2** → Valor do movimento (**E5\_VALOR**) convertido para **Real** quando a moeda do título for **Estrangeira.**

**Exemplos:**

**1 -** Compensação Contas a Pagar. (Pagamento em dólar e NF em real):  
  
Pagamento Antecipado (PA)

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014389312)

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014389372)

Saldo SE2 - Contas a Pagar![3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014389472)

Gravação SE5![4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014389652)

Note que o campo **E5\_VALOR** é gravado com base na moeda de cada título, e o **E5\_VLMOED2** é a conversão do movimento em moeda estrangeira.  
Para a registro do tipo **NF**, o movimento foi gerado em real.  
Para o **registro** do tipo **PA**, o movimento foi realizado em dólar.  
  
Considerando a taxa contratada do pagamento adiantado, $ 1560,31 é equivalente R$ 5.000,00  
$ 1.560,31 x 3,2045 = R$ 5.000,00  
  
**2** - Correção Monetária vs Taxa Contratada  
  
No padrão não existe correção monetária para taxa contratada (**E2\_TXMOEDA**). Esse campo deve ser preenchido quando existe um acordo comercial da taxa.   
Uma vez firmado esse acordo, os valores de pagamento / recebimento não estão sujeito a correção monetária visto que todas as operações realizadas   
com valores da (NF) Nota Fiscal e do (PA) Pagamento Antecipado estão estabelecidos no acordo comercial que prefixou uma taxa.  
  
Pagamento Antecipado (PA)

![5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014391851)

NF

![6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014392031)

Gravação SE5

![7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014392071)

Como pode ser verificado no imagem de gravação da SE5, **não é** gerado correção monetária quando ambos os títulos possuem taxa contratada.

***Em cenários que a NF possui taxa contratada e o PA não possui, não será gerado correção monetária uma vez que o posicionamento é na NF, caso a mesma possua taxa mesmo que o PA não possua, não irá gerar a correção monetária seguindo o exemplo do cenário 02***

**Importante:**Foi disponibilizado o parâmetro: **MV\_CMTXCON,** para permitir compensação títulos com taxa contratada distintas e gerar variação monetária do pagamento (PA) em relação Título (NF).  
Documentação do Parâmetros: [Criação do parâmetro MV\_CMTXCON](http://tdn.totvs.com/pages/viewpage.action?pageId=391550445)  
  
**Observação**:  
As rotinas e relatórios do sistema foram preparados para tratar os registros de base gerados antes e depois desta alteração, para exibirem o resultado esperado em ambos.
