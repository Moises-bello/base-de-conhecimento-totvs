---
article_id: 17903636405271
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 1c50cbe1897a7565c4ee676e2382c3864e8ef141ee8112efcd8dab9cd2b0d77d
fetched_at: '2026-06-28T22:42:42.148941+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Controle manual de revisões de estruturas
type: support-article
updated_at: '2023-09-29T12:53:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17903636405271-Manufatura-Linha-Protheus-SIGAPCP-Controle-manual-de-revis%C3%B5es-de-estruturas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17903667717783)***Tempo aproximado para leitura: **00:00:50 min  
  
Dúvida**Como fazer uso do **controle de revisões manual** no **cadastro de estruturas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O **controle manual das revisões de estruturas** permite que ao incluir ou excluir um componente da estrutura, uma nova revisão de estrutura seja criada**.**Para trabalhar com o **controle manual das revisões de estrutura**, o parâmetro **MV\_REVAUT-Indica se o controle de revisões será controlado automaticamente** deve ter o conteúdo igual a **.F.**Através da rotina **PCPA200 - Manutenção de Estruturas**, é possível ajustar os campos **G1\_REVINI - Revisão Inicial do Componente** e **G1\_REVFIM- Revisão Final do Componente**, com a revisão desejada.  
  
**Exemplo**PA  
--> MP1 (revisão inicial 001 revisão final 001)  
--> MP2 (revisão inicial 002 revisão final 002)  
  
No momento de abrir a **OP - Ordem de Produção** é possível informar através do campo **C2\_REVISAO - Revisão** a **revisão da estrutura** na qual quer que gere os **empenhos**.  
  
Ao abrir uma **OP** para o produto PA, na revisão 001, o componente **MP1** será empenhado.  
Ao abrir uma **OP** para o produto PA, na revisão 002, o componente **MP2** será empenhado.
