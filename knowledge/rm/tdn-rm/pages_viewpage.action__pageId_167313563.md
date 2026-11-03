---
content_hash: 269e637601e926c882f0049b274597e384c11c198df8770c3f6f5c836fe389ea
fetched_at: '2026-06-29T00:05:57.252812+00:00'
page_id: '167313563'
product: rm
source: tdn-rm
title: Cálculo de IPI Pautado utilizando Alíquota AD REM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=167313563
version: 1
---

Avaliação

* ***Como Fazer***

Como parametrizar o sistema para calcular IPI Pautado utilizando alíquota AD REM?

* ***Definição do Processo***

Tem como funcionalidade gerar valor calculado dos tributos IPI Pautado obedecendo cadastro de Eventos Tributários através da “Alíquota AD REM(Alíquota representada por R$/UN)” informada por item.

Solução

* ***Parametrizações Necessárias***

Acessar **| Cadastro | Tabelas de Tributação | TRIBUTOS |** e cadastrar os tributos **| IPI PAUTADO |**, onde deve informar:

Sigla: IPI-P (por exemplo)

Tipo tributo fiscal: IPI

Tipo: Variável

Incidência: Produto

Buscar Alíquota: Pauta do Produto

Código da Receita: (Opcional)

Acessar **| Cadastro | Produto |** editar produto a ser referenciado na movimentação. A seguir acessar aba **| Controle de Estoque | Unidades |** e verificar qual código de unidade está informado no campo **| Unidade de Controle |**.

Importante:

O cálculo do tributo pautado por Alíquota AD REM vai considerar o fator de conversão pertinente “unidade base” vinculada a esta unidade de controle. Esta informação será consultada em **| Cadastro | Unidades | XX | Conversão |** onde deve verificar a unidade referenciada no campo “Cod. Unidade Base” e o conteúdo preenchido no campo “Fator de Conversão”.

Ainda no cadastro do produto, deverá clicar no ícone **| Anexos | Pautas do Produto | Incluir |** e preencher os dados pertinentes ao tributo pautado informando:

Código do Tributo: preencher do tributo a ser considerado na pauta (IPI-P)

Início de Vigência: informar data inicial pauta deste tributo

Fim de Vigência: informar data final pauta deste tributo

Alíquota Débito: preencher alíquota expressa em valores para débito do imposto (utilizada para movimentações de saída)

Alíquota Crédito: preencher alíquota expressa em valores para crédito do imposto (utilizada para movimentações de entrada)

Unidade: informar unidade utilizada para a Alíquota AD REM, esta é a unidade do fator de conversão da unidade do produto preenchida em **| Cadastro | Produto | Controle de Estoque | Unidades | Unidade de Controle |**

Preço/Pauta: informar preço de referência ou pauta do produto

Acessar **| Cadastro | Tabelas de Tributação | Natureza de Operação |** editar o registro desejado **| aba Tributação ICMS/IPI | Edite a regra do IPI | aba Dados IPI**, onde deve informar:

IPI Pautado: Marcar a opção

Acessar | **Opções | Parâmetros | RMNucleus |** e selecionar processo onde o tipo de movimento a ser utilizado para este fim foi configurado. A seguir editar o mesmo e informar:

**Etapa Fis Tributação – Item**

**Tributo**: IPI-P

**Cód.Retenção**: (opcional)

**Fórmula da base de cálculo do tributo**: Informar a fórmula da base de cálculo

**Procurar alíquota em**: Pauta do Produto

T**ributo Base**: IPI

**Etapa Fis- Escrituração**

- Gerar Escrituração: Habilitar

- Tipo de Documento Escrituração: informar o tipo de documento que deve ser apresentado no Totvs Gestão Fiscal

\*\* A parametrização acima é obrigatória para tipos de movimentos que geram escrituração\*\*

**Etapa Fis – Natureza**

- Edição: Edita

- Seleção Automática da Natureza: informar se a natureza de operação deve ser informada por item ou no movimento.

* ***Descrição do Processo***

A inclusão dos movimentos será feita como de costume, porém ao editar o item de movimento na aba **| Alíquota por Valor (AD REM) |** será apresentada alíquota informada anteriormente em **| Cadastro | Produto | Anexos | Pautas do Produto | Alíquota |** e será considerada para composição do valor calculado do tributo.

**Memória de Cálculo**

**Quantidade X Fator de Conversão da Unidade Base do Produto x Alíquota = Valor Calculado***(somente se a unidade de controle do produto for DIFERENTE da unidade de medida preenchida na pauta do produto)*

Onde:

- Quantidade = quantidade preenchida no item de movimento

- Fator de Conversão da Unidade Base do Produto = informação preenchida em **| Cadastro | Unidades**| onde deve selecionar unidade preenchida em **| Cadastro | Produto | Controle de Estoque | Unidade de Controle |** e verificar informação preenchida no campo “Fator de Conversão”

- Alíquota = informação preenchida em **| Cadastro | Produto | Anexos | Pautas do Produto | Alíquota de Débito ou Crédito |** depende da movimentação que está sendo inclusa.

Exemplo:

Quantidade: 1300 Fator de Conversão da Unidade: 1 Alíquota Débito: 6 Alíquota Crédito: 12

Cálculo para movimento de Compra(Alíquota de Crédito)

1300 x 1 x 12 = 15.600,00

Cálculo para movimento de Venda(Alíquota de Débito)

1300 x 1 x 6 = 7.800,00

**OU**

**Quantidade x Alíquota = Valor Calculado***(somente se a unidade de controle do produto for IGUAL da unidade de medida preenchida na pauta do produto)*

Cálculo para movimento de Compra(Alíquota de Crédito)

1300 x 12 = 15.600,00

Cálculo para movimento de Venda(Alíquota de Débito)

1300 x 6 = 7.800,00

* ***Escrituração do Movimento***

A escrituração dos movimentos será feita como de costume onde o usuário deve acessar **| Opções | Escrituração de Lançamentos – RMLIBER |**incluir lote para escrituração e fazer filtro da nota fiscal desejada.

Depois de concluído processo de escrituração, ao acessar o Totvs Gestão Fiscal em **| Cadastro | Manutenção de Lançamentos |** e editar o lançamento fiscal os dados do tributo serão apresentados na aba

|  |
| --- |
| Identificação |
