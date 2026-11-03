---
article_id: 4409826385047
category: Inspeção de Processos (SIGAQIP)
content_hash: 25d1226bad2e290ca8ffe0c2e115cfa4921799080ec563bb86a274e1fa7cf639
fetched_at: '2026-06-28T22:42:25.829405+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - MATA650 - Help C650NOPRI
type: support-article
updated_at: '2023-08-10T20:05:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409826385047-Manufatura-Linha-Protheus-SIGAQIP-MATA650-Help-C650NOPRI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16679021245719) Tempo aproximado para leitura: **00:01:25 min****Ocorrência**No módulo **SIGAPCP - Planejamento e Controle de Produção**, ao incluir uma **OP - Ordem de Produção** na rotina **MATA650 - Ordens de Produção** é apresentado o *help* **C650NOPRI**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**O *help***C650NOPRI**é apresentado quando o conteúdo do parâmetro **MV\_QIPFROT - Indica se deve utilizar o roteiro de operações primário, da especificação do produto, na abertura de Ordens de Produção** estiver com conteúdo igual à **T-True**. E neste caso, será considerado o roteiro primário e este deve ter o cadastro relacionado ao produto na especificação de produto.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique qual é o roteiro primário do produto da **OP**;  
2. Verifique se este produto possui especificação cadastrada na rotina **QIPA010 - Especificações** e se este cadastro está relacionado ao roteiro primário.  
  
**Observação**  
Caso utilize o parâmetro **MV\_QIPOPEP - Define a prioridade dos dados em relação à operação entre os ambientes QIP e PCP** com conteúdo igual à **3**, o conceito de integração inibe o funcionamento do parâmetro **MV\_QIPFROT**, visto que os roteiros do **SIGAPCP - Planejamento e Controle da Produção** poderão não existir no módulo **SIGAQIP - Inspeção de Processos**.
