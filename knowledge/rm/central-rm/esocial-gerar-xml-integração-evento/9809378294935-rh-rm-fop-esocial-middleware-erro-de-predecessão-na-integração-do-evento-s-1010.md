---
article_id: 9809378294935
category: eSocial - Gerar XML/ Integração Evento
content_hash: f9cc941d811a0f9f56c4853ead8986570a856fb448813cb0af2a3a9977726a31
fetched_at: '2026-06-28T22:47:13.079500+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Middleware - Erro de Predecessão na integração do
  evento S-1010 com o Governo
type: support-article
updated_at: '2024-06-17T13:10:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9809378294935-RH-RM-FOP-eSocial-Middleware-Erro-de-Predecess%C3%A3o-na-integra%C3%A7%C3%A3o-do-evento-S-1010-com-o-Governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao transmitir o evento S-1010 é apresentada a mensagem **Erro de predecessão ao enviar o evento S-1010 - ID IDXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX: Necessário enviar primeiramente o evento S-1010 de inclusão/carga inicial!****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse incidente ocorre quando é enviado o evento S-1010 com o Tipo de Operação **Alteração** e não há na Fila de Eventos o registro do evento S-1010 com o Tipo de Operação **Inclusão/Carga inicial.**  
  
**Solução**Para solucionar essa ocorrência, há duas alternativas:  
• **Desativar Predecessão** de Eventos  
1. Acesse **Configurações | Parametrizador | eSocial | Integração com Middleware | Outros Parâmetros** e marque a flag **Desativar predecessão de envio de eventos**, assim não será exigido o evento S-1010 na fila de eventos para transmiti-lo. 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9178381219991/mceclip0.png)

2. Em seguida, gere o XML do evento  S-1010  e transmita ao eSocial.  
  
**• S-1010 sem recibo**Se o evento S-1010  já estiver no eSocial mas não possuir número de recibo no RM, será necessário ajustar o recibo diretamente no evento. Para isso, acesse **Esocial | Fila de Eventos** e edite o evento que corresponde ao que está no ambiente do Governo.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9939675881879)

• **Tipo** de **Operação incorreto**  
1. Se  não existir o evento de **Inclusão/Carga inicial** no eSocial Web, este não será aceito. Sendo assim, deverá verificar a necessidade de incluir um novo manualmente com o Tipo de Operação Inclusão na Fila de Eventos. Para isso, acesse **Esocial | Fila de Eventos**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9811431909911)

2. Clique no botão **Incluir** e preenchas os dados da Rubrica com o **Tipo de Operação** inclusão e **Competência** desejado.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9811528717207)

3. Em seguida, gere o XML e envie ao eSocial.
