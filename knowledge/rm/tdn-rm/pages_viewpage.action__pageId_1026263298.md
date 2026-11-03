---
content_hash: ddcb50b9df56e2e9873427ba8158e6044c0965d9c311c57e05383798f987f7ba
fetched_at: '2026-06-29T00:05:48.644839+00:00'
page_id: '1026263298'
product: rm
source: tdn-rm
title: Folha Analítica - Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1026263298
version: 12
---

false

**A partir das Versões:**

* [DT - Smart View - Folha Analítica](https://tdn.totvs.com/pages/viewpage.action?pageId=1026263525)
* Vídeo How Too

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Mapeamentos dos campos**
4. **Demais Informações**

## **01. VISÃO GERAL**

## Objetivo

A **Folha Analítica** é um relatório detalhado da folha de pagamento que, em conformidade com a CLT (Consolidação das Leis do Trabalho), apresenta todos os eventos de proventos, descontos e bases de cálculo de cada colaborador. Consolidando-se como uma ferramenta essencial de gestão, o documento permite uma análise precisa de cada lançamento e facilita a identificação de inconsistências. Seu objetivo principal é fornecer transparência sobre a composição dos valores pagos e descontados, garantindo segurança na conferência e identificação de inconsistência da folha.

## **02. EXEMPLO DE UTILIZAÇÃO**

11Importação do LeiauteImportação do Leiaute

1) Acesse RH | Folha de Pagamento | Gestão | Smart View, e realize a importação do relatório.

true2Geração FilialGeração Filial

Acesse  RH | Folha de Pagamento | Folha Mensal | Folha analítica

**Código do Relatório SmartView**

Vincule o leiaute smartView para a geração.

**Quebra de Seção**   
Permite filtrar as filiais que serão consideradas na Folha Analítica, selecionando uma filial específica de acordo com seu código ou utilizando uma determinada quebra de filial.  
   
**Seleção de Funcionários**   
Permite filtrar os funcionários lotados nas seções referentes à quebra de seção escolhida. O filtro pode ser de acordo com a 'Situação', 'Tipo de Funcionário' ou 'Recebimento'.  
   
**Competência**  
Permite selecionar para qual competência a Folha Analítica será gerada, assim como o caixa e período.

**Atenção:**

Ao selecionar uma competência anterior à atual, a **situação considerada para cada funcionário será a última daquela competência**, de acordo com seu respectivo histórico de situação. Uma vez que a situação de funcionários voltando ou saindo de férias ('F - Férias') ou afastamento do tipo ('P - Af. Previdência', 'T - Af. Ac. Trabalho', 'O - Doença Ocupacional', 'M - Serv. Militar', 'L - Licença s/ venc', 'E - Licença Mater.', 'R - Licença Remun.', 'I - Apos. Invalidez', 'U - Outros', 'S - Mandato Sindical', 'W - Licença Mater. Compl. 180 dias', 'Y - Licença Paternidade') na competência atual é atualizada durante o processo de 'Liberação de Competência', ele pode estar em situação de afastamento antes da execução do processo e ter sua situação alterada para 'A - Ativo' após a execução (ou vice-versa). Assim, deve-se ficar atento ao gerar uma Folha Analítica referente a competências retroativas, pois alguns funcionários antes selecionados pelo filtro de situação e que constavam como afastados (ou ativos) nos contadores de funcionários da 'Seção' e 'Geral', podem constar como ativos (ou afastados) e possivelmente não atender mais ao filtro.

**Imprimir Funcionários Sem Movimentação**  
Ao marcar o parâmetro, o sistema irá trazer todos os funcionários que não possuem movimentação para o período selecionado. Para que seja possível marcar esse parâmetro, a folha analítica deve ser gerada por filial. Ao gerar por centro de custo, o parâmetro é desabilitado automaticamente.

**Filtrar Base de FGTS de Afastados por Período**  
Com esse parâmetro marcado, o sistema exibirá os totais apenas das seções onde há funcionários com movimento no período (considerando o fato de que o parâmetro "Imprimir Funcionários Sem Movimentação" esteja desmarcado. Com o parâmetro "Filtrar Base de FGTS de Afastados por Período" desmarcado, o sistema continuará exibindo totais de seções contendo base de FGTS de afastados, mesmo que a seção não tenha funcionários com movimento no período selecionado. Isso ocorre apenas se houver funcionários com afastamento do tipo "T - Acidente de Trabalho", "M - Serviço Militar" e "O - Doença Ocupacional" lotados na seção, uma vez que mesmo que os funcionários em tais situações não tenham movimento, a empresa precisa continuar depositando o FGTS deles.

**Considera Percentuais para INSS da Seção Centralizadora (SAT/Terceiros)**

Marque a opção, caso queira que seja considerado os percentuais de INSS (SAT e Terceiros) da seção centralizadora ao invés dos percentuais cadastrados na seção onde o funcionário estiver lotado.

falseATENÇÃO!

Quando os parâmetros "Habilita Histórico de INSS no cadastro de seção" e "Discriminar Percentual de Terceiros" em **Parametrizador | Folha Normal | Encargos Sociais**estiver marcado, a geração da folha analítica no campo de terceiros sempre irá considerar os dados do cadastro **Administração de Pessoal | Cadastros | Seções | Anexos | Histórico de Percentuais para INSS** Aba **percentuais de terceiros** das seções centralizadoras.

Mais informações:  [Habilita Histórico de INSS no Cadastro de Seção.](https://tdn.totvs.com.br/pages/releaseview.action?pageId=496388652)

**Desconsidera da 'Base FGTS' as verbas pagas por Dissídio**

Ao marcar esta opção, a folha analítica será gerada sem considerar as verbas pagas por dissídio nas bases de FGTS.

**Considera envelopes de retificação anterior à admissão por transferência**

Ao marcar esta opção, ao gerar a folha analítica de competências anteriores, o sistema também passará a considerar os envelopes de retificação lançados para os funcionários que foram admitidos por transferência.

**Totais de Funcionário**  
É possível selecionar quais bases de cálculo serão levadas para os totalizadores do relatorio.

**Importante:** **Totais de  Seção e Gerais não são utilizados na Folha Analítica - Smart View**

**Resumo do Funcionário - Fórmulas**

O campo **"Resumo Funcionário – Fórmulas"** da folha analítica permite a personalização de até 15 campos para exibição de dados relacionados ao colaborador. É possível incluir informações provenientes do banco de dados, como salário base, horas extras, adicionais, entre outros, que podem ser utilizados diretamente nas fórmulas.

Exemplo do novo relatorio

3Geração centro de custo Geração centro de custo 

Acesse o menu

**Código do Relatório SmartView**

Vincule o leiaute smartView para a geração.

**Imprimir por Centro de Custo**  
Ao marcar esta opção os seguintes campos serão habilitados.

**Centro de Custo - Usar código de quebra**

O sistema verifica a movimentação por centro de custo de todos os funcionários, desde que o código do centro de custo esteja dentro da quebra informada ou em quebra superior. Tratamento semelhante ao da quebra por seção.

**Exemplo:**

| Funcionário | Centro de Custo |
| --- | --- |
| 00001 | 02 |
| 00002 | 02.1 |
| 00003 | 02.1.1 |
| 00004 | 02.1.2 |
| 00005 | 01 |
| 00006 | 01.1.1 |
| 00007 | 03.1 |
| 00008 | 03.1.2 |

Informando a quebra 02, o sistema irá gerar os funcionários: 00001, 00002, 00003 e 00004;  
Informando a quebra ??, o sistema irá gerar todos os funcionários;  
Informando a quebra 02.1, o sistema irá gerar os funcionários: 00002, 00003 e 00004;  
Informando a quebra 0?.1, o sistema irá gerar os funcionários: 00002, 00003, 00004, 00006, 00007 e 00008.  
Caso no rateio fixo do funcionário 00003 tenha dois centros de custos informados (02.1.1 e 02.1) ao imprimir a folha analítica informando a quebra 0?.1, a movimentação do funcionário será agrupada.

**Atenção:**  
O sistema sempre irá quebrar por filial dentro da quebra de centro de custo.

**Seleção de Funcionários**   
Permite filtrar os funcionários lotados nas seções referentes à quebra de seção escolhida. O filtro pode ser de acordo com a 'Situação', 'Tipo de Funcionário' ou 'Recebimento'.  
   
**Competência**  
Permite selecionar para qual competência a Folha Analítica será gerada, assim como o caixa e período.

**Atenção:**

Ao selecionar uma competência anterior à atual, a **situação considerada para cada funcionário será a última daquela competência**, de acordo com seu respectivo histórico de situação. Uma vez que a situação de funcionários voltando ou saindo de férias ('F - Férias') ou afastamento do tipo ('P - Af. Previdência', 'T - Af. Ac. Trabalho', 'O - Doença Ocupacional', 'M - Serv. Militar', 'L - Licença s/ venc', 'E - Licença Mater.', 'R - Licença Remun.', 'I - Apos. Invalidez', 'U - Outros', 'S - Mandato Sindical', 'W - Licença Mater. Compl. 180 dias', 'Y - Licença Paternidade') na competência atual é atualizada durante o processo de 'Liberação de Competência', ele pode estar em situação de afastamento antes da execução do processo e ter sua situação alterada para 'A - Ativo' após a execução (ou vice-versa). Assim, deve-se ficar atento ao gerar uma Folha Analítica referente a competências retroativas, pois alguns funcionários antes selecionados pelo filtro de situação e que constavam como afastados (ou ativos) nos contadores de funcionários da 'Seção' e 'Geral', podem constar como ativos (ou afastados) e possivelmente não atender mais ao filtro.

**Imprimir Funcionários Sem Movimentação**  
Ao marcar o parâmetro, o sistema irá trazer todos os funcionários que não possuem movimentação para o período selecionado. Para que seja possível marcar esse parâmetro, a folha analítica deve ser gerada por filial. Ao gerar por centro de custo, o parâmetro é desabilitado automaticamente.

**Filtrar Base de FGTS de Afastados por Período**  
Com esse parâmetro marcado, o sistema exibirá os totais apenas das seções onde há funcionários com movimento no período (considerando o fato de que o parâmetro "Imprimir Funcionários Sem Movimentação" esteja desmarcado. Com o parâmetro "Filtrar Base de FGTS de Afastados por Período" desmarcado, o sistema continuará exibindo totais de seções contendo base de FGTS de afastados, mesmo que a seção não tenha funcionários com movimento no período selecionado. Isso ocorre apenas se houver funcionários com afastamento do tipo "T - Acidente de Trabalho", "M - Serviço Militar" e "O - Doença Ocupacional" lotados na seção, uma vez que mesmo que os funcionários em tais situações não tenham movimento, a empresa precisa continuar depositando o FGTS deles.

**Considera Percentuais para INSS da Seção Centralizadora (SAT/Terceiros)**

Marque a opção, caso queira que seja considerado os percentuais de INSS (SAT e Terceiros) da seção centralizadora ao invés dos percentuais cadastrados na seção onde o funcionário estiver lotado.

falseATENÇÃO!

Quando os parâmetros "Habilita Histórico de INSS no cadastro de seção" e "Discriminar Percentual de Terceiros" em **Parametrizador | Folha Normal | Encargos Sociais**estiver marcado, a geração da folha analítica no campo de terceiros sempre irá considerar os dados do cadastro **Administração de Pessoal | Cadastros | Seções | Anexos | Histórico de Percentuais para INSS** Aba **percentuais de terceiros** das seções centralizadoras.

Mais informações:  [Habilita Histórico de INSS no Cadastro de Seção.](https://tdn.totvs.com.br/pages/releaseview.action?pageId=496388652)

**Desconsidera da 'Base FGTS' as verbas pagas por Dissídio**

Ao marcar esta opção, a folha analítica será gerada sem considerar as verbas pagas por dissídio nas bases de FGTS.

**Considera envelopes de retificação anterior à admissão por transferência**

Ao marcar esta opção, ao gerar a folha analítica de competências anteriores, o sistema também passará a considerar os envelopes de retificação lançados para os funcionários que foram admitidos por transferência.

**Totais de Funcionário**  
É possível selecionar quais bases de cálculo serão levadas para os totalizadores do relatorio.

**Importante:** **Totais de  Seção e Gerais não são mais utilizados na Folha Analítica - Smart View**

**Resumo do Funcionário - Fórmulas**

O campo **"Resumo Funcionário – Fórmulas"** da folha analítica permite a personalização de até 15 campos para exibição de dados relacionados ao colaborador. É possível incluir informações provenientes do banco de dados, como salário base, horas extras, adicionais, entre outros, que podem ser utilizados diretamente nas fórmulas.

Exemplo do novo relatorio

4Execução SmartViewExecução SmartView

Nesse relatório temos os seguintes filtros disponíveis:

| Campo | Descrição do Campo | Campo na Tabela |
| --- | --- | --- |
| Código da Coligada | Código da Coligada |  |
| Matrícula | Filtra pela matrícula do funcionário. | PFUNC.CHAPA |
| Situação do Funcionário | Filtra pelo codigo de situação | PFUNC.CODSITUACAO |
| Mês Competência | Mês da competência que será gerado o relátorío |  |
| Ano Competência | Ano da competência que será gerado o relátorío |  |
| Mês Caixa | Mês caixa que será gerado o relátorío |  |
| Período | Períodos que serão considerados no relátorío |  |
| Seção | Filtra o código da seção de lotação do funcionário. | PFUNC.CODSECAO |
| Fórmulas | Vincule as fórmulas para calculo, vinculação de até 15 fórmulas | GFORMULA |
| Base e Totais | Marque as bases ou totais a serem impressas nos totalizadores por funcionário, filial ou centro de custo e empresa |  |
| Percentual Empresa | Cadastre o percentual que será considerado para calculo empresa |  |
| Código Situação | Filtra pelo código de situação do funcionário. | PFUNC.CODSITUACAO |
| Quebra por centro de custo | Ao marcar como verdadeiro o sistema irá gerar a folha analitica por centro de custo caso seja a opção falso será gerado pela quebra de filial |  |
| Filial | Filtra pela Filial | PFUNC.FILIAL |
| Imprimir eventos zerados | Ao marcar como verdadeiro o sistema irá trazer os eventos de valor zerado do envelope de pagamento, caso seja falso não será impresso os eventos |  |
| Imprimir eventos de base | Ao marcar como verdadeiro o sistema irá trazer os eventos do tipo base de calculo do envelope de pagamento na coluna bases/outros eventos, caso seja falso não será impresso os eventos |  |
| Imprimir Funcionarios sem movimentação | Ao marcar como verdadeiro o sistema irá listar os funcionários mesmo que não possuam movimentação, caso seja falso não será impresso |  |
| Verificar autônomos Gestão financeira | Ao marcar como verdadeiro o sistema vai trazer a lista no final de cada filial listando os autônomos |  |
| Verificar autônomos Externos (Outros backoffices) | Ao marcar como verdadeiro o sistema vai trazer a lista no final de cada filial listando os autônomos |  |
| Filtrar base de afastados do período | Com esse parâmetro marcado, o sistema exibirá os totais apenas das seções onde há funcionários com movimento no período (considerando o fato de que o parâmetro "Imprimir Funcionários Sem Movimentação" esteja desmarcado. Com o parâmetro "Filtrar Base de FGTS de Afastados por Período" desmarcado, o sistema continuará exibindo totais de seções contendo base de FGTS de afastados, mesmo que a seção não tenha funcionários com movimento no período selecionado. Isso ocorre apenas se houver funcionários com afastamento do tipo "T - Acidente de Trabalho", "M - Serviço Militar" e "O - Doença Ocupacional" lotados na seção, uma vez que mesmo que os funcionários em tais situações não tenham movimento, a empresa precisa continuar depositando o FGTS deles. |  |
| Desconsidera da base FGTS as verbas pagas por dissidio | Ao marcar esta opção como verdadeiro, a folha analítica será gerada sem considerar as verbas pagas por dissídio nas bases de FGTS. |  |
| Considera envelopes de retificação anterior à admissão por transferência | Ao marcar esta opção, ao gerar a folha analítica de competências anteriores, o sistema também passará a considerar os envelopes de retificação lançados para os funcionários que foram admitidos por transferência. |  |
| Ordenar funcionários por nome (falso ordena por chapa) | Ao marcar esta opção como verdadeiro, a ordenação será realizado pelo nome, caso falso a ordenção será por chapa |  |
| Codigo de quebra | é necessario colocar o coligo de quebra para a geração deve correponder a quabra da filial ou centro de custo |  |
| ID do filtro de seleção | utilizado somente para a geração em processo |  |

1) Acesse RH | Folha de Pagamento | Gestão | Smart View, para geração do relatório.

selecione o relatório e clique em executar no Smart View

Cadastre os filtros  e, em seguida, clique em 'Enviar' para iniciar o processo de geração do relatório. 

Sistema apresentará o novo relatório

## **Centro de custo**

**Lista funcionário**

**Totalização por centro de custo / filial**

será apresentado o valor total de cada centro de custo 

Totalizando o valor Proventos | Descontos | Bases / Outros valores | Bases de cálculo | Totais | Fórmulas

**Total empresa**

# **Filial**

## **Lista funcionário**

## **Totalização por filial**

será apresentado o valor total de cada filial 

Totalizando o valor Proventos | Descontos | Bases / Outros valores | Bases de cálculo | Totais | Fórmulas

## **Total empresa**

5MapeamentoMapeamento

|  |  |  |
| --- | --- | --- |
| DADOS EMPRESARIAIS | | |
| Nome da empresa | GCOLIGADA.NOMEFANTASIA |  |
| CNPJ / CPF | GCOLIGADA.CGC |  |
| Estabelecimento (Filial) | GFILIAL.CNPJ - GFILIAL.NOMEFANTASIA |  |
| DADOS CADASTRAIS | | |
| Tipo de folha | PFUNC.CODRECEBIMENTO |  |
| Nome da pessoa colaboradora | PPESSOA.NOMESOCIAL OU PFUNC.NOME |  |
| Matrícula | PFUNC.CHAPA |  |
| Cargo/Função | PFUNC.CODFUNCAO, PFUNCAO.DESCRICAO |  |
| Centro de custo | PFRATEIOFIXO.CODCCUSTO |  |
| Data de pagamento | PFFINANC.DTPAGTO |  |
| Salário bruto | PFUNC.SALARIO |  |
| Data de admissão | PFUNC.DATAADMISSAO |  |
| Categoria/Carga horária | PFUNC.CODRECEBIMENTO / PFUNC.JORNADA\_MENSAL |  |
| Data de desligamento | PFUNC.DATADEMISSAO |  |
| Dependentes do IR |  |  |
| Dependentes Salário-Família |  |  |
| Eventos envelope | | |
| Proventos | PFFINANC | Eventos do tipo provento |
| Descontos | PFFINANC | Eventos do tipo Desconto |
| Bases / Outros valores | PFFINANC | Eventos do tipo Base de calculo |
| Base de cálculo | | |
| Base FGTS | PFPERFF |  |
| Base INSS - Envelope | PFPERFF |  |
| Base INSS 13º Ñ Exp. Risco | PFPERFF | BaseINSS13GPS |
| Base INSS 20 Anos | Calculado |  |
| Base INSS 13º 25 Anos | PFPERFF | BaseINSS13GPS |
| Base Sal. Fam. | PFPERFF |  |
| Base IRRF 13º | PFPERFF |  |
| Base FGTS Resc. eSocial | PFPERFF |  |
| Base FGTS 13º | PFPERFF |  |
| Base INSS 13º - Envelope | PFPERFF |  |
| Base INSS 15 Anos | PFPERFF | BaseINSS13GPS |
| Base INSS 13º 20 Anos | PFPERFF | BaseINSS13GPS |
| Base INSS Pro-Labore | PFPERFF |  |
| Base IRRF | PFPERFF |  |
| Base IRRF PLR | PFPERFF |  |
| Base FGTS 13º Resc. eSocial | PFPERFF |  |
| Base FGTS Afast. | PFPERFF |  |
| Base INSS Ñ Exp. Risco | PFPERFF | BaseINSS13GPS |
| Base INSS 13º 15 Anos | PFPERFF | BaseINSS13GPS |
| Base INSS 25 Anos | PFPERFF | BaseINSS13GPS |
| Base INSS Auton. | PFPERFF |  |
| Base IRRF Férias | PFPERFF |  |
| Base FGTS Indeniz. eSocial | PFPERFF |  |
| Base FGTS Ind Resc. eSocial | PFPERFF |  |
| Totais | | |
| Proventos | Calculado |  |
| Descontos | Calculado |  |
| Valor líquido a receber | Calculado |  |
| Estorno INSS | PFPERFF |  |
| FGTS 13º | PFPERFF |  |
| FGTS | PFPERFF |  |
| FGTS 13º Rescisório | Calculado |  |
| FGTS Indenizado | Calculado |  |
| FGTS Indenizado Rescisório | Calculado |  |
| FGTS Rescisório | Calculado |  |
| INSS (Emp + SAT\_Ajust + Terc) | Calculado |  |
| INSS SAT | Calculado |  |
| INSS Empresa | Calculado | Perc. Empresa |
| INSS SAT Ajustado | Calculado |  |
| INSS Segurado | Calculado |  |
| INSS Terceiro | Calculado |  |
| Fórmulas | | |
| Fórmulas | GFORMULA | é possivél associar até 15 fórmulas |

## **03.** **DEMAIS INFORMAÇÕES**

* [Considerar histórico de situação de funcionário ao gerar Folha Analítica na competência atual](https://tdn.totvs.com/pages/viewpage.action?pageId=1005899558)
* [Nome Social](https://tdn.totvs.com/pages/viewpage.action?pageId=1006410450)
