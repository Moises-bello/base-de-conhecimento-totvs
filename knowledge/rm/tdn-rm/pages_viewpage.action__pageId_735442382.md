---
content_hash: 9ad36c9a3d57e5e2d9ff3aca659aacc6d29fd83cd9623f84c449d8b7ba4b6c3e
fetched_at: '2026-06-29T00:11:29.279847+00:00'
page_id: '735442382'
product: rm
source: tdn-rm
title: Integração Smart View - Objetos de Negócio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=735442382
version: 62
---

Aqui você encontra a lista de todos os Objetos de Negócio do **TOTVS Gestão Contábil** (Linha RM) e, se houver, suas regras para a carga de dados.

Os ON abaixo podem ser utilizados no **Smart View** na construção de Relatórios, Tabelas Dinâmicas e Visões de Dados. Para mais informações sobre o **Smart View** acesse a documentação neste [link](https://tdn.totvs.com/display/public/TREP/SMART+VIEW).

Razão Contábil Analítico

Foi disponibilizado um Objeto de Negócio para que possam ser extraídos os dados do Razão Contábil Analítico.

Os dados serão gerados obedecendo as regras da geração do , onde são detalhadas as particularidades para geração utilizando o Smart View como saída.

Alternativamente, ao efetuar a geração através da interface do Smart View, são disponibilizados os seguintes Filtros e Parâmetros:

**Filtros**

Estão disponíveis para utilização neste ON os seguintes filtros, **não obrigatórios**:

* **Código da Conta**: Código da Conta Contábil da Partida;
* **Código do Centro de Custo**: Centro de Custo da Partida;
* **Lote**: Lote do Lançamento;
* **Histórico Padrão**: Código do Histórico Padrão do Lançamento.

**Parâmetros**

Para geração das informações os seguintes parâmetros devem ser informados::

* **Buscar do Histórico Contábil:**Indicar se os Lançamentos devem ser buscados do Histórico ou do Período Aberto;
* **Código da Coligada**: Coligada dos Lançamentos que serão gerados;
* **Data Inicial:** Data Inicial para seleção dos Lançamentos;
* **Data Final**: Data Final para seleção dos Lançamentos.
  + É validado se as datas informadas estão dentro do Período Contábil vigente, caso o parâmetro "*Buscar do Histórico Contábil*" for FALSO, ou se são anteriores caso esse parâmetro seja VERDADEIRO

**Informações disponíveis**

Os seguintes campos são retornados pelo Objeto de Negócio e podem ser utilizados nos Relatórios, Tabelas Dinâmicas e Visões de Dados:

* **Coligada**: Coligada do Lançamento;
* **Nome da Coligada**: Nome da Coligada;
* **CNPJ da Coligada**: CNPJ da Coligada;
* **Código da Conta:** Código da Conta Contábil do Lançamento;
* **Código Reduzido****:** Código reduzido da Conta Contábil do Lançamento;
* **Descrição da Conta****:** Descrição da Conta Contábil do Lançamento;
* **Conta Contábil****:** Concatenação do Código e Descrição da Conta Contábil do Lançamento;
* **Saldo Anterior****:** Saldo anterior da da Conta Contábil;
* **Data**: Data do Lançamento;
* **ID. da Partida**: Identificador da Partida;
* **Referência**: Identificador do Lançamento;
* **Complemento**: Complemento de histórico padrão;
* **Documento**: Documento do Lançamento;
* **Código da Filial**: Código da Filial da Partida;
* **Nome da Filial**: Nome da Filial da Partida;
* **Filial**: Concatenação do Código e Nome da Filial da Partida;
* **CNPJ da Filial**: CNPJ da Filial da Partida;
* **Código do Centro de Custo**: Código do Centro de Custo da Partida;
* **Centro de Custo Reduzido**: Código reduzido do Centro de Custo;
* **Descrição do Centro de Custo**; Descrição do Centro de Custo;
* **Centro de Custo**: Concatenação do Código e Descrição do Centro de Custo;
* **Lote Origem**: Lote de Origem do Lançamento;
* **Departamento**: Departamento do Lançamento;
* **Conta Contra Partida**: Código da Conta Contra Partida;
* **Descrição da Conta Contra Partida**: Descrição da Conta Contra Partida;
* **Valor de Débito**: Valor de Débito da Partida;
* **Valor de Crédito**: Valor de Crédito da Partida;
* **Saldo Atual**: Saldo Atual da Conta Contábil;
* **Histórico padrão**: O campo está presente no ON somente para ser utilizado como filtro. A informação do Histórico Padrão é retornada no campo Complemento.

Informações | Conta sem movimentação

Nos registros de contas contábeis sem movimentação no período informado, o campo **Data** receberá o dia imediatamente anterior ao início do período de geração e o campo **Saldo atual** será preenchido com o mesmo valor do **Saldo Anterior**.

Balancete Contábil

Foi disponibilizado um Objeto de Negócio para que possam ser extraídos os dados do Balancete Contábil.

Os dados serão gerados obedecendo as regras da geração do , onde são detalhadas as particularidades para geração utilizando o Smart Views como saída.

Alternativamente, ao efetuar a geração através da interface do Smart View, são disponibilizados os seguintes Filtros e Parâmetros:

**Filtros**

Estão disponíveis para utilização neste ON os seguintes filtros, **não obrigatórios**:

* **Código da Conta**: Código da Conta Contábil da Partida;
* **Código do Centro de Custo**: Centro de Custo da Partida;
* **Histórico Padrã****o**: Código do Histórico Padrão do Lançamento;
* **Conta Analítica:** Indica o filtro que busca apenas contas analíticas;
* **Tipo Balancete**: Indica qual o Tipo do Balancete deseja filtrar.

**Parâmetros**

Para geração das informações os seguintes parâmetros devem ser informados:

* **Buscar do Histórico Contábil:**Indicar se os Lançamentos devem ser buscados do Histórico ou do Período Aberto;
* **Código da Coligada**: Coligada dos Lançamentos que serão gerados;
* **Data Inicial**; Data Inicial para seleção dos Lançamentos;
* **Data Final**: Data Final para seleção dos Lançamentos.
  + É validado se as datas informadas estão dentro do Período Contábil vigente, caso o parâmetro "*Buscar do Histórico Contábil*" for FALSO, ou se são anteriores caso esse parâmetro seja VERDADEIRO.

**Informações disponíveis**

Os seguintes campos são retornados pelo Objeto de Negócio e podem ser utilizados nos Relatórios, Tabelas Dinâmicas e Visões de Dados:

* **Coligada**: Coligada do Lançamento;
* **Nome da Coligada**: Nome da Coligada;
* **CNPJ da Coligada**: CNPJ da Coligada;
* **Código da Conta Contábil:** Código da Conta Contábil do Lançamento;
* **Código Reduzido****:** Código reduzido da Conta Contábil do Lançamento;
* **Descrição da Conta****:** Descrição da Conta Contábil do Lançamento;
* **Conta Contábil****:** Concatenação do Código e Descrição da Conta Contábil do Lançamento;
* **Código da Conta Gerencial:** Código da Conta Gerencial do Lançamento, se houver;
* **Código Reduzido da Conta Gerencial:** Código reduzido da Conta Gerencial do Lançamento, se houver;
* **Descrição da Conta Gerencial****:** Descrição da Conta Gerencial do Lançamento, se houver;
* **Conta Gerencial****:** Concatenação do Código e Descrição da Conta Gerencial do Lançamento, se houver;
* **Conta Analítica:** Indicador de conta analítica;
* **Natureza do Sped:** Natureza informada para geração do Sped;
* **Saldo Anterior****:** Saldo anterior da da Conta Contábil;
* **Valor de Débito**: Valor de Débito da conta;
* **Valor de Crédito**: Valor de Crédito da conta;
* **Movimentação**: Movimentação da conta
* **Saldo Atual**: Saldo Atual da Conta Contábil;
* **Código do Centro de Custo**: O campo está presente no ON somente para ser utilizado como filtro. Não é retornado conteúdo pois os registros não são individuais por partida;
* **Histórico padrão**: O campo está presente no ON somente para ser utilizado como filtro. Não é retornado conteúdo pois os registros não são individuais por partida.
* **Tipo Balancete**: O campo está presente no ON somente para ser utilizado como filtro. Não é retornado conteúdo. Se não informado no filtro assume o valor default "Contábil". Foram disponibilizadas as opções Contábil e Contábil-Gerencial.
Conciliação Contábil

Foi disponibilizado um Objeto de Negócio para que possam ser extraídos os dados da Conciliação Contábil.

Os dados serão gerados seguindo as informadas abaixo.

**Filtros**

Estão disponíveis para utilização neste ON os seguintes filtros, **não obrigatórios**:

* **Data Inicial**: Data inicial do relatório, caso não preencha nenhuma data ou data menor que o período Contábil para a Coligada Selecionada nos Parâmetros, será considerada a data Inicial do Período Contábil,

**Parâmetros**

Para geração das informações os seguintes parâmetros devem ser informados:

* **Coligadas**: Coligadas que contém a mesma conta contábil marcada como conciliável.
* **Data Final**: Data Final para seleção dos Lançamentos.
* **Código da Conta**: Código da Conta Contábil conciliável;
* **Considerar Lançamento não Integrado:** Considera os lançamentos que não foram integrados ao **lote zero.**
* **Considerar Lançamento Conciliado:** Considera lançamentos que já foram conciliados.

**Informações disponíveis**

Os seguintes campos são retornados pelo Objeto de Negócio e podem ser utilizados nos Relatórios, Tabelas Dinâmicas e Visões de Dados:

* **Coligada**: Coligada do Lançamento;
* **Id Movimento:** Identificador do Movimento:
* **Origem:** Origem do lançamento:
* **Id Lançamento:** Identificador do Lançamento Contábil:
* **Descrição:** Descrição do lançamento:
* **Data:** Data do Lançamento:
* **Código do Lote:** Código do Lote em que o lançamento esta integrado:
* **Código da Conta:** Código da Conta Contábil do Lançamento;
* **Total de Débito**: Valor de Débito da conta;
* **Total de Crédito**: Valor de Crédito da conta;
* **Conciliação:** Identifica se a conciliação esta feita para o lançamento.
* **Documento**: Numero do documento.
* **Id Financeiro:** Identificador do Lançamento Financeiro:
* **Status do Exercício:** Status atual do Exercício Contábil.
* **Código Cliente Fornecedor:** Código do Cliente Fornecedor:
* **Nome Cliente Fornecedor:** Nome do Cliente Fornecedor:
* **Código Filial:** Código da Filial:
* **Complemento Histórico:** Descrição do complemento histórico.

**Campos Controle de Filtro**

Foi necessário criar campos para efetuar controles/filtros internos, estes campos podem ser removidos da exibição.

* **Filtro Data Inicial:** Controle para Data Inicial:
* **Filtro Coligada**: Controle para Coligada do Lançamento:
Movimentação ContábilAtenção

Funcionalidade disponível à partir do Release 12.1.2310

Foi disponibilizado um Objeto de Negócio para que possam ser extraídos os dados das movimentações contábeis, isto é, retornarão os dados das Partidas e também das respectivas Dimensões. Inicialmente poderá ser consumido, no Smart View montando relatórios e demais artefatos disponíveis na ferramenta.

Para a utilização deste Objeto de Negócio é necessário que seja atribuída a permissão abaixo no perfil de segurança:

 

Este Objeto de Negócio disponibiliza as Partidas juntamente com os dados das Dimensões Contábeis das Entidades Cliente/Fornecedor e/ou Produto sendo que a Dimensão de Produto permite rateio, isto é, pode existir mais de um produto na mesma partida cada um com seu respectivo valor que representa o valor do rateio para tal produto.

Serão listados apenas os Lançamentos/Partidas já integrados ao Lote Oficial (lote 0).

A partidas serão ordenadas por Data e Id da Partida.

**Parâmetros**

Para geração das informações os seguintes parâmetros devem ser informados (cabe salientar que todos os parâmetros são de preenchimento obrigatório):

* **Buscar do Histórico Contábil:**Indicar se os Lançamentos devem ser buscados do Histórico ou do Período Aberto;
* **Código da Coligada**: Coligada dos Lançamentos que serão gerados;
* **Data Inicial**; Data Inicial para seleção dos Lançamentos;
* **Data Final**: Data Final para seleção dos Lançamentos.
  + É validado se as datas informadas estão dentro do Período Contábil vigente, caso o parâmetro "*Buscar do Histórico Contábil*" for FALSO, ou se são anteriores caso esse parâmetro seja VERDADEIRO.
* **Partidas Conciliadas:** Caso seja VERDADEIRO, serão selecionadas as partidas que estejam conciliadas.
* **Partidas não Conciliadas:** Caso seja VERDADEIRO, serão selecionadas as partidas que ainda estejam pendentes de conciliação.  
    Observação: Os dois parâmetros acima de conciliação podem ser marcados como verdadeiro caso necessário, assim serão buscados todos os lançamentos, independente do status da conciliação das partidas.
* **Exibir Contas sem Movimentação com Saldo:**Quando verdadeiro, retorna também as contas que possuem Saldo Anterior porém não possuem movimentação no período selecionado.
* **Exibir dados de Dimensões:** Controla a exibição de dados da dimensões contábeis no relatório. (**OBS.: Quando existe algum filtro com Dimensão Contábil esse parâmetro automaticamente se comportará como VERDADEIRO.**).

**Filtros**

Para geração das informações os seguintes filtros podem ser utilizados para restringir os registros a serem selecionados. São eles:

* **Histórico Padrã****o**: Código do Histórico Padrão da Partida/Lançamento;
* **Dimensões**: Dimensões Contábeis cadastradas na base de dados. Somente serão selecionados Lançamentos cujas Partidas possuam as Dimensões selecionadas neste filtro;
* **Cliente/Fornecedor:** Filtra os Lançamentos cuja Dimensão Cliente/Fornecedor tenha como valor um dos selecionados nesta opção;
* **Produto:** Filtra os Lançamentos cuja Dimensão Produtos tenha como valor um dos selecionados nesta opção;

**Informações disponíveis**

Os seguintes campos são retornados pelo Objeto de Negócio e podem ser utilizados nos Relatórios, Tabelas Dinâmicas e Visões de Dados:

* **Coligada**: Coligada da Partida;
* **Nome da Coligada**: Nome da Coligada;
* **CNPJ da Coligada**: CNPJ da Coligada;
* **Lançamento**: Identificador do Lançamento da Partida;
* **Referência**: Identificador do Lançamento Referência;
* **ID. da Partida**: Identificador da Partida;
* **Conciliado a Débito:** Identifica o status de conciliação da partida a débito;
* **Conciliado a Crédito:** Identifica o status de conciliação da partida a crédito;
* **Data**: Data do Lançamento;
* **Coligada da Conta**: Coligada da Conta da Partida;
* **Código da Conta:** Código da Conta Contábil da Partida;
* **Código Reduzido****:** Código reduzido da Conta Contábil da Partida;
* **Descrição da Conta****:** Descrição da Conta Contábil da Partida;
* **Conta Contábil****:** Concatenação do Código e Descrição da Conta Contábil da Partida;
* **Valor de Débito**: Valor de Débito da Partida;
* **Valor de Crédito**: Valor de Crédito da Partida;
* **Saldo Anterior:** Saldo Anterior da combinação de Conta Contábil + Dimensões;
* **Saldo Atual:** Saldo Atual da combinação de Conta Contábil + Dimensões após a movimentação da partida em questão;
* **Coligada da Conta Contra Partida**: Coligada da Conta Contra Partida da Partida;
* **Conta Contábil Contra Partida****:** Concatenação do Código e Descrição da Conta Contra Partida da Partida;
* **Lote**: Lote da Partida;
* **Lote Origem**: Lote de Origem da Partida;
* **Código da Filial**: Código da Filial da Partida;
* **Nome da Filial**: Nome da Filial da Partida;
* **CNPJ da Filial**: CNPJ da Filial da Partida;
* **Filial**: Concatenação do Código e Nome da Filial da Partida;
* **Centro de Custo**: Concatenação do Código e Descrição do Centro de Custo;
* **Complemento**: Complemento de histórico padrão;
* **Histórico padrão**: O campo está presente no ON somente para ser utilizado como filtro. A informação do Histórico Padrão é retornada no campo Complemento;
* **Coligada do Cliente/Fornecedor**: Coligada do cliente/fornecedor (originário da Dimensão);
* **Código e Nome do** **Cliente/Fornecedor**: Concatenação do código e come do cliente/fornecedor (originário da Dimensão);
* **Coligada do Produto**: Coligada do produto (originário da Dimensão);
* **Descrição do produto**: Concatenação do identificador, código e nome (nome fantasia) do produto (originário da Dimensão);
* **Valor rateado (Dimensão)**: Valor do rateio por Dimensão;
* **Código do Centro de Custo**: Código do Centro de Custo da Partida;
* **Centro de Custo Reduzido**: Código reduzido do Centro de Custo;
* **Descrição do Centro de Custo**; Descrição do Centro de Custo;
* **Documento**: Documento do Lançamento;
* **Conta Contra Partida**: Código da Conta Contra Partida;
* **Código Reduzido da Conta Contra Partida****:** Código reduzido da Conta Contábil da Partida;
* **Descrição da Conta Contra Partida**: Descrição da Conta Contra Partida da Partida;
* **Departamento**: Departamento do Lançamento;
* **Dimensões Contábeis:** O campo está presente no ON somente para ser utilizado como filtro.
* **Código do Cliente/Fornecedor**: Código do cliente/fornecedor (originário da dimensão);
* **Nome do Cliente/Fornecedor**: Nome do cliente fornecedor - campo NOME do tabela FCFO (originário da dimensão);
* **Identificador do produto**: Identificador do produto na tabela de produto;
* **Código do produto**: Código do produto formatada de acordo com uma determinada mascara;
* **Nome do produto**: Nome fantasia do produto;

Saldo Anterior

Ainda não existe Saldo Anterior armazenado por agrupamento de Dimensões Contábeis.

Desta forma, caso haja filtro por Dimensão Contábil, o Saldo anterior será calculado através da totalização da Movimentação desde o início do Período Contábil até o dia anterior ao dia inicial da geração do relatório. Esta totalização é agrupada por Conta e Dimensões Contábeis filtradas.

O Saldo Atual da Partida será calculado considerando o Saldo Atual da Partida imediatamente anterior (se for a primeira Partida é considerado o Saldo Anterior) + valor de débito - valor de crédito da Partida.

**Visão de dados com o uso das Dimensões de Cliente/Fornecedor e Produto**

Configurando o filtro com Dimensão de Cliente/Fornecedor e Produto

Resultado / Dados de uma visão de dados sem o uso de filtro. Note que neste caso, quando há a dimensão de produto (que permite rateio), os registros de partida se duplicam de acordo com a quantidade de produtos rateados.

**Visão de dados com o uso da Dimensão de Cliente/Fornecedor**

Configurando o filtro com Dimensão de Cliente/Fornecedor:

Resultado da execução da Visão de Dados, customizada com o agrupamento por Cliente/Fornecedor e Conta Contábil:
