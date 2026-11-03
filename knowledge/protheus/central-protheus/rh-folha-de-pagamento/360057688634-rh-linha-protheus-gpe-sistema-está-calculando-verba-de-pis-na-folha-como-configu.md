---
article_id: 360057688634
category: RH - Folha de Pagamento
content_hash: 220f232ea579c6d91237014387832bf2c83e2672b1aee46e0fab2edc93b7cca3
fetched_at: '2026-06-28T22:44:16.374836+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema está calculando verba de PIS na folha,
  como configurar para que não calcule
type: support-article
updated_at: '2025-08-22T19:26:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057688634-RH-Linha-Protheus-GPE-Sistema-est%C3%A1-calculando-verba-de-PIS-na-folha-como-configurar-para-que-n%C3%A3o-calcule
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26355732489623)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Sistema está calculando verba de PIS na folha, como configurar para que não calcule?  
  
**Ambiente**TOTVS RH - TOTVS TH (Linha Protheus) GPE Gestão de Pessoal - Todas as versões  
  
**Solução**Para gerar o PIS no cálculo, o Sistema verifica as verbas que estão com **sim** para PIS no cadastro de verbas, aba incidências.

Assim, para que não seja calculada essa verba, execute o processo abaixo:   
  
1. Acesse Consultas - Cadastros - Genéricos;  
2. Localize a tabela de verbas - SRV;  
3. Faça um filtro: **PIS igual a S**, adicione o filtro e confirme;  
4. Verifique e anote quais as verbas estão sendo listadas. Estas são as que estão configuradas com sim para Pis;  
5. Para que não gere na folha o PIS, entre no cadastro de cada uma das verbas que foi listada e altere o campo PIS para **não;**6. Depois disso, cancele o cálculo feito anteriormente e faça novamente.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
