---
content_hash: d49ff892499456a807c9cac2a1c10c7cc0a12ed2a22f2bb3b051f63a0625791f
fetched_at: '2026-06-29T00:09:16.096864+00:00'
page_id: '421385456'
product: rm
source: tdn-rm
title: Importar Cronograma via Excel 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385456
version: 3
---

---

A importação de cronograma via MS Excel permite que seja feita a importação de lançamentos realizados numa planilha do Excel para os cronogramas previsto, realizado e medido das respectivas tarefas nas planilhas de atividades, serviços e nos cenários. A importação de cronogram atualiza através dos lançamentos (Percentual/Quantidade/Valor) e convertendo para a grandeza selecionada (Quantidade/Valor/Percentual). Para realizar a importação é necessário que a planilha do Excel esteja estruturada devidamente, ou seja, cada cronograma de uma tarefa é representado por uma linha na planilha, uma coluna representa o código das tarefas, outra coluna representa o período inicial a aplicar o cronograma e as demais colunas representam os lançamentos por períodos (Valor numérico seguido pelo símbolo de percentual "%" ou número decimal entre 0 e 1, onde 1 representa 100% e 0 representa 0%).

* **Arquivo:** Arquivo de importação excel
* **Linha inicial:** Linha inicial da planilha excel
* **Código da tarefa:** Coluna onde o código da tarefa está informado na planilha excel
* **Início dos lançamentos:** Coluna onde se iniciam os lançamentos da planilha excel
* **Período inicial de cada tarefa:** Coluna onde está definido o período inicial dos lançamentos
* **Alterar Qtde. da tarefa pelo Cronograma:** Coluna para definir o comportamento da tarefa.
  + Caso o valor informado na coluna for 0, a quantidade da tarefa não será alterada na importação.
  + Caso o valor informado na coluna for 1, após realizar a importação, a quantidade da tarefa será alterada para a quantidade total dos lançamentos informados no cronograma.
* **Grandeza utilizada no arquivo de importação:**Grandeza utilizada no arquivo excel que será importado, o excel pode estar preenchido em percentual, quantidade ou valor.
* **Converter grandeza para:**Conversão das grandezas do arquivo excel para a grandeza desejada no projeto. A grandeza que for selecionada será a grandeza utilizada no cronograma. O cronograma pode estar preenchido em percentual, quantidade e valor.
* **Cronograma de destino:** Cronograma que será alterado na importação excel.
  + **Previsto:**O cronograma importado será direcionado para o cronograma previsto.
  + **Realizado:**O cronograma importado será direcionado para o cronograma previsto.  Para essa opção, o campo Alterar Qtde. da tarefa pelo Cronograma não estará habilitado.
  + **Medido:** O cronograma importado será direcionado para o cronograma previsto. Para essa opção, o campo Alterar Qtde. da tarefa pelo Cronograma não estará habilitado.

**REGRAS GERAIS:**

* *Os lançamentos não devem somar valores superiores a 100 (cem), pois o processo se dá na forma percentual e não aceita valores superiores;*
* *Os lançamentos informados para obras e etapas são aplicados às tarefas filhas;*
* *A ordem dos lançamentos é importante tendo a leitura e importação sendo feitas de forma sequencial, caso uma tarefa tenha valores de cronograma definidos na linha 3 e a sua etapa ou obra tenha seu valor definido na linha 5 (lançamentos desordenados), os valores de cronograma desta tarefa serão definidos conforme o informado para ela e logo serão sobrescritos pelos valores informados na etapa ou obra;*
* *A importação é interrompida ao encontrar uma linha em branco, a linha em branco representa o final do documento;*
* *A importação só opera sobre períodos não travados do cronograma.*
* *Não será permitido que seja escolhido mais de um cronograma de destino.*
* *Ao importar uma planilha, caso a mesma esteja "aberta", é necessário que após alguma alteração, a planilha seja salva, pois do caso contrário os dados modificados não serão importados.*
* *Ao colocar 0 na célula excel, a alteraçao do período será ignorada na importação. Caso a célula excel estiver vazia, o sistema excluirá a informação no cronograma para o período.*
* **Observação:** O processo de importação não contempla o processo de replanejamento do cronograma de forma automática necessitando este de ser feito manualmente via processo  na visão da planilha.

**SITUAÇÕES ONDE NÃO OCORRERÁ A IMPORTAÇÃO:**

* *Lançamentos ultrapassando o percentual máximo de 100%;*
* *Lançamentos que não informam percentuais (todos os períodos iguais a zero);*
* *Lançamentos com período inicial no Excel menor ou igual a zero;*
* *Lançamentos que possuem código diferente aos códigos da planilha;*
* *Lançamentos para tarefas que possuem o parâmetro "Alterar qtde. pelo cronograma" marcado;*
* *Lançamentos em períodos travados.*
* *Seguem abaixo os passos necessários para realizar a importação de cronograma via Excel para tarefas das planilhas de atividades, serviços e cenários:*
* *IMPORTAR CRONOGRAMA VIA EXCEL:*
* *Acessar a Planilha (Atividades/Serviços/Cenários) > Acessar o menu "Processos" > "Importação de cronograma via Excel" > Informar a localização do arquivo > Informar a linha inicial (primeira linha onde estão representadas as obras, serviços ou tarefas. Ex: Para Linha 1 informar 1) > Informar a coluna onde está localizado o código da tarefa (número da coluna do Excel correspondente ao código da tarefa. Ex: Para Coluna A informar 1) > Informar a coluna onde está localizado o período inicial de cada tarefa(número da coluna do Excel correspondente ao período inicial dos lançamentos do cronograma da tarefa. Ex: Para Coluna B informar 2) > Informar a coluna onde está localizado o lançamento referente ao início dos percentuais(número da coluna do Excel correspondente à primeira coluna que contém dados de lançamentos de períodos do cronograma. Ex: Para Coluna C informar 3) > Informar a grandeza para qual os lançamentos serão convertidos > Clicar em "Executar" > Calcular o cronograma.*

***E*xemplo:**

No exemplo abaixo podemos ver um exemplo de planilha do Excel que poderia ser utilizada na importação do cronograma através de representação de lançamentos percentuais:

**Tarefa     Período inicial**   
001                    0              5%    10%     30%     50%     5%  
001.01               2            30%                20%                1%

Podendo também ser representado por números decimais um modelo equivalente ao acima:

**Tarefa          Período inicial**   
001                       0            0,05    0,1       0,3      0,5      0,05  
001.01                  2            0,3                  0,2                 0,01

**Atenção:** A partir da versão 12.1.5, não é necessário ter instalado na máquina onde a importação está sendo executada a solução da Microsoft, como o MS Excel.

---
