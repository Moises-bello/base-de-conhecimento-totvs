---
article_id: 7657759522839
category: PMS - Projetos
content_hash: 12a0bee1ad2da430d482b3c19168b3cac54a4a89f619116754856e3cd98f5a98
fetched_at: '2026-06-28T22:37:14.924978+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Help "OPERACAO INVALIDA"
type: support-article
updated_at: '2025-04-29T19:17:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7657759522839-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Help-OPERACAO-INVALIDA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31751720699159) Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Ao incluir uma Autorização de Entrega apresenta o **help "OPERACAO INVALIDA - opção invalida nesta fase do projeto"**

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Causa**Na fase do projeto os campos **Inclui CP (Contrato de Parceria)** e **Inclui SC (Solicitação de Compras)** não estão habilitados.

![fase.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7657658277911)  
  
**Solução**Para não apresentar o Help, cadastre na fase do projeto os campos **Inclui CP (Contrato de Parceria)** e **Inclui SC (Solicitação de Compras)** como Sim.

O sistema valida o campo Solicitação de Compras, pois caso não tenha SC vinculada ao contrato, o sistema ira criar automaticamente para vincular a Autorização de Entrega.

Cheque se o campo **"Evento 83 (AEA\_EVEN83)"** está como "1 - Sim" em todas as fases de projeto e orçamento (rotinas PMSA070 e PMSA060)  
  
Cheque se não está ocorrendo por conta da não permissão do usuário (na seção do "Saiba mais" abaixo)

**Saiba mais:**

[Usuário sem permissão no módulo PMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17737986260503-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAPMS-Usu%C3%A1rio-sem-permiss%C3%A3o-no-m%C3%B3dulo-PMS)
