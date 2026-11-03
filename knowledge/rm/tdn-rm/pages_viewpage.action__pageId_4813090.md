---
content_hash: aeea4bdf0c02a336c2e9c0fe2c9500bf63b7e0de5e6325b3cecf90ce64615131
fetched_at: '2026-06-29T00:10:19.142019+00:00'
page_id: '4813090'
product: rm
source: tdn-rm
title: Cálculo de PIS e COFINS Pautado utilizando Alíquota AD REM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813090
version: 8
---

BLOCK

Cálculo de PIS e COFINS Pautado utilizando Alíquota AD REM

FAQ: **Cálculo de PIS e COFINS Pautado utilizando Alíquota AD REM**

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para calcular PIS e COFINS utilizando alíquota AD REM?

* ***Definição do Processo***

Tem como funcionalidade gerar valor calculado dos tributos PIS e\ou COFINS obedecendo cadastro de Eventos Tributários através da “Alíquota AD REM(Alíquota representada por R$/UN)” informada por item.

Ramo de industrialização e importação de álcool combustível (Lei 9.718/98):

Para este setor, a legislação reza que o contribuinte pode optar por um regime especial em que a tributação deverá ser feita utilizando-se uma alíquota específica, denominada ***AD REM*** e expressa em R$/Un (Reais por Unidade de Medida), ao invés de utilizar uma alíquota relativa (que é a utilizada normalmente), expressa em (%) percentual e denominada ***AD VALOREM***. Aqui, preencher os campos “Alíquota Expressa em Valores para Débito do Imposto”, “Alíquota Expressa em Valores para Crédito do Imposto” e “Unidade utilizada para a Alíquota AD REM”.

Solução

* ***Parametrizações Necessárias***

Acessar **| Cadastro | Tabelas de Tributação | TRIBUTOS |** e cadastrar os tributos **| PIS – COFINS |**, onde deve informar:

Sigla: PIS

Tipo tributo fiscal: PIS/PASEP

Tipo: Variável

Incidência: se o tributo deve incidir sobre produto x serviços ou ambos

Buscar Alíquota: Pauta do Produto

Código da Receita: (Opcional)

Sigla: COFINS

Tipo tributo fiscal: COFINS

Tipo: Variável

Incidência: se o tributo deve incidir sobre produto x serviços ou ambos

Buscar Alíquota: Pauta do Produto

Código da Receita: (Opcional)

Acessar **| Cadastro | Produto |** editar produto a ser referenciado na movimentação. A seguir acessar aba **| Controle de Estoque | Unidades |** e verificar qual código de unidade está informado no campo **| Unidade de Controle |**.

Importante:

O cálculo do tributo pautado por Alíquota AD REM vai considerar o fator de conversão pertinente “unidade base” vinculada a esta unidade de controle. Esta informação será consultada em **| Cadastro | Unidades | XX | Conversão |** onde deve verificar a unidade referenciada no campo “Cod. Unidade Base” e o conteúdo preenchido no campo “Fator de Conversão”.

Ainda no cadastro do produto, deverá clicar no ícone **| Anexos | Pautas do Produto | Incluir |** e preencher os dados pertinentes ao tributo pautado informando:

Código do Tributo: preencher do tributo a ser considerado na pauta (PIS e/ou COFINS)

Início de Vigência: informar data inicial pauta deste tributo

Fim de Vigência: informar data final pauta deste tributo

Alíquota Débito: preencher alíquota expressa em valores para débito do imposto (utilizada para movimentações de saída)

Alíquota Crédito: preencher alíquota expressa em valores para crédito do imposto (utilizada para movimentações de entrada)

Unidade: informar unidade utilizada para a Alíquota AD REM, esta é a unidade do fator de conversão da unidade do produto preenchida em **| Cadastro | Produto | Controle de Estoque | Unidades | Unidade de Controle |**

Preço/Pauta: informar preço de referência ou pauta do produto

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fis Tributação – Item**

**Tributo**: PIS

**Cód.Retenção**: (opcional)

**Fórmula da base de cálculo do tributo**: utilizar a função de Fórmula KQTTRIB

**Procurar alíquota em**: Pauta do Produto

T**ributo Base**: PIS

**Tributo**: COFINS

**Cód.Retenção**: (opcional)

**Fórmula da base de cálculo do tributo**: utilizar a função de Fórmula KQTTRIB

**Procurar alíquota em**: Pauta do Produto

T**ributo Base**: COFINS

**Etapa Fis- Escrituração**

- Gerar Escrituração: Habilitar

- Tipo de Documento Escrituração: informar o tipo de documento que deve ser apresentado no Totvs Gestão Fiscal

\*\* A parametrização acima é obrigatória para tipos de movimentos que geram escrituração\*\*

**Etapa Fis – Natureza**

- Edição: Edita

- Seleção Automática da Natureza: informar se a natureza de operação deve ser informada por item ou no movimento.

* ***Descrição do Processo***

A inclusão dos movimentos será feita como de costume, porém ao editar o item de movimento na aba **| Tributos |** os campos **| Base de Cálculo e Alíquota |** estarão vazios pelo fato de não haver uma informação definida para os campos.

Na aba **| Alíquota por Valor (AD REM) |** será apresentada alíquota informada anteriormente em **| Cadastro | Produto | Anexos | Pautas do Produto | Alíquota |** e será considerada para composição do valor calculado do tributo.

**Memória de Cálculo**

**Quantidade X Fator de Conversão da Unidade Base do Produto x Alíquota = Valor Calculado** *(somente se a unidade de controle do produto for DIFERENTE da unidade de medida preenchida na pauta do produto)*

Onde:

- Quantidade = quantidade preenchida no item de movimento

- Fator de Conversão da Unidade Base do Produto = informação preenchida em **| Cadastro | Unidades** | onde deve selecionar unidade preenchida em **| Cadastro | Produto | Controle de Estoque | Unidade de Controle |** e verificar informação preenchida no campo “Fator de Conversão”

- Alíquota = informação preenchida em **| Cadastro | Produto | Anexos | Pautas do Produto | Alíquota de Débito ou Crédito |** depende da movimentação que está sendo inclusa.

Exemplo:

Quantidade: 1300 Fator de Conversão da Unidade: 1 Alíquota Débito: 6 Alíquota Crédito: 12

Cálculo para movimento de Compra(Alíquota de Crédito)

1300 x 1 x 12 = 15.600,00

Cálculo para movimento de Venda(Alíquota de Débito)

1300 x 1 x 6 = 7.800,00

**OU**

**Quantidade x Alíquota = Valor Calculado** *(somente se a unidade de controle do produto for IGUAL da unidade de medida preenchida na pauta do produto)*

Cálculo para movimento de Compra(Alíquota de Crédito)

1300 x 12 = 15.600,00

Cálculo para movimento de Venda(Alíquota de Débito)

1300 x 6 = 7.800,00

* ***Escrituração do Movimento***

A escrituração dos movimentos será feita como de costume onde o usuário deve acessar **| Opções | Escrituração de Lançamentos – RMLIBER |** incluir lote para escrituração e fazer filtro da nota fiscal desejada.

Depois de concluído processo de escrituração, ao acessar o Totvs Gestão Fiscal em **| Cadastro | Manutenção de Lançamentos |** e editar o lançamento fiscal os dados dos tributos serão apresentados na aba **| Outros Tributos |**

Para maiores informações:

**COMUNIDADE **[R@Materiais e Finanças](https://totvs.byyou.com/?space=rmateriais)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015
