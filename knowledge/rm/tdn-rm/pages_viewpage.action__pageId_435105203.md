---
content_hash: 3713aa51e2c3cb396a7cadf51950cafe72eb1b29f3e3a5b935928d1d3ea0ab61
fetched_at: '2026-06-29T00:09:48.610180+00:00'
page_id: '435105203'
product: rm
source: tdn-rm
title: Gerar Contrato - Gestão Imobiliária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105203
version: 10
---

Para gerar contratos e cadastrar escrituras no TOTVS Construção e Gestão Imobiliária - TCGI, acesse o menu *Venda | Contratos de Venda*, selecione ou edite uma uma venda.

Acesse o menu A*nexos | Contratos | Gerar Contrato*:

Ao acessar esta opção o sistema apresenta a seguinte mensagem ao usuário:

*Esta venda não possui contrato associado. Deseja gerar um novo contrato?*

Escolhendo sim, a tela para Gerar Contrato é aberta com as seguintes opções:

**Geração do Número do Documento:** Nesta opção é possível gerar o número do documento para o contrato, baseado na [Máscara do Número do Contrato](https://tdn.totvs.com/pages/viewpage.action?pageId=435104735), de duas formas:

* **Automático:** O sistema irá gerar o número do contrato automaticamente;
* **Manual:** O sistema permite que o usuário informe o *número do Contrato* no campo destinado a este fim. Alguns clientes informam o próprio número da venda.

Aba **Contrato**:

Esta aba apresenta os campos abaixo relativo ao contrato e o TCGI:

* **Coligada:** Este campo é preenchido automaticamente pelo sistema, com base na Coligada na qual a venda está cadastrada;
* **Nº Venda:** Este campo é preenchido automaticamente com o número da venda selecionada;
* **Nº Contrato:** Este campo o identificador interno do contrato, que é preenchido automaticamente pelo sistema com base na chave primária deste registro na tabela de Contratos, que é único para todas as coligadas;
* **Contrato:** É o número do contrato gerado/informado na tela inicial do sistema. É possível de se editar esta informação, sempre que a Situação do Contrato estiver *Em Preparação*, sendo este número que será impresso no contrato que é enviado para o cliente;
* **Data de Emissão:** Este campo é preenchido automaticamente com a data que o usuário executou o processo da tela de Gerar Contrato, descrita acima;
* **Cliente:** Este campo é preenchido automaticamente com o Código e Nome do [Comprador](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Compradores) principal associado ao contrato desta venda;
* **Situação Contrato:** Este campo é preenchido automaticamente com a Situação do contrato sendo estas situações:
  + **Em Preparação:** Quando nesta situação, será possível de se editar o campo Contrato e o Documento a ser gerado na aba Documentos. Somente o botão *Efetivar* fica habilitado nesta aba;
  + **Efetivado:** Quando nesta situação, o sistema bloqueia as edições do campo Contrato e também a edição do Documento na aba Documentos. Os botões Voltar Situação, Suspender e Cancelar ficam habilitados nesta aba;
  + **Suspenso:** Quando nesta situação, o Contrato está suspenso e não permite nenhuma ação no mesmo, a não ser a utilização do botão *Voltar Situação;*
  + **Cancelado:** Quando nesta situação, o sistema permite apenas a edição do campo Contrato e habilita o botão *Voltar Situação*.
* **Objeto do Contrato:** Este campo é preenchido automaticamente com os dados do item (Apartamento/Lote) associado a esta venda. Sendo:
  + **Código do Empreendimento:** É o código do empreendimento ao qual o item de venda está associado;
  + **Código da Unidade/Bloco/Quadra:** É o código da unidade/bloco/quadra ao qual o item de venda está associado;
  + **Código da Subunidade/Apartamento/Lote:** É o código da subunidade/apartamento/lote ao qual o item de venda está associado;
  + **Valor Total:** este campo é preenchido automaticamente com a informação do campo [Valor Venda/Aluguel](https://tdn.totvs.com/pages/viewpage.action?pageId=435105242) que está visível no agrupador Valores do Contrato da tela de cadastro desta venda.

Além dos campos acima, são exibidos os seguintes botões para controle da Situação do Contrato, e as ações já citadas acima:

* **Voltar Situação:** Volta a situação do Contrato em relação à situação atual para efetivado ou em preparação;
* **Efetivar:** Efetiva a situação do contrato e aplica as permissões de edição relativas à esta situação;
* **Suspender:** Suspende o contrato e aplica as permissões de edição relativas à esta situação;
* **Cancelar:** Cancela o contrato e aplica as permissões de edição relativas à esta situação.

   
  
Aba **Documentos**  
   
Nesta aba, pode selecionar o [Modelo de Documento](https://tdn.totvs.com/display/LRM/Modelos+de+Contrato)que será utilizado para a impressão do Contrato.

Ao acessar esta aba, são apresentadas as seguintes opções:

Agrupador **Gerar Documentos do Contrato**:

* **Modelo do Contrato:** É um lookup para a seleção dos [Modelos de Contratos](https://tdn.totvs.com/display/LRM/Modelos+de+Contrato) já cadastrados no sistema;
* **Botão Gerar Contrato:**  Após a seleção do modelo acima, acione este botão para carregar o layout do modelo selecionado já com os dados relativos ao objeto deste contrato (é preciso que o modelo seja parametrizado corretamente para que esta ação ocorra), na tela de edição de documentos desta aba.

Esta tela de edição tem os recursos básico de um editor de texto, para a manipulação do contrato, como formatação, impressão, etc..

* **Cancelar Contrato:** Utilize este botão para limpar as informações do editor de texto.

Aba **Escritura do Contrato**  
   
Nesta aba é possível de se inserir os dados relativos à Escritura do Contrato.

Ao acessar esta aba, é apresentada uma visão com os registros associados à este contrato, sem possível Inserir, Editar e Excluir estes registros.

Ao acionar a opção para inserir um novo registro, o sistema apresenta uma tela com as seguintes opções:

Aba **Identificação**:

* **Contrato:** Este campo é preenchido automaticamente pelo sistema, com o código do contrato ao qual a escritura está associada;
* **Valor da Escritura:** Informe o valor da escritura. Este campo é em formato moeda;
* **Data Escritura:** Informe a data da escritura;
* **Observação:** Este campo é em texto livre para se detalhar qualquer informação pertinente à esta escritura;
* **Status Passada:** Informe se esta escritura já está passada ou não;
* **Data Passada:** Informe a data em que esta escritura foi passada;
* **Status Autorizada:** Informe se esta escritura já está autorizada ou não;
* **Data Autorizada:** Informe a data de autorização desta escritura;
* **Nº do Registro:** Informe o número de registro desta escritura;
* **Data Registro:** Informe a data de registro desta escritura;

Os campos abaixo tem preenchimento automático pelo sistema, com base no Objeto do Contrato:

* **Empreendimento:** É o código do empreendimento ao qual o item de venda está associado;
* **Unidade:** É o código do unidade ao qual o item de venda está associado;
* **Subunidade:** É o código do subunidade ao qual o item de venda está associado;
