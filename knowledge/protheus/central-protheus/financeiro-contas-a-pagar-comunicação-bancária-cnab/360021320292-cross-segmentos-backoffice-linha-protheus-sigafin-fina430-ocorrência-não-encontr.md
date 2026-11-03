---
article_id: 360021320292
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 192de5210dcb40e150f7423a64302e95d50901510ca2d587d42ce8d27213168f
fetched_at: '2026-06-28T22:37:55.060259+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA430- Ocorrência
  não encontrada
type: support-article
updated_at: '2024-01-24T17:04:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021320292-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA430-Ocorr%C3%AAncia-n%C3%A3o-encontrada
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20770946711063)****Tempo aproximado para leitura: ****00:05:00 min**  
  
Ocorrência:**Ao executar rotina de retorno de pagamentos **FINA430** é apresentada a mensagem de **ocorrência não encontrada**.  
  
**Ambiente:**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro - Todas as versões  
  
**Causa:**Esse incidente ocorre, pois a ocorrência realmente não está cadastrada ou o tipo da ocorrência (**EB\_TIPO**) foi informado de maneira incorreta. vale lembrar que para o **CNAB** a **Pagar** , o tipo deve ser sempre  **P(Contas a Pagar).**  
  
**Solução:**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Abra o Protheus **modulo 06 FINANCEIRO**;  
2. Acesse o menu **Atualizações** > **Cadastros** >**Ocorrências CNAB**;  
3. Ajuste o tipo de ocorrência para **P** (**Contas a Pagar**)
