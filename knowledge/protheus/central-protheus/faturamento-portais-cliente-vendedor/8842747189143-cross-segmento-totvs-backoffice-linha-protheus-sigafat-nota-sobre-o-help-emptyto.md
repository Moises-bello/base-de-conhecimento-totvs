---
article_id: 8842747189143
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 806258b631f0943a80cca816cf43d6d8a9505ff356de242914264489d4012147
fetched_at: '2026-06-28T22:38:23.871222+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota sobre o
  help EmptyToken / mv_mingtok
type: support-article
updated_at: '2022-09-21T13:11:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8842747189143-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-sobre-o-help-EmptyToken-mv-mingtok
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Ao incluir um usuário de portal é gerado o Help:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8841470478231/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - a partir da 12.1.27.  
  
**Solução**

O help é acionado , por conta, do direito  do usuário PORTALCLIENTEMINGLE - Portal do Cliente:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8841562848535/mceclip1.png)

Este direito foi criado para o uso do **[Portal Financeiro Protheus (Novo Portal do Cliente)](https://tdn.totvs.com/x/6D_AIg)** do módulo do Financeiro, com isso ao carregar os direitos do usuário do portal (Fata220), é inserido um novo serviço para utilização do mesmo, denominado **PORTALCLIENTE**.

Para que consiga concluir o cadastro do usuário do portal, após carregar os direitos, **será necessário deletar este item, (PORTALCLIENTE da coluna Código WS).**

**Observações:**

**1-** esta opção é apenas para quem usa os portais antigos (Portal do Vendedor/Portal do cliente).

Se for utilizado o novo portal do cliente, é necessário dar undelete sobre a linha a deixando disponível para uso e solicitar a criação do alias mingle para posterior preenchimento do parâmetro **MV\_MINCTOK** com o Token recebido por e-mail, conforme é indicado na documentação **[Portal Financeiro Protheus (Novo Portal do Cliente)](https://tdn.totvs.com/x/6D_AIg).**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8841833827479/mceclip2.png)

**2-**Se o ambiente estiver utilizando  a rotina  **Fata220 de 09/03/22**, ao incluir os direitos do usuário do portal, o sistema já traz este direito deletado . Atualização desta rotina encontra-se no pacote de expedição contínua do Faturamento: **[SIGAFAT](https://tdn.totvs.com/x/Iw4dHw)**

**3-**A chamada do help somente ocorrerá se este direito estiver habilitado para uso, conforme a demonstração a seguir:

![recording-2022-09-13-12-21-49.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/8842203001111/recording-2022-09-13-12-21-49.gif)

**3.1 - Demonstração de tela dos portais:**

**Portal do cliente antigo** que não utiliza configuração de alias mingle e configuração de chave rest para funcionamento:

**Portal do Cliente (Antigo)**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8842641506071/mceclip4.png)**

**Novo Portal do Cliente (Portal Financeiro Protheus)** que necessita a configuração da chave rest no server.ini e alias mingle para uso:**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8842428132247/mceclip3.png)**
