---
article_id: 4404256593431
category: Financeiro - Contas a Pagar
content_hash: 3ac4804a562829d970068f30ffc42534d69516f4cad79c935d9b30e03a1839e3
fetched_at: '2026-06-28T22:38:07.267044+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - DIRF 0422 - Valor correção
  monetária não integram valor da DIRF
type: support-article
updated_at: '2021-07-14T13:27:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404256593431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-DIRF-0422-Valor-corre%C3%A7%C3%A3o-monet%C3%A1ria-n%C3%A3o-integram-valor-da-DIRF
---

**Ocorrência**

Títulos com moeda estrangeira ao qual na data do pagamento quando existe variação monetária os valores ajustados por esta variação não são somados aos valores para a DIRF mesmo os campos aos quais são ajustados para integração com a **DIRF**.  **E2\_VALOR** | **E2\_DIRF**

**FINA050** ao Incluir titulo de **exemplo**:  Prefixo INV tipo NF em Moeda 2 em data retroativa.

**FINA080** Baixa

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404243637783/mceclip1.png)

Com a taxa contratada. Ex. 5,80.

O sistema automaticamente calcula o valor em reais e na moeda estrangeira.

Ao ajustar o valor usando os campos juros e multa.

Abaixo incluir R$ 4,00 reais de multa no título para baixa.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404243673751/mceclip2.png)

Os valores carregados para DIRF são os valores inclusos no cadastro do título não são carregados os valores realmente pagos, aos quais consideram (descontos, juros, multas, correção/alteração de taxa).

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - TOTVS Protheus SIGAFIN - FINA401 DIRF  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema no cadastro do Fornecedor não esta de acordo com a necessidade de IR para geração na Baixa.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1.  No campo **A2CALCIRF** deverá estar como na Imagem abaixo = **2 IR BAIXA**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404256434071/mceclip0.png)

**Mais informações sobre o funcionamento da DIRF para a Receita Federal:**

<https://receita.economia.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/dirf-declaracao-do-imposto-de-renda-retido-na-fonte/arquivos-mafon/manual-do-imposto-de-renda-retido-na-fonte-2012/rendimentos-de-residentes-ou-domiciliados-no-exterior>
