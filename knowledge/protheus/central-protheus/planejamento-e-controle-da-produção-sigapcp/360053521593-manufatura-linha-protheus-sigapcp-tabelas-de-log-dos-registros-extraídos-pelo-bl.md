---
article_id: 360053521593
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 2d9d9ecb948f23ec3cbaeac253f82ed815a50886620914631b6025343220921d
fetched_at: '2026-06-28T22:42:47.049482+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Tabelas de log dos registros extraídos
  pelo Bloco K
type: support-article
updated_at: '2023-11-09T14:05:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053521593-Manufatura-Linha-Protheus-SIGAPCP-Tabelas-de-log-dos-registros-extra%C3%ADdos-pelo-Bloco-K
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:50 min  
  
Dúvida  
Como posso conferir os registros de produção enviados para o **SpedFiscal** em períodos anteriores?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução****No processamento do **Bloco K**, as informações extraídas da produção para o **arquivo fiscal** são registradas em tabelas de **log** para fins de conferência e auxílio no cálculo de períodos futuros. Em caso de dúvidas na geração ou histórico é possível consultar os registros gerados verificando as tabelas abaixo:   
  
**K230 - Itens Produzidos** Tabela: **SVS - Bloco K - Registro K230**  
**K235 - Insumos Consumidos** Tabela: **SVT - Bloco K - Registro K235**  
**K290 - Produção Conjunta – Ordem de Produção** Tabela: **SVU - Bloco K - Registro K290**  
**K291 - Produção Conjunta – Itens Produzidos** Tabela: **SVV - Bloco K - Registro K291**  
**K292 - Produção Conjunta – Insumos Consumidos** Tabela: **SVW - Bloco K - Registro K292**  
**K270 - Correção de Apontamento dos Registros** Tabela: **T4G - Bloco K - Registro K270**  
**K275 - Correção de Apontamento e Retorno de Insumos dos Registros** Tabela: **T4H - Bloco K - Registro K275**  
**K260 - Reprocessamento/Reparo de Produto/Insumo** Tabela: **T4E - Bloco K - Registro K260**  
**K265 - Reprocessamento/Reparo – Mercadorias Consumidas e/ou Retornadas** Tabela: **T4F - Bloco K - Registro K260**Importante ressaltar que os **logs** referente aos registros de correção serão gerados somente se o ambiente não possuir customização neste processo, e somente para registros de produção.  
As tabelas possuem uma estrutura espelho do *layout* fiscal exigido pela receita.  
  
**Importante**Sempre que um período for regerado via **SpedFiscal** os registros do período serão apagados e recriados nas tabelas de **log**.
