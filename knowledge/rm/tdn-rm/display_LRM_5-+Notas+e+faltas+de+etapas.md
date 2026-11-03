---
content_hash: 7ff938175e4a9e1f329921da9bab3d9a0717a3bc702251e20b7fdbee832e141e
fetched_at: '2026-06-29T00:11:17.328865+00:00'
page_id: '679158646'
product: rm
source: tdn-rm
title: 5- Notas e faltas de etapas
type: documentation
url: https://tdn.totvs.com/display/LRM/5-+Notas+e+faltas+de+etapas
version: 102
---

Nesta tela, o professor poderá digitar as notas e faltas da etapa, inserir comentários (se necessário), liberar a visualização da etapa e encerrar a etapa para o(s) aluno(s).

Permissão de acesso

Para acessar esta funcionalidade, o **perfil do professor** deve possuir a seguinte permissão: **Serviços Globais → Segurança → Acesso → Perfil → Sistema: Educacional → Educacional (Portal) → Perfil do Professor → Diário de Classe → Notas de Etapa**

Filtros

O filtro **"Status na Disciplina"** exibirá os alunos conforme a seguinte regra:

* **Com resultado final (aprovado, reprovado, etc.):** será considerada a **situação final** do aluno na disciplina;
* **Sem resultado final:** será considerada a **situação atual de matrícula** do aluno na disciplina.

#### **Demais filtros disponíveis:**

* **Subturma**
* **Status na Disciplina**
* **Etapa de Notas**
* **Etapa de Faltas**

Filtros obrigatórios

É **obrigatório preencher ao menos um** dos seguintes filtros para realizar a consulta: **Etapa de Notas ou** **Etapa de Faltas**

Lista de alunos disponíveis

O portal exibirá os **alunos disponíveis na turma/disciplina** conforme a seguinte regra:

* A opção **“Disponível para digitação de notas/faltas e Agenda Infantil”** deve estar **marcada no cadastro da situação de matrícula** vinculada à disciplina do aluno.

Lista de etapas disponíveis

Após aplicar o **filtro por etapas**, será exibida uma **tabela** contendo o **nome dos alunos** e as **colunas correspondentes às etapas de notas e faltas** para cada aluno.

  
Visualizar de colunas "Etapas anteriores" de Notas ou Faltas

Para exibir as colunas de **“Etapas Anteriores”** de **Notas** ou **Faltas**, é necessário **habilitar o parâmetro** localizado em: **Gestão Educacional → Configurações → Configuração → Parâmetros → RM Portal → RM Portal - Gerais → Portal - Geral 5/15 → “Visualizar etapas anteriores na digitação de notas e faltas de etapa”**

Esta coluna é **somente para visualização** e **não permite a alteração dos valores exibidos**.

Visualizar as colunas de "Total Notas" ou "Total Faltas"

Para exibir as colunas de **“Total Notas”** ou **“Total Faltas”**, é necessário **habilitar o parâmetro** localizado em: **Gestão Educacional → Configurações → Configuração → Parâmetros → RM Portal → RM Portal - Gerais → Portal - Geral 5/15 → “Visualizar total das etapas na digitação de notas e faltas de etapa”.**

Esta coluna é **somente para visualização** e **não permite a alteração dos valores exibidos**.

O portal **não exibe** as colunas de **“Total Notas”** ou **“Total Faltas”** quando a **etapa selecionada não possui etapas anteriores**.

O portal **não exibe** a coluna **“Total Notas”** para avaliações cujo **tipo de nota seja conceitual**.

Coluna de Status

A coluna **“Status”** exibe a **situação de matrícula** do aluno na disciplina em que está matriculado.

Digitação de notas ou faltas

Ao selecionar o **botão “Pesquisar”**, o portal exibirá a **relação de alunos matriculados** nas turmas/disciplina correspondentes aos **filtros aplicados**.

Digitação de notas e faltas

A digitação de **notas ou faltas** ficará disponível **somente se forem atendidas as seguintes regras**:

* A **etapa e todas as suas avaliações** devem ter a opção **“Disponível para os alunos”** **marcada**;
* A etapa deve ter a opção **“Permite digitação diretamente na etapa”** **marcada**;
* A etapa deve ter o **“Período de Digitação” preenchido** e válido em relação à data atual. Caso **não esteja preenchido**, esta regra será desconsiderada;
* A etapa deve ter a opção **“Exibe no portal e na central do aluno”** **marcada**.

Turma mista

Ao registrar notas em uma **Turma Mista**, as informações serão replicadas para a **Turma de Origem**, desde que o cadastro das etapas e avaliações possua as mesmas configurações.  
O processo inverso, ou seja, o registro de notas na **Turma de Origem**, não será replicado para a **Turma Mista**.

Para mais informações, consulte a documentação disponível em: **Turma Mista**.

> **Importante:** as informações de **“Comentário”** e as funcionalidades **“Liberar Etapa”** e **“Liberar Avaliação”** não são replicadas entre as turmas.

Turma(s) de origem não estejam igualmente configuradas (Tipo de nota ou casas decimais)

O portal **não listará** as **turmas/disciplinas mistas** para o **ensino básico** caso algum aluno enturmado na Turma Mista possua **matriz curricular** cuja(s) Turma(s) de Origem **não estejam configuradas de forma equivalente**, seja no **Tipo de Nota** ou no **número de Casas Decimais**.

Bloquear alteração de notas e faltas

Esta regra **se aplica individualmente a cada aluno** da lista disponível.

O sistema **bloqueará a alteração das notas** caso a opção **“Bloquear alterações de notas e faltas”** esteja **marcada** no cadastro da **situação de matrícula** do aluno na disciplina.

Fórmula automaticamente

Para que a **fórmula da etapa de nota ou falta** seja **executada automaticamente**, é necessário **habilitar** o seguinte parâmetro: **Gestão Educacional → Configurações → Configuração → Parâmetros → Secretaria → Notas/Faltas → Executar fórmulas automaticamente**

Nota máxima da etapa

O portal possui um **recurso de validação** que **impede a digitação e o salvamento de notas** superiores aos **pontos distribuídos na etapa**.

Tipo de nota numérica

Este recurso está disponível **apenas para turmas/disciplinas cujo tipo de nota seja numérico**.

Somatório de nota

O portal possui um **recurso que valida o somatório das notas** lançadas na etapa selecionada para todos os alunos listados, comparando-o com o valor informado no campo **“Somatório notas”**:

* Se os valores forem iguais, o sistema **não exibirá nenhuma mensagem de alerta**;
* Se os valores forem diferentes, o sistema **notificará o professor sobre a divergência nas notas**;
* Se nenhum valor for informado no campo **“Somatório notas”**, o portal **não realizará nenhuma validação**.

A validação do somatório de notas tem caráter apenas informativo, não bloqueia o salvamento das notas em caso de divergência com o valor informado no campo **“Somatório notas”**, e este campo não é salvo, sendo limpo automaticamente a cada recarga das informações.

Tipos de Nota

O portal permite a digitação de **dois tipos de notas**: **numérica** ou **conceitual**.

Informação de Somatório notas

A informação de **“Somatório notas”** estará disponível **apenas para turmas/disciplinas com tipo de nota numérica**.

**1º**- **Notas conceituais**

Para **notas do tipo conceitual**, o sistema exibirá as **opções disponíveis**, permitindo que o professor selecione a nota correspondente.

**2º**- **Notas numéricas**

Para **notas do tipo numérico**, o sistema exibirá um **campo de entrada**, permitindo que o professor insira a nota correspondente.

Conceitos da disciplina

O portal **considerará a nota do tipo conceitual** apenas se o cadastro da etapa incluir as informações de **“Conceitos da disciplina”** e o **tipo de nota for conceitual**; caso contrário, se o tipo de nota for numérico, mesmo que os conceitos **estejam preenchidos**, o portal **considerará a nota como numérica**.

Obrigatório digitação de n° de aulas dadas - Etapa de Falta

Para a **etapa de falta**, o portal considerará a opção **“Obrigação digitação de nº de aulas dadas”** no cadastro da etapa.

* Se a opção estiver **marcada**, será **obrigatório informar o número de aulas dadas** para cada aluno com falta registrada.
* Se a opção estiver **desmarcada**, **não será necessário informar** o número de aulas dadas.

A coluna **“Aulas dadas”** na relação de alunos será atualizada automaticamente apenas quando o professor alterar o valor no campo **“Nº aulas dadas”**.

Parâmetros educacionais - "Alterar notas e faltas de etapas encerradas e/ou fora do período de digitação"

O parâmetro **“Alterar notas e faltas de etapas encerradas e/ou fora do período de digitação”**, disponível na aba **Notas e Faltas** dos **Parâmetros Educacionais** (localizados em: **Serviços Globais → Segurança → Acesso → Perfil → Sistema: Educacional → Educacional (Portal) → Perfil do Professor → Anexos → Parâmetros Educacionais → Notas e Faltas**), é **aplicável apenas ao RM.exe** e, portanto, **não impacta** as funcionalidades do menu **Notas e Faltas de Etapas** no **Portal do Professor**.

Quantidade de dígitos inteiros (antes da vírgula)

O portal deverá permitir a digitação de notas com a **mesma quantidade de dígitos inteiros** (antes da vírgula) correspondente ao **valor máximo definido para a avaliação**.

Liberar etapa

Para **exibir o botão “Liberar Etapa”**, é necessário habilitar o parâmetro **“Permitir a visualização das notas e faltas da etapa após a liberação do professor”**, disponível em: **Gestão Educacional → Configurações → Configuração → Parâmetros → Secretaria → Notas/Faltas**

Turma Mista

A funcionalidade de **“Liberar Etapa”** **não é replicada** da **Turma Mista** para a **Turma de Origem**.

Para mais informações, consulte a documentação disponível em: 

Encerrar etapa

A exibição do botão **“Encerrar Etapa”** ficará disponível **somente se forem atendidas as seguintes condições**:

* A etapa deve ter a opção **“Etapa final”** **marcada**;
* A etapa deve ter a opção **“Etapa encerrada” demarcada**.

Comentário

Será possível **inserir um comentário**, se necessário, clicando no ícone correspondente, o que habilitará uma **caixa de texto** para digitação.

> **Observação:** **não é permitido** **incluir ou alterar comentários** caso a etapa ou avaliação esteja marcada como **“Disponível para os alunos”**.

O **comentário do professor** **não está disponível** para visualização pelos **alunos** e seus **responsáveis**.

Turma Mista

A informação de **“Comentário”** **não é replicada** da **Turma Mista** para a **Turma de Origem**.

Para mais informações, consulte a documentação disponível em: 

Imprimir relatório

Para **exibir o botão “Imprimir”** no relatório das avaliações, é necessário que esteja configurado o **“URL de acesso ao Portal RM”** em: **Gestão Educacional → Ambiente → Parâmetros → Parâmetros Globais → Gerais → URL de acesso ao Portal RM**

No campo **“URL de acesso ao Portal RM”**, informe o endereço: [http://SERVIDOR/NOMEAPLICATIVO\_CORPORE.NET/](http://servidor/NOMEAPLICATIVO_CORPORE.NET/) (Exemplo: <http://servidor/corpore.net/>)

As funcionalidades que **ainda não foram migradas** para o **novo Portal do Professor** abrirão automaticamente uma **nova aba no navegador** ao serem acessadas. Nessa aba, o usuário será **redirecionado para o relatório correspondente no Portal do Professor antigo (Corpore.Net)**.

Casas decimais e Tipo de nota

A quantidade de **“Casas Decimais”** e o **“Tipo de Nota”** a serem considerados na tela são configurados conforme o contexto:

**1º-  Ensino Superior**

No contexto do **Ensino Superior**, as informações sobre o **número de casas decimais** e o **tipo de nota** estão disponíveis no **cadastro da disciplina**.

**2º-  Ensino Básico**

No contexto do **Ensino Básico**, as informações sobre o **número de casas decimais** e o **tipo de nota** estão disponíveis no **cadastro da disciplina da grade do aluno**.

**3º-  Itinerário Formativo**

No contexto do **Itinerário Formativo**, as informações sobre o **número de casas decimais** e o **tipo de nota** estão disponíveis no **cadastro da disciplina do itinerário formativo**.
