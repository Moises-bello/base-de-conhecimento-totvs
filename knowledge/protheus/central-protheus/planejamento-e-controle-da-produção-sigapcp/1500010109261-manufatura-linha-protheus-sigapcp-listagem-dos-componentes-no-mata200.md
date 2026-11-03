---
article_id: 1500010109261
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 8a5b2a06bc887da79e192b09de8519a812e799164a25fa5a15268e6f42a62005
fetched_at: '2026-06-28T22:42:43.523963+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Listagem dos componentes no MATA200
type: support-article
updated_at: '2022-05-23T11:45:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010109261-Manufatura-Linha-Protheus-SIGAPCP-Listagem-dos-componentes-no-MATA200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:00:55 min**  
**Dúvida**Que filtros são aplicados ao listar os componentes em tela  no **MATA200 - Cadastro de Estruturas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Ao listar os componentes em tela é avaliado se o componente faz parte da revisão da estrutura que está sendo consultada através da informação preenchida no campo **Revisão** que está em tela e o conteúdo dos campos **G1\_REVINI - Revisão Inicial** e **G1\_REVFIM  - Revisão Final,** se não fizer parte o mesmo não é listado.   
Já com relação aos itens intermediários, são listados aqueles que fazem parte da última revisão da estrutura do item, neste caso é avaliado o conteúdo do campo **B1\_REVATU - Revisão da Estrutura** do cadastro do item intermediário e o conteúdo dos campos **G1\_REVINI** e **G1\_REVFIM** dos seus componentes.
