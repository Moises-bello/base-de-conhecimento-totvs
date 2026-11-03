---
article_id: 6301696239255
category: eSocial - Gerar XML/ Integração Evento
content_hash: 269aa90f05402a0026a3098fb48c2aa315b5fd1cefb7f056039843c0e398ca4b
fetched_at: '2026-06-28T22:47:12.248427+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao transmitir eventos ao Governo - Código do
  erro: 000'
type: support-article
updated_at: '2024-12-18T15:49:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6301696239255-RH-RM-FOP-eSocial-Erro-ao-transmitir-eventos-ao-Governo-C%C3%B3digo-do-erro-000
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24161073800343) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Após eventos serem rejeitados pelo RET, na opção **Visualizar Inconsistência RET** é apresentada a mensagem de erro**Código do erro: 000 Descrição:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6301548969367)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Causa**Geralmente o erro ocorre quando está tentando transmitir eventos que o leiaute já encontra-se expirado.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Altere o leiaute do RM conforme documentação abaixo;  
    [RH - RM - FOP - eSocial - Alteração da versão do leiaute do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020185152-RH-RM-FOP-eSocial-Altera%C3%A7%C3%A3o-da-vers%C3%A3o-do-leiaute-do-eSocial)  
  
2. Caso utilize TAF, será necessário alterar também o leiaute no TAF. Caso utilize o Middleware, ignore  esse passo;  
  
3. Após alteração do leiaute, gere novamente o XML e integre com o governo.
