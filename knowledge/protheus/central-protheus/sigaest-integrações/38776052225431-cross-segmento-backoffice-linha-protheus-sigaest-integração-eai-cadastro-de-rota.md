---
article_id: 38776052225431
category: SIGAEST - INTEGRAÇÕES
content_hash: 964bd62b13e37319566d6d58da79811538545494575cdacbb770685c87ecb8fa
fetched_at: '2026-06-28T22:38:46.174065+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Integração EAI: Cadastro
  de Rotas'
type: support-article
updated_at: '2026-03-24T13:43:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38776052225431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Integra%C3%A7%C3%A3o-EAI-Cadastro-de-Rotas
---

O Cadastro de Rotas EAI (APCFG021) no Protheus é essencial para integrações via Mensagem Única, permitindo definir o serviço (SOAP ou REST) usado para enviar mensagens ao sistema integrado. É necessário informar o endereço, usuário e senha do serviço de destino, que será utilizado nos Adapters para envio das informações integradas.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38776052217751) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como funciona e para que serve o Cadastro de Rotas EAI (APCFG021)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Solução**  
Para o processo de Integração via Mensagem Única um dos cadastros essenciais é o Cadastro de Rotas EAI (APCFG021). Nele é possível indicar o Serviço que será utilizado para envio de mensagens ao sistema integrado.

Veja um vídeo do processo:

[![Cadastro de Rotas.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39256367767063)](https://youtu.be/d8yNi3_73T8?si=ZRGmTY0zEeofoBdo)

Os campos importantes neste cadastro são:

* Canal env (XB9\_CONVJ): Este campo define o tipo de Serviço que o sistema utilizará para comunicação. Nas integrações com o Backoffice Protheus podemos ter:
  + SOAP: Integração via WebServices ([**Webservices no Protheus**](https://tdn.totvs.com/x/qQlRCg))
  + REST: Integração via REST ([**Rest no Protheus**](https://tdn.totvs.com/x/nhHvGQ))

Dependendo do canal selecionado, na aba correspondente deve ser inserido o endereço do serviço do sistema de destino para onde o Protheus fará o envio da informação, o usuário e senha com acesso ao serviço:

![Rotas EAI.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38776052218007)

Agora basta informar esta rota nos Adapters da integração e o sistema irá considerá-la no envio das informações integradas.

***Saiba mais:***

[*Clique aqui e veja mais artigos sobre Integrações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)
