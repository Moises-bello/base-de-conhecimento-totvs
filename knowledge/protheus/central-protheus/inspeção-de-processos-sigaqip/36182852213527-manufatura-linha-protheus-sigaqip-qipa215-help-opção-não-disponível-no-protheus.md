---
article_id: 36182852213527
category: Inspeção de Processos (SIGAQIP)
content_hash: 427988da31f52b8cd2976f58f03221233696ad30591eb832efdf12ff1b4b7634
fetched_at: '2026-06-28T22:42:25.921644+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAQIP - QIPA215 - Help Opção não disponível
  no Protheus. Função: QP220CHKTCalled By {QP220Chkt()}'
type: support-article
updated_at: '2025-11-07T19:15:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36182852213527-Manufatura-Linha-Protheus-SIGAQIP-QIPA215-Help-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-QP220CHKTCalled-By-QP220Chkt
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36182852190871) Tempo aproximado para leitura: **00:01:50 min**  
  
**Dúvida**  
Ao acessar a rotina **QIPA215 - Resultados** apresenta o *help* **Opção não disponível no Protheus. Função: QP220CHKT Called By {QP220Chkt()}.** Como proceder?

**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12

**Solução**  
Para solucionar esse *help*, realize os seguintes passos:

1. Acesse o **SIGACFG - Configurador**;
2. Em **Base de Dados/Dicionários de Dados**, pesquise pela tabela **QPR - Medições**;
3. No campo **QPR\_DTMEDI - Data Medição**, verifique o conteúdo do campo **Validação - X3\_WHEN**;
4. Caso o conteúdo esteja apontando para a **função QP220CHKT**, limpe o conteúdo deste campo;
5. Salve a alteração realizada e atualize a base de dados.
