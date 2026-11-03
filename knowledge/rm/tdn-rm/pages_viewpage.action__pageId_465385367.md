---
content_hash: 1ecb288d5662a1de37b7d09108db5265ef8b8266ab199077ec2af9d567efae5f
fetched_at: '2026-06-29T00:10:15.912129+00:00'
page_id: '465385367'
product: rm
source: tdn-rm
title: Objeto de Manutenção (Principais)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=465385367
version: 1
---

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
