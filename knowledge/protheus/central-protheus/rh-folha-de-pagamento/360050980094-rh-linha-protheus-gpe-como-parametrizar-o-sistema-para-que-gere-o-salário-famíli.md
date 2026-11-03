---
article_id: 360050980094
category: RH - Folha de Pagamento
content_hash: 75335aa206403fb84282cf5f79762b4a10b97b221882e5fd4bfc3248cc1a0121
fetched_at: '2026-06-28T22:44:14.677179+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o sistema para que gere o salário
  família com base no salário mínimo menos uma verba
type: support-article
updated_at: '2024-09-09T19:53:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050980094-RH-Linha-Protheus-GPE-Como-parametrizar-o-sistema-para-que-gere-o-sal%C3%A1rio-fam%C3%ADlia-com-base-no-sal%C3%A1rio-m%C3%ADnimo-menos-uma-verba
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26251820389271) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**Como parametrizar o sistema para que gere o salário família com base no salário mínimo menos uma verba?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Para que o sistema gere o salário família com base no salário mínimo menos uma verba, basta realizar a seguinte configuração:

Criação das Fórmulas conforme exemplo:

Formula 1 (formula adicionada para considerar o valor do inss na base, por se tratar de um desconto, deve-se somar uma vez que o valor está negativo):

Val\_SALMIN := Val\_SALMIN + fBuscaPD(acodfol[064,1])

O fBuscaApd busca o valor referente ao ID de cálculo 64 (Inss)

![](https://tdn.totvs.com/download/attachments/281987333/image2017-6-23%2016%3A7%3A27.png?version=1&modificationDate=1498245416000&api=v2)

Fórmula 2 (Fórmula usada para retornar o valor do salário minimo):

Val\_SALMIN := Val\_SALMIN - fBuscaPD(acodfol[064,1])

 

![](https://tdn.totvs.com/download/attachments/281987333/image2017-6-23%2016%3A10%3A56.png?version=1&modificationDate=1498245416000&api=v2)

Adição das Fórmula no roteiro (Formula 1 antes do Calculo da Pensão e Formula 2 após o cálculo:

![](https://tdn.totvs.com/download/attachments/281987333/image2017-6-23%2016%3A12%3A10.png?version=1&modificationDate=1498245416000&api=v2)

Parâmetro 11:

![](https://tdn.totvs.com/download/attachments/281987333/image2017-6-23%2016%3A6%3A14.png?version=1&modificationDate=1498245416000&api=v2)

Folha Calculada:

Calculo Pensão = 724 - 180

Calculo pensão = 544

Calculo pensão = 544 \* 0,3

Calculo pensão = 163,2

![](https://tdn.totvs.com/download/attachments/281987333/image2017-6-23%2016%3A4%3A59.png?version=1&modificationDate=1498245416000&api=v2)

Cadastro Beneficiário:

![](https://tdn.totvs.com/download/attachments/281987333/image2017-6-23%2016%3A16%3A45.png?version=1&modificationDate=1498245416000&api=v2)  
  
**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
