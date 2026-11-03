---
article_id: 360044816253
category: PMS - Projetos
content_hash: 3c3a33d179bcb60deb28e9079d533c8faebe2ccc337b6bf63f9cde930c58580c
fetched_at: '2026-06-28T22:37:14.836322+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - PMS - Conceito do custo
  markup
type: support-article
updated_at: '2022-01-27T18:20:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044816253-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-PMS-Conceito-do-custo-markup
---

**Dúvida**

Qual o conceito e como funciona o Markup no Gestão de Projetos (**PMSA410**)?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

O **Markup** é o percentual sobre o custo cobrado do cliente. É muito importante compreender que este não é simplesmente o “lucro” do projeto e que engloba um conceito mais amplo.

Podemos citar o exemplo da construção civil, na qual é chamado de BDI (Bonificação de despesas indiretas).

Esse percentual deve incluir não só o lucro, como todas as despesas indiretas do projeto que não podem ser mensuradas, rateadas e incluídas em tarefas, ou que não fazem sentido no planejamento.

Exemplo:

Valores que podem ser cobertos pelo Markup são:

* Custos administrativos
* Equipamentos de uso e seus custos
* Lucro
* Impostos e taxas

**Cadastro do Markup no Projeto (rotina PMSA410)**

Para cada tarefa ou EDT determina-se uma alíquota de Markup diferenciada, se zerada, é considerara a alíquota geral do orçamento.

O markup cadastrado no campo AF8\_ VALBDI é utilizado para calcular o valor do markup total do projeto.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060243794/mceclip0.png)

**Cadastro do Markup na Tarefa**

Markup Padrão: Para conhecer o markup de cada tarefa/EDT, deve-se informar o markup individual, ou seja, este campo sugere em cada tarefa o percentual padrão do projeto. 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061172573/mceclip1.png)

Obs:  Os valores do Markup e ajustes devem ser inseridos manualmente seja no Orçamento ou no Projeto.
