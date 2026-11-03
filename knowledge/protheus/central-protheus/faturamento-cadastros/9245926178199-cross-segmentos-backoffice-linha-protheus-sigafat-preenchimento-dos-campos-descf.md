---
article_id: 9245926178199
category: Faturamento - Cadastros
content_hash: 70a9a47be379fef1f2afd8a5bad882c29ea9cf60c367eee314b2412890aedda1
fetched_at: '2026-06-28T22:38:36.725539+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Preenchimento dos
  campos "Desc.Financ." (E4_DESCFIN) e "Dias p/Desc." (E4_DIADESC)
type: support-article
updated_at: '2023-01-25T14:29:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9245926178199-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Preenchimento-dos-campos-Desc-Financ-E4-DESCFIN-e-Dias-p-Desc-E4-DIADESC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**

Como preencher os campos "Desc.Financ." (E4\_DESCFIN) e "Dias p/Desc." (E4\_DIADESC) e para que estes campos servem?

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões.

**Solução**

Na condição de pagamento, é possível definir descontos no título, para que sejam gatilhados no pedido de venda ao usar a condição de pagamento e no título ao gerar a emissão da nota fiscal de saída com uma TES que gere duplicatas.

O desconto **"Desc.Financ." [E4\_DESCFIN]** é obtido na baixa do título financeiro caso não seja pago nos últimos dias antes do vencimento **“Dias p/Desc [E4\_DIADESC]”.**

**Fluxogramas de gatilhos padrão:**

E4\_DESCFIN (Cond. Pagto)  -> C5\_DESCFI (Pedido de venda) -> E1\_DESCFIN (Título)

E4\_DIADESC (Cond. Pagto) -> E1\_DIADESC (Título)

**Exemplo:**

1 - Configuração da condição de pagamento:

* **"Dias p/Desc." E4\_DIADESC = 15 (Se o cliente pagar nos últimos dez dias antes do vencimento não terá desconto)**
* "Tipo" E4\_TIPO = 1
* "Cond. Pagto" E4\_COND = 30 (trinta dias até o vencimento após a emissão, por conta do tipo 1)
* "Dias da Cond" E4\_DDD = ‘Vazio’ (A regra da condição de pagamento (E4\_COND) será avalida instantaneamente após a emissão do título)
* **"Desc.Financ." E4\_DESCFIN = 10 (Dez porcento de desconto sobre o total do título [duplicata])**

**OBS:** O desconto será aplicado se o título não for baixado entre últimos 15 dias colocados no campo "Dias p/Desc." (**E4\_DIADESC).**

2 - Exemplo de um título gerado por um faturamento com a condição acima:

* "Emissao" E1\_EMISSAO = 01/01/2022 (Emissão da primeira duplicata, que é igual a data da emissão da nota fiscal de saída)
* "Vencimento" E1\_VENCTO = 31/01/2022 (Vencimento da parcela)
* "Vlr.Titulo" E1\_VALOR = 100 (Valor da parcela, como é a única, também é o total da nota fiscal de saída)
* **"Desc. Financ." E1\_DESCFIN = 10**
* **"Dias p/Desc." E1\_DIADESC = 15**

**Se a baixa ocorrer** entre o dia da emissão **(01/01/2022)** e o dia **16/01/2022** o **desconto será obtido** na baixa do título financeiro.

Se a baixa ocorrer na quantidade de dias **(E4\_DIADESC) anteriores em relação ao vencimento (31/01/2022),** ou seja, do **dia 17/01/2022** até o vencimento **(31/01/2022) não haverá descontos.**

**Exemplos de dias da baixa do título:**

**"DT Baixa" E1\_BAIXA** = 16/01/2022 (Dia da baixa, que não ultrapassou os 15 dias do campo "Dias p/Desc." (E4\_DIADESC), contando do Vencimento do título [E1\_VENCTO] para trás)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11928626487831)

Ao baixar o título o desconto é obtido na baixa. (10% de 100 = 10)

**Se o título não fosse baixado dia 17/01/2022 como no exemplo anterior e sim baixado dia 16/01/2022:**

**"DT Baixa" E1\_BAIXA** = 17/01/2022 (Dia da baixa, que ultrapassou os 15 dias do campo "Dias p/Desc." (E4\_DIADESC), contando do Vencimento do título [E1\_VENCTO] para trás)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11928588376215)

Ao baixar o título o desconto não é obtido na baixa.

**Saiba mais sobre as condições de pagamento:**

* **TDN:** [Condições de Pagamento - Completo](https://tdn.totvs.com/x/PdpSDg)
* **KCS:** [Condições de Pagamento - Específico](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiYm7bSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBnWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxNzQ2ODMxMi1Dcm9zcy1TZWdtZW50by1UT1RWUy1CYWNrb2ZmaWNlLUxpbmhhLVByb3RoZXVzLVNJR0FGQVQtQ29uZGklQzMlQTclQzMlQjVlcy1kZS1QYWdhbWVudG8GOwhUOg5zZWFyY2hfaWRJIikxMmE5MjAxYi1hNDYyLTRkYTYtYWZmNy1mN2ZhYTY0MjQ3YmUGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIh1jb25kacOnw7VlcyBkZSBwYWdhbWVudG8GOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--8f786711cbd49788c1821a37316cd02b45236625)
