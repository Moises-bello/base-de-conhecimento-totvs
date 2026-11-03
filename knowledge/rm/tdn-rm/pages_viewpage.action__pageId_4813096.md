---
content_hash: 15f88b9df22dc991c6b9a7543ac524505666eb5369330e3e4d6400aa71edefa9
fetched_at: '2026-06-29T00:10:19.151485+00:00'
page_id: '4813096'
product: rm
source: tdn-rm
title: Cálculo de PIS e COFINS Pautado utilizando Preço de Referência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813096
version: 5
---

BLOCK

Cálculo de PIS e COFINS Pautado utilizando Preço de Referência

FAQ: **Cálculo de PIS e COFINS Pautado utilizando Preço de Referência**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para calcular PIS e COFINS Pautado utilizando Preço de Referência?

* ***Definição do Processo***

Tem como funcionalidade calcular base de cálculo dos tributos PIS e\ou COFINS obedecendo informação preenchida em **| Preço/Pauta |** atendendo assim, Cadastro de Eventos Tributários de “Preço por Referência”.

Ramo de industrialização e importação de bebidas (Lei 10.833/03):

Para este setor, a legislação reza que o contribuinte pode optar por um regime especial em que a Tributação deverá ser feita através de um ***preço de referência*** ao invés do preço comercializado. A Base de Cálculo seria determinada em razão deste preço de referência e a quantidade comercializada; e o Valor do Imposto seria determinado em razão desta Base de Cálculo e uma alíquota pré-determinada (%). Este *preço de referência* é também conhecido como **PAUTA**. Para esse caso, preencher o campo “*Preço de Referência ou PAUTA do Produto*” do anexo.

Solução

* ***Parametrizações Necessárias***

Acessar **| Cadastro | Tabelas de Tributação | TRIBUTOS |** e cadastrar os tributos **| PIS – COFINS |**, onde deve informar:

Sigla: PIS

Tipo tributo fiscal: PIS/PASEP

Tipo: Variável

Incidência: se o tributo deve incidir sobre produto x serviços ou ambos

Buscar Alíquota: informar local de onde deve ser buscada alíquota do tributo

Código da Receita: (Opcional)

Sigla: COFINS

Tipo tributo fiscal: COFINS

Tipo: Variável

Incidência: se o tributo deve incidir sobre produto x serviços ou ambos

Buscar Alíquota: informar local de onde deve ser buscada alíquota do tributo

Código da Receita: (Opcional)

Acessar **| Cadastro | Produto |** editar o produto a ser referenciado na movimentação e clicar no ícone **| Anexos | Pautas do Produto | Incluir |** onde irá preencher dados pertinentes tributo pautado informando:

Código do Tributo: preencher do tributo a ser considerado na pauta

Início de Vigência: informar data inicial pauta deste tributo

Fim de Vigência: informar data final pauta deste tributo

Alíquota Débito: preencher alíquota expressa em valores para débito do imposto (utilizada para movimentações de saída)

Alíquota Crédito: preencher alíquota expressa em valores para crédito do imposto (utilizada para movimentações de entrada)

Unidade: informar unidade utilizada para a Alíquota AD REM, esta é a unidade do fator de conversão da unidade do produto preenchida em **| Cadastro | Produto | Controle de Estoque | Unidades | Unidade de Controle |**

Preço/Pauta: informar preço de referência ou pauta do produto

Acessar **| Cadastro | Fórmula | Inserir |** e cadastrar fórmula que seja utilizada para compor a “base de cálculo” do tributo pautado.

Formula IPI : ((KQT \* KPU) \* TABPRDPAUTA ('PIS\_P' , 'PRECOREFERENCIA' , 'V'))

Fórmula COFINS : ((KQT \* KPU) \* \* TABPRDPAUTA ('PIS\_P' , 'PRECOREFERENCIA' , 'V'))

Importante:

A variável **| TABPRDPAUTA |** considera informações preenchidas no cadastro de produtos em **| Anexo | Pautas do Produto |** e retornará 03 parâmetros onde deve informar:

Parâmetro 1: código do tributo a ser considerado

Parâmetro 2: campo do cadastro de pauta que será considerado na fórmula. Neste exemplo específico será considerado “Preco / Pauta”

Parâmetro 3: tipo de campo pertinente informação referenciada no “Parâmetro 2”

Acessar | **Opções | Parâmetros | RMNucleus |** selecionar etapa onde o tipo de movimento está referenciado e clicar em **| Avançar |**. A seguir editar tipo de movimento a ser parametrizado para este fim e informar:

**Etapa Fis Tributação – Item**

**Tributo**: PIS

**Cód.Retenção**: (opcional)

**Fórmula da base de cálculo do tributo**: informar código da fórmula inclusa anteriormente

**Procurar alíquota em**: definido pelo usuário

T**ributo Base**: PIS

**Tributo**: COFINS

**Cód.Retenção**: (opcional)

**Fórmula da base de cálculo do tributo**: informar código da fórmula inclusa anteriormente

**Procurar alíquota em**: definido pelo usuário

T**ributo Base**: COFINS

* **Etapa Fis- Escrituração**

- Gerar Escrituração: Habilitar

- Tipo de Documento Escrituração: informar o tipo de documento que deve ser apresentado no Totvs Gestão Fiscal

\*\* A parametrização acima é obrigatória para tipos de movimentos que geram escrituração\*\*

**Etapa Fis – Natureza**

- Edição: Edita

- Seleção Automática da Natureza: informar se a natureza de operação deve ser informada por item ou no movimento.

* ***Descrição do Processo***

A inclusão dos movimentos será feita como de costume, onde ao editar o item de movimento na aba **| Tributos |** serão apresentados campos **| Base de Cálculo** e **Alíquota |** preenchidos. Na aba | **Alíquota por Valor (AD REM) |** será apresentada alíquota cadastrada anteriormente em **| Cadastro | Produto | Anexos | Pautas do Produto | Alíquota |**, porém esta informação não vai interferir no valor calculado do tributo, visto que, a alíquota será buscada do local parametrizado pelo usuário na inclusão do tributo.

**Memória de Cálculo**

**Quantidade x Preço Unitário x Alíquota de Pauta = Base de Cálculo**

Onde:

- Quantidade = quantidade preenchida no item de movimento

- Preço Unitário = preço unitário preenchido no item de movimento

- Alíquota de Pauta = informação preenchida em **| Cadastro | Produto | Anexos | Pautas do Produto | Alíquota de Débito ou Crédito |** depende da movimentação que está sendo inclusa.

Exemplo:

Quantidade: 1300 Preço Unitário: 10 Preço/Pauta IPI: 1,77 Preço/Pauta: COFINS: 1,89

(1300 x 10) x 1,77 = 23.010,00 = Base de Cálculo de PIS

(1300 x 10 ) x 1,89 = 24.570,00 = Base de Cálculo de COFINS

* ***Escrituração do Movimento***

A escrituração dos movimentos será feita como de costume onde o usuário deve acessar **| Opções | Escrituração de Lançamentos – RMLIBER |** incluir lote para escrituração e fazer filtro da nota fiscal desejada.

Depois de concluído processo de escrituração, ao acessar o Totvs Gestão Fiscal em **| Cadastro | Manutenção de Lançamentos |** e editar o lançamento fiscal os dados dos tributos serão apresentados na aba **| Outros Tributos |**
