---
content_hash: 4fda75c79ddccf97aa97e2d3c7389f3a450e76736f8433c81573fe3cdd404bdc
fetched_at: '2026-06-29T00:10:06.804569+00:00'
page_id: '452719339'
product: rm
source: tdn-rm
title: Folha Analítica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719339
version: 20
---

## Objetivo

A folha analítica, conforme a CLT (Consolidação das Leis do Trabalho), é um relatório detalhado da folha de pagamento que mostra todos os eventos (proventos, descontos e bases de cálculo) de cada funcionário em um determinado período. É um documento essencial para a conferência e gestão da folha de pagamento, permitindo uma análise minuciosa de todos os valores envolvidos. 

O objetivo da folha analítica é fornecer um detalhamento minucioso dos eventos de cálculo da folha de pagamento de um funcionário, permitindo uma análise precisa de cada lançamento e seus valores. Esse relatório detalhado facilita a conferência dos cálculos, a identificação de inconsistências e a compreensão completa da composição dos valores pagos e descontados. 

**Quebra de Seção**   
Permite filtrar as seções que serão consideradas na Folha Analítica, selecionando uma seção específica de acordo com seu código ou utilizando uma determinada quebra de seção.  
   
**Seleção de Funcionários**   
Permite filtrar os funcionários lotados nas seções referentes à quebra de seção escolhida. O filtro pode ser de acordo com a 'Situação', 'Tipo de Funcionário' ou 'Recebimento'.  
   
**Competência**  
Permite selecionar para qual competência a Folha Analítica será gerada, assim como o caixa e período.

**Atenção:**

Ao selecionar uma competência anterior à atual, a **situação considerada para cada funcionário será a última daquela competência**, de acordo com seu respectivo histórico de situação. Uma vez que a situação de funcionários voltando ou saindo de férias ('F - Férias') ou afastamento do tipo ('P - Af. Previdência', 'T - Af. Ac. Trabalho', 'O - Doença Ocupacional', 'M - Serv. Militar', 'L - Licença s/ venc', 'E - Licença Mater.', 'R - Licença Remun.', 'I - Apos. Invalidez', 'U - Outros', 'S - Mandato Sindical', 'W - Licença Mater. Compl. 180 dias', 'Y - Licença Paternidade') na competência atual é atualizada durante o processo de 'Liberação de Competência', ele pode estar em situação de afastamento antes da execução do processo e ter sua situação alterada para 'A - Ativo' após a execução (ou vice-versa). Assim, deve-se ficar atento ao gerar uma Folha Analítica referente a competências retroativas, pois alguns funcionários antes selecionados pelo filtro de situação e que constavam como afastados (ou ativos) nos contadores de funcionários da 'Seção' e 'Geral', podem constar como ativos (ou afastados) e possivelmente não atender mais ao filtro.

**Imprimir Funcionários Sem Movimentação**  
Ao marcar o parâmetro, o sistema irá trazer todos os funcionários que não possuem movimentação para o período selecionado. Para que seja possível marcar esse parâmetro, a folha analítica deve ser gerada por seção. Ao gerar por centro de custo, o parâmetro é desabilitado automaticamente.

**Filtrar Base de FGTS de Afastados por Período**  
Com esse parâmetro marcado, o sistema exibirá os totais apenas das seções onde há funcionários com movimento no período (considerando o fato de que o parâmetro "Imprimir Funcionários Sem Movimentação" esteja desmarcado. Com o parâmetro "Filtrar Base de FGTS de Afastados por Período" desmarcado, o sistema continuará exibindo totais de seções contendo base de FGTS de afastados, mesmo que a seção não tenha funcionários com movimento no período selecionado. Isso ocorre apenas se houver funcionários com afastamento do tipo "T - Acidente de Trabalho", "M - Serviço Militar" e "O - Doença Ocupacional" lotados na seção, uma vez que mesmo que os funcionários em tais situações não tenham movimento, a empresa precisa continuar depositando o FGTS deles.

**Considera Percentuais para INSS da Seção Centralizadora (SAT/Terceiros)**

Marque a opção, caso queira que seja considerado os percentuais de INSS (SAT e Terceiros) da seção centralizadora ao invés dos percentuais cadastrados na seção onde o funcionário estiver lotado.

falseATENÇÃO!

Quando os parâmetros "Habilita Histórico de INSS no cadastro de seção" e "Discriminar Percentual de Terceiros" em **Parametrizador | Folha Normal | Encargos Sociais**estiver marcado, a geração da folha analítica no campo de terceiros sempre irá considerar os dados do cadastro **Administração de Pessoal | Cadastros | Seções | Anexos | Histórico de Percentuais para INSS** Aba **percentuais de terceiros** das seções centralizadoras.

Mais informações:  [Habilita Histórico de INSS no Cadastro de Seção.](https://tdn.totvs.com.br/pages/releaseview.action?pageId=496388652)

**Desconsidera da Base FGTS as verbas pagas por Dissídio**

Este parâmetro define como os valores relacionados a dissídio serão considerados na composição da base de cálculo do FGTS na geração do relatório Folha Analítica.

Quando habilitado, o sistema amplia as regras de desconsideração da base de FGTS, impactando diretamente o valor total apurado.

Parâmetro desmarcado:  
O sistema soma os valores das verbas com incidência de FGTS e deduz apenas os eventos que possuem incidência de estorno.  
  
Parâmetro marcado:  
O sistema soma os valores das verbas com incidência de FGTS e deduz os eventos com incidência de estorno, desconsiderando da base os valores dos eventos vinculados aos seguintes códigos de cálculo:

* + **69** – Diferença de Dissídio
  + **111** – Estorno de FGTS
  + **410** – Diferença de FGTS (Dissídio)
  + **354 -** Diferença da Base de FGTS de Afastados

**Considera envelopes de retificação anterior à admissão por transferência**

Ao marcar esta opção, ao gerar a folha analítica de competências anteriores, o sistema também passará a considerar os envelopes de retificação lançados para os funcionários que foram admitidos por transferência.

**Imprimir por Centro de Custo**  
Ao marcar esta opção os seguintes campos serão habilitados.

**Centro de Custo - Usar filtro**

O sistema filtra os centros de custo dos funcionários considerando somente os de tamanho igual ou inferior ao tamanho do filtro informado, além de comparar cada caractere do centro de custo com máscara do filtro.

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

Informando o filtro 02, o sistema irá gerar somente o funcionário 00001;  
Informando o filtro ??, o sistema irá gerar somente o funcionário 00001 e 00005;  
Informando o filtro 02.1, o sistema irá gerar os funcionários 00001 e 00002;  
Informando o filtro 0?.1, o sistema irá gerar os funcionários 00001, 00002, 00005 e 00007;

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
O sistema sempre irá quebrar por seção dentro da quebra de centro de custo.

**Centro de Custo - Ordenar por seção**

O sistema irá ordenar por seção quebrando o relatório por centro de custo.  
                
**Exemplo:**

| Chapa | Centro de Custo | Seção |
| --- | --- | --- |
| 00001 | 01.1  01.4 | 01.04 |
| 00002 | 01.4  01.5 | 01.05 |
| 00003 | 02.1  04.3 | 03.01 |
| 00004 | 01.4  01.7 | 03.01 |
| 00005 | 01.5 | 02.02 |
| 00006 | 01.4  01.7 | 01.04 |
| 00007 | 01.1 | 01.05 |
| 00008 | 02.1  04.3 | 01.01 |

**Resultado:**  
Campo Ordenar por seção: MARCADO  
Quebra da seção: ??  
   
Ordenado por Seção

| Chapa | Centro de Custo | Seção |
| --- | --- | --- |
| 00001 | 01.1 | 01 |
| 00007 | 01.1 | 01 |
| 00001 | 01.4 | 01 |
| 00002 | 01.4 | 01 |
| 00006 | 01.4 | 01 |
| 00002 | 01.5 | 01 |
| 00006 | 01.7 | 01 |
| 00008 | 02.1 | 01 |
| 00008 | 04.3 | 01 |
| 00005 | 01.5 | 02 |
| 00004 | 01.4 | 03 |
| 00004 | 01.7 | 03 |

                   
Ordenado por centro de custo

| Chapa | Centro de Custo | Seção |
| --- | --- | --- |
| 00001 | 01.1 | 01 |
| 00007 | 01.1 | 01 |
| 00001 | 01.4 | 01 |
| 00002 | 01.4 | 01 |
| 00006 | 01.4 | 01 |
| 00004 | 01.4 | 03 |
| 00002 | 01.5 | 01 |
| 00005 | 01.5 | 02 |
| 00006 | 01.7 | 01 |
| 00004 | 01.7 | 03 |
| 00008 | 02.1 | 01 |
| 00003 | 02.1 | 03 |
| 00008 | 04.3 | 01 |
| 00003 | 04.3 | 03 |

**Totais de Funcionário, Seção e Gerais**  
É possível selecionar separadamente quais bases de cálculo serão levadas para os totalizadores de funcionário, seção e geral da folha analítica.

**Importante:** Para que a seleção das bases de cálculo funcione, é necessário importar o layout mais recente da folha analítica pdf e txt. Caso o layout do relatório esteja desatualizado, todas as bases de cálculo serão impressas nos totalizadores de funcionário, seção e geral da folha analítica, independente da seleção realizada.

**Resumo do Funcionário - Fórmulas**

O campo **"Resumo Funcionário – Fórmulas"** da folha analítica permite a personalização de até 15 campos para exibição de dados relacionados ao colaborador. É possível incluir informações provenientes do banco de dados, como salário base, horas extras, adicionais, entre outros, que podem ser utilizados diretamente nas fórmulas.

**Exemplo 1 - Sem parâmetros específicos.**

Em Folha Mensal | Folha Analítica | Aba Dados do Funcionário. foi selecionado a fórmula 1, conforme print abaixo. Selecione uma fórmula e no campo abaixo no**Resumo funcionário - Fórmulas**, informe a fórmula de cálculo. No exemplo abaixo a **Fórmula 1** foi associada a fórmula de cálculo Salario.

Após a geração verifique que campo foi apresentado com o retorno da formula:

**Exemplo 2 - Com parâmetros específicos.**

Em Folha Mensal | Folha Analítica na aba Dados do Funcionário, foi selecionado a fórmula 1, conforme print 1 abaixo. Avance para a tela de **Seleção de Coligadas**, conforme print 2 abaixo, edite a coligada e acesse os **Parâmetros Específicos**. Nesta tela, no campo **Fórmulas do** **Resumo - Funcionário** ,  informe a fórmula de cálculo. No exemplo abaixo a Fórmula 1 foi associada a fórmula de cálculo **Salário**.

Após a geração verifique que campo foi apresentado com o retorno da fórmula.

## **DEMAIS INFORMAÇÕES**

* [Considerar histórico de situação de funcionário ao gerar Folha Analítica na competência atual](https://tdn.totvs.com/pages/viewpage.action?pageId=1005899558)
* [Nome Social](https://tdn.totvs.com/pages/viewpage.action?pageId=1006410450)
