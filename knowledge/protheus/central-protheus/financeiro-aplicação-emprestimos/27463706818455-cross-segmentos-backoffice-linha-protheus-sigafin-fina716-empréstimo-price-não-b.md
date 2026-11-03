---
article_id: 27463706818455
category: Financeiro - Aplicação / Emprestimos
content_hash: aa0b1b8413fd33b78ac50255b97dc8a256cab5e0e924ac3c9ee8961791192c53
fetched_at: '2026-06-28T22:37:59.548841+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice linha Protheus - SIGAFIN - FINA716 Empréstimo
  Price não bate as parcelas, como posso fazer as parcelas baterem com o contrato
  quando possui IOF, despesa e carência.
type: support-article
updated_at: '2024-10-31T14:58:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27463706818455-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA716-Empr%C3%A9stimo-Price-n%C3%A3o-bate-as-parcelas-como-posso-fazer-as-parcelas-baterem-com-o-contrato-quando-possui-IOF-despesa-e-car%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27463681502999) Tempo aproximado para leitura: **00:15:00 min****Dúvida**Empréstimo Price não bate as parcelas do contrato do banco, como posso fazer as parcelas baterem quando o contrato possui IOF, despesa e carência.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - Todas as versões  
  
**Solução**

Exemplo de contrato:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27463706794775)

Podemos observar que:

A data do valor liberado foi no dia **24/05/2024**

O valor do vencimento da primeira parcela vai ocorrer no dia **26/12/2024** (parcela com valor a ser pago)

Logo esse contrato possui **carência de 6 meses** que seriam:

os meses 06, 07, 08, 09, 10 e mês 11. E no mês 12 terá o dia para efetuar o pagamento.

Taxa anual **14,300%** (baseado em 360 dias ) MV\_DIASCTB = 360

Valor a operação **R$ 2.698.372,00**

Temos IOF no valor de **R$ 51.955,10**

Quantidade de parcelas são 42 parcelas + 6 de carência = **48 parcelas**

Temos despesas no valor de **R$ 26.069,48**

Valor de cada parcela **R$ 89.422,99**

Segue exemplo de inclusão no protheus

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27463706795671)

Obs: Não inserir as parcelas, e inserir no campo **Valor Amortização Parcela** o valor da parcela do seu contrato.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27463706796567)

Segue a projeção das parcelas

Onde cada parcela será de **R$ 89.422,99**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27463681509271)

**Gerando as 48 parcelas**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27463681510807)

Caso for inserido a quantidade 48 parcelas sem informar o valor da cada prestação

Qual o valor que o sistema irá gerar de prestação?.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27463681511831)

O valor da parcela calculada pelo sistema será de **R$ 89.147,78** ao invés de **R$ 89.422,99**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27463706800919)

Como é feito o cálculo?

**a)** Primeiro será necessário converter a taxa anual para a taxa diária

=(1+14,3%)^(1/360)-1

=**0,0371337%**

Obs: O conteúdo na formula "360" é pego do conteúdo do parâmetro MV\_DIACTB

**b)** calculando o juros compostos

=2776396,58\*(1+0,0371337%)^32-2776396,58

**=R$ 33.181,92**

Obs: O conteúdo na formula "32"  é referente a dias 25/06/2024 - 24/05/2024 = 32 dias

**c)** Segue aplicado a formula juros compostos para todos os meses   
Mês 06 = R$ 33.181,92  
Mês 07 = R$ 31.468,10  
Mês 08 = R$ 32.887,35  
Mês 09 = R$ 33.268,05  
Mês 10 = R$ 32.561,51  
Mês 11 = R$ 34.030,07

Total de juros compostos = **R$ 197.396,99**

Somando o valor do contrato + IOF + Despesas + os juros compostos referente aos mês 06, 07, 08, 09, 10 e mês 11, dá um total de **R$ 2.973.793,57**

R$ 2.698.372,00 Contrato + R$ 51.955,10 IOF + R$ 26.069,48 Despesas) +R$ 197.396,99 juros compostos do mês 06 até mês 11 = R$ 2.776.396,58

R$ 2.776.396,58 +R$ 197.396,99 = **R$ 2.973.793,57**

**d)** Calculo das parcelas ( **Primeiro modelo de formula** )

Achamos o FATOR

=(((14,3%)+1)^(30/360))-1

=**0,01120029**

Obs: O conteúdo na formula "360" é pego do conteúdo do parâmetro MV\_DIACTB

=(1+0,01120029)^42

=**1,596473781**

Obs: O conteúdo na formula "42"  é referente a quantidade de parcelas menos a carência. = 48-6 = **42 parcelas**

=**R$ 2.973.793,57**\*((1,596473781\*0,01120029)/(1,596473781-1))

=**89.147,78** de valor de prestação a ser paga

**e)** Calculo das parcelas ( **Segundo modelo de formula** )

Converter a taxa anual para taxa mensal

=(1+14,3%)^(1/12)-1

=**1,1200291%**

Obs: O conteúdo na formula "12"  é referente a quantidade de meses do ano. E 14,30% é a taxa anual do contrato.

=((1+1,1200291%)^42 \* 1,1200291% / ((1+1,1200291%)^42 - 1)) \* **2.973.793,57**

=**89.147,78** de valor de prestação a ser paga

Obs: O conteúdo na formula "42"  é referente a quantidade de parcelas - carência. = 48-6 = 42 parcelas

Por esse motivo o valor da prestação será de **R$ 89.147,78**e não de R$ 89.422,99

E o modo de incluir o contrato no protheus seria chumbar o valor da parcela no campo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27463681514775)

Caso contrário, o responsável por afirmar o contrato junto a instituição financeira terá que solicitar o cálculo de como instituição chegou no valor de parcela **R$ 89.422,99** seguindo o mesmo exemplo acima, para que possamos compartilhar a informação com o produto.

Iremos precisar saber:

 - Como foi calculado o juros das parcelas com carência

 - Como gerou o valor presente do contrato (valor do contrato + juros + IOF + Despesa) para ser inserido na formula das parcelas (item **c**)

 - Qual formula com valores aplicador para chegar na parcela (item d)

Sabia mais:

[FINA716 Como é feito o cálculo dos juros compostos em uma aplicação ou empréstimo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27324210803735-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA716-Como-%C3%A9-feito-o-c%C3%A1lculo-dos-juros-compostos-em-uma-aplica%C3%A7%C3%A3o-ou-empr%C3%A9stimo)

[FINA716 - Como é efetuado o calculo do juros nas parcelas?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13782176773527-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Como-%C3%A9-efetuado-o-calculo-do-juros-nas-parcelas)

[Aplicações - FINA716](https://tdn.totvs.com/pages/releaseview.action?pageId=684987286)

[Aplicações e empréstimos - FINA716 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=680254799)
