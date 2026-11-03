---
content_hash: 4b0ca581ed11ffe7d9accd581bfef67f7ff81af282ff5b039d59d493697fc194
fetched_at: '2026-06-29T00:10:29.993928+00:00'
page_id: '518473146'
product: rm
source: tdn-rm
title: Livro de Medicamentos Controlados
type: documentation
url: https://tdn.totvs.com/display/LRM/Livro+de+Medicamentos+Controlados
version: 32
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Por meio do livro de medicamentos controlados, os medicamentos poderão ser agrupados conforme a necessidade de cada hospital e das exigências legais aplicadas sobre as substâncias sujeitas a controle especial, conforme a Portaria n.º 344 de 12 de maio de 1998. Os medicamentos controlados devem ser classificados conforme o grau de perigo que pode oferecer à saúde do paciente, caso seja usado indevidamente e sem um controle adequado.

Caso o Gestão Hospitalar esteja integrado com o EMS (Datasul), pode-se configurar a busca da movimentação dos itens controlados da seguinte maneira: se marcar o parâmetro "Utiliza modelo de multifaixas", deve-se informar também o parâmetro "Quantidade permitida de itens que não são controlados dentro de cada faixa". Esses parâmetros seriam para otimizar a busca das movimentações dos produtos, já que a consulta é por faixa de códigos. Caso os códigos dos produtos não sejam sequenciais, dentro de uma faixa única, podem existir muitos itens que não são controlados. Criando múltiplas faixas, o sistema retornará menos itens não controlados para montar o livro.

## **02. EXEMPLO DE UTILIZAÇÃO**

ProcessospreRequisitoPré-Requisitos para Uso do Livro de Medicamentos Controlados

**1 – Configurações gerais do ambiente**

**Preencher as seguintes informações no Gestão Hospitalar:**

1.1 – Cadastro prévio das classificações em: **Cadastros | Estoque | Cadastro de estoques | Classificação de Medicamentos Controlados**;

1.2 – Informar a Classificação de cada Produto em: **Cadastros | Estoque | Produto | Anexo Informações do RM Saúde, no campo “Classificação de Medicamento Controlados”**;

1.3 - Criar os tipos de livros que são mantidos pelo hospital em: **Ambiente |** **Parâmetros | Gestão Hospitalar | Medicamentos Controlados**

### **Configurações**

### **Livro: preencher a aba Identificação e Itens livro medicamento**

## **2 – Processo “Incluir itens no Livro” no menu Farmácia | Consultas e Relatórios | Livro de Medicamentos Controlados**

Importante

No processo “Incluir itens no livro”, as movimentações geradas no BackOffice RM somente serão incluídas como itens do livro, caso estejam registradas na tabela TRELSLD.

No BackOffice, Gestão de Estoque, esta tabela é alimentada pelo processo “Regerar Saldos e Custos” no menu “Estoque/Processos”

Vide mais detalhe do regerar saldos em <https://tdn.totvs.com/x/JMtEGQ>

Resultado da inclusão de itens no livro:

Cadastro do livro

## **Cadastro do livro**

* Acesse Estoques/Consultas e Relatórios/Livro de Medicamentos Controlados.
* Será exibida a tela de cadastro de Livros de Medicamentos Controlados.
* Clique em Novo.
* Selecione o tipo de livro que deseja gerar
* O número do livro será gerado automaticamente ao entrar no campo de número
* Informe o número de páginas (não obrigatório). Visível somente quanto parametrizado a sua utilização
* Selecione a data de abertura e a data de fechamento.
* Pode ser configurado o livro de medicamento por filial

* Caso esteja parametrizado para "Utilizar numeração prévia da quantidade de páginas do livro", o campo "Número de páginas" será exibido

Incluir Itens

## **Incluir itens**

1. Para incluir os itens no livro, selecione o processo "Incluir itens no livro"
   1. Validações para inclusão:
      1. O livro não pode estar impresso
      2. A data de abertura deve estar preenchida
      3. A data de fechamento deve estar preenchida caso não utilize o modelo de numeração prévia das páginas
      4. O livro deve estar vazio
      5. O número de páginas deve estar preenchido se utilizar o modelo de numeração prévia

## **Comportamento na inclusão de itens no Livro de Medicamentos Controlados**

### **Descrição da rotina**

Durante o processo de **inclusão de itens no Livro de Medicamentos Controlados**, o sistema exibirá **todos os itens configurados** como pertencentes ao livro, **incluindo aqueles que não apresentaram movimentação de estoque** no período selecionado.

### **Detalhamento**

* Ao gerar o livro, os itens sem movimentação também serão listados para garantir a **integridade das informações do registro**, mantendo o controle completo de todos os medicamentos vinculados.
* Para esses itens que **não tiveram movimentação de estoque** no período, a **data exibida** será a **data atual**.
* Essa data tem o propósito de indicar que, **no momento da geração do livro**, **não houve movimentação** para o item em questão — apenas sua inclusão como parte da estrutura do livro.

### **Exemplo prático**

Se o livro de medicamentos for gerado para o período de **01/01/2025 a 31/01/2025**, e um determinado item não tiver nenhuma entrada ou saída nesse intervalo, o item será exibido normalmente no relatório com a **data atual** (ex.: 28/10/2025), indicando que **não houve movimentação registrada** no período.

Excluir Itens

## **Excluir itens**

1. Para excluir os itens no livro, selecione o processo "Excluir itens do livro"
   1. Validação para exclusão:
      1. O livro não pode estar impresso

Itens excluídos

Imprimir o livroAtenção

Ao imprimir o livro de medicamento controlado, não será permitido nenhuma alteração em seu cadastro.

- O processo para impressão do relatório somente será habilitado se o perfil do usuário ter permissão de acesso ao item de menu Gestão Hospitalar: Estoque | Consultas e Relatórios | Livro de Medicamentos Controlados | Imprime Livro de Medicamento Controlado.

- Para realizar a impressão, selecione o relatório e escolha uma das opções:

**Visualizar:** o relatório será gerado, mas o campo “Impresso” não será marcado.

**Imprimir:** o relatório será gerado, e o campo “Impresso” será marcado. Uma vez impresso com esta opção, não se pode mais alterar o livro de medicamentos.

- O relatório RM Reports deve possuir os parâmetros CODCOLIGADA, CODLIVRO, NUMEROLIVRO. O tipo do relatório deve ser “Estoques”.

Numeração prévia das páginasImportante

Esta opção só está disponível quanto há a utilização do BackOffice RM juntamente com o Gestão Hospitalar.

Os parâmetros relacionados ao relatório, servem para o sistema calcular a quantidade de itens que irão compor o livro.

Dependendo da estrutura do relatório, os valores desses parâmetros deverão ser ajustados.

* Quantidade de itens por página
  + Representa quantos itens cabem num página do livro, considerando uma página sem cabeçalho e sem quebra por centro de custo
* Quantidade de itens ocupados pelo cabeçalho
  + Representa quantos itens cabem no espaço do cabeçalho, onde tem o nome do produto, o local de estoque e o cabeçalho das colunas
* Quantidade de itens ocupados pela quebra por centro de custo
  + Representa quantos itens cabem no espaço da banda de quebra por centro de custo, onde tem o

   Configuração de Kit para exibir nome do pacienteUtilização de Kit

O livro de medicamentos controlados não contempla a utilização de medicamentos controlados em kit, com exceção aos clientes que utilizem BackOffice RM do Gestão de Estoque.

Importante

Esta opção só está disponível quanto há a utilização do BackOffice RM juntamente com o Gestão Hospitalar.

Ao dar baixa no kit pré-montado, o RM Saúde enviará ao RM Nucleus as informações da movimentação para que ao gerar o relatório de ficha física financeira o número da movimentação gerado no saúde seja identificado.

Com essa informação compartilhada, as informações que compõe o livro serão geradas com os complementos do atendimento do paciente, incluindo o nome.

Configuração no RM Saúde (Delphi)

Gestão hospitalar→ Integrações→ Configurações gerais 1/5

Configuração do tipo de movimentação que baixa kit no RM Nucleus (MDI)

BackOffice → Gestão de Estoque, Compras e Faturamento → Ambiente → Configurações → Parâmetros → Gestão de Estoque, Compras e Faturamento.

Integração Protheus

Configuração RM X Protheus

**05. TABELAS UTILIZADAS**

* SZLIVROMEDCTRL
  + Contém os dados do livro de medicamentos controlados
* SZITMLIVROMEDCTRL
  + Contém os itens movimentados do livro
* SZITMLIVROMEDCTRLNAOMOV  
  + Contém os itens não movimentados

]]>
