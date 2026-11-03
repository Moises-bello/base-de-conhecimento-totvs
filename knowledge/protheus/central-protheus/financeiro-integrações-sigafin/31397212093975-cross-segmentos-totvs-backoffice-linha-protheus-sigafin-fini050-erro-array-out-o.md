---
article_id: 31397212093975
category: Financeiro - Integrações (SIGAFIN)
content_hash: e9c8396599df67a34a236bd508dcc30564f74cf6fe3aa97192b10bc08d986e95
fetched_at: '2026-06-28T22:38:18.516059+00:00'
product: protheus
section_id: 1500001539241
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice Linha Protheus - SIGAFIN - FINI050 - Erro:
  array out of bounds ( 3 of 2 ) on V2000(FINI050.PRW) 01/08/2022 10:21:19 line :
  534'
type: support-article
updated_at: '2025-04-14T19:27:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31397212093975-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINI050-Erro-array-out-of-bounds-3-of-2-on-V2000-FINI050-PRW-01-08-2022-10-21-19-line-534
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31397212084631) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Erro: array out of bounds ( 3 of 2 ) on V2000(FINI050.PRW) 01/08/2022 10:21:19 line : 534  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice Protheus - Contas a Pagar - A partir da versão 11  
  
**Causa**Esse erro ocorre devido a configuração do De/Para do centro de custo   
  
**Solução**Necessário corrigir o cadastro do De/Para para o centro de custo   
  
Passo1: Acessar o configurador (**SIGACFG**) -> Ambiente -> Schedule -> De Para de Mensagem Única  
Passo2: Filtrar o Alias do **Centro de Custo** que é a tabela **CTT**  
  
A estrutura para configurar o De/Para é separando por pipe '|' deve seguir por -> **Grupo | filial | Centro de custo**  
Exemplo de um cadastro de De/Para se a tabela **CTT** estiver com o compartilhamento   
**exclusivo:**  01|01|0585  
  
Exemplo de um cadastro de De/Para se a tabela **CTT** estiver com o compartilhamento   
**Compartilhado**: 01||0585
