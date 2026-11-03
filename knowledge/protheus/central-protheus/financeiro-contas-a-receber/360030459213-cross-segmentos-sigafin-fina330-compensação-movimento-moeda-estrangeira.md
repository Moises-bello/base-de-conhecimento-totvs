---
article_id: 360030459213
category: Financeiro - Contas a Receber
content_hash: 2689f2fd2451adffb7de250c41c40a874a055601204e7908cb4ef19fd6472ee0
fetched_at: '2026-06-28T22:38:14.216463+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - SIGAFIN - FINA330 - Compensação Movimento Moeda Estrangeira
type: support-article
updated_at: '2023-07-06T21:35:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360030459213-Cross-Segmentos-SIGAFIN-FINA330-Compensa%C3%A7%C3%A3o-Movimento-Moeda-Estrangeira
---

**Dúvida**Compensação Movimento Moeda Estrangeira.

**Ambiente**Microsiga Protheus - Financeiro  - A partir da versão 12

**Solução**1 - Para o processo de Compensação a Receber que não considera **banco,** a gravação respeita a moeda do título.

**E5\_MOEDA** → Moeda do título envolvido na compensação  
**E5\_VALOR** → Valor do movimento na moeda do Título  
**E5\_VLMOED2** → Valor do movimento (**E5\_VALOR**) convertido para **Real** quando a moeda do título for **Estrangeira.****Exemplos:**  
**1.** **Compensação Contas a Receber** (Recebimento em dólar e **NF** em real)

**Recebimento Antecipado** (**RA**)![](http://tdn.totvs.com/download/attachments/451255094/ra_incl.PNG?version=1&modificationDate=1547482121790&api=v2)  
  
**NF**:  
![](http://tdn.totvs.com/download/attachments/451255094/nf_incl.PNG?version=1&modificationDate=1547482159943&api=v2)

Saldo **SE1** - **Contas a Receber**![](http://tdn.totvs.com/download/attachments/451255094/Comp_01_E1.PNG?version=2&modificationDate=1547482219953&api=v2)

 

Gravação **SE5** - **Movimentos Bancários**  
![](http://tdn.totvs.com/download/attachments/451255094/Comp_01_E5.PNG?version=1&modificationDate=1547482191577&api=v2)

Note que o campo **E5\_VALOR** é gravado com base na moeda de cada título e o **E5\_VLMOED2** é a conversão do movimento em moeda estrangeira.  
Para a registro do tipo **NF**, o movimento foi gerado em real.  
Para o registro do tipo **RA**, o movimento foi realizado em dólar.  
  
Considerando a taxa contratada do recebimento adiantado, $ 1560,31 é equivalente R$ 5.000,00  
$ 1.560,31 x 3,2045 = R$ 5.000,00

**2.** Correção Monetária vs Taxa Contratada  
  
No padrão não existe correção monetária para taxa contratada (**E1\_TXMOEDA**). Esse campo deve ser preenchido quando existe um acordo comercial da taxa.   
Uma vez firmado esse acordo, os valores de pagamento / recebimento não estão sujeito a correção monetária visto que todas as operações realizadas com valores da Nota Fiscal (**NF**) e do Recebimento Antecipado (**RA**) estão estabelecidos no acordo comercial que determinou uma taxa.  
  
**Recebimento Antecipado** (**RA**)**![](http://tdn.totvs.com/download/attachments/451255094/ra_incl_2.PNG?version=1&modificationDate=1547483143363&api=v2)**

 

**NF**  
![](http://tdn.totvs.com/download/attachments/451255094/nf_incl_2.PNG?version=2&modificationDate=1547483123517&api=v2)

Gravação **SE5** - **Movimentos Bancários**  
![](http://tdn.totvs.com/download/attachments/451255094/Comp_02.PNG?version=1&modificationDate=1547483205557&api=v2)  
**Observação**:  
Como pode ser verificado na imagem de gravação da **SE5**, não é gerado correção monetária quando ambos os títulos possuem taxa contratada.

**Importante**:  
Quanto a contabilização do processo de **Compensação CR** (para rotina **FINA330** com data superior à 27/12/18), vale ressaltar que com a mudança na gravação dos valores em moeda estrangeira, pode ocorrer casos em que os Lançamentos Padrões **596 e 588** (LP de compensação e estorno, respectivamente) que utilizem o campo **E5\_VALOR** (ou o **E5\_VLMOED2)** para a contabilização e necessitem ser tratados para que a contabilização seja feita na moeda corrente.

Ex.: Atuar em um **LP 596** que utiliza como valor da moeda 01 o campo **E5\_VALOR:** ![](http://tdn.totvs.com/download/attachments/451255094/sem%20tit.jpg?version=1&modificationDate=1549997026257&api=v2)

Na ilustração acima, atuamos em uma movimentação bancária com valores em moeda estrangeira, o sistema passa a considerar o valor do **E5\_VLMOED2** para contabilização (R$ 2.000,00) ao invés do valor de US$ 666,67 do campo **E5\_VALOR.**![](http://tdn.totvs.com/download/attachments/451255094/sem%20tit1.jpg?version=1&modificationDate=1549997285183&api=v2)

Dessa forma a contabilização continua correta:![](http://tdn.totvs.com/download/attachments/451255094/sem%20tit2.jpg?version=1&modificationDate=1549997658283&api=v2)

Foi disponibilizado o parâmetro: **MV\_CMTXCON,** para permitir compensação títulos com taxa contratada distintas e gerar variação monetária do recebimento (**RA)** em relação Título (**NF**).

**Saiba mais:**  
Documentação do Parâmetros: [Criação do parâmetro MV\_CMTXCON](http://tdn.totvs.com/pages/viewpage.action?pageId=391550445)
