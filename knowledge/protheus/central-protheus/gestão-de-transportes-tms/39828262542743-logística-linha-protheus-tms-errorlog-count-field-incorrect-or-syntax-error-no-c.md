---
article_id: 39828262542743
category: Gestão de Transportes (TMS)
content_hash: 217197c3b80d49b6036f3afc9b9d16b47cf3b6272ad04d9867924d157a7484d9
fetched_at: '2026-06-28T22:45:27.721796+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Errorlog COUNT field incorrect or syntax
  error no cálculo de documentos
type: support-article
updated_at: '2026-04-17T17:36:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39828262542743-Log%C3%ADstica-Linha-Protheus-TMS-Errorlog-COUNT-field-incorrect-or-syntax-error-no-c%C3%A1lculo-de-documentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39828297312407) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao calcular documento no TMS utilizando o Configurador de Tributos, ocorre *errorlog* **COUNT field incorrect or syntax error** em *query* relacionada as tabelas **CKC, F23, F26 e CIO** do fonte **BACKOFFICE.FISCAL.CONFIGURADOR.MESSAGES.MESSAGE-GROUP-DECODER.TLPP** do fiscal.  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Causa**  
Esse *errorlog* ocorre porque o fonte **BACKOFFICE.FISCAL.CONFIGURADOR.MESSAGES.MESSAGE-GROUP-DECODER.TLPP** tenta executar a *query* com 23 parâmetros, e só há 22 parâmetros. O parâmetro faltante é o Tipo de Operação, que caso não seja preenchido no TMS, não estava sendo enviado ao Fiscal.  
  
**Solução**  
Para solucionar essa ocorrência, o fonte **TMSXFUNB.prw** do TMS deve estar com a data **25/03/2026 ou superior.**  
  
**Saiba mais**  
Pacotes de correção do fonte **TMSXFUNB.prw** de 25/03/2026: 12.1.2310: <https://r.totvs.io/p/1244611>;   
12.1.2410: <https://r.totvs.io/p/1244612>; 12.1.2510: <https://r.totvs.io/p/1244613>  
Documentação da correção: [DT Inconsistência em Query do fiscal ao calcular documento.](https://tdn.totvs.com/pages/viewpage.action?pageId=1054115388)  
Esse pacote será incorporado final de abril ao pacote acumulado: [Pacotes de Atualização - TOTVS Logística TMS Linha Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=553908682#issues-17)
