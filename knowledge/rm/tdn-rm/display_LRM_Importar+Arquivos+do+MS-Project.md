---
content_hash: f90f7de66b6bfb99e3222005334cfa2aa5a5b93da7fb32432f0f280297598bf7
fetched_at: '2026-06-29T00:09:16.116183+00:00'
page_id: '421385459'
product: rm
source: tdn-rm
title: Importar Arquivos do MS-Project
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+Arquivos+do+MS-Project
version: 1
---

**Importar Arquivos do MS-Project**

---

A importação de projetos (arquivos .mpp ou .xml) consiste em Incluir tarefas em um novo projeto ou em um projeto já existente. A funcionalidade consiste em gerar uma planilha ou cenário espelho do arquivo Project que se escolheu importar.   
O processo tem início informando o caminho onde está o arquivo Project a ser importado. Em seguida, Informar a qual grupo de custo os recursos importados pertenceram.  
Linha de Início e Linha Fim:  informe a primeira linha do arquivo a ser importada e a última linha do arquivo a ser importada. Se selecionado a opção Nova (s) Obra (s) indica que será importada uma nova obra. Se não selecionada indica que serão importadas as tarefas 'filhas' de uma obra existente no projeto. Se desejar que a obra importada tenha quantidade igual a um deverá ser marcado a opção valor unitário para obras. Se desejar, informe uma unidade default de importação, esta será unidade default para insumos ou composições criadas durante a importação.  
   
**Atenção:**  
Com o intuito de permitir que o TOP trabalhe de forma autônoma da solução da Microsoft, o processo de Importação via MS Project foi modificado, removendo a obrigatoriedade da utilização de licenças do mesmo no ambiente. No entanto o processo permanece sem alterações.  
   
**Observação:**  
O sincronismo é feito no momento da importação  
A comunicação entre o arquivos .mpp ou .xml e o TOTVS obras e Projetos na importação são as colunas correspondente aos campos a serem importados. Colunas no Projeto e campos no Obras e Projetos. Deste modo durante o processo de importação deve-se informar uma coluna do Projeto correspondente a um campo na planilha. Selecione a coluna (no arquivo Project) que corresponde aos campos Código, Nome, Descrição, Quantidade, Unidade, Valor Cotado, Nome Recurso, Tipo Rec (G/L), BDI Dif., Data Início, Data Término e Tarefa Sucessora. Caso não exista algum desses campos na planilha não preencha a coluna do Project. Exceto para o campo código, seu preenchimento é obrigatório, se a coluna que corresponde ao campo Código não for informada, a importação não será efetuada.  
   
**Observações**  
Data Início, Data Término e Tarefa Sucessora são importadas para o Pert. Considerando as datas de início e término, é feito o cálculo da duração das tarefas em dias corridos. A defasagem é importada somente quando a ligação for importada.  
Se desejar a quantidade da tarefa pode ser alterada no momento da importação, para isto deve ser aplicado um fator, selecione somar, multiplicar ou dividir este fator a quantidade da tarefa. Se não desejar alterar a quantidade a ser importada marque a opção não modificar quantidade. A opção de cenários foi implementada à funcionalidade "Importação de tarefas via MS-Project", no momento da importação deverá ser escolhido qual cenário receberá a importação. Se planilha de atividades, se planilha de serviços ou os demais cenários que é permitido criar no TOTVS Obras e Projetos.  
   
**Observações:**  
   
Para os recursos de cada tarefa é criada uma composição com o código CCMPMSPXXX, onde CCMP indica que é um código de composição, MSP indica que foi importado do MS Project e XXX é o identificador da composição. A unidade da composição é UN e a descrição é DCMPMSPXXX, onde DCMP indica que é a descrição da composição, os demais caracteres seguem o mesmo critério do código. A quantidade do recurso na composição é a mesma existente no MS Project. Os recursos da tarefa são inseridos na composição. Os recursos são criados com o código CISMMSPXXX, onde CISM indica que é um código de insumo, MSP indica que foi importado do MS Project e XXX é o identificador da composição. A descrição do insumo é DISMMSPXXX, onde DISM indica que é a descrição do insumo, os demais caracteres seguem o mesmo critério do código.  
A quantidade da tarefa pode ser preenchida com o conteúdo de um dos campos disponíveis: Duração, Duração1, Duração2, Duração3, Duração4, Numero1, Numero2, Numero3, Numero4, Numero5 ou Trabalho. A duração das tarefas no MS Project é configurável pelo usuário, mas internamente ela é representada em minutos. Nesse processo de importação a quantidade é o número de horas dividido por 480, pois, é considerada a jornada de trabalho de 8 horas. Dessa forma, a duração é importada em dias. Através da aplicação do fator você pode alterar a forma de converter a quantidade.  
Se a tarefa não possuir quantidade ou se a coluna correspondente não for informada, o valor da mesma será setado para 1. Se alguma etapa possuir quantidade, a quantidade da mesma será desprezada.  
Se a tarefa a ser importada possuir valor cotado e recurso, a importação prioriza o recurso e importa o valor cotado desativado.  
Se o projeto estiver parametrizado a utilizar máscara de insumo ou composição, o sistema irá fazer as consistências de máscaras, apenas quando o insumo ou composição estiverem em inserção.  
O recurso é localizado no cadastro do TOTVS Obras e Projetos através do seu nome, já que no MS Project normalmente os recursos são encontrados através de seu nome.  
Para mostrar que um recurso é global deve-se usar uma coluna e colocar o caractere 'g' ou 'G' e indicar que deseja que o sistema verifique a coluna em busca dos indicativos de tipo de recurso. Caso contrário, o recurso será considerado como Local (do projeto corrente).  
Para identificar o recurso, primeiro é feita uma busca no cadastro de composições e depois no de insumo, pois não existe uma identificação do mesmo no MS Project.  
Se a unidade da tarefa não existir no Cadastro de Unidades, será exibida a janela de Importação de Unidade para a tarefa. Através dessa janela a unidade pode ser inserida ou convertida para uma que já exista.  
Se o código da tarefa já existir, o mesmo será ignorado.  
Em projetos cujo status estão: paralisados ou concluído ou revisados ou cancelados não será permitido a utilização da funcionalidade "Importação de tarefas via MS-Project".
