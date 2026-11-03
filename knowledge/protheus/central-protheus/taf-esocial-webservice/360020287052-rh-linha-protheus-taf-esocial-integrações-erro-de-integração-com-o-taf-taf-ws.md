---
article_id: 360020287052
category: TAF - eSocial - WebService
content_hash: 37d13263a8f36fca6109fbdfb862b0f10647bc0e9d8b22823eacb7f5ab08fbd1
fetched_at: '2026-06-28T22:45:15.212212+00:00'
product: protheus
section_id: 1500001536741
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Integrações  - Erro de integração com
  o TAF (TAF-WS)
type: support-article
updated_at: '2026-06-26T12:01:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020287052-RH-Linha-Protheus-TAF-eSocial-Integra%C3%A7%C3%B5es-Erro-de-integra%C3%A7%C3%A3o-com-o-TAF-TAF-WS
---

**Dúvida**Quais os procedimentos de utilização e configuração da Web Service REST - Integração com o TAF quando houver erro de integração? **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - Todas as Versões.  
  
**Solução**

1 - Verifique se o TAF-WS está ativo, e se não estiver basta iniciar. Caso esteja com o serviço em execução, reinicie. Se tiver dificuldades em parar o TAF-WS siga o procedimento abaixo:

[RH - Linha Protheus - TAF - SERVIÇOS - Como parar o serviço TAF-WS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036631673-TAF-SERVI%C3%87OS-Como-parar-o-servi%C3%A7o-TAF-WS)

2 - Se o problema não resolveu no passo anterior, precisa verificar a conexão com o DBAccess. Acesse a pasta do DBAccess e abra o arquivo dbaccess.ini e verifique qual a porta utilizada na seção [GENERAL] e qual *alias* está configurado conforme exemplo abaixo:

**Exemplo:**

*\*Favor não copiar as informações do exemplo abaixo!!!*

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405147193879)

3 - Em seguida acesse a pasta de instalação do TAF, vá nas pastas bin/app e abre o arquivo appserver.ini e verifique a seção [TOPCONNECT] e procure a porta e o alias se estão iguais com as configurações conforme abaixo:

**Exemplo:**

*\*Favor não copiar as informações do exemplo abaixo!!!*  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405132828951)

Se modificar as configurações acima, reinicie o TAF-WS.

4 - Persistindo o problema de integração, peço que acessa novamente a pasta do DBAccess e localize a pasta *client:*

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405134476695)

5 - Acesse a pasta *client* e copie o arquivo dbapi.dll:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405151804439)

6 - Acessa a pasta do TAF e vá em bin/app e localize o outro arquivo dbapi.dll e faça um backup deste arquivo e em seguida cole o arquivo copiado da pasta do dbaccess. Reinicie o TAF-WS e faça uma nova integração.

7 - Se ainda permanecer com os problemas de comunicação entre o seu ERP e o TAF, verifique com o time de infra (TI) se o IP e Porta do REST (Servidor) está comunicável com o Host (Máquina de usuário). Se for o caso, peço que abram um chamado na TOTVS e nos enviem os arquivos APPSERVER.INI e CONSOLE.LOG da pasta bin/app para validarmos o cenário.
