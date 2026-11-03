---
article_id: 6304331983127
category: eSocial - Gerar XML/ Integração Evento
content_hash: b5c2f683b76cd458712c2d85dade6e9c3477b08b754aa3584d17f5817af382fe
fetched_at: '2026-06-28T22:47:12.253780+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Erro ao transmitir eventos ao Governo - O evento
  ID 'IDXXXXXXXXXXXXXXXXXXXXXXXXXXXX' foi rejeitado pelo RET
type: support-article
updated_at: '2025-04-10T13:44:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6304331983127-RH-RM-FOP-eSocial-Erro-ao-transmitir-eventos-ao-Governo-O-evento-ID-IDXXXXXXXXXXXXXXXXXXXXXXXXXXXX-foi-rejeitado-pelo-RET
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484524334231) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Após eventos serem rejeitados pelo RET, no menu **Retorno da Integração** é apresentada a mensagem **O evento ID 'IDXXXXXXXXXXXXXXXXXXXXXXXXXXXX' foi rejeitado pelo RET.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6304452035735)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**O erro supracitado pode ocorrer por vários motivos, sendo o mais comum é quando o governo não recepciona mais os eventos no leiaute do XML que está tentando integrar.   
A seguir passo a passo para identificar o código e mensagem de erro enviado pelo Governo.

1. Acesse o banco de dados do TSS e realize a consulta SELECT \* FROM SPED400 WHERE CHAVE = '**informe o I****D do evento**';  
2. No resultado da consulta, verifique no campo **CODRECEITA** e **DSCRECEITA** a mensagem retornada pelo RET.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6305340690071)  
3. Para obter a solução da mensagem de inconsistência, poderá abrir uma solicitação em nosso canal de atendimento.

**Saiba mais:**- [Alteração da versão do leiaute do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020185152-RH-RM-FOP-eSocial-Altera%C3%A7%C3%A3o-da-vers%C3%A3o-do-leiaute-do-eSocial)
