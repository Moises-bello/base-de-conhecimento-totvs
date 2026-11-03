---
article_id: 24630409820951
category: Financeiro - Comissão
content_hash: 36022a4ea2b87ae6b20e46bc139f038afcc6ed205c2da8313e3890cfbdef99ff
fetched_at: '2026-06-28T22:37:50.846144+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF Bloco 4080
type: support-article
updated_at: '2026-02-06T14:55:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24630409820951-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Bloco-4080
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38216180053271) Tempo aproximado para leitura: **00:08 min**

**Ocorrência**  
Não está sendo gerado o IRRF de comissão para o vendedor

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33.

**Causa**  
Neste cenário, recomenda-se a validação de todos os cadastros relacionados ao processo.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o módulo Financeiro, Atualizações, Cadastros de Cliente, Aba Fiscais, os campos abaixo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24630425659159)

2. Acesse o cadastro de naturezas, aba Impostos, ajuste os campos, calcule IRRF, porcentagem IRRF (conforme a necessidade) e recolhe IRRF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24630425661975)![](https://centraldeatendimento.totvs.com/hc/article_attachments/24630425667863)

3. Acesse o cadastro de Produtos, aba Impostos, ajuste o campo **Imposto de Renda.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24630425672087)

4. No cadastro de vendedor, a aba **Pagamento de Comissão** deverá conter o fornecedor vinculado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24630409769879)

5. Ao incluir um pedido de venda, após preencher as informações necessárias do pedido, é necessário selecionar a **natureza de rendimento** para cada produto individualmente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24630425680663)

6. Em "Outras ações", na Planilha Financeira, é possível visualizar o imposto de IRRF que será gerado. Ao transmitir o pedido, o TX do imposto será gerado no Contas a Pagar.![](https://centraldeatendimento.totvs.com/hc/article_attachments/24630409782551)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24630409790103)

7. Ao executar o extrator fiscal, o registro T162 será gerado.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/24630409791767)**

**Saiba mais**

[Fique por dentro das atualizações do Reinf](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[How To - Reinf](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Bloco-40-Gera%C3%A7%C3%A3o-dos-layouts-T154-e-T158)
