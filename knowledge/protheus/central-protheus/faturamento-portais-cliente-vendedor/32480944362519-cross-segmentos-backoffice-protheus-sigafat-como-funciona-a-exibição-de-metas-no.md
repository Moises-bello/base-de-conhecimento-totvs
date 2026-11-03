---
article_id: 32480944362519
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 754d9d32ca7b9d8dcf6cd20bd771eec6e0cb70e8210301f7f89f0fa52aeefe28
fetched_at: '2026-06-28T22:38:23.904097+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como funciona a exibição
  de metas no PGV (Portal Gestão de Vendas)?
type: support-article
updated_at: '2025-05-30T21:02:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32480944362519-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-funciona-a-exibi%C3%A7%C3%A3o-de-metas-no-PGV-Portal-Gest%C3%A3o-de-Vendas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32480952245143) Tempo aproximado para leitura: **00:02:00 min****

**Dúvida**

Como são definidas e exibidas as metas no PGV?

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

As metas exibidas no **PGV (Portal Gestão de Vendas)** na opção ***Minhas Metas*** são definidas diretamente no Protheus, por meio da rotina Metas de Vendas (**FATA050**).

Para que a meta seja considerada corretamente pelo PGV, é necessário seguir estas orientações no cadastro:

1. Preencher obrigatoriamente os campos:

   * Vendedor
   * Data (referente ao mês/ano da meta)
   * Valor da Meta
2. Deixar em branco os campos:

   * Região
   * Grupo de Produtos
   * Tipo de Produto
   * Produto

O PGV considera **apenas a primeira linha de meta cadastrada para o vendedor e o mês correspondente**, ignorando qualquer filtro adicional. Por isso, caso esses campos estejam preenchidos, o PGV pode não exibir a meta corretamente.

Importante destacar que a rotina Metas de Vendas (**FATA050**) serve apenas para cadastrar as metas.  
A comparação entre metas e vendas realizadas no PGV é feita automaticamente, porém de forma simplificada.

Caso a necessidade for um comparativo mais completo e analítico, com filtros por região, grupo de produto, tipo ou até por produto, recomendamos utilizar o relatório **Metas x Realizado (FATR050)**, que está disponível no módulo Faturamento (SIGAFAT - CRM).

Cada ferramenta tem seu foco: o PGV é mais visual e operacional, enquanto o **FATR050** é mais gerencial e detalhado.

**Saiba mais:**

[Metas de Venda (FATA050 - SIGAFAT)](https://tdn.totvs.com/x/Xp1dFQ)

[Metas x Realizado (FATR050 - SIGAFAT)](https://tdn.totvs.com/x/AEWbEg)

[Portal Gestão de Vendas: Guia de Referência - DR - Minhas Metas](https://tdn.totvs.com/x/CoY6MQ)
