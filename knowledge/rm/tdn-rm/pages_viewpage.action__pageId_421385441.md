---
content_hash: 5fe72bd6b7fc31305a6509ba3ec65e9efc248e612441b3d544ab70dc0c208bb1
fetched_at: '2026-06-29T00:09:16.016136+00:00'
page_id: '421385441'
product: rm
source: tdn-rm
title: Importar Arquivos do MS-Project.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385441
version: 6
---

---

A importação de arquivos de projetos (.mpp ou .xml) consiste em Incluir tarefas em um novo projeto ou em um projeto já existente. A funcionalidade consiste em gerar uma planilha ou cenário espelho do Projeto que se escolheu importar. O processo tem início informando o caminho onde está o arquivo a ser importado. Em seguida, informar a qual grupo de custo os recursos importados pertenceram. Linha de Início e Linha Fim: informe a primeira linha do arquivo a ser importada e a última linha do arquivo a ser importada. Se selecionado a opção Nova (s) Obra (s) indica que será importada uma nova obra. Se desejar que a obra importada tenha quantidade igual a 1 (um) deverá ser marcado a opção valor unitário para obras. Uma unidade default de importação deverá ser informada, esta será unidade default para insumos ou composições criadas durante a importação.

**Observações:**

O sincronismo é feito no momento da importação, disponível em Projeto>Importações>Importar Tarefas via MS Project .

A comunicação entre o arquivo (.mpp ou .xml) e o TOTVS obras e Projetos na importação são as colunas correspondentes aos campos a serem importados. Deste modo durante o processo de importação deve-se informar uma coluna do arquivo correspondente para cada campo do sistema:

Na tela acima, informe a localização do arquivo do Project (.mpp)

A opção de cenários foi implementada à funcionalidade "Importação de tarefas via MS-Project", e no momento da importação deverá ser escolhido qual cenário receberá a importação, se Principal ou entre as quatro opções de cenários disponíveis por projeto. Apenas ficarão visíveis cenários ativos.

A opção de planilha listará sempre planilha de atividades ou de serviços dependendo da planilha que deseja importar.

Deverá informar um grupo de custo existente para que o mesmo seja associado às tarefas.

Na linha de início deverá informar a primeira linha da planilha cujos dados serão importados. Da mesma fora para a linha final, porém esta não é obrigatória caso queira importar todas as linhas contidas na planilha

A unidade default também é obrigatória

**Colunas**

Selecione a coluna (no arquivo Project) que corresponde aos campos Código, Nome, Descrição, Quantidade, Percentual, Unidade, Valor Cotado, Nome Recurso, Tipo Recurso (G/L), BDI Diferenciado, Data Início e Data Término.

Data Início e Data Término são importadas para o Pert. Considerando as datas de início e término, é feito o cálculo da duração das tarefas em dias corridos. A defasagem é importada somente quando a ligação for importada.

Se desejar a quantidade da tarefa pode ser alterada no momento da importação, para isto deve ser aplicado um fator, selecione somar, multiplicar ou dividir este fator a quantidade da tarefa. Se não desejar alterar a quantidade a ser importada marque a opção não modificar quantidade.

  Para os recursos de cada tarefa é criada uma composição com o código CCMPMSPXXX, onde CCMP indica que é um código de composição, MSP indica que foi importado do Project e XXX é o identificador da composição. A unidade da composição é UN e a descrição é DCMPMSPXXX, onde DCMP indica que é a descrição da composição, os demais caracteres seguem o mesmo critério do código. A quantidade do recurso na composição é a mesma existente no Project.

Os recursos da tarefa são inseridos na composição. Os recursos são criados com o código CISMMSPXXX, onde CISM indica que é um código de insumo, MSP indica que foi importado do Project e XXX é o identificador da composição.

A quantidade da tarefa pode ser preenchida com o conteúdo de um dos campos disponíveis: Duração, Duração1, Duração2, Duração3, Duração4, Numero1, Numero2, Numero3, Numero4, Numero5 ou Trabalho. A duração das tarefas no Projeto é configurável pelo usuário, mas internamente ela é representada em minutos. Nesse processo de importação a quantidade é o número de horas dividido por 480, pois, é considerada a jornada de trabalho de 8 horas. Dessa forma, a duração é importada em dias. Através da aplicação do fator você pode alterar a forma de converter a quantidade.

Se a tarefa não possuir quantidade ou se a coluna correspondente não for informada, o valor da mesma será setado para 1.

A definição de que uma linha do Project será considerada como etapa será obtida através da hierarquia das tarefas no Project.  
Para tal, caso a linha do Project não possua uma subtarefa, ela será considerada como serviço.

Se alguma etapa possuir quantidade, a quantidade da mesma será desprezada.

Se a tarefa a ser importada possuir valor cotado e recurso, a importação prioriza o recurso e importa o valor cotado desativado. Se o projeto estiver parametrizado a utilizar máscara de insumo ou composição, o sistema irá fazer as consistências de máscaras, apenas quando o insumo ou composição estiverem em inserção.

O recurso é localizado no cadastro do TOTVS Obras e Projetos através do seu nome, já que no arquivo Project normalmente os recursos são encontrados através do nome. Para mostrar que um recurso é global deve-se usar uma coluna e colocar o caractere 'g' ou 'G' e indicar que deseja que o sistema verifique a coluna em busca dos indicativos de tipo de recurso. Caso contrário, o recurso será considerado como Local (do projeto corrente).  
Para identificar o recurso, primeiro é feita uma busca no cadastro de composições e depois no de insumo, pois não existe uma identificação do mesmo no MS Project. Se a unidade da tarefa não existir no Cadastro de Unidades, será exibida a janela de Importação de Unidade para a tarefa. Através dessa janela a unidade pode ser inserida ou convertida para uma que já exista. Se o código da tarefa já existir, o mesmo será ignorado. Em projetos cujo status estão: paralisados ou concluído ou revisados ou cancelados não será permitido a utilização do recurso "Importação de tarefas via MS-Project".

Para que as composições e insumos sejam importadas do arquivo Project é necessário marcar o parâmetro abaixo:

**Cronograma**

Nessa aba temos as opções de:

* Exportar % concluído (Pert) para o Cronograma Realizado, recalculando o planejamento, que faz a mesma exportação do PERT para o cronograma, preenchendo no primeiro período aberto.

* Bloquear Período Realizado: após o preenchimento do % concluído é possível bloquear o período, marcando essa opção. O processo irá buscar sempre o primeiro período disponível conforme parâmetro do projeto.
* Bloquear Período Previsto: assim como o realizado é possível realizar o bloqueio após a execução do processo.

**Atenção:**

Não é necessário ter nenhum software instalado (exemplo: Microsoft Project) na máquina do usuário para que este processo possa ser executado.

---
