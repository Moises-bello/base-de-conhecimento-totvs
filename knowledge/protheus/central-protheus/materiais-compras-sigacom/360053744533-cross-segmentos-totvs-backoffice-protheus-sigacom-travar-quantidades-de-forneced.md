---
article_id: 360053744533
category: Materiais - Compras (SIGACOM)
content_hash: 27b4d5e3de3d3d73df427204fd6b769155807763550cbbd437f9568737c68dc1
fetched_at: '2026-06-28T22:41:25.374704+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Travar quantidades
  de fornecedores na Cotação para algum Grupo/usuário
type: support-article
updated_at: '2022-05-18T21:24:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053744533-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Travar-quantidades-de-fornecedores-na-Cota%C3%A7%C3%A3o-para-algum-Grupo-usu%C3%A1rio
---

**Dúvida**

Travar quantidades de fornecedores na Cotação para algum Grupo/usuário  
  
**Ambiente**

Protheus – Compras – A partir da versão 12  
  
**Solução**

Como configurar para que o usuário não altere a quantidade de fornecedor e tenha sempre um valor fixo no pergunte?

O parâmetro **MV\_SELFOR** deve constar habilitado para que seja apresentada a tela de parâmetros na rotina de Gerar Cotação (**MATA131**).

Acesse via Configurador > Senhas > Configuração de Perguntas, nessa opção é possível determinar por grupo ou por usuário

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087419654/mceclip2.png)

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087412094/mceclip0.png)**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087420234/mceclip3.png)**

Para identificar o nome do Pergunte pressione F1 no campo do pergunte.

No exemplo abaixo consta bloqueado, pois foi cadastrado no configurador para esse usuário

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087419594/mceclip1.png)**

Nessa situação o usuário não conseguirá alterar a informação desses campos, pois constará como bloqueado.
