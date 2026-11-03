---
article_id: 4403954746903
category: Controle de Documentos (SIGAQDO)
content_hash: 79bdfe15652ffcf0f8e5befdbf349235a74f55508b69a93f023e540cbccc041e
fetched_at: '2026-06-28T22:42:29.120808+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QD050ECP exibido na rotina QDOA050
type: support-article
updated_at: '2025-06-30T17:48:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403954746903-Manufatura-Linha-Protheus-SIGAQDO-Help-QD050ECP-exibido-na-rotina-QDOA050
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33154163517335) Tempo aproximado para leitura: **00:00:50 min**  
**Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao finalizar o documento é exibido o *help* **QD050ECP - Existem criticas pendentes para este documento**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Este *help* é exibido quando existe uma crítica relacionada ao documento e esta crítica não foi baixada, ou quando a crítica foi gerada pelo usuário, mas invés de clicar em Devolver Documento é clicado Finalizar Documento.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Consulte o documento em questão na rotina **QDOA050 - Cadastro de Documentos** ou na rotina **QDOA030 - Pendências**;  
2. No botão **Críticas** e em **Outras Ações/Txt Crit**, realize a leitura da crítica relacionada à este documento;  
3. Ainda neste botão, clique em **Outras Ações/Baixa Cr** para realizar a baixa da crítica;  
4. Finalize o documento.
