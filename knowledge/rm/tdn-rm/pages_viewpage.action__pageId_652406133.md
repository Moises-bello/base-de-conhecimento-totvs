---
content_hash: d4423ed1bb7204545c0167202ad65cb525d06f83a21f80818f31943196258e14
fetched_at: '2026-06-29T00:11:12.381362+00:00'
page_id: '652406133'
product: rm
source: tdn-rm
title: 4- Notas de avaliação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=652406133
version: 141
---

Nesta tela, o professor poderá digitar as notas de avaliação, inserir comentários (caso necessário), liberar a avaliação para visualização e liberar a etapa para o(s) aluno(s).

Permissão de acesso

Para acessar a funcionalidade, o perfil do professor deverá ter a permissão em: **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Notas de Avaliação.**

Filtros

O filtro "Status na Disciplina" exibirá os alunos de acordo com a seguinte regra:

* Se o aluno **possuir resultado final** (aprovado, reprovado, etc.), será considerada a **situação final** na disciplina.
* Se o aluno **ainda não possuir resultado final**, será considerada a **situação atual de matrícula** na disciplina.
Lista de alunos disponíveis

O portal listará os alunos disponíveis na turma/disciplina conforme a seguinte regra:

A opção **"Disponível para digitação de notas/faltas e Agenda Infantil"** deve estar **marcada** no cadastro da **situação de matrícula vinculada à disciplina do aluno**.

Lista de avaliações disponíveis

O portal  listará as avaliações disponíveis na turma/disciplina, considerando a seguinte regra:

Avaliações com subturma

Para listar as avaliações disponíveis na turma/disciplina de uma subturma na qual o aluno está matriculado, o sistema seguirá a seguinte regra:

1. **Se o aluno estiver matriculado em uma subturma e a turma/disciplina possuir subturmas:**  
   O sistema deverá exibir apenas as avaliações: vinculadas à subturma na qual o aluno está matriculado, ou que estiverem com a opção **"Disponível para todas as subturmas"** **marcada**, ou que **não estiverem vinculadas a nenhuma subturma**.
2. **Se o aluno estiver matriculado apenas na turma/disciplina e esta não possuir subturmas:**  
   O sistema deverá exibir **todas as avaliações da turma/disciplina**.
3. **Se o aluno estiver matriculado apenas na turma/disciplina e esta possuir subturmas:**  
   O sistema deverá exibir **todas as avaliações da turma/disciplina**, **independentemente** de estarem ou não vinculadas a alguma subturma.
Coluna de Status

A coluna "Status" corresponde à situação de matrícula do aluno na disciplina em que está matriculado.

Coluna de nota na etapa

A coluna **"Nota na Etapa"** exibe as notas atribuídas ao(s) aluno(s) na etapa de avaliação selecionada. O título da coluna corresponde à descrição da etapa escolhida. As notas serão listadas apenas se existirem registros para a etapa em questão.

**Esta coluna é apenas para visualização, não sendo possível alterar seu valor nesta tela.**

Digitação de notas

Ao selecionar o botão "Pesquisar", o portal listará a relação de alunos matriculados nas turmas/disciplina correspondentes aos filtros aplicados.

Digitação de notas

A digitação de notas ficará disponível caso sejam atendidas as seguintes regras:

* A etapa deve estar com a opção **"Período de Digitação"** **preenchida e válida** em relação à data atual. Caso esta opção **não esteja preenchida**, a regra será desconsiderada.

* A etapa deve estar com a opção **"Exibe no portal e na central do aluno"** **marcada**.

Turma Mista

Ao registrar notas em uma **Turma Mista**, as informações serão replicadas para a **Turma de Origem**, desde que o cadastro das etapas e avaliações possua as mesmas configurações.  
O processo inverso, ou seja, **o registro de notas na Turma de Origem, não será replicado para a Turma Mista**.

Para mais informações, consulte a documentação disponível em: **.**

> **Importante:** As informações de **"Comentário"** e as funcionalidades **"Liberar Etapa"** e **"Liberar Avaliação"** **não são replicadas** entre as turmas.

Turma(s) de Origem não estejam igualmente configuradas (Tipo de Nota ou Casas Decimais)

O portal **não listará as turmas/disciplinas mistas para o ensino básico** caso algum aluno enturmado na **Turma Mista** possua matriz curricular cuja(s) **Turma(s) de Origem** **não estejam configuradas** de forma equivalente, seja no **Tipo de Nota** ou no número de **Casas Decimais**.

Mensagem de alerta quando a(s) turma(s)/disciplina(s) de origem não estejam devidamente configuradas (Código de alguma avaliação diferente) de acordo com a turma(s)/disciplina(s) mistas

Ao registrar notas em uma Turma Mista, caso o código da avaliação **esteja cadastrado apenas na** **Turma Mista** e **não** na **Turma de Origem**, o sistema **tentará cadastrar essa avaliação** na Turma de Origem, aplicando a seguinte validação:

* **A soma do valor de todas as avaliações já cadastradas na Turma de Origem** **+ soma o valor da nova avaliação a ser cadastrada** deve ser **menor que os "Pontos distribuídos" na Etapa**.

**Caso não atenda o critério acima, será exibido o alerta abaixo**:

Exemplo

Caso existam avaliações cadastradas em uma etapa cujo total de pontos distribuídos seja igual a 10:

* Avaliação 1, Valor =  2
* Avaliação 2, Valor =  2
* Avaliação 3, Valor =  1
* Avaliação 4, Valor =  2
* Avaliação 5, Valor =  3

O portal tenta cadastrar a Avaliação 6 com valor 3, mas será exibido um alerta (conforme o primeiro print), pois a soma das notas de todas as avaliações já cadastradas (totalizando 10 pontos) mais o valor da Avaliação 6 (3 pontos) ultrapassaria o limite de pontos distribuídos na etapa (que é 10 pontos). Ou seja, a inclusão da Avaliação 6 excederia em 3 pontos o total permitido para a etapa.

Bloquear alteração de notas e faltas

**Esta regra se a aplica a cada aluno da lista disponível**

O sistema **bloqueará** a alteração das notas caso a opção "**Bloquear alterações de notas e faltas**" esteja **marcada** no cadastro da situação de matrícula na disciplina.

Nota máxima da avaliação

O portal possui um recurso de validação que **impede a digitação e o salvamento** de notas superiores ao valor máximo definido para a avaliação.

Tipo de nota numérica

Esse recurso está disponível apenas para turmas/disciplinas cujo tipo de nota seja **numérico**.

Nota do aluno abaixo da média

O portal possui o recurso de exibir as notas das avaliações e da etapa em **vermelho** caso estejam **abaixo da média da avaliação e da etapa**, respectivamente. Caso a média da avaliação ou da etapa **não esteja informada**, a validação correspondente não será realizada.

Tipo de nota numérica

Esse recurso está disponível apenas para turmas/disciplinas cujo tipo de nota seja **numérico**.

Apenas informativo

Este recurso é **apenas informativo** e **não bloqueia** a inserção de notas.

Quantidade de dígitos inteiros (antes da vírgula)

O portal deverá permitir a digitação de notas com a mesma quantidade de dígitos inteiros (antes da vírgula) correspondente ao valor máximo definido para a avaliação.

Digitação na avaliação descritiva

A avaliação descritiva consiste em um procedimento realizado exclusivamente pelo portal, no qual os professores avaliam manualmente cada aluno matriculado em suas turmas/disciplinas. Para mais informações, consulte: **[Avaliação descritiva](https://tdn.totvs.com/x/6Yf-L)**

Liberar avaliação

Para exibir o botão de "Liberar Avaliação", é necessário marcar o parâmetro "Permitir a visualização das notas das avaliações e faltas somente após a liberação do professor". Esse parâmetro está disponível em: **Gestão Educacional | Configurações | Configuração | Parâmetros | Secretaria | Notas/faltas**

Na liberação de visualização de uma avaliação, é possível habilitar a execução de uma fórmula previamente cadastrada.

Botão desabilitado

O botão **"Liberar Avaliação"** será habilitado **apenas** quando for selecionada uma única avaliação no filtro "Avaliações" da tela.

Turma Mista

A funcionalidade de "**Liberar avaliação**" **não é replicada** da **Turma Mista** para a **Turma de Origem.**

Para mais informações, acessar a documentação disponível em:

Liberar etapa

Para exibir o botão de "Liberar Etapa", é necessário marcar o parâmetro "Permitir a visualização das notas e faltas da etapa após a liberação do professor". Esse parâmetro está disponível em: **Gestão Educacional | Configurações | Configuração | Parâmetros | Secretaria | Notas/faltas**

Turma Mista

A funcionalidade de "**Liberar etapa**" **não é replicada** da **Turma Mista** para a **Turma de Origem.**

Para mais informações, acessar a documentação disponível em:

Comentário

Será possível inserir um comentário caso necessário. Basta clicar no ícone:  ,  que habilitará uma caixa de texto para a inserção do comentário.

**Não é permitido incluir ou alterar um comentário** caso a etapa ou avaliação **esteja "Disponível para os alunos".**

O comentário do professor não está disponível para visualização pelos alunos e seus responsáveis.

Turma Mista

A informação de "**Comentário"** **não é replicada** da **Turma Mista** para a **Turma de Origem.**

Para mais informações, acessar a documentação disponível em:

Imprimir relatório de avaliação

O botão "Liberar Avaliação" será habilitado **somente** quando for selecionada uma única avaliação no filtro "Avaliações" da tela.

Para exibir o botão "Imprimir" nos relatórios das avaliações, é necessário que o relatório — cuja tabela principal seja a SNOTAS — esteja configurado em: **Gestão Educacional > Configurações > Configuração > Parâmetros > RM Portal > RM Portal - Gerais.**

Casas decimais e Tipo de nota

A quantidade de "Casas Decimais" e o "Tipo de Nota" a serem considerados na tela são configurados conforme o seguinte contexto:

**1º-  Ensino Superior**  
No contexto do Ensino Superior, as informações sobre o número de casas decimais e o tipo de nota estão disponíveis no cadastro da disciplina.

**2º-  Ensino Básico**

No contexto do Ensino Básico, as informações sobre o número de casas decimais e o tipo de nota estão disponíveis no cadastro da disciplina da grade do aluno.

**3º-  Itinerário Formativo**

No Itinerário Formativo, as informações sobre o número de casas decimais e o tipo de nota estão disponíveis no cadastro da disciplina do itinerário formativo.

Fórmula visual

O portal também possui o recurso de Fórmula Visual. **Para saber mais acesse** **[Fórmula Visual](https://tdn.totvs.com/x/lC4mDg)**

* Data Server: **EduAlunoProvaData**
* Gatilhos disponíveis:
  + Ler os registros:
    - ****Antes da Leitura da Edição****
    - ****Após a Leitura de Edição****
  + Salvar os registros:
    - ****Antes de Salvar um Registro****
    - ****Após Salvar o Registro****
Visualizar entregas

Disponível a partir da versão 12.1.2502

Essa funcionalidade permite visualizar as entregas feitas pelos alunos em avaliações que aceitam submissão de arquivos. Na interface de visualização, é possível pré-visualizar arquivos nos formatos PDF, PNG, JPEG e TXT diretamente no sistema. Além disso, para esses e outros tipos de arquivos, é possível fazer o download para visualizá-los em seu computador.

A funcionalidade também possibilita marcar as entregas como visualizadas, facilitando o acompanhamento do progresso.

Ao acessar o menu "Notas de Avaliação" e selecionar uma avaliação que tenha entrega de trabalho parametrizada, será exibido um ícone indicando se a entrega foi realizada ou não pelo aluno.

* **Entrega ainda não foi realizada pelo Aluno**
* **Entrega realizada** pelo aluno e ainda não foi confirmado como visualizado pelo professor
* **Entrega realizada e o professor já confirmou o recebimento**

Para o professor conformar o recebimento, é necessário que o mesmo, acesse a entrega do Aluno, através do ícone: , onde o professor será redirecionado uma uma tela, onde o mesmo poderá visualizar os detalhes da entrega e o arquivo anexado pelo aluno.

Para confirmar o recebimento, o professor deverá clicar no botão: Marcar como visualizado.

Onde ao clicar, será exibido a mensagem que a entrega foi marcada como visualizada e o professor será redirecionado para a tela inicial e o ícone será alterado para  ( Entrega realizada e confirmado o recebimento).

### Visualização do processo
