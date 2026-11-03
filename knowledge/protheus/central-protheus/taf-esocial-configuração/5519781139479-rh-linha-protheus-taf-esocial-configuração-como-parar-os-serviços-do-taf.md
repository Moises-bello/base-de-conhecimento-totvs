---
article_id: 5519781139479
category: TAF - eSocial - Configuração
content_hash: 6ee905bf85414d9a94b044b1f1cde1f2b8eaed3eba70e30508edbca4eb6b4102
fetched_at: '2026-06-28T22:45:14.459270+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial  - Configuração - Como parar os serviços
  do TAF
type: support-article
updated_at: '2026-06-25T12:33:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5519781139479-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Como-parar-os-servi%C3%A7os-do-TAF
---

**Dúvida**Como parar os serviços do TAF  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Configuração - Todas as versões  
  
**Solução**

1 - Para que os serviços do Protheus sejam parados existem alguns processos para que seja completado a execução de acordo com o seu sistema operacional e ou servidor;

2 - Acesse o Gerenciador de Tarefas no Windows na aba serviços botão direito e parar o serviço:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519685777943)

3 - Se caso o serviço ainda não parar, basta acessar a aba Processos, aba Processos e nos processos em segundo plano procurar pelo serviço responsável e clicar em Finalizar tarefa:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519721764631)

4 - Outro processo que pode acontecer é parar o serviço via prompt de comando (CMD). Acesse a aba serviços procure o nome do serviço e grave o número do PID:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519731518359)

5 - Acesse o prompt de comando (CMD) e digite o seguinte comando taskkill /pid numero\_pid /f e aperte ENTER para que o serviço seja parado:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5519753990295)
