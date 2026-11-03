---
article_id: 360000533207
category: RH – DIRF
content_hash: 893bb753f0d3b240941ee0053a1fc11ac094d04bb0ec4fcf79c29e622d80dee0
fetched_at: '2026-06-28T22:44:06.848454+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o plano de saúde para carregar
  os dados utilizados na DIRF
type: support-article
updated_at: '2025-08-21T12:50:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000533207-RH-Linha-Protheus-GPE-Como-configurar-o-plano-de-sa%C3%BAde-para-carregar-os-dados-utilizados-na-DIRF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34341417553303)**Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**  
Como configurar o plano de saúde para carregar os dados utilizados na DIRF?  
   
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
1. A verba de desconto plano de saúde deve ter incidência **R** para a DIRF na aba **Anuais**, caminho da rotina **>Atualizações >Definições de cálculos >Verbas:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11133990885911)​  
  
2**.** Cadastre o fornecedor do plano de saúde nas tabelas **S016 e S017** da rotina **Manutenção de Tabelas**, pelo caminho **>Atualizações >Definições de cálculos >Manutenção Tabelas;**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11133996762647)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11134026338583)  
​  
3. Cadastre os planos na rotina Planos de Saúde Ativos pelo caminho **>Atualizações >Benefícios >Plano de saúde > Plano de Saúde Ativos:**  
![](https://totvssuporte.zendesk.com/attachments/token/qoDpeaeCuMeIRZxNE3aUk4Abe/?name=inline-1156508987.png)  
  
4. Calcule o plano de saúde pelo caminho **>Atualizações >Benefícios >Plano de saúde > Cálculos Planos de Saúde:**  
![](https://totvssuporte.zendesk.com/attachments/token/UU8zC5IuH8kuuH95qeBBL1HvF/?name=inline634793311.png)  
  
5. Consulte se o cálculo foi realizado pelo caminho **>Atualizações >Benefícios >Plano de saúde >Relatório de cálculos**;  
​  
6. **Integre** o cálculo com a folha pelo caminho **>Atualizações >Benefícios >Plano de saúde >** Integrações;  
​  
7. Após cálculo e conferência na folha de pagamento, faça o fechamento do roteiro PLA pelo caminho **>Atualizações >Benefícios >Plano de saúde >Fechamento:​**  
![](https://totvssuporte.zendesk.com/attachments/token/j4sn83WfAtiyOCT63BwUWx60b/?name=inline644402111.png)  
  
8. O fechamento do cálculo do plano de saúde gravou os dados na **RHS - Histórico Planos de Saúde e RHP - Histórico co-partic./Reembolso.**  
![](https://totvssuporte.zendesk.com/attachments/token/r2nzzmgbKbhYTJ2iNH8M8VIdl/?name=inline-820675741.png)​​​  
  
  
**Saiba mais**  
[RH - Linha Protheus - GPE - Como realizar a conferência do plano de saúde, coparticipação e reembolso para a DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022836972)  
[RH - Linha Protheus - GPE - Quando os planos de saúde são informados manualmente para o funcionário o que fazer para DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021563052)
