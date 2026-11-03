---
article_id: 4416008039703
category: Inspeção de Entradas (SIGAQIE)
content_hash: cc3771a4592bb592de22e95ef1cba3897a6c8eed55ad9d806636e9798de1199f
fetched_at: '2026-06-28T22:42:27.011958+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Help Q070NAOUSU
type: support-article
updated_at: '2021-12-16T10:59:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416008039703-Manufatura-Linha-Protheus-SIGAQIE-Help-Q070NAOUSU
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:00:40 min****Ocorrência**Na rotina **QIEA070 - Equipes de Follow-Up** ao incluir um responsável ocorre o *help* **Q070NAOUSU - O usuário informado não foi localizado**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Causa**O *help* **Q070NAOUSU** ocorre quando o campo **Filial - QE5\_FILRES** está fora da posição padrão, pois o mesmo precisa estar na primeira coluna do **cadastro de follow-up**.  
  
**Solução**1. Acessar via **APSDU** a tabela **SX3 - Campos** e filtrar pela tabela **QE5 - Responsáveis por cada Equipe**;  
2. Substituir informações da **QE5** atual pela **QE5** anexada neste artigo.  
  
**Anexo**
