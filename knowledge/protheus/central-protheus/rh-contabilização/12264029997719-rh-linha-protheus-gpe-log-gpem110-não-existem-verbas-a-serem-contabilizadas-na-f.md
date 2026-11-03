---
article_id: 12264029997719
category: RH - Contabilização
content_hash: 724156c9c72dde7d53dd7c091cfb5784731718534cea258a710e7154fc5c57bc
fetched_at: '2026-06-28T22:43:45.981349+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: 'RH - Linha Protheus - GPE - LOG GPEM110: Não existem verbas a serem contabilizadas
  na filial'
type: support-article
updated_at: '2025-07-23T20:15:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12264029997719-RH-Linha-Protheus-GPE-LOG-GPEM110-N%C3%A3o-existem-verbas-a-serem-contabilizadas-na-filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33671880258199) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**No processamento da contabilização na rotina GPEM110, é apresentado um LOG : Não existem verbas a serem contabilizadas na filial  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12271828181399)   
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Ausência de cálculo ou ausência/erro na configuração dos lançamentos padrões  
  
**Solução**  
Para solucionar essa ocorrência, verifique as seguintes e os seguintes passos:  
  
1. Verifique se há cálculo de folha, provisão ou ambas para a competência informada.  
  
2. Verifique em uma das verbas que são apresentadas na consulta de cálculo ou relatório , se possui lançamento padrão atrelado, na Aba contabilização no cadastro de verbas.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12266355836055)  
  
3. Caso possua lançamento padrão , verifique se após o processamento da contabilização as verbas são gravadas na tabela SRZ.

4. Realize um teste criando um lançamento padrão conforme documentação abaixo e atrelando à uma das verbas que apresentam-se no cálculo. Em seguida refaça o processo de contabilização.

[RH - Linha Protheus - GPE - Como configurar Lançamento Padrão para Folha de Pagamento do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021101152-RH-Linha-Protheus-GPE-Como-configurar-Lan%C3%A7amento-Padr%C3%A3o-para-Folha-de-Pagamento-do-Protheus-)

**Observação:**

Caso ocorra o processamento da contabilização com a realização do passo 4, será necessário reavaliar as fórmulas dos lançamentos padrões criados , de modo que conclua o processamento e siga a regra de negócio da empresa , respeitando as devidas contas contábeis.

**Saiba Mais:**  
[Página Centralizadora da Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o)
