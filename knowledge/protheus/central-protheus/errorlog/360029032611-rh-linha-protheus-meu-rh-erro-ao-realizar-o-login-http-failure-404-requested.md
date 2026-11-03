---
article_id: 360029032611
category: ERRORLOG
content_hash: 23106d1cbd26a73eb14e682a05d50a5981215ac13e17d619ab1003eecc14418c
fetched_at: '2026-06-28T22:44:39.506918+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Erro ao realizar o login - Http failure 404
  Requested
type: support-article
updated_at: '2026-06-18T18:37:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029032611-RH-Linha-Protheus-MEU-RH-Erro-ao-realizar-o-login-Http-failure-404-Requested
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**O que ajustar quando apresenta o erro ao acessar o Meu RH "**Http failure response for ... auth/isLogged: 404 Requested file not found**"?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8837392896663/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – Todas às versões  
  
**Solução**Verifique se a porta indicada no arquivo PROPERTIES.JSON está correta. Na "**baseUrl**" deve conter a porta do **REST** e não a porta **HTTP**.  
  
**IMPORTANTE:** Após qualquer alteração no seu **APPSERVER.INI** ou **PROPERTIES.JSON** é obrigatório que limpe o cache de memória do seu Navegador ou Aplicativo.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8837634342039/mceclip3.png)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8837566040343/mceclip2.png)  
  
Será necessário também que seja gerado novo **QRCode** aplicando as alterações efetuadas para que consiga acessar o MEU RH via aplicativo. Caso tenha dúvidas, verifique o documento abaixo onde demonstram as informações que devem ser incluídas no **QRCode**.  
  
[RH - Linha Protheus - MEU RH - Como configurar o APPSERVER.INI, PROPERTIES.JSON e URL do QRCODE para acesso ao MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044715514)  
  
**Realizou os passos desse artigo e o problema persiste?**Neste caso, por gentileza, abra um Ticket para o Suporte Técnico, explique o seu cenário, informe se o erro ocorre no acesso via navegador ou aplicativo e encaminhe seus arquivos **APPSERVER.INI**,  **PROPERTIES.JSON** e **CONSOLE.LOG.**  
  
[RH - Linha Protheus - MEU RH - Como gerar o Console.log para análise de erros do MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416746889751)  
  
**Saiba Mais**  
**[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**[para acessar mais artigos e FAQs sobre o MEU RH](%20https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH) **[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**[para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
