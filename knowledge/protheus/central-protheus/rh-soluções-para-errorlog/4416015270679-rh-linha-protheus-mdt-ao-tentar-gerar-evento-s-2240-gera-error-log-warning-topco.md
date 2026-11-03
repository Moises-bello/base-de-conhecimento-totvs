---
article_id: 4416015270679
category: RH - Soluções para error.log
content_hash: b6a957b9a66e4decc2bfef979a795dcec9dd4153569d63e8f8c199adc0b852fe
fetched_at: '2026-06-28T22:44:08.979028+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - MDT - Ao tentar gerar evento S-2240 gera error log -
  Warning - TOPCONN - Create index error: -19 : COMMAND_FAILED - TOP Error -19 - Field
  [CM9_NOMEVE] not found.'
type: support-article
updated_at: '2025-09-16T17:09:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416015270679-RH-Linha-Protheus-MDT-Ao-tentar-gerar-evento-S-2240-gera-error-log-Warning-TOPCONN-Create-index-error-19-COMMAND-FAILED-TOP-Error-19-Field-CM9-NOMEVE-not-found
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34980746944279) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao tentar gerar **Evento S-2240 (Riscos)**, através da rotina **MDTA881** gera *error log*: "**Warning - TOPCONN -** **Create index error: -19 : COMMAND\_FAILED - TOP Error -19 - Field [CM9\_NOMEVE] not found.**".  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões.  
  
**Causa**O erro ocorre pois o ambiente não possui o **campo CM9\_NOMEVE.**  
  
**Solução**Para solução do problema será necessário seguir os passos abaixo:  
**1.** Verificar se existe o campo (CM9\_NOOMEVE) no dicionário (SX3);  
**2.** Se o campo existir, será necessário efetuar backup da tabela CM9 e recriá-la;  
**3.** Caso o campo não exista, será necessário **rodar o dicionário** abaixo, através do **UPDDISTR** para criação do mesmo:  
<https://suporte.totvs.com/portal/p/10098/download#detail/1044897>  
  
**Saiba Mais:**Como executar o UPDDISTR corretamente:<http://tdn.totvs.com/pages/viewpage.action?pageId=366649057>  
Pacote de Expedição Contínua do Gestão de Pessoal: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854> Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)  
Pacote de Expedição Contínua do Medicina e Segurança do Trabalho:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773>
