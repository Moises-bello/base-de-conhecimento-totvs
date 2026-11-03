---
article_id: 360043619673
category: RH - Soluções para error.log
content_hash: 57771b25b59a25225712b186357ea2f73bc2b88d6540f625e01d3e5896264eca
fetched_at: '2026-06-28T22:44:09.093944+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Error log na importação de variáveis - argument
  #0 error, expected D->C, function dtoc on RETPERGLOG(GPEXREL.PRX)'
type: support-article
updated_at: '2025-09-12T11:48:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043619673-RH-Linha-Protheus-GPE-Error-log-na-importa%C3%A7%C3%A3o-de-vari%C3%A1veis-argument-0-error-expected-D-C-function-dtoc-on-RETPERGLOG-GPEXREL-PRX
---

**Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**Ao efetuar a importação de variáveis, através da rotina GPEA210, gera o *error log*: *"****argument #0 error, expected D->C, function dtoc on* RETPERGLOG(GPEXREL.PRX)**"**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
 **Causa**O problema ocorre por inconsistência no **Grupo de Perguntas** **GPE210A.**  
  
**Solução**Para solucionar essa ocorrência, será necessário:  
**1.** Analisar se existem perguntas em duplicidade e caso exista, efetuar a manutenção do grupo de perguntas **GPE210A**;  
**2.** Analisar se o grupo de perguntas está conforme o padrão, (se contém todas as ordens de 1 a 5) conforme abaixo:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059102033)

**Saiba Mais:**[RH - Soluções para Error Log](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115003853987-RH-Solu%C3%A7%C3%B5es-para-error-log) Pacote de Expedição Contínua RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>   
Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)
