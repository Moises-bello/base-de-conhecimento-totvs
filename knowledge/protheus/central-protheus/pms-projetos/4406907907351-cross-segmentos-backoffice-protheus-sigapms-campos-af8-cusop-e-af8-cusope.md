---
article_id: 4406907907351
category: PMS - Projetos
content_hash: 60a28ec3c13d29b88db938398e1b8948e43fa7fb8462ddf5b1cdaa05411a9aed
fetched_at: '2026-06-28T22:37:14.875837+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Campos AF8_CUSOP e AF8_CUSOPE
type: support-article
updated_at: '2024-02-23T12:42:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406907907351-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Campos-AF8-CUSOP-e-AF8-CUSOPE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21563979111319) Tempo aproximado para leitura: **2 min** **Dúvida**

Como é realizado o calculo de custo do projeto ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas versões.

**Solução**

O módulo Gestão de Projetos (PMS) possibilita que o processo de produção de um determinado produto gere custos a um projeto, integrando-o assim com o módulo PCP (Planejamento e Controle de Produção). Quando uma Ordem de Produção (OP) é gerada por um planejamento de um projeto, automaticamente esta OP fica vinculada ao projeto para que seus custos sejam repassados ao mesmo. Para melhor controlar esses custos, podemos escolher o que e quando considerar como custo de um projeto, por meio dos campos **AF8\_CUSOP** e **AF8\_CUSOPE**.

Temos então 2 alternativas para o campo AF8\_CUSOP (Custo de Produção), como padrão, o campo vem

 como **1-Movimento de Requisição**:

**AF8\_CUSOP estiver igual à “1“ – Movimento de requisição:**

O sistema considerará para custos do projeto, somente os movimentos internos (SD3) que forem de requisições para uso do projeto e não vinculados à OP, ou seja, verificará as amarrações na tabela AFI (Movimentos internos x PMS).

**AF8\_CUSOP estiver igual à “2“ – Movimento de Produção:**

O sistema irá considerar para custos do projeto, somente os movimentos internos (SD3) que forem referentes a requisições de matérias primas para uma OP específica.

Neste caso o ponto definido para agregação de custos são as requisições de materiais necessários para produção do produto final. A cada movimento interno do tipo **Requisição** ou um apontamento de produção que gere movimentos de requisições automáticas, serão atualizados os custos do projeto, referente a esta produção.

**Maiores detalhes em : <https://tdn.totvs.com/x/Zq9n>**
