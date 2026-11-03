---
article_id: 360049701194
category: Controle de Não Conformidades (SIGAQNC)
content_hash: 63b7e982900cf064f4804ec65245072cac40a5d9cfbfdeb3ee1c6c2c9b517c7d
fetched_at: '2026-06-28T22:42:28.003282+00:00'
product: protheus
section_id: 360005876654
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQNC - Não será permitida a Geração da Revisão
  para Lançamentos Pendentes
type: support-article
updated_at: '2021-05-19T12:00:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049701194-Manufatura-Linha-Protheus-SIGAQNC-N%C3%A3o-ser%C3%A1-permitida-a-Gera%C3%A7%C3%A3o-da-Revis%C3%A3o-para-Lan%C3%A7amentos-Pendentes
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min**  
**Ocorrência**Na rotina **QNCA030 - Cadastro de Plano de Ação**, ao clicar em **Outras Ações/Gera Revisão** é exibido o *help***Não será permitida a Geração da Revisão para Lançamentos Pendentes**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Não Conformidades (SIGAQNC) – Todas as versões  
  
**Causa**Este *help* é exibido quando existem etapas pendentes, ou seja, etapas que não foram 100% baixadas.  
  
**Solução**Para solucionar essa ocorrência, selecione o plano de ação na qual deseja gerar revisão e realize os seguintes passos:  
1. Clique em **Alterar**;  
2. Clique em **Outras Ações/Acao/Etap;**  
3. Verifique qual é o conteúdo do campo **Status Acao** de cada etapa.  
4. Somente será permitido gerar revisão para um plano de ação onde todas as etapas estejam com o campo **Status Acao** com o conteúdo igual a **4 - 100%**.
