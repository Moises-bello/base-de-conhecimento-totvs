---
article_id: 360047685334
category: PMS - Dúvidas Gerais
content_hash: 9cd78e7a52cb43e2cc4e4b54e54eee18540803d54826852852fb421020e29336
fetched_at: '2026-06-28T22:37:17.776443+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Medição Venda Remessa
type: support-article
updated_at: '2025-01-10T19:56:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047685334-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Medi%C3%A7%C3%A3o-Venda-Remessa
---

**Dúvida**

Após informar a Tarefa para cadastrar Medição de venda e remessa, o botão "Adicionar"  não é habilitado.

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da versão 12.  
  
**Solução**

Só é permitido faturar os Itens da tarefa se o campo Vlr. Total de Venda estiver preenchido.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071058473)

Efetue os procedimentos, abaixo para o correto funcionamento da rotina;

1. Estrutura do projeto, Informe o Custo Standard do produto **AFA\_CUSTD;**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069930534)**

2. Informe o Valor da Despesa **AFB\_VALOR**;

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069930874)**

**3. Na rotina Medição de Vendas e Remessa;**

Na parte inferior da tela informe Valor da Venda, % Faturar, Quantidade Faturar, e automaticamente o campo "Adicionar" será habilitado e o Item do projeto pronto para o Faturamento.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069931294)

**Saiba mais em : <https://tdn.totvs.com/x/lMeFDg>**
