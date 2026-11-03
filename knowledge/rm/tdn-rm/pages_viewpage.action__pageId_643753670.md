---
content_hash: 0d3b1187fcbc4e5a50633c662c8ac7177bb409aff9e0bf1fc4b1173865a65726
fetched_at: '2026-06-29T00:11:10.421707+00:00'
page_id: '643753670'
product: rm
source: tdn-rm
title: Importação da Produção Agrária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=643753670
version: 15
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. ****Tela da Importação da Produção Agrária****
   1. **Principais Campos e Parâmetros**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Nesse processo será importada a produção agrária dos funcionários rurícolas e saqueiros nas unidades de produção referentes a um determinado período de fechamento, seja na safra ou entressafra.

Deverá cadastrar as informações fundamentais para os processamentos da importação da folha agrária, a saber:

1. Parametrizador / Folha Agrária
2. Parâmetros Locais do Usuário
3. Unidade Agrária de Produção.
4. Programação Agrária.
5. Finalidade da Tarefa Agrária.
6. Tipo de Finalidade da Tarefa Agrária
7. Tarefa Agrária.
8. Regra de Cálculo para Tarefa Agrária.
9. Associação de Regra de Cálculo e Tarefa Agrária
10. Cultura Cultivada.
11. Vigência do Preço da Cultura Cultivada.
12. Preço Unitário de Produção Na Unidade Agrária (Teste).

Para a importação será considerada a filial de contexto selecionada, inclusive para a parametrização em Parametrizador / Folha Agrária / Parâmetros da Filial.

Operações executadas pela importação da folha agrária:

* **Ignorar** - Caso já exista um registro equivalente nenhuma ação será executada. Novos registros serão criados.
* **Somar** - Caso já exista um registro equivalente a quantidade informada no arquivo será somada à existente. Caso a opção "Apenas validar" estiver marcada essa operação não será executada.
* **Substituir** - Serão excluídos todos os registros de produção, exceto registros já lançados em folha. Caso a opção "Apenas validar" estiver marcada essa operação não será executada.

O layout para importação deverá ser previamente cadastrado em Configurações / Importações / Layout de Importação selecionando o tipo de importação “Importação de Produção Agrária”.

O arquivo deve seguir a formatação do layout selecionado, sendo que as datas importadas nos arquivos devem ter o formato DD/MM/AAAA, inclusive no layout deve ser criado da mesma forma.

As datas selecionadas dentro da importação devem estar compreendidas entre as datas cadastradas em Folha Agrária / Parâmetros Locais do Usuário e em Parametrizador / Folha Agrária / Parâmetros da Filial / Período Global de Produção cadastrado nos parâmetros de filial.

Quando o parâmetro “Validar quantidade de diária” estiver marcado em Folha Agrária / Mais / Regra de Cálculo para Tarefa Agrária será validado o valor da quantidade informado no arquivo com a “Quantidade máxima para diária” de acordo com o somatório das quantidades das produções do funcionário no dia do apontamento em sua filial.

O somatório das produções deverá seguir a regra:

1. Caso a operação seja ignorar serão consideradas todas as quantidades gravadas e as quantidades do arquivo que não existirem na produção;
2. Caso a operação seja somar será considerada toda a quantidade da produção gravada somadas com as quantidades do arquivo.
3. Caso a operação seja substituição será considerada a quantidade dos apontamentos de produção do arquivo;
4. Caso no arquivo de importação o registro importado possuir: (minutos > 0) E (Finalidade da tarefa = ‘diária’) E (quantidade = “ZERO”) o campo quantidade deste registro receberá: minutos / jornada (Chronus).
   * **Exemplo:** 390minutos / 440minutos jornada = 0,8863 (valor a gravar no campo quantidade);
     + Obtendo valor: 0,8863 \* 0,0367424 = R$ 28,66
     + Obtendo pausa: 50minutos \* 0,073484 = R$ 3,67
     + Somados = R$ 32,33 (diária, que é exatamente salário R$ 970,00 / 220 / 60 \* 440 = 32,33)

Antes de importar o arquivo com os dados para a produção agrária poderá ser validado pelo parâmetro “Apenas Validar”.

Com a opção “Apenas Validar” selecionada não será lançado na Produção Agrária as informações existentes no arquivo a ser validado.

Somente será validado o arquivo com esse parâmetro marcado.

**Atenção:** Os dados serão importados normalmente mesmo que o arquivo não seja alterado ou validado antes da importação. O sistema não fará as validações do arquivo no momento da importação.

O parâmetro “Importar produção para funcionário com transferência posterior” será selecionado para permitir aceitar a produção anterior à data de transferência para os casos que a produção do funcionário, anterior a sua transferência, não tenha sido processada.

A seleção de “Regra de Cálculo das Tarefas” servirá de filtro para que somente os apontamentos em que as tarefas vinculadas as estas regras sejam processados.

**Informações sobre regras para cada “Tipo de Cálculo”:**

**Obter preço unitário:**

* Para Regra de Cálculo da Tarefa com o campo Preço Informado marcado será obtido o valor do Preço Pago registrado no cadastro “Preço Unitário de Produção Na Unidade Agrária (Teste)” referente ao campo PPRECOPRODUCAO.PRECOPAGO de acordo com:
  1. A coligada corrente; E.
  2. Filial, Unidade agrária, Fração Agrária, Programa, Tarefa, E.
  3. O Dia do Apontamento da Produção.
* Caso não encontre o “Preço Unitário (teste)” será incluído automaticamente no Preço Unitário Na unidade Agrária de Produção (Teste) com o último Preço unitário anteriormente cadastrado.
* Para incluir o Último Preço Unitário (teste) serão seguidas as regras abaixo:
  1. A data do dia para a cultura e filial referente ao apontamento não poderá ser superior ao período da Vigência do Preço da Cultura Cultivada. Caso não haja vigência que atenda será registrada mensagem no Log.
  2. O Parâmetro da Filial “Dias a retroceder na Inclusão automática do Preço Unitário na Unidade Agrária” seja maior que zero em Parametrizador / Folha Agrária / Parâmetros da Filial / Cálculo

**Diária:** O preço unitário será o salário do funcionário divido pela Jornada mensal multiplicado pela jornada diária em que:

* O Salário do Funcionário será obtido pelo campo PFUNC.SALARIO;
* A Jornada mensal será obtida do cadastro de funcionário;
* A jornada diária será obtida do número de horas trabalhadas registrada no horário do RMCHRONUS no dia do apontamento. Caso não tenha integração com o RMCHRONUS será a jornada mensal dividida por 30 se o parâmetro mês comercial estiver marcado ou pela quantidade de dias do mês se o parâmetro mês comercial estiver desmarcado.

**Depende de outras Tarefas:** Será o somatório das demais produções no dia de ordem de prioridade maior, ou seja, o campo “Prioridade de cálculo” cadastrado dentro da “Regra de Cálculo para Tarefa Agrária” tenha o valor menor que da Tarefa informada dentro do arquivo de importação.

**Sem cálculo Interno:** Retornará zero caso não tenha informado nenhum dos campos no cadastro da “Regra de Cálculo para Tarefa Agrária”. Ou retornará o valor da sentença SQL, valor fixo ou fórmula, sendo que se houver valor retornando em mais de um campo será o somatório dos valores retornados.

**Observação:** Os valores obtidos nos tópicos acima (Sentença SQL, Valor do Fixo e Fórmula) deverão ser somados apenas se o Tipo de Cálculo selecionado seja “Sem cálculo interno”. Portanto, os campos Sentença SQL, Valor do Fixo e Fórmula estarão desabilitados para qualquer Tipo de Cálculo, exceto para a opção “Sem cálculo interno”.

**Complemento de Diária Mínima*:*** Será Abatido o valor calculado do obtido da regra de Tarefa informado no parâmetro “Parâmetro para Regra para Mínimo Garantido Para Diária” em Parametrizador / Folha Agrária / Parâmetros da Filial. Em que:

* O resultado sendo negativo significa que é a diferença a ser paga, sendo assim o preço unitário deverá assumir o valor absoluto do resultado;
* O resultado sendo positivo ou zero deverá retorna zero o preço unitário.

**Observação:** Existe a variável **DIAPRODUCAOAGRARIA** que retorna o dia de produção agrária que poderá ser utilizada em sentenças SQL ou Formulas. O principal objetivo é poder construir formulas e sentenças SQL que possam calcular complementos. Os complementos são calculados obtendo o valor da diária mínima e comparando com o valor total das Tarefas de produção. Não sendo igual ou superior a diária mínima deverá obter o valor da diferença a ser completada.

**Observações para funcionário demitido ou afastado:**

* Caso o funcionário esteja demitido, ou seja com rescisão calculada, e ainda existir produção a ser importada, a mesma será importada produção até a data da demissão e será informado no Log a mensagem de aviso “Produção Lançada para funcionário Demitido <Chapa>. Linha <Linha> “.
* Caso o funcionário esteja afastado será informado no Log a mensagem de aviso “Produção Lançada para funcionário Afastado <Motivo> <Chapa>. Linha <Linha> “. somente para o primeiro dia de afastamento pois pode ocorrer afastamento em parte do dia de início do afastamento, depois de apontamento a ser importado. Exemplo: Funcionário tem acidente de trabalho a tarde e tem produção na parte da manhã.

**Observação para o campo tonelada:** O campo tonelada na produção é preenchido para Tarefas que em sua regra de cálculo a opção de cálculo seja de preço informado. O seu cálculo é Quantidade da produção multiplicado por Kg Metro Pago (do Teste) dividido por 1000.

1. Kg Por Metro é o campo definido em Preço Unitário de Produção Na Unidade Agrária (Teste).
2. Só será registrado na produção se o campo apenas validar estiver desmarcado.

## **02. EXEMPLO DE UTILIZAÇÃO**

**01 -** Criado o layout em Configurações / Importações / Layout de Importação selecionando o tipo de importação “Importação de Produção Agrária”.

<?xml version="1.0" encoding="UTF-8"?>

<layout>

  <tabela>PPRODUCAOAGRARIA</tabela>

  <descricao> LAYOUT PARA FOLHA AGRÁRIA</descricao>

  <parametros>

    <separador\_decimal>,</separador\_decimal>

    <formato\_data>DD/MM/AAAA</formato\_data>

    <possui\_separador>1</possui\_separador>

    <separador\_importacao>;</separador\_importacao>

  </parametros>

  <campos>

    <campo ordem="0" tipo="int">CODCOLIGADA</campo>

    <campo ordem="1" tipo="string">CHAPA</campo>

    <campo ordem="2" tipo="DateTime">DATAPRODUCAO</campo>

    <campo ordem="3" tipo="string">CODUNIDAGRARIA</campo>

    <campo ordem="4" tipo="int">CODFRACAOAGRARIA</campo>

    <campo ordem="5" tipo="double">CODPROGRAMA</campo>

    <campo ordem="6" tipo="string">CODTAREFA</campo>

    <campo ordem="7" tipo="double">QTDEPRODUZIDA</campo>

    <campo ordem="8" tipo="int">HORAS</campo>

  </campos>

  <eventos />

</layout>

**02 –** Criado arquivo txt para importação

1;00001;18/05/2021;01;1;1;00001;10;0800

As informações fundamentais para os processamentos da importação da folha agrária já devem estar previamente cadastradas.IMPORTANTE!

**03 -** Informação no processo de importação

**04 –** Após importação será visualizado em Produção Agrária

**Observação:** Como se trata de uma importação de Diária, o preço unitário seguiu a regra do salário do funcionário divido pela Jornada mensal multiplicado pela jornada diária, que nesse caso seria 7650,00 / 220 \* 6 = 208,63636363...

**03. Importação da Produção Agrária**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Código de Quebra | Selecione a quebra |
| Seleção de funcionários | Selecione os funcionários |
| Operação | Ignorar / Somar / Substituir |
| Layout da produção agrária | Selecione o layout cadastrado previamente em Configurações / Importações / Layout de Importação |
| Arquivo de importação | Selecione o arquivo que estará configurado conforme layout selecionado anteriormente |
| Período de apontamento | Período para o qual será feita a importação que deve estar compreendido entre o Parâmetros Locais do Usuário e o período do Parametrizador / Folha Agrária / parâmetros da Filial |
| Quantidade máxima para diária | Quantidade para validação conforme parâmetro Validar quantidade de diária na Regra de Cálculo para Tarefa Agrária |
| Apenas validar | Será feita apenas a validação do arquivo sem importar |
| Importar produção para transferência posterior | Será feita a importação da produção em dias anteriores à transferência do funcionário |
| Forma de exibição do log | Simples / Detalhado |
| Regras de Cálculos das Tarefas | Selecione as regras de cálculos das tarefas que deverão constar no arquivo de importação |

Alguns campos têm particularidades, veja em Visão Geral (item acima).IMPORTANTE!

## **04. TABELAS UTILIZADAS**

* PUSRPARAMLOCAL
* PUNIDADEAGRARIA
* PPROGRAMACAOAGRARIA
* PFINALIDADETAREFAAGRARIA
* GDINAM - PTPFINAGRI
* VTAREFA
* PRGRCALCAGRARIA
* PRGRCALCTAREFAAGRARIA
* PCULTURAAGRAIA
* PVIGENCIACULTURA
* PPRECOPRODUCAO
* PPRODUCAOAGRARIA
