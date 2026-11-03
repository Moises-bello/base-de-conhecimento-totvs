---
content_hash: 1061bd43229e80e3ab4ddfdb8dea7cbed29d18064903c4efc895715d7272e7d7
fetched_at: '2026-06-29T00:11:27.629080+00:00'
page_id: '728629470'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Utilitários - Conversor TAA para Atendimento
  TCGI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=728629470
version: 3
---

A partir do Release 12.1.2209, disponibilizamos a ferramenta ***Conversor TAA para Atendimento TCGI*** para facilitar a integração entre os Atendimentos criados relativos às questões de Vendas e Aluguéis criados no [TOTVS Aprovações e Atendimentos (TAA)](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=198948845) e a visão de atendimentos do TCGI.

Para acessar esta ferramenta, basta acessar a aba *Utilitários | Ferramentas |* ***Conversor TAA para Atendimento TCGI***:

Para executar esta ferramenta é preciso ter acesso à opção ***06.01.05.08 - Atendimento Conversor: TAA para Atendimento TCGI***, presente no agrupador de *Atendimento* da aba de *Acesso a Menus*, do *Perfil*:

Esta ferramenta irá preencher as informações nas Tabelas XATENDIMENTO e XATENDIMENTOTIPO:

Ao abrir a tela do ***Conversor TAA para Atendimento TCGI***, o sistema apresenta ao Usuário as opções de Parâmetros para localizar os atendimentos aos quais estão associados os Contratos de Vendas e de Locação de Imóveis. Estes Parâmetros são:

* ***Tipo de Contrato:*** *Venda* ou *Aluguel*, no qual o Usuário poderá escolher os Atendimentos de qual tipo de Contrato ele irá converter.

Para os dois Parâmetros abaixo, ao informar o nome deste campo e pressionar a tecla TAB, o sistema irá validar se o mesmo está correto e emitirá uma exceção ao Usuário em caso de inconsistência

* Nome do ***Campo Complementar*** do *Atendimento:* essa informação é essencial para localizar a Venda ou o Contrato de Locação, conforme a opção escolhida no Parâmetro acima. Caso o Atendimento no TAA não tenha este campo preenchido, ele deverá ter obrigatoriamente essa informação preenchida na opção abaixo;
* *Número/****Código do Parâmetro do Atendimento***: idem ao campo acima, porém neste campo, o Usuário irá informar o **número** do *Parâmetro* utilizado para identificar o Contrato de Venda ou o Contrato de Locação;

O Parâmetro do Filtro descrito abaixo, será validado ao se clicar no botão para avançar o processo:

* ***Filtro de SQL:*** utilizado para limitar/filtrar os Atendimentos existentes na Tabela ***HATENDIMENTOEXT***, que atendam aos Parâmetros definidos acima. Através deste filtro, pode-se selecionar qualquer campo da tabela acima e ainda combina com os campos de alguma outra tabela que se relacione com ela, através do comando sql *EXISTS*:

Atenção!

O ***Conversor TAA para Atendimento TCGI***, somente irá funcionar caso os Atendimentos no TAA tenham o Número do Contrato de Venda ou Aluguel informados.

Caso esta informação não esteja no Atendimento, será necessária incluí-la através das opções descritas abaixo.

Para identificar o ***Nome do Campo Complementar***, o Usuário precisa acessar um *Atendimento* que deverá ser convertido, navegar até a aba *Campos Complementares*, clicar com o botão direito na tela desse registro e solicitar para *Visualizar Nome dos Campos*:

A mesma ação deve ser realizada para verificar o *Número/****Código do Parâmetro do Atendimento***, dos Atendimentos que tiverem as informações dos Contratos de Venda/Aluguel preenchidos. No exemplo da imagem abaixo, deve-se informar no ***Conversor TAA para Atendimento TCGI***, somente o número **14**, que é o ID do Campo VENDA:

Conforme informado acima, esta ferramenta ainda possibilita que sejam realizados Filtros por comandos sql  na Tabela *HATENDIMENTOEXT* e nas demais tabelas que se relacionam com ela, através do comando EXISTS.

Um exemplo de filtro que pode ser utilizado é o Campo *CODSTATUS* da Tabela *HATENDIMENTOEXT* que apresenta as constantes abaixo, para as [Situações dos Atendimentos](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=715833069):

Códigos de Situações dos Atendimentos (HATENDIMENTOEXT.CODSTATUS):

* A - Em Atendimento;
* R - Concluído a Responder;
* O - Concluído Respondido;
* F - Concluído Confirmado;
* U - Concluído Automático (pelo sistema);
* V - Avaliado;
* G - Agendado Responder;
* E - Agendado Respondido;
* T - Aguardando Terceiros;
* C - Cancelado; e
* D - Despertado

Assim o Usuário pode parametrizar o ***Conversor TAA para Atendimento TCGI***, combinando diversas opções da forma que melhor lhe atenda:

Após preencher esses Parâmetros e avançar com este processo, o sistema exibirá uma tela para que o Usuário confira os IDs dos Tipos de Atendimentos que serão convertidos, bem como a sua Coligada, o Código do Grupo de Atendimento, a Quantidade de Registros, entre outras informações, para conferência:

Ao avançar novamente com este processo, o sistema detalhará para o Usuário os IDs dos Atendimento, a Coligada e o Número do Contrato, entre outras informações para conferência:

Ao da continuidade executando este processo, o sistema apresentará a tela de conclusão com o resultado da execução do mesmo:

Ao ser concluído com sucesso, as Tabelas XATENDIMENTO e XATENDIMENTOTIPO estarão populadas:

Essas informações estarão acessíveis para o Usuário através das funcionalidade de ***[Atendimentos](https://tdn.totvs.com/pages/viewpage.action?pageId=715158089)*** do app *Meu Imóvel\**, do menu de ***[Atendimentos](https://tdn.totvs.com/display/LRM/Portal+do+Cliente+-+PDC+-+Atendimento)*** do *Portal do Cliente* (*PDC*)\*, através do menu de ***[Atendimentos](https://tdn.totvs.com/display/LRM/COCKPIT+360+-+Atendimentos)*** do *Cockpit 360* e também através da ***[Visão de Atendimentos](https://tdn.totvs.com/pages/viewpage.action?pageId=641160309)***, na interface do TCGI.

Importante!

\*Para que esses Atendimentos esteja acessíveis para o Cliente nos Atendimentos do app *Meu Imóvel* e do *Portal do Cliente* (*PDC*) é preciso marcar a opção [***Exibir Tipo de Atendimento no Portal do Cliente / App Meu Imóvel***](https://tdn.totvs.com/pages/viewpage.action?pageId=641160309):
