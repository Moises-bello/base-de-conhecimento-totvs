---
article_id: 4409629817111
category: eSocial - Middleware
content_hash: ef41845e524216aa0feccefab8a653f576e0ffbc5247eee5739c346848cf92c4
fetched_at: '2026-06-28T22:47:05.593000+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: 'RH - RM - FOP - eSocial - Middleware: Edição de XML'
type: support-article
updated_at: '2024-11-02T16:11:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409629817111-RH-RM-FOP-eSocial-Middleware-Edi%C3%A7%C3%A3o-de-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min****Dúvida**Como realizar a edição de XML no Middleware?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**O processo de **edição de XML** é direcionado para alterações em XML’s a serem enviados ao governo, sendo a alteração direta a última opção de contorno para possíveis inconsistências sistêmicas (caso não seja possível a correção do mesmo antes do seu prazo de envio).

Como premissas da edição, temos:

- **Utilizar o middleware** como forma de integração de eventos;  
- O evento estar nos status **1 - Gerado**, **2 - Erro na geração**, **5 - Erro na Integração** ou **9 - Rejeitado Ret**;  
- **Garantir que a informação alterada seja devidamente preenchida** conforme o leiaute e manual do eSocial. Isso se faz necessário pois o sistema não irá validar a informação alterada, acatando e enviando ao governo a informação preenchida;  
- **Garantir que a alteração tenha sido feita no devido cadastro** para manter consistentes as informações no sistema. Caso tenha sido gerado um novo gatilho dessa alteração, deverá verificar a necessidade de envio desse, ou sua exclusão.

Antes de realizar a edição de um XML, é necessário configurar o parametrizador do eSocial, conforme documentação a seguir (aba **Relatório de Conferência e Edição de XML**): [Passos para ativação do Middleware, configuração do Relatório de Conferência e Edição de XML](https://tdn.totvs.com/pages/viewpage.action?pageId=563428854)

Após realizar as devidas configurações, siga os passos abaixo para realizar a edição do XML:

1. Acesse o menu **eSocial | Fila de Eventos** ou **eSocial | Eventos Periódicos**, selecione o evento desejado e clique no botão **Editar XML**:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409643430423/mceclip2.png)

2. Será exibida uma mensagem de alerta. Confirme a opção para continuar com a edição;

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409629578903/mceclip4.png)

3. Altere a informação desejada e clique na opção **Salvar**;

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409629643543/mceclip5.png)

4. Após a edição, o sistema salvará um histórico de edição em **Anexos | Histórico Edição XML eSocial**.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409629699223/mceclip6.png)

**Importante**Caso o evento tenha sido editado, poderão ser enviados ao governo os que possuem status: **1 - Gerado**, **2 - Erro na geração**, **5 - Erro na Integração** e **9 - Rejeitado Ret**.

Qualquer alteração feita através desse processo será de **responsabilidade do usuário**. Dessa forma ele deve garantir a persistência dos dados para que não ocorra divergências entre o ambiente do governo e a base de dados.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Middleware - Edição de XML's - eSocial do Futuro](https://tdn.totvs.com/pages/viewpage.action?pageId=540888308)
