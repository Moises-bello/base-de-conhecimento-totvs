---
article_id: 19367274675863
category: DIVERSOS e INTERNOS
content_hash: d450de99ae96ad4b09c6ddb378d853da26deae26d452fc4929a72ad09dcd51fd
fetched_at: '2026-06-28T22:44:31.697695+00:00'
product: protheus
section_id: 10325351758359
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como restringir a visualização dos webservices
  a somente usuários autorizados
type: support-article
updated_at: '2026-06-24T11:52:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19367274675863-RH-Linha-Protheus-MEU-RH-Como-restringir-a-visualiza%C3%A7%C3%A3o-dos-webservices-a-somente-usu%C3%A1rios-autorizados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19367247307799) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como restringir a visualização dos *webservices* a somente usuários autorizados?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Se a ***URL***do serviço ***REST*** estiver exibindo todos os ***webservices***, conforme o exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19367284567191)  
  
Significa que a configuração da sessão **HTTPREST** do arquivo de configuração **appserver.ini** do MEU RH está com a chave ***SECURITY=0***, diferente da do padrão recomendado.  
  
Exemplo***:***  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19367269006999)  
  
Esta chave é responsável em exigir as autenticações para a utilização das ***API's***, caso não esteja ligada (**=1**), o *server* responderá qualquer requisição recebida sem validação, e também exibirá todos os webservices do serviço ***REST***.  
  
Para corrigir esta configuração basta alterar o valor da chave ***SECURITY=1***, exemplo:  
***![](https://centraldeatendimento.totvs.com/hc/article_attachments/19367247316119)***  
  
Após alteração, reinicie o serviço ***REST***e acesse novamente a *URL* do serviço ***REST***:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19367259134615)Será exibido uma tela de autenticação de usuário e agora todas as requisição recebidas no ***REST*** passarão por validação.  
  
Abaixo, temos também um *link* da documentação oficial da equipe de produto, com informações relevantes sobre ***HTTP*** e ***REST*** no contexto do MEU RH:  
[Informações Relevantes sobre HTTP/REST no MeuRH](https://tdn.totvs.com/pages/viewpage.action?pageId=550327736)  
  
**Saiba Mais**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
