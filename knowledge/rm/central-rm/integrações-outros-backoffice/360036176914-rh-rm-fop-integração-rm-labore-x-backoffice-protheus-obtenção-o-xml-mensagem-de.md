---
article_id: 360036176914
category: Integrações Outros BackOffice
content_hash: 27d69d114b274b413bac4238d0aaa4fd6491b7fc24aa76c0b3e0a090becb8d7f
fetched_at: '2026-06-28T22:46:42.198475+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: 'RH - RM - FOP - Integração RM Labore x BackOffice Protheus: Obtenção o XML
  mensagem de Resposta e Transformada no RM'
type: support-article
updated_at: '2025-02-10T16:39:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036176914-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Obten%C3%A7%C3%A3o-o-XML-mensagem-de-Resposta-e-Transformada-no-RM
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:28 min  
  
Dúvida**Como obter o XML mensagem de Resposta e Transformada no RM?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para obter o XML  mensagem de resposta e transforma do RM, realize os passos abaixo:

**Caso utilize o EAI 2.0:**

1. Acesse o módulo **Integrações | aba EAI 2.0 | Gerenciamento de Mensagens.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5523581984791/mceclip1.png)

2. Selecione o registro que apresentou erro e apresentará duas mensagens para o mesmo adapter existindo a **BusinessMessage** e a **Response**.

3. Para obter a mensagem Transformada, edite a **BusinessMessage** e selecione a aba **Dados da execução.**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5523593686295/mceclip3.png)

4. Para obter a mensagem **Resposta**, edite a **Response**e obtenha através da aba **Dados da mensagem.**  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5523684826391/mceclip4.png)

**Caso utilize o EAI 1.0**  
1. Acesse o módulo **Integrações | aba Integrações | Mensagem Única | Fila de mensagens únicas:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048216853/mceclip0.png)

2. Selecione o registro que apresentou erro e acesse **Anexos | Informação de execução de mensagem:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047328814/mceclip1.png)

3. Caso os campos **Mensagem Transformada** e **Mensagem de Resposta** tenham informação, clique no ícone [...] para obter o XML de cada mensagem.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048217473/mceclip2.png)

**Saiba mais**  
Para consulta do manual de integração RM Labore x Protheus [clique Aqui](https://tdn.totvs.com/display/public/INT/Manual_Doc_Integracao_RMLabore_BackOfficeProtheus).
