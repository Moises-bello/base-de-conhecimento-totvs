---
article_id: 4416746889751
category: ERRORLOG
content_hash: 8536f04385a14fda5bff7eb5b04bac69de9db9e0ebe036cb7cedfb66f7f8bf7d
fetched_at: '2026-06-28T22:44:39.492284+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como gerar o Console.log para análise de erros
  do MEU RH
type: support-article
updated_at: '2026-06-19T17:03:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416746889751-RH-Linha-Protheus-MEU-RH-Como-gerar-o-Console-log-para-an%C3%A1lise-de-erros-do-MEU-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24770059374999) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como gerar o **console.log** para análise do Suporte?  
  
**Ambiente**TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**Em algumas situações o Suporte irá solicitar para análise o arquivo **Console.log,** para analisar por exemplo quando a tela do MEU RH fica Congelada/Travada/Branca ao acessá-lo via Navegador ou APP ou até mesmo algum error log relacionado ao acessar determinada rotina.  
  
Para uma análise mais assertiva é importante:  
  
1- Acessar a pasta **appserver** do ambiente do **MEU RH;**2 - **Renomear** o arquivo **Console.log** existente;  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416746451095)  
  
3 - Acessar o **MEU RH** novamente para gerar o erro;  
  
4 - Copiar o novo arquivo **Console.log** gerado e anexar ao *Ticket* do Suporte;  
  
5 - Importante verificar se o serviço **REST** está sendo executado e apresentado no **console.log** conforme imagem abaixo:  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416739319063)  
  
6 - Caso seja possível efetuar o login no MEU RH, no **console.log** aparecerá a seguinte autenticação:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416746619031)  
  
7 - Exemplo de como é apresentado no **console.log** quando **não** é efetuada a autenticação do usuário:  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4416739574551)  
  
**Saiba Mais**  
**[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**[para acessar mais artigos e FAQs sobre o MEU RH](%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH) **[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**[para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
