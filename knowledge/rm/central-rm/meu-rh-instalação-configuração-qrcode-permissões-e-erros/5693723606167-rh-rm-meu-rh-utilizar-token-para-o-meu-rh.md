---
article_id: 5693723606167
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: c173da6b13e51ec3a04ed50be6732cfcb9f47dbe3719f12a3a3579e1fb8d888e
fetched_at: '2026-06-28T22:47:29.511433+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - Utilizar token para o Meu RH
type: support-article
updated_at: '2025-03-27T18:59:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5693723606167-RH-RM-Meu-RH-Utilizar-token-para-o-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24076301926295) Tempo aproximado para leitura: **00:03:14 min** **Dúvida**Como utilizar o Token durante o login no Meu RH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.31  
  
**Solução**Para aumentar a segurança na autenticação, pode ser habilitado o *token* no *login.*  
Para habilitar o token :  
   
No diretório \FrameHTML\web\app\RH\PortalMeuRH e arquivo "properties.json" atribuir o valor  "true" à propriedade "USE\_TOKEN".

|  |
| --- |
| `"USE_TOKEN": true` |

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24076301939863)  
   
Sobre a utilização do *token*, o funcionamento é da seguinte forma no Meu RH :  
  
Foi implementada a utilização do *bearer token* para autenticação do usuário ao invés do processo de *basic authentication*. A *bearer authentication* (também chamada de autenticação por *token*) é um esquema de autenticação HTTP que envolve tokens de segurança chamados *bearer tokens*. O nome "*Bearer token*" pode ser entendido como "dar acesso ao portador deste *token*". O *bearer token* é uma string criptografada, gerada pelo servidor em resposta a uma solicitação de login. O *client* deve enviar este token no cabeçalho de autorização ao fazer solicitações para recursos protegidos. Utilizamos a API Autorização / Autenticação Basic e *Bearer Token*que retorna um *token* contendo as informações do usuário e outras *claims* que são relevantes para ele.  
  
![](https://tdn.totvs.com/download/attachments/626133948/image2021-10-18_12-35-37.png?version=1&modificationDate=1634571337490&api=v2)

Para ter mais informações referentes ao utilização do token, basta acessar: [RH - RM - Meu RH utilização de token](https://tdn.totvs.com/pages/viewpage.action?pageId=519207769)
