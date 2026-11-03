---
article_id: 360028525832
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: b16f9d8330fd88ca83bbb0290f2932f34a04d24e5f82d4dd2403e36b8be22214
fetched_at: '2026-06-28T22:42:44.481571+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Mensagem Id do formulário de origem:
  [CZ3MASTER] Id do campo de origem: [CZ3_CDFA]'
type: support-article
updated_at: '2022-05-20T14:58:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028525832-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-Id-do-formul%C3%A1rio-de-origem-CZ3MASTER-Id-do-campo-de-origem-CZ3-CDFA
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao confirmar o cadastro de um produto o usuário recebe a mensagem **Id do formulário de origem: [CZ3MASTER] Id do campo de origem: [CZ3\_CDFA].**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**Essa situação ocorre quando a integração com os módulos **SIGASFC - Chão de Fábrica ou SIGADPR** - **Desenvolvedor de Produtos** está ativa através dos parâmetros **MV\_INTSFC - Define se existe integração entre o Módulo SIGASFC e outros módulos** ou **MV\_INTDPR - Define se existe integração entre o Módulo SIGADPR e outros módulos**, mas os grupos de produtos não estão na tabela correspondente no **SIGASFC** ou **SIGADPR.**  
  
**Solução**Para solucionar essa ocorrência, execute o seguinte passo:  
1. Acesse a rotina **SFCA020 - Família**;   
2. Clique em **Regerar**;   
3. Efetue novamente o cadastro do produto.
