---
article_id: 37402315885975
category: Financeiro - Contas a Pagar
content_hash: b336c49d8aacdecb9da6effd4889ceaff91ad45c413c56ee5887db822d259d1f
fetched_at: '2026-06-28T22:38:09.823394+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFIN - Desdobramento de titulos
  com percentuais por parcela
type: support-article
updated_at: '2026-01-05T10:36:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37402315885975-Cross-Segmentos-Backoffice-Protheus-SIGAFIN-Desdobramento-de-titulos-com-percentuais-por-parcela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37402315860887) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida:**

Como realizar o desdobramento de um título em múltiplas parcelas (ex: 05 parcelas) onde a primeira parcela possua um valor de percentual diferente das demais?

**Ambiente:**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**  
  
Para realizar o desdobramento de títulos com valores personalizados por parcela, deve-se utilizar o cadastro de Condição de Pagamento com o Tipo 8.

A condição de pagamento tipo 8, atua de forma personalizada e permite que o usuário defina exatamente o percentual de rateio para cada parcela, possibilitando que a primeira parcela tenha um peso financeiro distinto do restante do título.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37402315861655)

No momento da inclusão do título ou na geração via documento de entrada/saída, o sistema aplicará esses percentuais sobre o valor total para gerar os vencimentos.

![Sem nome (1908 x 898 px).gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37402315862423)

**Importante:**

* A soma dos percentuais informados na condição de pagamento deve ser obrigatoriamente **100%**.
* Caso persistam dúvidas técnicas sobre a sintaxe de montagem da regra no cadastro da condição de pagamento (Tipo 8), recomenda-se o contato com o time de suporte do **Faturamento**, responsável por este cadastro base.

**Saiba Mais:**

[Cross Segmentos - Backoffice Protheus - SIGAFAT - Criação da condição de pagamento Tipo 8](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21678582446999-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cria%C3%A7%C3%A3o-da-condi%C3%A7%C3%A3o-de-pagamento-Tipo-8)  
[FAT0089 - Condições de Pagamento (MATA360) - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=240310845)
