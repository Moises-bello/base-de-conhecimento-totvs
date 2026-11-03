---
article_id: 11337332768791
category: eSocial - Middleware
content_hash: e3802cd9ec14694a0f4e86558c1ca6ff35b674694591d2133e4c360f731b410a
fetched_at: '2026-06-28T22:47:05.536198+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware: Ajuste de recibo do eSocial'
type: support-article
updated_at: '2026-04-30T21:30:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11337332768791-RH-RM-FOP-eSocial-Middleware-Ajuste-de-recibo-do-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20822695545495) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como ajustar recibo no Middleware?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
O Middleware permite realizar a inclusão ou alteração de Recibo do eSocial do evento na Fila de Eventos manualmente. Abaixo passos para realizar tal ajuste:

1. Acesse o **portal do e-Social**, localize o evento em questão;

2. Localize o número de recibo do evento e copie o mesmo;  
3. Na fila de eventos, selecione o evento desejado e preencha o campo **Recibo** e salve.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11337131886359)

**Importante**  
É possível realizar o ajuste do campo **Recibo** somente para eventos com Status diferente de aceito e ou excluído **RET/TAF**. Caso necessário realizar a alteração do ***Status*** **do Evento** e ou do campo **Recibo** (onde o campo esteja bloqueado)tal alteração deverá ser realizada via *UPDATE* no Banco de Dados. Lembrando que tal *UPDATE* não se enquadra no escopo de atendimento do suporte padrão, devendo ser realizado pela própria empresa ou com o auxílio da equipe de consultoria técnica.

Tabela: PESOCIALEVENTOS   
Campos: RECIBO, STATUS
