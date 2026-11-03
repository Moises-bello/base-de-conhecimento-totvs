---
content_hash: b84d73362530c4b6ce9038859b2081481d77380bf53c6bc44e171fa9c59d0c0f
fetched_at: '2026-06-29T00:09:32.570355+00:00'
page_id: '425458876'
product: rm
source: tdn-rm
title: Rematrícula no Ensino Básico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458876
version: 34
---

O processo de rematrícula permite que os alunos sejam rematriculados no período letivo seguinte ao que estão cursando.

Esse processo está disponível em ***Matrícula e Avaliação | Matrícula | Rematrícula***

### **Procedimento para fazer a matricula no período letivo durante a**rematrícula

* Acesse Matrícula e Avaliação | Matricula | Rematrícula; Selecione Período letivo, Situação de matricula; Seleção de aluno por R.A ou Seleção de alunos por curso ou Seleção de aluno por consulta SQL;
* Adicione os alunos e avance;
* Selecione os alunos que serão rematriculados; Escolha a "Situação de matricula" e "Tipo de matricula"; Avance e execute.

Importante: Os lançamentos podem ser gerador em lote ou individualmente. Seguindo as mesmas primícias do processo de Geração de lançamento feito no durante a matricula feita via portal ou sistema. Esse processo visa calcular o salário do professor por meio de todas as atividades executadas pelo mesmo, dentro da instituição de ensino.

### **Procedimento para fazer a matricula nas disciplinas durante a**rematrícula

* Acesse Matrícula e Avaliação / Matricula / Rematrícula; Avance e selecione: Período letivo, Situação de matrícula, Seleção de aluno por R.A ou Seleção de alunos por curso ou Seleção de aluno por consulta SQL;
* Adicione os Alunos e avance; Selecione os alunos que serão rematriculados;
* Selecione: "Situação de matricula" e "Tipo de matricula";
* Marque o parâmetro "Cadastrar disciplinas automaticamente"; Avançar; Executar.

### **Procedimento para associação de contrato no processo de**rematrícula

* Acesse Matrícula e Avaliação / Matricula / Rematrícula; Avance e selecione: Período letivo, Situação de matrícula, Seleção de aluno por R.A ou Seleção de alunos por curso ou Seleção de aluno por consulta SQL;
* Adicione os Alunos e avance;
* Selecione os alunos que serão rematriculados;
* Selecione "Situação de matricula" e "Tipo de matrícula";
* Marque parâmetro "Cadastrar contrato financeiro"; Avance e execute.

A partir da versão 12.1.29 a visualização do alunos foi alterada para permitir que os alunos selecionados mediante filtro, possam ser removidos antes da execução do processo.

Ao alterar algum filtro, a lista de alunos a serem removidos da matrícula é apagada, o usuário deverá selecioná-los novamente.

Ao finalizar o processo uma mensagem é exibida para confirmar que os alunos retirados não farão parte da rematrícula, caso confirme, o processo é executado.

***Observação:***Caso o filtro Multi Contexto estiver marcado, não será permitido selecionar os alunos na tela de pré-visualização.

***Observação 2:****Para selecionar um Plano de pagamento na rematrícula é necessário que um curso seja preenchido no **Filtro por Período Letivo / Matriz Aplicada.***

### Lista de situações de matrícula

Serão listadas na grid de situação de matrícula, todas pertencente ao contexto logado e que estejam habilitadas no período letivo.

| Situação de matrícula habilitada no período letivo |
| --- |
|  |

### Filtros de seleção de alunos

##### Filtro Genérico

Permite executar um filtro conforme a visão de matrículas de alunos. Filtro **permitido** quando a opção de multi contexto estiver habilitada.

##### Filtro por Período Letivo / Matriz Aplicada

Permite filtrar utilizando o período letivo informando juntamente com a matriz aplicada. Filtro **não permitido** quando a opção de multi contexto estiver habilitada.

##### Consulta SQL

Permite a utilização de uma consulta SQL obedecendo as informações mínimas para filtrar os alunos. Filtro **não** **permitido** quando a opção de multi contexto estiver habilitada.

É necessário selecionar os campos CODCOLIGADA, RA da tabela SALUNO, IDHABILITACAOFILIAL da tabela SMATRICPL e NOME da tabela PPESSOA. Opcionalmente poderá selecionar o campo CODTURMA da tabela SMATRICPL, entretanto se não informar este campo as opções de rematricular na mesma e/ou próxima turma não irão funcionar corretamente.

### **Competência contábil: inicial e final**

Se o sistema estiver parametrizado para "Utilizar contabilização por competência", a data contábil de competência estiver parametrizada para "Data contábil do contrato e plano de pagamento" (Parâmetros > Integrações > Contabilidade -> Data contábil), opção de cadastrar contrato marcada e o usuário tiver permissão de perfil Educacional -> Financeiro / Contábil -> Contratos -> Contratos -> Permite alteração de data contábil do contrato marcada, o sistema exibirá os campos de competência inicial e competência final que conterão os valores a serem preenchidos nos contratos que serão gerados  
Se um dos campos for preenchido, o outro será obrigatório.  
Preenchendo ambos os campos, o sistema considerará o período de competência informado no processo para todos os contratos a serem gerados.   
Caso não seja informado nenhum valor para os campos de competência, o sistema buscará os valores preenchidos no plano de pagamento utilizado como modelo para a criação das parcelas do contrato.

### **Rematrícula no próximo itinerário formativo (Novo Ensino Médio)**

Foi incluído no novo processo de rematrícula o parâmetro **Rematricular no próximo itinerário formativo** que, ao ser marcado, fará com que o processo matricule o aluno no [itinerário formativo](https://tdn.totvs.com/x/gjmeI) configurado no campo **Próximo Itinerário Formativo**, existente no [itinerário formativo](https://tdn.totvs.com/x/gjmeI) que está sendo cursado pelo aluno no período letivo atual.

Durante a execução do processo serão feitas validações referente a [matrícula no itinerário formativo](https://tdn.totvs.com/x/4vtbGQ), caso ocorra algum problemas nessas validações, todo o processo de rematrícula do aluno será cancelado, ou seja, não será feita a rematrícula no próximo período letivo e nem no próximo itinerário formativo.

Rematrícula nas disciplinas do itinerário formativo

Além de realizar a matrícula nos itinerários formativos do próximo período letivo, quando o sistema estiver configurado para isso conforme explicado anteriormente, o processo de rematrícula irá realizar também a matrícula nas disciplinas ofertadas dos itinerários formativos. Para que isso ocorra as seguintes regras devem ser seguidas:

* Marcar o parâmetro **Rematricular no próximo itinerário formativo**
* Marcar o parâmetro **Rematricular na próxima turma** (a próxima turma deve ser válida e configurada no campo apropriado no cadastro da turma do período letivo atual)

O processo de rematrícula irá matricular o aluno primeiramente em todas as disciplinas obrigatórias do itinerário, **dando preferência para a turma do aluno**, depois, o aluno será matriculado nas disciplinas opcionais buscando atingir o valor (ou mais próximo dele possível), da carga horária máxima das disciplinas para o itinerário (quando o controle de matrícula no itinerário for por carga horária) ou do número máximo de disciplinas exigidas no itinerário (quando o controle de matrícula no itinerário for por número de disciplinas).

Importante

Se durante o processo de rematrícula alguma validação referente a matrícula em todas as disciplinas obrigatórias, carga horária mínima/máxima ou ao número mínimo/máximo de disciplinas configuradas no itinerário formativo não for executada com sucesso, não será realizada matrícula em nenhum das disciplinas desse itinerário formativo, porém, a matrícula no itinerário formativo será feita normalmente.

Plano de pagamento e bolsa associado ao prospect

Para mais informações referentes à prospecções, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=702373785).

Informações Complementares

---

**[Novo Ensino Médio](https://tdn.totvs.com/x/C3R9IQ)**

* [Itinerário Formativo](https://tdn.totvs.com/x/gjmeI)
* [Competências e habilidades](https://tdn.totvs.com/x/8RVxIQ)
* [Itinerário Formativo da Matriz Curricular](https://tdn.totvs.com/x/ThVxIQ)
* [Estrutura Curricular](https://tdn.totvs.com/x/zf1bGQ)
* [Turma/Disciplina do Itinerário Formativo](https://tdn.totvs.com/x/jBVxIQ)
* [Parametrização por Curso](https://tdn.totvs.com/x/x-xbGQ)
* [Disponibilidade do Itinerário Formativo](https://tdn.totvs.com/x/VQx9IQ)
* [Matricular Aluno](https://tdn.totvs.com/x/4vtbGQ)
* [Registro de avaliação por habilidades](https://tdn.totvs.com/x/Ygp9IQ)
