---
article_id: 20653853881751
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 0d1e5754f5be1e9cb5e9f2b07362aa7f0a124f373d6f7640ccb921cfea118ebc
fetched_at: '2026-06-28T22:37:56.517107+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA710
  - Preenche a tabela F75 - Titulos, mas não preenche a tabela F76 - Pedidos '
type: support-article
updated_at: '2024-03-15T14:35:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20653853881751-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Financeiro-FINA710-Preenche-a-tabela-F75-Titulos-mas-n%C3%A3o-preenche-a-tabela-F76-Pedidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20653882054679) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar executar o JOB, os dados da tabela **F76 ou F75** não estão sendo populados, com isso não exibe os titulos e pedidos de venda/compra no **Novo Gestor Financeiro - FINA710**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Causa**Esse incidente ocorre, pois na **SX2**, o compartilhamento das tabelas **F75, F76** podem estar divergentes, para o correto funcionamento dos registros, ambas devem possui o mesmo modo de compartilhamento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20653882059799)

**Saiba mais:**

**[Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=611007335)**  
**[NGFJOBQR - Adiciona filtro na query de seleção dos títulos e/ou pedidos no JOB do Novo Gestor Financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=718423712)**
