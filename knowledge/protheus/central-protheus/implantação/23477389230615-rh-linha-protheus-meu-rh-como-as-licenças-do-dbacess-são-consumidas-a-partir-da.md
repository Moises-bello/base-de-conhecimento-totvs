---
article_id: 23477389230615
category: IMPLANTAÇÃO
content_hash: 197e28349e0331c6831e42c244dfb690d2aaf77456f03989a537ebe46b61790e
fetched_at: '2026-06-28T22:44:33.340222+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - Meu RH - Como as licenças do DBAcess são consumidas a
  partir da distribuição das licenças do App Meu RH / REST
type: support-article
updated_at: '2026-06-23T21:08:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23477389230615-RH-Linha-Protheus-Meu-RH-Como-as-licen%C3%A7as-do-DBAcess-s%C3%A3o-consumidas-a-partir-da-distribui%C3%A7%C3%A3o-das-licen%C3%A7as-do-App-Meu-RH-REST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23477420306455) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como as licenças do *DBAcess* são consumidas a partir da distribuição das licenças do App Meu RH / *REST*  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**Na abertura de uma rotina, na qual **haja consumo de licenças**, essa conexão aberta com o *Dbaccess* **também consumirá licença do *Dbaccess*.**  
  
Se na regra, por algum motivo tiver abono de licenças, o *Dbaccess* se comportará da mesma forma, no caso, das licenças do Meu RH, **terá o consumo destas licenças**.  
  
Como o Meu RH **poderá utilizar licenças sob demanda**, ou seja, **apenas quando houver interação**, essa relação de 1 para 1 ainda será válida, **porque quem irá controlar o consumo de licenças será o serviço *REST*.**  
  
Para isso, as *tags* a seguir, precisarão ser inseridas no **appserver.ini do Meu RH/REST:**  
- Compression=1 na sessão **HTTP ou HTTPS**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23477420308247)  
  
- EnableKeepAlive=0 na sessão **HTTPENV**  
- MODULE=7\*\*\* na sessão **HTTPENV**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23477389201175)  
\*\*\* IMPORTANTE:  
A tag MODULE=7 **não deverá ser incluída** quando, no *License Server*, a Empresa utilizar **licenças 4001 - TOTVS I**. Se essa modalidade for utilizada, **o MODULE=7 não deverá ser incluído.**  
Somente incluir MODULE=7 se e somente se, **as licenças utilizadas para o REST do Meu RH, forem ao licenças ON DEMAND**, as quais necessitam da *tag* na sessão HTTPENV do appserver.ini.  
  
- Stateless=1 na sessão **HTTPV11  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23477420313751)**Ou seja, se por exemplo, a Empresa contratou **1000 licenças para o Meu RH** e, mesmo após inserção das *tags*, todas essas licenças forem consumidas, **precisarão ter a mesma quantidade de licenças para o *DBAcess*.**  
Importante frisar que, se houver o erro abaixo no *login* do Meu RH, será necessário **atualização da LIB e Binário do serviço Meu RH / REST.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27268914709783)  
  
**Para saber mais sobre as licenças e, como são consumidas pelo Meu RH/REST, [clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13225445268247-RH-Linha-Protheus-Meu-RH-Como-as-licen%C3%A7as-no-Meu-RH-s%C3%A3o-consumidas?source=search)****Saiba Mais:  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referência do MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
