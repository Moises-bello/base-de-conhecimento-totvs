---
content_hash: 71e173f12a0ded17c190d422ac1d53baeb66b59aa1e6b913d1339e577449e8f3
fetched_at: '2026-06-29T00:11:17.921891+00:00'
page_id: '681311298'
product: rm
source: tdn-rm
title: Rendimentos de Trabalhador Rural por Setor e Lote
type: documentation
url: https://tdn.totvs.com/display/LRM/Rendimentos+de+Trabalhador+Rural+por+Setor+e+Lote
version: 13
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tela Rendimentos de Trabalhador Rural por Setor e Lote**
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O relatório tem o objetivo de apresentar as informações de produção e valores pagos aos funcionários considerando as tarefas selecionadas pelo usuário nos campos e parâmetros de tela.

As informações serão agrupadas e totalizadas por Total de Trabalhadores, valor ganho, empreita/dia, informações de produção (por metros produzidos, área, toneladas, média destes valores com relação ao total de trabalhadores). Essas informações serão recuperadas e apresentadas ao final da geração do relatório e agrupadas, detalhadas e totalizadas por seção. Para emitir os relatórios deverão ser informados os seguintes campos na tela de geração:

* Selecionar a quebra por seção e/ou seleção de funcionários;
* Selecionar o período que o relatório será emitido, informando a data de início e fim do período e se deseja que seja utilizado ou não o histórico de produção;
* Informar o percentual de direitos;
* Selecionar as tarefas desejadas para a geração do relatório;
* Selecionar os valores as serem considerados (efetivamente pago ou realmente apurado);
* Informar a mascara unidade agrária totalizadora e a mascara seção na linha detalhe;

Após informados os campos acima, deverá ser informado/selecionado o Código do Relatório '**FOPREL00197 - Folha Agrária - Rendimentos de Trabalhador Rural por Setor e Lote.TotvsReport**'.

**Observação:** Este relatório deverá ser importado em **Gestão** | **RM Reports**.

Informar as Finalidades das tarefas que serão consideradas para Empreita/Diária que serão levadas para o relatório.

Informar os Eventos a serem considerados na coluna Ganho total.

No Relatório serão listadas as seguintes linhas e colunas:

**Cabeçalho:**

Será listado o nome do relatório, a referência informada no campo 'Período' da tela de geração, o nome da coligada, a página, a data e hora de geração no formato DDMMAAAA e HHMMSS, respectivamente e o CNPJ da coligada.

**Ordenação:**

A ordenação será por **Código da Unidade Agrária** e **Código de Seção**.

**Campos do Relatório (Linha detalhe/valores)**

**Cidade** - Nome da seção que deverá coincidir com a máscara informada no campo 'Máscara para seção na  linha de detalhe' (seção da Unidade Agrária da produção);

**Trab** - Somatório do número de funcionários que tiveram produção dia a dia para eventos de corte (onde a finalidade de regra de cálculo representa uma finalidade de corte) e de acordo com a seção (cidade) referente à unidade agrária onde a produção esteja vinculada ao preço unitário da produção;

**Valor ganho (Vlr Ganho)** - Somatório da quantidade produzida multiplicada pelo preço unitário, para eventos de corte (considerando os parâmetros/filtros selecionados no relatório) onde o preço unitário será determinado pelo parâmetro/filtro 'Valor a ser considerado' que poderá ser 'Valor efetivamente pago', ou seja, o preço unitário será o preço pago ou 'Valor realmente apurado', onde o preço unitário será o valor real;

**Média Sem Direito (Média S/D)** - Calculado a partir do valor do campo '**Valor ganho**' divido pelo campo **Trab**;

**Empreita/Diária (Empr/Dia)** - Somatório do valor na produção das tarefas em que na regra de cálculo e a finalidade seja uma das finalidades selecionadas no parâmetro do relatório (finalidades para empreita/diária) e a este valor adiciona-se o '**Valor ganho**' e desta adição deve-se dividir pelo campo '**Trab**';

**Média Com direitos (Média C/D)** - Calculado com base no valor da '**Média Sem Direito**' e aplica-se a este valor o percentual definido no parâmetro/filtro '**Percentual de direitos**';

**Metros** - Somatório da quantidade produzida para os eventos de corte onde a produção contém preço unitário da produção definido;

**Média Mts** - Será obtido a partir do cálculo de '**Metros**' dividido pelo '**Trab**';

**Área** -  Somatório '**Metros**' dividido pelo espaçamento linear da unidade agrária da produção;

**Toneladas** - Será o somatório para eventos de corte da quantidade produzida multiplicada pelo preço Kg/Metro dividido por 1000 onde o preço Kg/Metro será determinado pelo parâmetro/filtro “Valor a ser considerado”:

a) Caso esteja marcado como “Valor efetivamente pago” então o preço será **Kg Metro Pago** (tabela PPRECOPRODUCAO). Toneladas = (quantidade produzida \* **Kg Metro Pago**) / 1000**;**

b) Caso esteja marcado como “Valor realmente apurado” então o valor a ser utilizado para preço será o **Kg Metro Real** (tabela PPRECOPRODUCAO). Toneladas = (quantidade produzida \* **Kg Metro Real**) / 1000.

**Observação:**

Em ambos os casos os valores de produção estarão vinculados ao preço unitário da produção.

**Média/Toneladas (Média Ton)** -  Calculado com base nas 'Toneladas' dividido pelo valor recuperado pelo somatório de homens/dia da tabela de produção;

**Campos do Relatório (Subtotal da unidade agrária - Linha detalhe/Totalizador)**

**Nome da Seção -** Será preenchido com o nome da seção de acordo com o código da seção informado na máscara do campo 'Máscara para unidade agrária totalizadora'. As informações deste campo serão buscadas do cadastro de seção.

**Observação:**

Para cada coluna de valores na linha de detalhe deverá proceder conforme regra de cálculo informada em cada campo.

**Campos do Relatório (Totalizador geral)**

Para cada coluna de valores do Totalizador geral deverá proceder conforme regra de cálculo informada para cada campo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Foi acessado o menu Folha Agrária | Relatórios | Produção | Rendimentos de Trabalhador Rural por Setor e Lote e a base exemplo onde existem vários casos parametrizados.

Na tela de parâmetros foi parametrizado da seguinte forma:

Depois de executado apresenta o relatório no seguinte modelo:

## **03.****TELA: Rendimentos de Trabalhador Rural por Setor e Lote**

**Principais Campos e Parâmetros**

| Ação | Descrição |
| --- | --- |
| Quebra de seção | Seleciona a seção para a geração do relatório. |
| Seleção de Funcionários | Seleciona os funcionários que deseja gerar no relatório. |
| Valor efetivamente pago | Marque esta opção, caso queira que seja considerado o preço unitário como preço pago no campo Valor ganho e no somatório do campo Toneladas. |
| Valor realmente apurado | Marque esta opção, caso queira que seja considerado o preço unitário como Valor real no campo Valor ganho e no somatório do campo Toneladas. |
| Período | Seleciona o período que o relatório será emitido. |
| Utilizar histórico de produção | Marcar a opção se deseja que os dados listados no relatório sejam buscados do histórico de produção. |
| Percentual de direitos | Informe o percentual de direitos para a geração do relatório. |
| Tarefa | Seleciona a Tarefa que o relatório será emitido. |
| Mascara unidade agrária totalizadora | Informe a máscara da unidade agrária que deseja que seja considerada para a totalização dos registros listados. |
| Mascara seção na linha detalhe | Informe a máscara da seção que deseja que seja considerada para a linha de detalhe dos registros listados. |
| Código do Relatório | O relatório “FOPREL00197 - Folha Agrária - Rendimentos de trabalhador rural por setor e lote” deve ser importado em Gestão /  RM Reports para ser selecionado no código do relatório. |

## **04. TABELAS UTILIZADAS**

* PFUNC
* VTAREFA
* PFHSTSIT
* PPESSOA
* PPRODUCAOAGRARIA
* PSECAO
* PFINALIDADETAREFAAGRARIA
* PRGRCALCTAREFAAGRARIA
* PHSTPRODUCAOAGRARIA
* PPRECOPRODUCAO
* PUNIDADEAGRARIA
