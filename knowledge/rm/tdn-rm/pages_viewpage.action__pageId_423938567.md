---
content_hash: 80b0ab2aa2838821bf3ff453fb795c17a076464981d0a672b3c16bdf308a52b9
fetched_at: '2026-06-29T00:09:27.909520+00:00'
page_id: '423938567'
product: rm
source: tdn-rm
title: Objeto de Manutenção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938567
version: 9
---

Objeto de Manutenção é todo objeto que faz parte do parque de maquinas de uma empresa ou todo objeto que se destina a manutenção de uma empresa que presta serviços de manutenção.   
Os objetos de manutenção são divididos por tipologia, o tipo de objeto de manutenção é definido por cada empresa de acordo com o seu segmento.   
A partir de tal segmentação é possível avaliar, planejar e executar ações de manutenções que devem ser aplicadas aos Objetos de Manutenção.   
Ao definir os tipos de objetos de manutenção estabelecemos o que será mapeado, equipamentos e os seus subconjuntos, que também são tratados como objetos de manutenção.   
Para cada tipo é necessário definir o padrão e nome do primeiro e segundo identificador, bem como os dados importantes que deverão ser levantados e cadastrados no processo de mapeamento.  
Exemplo: Veículos, equipamentos, estruturas, componentes de instalação, máquinas, aviões, monitores, pneus etc.   
Também é possível cadastrar uma máscara para o primeiro e segundo identificador.   
Essa máscara é cadastrada no cadastro de tipo de objeto de manutenção na aba identificação.   
Para saber mais sobre o cadastro da máscara do primeiro e segundo identificador do [Tipo de Objeto de Manutenção](http://tdn.totvs.com/pages/viewpage.action?pageId=423937891)..  
Através do cadastro de Objeto de Manutenção o usuário poderá visualizar todos os dados relacionados aos objetos de manutenção que são gerenciados pelo sistema, tal como o histórico de indicadores de uso deste objeto, os índices de acompanhamento deste objeto, os [Planos de Manutenção](http://tdn.totvs.com/pages/viewpage.action?pageId=423938407) cadastrados para este objeto e muito mais.  
O objeto de manutenção possui as seguintes pastas:

* **Identificação**: Permite cadastrar e editar os dados de identificação dos objetos de manutenção que podem ser gerenciados pelo sistema.
* **Dados Complementares**: Permite incluir uma descrição para o objeto de manutenção. Basta digitar as observações no espaço apropriado.
* **Campos Configuráveis**: Permite cadastrar dados em campos configurados no menu Parâmetros | Tipos de Objetos de Manutenção, na pasta Campos e Tabelas Opcionais.
* **Pasta Indicador(es) de Uso**: Permite o controle dos indicadores de uso do objeto de manutenção.
* **Integração**: Aqui você poderá associar um Objeto de Manutenção à um Bem Patrimonial.  
  ***Observação***: Esta pasta apenas estará disponível se flag em Opções | Parâmetros | Sistema pasta Identificação "Integração com RM Bonum" estiver marcado.  
  Para associar um objeto de manutenção que possua OS em aberto a um bem patrimonial o usuário terá que marcar o parâmetro "Permite vincular um bem patrimonial ao objeto que possui OS em aberto" em Opções | Parâmetros | Sistema, aba Ordem de Serviço, caso contrário o sistema emitirá uma mensagem de erro informando que o objeto possui OS em aberto e não poderá ser vinculado a um bem patrimonial.  
  ***Atenção!***  Por questão de segurança, o será permitido ao usuário associar apenas um Bem Patrimonial a um Objeto de Manutenção, cujo perfil possua permissão de acesso definido em Cadastro | Segurança | Perfil de Usuário | Acesso a Menus.
* **Agregados**: Permite cadastrar os objetos-filhos para o objeto de manutenção selecionado.
* **Campos Complementares**: Permite cadastrar dados em campos criados através do menu Cadastro | Campos Complementares | Objeto de Manutenção.

**Identificação**

Essa janela permite você cadastrar e editar os dados de identificação dos objetos de manutenção que podem ser gerenciados pelo sistema, tais como automóveis, telefones celulares, condicionadores de ar, circuitos de comunicação, pneus, entre outros.

**1º** Identificador do Objeto de Manutenção: Código alfanumérico que identifica cada objeto de manutenção dentro do sistema.   
***Atenção!*** Para cada Tipo de Objeto de Manutenção pode-se definir um nome diferente para este identificador.   
Exemplo: No caso de veículos, o 1º identificador poderia ser o chassi. Telefones celulares utilizariam como identificador o ESN e condicionadores de ar o Número de Série. Já os Pneus poderia ser marca de fogo, uma marca impressa.

**2º** Identificador do Objeto de Manutenção: Código alfanumérico auxiliar que identifica um objeto de manutenção dentro do sistema.  
***Atenção!*** Para cada Tipo de Objeto de Manutenção pode-se definir um nome diferente para este identificador.   
Exemplo: Nos Veículos o segundo identificador poderia ser a sua placa. Telefones celulares utilizariam como identificador o MSN e condicionadores de ar a sua etiqueta de patrimônio.  
***Dica***: O 2º Identificador poderá ser obrigatório se habilitado em Opções | Parâmetros | Tipos de Objetos de Manutenção | edição do Tipo de Objeto de Manutenção, campo "2º Identificador do Objeto Obrigatório?".

**Cód. do Tipo de Objeto de Manutenção**: Identifica qual é o tipo deste objeto de manutenção. O tipo de objeto de manutenção é cadastrado em Opções | Parâmetros | Sistema | Tipos de Objetos de Manutenção.  
***Atenção!*** Este campo só ficará disponível para edição caso a opção Permite Múltiplos Tipos de objetos de Manutenção estiver marcada, em Opções | Parâmetros | Sistema | Pasta Nomes de Campos e Tabelas.  
Fabricante: Aqui você define o fabricante do seu Tipo de Objeto de Manutenção. Só serão apresentados os fabricantes relacionados ao tipo de objeto de manutenção selecionado.

**Cód. Modelo**: Código do modelo do objeto de manutenção do sistema. São exibidos para seleção somente os modelos do fabricante selecionado.

**Cód. Sub-Modelo**: Código do sub-modelo do objeto de manutenção do sistema. São exibidos para seleção somente os sub-modelos do modelo selecionado.

**Estado de Conservação**: Selecione o estado de conservação do objeto de manutenção, conforme situações de estados, cadastrados internamente no aplicativo. O estado de conservação indicará a condição em que se encontra do objeto.  
Caso seja feita alguma reforma para o objeto então o estado passará a ser "REFORMADO". Se a reforma for excluída, este campo passará automaticamente para o status "USADO". Uma reforma ocorre quando um objeto de manutenção passa por uma Ordem de Serviço de reforma.  
Exemplo: Novo - Objeto nunca foi usado. Usado - Objeto que já está sendo utilizado. Reformado - Objeto que já sofreu processo de reforma. Danificado - Não está apto para ser utilizado, proibindo a agregação a qualquer objeto. Sucateado - Objeto considerado impróprio. Todo Objeto que for sucateado deverá ser informado o motivo de sucateamento.  
***Observação***: Objetos sucateados não podem ser alterados, agregados, mandado para estoque, gerar Ordem de Serviço.  
Situação do Objeto de Manutenção: Ao clicar nesse botão é exibida a situação do Objeto, exemplo, são situações do Objeto de Manutenção:

* Agregado
* Normal
* Em Estoque
* Em Terceiros
* Oficina
* Transferido (é informado o local para onde ele foi transferido).

**Data de Venda**: É utilizado normalmente em movimentos de ordem de serviço com garantia.

**Data de Fabricação**: Data de fabricação do objeto de manutenção.

**Ano de Fabricação**: Campo preenchido automático pelo sistema, a partir do preenchimento do campo 'Data de Fabricação'.

**Ano do Modelo**: Digite o ano do projeto do modelo.

**Valor de Aquisição**: Informa o preço de compra do objeto de manutenção.

**Status**: Especifica a localização e a situação do objeto no qual a empresa efetuará a manutenção.

**Centro de custo**: Esse campo é evitável, a não ser que o objeto de manutenção esteja vinculado a um bem do RM Bonum. Neste caso, o Centro de Custo deve ser o mesmo que está cadastrado para o bem no Bonum e o campo deve ficar indisponível para edição no Officina. Se o vínculo for desfeito, o Centro de Custo, no Officina, receberá o valor nulo.  
***Observação***: Ao cadastrar uma Ordem de Serviço o centro de custo será preenchido com o centro de custo do Objeto de Manutenção, desde que não haja default para o centro de custo do Tipo de Movimento e centro de custo default para o cliente/Fornecedor, ou seja, a busca do centro de custo para a Ordem de Serviço terá a seguinte ordem

1. Centro de Custo do Cliente/Fornecedor
2. Centro de Custo do Tipo de Movimento
3. Centro de Custo do Objeto de Manutenção

**Data de Criação**: Data de Inclusão do Objeto de Manutenção no Sistema.

**Código Cliente/Fornecedor**: Código alfanumérico que identifica cada cliente/fornecedor dentro do sistema. Clicando no ícone 'Visualizar Localização do Objeto' você encontra o local onde se encontra o objeto de manutenção.  
***Observação***: O local de instalação é inserido no cadastro de Cliente/Fornecedor, anexo Locais de Instalação, e é preciso Instalar o Objeto de Manutenção, disponível em Operações | Instalação de Objeto de Manutenção.

**Quantidade de Reforma**: Este campo pode ser preenchido manualmente, porém pode não ser a realidade do objeto. Este campo será incrementado a cada processo de reforma que ele passar.  
Os campos abaixo aparecem apenas quando os objetos são agregados:

* **Identificador do Objeto Raiz**: Identificador que estiver no nível mais alto.
* **Identificador do Objeto Pai**: Identificador do Objeto pai, ou seja, onde este agregado está de fato apenso.

Exemplo: Objeto 1 Objeto 2 (Agregado do Objeto 1) Objeto 3 (Agregado do Objeto 2)  
Tomando como referência o Objeto 3, o identificador do objeto Pai será o identificador do Objeto 2 e o identificador do Objeto Raiz será o identificador do Objeto 1. Se o caso for uma agregação simples (um objeto agregado a outro), o identificador do objeto pai e do objeto raiz serão os mesmos.

---
