---
article_id: 360036569613
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b55f5f706b3e47838080be58a027237ed855565594b1e4475da2c1583b6d37f5
fetched_at: '2026-06-28T22:38:41.289044+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP-FAT-Cadastro de Regras de Acesso (Privilégios) não funcionam na rotina MATA456
type: support-article
updated_at: '2021-04-28T15:50:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036569613-MP-FAT-Cadastro-de-Regras-de-Acesso-Privil%C3%A9gios-n%C3%A3o-funcionam-na-rotina-MATA456
---

**Dúvida**

Cadastro de Regras de Acesso (Privilégios) não funcionam na rotina MATA456  
  
**Ambiente**

Microsiga Protheus - a partir da versão 12.  
  
**Solução**

Para a priorização da configuração do Grupo, é necessário configurar o campo em destaque abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/65XnZc056sGbeBrMV1js42u0c/?name=image-2019-08-22-11-46-34-588.png)  
**USR\_GRPULE =priorizar.**  
  
A documentação deste campo encontra-se em tdn: [**http://tdn.totvs.com/pages/viewpage.action?pageId=271388115**](http://tdn.totvs.com/pages/viewpage.action?pageId=271388115) , veja o trecho que fala sobre **regra de acesso por grupo**.
