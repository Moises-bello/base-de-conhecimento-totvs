---
content_hash: 1bb10ed84a66da0bba18c052b1883d49e1cba64e29eb5754dac92f1f88a74062
fetched_at: '2026-06-29T00:10:10.601418+00:00'
page_id: '452719889'
product: rm
source: tdn-rm
title: Integrar com TAF / Middleware
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719889
version: 15
---

Este assistente tem a função de enviar os eventos gerados ou que tiveram algum tipo de erro de integração para o TAF (TOTVS Automação Fiscal) ou Middleware, que são os sistemas responsáveis pelas validações finais e transmissão ao governo  
   
**OBSERVAÇÕES:**

* A Quebra de Seção e Seleção de funcionários na tela principal e nos parâmetros específicos da coligada, apenas serão habilitados caso seja marcado algum evento que relacione funcionários ou Eventos Periódicos.
* O Período de Apuração será obrigatório caso selecione algum dos Eventos Periódicos.
* O Parâmetro "Utilizar filtro de afastamento" só será habilitado caso selecione o evento S-2230-(Afastamento Temporário).

false

**ATENÇÃO:**

Para maior segurança e para evitar o envio de informações do eSocial em ambiente incorreto no governo, quando a base de dados for considerada uma base de [Homologação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003443352-RM-Frame-Tipo-de-Ambiente-RMAtualizador), o sistema não permitirá realizar a transmissão dos eventos do eSocial para o ambiente de **Produção** do governo, somente para ambiente de **Produção Restrita**.

Caso a base esteja parametrizada ([Parametrizador | eSocial | Configurações Gerais 1/7](https://tdn.totvs.com/pages/viewpage.action?pageId=452719604)) com o Tipo de Ambiente de **Produção** e for uma base de dados configurada como [Homologação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003443352-RM-Frame-Tipo-de-Ambiente-RMAtualizador), o sistema não irá fazer a transmissão e apresentará erro no log.

Se por algum motivo for necessário realizar a transmissão dos eventos em uma base de dados configurada como [Homologação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003443352-RM-Frame-Tipo-de-Ambiente-RMAtualizador) que esteja com o Tipo de Ambiente parametrizado como **Produção**, o usuário terá duas alternativas, sendo elas:

1º) Alterar a configuração da base de dados  para [Produção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003443352-RM-Frame-Tipo-de-Ambiente-RMAtualizador) ou

2º) Alterar o Tipo de Ambiente do eSocial para "[2 - Produção Restrita](https://tdn.totvs.com/pages/releaseview.action?pageId=452719604)" e gerar novamente os xml's para atualizar a tag "**tpAmb**".

|  |  |
| --- | --- |
|  | Como Fazer |

---

[Parametrizar Integração TOTVS Folha de Pagamento x TAF](http://tdn.totvs.com/pages/viewpage.action?pageId=273994784)

[Integração TOTVS Folha de Pagamento x TAF](http://tdn.totvs.com/pages/viewpage.action?pageId=273997620)

[Seleção de Coligadas -Parâmetro "Considerar Todas as Coligadas"](http://tdn.totvs.com/pages/viewpage.action?pageId=444607665)
