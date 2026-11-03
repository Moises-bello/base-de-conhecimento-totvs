---
article_id: 20712858681751
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 3348ca817927418d46e7451c01244be5326849163429bcee5d631113a0d02f71
fetched_at: '2026-06-28T22:42:44.475347+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Mensagem FORMUL
type: support-article
updated_at: '2026-01-20T21:22:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20712858681751-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-FORMUL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20712858652055)** Tempo aproximado para leitura: **00:00:39 min**  
  
**Ocorrência**  
Na rotina **MATA650 - Ordem de Produção**, ao clicar para gerar os empenhos mostra a mensagem **FORMUL**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20712858653079)**

**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12.  
  
**Causa**  
Está apresentando erro na fórmula informada no cadastro de produto.  
  
**Solução**  
É necessário verificar para todos os produtos que serão empenhados, o conteúdo dos campos **B1\_ESTFOR - Formula Estoque Segurança** e **B1\_FORPRZ - Formula Calculo do Prazo**, é preciso rever a fórmula ou limpar o conteúdo desses campos.
