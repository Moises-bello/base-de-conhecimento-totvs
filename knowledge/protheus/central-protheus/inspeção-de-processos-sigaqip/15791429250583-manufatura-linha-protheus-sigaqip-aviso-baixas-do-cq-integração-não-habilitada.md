---
article_id: 15791429250583
category: Inspeção de Processos (SIGAQIP)
content_hash: 8a3b9a8a7d48974e2b6d129c116fd180d095fb8103d28003dc3025ca016e5d49
fetched_at: '2026-06-28T22:42:25.664979+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Aviso Baixas do CQ - Integração Não
  Habilitada
type: support-article
updated_at: '2023-07-07T14:37:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15791429250583-Manufatura-Linha-Protheus-SIGAQIP-Aviso-Baixas-do-CQ-Integra%C3%A7%C3%A3o-N%C3%A3o-Habilitada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15791417954711) Tempo aproximado para leitura: **00:00:50 min****Ocorrência**Na rotina **QIPA215 - Resultados**, ao selecionar a aba **Baixas do CQ** é retornado aviso **Baixas do CQ - Integração Não habilitada (MV\_QIPEST) - A integração entre módulo de Inspeção de Processos (SIGAQIP) e o módulo de Estoque e Custos (SIGAEST) está desabilitada**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**O aviso **Baixas do CQ** ocorre sempre ao clicar na aba **Baixas do CQ** quando não existe integração habilitada entre o módulo **Inspeção de Processos - SIGAQIP** e o módulo de **Estoque e Custos - SIGAEST**.  
  
**Solução**  
Para solucionar essa ocorrência, realize o seguinte passo:  
1. Caso não tenha integração habilitada com o **SIGAEST**, clique no botão **OK** para fechar o aviso. O aviso não é impeditivo para executar o processo na rotina **QIPA215 - Resultados.**  
**Importante**  
Esta validação e consistência estará liberada oficialmente no **pacote 12.1.2310**. Para versões anteriores anteriores é necessário a criação manual dos parâmetros descritos no tópico **Observação**.  
  
**Saiba mais**Para habilitar a integração poderá verificar o passo a passo descrito no documento [Baixas do CQ (QIPA215 - SIGAQIP).](https://tdn.totvs.com/pages/releaseview.action?pageId=742224954)
