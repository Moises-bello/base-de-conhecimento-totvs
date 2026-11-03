---
article_id: 360016053771
category: PMS - Projetos
content_hash: 8f156bba4601fd2556d4b8ceeccd4d3463ed96a444aa6d8e916a548532a42885
fetched_at: '2026-06-28T22:37:14.908835+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Gerar Empenho por Projeto
type: support-article
updated_at: '2024-02-23T12:12:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016053771-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Gerar-Empenho-por-Projeto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21563491123991) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Como gerar Empenho através do Gestão de Projetos?   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da versão 11.80  
  
**Solução**

Para a Integração seguir os procedimentos:

1. Configure os parâmetros;

MV\_PMSCSC = .F.

MV\_PMSREPL = 2

MV\_PMSPREV = 2

2. Data da necessidade do Item do projeto, tem que ser menor que a data que esta sendo gerada o planejamento de execução;

![necessidade.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414476584343)

3. Após Incluir o Projeto, va em :  Atualizações > Projetos > Gerenciamento de Execução;

4, Selecionar o Projeto > Planejamentos > Gerar;

![20211130_084534.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4414482791319)

Detalhes na Faq : [Projetos](https://tdn.totvs.com/x/ZaTxF)
