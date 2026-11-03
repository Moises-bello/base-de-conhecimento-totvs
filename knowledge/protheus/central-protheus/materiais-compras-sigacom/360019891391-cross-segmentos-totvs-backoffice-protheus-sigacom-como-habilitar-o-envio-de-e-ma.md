---
article_id: 360019891391
category: Materiais - Compras (SIGACOM)
content_hash: fa9067a7148b7195a8ef0c78ee8d12f884b9213f65b4003085ce5fda357b4ecb
fetched_at: '2026-06-28T22:41:07.669349+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como habilitar o envio
  de e-mails para fornecedores
type: support-article
updated_at: '2026-03-04T11:20:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019891391-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-habilitar-o-envio-de-e-mails-para-fornecedores
---

**Dúvida**

Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como habilitar o envio de e-mails para fornecedores  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**

Segue o passo a passo para habilitar o envio de e-mails.

1. Parâmetro MV\_ENVPED - O parâmetro **MV\_ENVPED** permite o envio de e-mails com os pedidos de compra para os fornecedores durante a sua inclusão. As opções de configuração são:

* **0** – Desabilitado: não envia e-mail ao fornecedor.
* **1** – Habilitado: o e-mail só é enviado manualmente, por meio do botão **Outras Ações > Reenviar e-mail**.
* **2** – Habilitado: o e-mail é enviado automaticamente ao criar o pedido de compra. **(Essa configuração só se aplica quando o pedido é incluído e liberado diretamente, sem passar pelo processo de aprovação, ou seja, quando não há alçada de aprovação.)**  
    
  Para que o envio de e-mails aos fornecedores funcione corretamente no Protheus, é fundamental que os seguintes parâmetros estejam devidamente configurados:
* **MV\_EMCONTA:** [user@gmail.com](mailto:user@gmail.com)
* **MV\_RELACNT:** [user@gmail.com](mailto:user@gmail.com)
* **MV\_RELAUSR:** user
* **MV\_RELFROM:** [user@gmail.com](mailto:user@gmail.com)
* **MV\_RELSERV:** smtp.gmail.com
* **MV\_ENVPED:** 1
* **MV\_RELAUTH:** .T.
* **MV\_RELSSL:** .F.
* **MV\_RELTLS:** .T.
* **MV\_EMSENHA:** senha do e-mail
* **MV\_RELAPSW:** senha do e-mail
* **MV\_RELPSW:** senha do e-mail

**Importante:**  
Os parâmetros relacionados à senha (**MV\_EMSENHA**, **MV\_RELAPSW** e **MV\_RELPSW**) devem ser igualados e preenchidos com a senha correta da conta de e-mail utilizada no envio. Isso garante o correto acesso e autenticação junto ao servidor SMTP durante o envio das mensagens.

2. É necessário incluir o arquivo **MATA120\_MAIL001.html** na pasta **protheus\_data/samples/wf** para garantir o funcionamento correto do parâmetro.

![1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35161194462103)

-> O arquivo esta disponível aqui : [MATA120\_Mail001.html](https://tdn.totvs.com/download/attachments/272164717/MATA120_Mail001.html?version=1&modificationDate=1490029697000&api=v2)

3. Cadastro do Fornecedor;

-> Preencha o campo e-mail(A2\_EMAIL);

![2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35161194463383)

**IMPORTANTE**

* O arquivo permite a alteração do seu layout para melhor atender o cliente mas apenas com as variáveis que já constam no HTML, ou seja, não é possível personalizar esse relatório para adicionar mais campos.
* Não é possível carregar campos criado via customização/ ponto de entrada para o layout do arquivo.
* O Suporte Protheus não auxilia no desenvolvimento de customizações. É recomendado que realize junto a um desenvolvedor. Para obter informação de quais pontos de entrada há disponíveis na rotina desejada, acione nossos canais de autoatendimento e o canal de Suporte do módulo.
* Não deve ser alterado o nome externo do arquivo na pasta samples. É orientada apenas a alteração do nome do arquivo para possuir todas letras minúsculas, conforme exemplo: " mata120\_mail001.html "
* Pedidos que possuem alçada de aprovação também são disparados os e-mails referente ao pedido.

Pergunta: Como é preenchido o campo "Cliente" que é apresentado no formulário a seguir  do arquivo [MATA120\_Mail001.html](https://tdn.totvs.com/download/attachments/272164717/MATA120_Mail001.html?version=1&modificationDate=1490029697000&api=v2)  e na imagem abaixo ?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26328690307095)

Resp.: É preenchido  conforme exemplo abaixo:

Você que usa o Protheus é da empresa **A**, e está fazendo um pedido para empresa **B**  
No formulário ficaria assim:  
Fornecedor: **B**  
Cliente: **A (Sua empresa)**

**Importante:**

Se o diretório estiver em um ambiente LINUX é necessário que o nome do arquivo seja todo em minúsculo (**mata120\_mail001)**.

***Saiba Mais :***  
[Parâmetro MV\_ENVPED](http://tdn.totvs.com/pages/viewpage.action?pageId=272164717)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
