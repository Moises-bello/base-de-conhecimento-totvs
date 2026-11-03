---
article_id: 6273474953879
category: eSocial - Parametrizador
content_hash: 6b7b1ead9a0fdf4c96da8eceb94d7b0e751a7241049db5b8c8a823c6e5effb74
fetched_at: '2026-06-28T22:47:06.314798+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: RH - RM - FOP - eSocial - Erro 403 na transmissão de eventos - Leiaute do evento
  inválido
type: support-article
updated_at: '2025-02-04T11:36:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6273474953879-RH-RM-FOP-eSocial-Erro-403-na-transmiss%C3%A3o-de-eventos-Leiaute-do-evento-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29737553123863) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao transmitir eventos para o governo é retornado a inconsistência **Código da Resposta:** **403 - Leiaute do evento inválido.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6276661698455)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O término de convivência entre as versões S-1.2 e S-1.3 se encerrou no dia 02/02/2025. Sendo assim, o erro é apresentado quando são enviados eventos no leiaute S-1.2 após essa data.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Altere o leiaute do RM conforme documentação abaixo;  
     [RH - RM - FOP - eSocial - Alteração da versão do leiaute do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020185152-RH-RM-FOP-eSocial-Altera%C3%A7%C3%A3o-da-vers%C3%A3o-do-leiaute-do-eSocial)  
  
2. Caso utilize TAF, será necessário alterar também o leiaute no TAF. Caso utilize o Middleware, ignore esse passo;  
    [RH - Linha Protheus - TAF - eSocial - Atualização - Como atualizar a versão do layout no TAF E-social?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18585564590999)  
  
3. Após alteração do leiaute, gere novamente o XML e integre com o governo.  
  
**Saiba mais**Para mais informações, acesse:     - [RH - RM - FOP - eSocial - Leiaute S-1.3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26091695488919)
