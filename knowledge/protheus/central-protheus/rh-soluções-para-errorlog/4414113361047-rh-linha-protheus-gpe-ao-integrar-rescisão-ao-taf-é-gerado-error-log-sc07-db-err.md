---
article_id: 4414113361047
category: RH - Soluções para error.log
content_hash: d0813d2cb022a9ba354b98f616763ef9df34e7380f879567bb8ead6d95eea88d
fetched_at: '2026-06-28T22:44:09.031659+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao Integrar Rescisão ao TAF é gerado error log
  - _SC07: DB error (Insert): -27 File: _SC07 -  on MSUNLOCK'
type: support-article
updated_at: '2021-11-25T13:31:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414113361047-RH-Linha-Protheus-GPE-Ao-Integrar-Rescis%C3%A3o-ao-TAF-%C3%A9-gerado-error-log-SC07-DB-error-Insert-27-File-SC07-on-MSUNLOCK
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao tentar realizar uma **Integração de Rescisão** ao Módulo do **TAF**, através da rotina **GPEM040**, para geração do Evento **S-2299** ou **S-2399** é gerado ***error log***: "**\_SC07: DB *error (Insert)*: -27 *File*: \_SC07 - *on* MSUNLOCK(APLIB060.PRW)**"  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Este erro ocorre devido à utilização de **DBAccess** com versão anterior à **20.1.1.5**  
  
**Solução  
1. Atualizar** o **DBAccess** com a versão do link abaixo:  
Windows x64: <https://suporte.totvs.com/portal/p/10098/download#detail/1031464>   
Linux x64: <https://suporte.totvs.com/portal/p/10098/download#detail/1031462>   
  
**Informações complementares**  
Documentação Técnica sobre a Correção: <https://tdn.totvs.com/display/tec/20.1.1.5>   
Como atualizar DBAccess: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020724792>   
Pacote de Expedição Contínua do RH:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>   
Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)  
Pacote de Expedição Contínua do Medicina e Segurança do Trabalho:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773>
