---
article_id: 9198951795863
category: eSocial - Tabelas/Não Periódicos
content_hash: 45107575f179f7ddff305fd1bd45d4488040e216ab4e551fbe64e246ddb6a5ef
fetched_at: '2026-06-28T22:47:10.426312+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na integração com governo: A inclusão de novo
  período de validade de uma rubrica vigente não pode ter todos os atributos idênticos
  ao período imediatamente anterior'
type: support-article
updated_at: '2024-12-30T13:59:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9198951795863-RH-RM-FOP-eSocial-Erro-na-integra%C3%A7%C3%A3o-com-governo-A-inclus%C3%A3o-de-novo-per%C3%ADodo-de-validade-de-uma-rubrica-vigente-n%C3%A3o-pode-ter-todos-os-atributos-id%C3%AAnticos-ao-per%C3%ADodo-imediatamente-anterior
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min****Ocorrência**Ao transmitir o evento S-1010 para o governo é retornado a inconsistência **Erro 1505 - Evento inválido. A inclusão de novo período de validade de uma rubrica vigente não pode ter todos os atributos idênticos ao período imediatamente anterior**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**Esse incidente ocorre quando envia o evento S-1010 com os dados que já existe no ambiente do Governo.

*Regra de Validação Leiaute S-1.0*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9300636438039/mceclip0.png)

**Solução**Para correção da ocorrência favor realizar as validações abaixo:  
• **Exclusão** de evento indevido  
1.  Acesse  **Esocial | Fila de Eventos** e  inclua um gatilho manualmente do S-1010 do evento que necessita excluir no eSocial com tipo de operação de **exclusão** e a competência deverá ser a vigência que iniciou no eSocial.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9203522976535/mceclip3.png)

2. Após o evento S-1010 de exclusão estiver com o status Aceito RET, poderá enviar o novo de inclusão com a competência desejada.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9304463831447/mceclip1.png)

• **Alteração** de dados no S-1010  
1. Acesse novamente a **Fila de Eventos** e gere o evento e envie como **alteração**e a competência deverá ser a vigência que iniciou no eSocial.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9304569813143/mceclip2.png)

2. Após gere o XML e envie ao eSocial.
