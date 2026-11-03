---
article_id: 38833871189527
category: Rental by ItUp Business
content_hash: c94b4d6de2410dad6b9bdedc9c070eb05b3f1e546544167c204d3fd1c2b05b9e
fetched_at: '2026-06-28T22:36:20.517280+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como ativar a gravação da
  tabela FQZ na devolução de locação
type: support-article
updated_at: '2026-03-05T19:49:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38833871189527-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-ativar-a-grava%C3%A7%C3%A3o-da-tabela-FQZ-na-devolu%C3%A7%C3%A3o-de-loca%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38833871174167) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como configurar o sistema para que a devolução da Remessa de Locação realize a gravação dos dados na tabela FQZ?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Solução**  
A persistência dos dados na tabela **FQZ** (Movimentação de Retorno de Locação) depende da ativação de um parâmetro de controle. Para realizar essa configuração, siga os passos abaixo:

1. **Configuração do Parâmetro:**

   * Acesse o módulo **SIGACFG (Configurador)**;
   * Vá em **Atualizações > Dicionários > Base de Dados > Parâmetros**;
   * Localize o parâmetro **MV\_LOCX022**;
   * Altere o seu conteúdo para **.T.** (Verdadeiro).
2. **Funcionamento do Processo:**

   * Com este parâmetro ativo, ao processar o retorno de locação pela rotina **LOCA001 (Manutenção de Projetos)**, o sistema passará a alimentar a tabela **FQZ**.

---

**Importante:** A ativação do **MV\_LOCX022** é essencial para a rastreabilidade do projeto, permitindo que o módulo de Locação identifique exatamente qual item retornou e em qual documento fiscal ele foi amparado.
