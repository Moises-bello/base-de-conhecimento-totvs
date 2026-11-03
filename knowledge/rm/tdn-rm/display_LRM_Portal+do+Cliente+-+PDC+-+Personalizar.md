---
content_hash: 71be454c91ecdb24dbbe72a4d457ec25f698493766fa937ef96a4889a60f1c20
fetched_at: '2026-06-29T00:09:48.598053+00:00'
page_id: '435105200'
product: rm
source: tdn-rm
title: Portal do Cliente - PDC - Personalizar
type: documentation
url: https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Personalizar
version: 4
---

**Personalizar**

---

**Descrição**  
Esta funcionalidade permite a Incorporadora personalizar o Portal, dando características próprias de forma a deixar o comprador familiarizado com o ambiente.

|  |  |
| --- | --- |
|  | Como Fazer |

---

A personalização do portal pode ser feita de 3 formas distintas: Menu, Tema e Home page. Apenas administradores do portal tem a possibilidade de personalizar o portal e essa permissão e concedida no modulo da nova MDI -> Serviços globais -> aba Segurança - > Perfil -> selecione o Perfil | Tópico: Incorporação(portal) | Administrador | Personalizar.  Abaixo iremos abordar cada uma das formas Personalização que o administrador poderá customizar.  
A personalização do portal pode ser acessada pelo menu (Gestão->Personalizar) ou através da engrenagem localizada no canto superior direito do Portal. Ao acessar a opção Personalizar será exibida uma página intermediária com as opções de personalização:

* **Menu**

A customização do menu pode ser feita para definir a melhor forma de exibição das opções de menu . O administrador poderá ordenar o menu do perfil do comprador e perfil de Gestão.

* **Temas**

A customização do Layout do portal pode ser feita na opção Temas. Nesta funcionalidade o Administrador tem a possibilidade de modificar as cores do portal para a cores da Incorporadora.   
   
Ao clicar no botão  Novo, será aberto uma página para a customização do layout podendo ser alterado as cores:

* Barra superior - Cor de fundo
* Título - Cor da fonte
* Subtítulo - Cor da fonte
* Menu de boas vindas - Cor de fundo
* Menu de boas vindas - Cor da fonte
* Menu lateral - Cor de fundo
* Menu lateral - Cor da fonte do nome do empreendimento
* Menu lateral - Cor da linha superior de separação
* Menu lateral - Cor da fonte

Na personalização do Tema também é possível alterar a Logomarca do portal, podendo ser inserido a Log da Incorporadora.

* **Página Inicial**

O portal também disponibiliza em sua arquitetura a personalização da Página inicial do comprador. A abrir a página de personalização será mostrado a listagem das páginas já cadastradas pelo administrador:  
   
Nesta listagem é possível editar uma Home Page, publicar a página para que os compradores já possam visualizar , excluir uma página ou apenas despublicar.   
Ao clicar no Botão novo localizado no cabeçalho da página, o administrador poderá criar uma nova página seguindo as seguintes configurações:

* **Descrição:** Descrição da Home page, afim de identificar a mesma na listagem de páginas.
* **Número de Slot na página:** Este parâmetro define quantos quadros serão adicionados na sua página inicial, neste quadro poderá ser incluso um Widget,  frame  ou um conteúdo HTML.
* **Global:** Define se a página criada será visualizada para todos os empreendimentos cadastrados. É importante informar que apenas uma página poderá ser global.
* **Mobile**: Define se a página criada será visualizada somente para os usuários do [App Meu Imóvel](http://tdn.totvs.com/pages/viewpage.action?pageId=489780379). É importante informar que apenas uma página poderá ser classificada como mobile.
* **Empreendimento:** Ao clicar na Lupa o administrador poderá associar a página a um ou mais empreendimentos.
* **Botão Cancelar:** Este botão tem ação de cancelar a edição ou criação da página.
* **Botão Configurar Layout:** Este botão tem ação de exibir a página de configuração da página.
* **Botão salvar:**  Este botão tem ação de salvar a página, é importante informar que ao salvar uma página a mesma ainda não estará disponível para o comprador, é necessário a publicação da mesma para que ela seja exibida na home do comprador.

Na página de configuração é possível personalizar a página inicial informando a opções de desejo como: Widget, Frame ou Conteúdo HTML:

* **Widget:** Ao informar Widget a Totvs disponibiliza nesta versão 3 Widgets distintos: Andamento Geral da Obra, Comunicados e Situação financeira
* **Frame:** Ao informar Frame o usuário poderá incluir um frame de uma página externa, informando a url e o tamanho da exibição
* **Conteúdo HTML:** Se o usuário selecionar a opção de conteúdo html, será possível incluir na página conteúdo HTML para ser exibido. Não será possível a inclusão de javascript. Mas pode ser incluído CSS inline para personalização do conteúdo, conforme exemplo a seguir:

  <img src="minha\_imagem.jpg" style="height:auto;width:100%;" />

Após a configuração da página inicial o portal obriga a visualização da página para ter a certeza de que a página criada está correta, e para visualizar o preview da página clique no botão visualizar.  
Após clicar na opção visualizar será exibido para administrador o preview da página com a opção de publicar.  
Ao clicar no botão publicar a página estará disponível para o comprador:

* Caso o portal identifique que a página criada contém empreendimentos que também estejam em outras páginas publicadas será exibido uma mensagem de substituição do empreendimento para a página atual.
