---
content_hash: 90290e3973c2ae665c4c84303e00e5e32090d215a9caa4642f4f39388e06dc9f
fetched_at: '2026-06-29T00:10:11.884198+00:00'
page_id: '453294995'
product: rm
source: tdn-rm
title: Portal da Obra
type: documentation
url: https://tdn.totvs.com/display/LRM/Portal+da+Obra
version: 124
---

---

No mundo dos negócios, onde as empresas precisam ter controle sobre suas operações e, ao mesmo tempo, agilidade para atender aos diversos processos que acontecem simultaneamente foi criado o Portal da Obra.

Mais informações sobre instalação: [Configuração de Instalação - Portal da Obra e Cockpit TOP](https://tdn.totvs.com/x/Qhz6IQ)

PaginageralLogin e Contexto de Projeto

Neste Portal Web o usuário tem a possibilidade de selecionar a Coligada e o Projeto conforme modelo abaixo, respeitando as parametrizações e permissões do RM para o usuário.

No topo da tela principal do portal é exibido o projeto atual que o usuário está logado.

E ao lado direito ainda no topo da página na logo da Totvs é possível realizar a troca de contexto selecionando outro projeto para visualização.

Ao realizar a troca os parâmetros serão atualizados de acordo com o projeto selecionado.

Login integrado via aplicativo SAML

É possível configurar o login no portal da obra, para ser integrado com qualquer provedor de nuvem ou serviço de identidade que suporte aplicativos SAML, como o Microsoft Azure por exemplo.

Para isso, os passos abaixo devem ser seguidos:  
  
1 - Configurar um aplicativo SAML no provedor de nuvem ou serviço de identidade de sua preferência (Para ver um exemplo de tal configuração, vide

)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2 - Criar um novo registro no cadastro de 'Aplicativos SAML' na aba 'Gestão' do RM conforme imagem abaixo:

Na edição do novo registro, preencher da seguinte forma:

Os campos de preenchimento obrigatório são:

Nome do Provider: É apenas um identificador, pode ser preenchido da forma que melhor se adequar a suas necessidades.

Url de Retorno: Deve ser preenchida com a URL de login do Portal da Obra, tipicamente seria

<http://localhost:8051/PortalTopWeb/login>

Substituindo localhost e 8051 pelo servidor e porta adequados respectivamente.

Url de login do provider: Deve ser preenchida com a URL de login do aplicativo SAML criado no provedor de nuvem ou serviço de identidade.

Url de logout do provider: Deve ser preenchida com a URL de logout do aplicativo SAML criado no provedor de nuvem ou serviço de identidade.

Metadados: Deve ser preenchido com o certificado SAML do aplicativo criado no provedor de nuvem ou serviço de identidade em base64, para mais detalhes vide 

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3 - Parar o serviço de host e acrescentar a seguinte TAG:  
  
<add key="SamlProviderIdPortalDaObra" value="1" />  
  
Em seguida iniciar o serviço novamente, é importante observar o atributo value da TAG deve ser preenchido com o ID do aplicativo SAML recém criado.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4 - Se a configuração até agora estiver OK, ao acessar o login do portal da obra, a página convencional (que solicita usuário e senha) será substituída pela seguinte:

Ao clicar no botão 'Portal da Obra', caso o usuário já estiver autenticado no provedor de nuvem ou serviço de identidade configurado, o login será feito automaticamente e o Portal da Obra será aberto com o usuário do RM que tiver o mesmo email autenticado no browser, caso não estiver autenticado, ao clicar no botão, ele será direcionado para pagina de autenticação do provedor de nuvem ou serviço de identidade configurado e após a autenticação ser concluída, o Portal da Obra será aberto da mesma forma.

**Atenção:**Devido a cache e alguns outros fatores, no primeiro acesso ao portal, pode ser que a pagina de login antiga seja exibida por alguns segundos antes de mostrar a tela acima.

Monitor de Obras
> Temporariamente, a partir da versão 12.1.2506, para utilizar o Pedido, Pedido Extra ou Monitor de Obras, no Portal da Obra, será necessário executar o instalador TOTVS RM Portal Pedidos Monitor que está disponível na Central de Downloads.
>
> A alteração acontece para atender demandas da evolução tecnológica. Caso você utilize alguma dessas funcionalidades, entre em contato com o administrador do sistema e solicite a instalação.

**Monitor de Obras**

Pedido
> Temporariamente, a partir da versão 12.1.2506, para utilizar o Pedido, Pedido Extra ou Monitor de Obras, no Portal da Obra, será necessário executar o instalador TOTVS RM Portal Pedidos Monitor que está disponível na Central de Downloads.
>
> A alteração acontece para atender demandas da evolução tecnológica. Caso você utilize alguma dessas funcionalidades, entre em contato com o administrador do sistema e solicite a instalação.

Pedido Extra
> Temporariamente, a partir da versão 12.1.2506, para utilizar o Pedido, Pedido Extra ou Monitor de Obras, no Portal da Obra, será necessário executar o instalador TOTVS RM Portal Pedidos Monitor que está disponível na Central de Downloads.
>
> A alteração acontece para atender demandas da evolução tecnológica. Caso você utilize alguma dessas funcionalidades, entre em contato com o administrador do sistema e solicite a instalação.

### Pedido Extra

O Pedido Extra tem a finalidade de controlar os gastos extras, ou seja, material além do planejado. São controladas todas as movimentações de pedidos, autorização do pedido, quantidade pedida para determinada tarefa e principalmente as pessoas envolvidas no processo.

Para a funcionalidade de cadastro do Pedido Extra no TOTVS Obras e Projetos foram desenvolvidas telas Web para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.

Foram desenvolvidas todos os cadastros e visões de anexo para o Pedido Extra da seguinte forma:

* Tela com a listagem dos pedidos de materiais extras salvos na base de dados com opções para Adicionar, editar, visualizar e excluir ;

Tela com os detalhes do Pedido Extra;

* Item de Pedido Extra;
* Status do Pedido;
* Data Requisição;

Configurações:

* + Utiliza Preço Orçado;
  + Responsável;
  + Tipo de Movimento;
  + Local de Estoque;
  + Observação

Integração com TOTVS Aprovações e Atendimento

Caso o pedido extra esteja integrado com o TOTVS Aprovações e atendimento, o fluxo de aprovação tradicional(Parâmetros de Projeto → Integração → Suprimentos/Faturamento → Pedido Extra → Utilizar fluxo de aprovação para pedido extra) não será exibido no portal, que são os processos descritos abaixo.

De acordo com o status do pedido haverá um botão para executar os processos:

* **Retornar para criação:** Quando o pedido está no status "Em aprovação" e deseja-se realizar alterações no pedido.
* **Enviar para Aprovação:** Quando o pedido está no status "Em criação" e pronto para ser analisado e aprovado.
* **Finalizar Aprovação:** Quando o pedido está no status "Em aprovação" e houve alguma alteração individual em algum item, ou seja foi aprovado parcialmente.
* **Aprovar Pedido Extra:** Quando o pedido está no status "Em aprovação" e deseja aprovar o pedido por completo, sem nenhuma ressalva.
* **Reprovar Pedido Extra:** Quando o pedido está no status "Em aprovação" e deseja reprovar o pedido por completo.

Não será possível selecionar múltiplos registros para execução dos processos, seguindo o padrão de uso Web, devendo executar item a item. Foram migados todos os processos que envolvem o Pedido:

* Pedido
  + Retornar para criação
  + Enviar Pedido Extra para Aprovação
  + Finalizar Aprovação de Pedido Extra
  + Aprovar Pedidos Extra
  + Reprovar Pedidos Extra
  + Gerar 1 Movimento
  + Gerar Movimento por Data de Entrega
  + Excluir Movimento
* Anexo Item do Pedido

* + Aprovar item
  + Reprovar Item
  + Aprovar Item Parcialmente
  + Colocar Itens em Análise

* Movimento
  + Rastreamento de movimento foi mantido o comportamento similar ao da interface WinForms, onde o usuário somente executa o processo e recebe como retorno a mensagem com o status de processamento.

* Ao Adicionar um novo Item de Pedido Extra, existe o campo "Manter preenchimento do último item adicionado".
  + Caso esteja marcado, ao Adicionar Novo Item, a tela deve vir preenchida com os dados do último item adicionado, exceto a Quantidade que deve vir em branco.
  + Se o campo não estiver marcado, o comportamento se mantém o atual.

Saiba mais em.: [Geração de Pedido](http://tdn.totvs.com/display/LRM/Pedido+de+Material) e [Geração de Pedido Extra](http://tdn.totvs.com/pages/viewpage.action?pageId=421385494&moved=true).

Cockpit TOPDashboard de IndicadoresPlanilha ExecutivaMinhas Inspeções

Pode ser acessado tanto pelo aplicativo Minhas Inspeções quanto pelo Portal da Obra. Abaixo, é possível acessar a documentação de ambos, clicando nas respectivas abas:

Diário de ObraPERT
