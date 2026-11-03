---
article_id: 1500011531621
category: Gestão de Distribuição (SIGAOMS)
content_hash: 55d8c84bf4de6ba5db2159f8a9edf1c4ea1f18ca2d18f3444b52ebdd41bc0755
fetched_at: '2026-06-28T22:45:50.064719+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Por que o help OMS200ASSVEI é apresentado
  ao associar veículo na Montagem de Carga do TOTVS OMS
type: support-article
updated_at: '2021-08-13T17:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011531621-Log%C3%ADstica-Linha-Protheus-OMS-Por-que-o-help-OMS200ASSVEI-%C3%A9-apresentado-ao-associar-ve%C3%ADculo-na-Montagem-de-Carga-do-TOTVS-OMS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:42 min**  
**Dúvida**Por que o **help OMS200ASSVEI - O veículo deve ser do mesmo tipo informado pelo Cockpit Logístico** é apresentado ao **associar veículo** na **Montagem de Carga** do **TOTVS OMS**?  
  
**Ambiente**

TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - A partir da versão 12  
  
**Solução**Quando a carga for gerada pela integração do **TOTVS OMS - Order Management System** **com o TOL - TOTVS Otimização Logística**, o campo **Viagem Roteirizador - DAK\_VIAROT** será preenchido com o **número da Viagem**.  
  
Caso necessitar informar um veículo pela função de **Associar veículo**, localizada em  **Atualizações/Carga/Montagem de Carga - OMSA200/Carregamento** e informar um veículo com **Tipo de Veículo** diferente que está gravado na **tabela DK0 - Viagem CPL,** o **help OMS200ASSVEI** será apresentado.  
  
O parâmetro  **Tipo Veículo Otimização -** **MV\_CPLTVO,** localizado em  **Atualizações/Cockpit Logístico/Parâmetros de Integração/Geral**, reflete na apresentação do **help OMS200ASSVEI**, contém as seguintes opções:

* **1 - Impedir**: no vínculo do veículo na carga, se for informado um tipo de veículo diferente do que consta na viagem do **TOL**, não será permitido, sendo apresentado o **help OMS200ASSVEI**.
* **2 - Alertar**: o Sistema avisa que o tipo informado é diferente do tipo da viagem no **TOL** e o usuário define se permite o vínculo ou não.
* Se o parâmetro estiver igual a **Branco**, o **help OMS200ASSVEI** não será apresentado, pois a validação não será ativada quando for informado um valor diferente de **1 ou 2**.

**Saiba mais**Mais informações poderão ser acessadas no *link*: [Integração TOTVS OMS x TOTVS Otimização Logística](https://tdn.totvs.com/pages/releaseview.action?pageId=268801735)
