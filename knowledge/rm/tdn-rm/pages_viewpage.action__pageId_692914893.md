---
content_hash: d0f88124cf880a47ae36ae644dba3462da9dd4d36dd023572a62da4b985317b8
fetched_at: '2026-06-29T00:11:21.344654+00:00'
page_id: '692914893'
product: rm
source: tdn-rm
title: Relatório Gerenciador de Faltas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=692914893
version: 13
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplos de utilização**
3. **Tela Relatório Gerenciador de Faltas**
   1. **Principais Campos e Parâmetros**
   2. **Tipo de Relatório - Índice de Faltas Resumido**
   3. **Tipo de Relatório - Índice de Faltas Detalhado**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

O objetivo do relatório é a criação de uma interface comum para os relatórios de faltas onde o usuário selecionará o relatório que deseja gerar bem como preencher os parâmetros/filtros para a geração do mesmo. Os Relatórios de faltas são utilizados para verificar a quantidade de faltas dos trabalhadores rurícolas, com estes relatórios será feita a análise das faltas e ocorrências no setor de produção.

Serão considerados os registros de funcionários somente aqueles cujo total de faltas no período esteja dentro da faixa informada nos parâmetros/filtros.

* Selecionar a quebra por seção e/ou seleção de funcionários;
* Selecionar o período que o relatório será emitido, informando a data de início e fim do período;
* Marcar para que seja considerado ou não funcionários demitidos no período;
* Marcar para que seja utilizado a tabela de histórico de produção;
* Informar a referência de Médias de Toneladas a ser considerado na emissão do relatório;
* Informar a faixa de indíce de faltas a ser considerado na emissão do relatório;
* Selecionar o Tipo de Relatório que são divididos em layouts diferentes (Índíce de Faltas Resumido ou Índíce de Faltas Detalhado);
* Marcar uma das opções de 'Ref. a Toneladas' se deseja que seja considerado 'Abaixo da', 'Dentro da', 'Acima da Média' e 'Todos';
* Selecionar se a Ordenação será por 'Nome' ou 'Chapa';
* Informar as 'Máscara para seção totalizadora' e 'Máscara para seção na linha de detalhe';

Após informados os campos acima, deverá ser informado/selecionado o Código do Relatório '**FOPREL00199 - Folha Agrária - Relatório de índice de faltas resumido.TotvsReport**' se deseja o relatório gerado por 'Índice de Faltas Resumido' ou '**FOPREL00201 - Folha Agrária - Relatório de índice de faltas detalhado.TotvsReport**' se desejar que o relatório seja gerado por 'Índice de Faltas Detalhado'.

**Observação:** Este relatório deverá ser importado em **Gestão** | **RM Reports**.

No Relatório serão listadas as seguintes linhas e colunas:

**Cabeçalho:**

Será listado o nome do relatório, a referência informada no campo 'Período' da tela de geração, o nome da coligada, a página, a data e hora de geração no formato DDMMAAAA e HHMMSS, respectivamente e o CNPJ da coligada.

**Ordenação:**

A ordenação será pela '**Máscara para seção totalizadora**' e '**Máscara para seção na linha de detalhe**'.

**Campos do Relatório (Linha detalhe/valores)**

**Número de Dias**

**Turma:** Será impresso o código da turma de trabalho;

**Nome da Turma:** Será impresso o Nome da turma de trabalho;

**Atv:** Será impresso quantos funcionários estão Ativos na turma de trabalho;

**Trab:** Será impresso a quantidade de dias trabalhados da turma de trabalho;

**Corte:** Será impresso a quantidade que foi cortada pela turma de trabalho;

**Flt:** Será impresso a quantidade faltas daquela turma de trabalho;

**%:** Será impressa a relação da quantidade de faltas dividido pela quantidade de dias trabalhados pelas toneladas produzidas daquela turma de trabalho;

**Aft:** Será impresso a quantidade afastamentos daquela turma de trabalho;

**Toneladas Médias**

**Tonel.:** Será impressa a quantidade de toneladas produzidas pela turma;

**Até 5:** Será impresso a quantidade de funcionários que produzirão até 5 toneladas;

**5 a 6:** Será impresso a quantidade de funcionários que produzirão de 5 até 6 toneladas;

**+6:** Será impresso a quantidade de funcionários que produzirão Mais de 6 toneladas;

**Ton. Média:** Será impressa a quantidade média de toneladas produzidas pela turma;

## **02. EXEMPLO DE UTILIZAÇÃO**

Foi acessado o menu Folha Agrária | Relatórios | Produção | Gerenciador de Faltas e a base exemplo existem vários casos parametrizados.

Na tela de parâmetros foi parametrizado da seguinte forma:

**Tipo de Relatório - Índice de Faltas Resumido**

Depois de executado apresenta o relatório no seguinte modelo:

**Tipo de Relatório - Índice de Faltas Detalhado**

Depois de executado apresenta o relatório no seguinte modelo:

## **03.****TELA: Gerenciador Relatórios Faltas**

**Principais Campos e Parâmetros**

| Ação | Descrição |
| --- | --- |
| Quebra de seção | Seleciona a seção para a geração do relatório. |
| Seleção de Funcionários | Seleciona os funcionários que deseja gerar no relatório. |
| Período Início e Fim | Seleciona o período que o relatório será emitido, informando a data de início e data de fim. |
| Incluir funcionários demitidos no período | Marque esta opção para que sejam considerados os demitidos do período informado. |
| Utilizar histórico de produção | Marcar a opção se deseja que os dados listados no relatório sejam buscados do histórico de produção . |
| Ref. Média Toneladas | Informar a média de toneladas que deseja que seja levado para o relatório no somatório das toneladas dividido pelo somatório do homem/dia (HOMEMDIA) no período obtido na tabela de produção (PPRODUCAOAGRARIA / PHSTPRODUCAOAGRARIA). |
| Faixa de Índice de Faltas | Informar a faixa de indíce de faltas que deseja que seja levado para o somatório do número de faltas dos funcionários considerando que no dia ativo (útil) não houve produção para cada funcionário monta-se o seu período (de acordo com o período selecionado e admissão/transferência, demissão), se percorre estas datas identificando se o dia é ativo (útil) e se houve produção, caso não exista produção na data então é considerado falta |
| Tipo de Relatório - Índice de Faltas Resumido | Este relatório apresentará o número de dias trabalhados, número de faltas e produção no período onde haverá uma relação entre informações de produção e as informações de dias trabalhados (média, percentual). Este relatório será por seção. |
| Tipo de Relatório - Índice de Faltas Detalhado | Este é um relatório bastante similar ao relatório de faltas resumido (Req. 02 - FOP002469 - Relatório de índice de faltas resumido) onde a diferença maior é que neste relatório serão listados os funcionários e seus dados ao invés de se efetuar a acumulação por seção. |
| Ref. a Toneladas | Marcar uma das opções de 'Ref. a Toneladas' se deseja que seja considerado 'Abaixo da', 'Dentro da', 'Acima da Média' e 'Todos'; |
| Ordenação | * Selecionar se a Ordenação será por 'Nome' ou 'Chapa'; |
| Máscara para seção totalizadora | Informe a máscara da seção que deseja que seja considerada para a totalização dos registros listados. |
| Máscara para seção na linha detalhe | Informe a máscara da seção que deseja que seja considerada para a linha de detalhe dos registros listados. |
| Código do Relatório | Os relatórios “**FOPREL00199 - Folha Agrária - Relatório de índice de faltas resumido.TotvsReport**” e "**FOPREL00201 - Folha Agrária - Relatório de índice de faltas detalhado.TotvsReport**" deverão ser importados em Gestão /  RM Reports para ser selecionado no código do relatório. |

## **04. TABELAS UTILIZADAS**

* PFUNC
* PPESSOA
* PFHSTAFT
* PFHSTSIT
* PFUFERIASPER
* PFHSTFALTA
* PPRODUCAOAGRARIA
* PSECAO
* PFINALIDADETAREFAAGRARIA
* PRGRCALCTAREFAAGRARIA
* PHSTPRODUCAOAGRARIA
* PPRECOPRODUCAO
* PUNIDADEAGRARIA
* PFHSTSEC
