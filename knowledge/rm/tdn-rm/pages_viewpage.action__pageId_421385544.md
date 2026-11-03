---
content_hash: b4f994819795aaa4bbfabd4d484fd3543203f48cec731a24a9a50eb97ebc51e0
fetched_at: '2026-06-29T00:09:16.753807+00:00'
page_id: '421385544'
product: rm
source: tdn-rm
title: Replanejamento de Índices
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385544
version: 33
---

---

Em algumas situações, durante a execução do projeto, é necessário realizar **alterações nos índices** (quantidades) dos recursos da composição, porém, algumas das **atividades que estão associadas a ela** podem já estar em execução, por este motivo, é necessário preservar os valores da composição para a parte já executada destas atividades.

Dessa forma, é necessário um Replanejamento que permita a realização destas **alterações nos índices da composição sem causar impacto** nas partes já executadas das atividades. O processo de replanejamento cria uma nova composição com a nova quantidade informada. Esta nova composição irá armazenar a referência da composição original. O código da nova composição irá obedecer a máscara definida nos parâmetros do projeto, caso a máscara não esteja parametrizada, o código será composto por CMPRPL + incremento.

**Processos da Composição :** O processo de replanejamento de índices não poderá ser executado para tarefas que possuem divisão. O sistema validará informando quais tarefas são do tipo de divisão. [Dividir Tarefas](https://tdn.totvs.com/pages/editpage.action?pageId=744482552)

O processo de Replanejamento é dividido em dois passos:

* O primeiro passo exibe os recursos (insumos) associados à composição selecionada, neste passo é obrigatório realizar a alteração dos índices (quantidades) para que o processo permita avançar para o segundo passo.
* No segundo passo é exibida uma visão com uma grid listando todas as atividades associadas diretamente a composição selecionada para replanejamento. Só serão exibidas tarefas que possuem percentual de cronograma realizado diferente de 0% e de 100%, ou seja, percentuais entre 0% e 100% e também percentuais maiores que 100%. Neste passo é permitido alterar a quantidade da atividade, no entanto, esta alteração respeitará as consistências conforme o cronograma realizado.

*Observação: É necessário ter o cronograma previsto igual a 100% informado na tarefa para que o processo funcione corretamente. Caso o cronograma previsto for menor que 100% o processo retornará a mensagem "O cronograma previsto da atividade não fecha em 100%" Tarefas globais não são exibidas no processo de replanejamento de índices.*

O processo de replanejamento de índices transforma a tarefa replanejada pelo processo em etapa e cria duas tarefas filhas. O segundo passo do processo possui um checkbox "Replanejar cronograma da nova tarefa" e ele faz com que ocorra replanejamento do cronograma previsto na criação da 2ª tarefa após a execução.

A quantidade preenchida no cronograma realizado será a quantidade da 1ª tarefa da hierarquia e o restante da quantidade que não estava preenchida no cronograma será a quantidade da 2ª tarefa da hierarquia mesmo que há alteração de quantidade da tarefa durante a execução do processo.

* 1ª Tarefa criada:

A tarefa será criada mantendo os percentuais do cronograma conforme estavam preenchidos.

PERT será cadastrado com a mesma data início e fim programado da tarefa que foi transformada em etapa.

A quantidade preenchida no cronograma realizado será a quantidade da 1ª tarefa da hierarquia após o replanejamento de índices e consequentemente, o cronograma previsto e o realizado serão preenchidos com 100% relacionado a quantidade da tarefa.

* 2ª Tarefa criada:

A nova composição replanejada será associada a tarefa e também será acrescentado a ela a descrição "

Replanejada em \[DATA\]"

A tarefa não possuirá cronograma preenchido

PERT não irá vir preenchido com a data início e fim programado.

- A quantidade restante que não estava preenchida no cronograma realizado da tarefa antes do replanejamento de índices será a quantidade da nova tarefa, ou seja, se a tarefa antes do replanejamento tinha quantidade igual a 4 e o percentual de cronograma realizado totalizar uma quantidade de 2 a segunda tarefa será criada com quantidade igual a 2. O mesmo cálculo ocorre caso ocorra replanejamento aumentando a quantidade da tarefa.

- Caso o checkbox "Replanejar cronograma da nova tarefa" estiver desmarcado, a tarefa não terá seu cronograma previsto preenchido.

- Caso o checkbox "Replanejar cronograma da nova tarefa" estiver marcado, a tarefa virá com o cronograma previsto preenchido em 100% de acordo com a sua quantidade (seja ela alterada ou não durante o processo).

*Observação: É possível fazer o replanejamento acrescentando, reduzindo ou mantendo a mesma quantidade de tarefas, mas no caso de redução da quantidade o sistema verifica a seguinte consistência: Será verificada a quantidade realizada pelo cronograma realizado e, a nova quantidade, deve ser superior ao que já está preenchido no cronograma realizado.*

*Exemplo da redução de quantidade da tarefa:*

*Tarefa 001.01.01 possui quantidade 6 e o seu cronograma realizado está preenchido com 50% então, a quantidade realizada da tarefa é 3.*

*Caso há redução na quantidade da tarefa durante o replanejamento de índices a nova quantidade da tarefa deve ser no mínimo 3, pois já existe cronograma realizado com quantidade 3.*

*Caso seja informada a quantidade 3 para a tarefa o sistema após o replanejamento de índices irá transformar a tarefa 001.01.01 em etapa e criar as tarefas: 001.01.01.01 com quantidade 3 e 001.01.01.02 com quantidade 0.*

**Parâmetro "Utiliza PERT" na execução do processo:**

* **Parâmetro Utiliza PERT desmarcado:** somente o cronograma da tarefa irá influenciar no replanejamento de índices mas quando o parâmetro está marcado o sistema verifica o campo "Percentual concluído" do PERT da tarefa.
* **Parâmetro Utiliza PERT marcado:** os campos "Percentual concluído" e o total do "Cronograma realizado" da tarefa devem estar com o mesmo valor, caso contrário, o processo retornará erro após a execução informando que existem divergências entre os percentuais de completude do PERT e do cronograma.

A execução do Replanejamento de Índices impacta nos contratos cadastrados (possuindo medição ou não e até os que estão 100% medidos) e também influencia nos pedidos de materiais.

*Exemplo do comportamento após execução do processo:*

*1. Transforma a tarefa em etapa com o mesmo código da atividade original, por exemplo, tarefa 001.01.01. O nome da etapa após execução do processo também será o mesmo da atividade original.*

*2. São criadas duas atividades na hierarquia da etapa adicionando um novo nível em seu código, tarefa 001.01.01.01 e 001.01.01.02.*

*3. A atividade 001.01.01.01 receberá a quantidade executada até o momento da atividade original. O percentual concluído será obtido do Cronograma ou Pert, conforme definição do Parâmetro de Projeto | Utiliza Pert*

*4. O cronograma realizado atividade 001.01.01.01 será atualizado para 100% e o cronograma planejado receberá os percentuais do cronograma modificado deste item.*

*5. Para a atividade 001.01.01.01, a associação com a composição original (CMP01) será preservada. Nenhuma outra alteração será feita.*

*6. Será criada uma nova atividade com código 001.01.01.02.*

*7. O nome e a descrição da atividade 001.01.01.02 será o mesmo nome da atividade original, adicionando o sufixo " - Replanejada em dd/mm/aaaa" (data da alteração).*

*8. A atividade 001.01.01.02 será criada com o Pert 0% e com o cronograma previsto vazio. No entanto, existe a opção de replanejar a nova tarefa com o saldo restante da tarefa original.*

*9. A quantidade da atividade 001.01.01.02 será a diferença entre a quantidade da atividade original e a quantidade da atividade 001.01.01.01.*

*10. A nova composição (CMPRPL02 ou o código definido pela máscara), já com os índices replanejados, será associada à atividade 001.01.01.02.*

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Código | Nome | Descrição | Quantidade | Composição Local |
| 001 | Obra | Obra | 1 |  |
| 001.01 | Etapa | Etapa |  |  |
| 001.01.01 | Tarefa 1 | Tarefa 1 |  |  |
| 001.01.01.01 | Tarefa 1 | Tarefa 1 | 2 | CMP01 |
| 001.01.01.02 | Tarefa 1 - Replanejada em 01/05/2018 | Tarefa 1 - Replanejada em 01/05/2018 | 1 | CMPRPL02 |

**Vigência de Recurso**

A Vigência de Recurso é utilizada para que os Recursos das Tarefas possam impactar em diferentes períodos de execução da Obra com diferentes índices (quantidade). Para utilização da Vigência de Recurso deve-se habilitado o Parâmetro “Utiliza Vigência de Recurso” em Projeto | Construção e Projetos | Projetos (F6) | Composição.

Após habilitar o parâmetro, deve-se executar o Processo “Replanejamento de índice” em Orçamento | Composições | Cadastro (F9) | Processos. Para o Replanejamento com Vigência de Composição o Projeto deve estar parametrizado para ser obrigatório o fechamento do Cronograma Planejado em 100% e possuir uma grandeza de lançamento no Cronograma Planejado.

* É criada uma nova composição com a nova quantidade informada e esta nova composição armazena a referência da Composição original;
* A nova Composição é vinculada a Tarefa de forma Ativa, inativando a Composição original também vinculada a Tarefa;
* Para executar o Processo deve-se obrigatoriamente ter valores preenchidos no Cronograma Realizado da Tarefa;
* Caso o Projeto utilize PERT, o Percentual Concluído da Tarefa no PERT deve estar coeso com o valor preenchido no Cronograma Realizado da Tarefa;
* O Replanejamento é realizado para todas as tarefas que sofrem impacto na Composição. Ao alterar a quantidade de uma tarefa, a diferença da quantidade alterada será aplicada no recurso ativo.
* O Replanejamento com Vigência de Recurso permite a alteração de índice (quantidade) da composição auxiliar, desde que a mesma não tenha sido replanejada.
* Após o primeiro replanejamento de índice a tarefa não poderá ter seu recurso alterado para insumo ou transformada em Valor Cotado.
* Para utilizar a vigência em determinado período deve-se obrigatoriamente bloquear o (s) período (s) do cronograma realizado.
* O Processo de Replanejamento de índice iguala as quantidades do Cronograma Previsto com o Cronograma Realizado.
* Após a primeira Vigência de Recurso executada o sistema valida se o Cronograma Previsto encontra-se 100% (cem por cento) preenchido, caso não esteja deve-se obrigatoriamente preencher para prosseguir com a execução.
* Ao utilizar o processo de vigência de recursos não é mais permitido alterar a unidade da composição. Mesmo após usar o processo de Habilitar/Desabilitar Edição de Composições Replanejadas, se houver alguma alteração no campo "Unidade" irá retornar uma mensagem de erro dizendo: "Composição replanejada não pode ter sua unidade alterada".
* A tarefa associada irá receber a nova composição replanejada, mesmo se a tarefa já estiver sido realizada.

*Observação: Após o replanejamento a composição replanejada não pode ser alterada.*

Em Orçamento | Planilha | Planilha de Atividades (F10) | Anexos | Recurso da Tarefa, é possível visualizar todos os Recursos que tem vínculo com a Tarefa, sendo que apenas um estará ativo. É listado Período, Código da Composição, Descrição da Composição, Quantidade e Total. Este anexo é preenchido apenas para Tarefas que possuem Vigência de Recurso.

---
