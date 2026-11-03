---
article_id: 360050318634
category: RH - Folha de Pagamento
content_hash: a89a2eac3b7c044bb9f9d3867ea1b4d93101061fe43c8daa87ce3391735ac54b
fetched_at: '2026-06-28T22:44:16.360505+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema calcula provento de insuficiência de saldo
  e liquido na folha de pagamento e/ou rescisão
type: support-article
updated_at: '2024-09-05T18:19:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050318634-RH-Linha-Protheus-GPE-Sistema-calcula-provento-de-insufici%C3%AAncia-de-saldo-e-liquido-na-folha-de-pagamento-e-ou-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26158819013143) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Sistema calcula provento de insuficiência de saldo e liquido de pagamento, o que verificar neste caso?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da Versão 11.8.  
  
**Solução**Quando o sistema calcula uma verba de provento de insuficiência de saldo (ID 0045) e liquido de pagamento (0047) é porque alguma verba de provento esta como Pagamento Obrigatório, sendo assim o sistema calculará um liquido de no mínimo o mesmo valor desta verba.  
  
Mas como identificar a verba que esta como pagamento obrigatório? Abaixo exemplo:  
Geralmente nesses casos, o liquido fica no mesmo valor da verba de pagamento obrigatório:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076898614)  
Então no caso acima, a verba com pagamento obrigatório é a 013.  
  
Caso ela não tenha que ser pagamento obrigatório, entre no cadastro da Verba em **Atualizações > Definições de Cálculos > Verbas (GPEA040)** e **Altere** o campo abaixo para **N-Não:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078049193)

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
