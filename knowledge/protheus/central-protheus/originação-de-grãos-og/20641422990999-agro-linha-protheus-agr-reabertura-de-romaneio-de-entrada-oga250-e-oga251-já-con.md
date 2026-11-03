---
article_id: 20641422990999
category: Originação de Grãos (OG)
content_hash: ee0204a99fdbc594a89cfd568bdd4fc42fa8ad0064f6e681990d1b35a09ccc74
fetched_at: '2026-06-28T22:45:44.744107+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Reabertura de Romaneio de entrada OGA250  e OGA251
  já confirmado
type: support-article
updated_at: '2025-06-26T11:13:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20641422990999-Agro-Linha-Protheus-AGR-Reabertura-de-Romaneio-de-entrada-OGA250-e-OGA251-j%C3%A1-confirmado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20641422967703) Tempo aproximado para leitura: **00:00:45 min****Ocorrência**  
No módulo Comercialização (Linha Protheus) - Originação de Grãos (OG), ao realizar o processo para reabrir um romaneio de entrada com pesagem ou sem pesagem é apresentada mensagem de Romaneio de entrada OGA250 e OGA251 já confirmado.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é preciso realizar o processo para reabrir um romaneio de entrada **com pesagem ou** **sem pesagem** no Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, será preciso reabrir um romaneio de entrada já confirmado. Sendo necessário reabrir porque faltaram informações importantes para este registro, realize os seguintes passos:

**1.** Acesse o **romaneio** que necessita ser reaberto e verifique a numeração da **Nota Fiscal**, na aba de **Comercialização**;

**2.** Acesse a rotina **MATA103** - **Documento de Entrada**e exclua a **Nota Fiscal de Entrada** gerada pelo **romaneio**;

**3.** Acesse novamente o registro de **romaneio** que necessita ser reaberto e por meio das **Ações Relacionadas** selecione a opção **Reabrir**. O **romaneio** será reaberto e as alterações necessárias poderão ser efetuadas.
