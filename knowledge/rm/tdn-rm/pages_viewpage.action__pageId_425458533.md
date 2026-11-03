---
content_hash: 9c3d63e98a95c28a1f1d175fe31f40d5c6bbdd853e1565cc6d83115dbddf0e78
fetched_at: '2026-06-29T00:09:30.817055+00:00'
page_id: '425458533'
product: rm
source: tdn-rm
title: Exportação de dados para o Urânia
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458533
version: 5
---

---

Este processo, executado via TOTVS Educacional, é responsável pela geração do arquivo **URANEXP.XML**. Ele estará disponível para utilização exclusivamente quando a integração com o sistema Urânia estiver habilitada no menu Integrações | Urânia.

Ao executar o processo o usuário deverá definir as parametrizações para a exportações de dados, nesta etapa deverá ser informado o período letivo, o turno, quais entidades que serão exportadas (Disciplinas, turmas, professores, grade -turma/disciplina), total de aulas por dias das turmas, quais os dias da semana que irão ocorrer as aulas e onde será gerado o arquivo com os dados que será importado para o Urânia.

Regra de Validação: Total de Aulas por Dia

Um ponto de atenção essencial na parametrização é o campo **Total de aulas por dia das turmas**. Este campo define a expectativa de quantidade de horários para cada turma que o Urânia vai considerar para a montagem de horário.

**Lógica de Cálculo:** O sistema realiza a soma dos horários de cada **Agrupamento** em que as  estão inseridas e compara esse total com o valor informado no processo de exportação.

> **Exemplo Prático:**
>
> * **Cenário:** Turma `T12026.1` vinculada ao **Agrupamento 2**.
> * **Configuração do Agrupamento:** Possui apenas **01 horário** cadastrado (ex: 08:40 – 09:30).
> * **Parametrização do Processo:** Usuário informa **02** no campo **total de aulas por dia das turmas**.
> * **Resultado:** Como a soma do **agrupamento** **2** é 1, ele diverge do parametrizado (**total de aulas por dia das turmas**) que é **2**, o sistema emitirá um alerta.

**Tratamento de Divergências:** Caso haja inconsistência entre o número de horários do agrupamento e o valor total de aulas definido, o sistema exibirá o seguinte aviso:

> *"Turma 'T12026.1'. O número de horários por dia do agrupamento da turma é diferente do valor total de aulas do processo. A turma será incluída no arquivo XML, mas verifique se é necessário realizar um ajuste no número de aulas no processo ou incluir agrupamentos de horários para o turno da turma."*

**Observação:** O alerta não impede a geração do arquivo `.XML`, mas serve como um indicativo.

Caso as entidades Disciplinas, Turmas ou Grade sejam selecionadas, o sistema incluirá uma etapa adicional para a seleção das turmas. Essa definição pode ser realizada por meio de:

* Filtros de Turma: utilizando os parâmetros de curso, habilitação e turma;
* Consulta SQL: para seleções personalizadas via banco de dados;
* Filtros Globais: para aplicar critérios predefinidos no sistema.

Adicionalmente, ao selecionar a entidade Professor, será exibido um passo específico para identificar e filtrar os docentes que farão parte do processo de importação.

Ao concluir a execução do processo será exibido informações no log das entidades que foram exportadas para o arquivo **URANEXP.XML**. O arquivo criado está seguindo o layout definido disponibilizado pelo Urânia.

**Importante**  
O log do processo irá informar:

* Se existir turmas associadas a um turno que não possui nenhum agrupamento de horário informado;
* Se existir turmas que  não tiver agrupamento de horário definido e o turno associada tiver a definição de mais de um agrupamento;
* Se o número de horários do agrupamento da turma for diferente do valor total de aulas definido no processo;
* Quando existir informações no layout do urânia menores que as respectivas informações do TOTVS Educacional e que precisarem forem truncadas;
* Cadastros que não foram exportados.

Ao executar o processo, se estiver parametrizado para exportar "Grades" (turmas/disciplinas) irá apenas as turmas/disciplinas ativas e que não sejam gerenciadas.

**Consistências realizadas no processo**

Nome da turma

O campo "Nome turma" do arquivo de "turmas" está relacionado ao nome reduzido do cadastro de turma do TOTVS Educacional. Caso o campo do cadastro da turma estiver vazio ou for maior que o definido no layout, a turma não será informada no arquivo.

Número de aulas

O campo "Número de aulas" do arquivo de "Disciplinas" está relacionado ao número de aulas do cadastro de turma/disciplina do TOTVS Educacional e este deve estar preenchido, caso o mesmo esteja em branco a  a turma/disciplina não será informada no arquivo.

Abreviatura do professor

O campo "Abreviatura" do arquivo de "professores" está relacionado ao campo apelido do cadastro de professores do TOTVS Educacional. Caso o campo do cadastro do professor  estiver vazio ou for maior que o definido no layout, o professor não será informado no arquivo.

Observação: Quando é exportado além dos dados um turno integral para o urânia, o Sistema divide o turno em dois para facilitar a criação dos horários. Assim na hora de importar para o Educacional é necessário selecionar a opção de exportar vários arquivos no sistema urânia para que haja a unificação dos dois horários, e o sistema educacional receba um único arquivo contendo todos os horários do turno integral.
