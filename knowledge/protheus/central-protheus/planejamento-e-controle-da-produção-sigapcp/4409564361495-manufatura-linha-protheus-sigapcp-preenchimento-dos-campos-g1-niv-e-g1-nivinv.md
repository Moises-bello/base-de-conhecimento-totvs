---
article_id: 4409564361495
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 57890d2191b336151ea3da84b3e3fd1352acd5204de756ffda17eb9e4227db78
fetched_at: '2026-06-28T22:42:45.732623+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Preenchimento dos campos G1_NIV e G1_NIVINV
type: support-article
updated_at: '2021-09-28T10:44:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409564361495-Manufatura-Linha-Protheus-SIGAPCP-Preenchimento-dos-campos-G1-NIV-e-G1-NIVINV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:50 min** **Dúvida**Quando os campos **G1\_NIV - Nível do Produto** e **G1\_NIVINV - Nível Invertido** são preenchidos?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Os campos **G1\_NIV** e **G1\_NIVINV** são preenchidos quando ocorre o recálculo dos níveis das estruturas. Esse processo é executado quando nas rotinas **MATA200 - Cadastro de Estruturas** ou **PCPA200 - Estrutura** são incluídos ou excluídos componentes de uma determinada estrutura e o usuário confirma o recálculo de níveis ao sair da rotina.   
Ou ao executar o **MATA712 - MRP** ou **PCPA107 -MRP Multi-empresa** com o parâmetro **MV\_NIVALT - Define se a estrutura teve ou não alterações**, com o conteúdo **S** e o parâmetro da rotina **Recalcula Níveis da Estrutura** com o conteúdo **Sim**.
