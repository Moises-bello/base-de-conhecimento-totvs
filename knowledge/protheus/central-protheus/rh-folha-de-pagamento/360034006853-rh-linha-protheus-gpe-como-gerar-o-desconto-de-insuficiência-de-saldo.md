---
article_id: 360034006853
category: RH - Folha de Pagamento
content_hash: 430c83415e08a83289a0b13db0a3f8821943ec5ddb32bced34fc0983893a380a
fetched_at: '2026-06-28T22:44:13.537172+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar o desconto de insuficiência de saldo
type: support-article
updated_at: '2024-09-10T20:59:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034006853-RH-Linha-Protheus-GPE-Como-gerar-o-desconto-de-insufici%C3%AAncia-de-saldo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26282197707927)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como gerar o desconto de insuficiência de saldo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para que o sistema calcule o desconto de insuficiência de saldo no mês seguinte é necessário que a verba de provento de insuficiência de saldo (**ID 0045**) esteja com o campo **RV\_CODMSEG** preenchido com o código da verba relacionada ao **identificador de cálculo 0046**, conforme o cadastro de verbas abaixo:  
Provento  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101261433)  
  
Desconto  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099038934)  
  
**Atenção**Caso tenha efetuado o **fechamento do período** **sem ter configurado as verbas** conforme explicação acima terá que lançar a verba de desconto de insuficiência de saldo (ID 0046) na tabela RGB preenchendo o campo RGB\_DTREF com a data de referência que foi gerada a insuficiência de saldo. O campo RGB\_PERIODO deve ser preenchido com a data de referência do período em aberto (período que irá gerar o provento de insuficiência de saldo).  
  
**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
