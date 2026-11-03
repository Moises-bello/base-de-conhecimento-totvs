---
article_id: 19429764987159
category: LOGIN
content_hash: dfbbf6186f59609ff7826330c5efd36929bf2b5004218cdf7803a0de4836126c
fetched_at: '2026-06-28T22:44:40.440708+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - Meu RH - Como evidenciar nos logs, os elementos de disparo
  de e-mail
type: support-article
updated_at: '2026-06-23T21:14:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19429764987159-RH-Linha-Protheus-Meu-RH-Como-evidenciar-nos-logs-os-elementos-de-disparo-de-e-mail
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19429748101783) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como evidenciar nos logs do MEU RH os elementos de disparo de *e-mail* ?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
 **Solução**Para trazer este nível de detalhamento nos *logs* gerados no **MEU RH** é necessário adicionar uma chave na sessão [*MAIL]* chamada *VERBOSE=1* no arquivo de configuração ***appserver.ini do MEU RH*****:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19429760728215)  
  
Após a inclusão é necessário reiniciar os serviços do **MEU RH**.  
  
Feito isso, qualquer ação que envolva a sessão de disparo de *e-mail,* seja na função "*Esqueceu a senha*" ou "*Workflow*", terá o detalhamento no console.log do **MEU RH**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19429781171735)  
  
Isso ajuda na identificação de falhas que podem ser ocasionadas por configurações externas ao aplicativo **MEU RH**, como por exemplo, bloqueio/restrição no ***firewall*** do ***domínio***.  
  
Para mais detalhes sobre as rotinas que envolvem o uso do e-mail no **MEU RH**, acesse os *links* abaixo:  
[RH - Linha Protheus - MEU RH - Como configurar o E-mail de Workflow de solicitações do MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055230453)  
[RH - Linha Protheus - MEU RH - Como configurar o Esqueceu a Senha do MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052543934)  
  
**Saiba Mais  
[Permissão de funcionalidades do Meu RH - Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=494805578#:~:text=Configurar%20permiss%C3%A3o%2Frestri%C3%A7%C3%A3o%20acesso%20%C3%A0s,SIGATCF%2C%20conforme%20instru%C3%A7%C3%B5es%20a%20seguir)**  
**[RH - Linha Protheus - MEU RH - Quais são as funcionalidades disponibilizadas no Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5540795734807)****[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**  
**[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
