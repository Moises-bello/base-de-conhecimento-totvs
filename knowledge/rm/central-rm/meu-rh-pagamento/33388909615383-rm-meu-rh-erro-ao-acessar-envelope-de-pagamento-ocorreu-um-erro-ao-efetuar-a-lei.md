---
article_id: 33388909615383
category: Meu RH - Pagamento
content_hash: 6f2077b9a2c5207fd2cf7a9a5c482f8d0f7f314034fb7aef0ff12e4a4778a9b6
fetched_at: '2026-06-28T22:47:33.854007+00:00'
product: rm
section_id: 1500000835221
source: central-rm
title: 'RM - Meu RH - Erro ao acessar envelope de pagamento Ocorreu um erro ao efetuar
  a leitura do resgistro: Object reference not set to an instance of object'
type: support-article
updated_at: '2025-07-14T17:18:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33388909615383-RM-Meu-RH-Erro-ao-acessar-envelope-de-pagamento-Ocorreu-um-erro-ao-efetuar-a-leitura-do-resgistro-Object-reference-not-set-to-an-instance-of-object
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33388909594135) Tempo aproximado para leitura: **00:02:24 min**  
  
**Ocorrência**  
Ao acessar o envelope de pagamento no Meu RH é apresentado a mensagem de erro " **Ocorreu um erro ao efetuar a leitura do registro: Object reference not set to an instance of object**. "  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33388909595031)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Eventos no envelope de pagamento sem ter o campo chave preenchido corretamente.  
  
**Solução**  
Basta acessar o envelope de pagamento do colaborador e então verificar se em algum evento o campo chave não esta preenchido .

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33388880260375)

Você também pode realizar uma consulta SQL para verificar todos os eventos:

**Select chave, codigo from pevento order by chave**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33388909598487)

Caso algum evento apresente o campo vazio ou NULL você deve acessar este evento e então preencher esta informação.
