---
content_hash: cb715e4ac9325fa6d408a603c7463bb7e34a17b657ded5bdf0ea36d55bffd9df
fetched_at: '2026-06-29T00:11:28.447491+00:00'
page_id: '731215136'
product: rm
source: tdn-rm
title: 04 - Alocar horário/professor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=731215136
version: 67
---

Esta etapa consiste na funcionalidade para realização da montagem do quadro de horário das turmas/disciplinas do planejamento de oferta, assim como a alocação de professores nas turmas que possuam alocações em horários.

### **Permissão de acesso**

Para ter acesso a etapa de alocar horário/professor no processo de planejamento de oferta, o usuário autenticado deve possuir a seguinte permissão de usuário no seu Perfil:

Acessar RM.exe I Menu | Serviços Globais | Perfil | Educacional | Acesso ao Menus | Educacional | Educacional (Portal) | Gestão Educacional | Gestão de ofertas | Alocação de professores

### **Filtros da etapa do processo**

Os filtros curso, habilitação, matriz e turno passam a ser obrigatórios para o preenchimento nesta etapa, onde o botão de Selecionar somente será habilitado, após a seleção destes filtros.  
O filtro Período não é obrigatório, podendo ser selecionado como Todos ou sendo selecionado algum período específico. Caso este filtro seja selecionado com a opção Todos, serão exibidos um quadro de horário para cada período onde possuam turmas/disciplinas planejadas geradas. **OBS. Ao selecionar o idhabilitacaofilial que já tem oferta gerada, o quadro de horário não será exibido e emitirá validação.**

### **Exibição dos horários disponíveis no quadro de horário**

Para que seja exibido um quadro de horário, com os horários desejados para a alocação de Turmas e Professores, é necessário que cada um dos horários cadastrados no Turno selecionado no filtro estejam parametrizados como disponíveis para o planejamento de oferta, através da seleção do campo Disponível para o planejamento de oferta no cadastro de Horário, anexo de Turno, disponível em: ( Currículo e Oferta | Acadêmico | Turnos e Horários).

Após a parametrização de todos os horários que serão disponíveis para o planejamento, será possível realizar a alocação de Turmas de planejamento e Professores nestes horários.

### **Horários indisponíveis para a alocação**

Somente horários disponíveis para o planejamento serão exibidos e disponíveis para alocações de turmas e consequentemente professores. Horários que são cadastrados e disponibilizados apenas em um dos dias da semana e não em outro, somente serão habilitados para alocação no dia correspondente. Nos demais dias, os horários estarão desabilitados, identificado com a cor cinza, indicando que não estarão disponíveis para a alocação, conforme exemplo abaixo:

O quadro de horário acima, possui os horários de 22:40 às 23:30 desabilitados de Terça-feira até Sexta-feira, isso porque só foi cadastrado este horário, ou disponibilizado para alocação apenas na Segunda-feira. Portanto, somente segunda-feira deixará o horário disponível para alocações de Turmas, enquanto nos demais não poderão ser alocados nenhuma Turma.

### **Considerar apenas professores autorizados na disciplina**

As alocações de professores, podem ser validadas para identificar se o professor alocado em uma disciplina possui autorização para ministrar a disciplina em questão. Para que o processo de alocação do planejamento de oferta realize estas validações, deve ser habilitado o parâmetro conforme abaixo em: Parâmetros | Secretaria | Geral 1/7 - "Considerar somente disciplinas autorizadas dos professores".

Caso este parâmetro esteja marcado, no cadastro de professor deve ser realizado o cadastro das disciplinas em que cada professor possui autorização para lecionar através do anexo [Disciplinas do Professor](https://tdn.totvs.com/display/LRM/Disciplinas+do+Professor).

### **Disponibilidade de horário de professor**

As alocações dos professores podem ser validadas de acordo com a disponibilidade de horários de cada professor. Desta forma, o processo de alocação poderá alertar professores que não possuam disponibilidade em horários em que foram alocados.

Para cadastrar disponibilidade de horário do professor, pode-se utilizar o cadastro de disponibilidade no RM, localizado em Currículo e Oferta | Professores | Disponibilidade do professor, ou a mesma funcionalidade também disponível no Corpore.Net onde os próprios professores podem informar sua disponibilidade.

### 

Para que a disponibilidade do professor seja considerada durante o processo de alocação, deve haver pelo menos um cadastro de disponibilidade para o período letivo correspondente ao que está sendo planejado. Caso o professor não possua nenhum horário de disponibilidade cadastrado, o professor será considerado disponível em todos os horários.

Aviso: Validação de disponibilidade de horário

As validações aqui realizadas para alocação do professor em horário são **exclusivas** do Planejamento de Oferta.

### **Listagem de disciplinas**

As disciplinas disponíveis para alocação de horários, serão apenas disciplinas que estiverem sendo planejadas nas etapas anteriores a etapa de Alocar horário/professor, e correspondente ao seu período.

### 

Desta forma, as disciplinas exibidas na aba Disciplina, serão o grupo de disciplinas planejadas de acordo com o filtro selecionado. Vale ressaltar que o nome da disciplina será o seu nome reduzido se houver. Caso não tenha nome reduzido, o nome completo será exibido, porém o mesmo será cortado em 30 caracteres, sendo 27 caracteres para o nome da disciplina e 3 caracteres para os três pontinhos. Somente disciplinas com o nome reduzido terão o hint ao passar o mouse em cima do ícone  na lista de disciplinas, entretanto este ícone não fica disponível no quadro de horário, apenas na lista de disciplinas.

### 

### **Disciplina Gerencial**

Quando a disciplina foi parametrizada como Gerencial ( Na Etapa: Gestão de Turmas) será exibido o ícone:  ao lado da disciplina; ao colocar o cursor do mouse será apresentado um *tooltip* informando que é uma disciplina Gerencial e ao clicar sobre o mesmo, será listado a relação de disciplinas Gerenciadas que estão associados à ela, conforme a imagem abaixo:

### 

### **Disciplina Gerenciada**

As turmas/disciplinas gerenciadas não são listadas ao realizar uma consulta na etapa de alocação de horário/professor. Isso acontece porque essas turmas seguem as definições feitas para a turma/disciplina gerencial, ou seja, quando a turma/disciplina gerencial for alocada em algum horário do quadro de horários, o mesmo acontecerá para as turmas/disciplinas gerenciadas. Dessa forma, as turmas/disciplinas gerenciadas não são listadas garantindo assim, que o usuário não realiza alterações nas mesmas sem passar antes pela turma/disciplina gerencial.

No quadro de horários, as turmas/disciplinas gerenciadas aparecem, mas o usuário não poderá realizar nenhuma ação, tal como excluir a disciplina do horário, alterar/incluir professores, ou mesmo arrastar a turma/disciplina para outro horário. Qualquer ajuste dessa natureza precisa ser feita na turma/disciplina gerencial.

### **Disciplina Livre**

Quando a disciplina foi parametrizada como Livre (sem o vínculo da Matriz Aplicada) configurado na Etapa: Gestão de Turmas, ao informar o tipo de Curso como: Turma Livre e Turno, ao carregar o Quadro de horários, será apenas a informação do Turno em que a(s) disciplina(s) foram configuradas, conforme a imagem abaixo:

### 

### **Listagem de subturmas**

As subturmas das disciplinas disponíveis para alocação de horários, serão apenas disciplinas que estiverem sendo planejadas nas etapas anteriores a etapa de Alocar horário/professor, com subturma gerada e correspondente ao seu período.

### 

Quando uma disciplina possuir subturma será possível alocá-la em algum horário, para isso, basta abrir a seta  na linha da disciplina, ao clicar nela será exibida todas as subturmas daquela disciplina.

### 

Ao clicar na seta, as subturmas disponíveis serão exibidas conforme abaixo.

### 

Após a alocação da subturma em algum horário, será possível alocar professor na subturma naquele horário. Com isso é possível alocar professor apenas na disciplina, apenas na subturma ou em ambas entidades.

### 

### **Listagem de Professores**

Os professores disponíveis para alocação de horários(Aba| Docentes) serão todos os professores que tenham histórico de ter lecionado as disciplinas no passado (anexo professor turma), que tenham vínculos com as disciplinas do período. seguindo a seguinte regra:

1. O professor deve possuir permissão na Filial em que está sendo planejado, através do anexo Filiais do professor do cadastro de Professor, e que este cadastro esteja Ativo.
   1. Se o professor possuir uma chapa definida no cadastro de Filiais do professor, a chapa não deve estar com o status de Demitido.
   2. Se não possuir chapa definida, apenas o campo Ativo é considerado.
2. O professor que tenha usuário gerado, esteja alocado no Nível de ensino conforme o Planejamento está sendo elaborado.

Desta forma, todos os professores que correspondem as condições acima, serão listados na aba Docentes.

### 

### **Listagem de professores disponíveis para alocação**

Quando o parâmetro Parâmetros | Secretaria | Geral 1/7 | "Considerar somente disciplinas autorizadas dos professores" estiver marcado, a lista de professores exibidos na aba de Docentes, irá conter apenas os professores aptos a ministrar alguma das disciplinas exibidas na aba Disciplinas no seu anexo Disciplinas autorizadas no cadastro de Professor.

### 

### **Realizando alocação de Turmas**

Para realizar alocação de horários das Disciplinas e Professores, deve-se utilizar o recurso de arrastar e soltar. Para alocar uma disciplina em um determinado horário, basta selecionar uma das disciplinas disponíveis na aba Disciplinas e arrastar para dentro de um horário desejado, conforme exemplo abaixo:

### 

Com o objetivo de otimizar o processo de montagem do quadro de horários, agora é possível alocar uma turma/disciplina em múltiplos horários simultaneamente. Essa melhoria reduz ações repetitivas e aumenta a eficiência.

Em cenários onde uma mesma disciplina ocorre diversas vezes na semana (por exemplo, 5 aulas), o usuário não precisa mais realizar a alocação manual de cada horário individualmente.

Para utilizar a funcionalidade:  
Pressione e mantenha pressionada a tecla **Ctrl**, selecione múltiplos horários e, em seguida, clique na turma/disciplina. Arraste para um dos horários selecionados e solte o mouse. O sistema realizará automaticamente a alocação em todos os horários escolhidos.

**Observações:**

* Apenas horários disponíveis podem ser selecionados.
* Caso um ou mais horários já estejam ocupados com a disciplina, a operação será cancelada.
* Esta funcionalidade não se aplica ao arraste de professores.

**Disponível a partir das versões:**  
12.1.2510.182 e 12.1.2602.107

### **Botão de seleção de professores**

Cada disciplina alocada, quando ainda não houver nenhum professor alocado no horário da disciplina, irá exibir um botão "+" logo abaixo da disciplina onde permite ao usuário exibir uma nova janela listando apenas os professores que estão aptos a ministrarem a disciplina selecionada, além de professores onde ainda possuam disponibilidade no horário desejado conforme exemplo abaixo:

### 

Duas ou mais disciplinas no mesmo horário

No exemplo abaixo, o mesmo horário possui duas disciplinas alocadas. Sendo que cada disciplina pode ser definida diferentes professores.

### 

### **Exclusão de alocação de disciplina**

O ícone de lixeira exibido na alocação da disciplina aciona um modal onde pode-se escolher entre acionar  além de excluir também todas as alocações dos professores deste horário, caso houverem.

### **Movendo alocações de disciplinas já alocadas**

Qualquer disciplina já alocada, também pode ser remanejada para qualquer outro horário do quadro de horário, sem a necessidade de exclusão da alocação e alocação em um novo horário. Para isso, basta arrastar uma disciplina já alocada para dentro de um outro horário desejado, conforme exemplo abaixo:

### 

### **Realizando alocação de Professores**

Para realizar alocação de horários de professores, segue a mesma lógica utilizada na alocação de disciplinas, porém, somente serão possíveis alocar professores em disciplinas já alocadas. Não é possível alocar professores em horários disponíveis sem que haja disciplina alocada no horário. Para alocar um professor em um determinado horário, basta selecionar a aba de Docentes, e arrastar o professor desejado para dentro de uma disciplina desejada, conforme exemplo abaixo:

### 

Ao clicar na disciplina alocada, os nomes dos professores que já lecionaram essa disciplina anteriormente estão destacados em verde.

### 

Ao tentar alocar um professor por meio do botão '+', será exibida uma lista com todos os docentes. Aqueles que já lecionaram a disciplina no passado, aparecerão em preto, enquanto os que já a lecionaram, mas não possuem disponibilidade de horários, serão exibidos em vermelho.

### **Alocação de professor para todas as disciplinas já alocadas automaticamente**

Quando a mesma disciplina já está alocada em vários horários do quadro de horário, ao alocar um novo professor, ele será alocado automaticamente em todos os horários desta mesma disciplina sem a necessidade que seja alocado individualmente o professor em todas as ocorrências da disciplina, conforme exemplo abaixo:

### 

### **Alocação de professor em um horário pontual**

Em algumas situações pode ser desejado alocar um professor em apenas um horário específico da disciplina, e não em todos os horários em que a disciplina está alocada. Para alocar um professor em apenas um horário específico, basta fazer a alocação do professor mantendo a tecla Control no teclado (Ctrl) pressionada durante o arrasto do professor na disciplina, conforme exemplo abaixo:

### **Botão de seleção de professores disponíveis**

Outra forma de alocar um professor em uma disciplina alocada, é selecionar botão "+" exibido logo abaixo da disciplina. Será exibido uma nova janela com a lista de professores aptos a ministrar a disciplina selecionada, desde que possuam disponibilidade de horários, e não possuam choques de horário no horário. Também será possível selecionar mais de um professor ao mesmo tempo, alocando um ou mais professores de forma simultânea.

Aqueles Professores que já lecionaram a disciplina no passado, aparecerão em preto, enquanto os que já a lecionaram, mas não possuem disponibilidade de horários, serão exibidos em vermelho.

### **Alocando mais de um professor na mesma disciplina**

Cada disciplina alocada no quadro de horário pode possuir mais de um professor que irá ministrar a disciplina. Desta forma, pode ser selecionado mais de um professor na seleção de professores, ou arrastar um novo professor para dentro da disciplina desejada, conforme exemplo abaixo:

### **Exclusão de alocação de professor**

Cada professor já alocado, pode ser excluído de forma individual ou em lote. Para excluir o professor, selecione a lixeira ao lado da alocação do professor desejado, onde em seguida, será apresentado uma mensagem conforme o exemplo abaixo:

### **Movendo alocação de professor de uma disciplina para outra**

É possível mover as alocações de professores definidos em uma determinada disciplina para outra disciplina. Somente é possível mover a alocação de professores para outra disciplina, e não para horários que ainda não possuam nenhuma disciplina alocada, conforme exemplo abaixo:

### **Movendo alocação de disciplinas juntamente com professores**

Caso a disciplina seja remanejada para um novo horário, e ela já possua uma alocação de professor associada, será alterado o horário da alocação da disciplina e todos os professores também serão movidos juntamente com a disciplina, conforme exemplo abaixo:

**Realizando alocação de Professores sem horário**

Caso a instituição não tenha os horários definidos para os professores, é possível realizar a alocação apenas do professor na turma, conforme abaixo:

Os professores disponíveis para alocação de horários(Aba| Docentes) serão todos os professores que tenham histórico de ter lecionado as disciplinas no passado (anexo professor turma), que tenham vínculos com as disciplinas do período.

Ao clicar na disciplina alocada, os nomes dos professores que já lecionaram essa disciplina anteriormente estão destacados em verde.

Ao tentar alocar um professor por meio do botão '+', será exibida uma lista com todos os docentes. Aqueles que já lecionaram a disciplina aparecerão em preto.

**Validações**

O processo de alocação de horários de disciplinas e professores, contam com três validações principais que ocorrem após a alocação de um novo professor. Estas validações não ocorrem durante a alocação de novas disciplinas. São elas:

* **Validação de choque de horário entre as alocações do professor**
* **Validação da disponibilidade de horário do professor, em relação a alocação realizada**
* **Validação da autorização para ministrar a disciplina, em relação a alocação realizada**

Regras de validação

As validações realizadas durante o processo de alocação de horários, **não tem o objetivo de impedir nenhum tipo de alocação**, e sim **apenas informar** para o usuário que uma das três situações mencionadas acima podem ter ocorrido após alguma alocação de professor. Portanto, o usuário terá total autonomia para manter a alocação

### Exibição das validações no quadro de horário

Caso ocorra uma (ou mais) situações mencionadas acima no quadro de horário, irá ser exibido a disciplina na cor alaranjado, indicando que há a ocorrência de alguma validação. O professor que possuir a incidência de uma (ou mais) validações, será destacado na cor amarela, para identificar qual dos professores da disciplina está sendo alertado. No exemplo abaixo, a professor **Patricia Luiza Rangel**, não possui nenhum alerta referente a disciplina de **Estágio Supervisionado I.** Apenas a professora **Rosana Dos Reis Silva** possui algum tipo de validação sendo alertada.

### Detalhes das validações encontradas

Em cada disciplina que ocorre algum alerta nas validações, possuirão um ícone para exibir mais detalhes sobre o alerta. Os detalhes exibirão em uma nova janela, todas as ocorrências de validações para todas as disciplinas exibidas no quadro de horário, e não apenas as validações da disciplina em que foi selecionada a opção de mais detalhes da validação. Portanto, para exibir os detalhes, basta clicar no botão **Detalhes de validações de alocação**, de qualquer disciplina, conforme exemplo abaixo:

### Validação de choque de horário entre as alocações do professor

Esta validação identifica se já existe uma alocação do professor no mesmo horário porém, em qualquer outro curso ou disciplina exatamente no mesmo horário. Neste caso, a validação irá destacar a disciplina e também o professor dentro do quadro de horário. Ao exibir mais detalhes de validação, serão listados quais são os choques de horários encontrados na validação, conforme exemplo abaixo:

### **Validação da disponibilidade de horário do professor**

Esta validação identifica se um professor foi alocado em um determinado horário no qual ele não possui disponibilidade de horário no seu cadastro de **Disponibilidade de horários.** No exemplo seguinte, a professora Rosana possui disponibilidade de horário apenas na segunda-feira, e na terça de 07:00 às 08:00. Portanto a validação indica que o horário de 07:50 às 08:40 possui um alerta de validação. Quando esta situação ocorrer, será exibido a validação conforme exemplo abaixo:

### **Validação da autorização para ministrar a disciplina**

Esta validação identifica se um professor foi alocado em um horário de uma disciplina na qual ele não possui autorização para ministrar tal disciplina. Esta validação ocorre apenas quando o parâmetro **Parâmetros | Secretaria | Geral 1/7 | "****Considerar somente disciplinas autorizadas dos professores"** estiver marcada, e quando o professor possui ao menos uma disciplina cadastrada no anexo **Disciplinas autorizadas** no seu cadastro de professor. Quando ocorrer essa situação, será exibido a validação conforme exemplo abaixo:

### **Horário modular**

Permite o cadastro e a gestão de turmas/disciplinas que não seguem o padrão contínuo de datas do período letivo, possibilitando o registro de horários modulares.  
Essa funcionalidade atende situações em que uma disciplina é ofertada em blocos de tempo específicos, com intervalos ou datas diferentes do período letivo regular.

No modelo atual, todas as turmas/disciplinas assumem as mesmas datas de início e fim do período letivo. Contudo, existem exceções em que as aulas são organizadas de forma modular, por exemplo:

* Início após a data oficial do período letivo.
* Conclusão antes do término do período letivo.
* Oferta em blocos intercalados (ex.: semana sim/semana não; meses alternados).
* Alocação de horários e professores diferenciada por blocos de datas

O **Horário Modular** é a configuração que permite dividir uma disciplina em blocos de tempo independentes, dentro do período letivo, possibilitando:

* Gestão personalizada de datas.
* Alocação de professores diferentes por módulo.
* Visualização estruturada no quadro de horários.

A **alocação de professores (aba 1)** se aplica apenas ao bloco modular selecionado.

A **gestão de horário modular (aba 2)** centraliza todos os registros de horário modular da turma/disciplina, independentemente do bloco.

Somente professores já alocados na disciplina podem ser vinculados a blocos modulares. A inclusão de novos professores deve ser feita exclusivamente pela aba 1.

Utilizando a opção "Gerar horário por recorrência", é possível criar vários horários modulares de forma intermitente dentro de um período.

Cada bloco (disciplina + professor) é independente e pode ser movimentado no quadro de horários.

Após a montagem, é possível arrastar professores entre blocos.

Observação: O sistema **não permite** arrastar blocos de horário modular para:

* Um destino que já contenha a mesma disciplina sem horário modular.
* Um destino que já contenha a mesma disciplina

**Subturmas**

A alocação de horário modular para subturmas funciona seguindo as mesmas regras descritas anteriormente para horário modular da turma, salvo por ser necessário gerar subturmas na etapa de **Gestão de Turmas** do planejamento:

### **Geração da oferta do horário modular**

Ao processar a geração de oferta, a turma disciplina resultante possui os horários com as mesmas datas especificadas no respectivo horário modular do planejamento de oferta:

Horário da turma/disciplina no período letivo após geração de oferta:

**Geração da oferta do horário modular para  Sub-turma**

Ao marcar o parâmetro “Utilizar turma/disciplina e subturma com horários independentes”, é possível cadastrar horários modulares para a subturma. Dessa forma, ao realizar a geração de oferta, as subturmas são criadas com seus respectivos horários modulares e com os professores vinculados diretamente ao cadastro desses horários.
