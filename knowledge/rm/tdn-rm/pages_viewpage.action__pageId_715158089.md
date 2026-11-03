---
content_hash: 4ade82afd0907967910ff38ae7e7599dc1be2d1e3db674597aea72de0064035a
fetched_at: '2026-06-29T00:11:26.102568+00:00'
page_id: '715158089'
product: rm
source: tdn-rm
title: Meu Imóvel - Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715158089
version: 32
---

A funcionalidade de ***Atendimentos*** está disponível a partir do Release [12.1.2302](https://tdn.totvs.com/pages/viewpage.action?pageId=708100194) e tem como pré-requisito, que o [Novo Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=641160309) esteja habilitado no sistema.

Novidades!

* A partir do Release 12.1.2502 é possível armazenar os arquivos em anexo nos atendimentos do *Meu Imóvel* no repositório de arquivos FileRepo e não mais na tabela de arquivos anexos ao atendimento do RM.

Essa implementação foi concebida para atender a necessidade de armazenamento destes diversos tipos de arquivos e seus respectivos tamanhos, sem onerar a base de dados RM.

Acesse [***Anexos em Repositório de Arquivo*****s**](https://tdn.totvs.com/pages/viewpage.action?pageId=881262199) para conhecer esta opção.

* Veja também como promover uma ***[Interação Usuário x Atendente](https://tdn.totvs.com/pages/viewpage.action?pageId=725727469)*** diretamente pelo Meu Imóvel.

Reforçando que a funcionalidade acima não se trata de nenhum tipo de chat online, mas sim de uma forma de enviar uma mensagem diretamente no Atendimento, após a sua abertura.

A partir desse menu, o usuário do app poderá visualizar e criar um novo Atendimento, conforme as Permissões aplicadas no Perfil deste Usuário:

Ao acessar esse menu, é exibida a tela com a Visão dos Atendimentos, onde são apresentados uma lista "infinita" em forma de cards com todos os atendimentos para este Cliente. Nestes cards temos os seguintes campos:

* + **Assunto:** Assunto do Atendimento. Exemplo: garantia, entrega de chaves, etc.;
  + **Número:** Número do Atendimento, no TCGI;
  + **Data de Abertura:** Data de abertura do Atendimento;
  + **Status:** É a situação do Atendimento ; e
  + **Unidade:** É composto pelos Códigos do Empreendimento, da Unidade e da Subunidade.
  + **Ícone de Clipe:** É o símbolo de arquivos em Anexo. Toque neste ícone para acessar os arquivos anexados a este Atendimento.

É possível aplicar os Filtros na visão dos Atendimentos, clicando no ícone no canto superior direito, onde o Usuário pode filtrar os Status e os Empreendimentos dos Atendimentos:

Ao “clicar” sobre um card o sistema abre o atendimento em questão, permitindo a visualização dos detalhes e permite a iteração com o mesmo:

Ao acionar o botão Novo Atendimento…

… o sistema apresenta as seguintes etapas:

##### Etapa 1 - **Para Qual Unidade Você Quer Abrir a Solicitação**

Onde são exibidas as unidades que este Cliente tem Contratos, para que ele possa solicitar o Atendimento:

##### Etapa 2 - Conte-nos Qual é o Assunto:

Onde o Cliente pode uma lista de assuntos previamente cadastrados no TCGI para gerar o Atendimento. Os assuntos são apresentados em forma de uma listagem vertical e após selecionados devem ser conformados, por meio do botão OK:

Importante!

A partir dessa etapa, o sistema apresenta as demais etapas de forma dinâmica de acordo com as parametrizações aplicadas no [Tipo de Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=641160309).

Apresentamos abaixo o fluxo de Etapas completo, que é apresentado quando as opções *Exibir Preferências no Período de Visitas no Atendimento* e   
*Exigir o Envio de Anexo no Portal do Cliente*, estão marcadas:

##### Etapa 3 - Deseja Adicionar Alguma Garantia?

Nesta  etapa, o sistema apresenta as opções de Cobertura de Garantia e toda a sua hierarquia para que o usuário possa especificar de forma adequada a sua requisição:

O sistema irá apresentar ao usuário também a opção para Voltar ao Início da árvore, caso ele não encontre a opção desejada durante a sua navegação. As garantias válidas são apresentadas com um ícone verde, já as garantias expiradas, tem o ícone vermelho:

##### Etapa 4 - Conte-nos Agora o Que Está Acontecendo:

Nessa tela, é disponibilizado um campo para o Cliente descrever o motivo pelo qual ele está solicitando o Atendimento. Esta descrição deve ter no mínimo 11 e no máximo 256 caracteres, sendo que o botão para Pronto! para avançar a Etapa seja habilitado:

##### Etapa 5 - Vamos Agora vamos incluir fotos na sua solicitação.

Nesta etapa é possível de se anexar os seguintes formatos de arquivos ao Atendimento que será criado, com um limite de 5 a 100MB por arquivo, conforme parametrizado nos *[Parâmetros Gerais do TCGI](https://tdn.totvs.com/pages/viewpage.action?pageId=731881683)* e nos [*Parâmetros dos Arquivos Anexos ao Atendimento do TAA*](https://tdn.totvs.com/pages/viewpage.action?pageId=425458436):

* **pdf;**
* **jpeg;**
* **jpg;**
* **png; ou**
* **dwg**

Importante!

Para enviar mais de um arquivo anexo, selecione todos de uma vez no momento do envio.

Caso seja selecionado um arquivo e posteriormente selecionado outro, o sistema irá sobrepor o primeiro.

##### Etapa 6 - Vamos Agora selecionar o melhor período para visita de Inspeção e reparos.

##### Etapa 7 - Após selecionar o melhor ou os melhores períodos para visita , agora é selecionar o dia ou dias de semana são os melhores para o atendimento.

Ao clicar no botão Finalizar, o sistema apresenta uma mensagem com o resultado deste processo:

Atendimento Gerado com sucesso no APP meu Imóvel.

Interagir no Atendimento : Nesta opção é possivel interagir no atendimento , enviar uma mensagem para que fique registrado algum imprevisto ou algo que possa ser reforçado no mesmo.
