---
article_id: 35139166778007
category: Financeiro - Aplicação / Emprestimos
content_hash: bfcb999360f284f4ea1e21ce979ecaf277384121d9b0f641c1aa4acb8f059dfe
fetched_at: '2026-06-28T22:37:59.499331+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA716 - Como é feita
  a geração das parcelas na rotina de aplicação empréstimo?
type: support-article
updated_at: '2025-09-26T12:34:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35139166778007-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Como-%C3%A9-feita-a-gera%C3%A7%C3%A3o-das-parcelas-na-rotina-de-aplica%C3%A7%C3%A3o-empr%C3%A9stimo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35139176730135) Tempo aproximado para leitura: **00:01:00min**  
  
**Ocorrência**  
FINA716 - Como é feita a geração das parcelas na rotina de aplicação empréstimo?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA716 - Todas as versões  
  
**Causa**  
Ao incluir operações do tipo "FIN, COM, TAN, ALD, TIB, HOT" e etc... o campo "Gera Parcela" (c) fica desabilitado para a inclusão do empréstimo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35139176731031)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35139176731671)

**Solução**  
Atualmente a opção de geração de parcela para empréstimo somente irá funcionar para os tipos de operações "**EMP**" e "**TEM**" caso tenha configurado Template

Pois no padrão do sistema existe um gatilho que limita outros tipos de operação.

Gatilho que possui o campo EH\_GERPARC  
M->EH\_APLEMP == "EMP" .And. M->EH\_TIPO $ "EMP|TEM"

Segue trecho da documentação

[MSERV-4529\_DT\_Gera\_parcela\_validação\_SEH](https://tdn.totvs.com/pages/releaseview.action?pageId=269421068)                                                                                  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/35216560905367)

Saiba mais:  
[MSERV-4529\_DT\_Gera\_parcela\_validação\_SEH](https://tdn.totvs.com/pages/releaseview.action?pageId=269421068)

<https://tdn.totvs.com/pages/releaseview.action?pageId=269420881>

[Empréstimos - FINA716](https://tdn.totvs.com/pages/releaseview.action?pageId=684987254#tabs-08)
