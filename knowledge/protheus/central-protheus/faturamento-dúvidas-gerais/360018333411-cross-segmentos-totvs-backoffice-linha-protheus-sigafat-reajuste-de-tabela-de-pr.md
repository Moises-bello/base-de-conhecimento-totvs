---
article_id: 360018333411
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 39076c50219d4246a23f5629f55e0be210d3c94a8de083357645670e9c5af076
fetched_at: '2026-06-28T22:38:30.037067+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Reajuste de
  Tabela de Preço por Planilha de Formação de Preço
type: support-article
updated_at: '2025-02-11T18:47:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018333411-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Reajuste-de-Tabela-de-Pre%C3%A7o-por-Planilha-de-Forma%C3%A7%C3%A3o-de-Pre%C3%A7o
---

**Dúvida**

Como efetuar o reajuste de tabela de preço por planilha de formação de preço?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**

Para efetuar o reajuste:

**1-** Em faturamento, ter uma **tabela de preço** (**OMSA010**) a ser reajustada.

Exemplo: produto 000001 ao preço de R$9,00para demonstrar a rotina de reajuste por tabela de formação de preço.

**2-**Em Estoque, consultas, **formação de preços** **(MATC010),** indique a tabela de preço a ser reajustada;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412259710743)

**Observações relevantes do processo:**  
  
Ao dar duplo clique no campo, abrirá a janela para edição.

\*O campo da Descrição da linha da Formação de Preço precisa conter:   **#código, espaço e o nome da tabela de preço.**\* A fórmula a ser utilizada dependerá da necessidade de cada cliente podendo usar um campo fixo, exemplo SB1->B1\_CUSTED, ou como nos exemplos acima.

**3**- Retornando ao Faturamento, Cenário de Vendas, Tabela de Preço, Ações Relacionadas, Reajuste;

**4-** No campo planilha, coloque o nome da **planilha de** **formação de preço** , que no caso foi utilizado a **Standard.pdv** mesmo, porém seu sufixo ".pdv".

**5-** Após a confirmação dos parâmetros e confirmação do reajuste, veja que o produto 000001 que custava R$ 9,00  para a venda, passou a custar R$ 10,00, conforme a linha 16 da planilha de formação, total variável.

Veja a demonstração de alteração de preço:

![20211104_153507.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412274752279)

**IMPORTANTE**

Com relação ao reajuste da Tabela de Preço (OMSA010) por planilha de formação de preço, atualmente,  não está preparada para reajustar com o uso da tabela SCO, para que o reajuste funcione tem que utilizar a planilha standard.pdv na system e configurar o parâmetro**MV\_REVPLAN = F.**  
Caso necessite de Auxílio no cadastro da Planilha de Formação de Preços (MATC010), entre em contato com o **Suporte Estoque/Custos** da TOTVS.

Para mais detalhes do processo, acesse a FAQ: **[Reajuste de Tabela de Preço por Planilha de Formação de Preço](https://tdn.totvs.com/x/S_gpE)**

**Saiba mais:**

**[Cross-Segmentos-Totvs-BackOffice-Protheus-Fatuamento-SIGAFAT-Reajuste-de-Valores-na-Tabela-de-Preço-Preço-Base-e-Pedidos-em-Aberto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019193491-Cross-Segmentos-Totvs-BackOffice-Protheus-Fatuamento-SIGAFAT-Reajuste-de-Valores-na-Tabela-de-Pre%C3%A7o-Pre%C3%A7o-Base-e-Pedidos-em-Aberto)**

**[Cross Segmentos- TOTVS Backoffice (Linha Protheus)- SIGAFAT-Reajuste-de-preço-através-da-rotina-MATA511B](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018663971-MP-FAT-Reajuste-de-pre%C3%A7o-atrav%C3%A9s-da-rotina-MATA511B)**
