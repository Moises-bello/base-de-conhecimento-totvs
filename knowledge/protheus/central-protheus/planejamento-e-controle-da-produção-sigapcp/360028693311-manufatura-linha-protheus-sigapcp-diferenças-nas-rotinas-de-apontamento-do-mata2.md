---
article_id: 360028693311
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1c2bfd913ba0329fb1eac693e387a3faea4e24e4c9c48cc24886abd376024759
fetched_at: '2026-06-28T22:42:42.200922+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Diferenças nas rotinas de apontamento
  do MATA250, MATA680 e MATA681
type: support-article
updated_at: '2024-05-14T20:44:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028693311-Manufatura-Linha-Protheus-SIGAPCP-Diferen%C3%A7as-nas-rotinas-de-apontamento-do-MATA250-MATA680-e-MATA681
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23484937416983)*Tempo aproximado para leitura: **00:01:30 min****Dúvida**Quais as diferenças no apontamento através do **MATA250 - Produção Simples**, **MATA680 - Produção Pcp Mod1** e **MATA681 -**  **Produção Pcp Mod2**?  
  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O apontamento por meio do **MATA250** é utilizado quando a empresa não controla os processos envolvidos na produção. A **OP - Ordem de Produção** é produzida sem controle dos recursos envolvidos. Neste caso somente os produtos empenhados são requisitados, se o programa estiver parametrizado para realizar esse movimento automaticamente.  
  
No apontamento de produção por meio do **MATA681** é necessário que o produto produzido tenha um roteiro cadastrado em **Processo Produtivo - PCPA124** ou **Processo Produtivo por Estrutura - PCPA129**. Ao realizar o apontamento de produção é necessário apontar todas as operações envolvidas, indicando recursos e duração.  
Neste modelo, além de requisitar os produtos empenhados, o Sistema também requisita a **MOD - Mão de Obra** correspondente ao centro de custos do recurso em questão, e a quantidade requisitada é a duração calculada pelo Sistema, com base nas informações fornecidas de data e hora inicial e data e hora final.  
  
Já no apontamento por meio do **MATA680** o Sistema faz a leitura da tabela **SH8 - Operações Alocadas**, gerada a partir do **MATA690** **- Carga Máquina** e faz a sugestão do recurso, data e hora inicial e final. A requisição dos componentes e do **MOD** é da mesma forma que no **MATA681**.
