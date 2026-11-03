---
article_id: 360018852571
category: RH - Folha de Pagamento
content_hash: 001b1adf59bc7433ea5a5e3eddd36d403c0c8cbb0db405d12930acd032f06084
fetched_at: '2026-06-28T22:44:16.371728+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema está calculando periculosidade sobre verbas
  para funcionário afastado por todo o período
type: support-article
updated_at: '2025-06-16T18:27:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018852571-RH-Linha-Protheus-GPE-Sistema-est%C3%A1-calculando-periculosidade-sobre-verbas-para-funcion%C3%A1rio-afastado-por-todo-o-per%C3%ADodo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26105172165143)Tempo aproximado para leitura:00:02:30 min***

**Ocorrência**No módulo Gestão de Pessoal, o sistema está calculando periculosidade sobre verbas para funcionário afastado por todo o período  
  
**Ambiente**Microsiga Protheus - Gestão de Pessoal - Todas as versões 

**Causa**Quando no cadastro do sindicato está configurado para periculosidade sobre verbas o sistema calcula a verba com ID 1281 indevidamente, porém, se no cadastro do sindicato estiver com periculosidade sobre salario, o sistema não calcula valor da periculosidade (ID 0036).  
  
**Solução**Efetuado ajuste para que cálculo da periculosidade não ocorra se não existir verbas pagas.  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Realize o *backup* prévio;  
  
2. Aplique o pacote de atualização;

**12.1.2210** <https://suporte.totvs.com/portal/p/10098/download?e=1080347>  
**12.1.2310** <https://suporte.totvs.com/portal/p/10098/download?e=1123885>  
**12.1.2410** <https://suporte.totvs.com/portal/p/10098/download?e=1170810>  
  
3. Refaça o teste.  
  
**Saiba Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
