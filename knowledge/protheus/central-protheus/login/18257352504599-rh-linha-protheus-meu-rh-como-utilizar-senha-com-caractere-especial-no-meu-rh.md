---
article_id: 18257352504599
category: LOGIN
content_hash: 74bde03f642d7db3443d562c256feb3fb35c57b878776c46a01b310f567d2b2e
fetched_at: '2026-06-28T22:44:40.482340+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como utilizar senha com caractere especial no
  Meu RH
type: support-article
updated_at: '2026-06-23T21:23:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18257352504599-RH-Linha-Protheus-MEU-RH-Como-utilizar-senha-com-caractere-especial-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18257322108567) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como utilizar caracteres especiais nas senhas do Portal Meu RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**Ao tentar realizar o *login* com caracteres especiais, possuindo toda a **configuração correta de criptografia**, alguns caracteres **não são aceitos** pelo **Meu RH.**  
A ocorrência reportada ocorre devido ao método de ***login* do Meu RH.**  
  
Foi implementado uma nova estrutura de *login*, visando sanar o problema **de caracteres especiais nas senhas.**  
Para isto, foi criado um novo parâmetro para que seja possível habilitar esse novo *login*.  
  
É obrigatório configurar o ***setting/companySettings*** na chave ***Public*** do **appserver.ini**, conforme abaixo:  
![image2023-5-30_15-5-17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18257297858583)

Public=fwjwt/refresh\_token,auth,**setting/companySettings**

Novo parâmetro criado para utilizar a nova estrutura de *login*:

| Campo | Conteúdo |
| --- | --- |
| Nome da variável (X6\_VAR): | MV\_MRHLOGI |
| Tipo (X6\_TIPO): | Lógico |
| Descrição (X6\_DESCRIC): | Habilita nova estrutura de *login* no MeuRH |
| Valor Padrão (X6\_CONTEUD): | .F. |

**Importante**Caso você entenda que deve haver algum comportamento diferente ou outras opções de personalização, por gentileza, registre uma solicitação de melhoria através do da **[Central Colaborativa TOTVS](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br).**É possível acompanhar as funcionalidades já disponíveis e o planejamento do que está por vir através do **[ROADMAP MEU RH - PROTHEUS](https://tdn.totvs.com/display/public/NPR/Roadmap+-+Protheus).  
  
Saiba Mais  
[CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)**[para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH) **[CLIQUE AQUI](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)** [para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
