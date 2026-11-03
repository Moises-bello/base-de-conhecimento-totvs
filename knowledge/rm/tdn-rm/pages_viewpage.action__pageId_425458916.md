---
content_hash: 0e34babb0f1943c50b72f0678941ee1d10fe48b5afe6fcd0246ab4c9e796e807
fetched_at: '2026-06-29T00:09:32.771784+00:00'
page_id: '425458916'
product: rm
source: tdn-rm
title: Central de Estágio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458916
version: 28
---

A central de estágio possibilita explorar meios que proporcionam ao aluno formação profissional de qualidade, no âmbito dos estágios curriculares e na relação com o mercado de trabalho. Esta relação se desenvolve no contato direto com as empresas privadas, públicas, organizações sem fins lucrativos e órgão de classes.

Em âmbito institucional assume a função acadêmico-administrativa de orientar e articular as ações propostas pelas Coordenações de Curso e/ou de Estágios, tendo em vista assegurar a qualidade do estágio dos estudantes, respeitando as particularidades de cada curso. Além de realizar o cadastro pelo TOTVS Educacional é possível também efetuar os cadastros básicos da rotina de estágio, (cadastro de empresas, cadastro de funcionários da empresa, cadastro de vagas de estágio oferecidas pela empresa) dentro do Fluig, com as novas interfaces criadas com base no TOTVS HTML Framework.

Antes de iniciar os cadastros configure os parâmetros disponíveis para a funcionalidade. 

Como primeiro passo devemos incluir empresas conveniadas a instituição para a disponibilização das oportunidades de estágio e emprego. Assim acesse .

---

central-estagio-deck0.2Vagafade

### **Vaga**

No cadastro de vagas preenchemos as informações pertinentes a vaga, os requisitos, cargo, departamento, local de trabalho, a carga horária semanal, hora inicial e final do expediente, horário de intervalo, a quantidade de vagas, vagas para deficientes, valor da bolsa, data limite para divulgação, se a vaga é de estágio ou emprego e o status atual: Pendente de aprovação, em aberto ou preenchida.  
Em anexo a vaga associamos o público alvo e definimos qual é o período mínimo para concorrer a vaga.   
O período mínimo não é obrigatório. Ele poderá ser alterado desde que não tenha nenhum candidato associado a vaga. No processo de matrícula do aluno é informado em qual período ele está sendo matriculado, portanto é necessário verificar se o período mínimo da vaga corresponde ao do aluno.  
No portal educacional, há a possibilidade do funcionário da empresa parceira da instituição cadastrar uma nova vaga ou editá-la, essas vagas recebem o status "Pendente de aprovação". Além de associar as mesmas ao público alvo.

0.2Candidatos as Vagasfade

### **Candidatos as Vagas**

O aluno acessa o portal para visualizar as vagas disponíveis. Para que a vaga seja exibida, é importante que o público-alvo definido seja compatível com a habilitação do aluno. O aluno deve estar matriculado em um período letivo da coligada especificada na parametrização das vagas. Além disso, as vagas devem ter status de "aberta" e a data limite de publicação deve estar ativa.

Nos campos exibidos, estarão incluídos o código da vaga, informações da empresa, instituição e filial, dados do aluno, e o status da inscrição.

|  |
| --- |
|  |
| Após clicar em salvar, clique em **Arquivos anexos** no menu Anexos para inserir o currículo do candidato: |
| Caso a empresa e a parametrização da vaga esteja com o e-mail cadastrado, o sistema oferece ao usuário a opção de envio do arquivo para o e-mail cadastrado: |

Solicitação de estagiofade

### **Solicitação de estagio**

O aluno realiza a solicitação de estágio através do portal, no menu "solicitação de estágio". O parâmetro de sistema chamado "Permitir informar empresa/funcionário que não esteja cadastrada para estágio na solicitação?" define se na solicitação de estágio o aluno poderá informar os dados da empresa e funcionário para que seja cadastrado e utilizado em seu estágio. Ou seja, caso este parâmetro esteja desmarcado, o sistema deverá obrigar ao aluno selecionar apenas empresas e funcionários já cadastrados. Caso contrário, deverá permitir ao aluno informar os dados para posterior cadastro do usuário responsável pelo setor de estágio.

A partir da versão: 12.1.2406.186

Para alunos **emancipados**, será possível atribuí-los como responsáveis legais.

A Instituição de ensino poderá cadastrar o aluno (menor de idade), será exibida uma mensagem abaixo indicando que o mesmo é o responsável legal, embora seja menor de idade; ao marcar **'SIM'**, a solicitação de estágio será aprovada e o termo de compromisso gerado normalmente.

Termo de compromissofade

### **Termo de compromisso**

 O termo de compromisso é o contrato firmado entre Instituição, Aluno e Empresa. Além das informações referentes a vaga é necessário informar qual é o código do contrato, data de vigência, o supervisor e o professor responsável.

No cadastro de disciplina é possível informar que determinada disciplina é exclusiva para estágio, caso esse seja o cenário, será possível selecionar a disciplina no termo de compromisso.

No termo de compromisso informamos quais são os objetivos do estágio, motivos para rescisão, responsável legal. Quais são as responsabilidades do Aluno, Instituição e da Empresa.

É possível informar nos anexos: Apólice de seguro, documentos e verificar quais os arquivos anexos ao termo de compromisso.  
No anexo banca do estagio é possível cadastrar além de professores e funcionários da empresa, os servidores como participantes de banca, desde que este ultimo esteja cadastrado com uma pessoa no sistema.

Caso ocorra alguma alteração após a sua assinatura, o status do termo de compromisso deixará de ser **Assinado** e voltará a ser **Pendente de Assinatura.**

Para encerrar um termo de compromisso que possui obrigatoriedade de defesa (campo necessita relatório, na aba características, marcado Com defesa), é necessário que tenha uma banca cadastrada com pelo menos um participante e que o mesmo tenha informado a nota deste aluno.

Quando o termo de compromisso sofrer uma alteração com status **Assinado** poderá ser incluso um motivo para essa operação. A inclusão desse motivo **não é obrigatória**.

Os motivos de alteração de termos de compromissos devem ser cadastrado na tabela dinâmica: ***MOTALTTERM*** *- Motivo de alteração do termo de compromisso*.

Caminho: *Serviços globais | Tabelas dinâmicas | Código: **MOTALTTERM** | Anexos | Item de tabela dinâmica*

O termo de compromisso sempre irá buscar o identificador da parametrização da vaga quando a vaga do termo for informada. Mesmo que a parametrização esteja inativa ou com data fora do período.

Se a vaga não for informada, o sistema irá validar a data e a atividade da parametrização da vaga. Sendo assim, caso a mesma esteja com data fora do período ou inativa, ela não será exibida para seleção.

Horário de expediente e horário de intervalo

O cadastro de termo de compromisso possui uma validação que impede que o horário final de expediente seja menor do que o horário inicial, com o objetivo de evitar erros no cadastro.  
Em situações onde o horário de expediente ocorre uma **Inter jornada**, ou seja, se inicia em um dia e termina o expediente no dia seguinte, o sistema irá considerar todos os horários com o início de expediente após as 18:00h como passíveis desta situação, e o horário final de expediente pode ser informado até as 06:00h, completando 12h.   
  
O horário de intervalo deverá obrigatoriamente estar dentro deste intervalo, podendo também ser informado entre um horário de Inter jornada, porém dentro do limite do horário do expediente.

Exemplo 1- Parametrização de vagas com data de termino fora do período e inativa:

Ao informar a vaga, a parametrização será automaticamente preenchida com a parametrização correspondente da vaga.

Exemplo 2 - Parametrização de vagas com data de termino fora do período e inativa:

Se tentarmos informar a parametrização da vaga sem preenchermos a vaga, o sistema validará a data e o parâmetro, não exibindo a parametrização.

No cadastro de termo de compromisso é possível realizar a geração do relatório (EDUREL0054 - Termo de Compromisso de Estágio) através do botão .

Para  utilizar o relatório, devemos informa-lo nos parâmetros do educacional. Configurações | Parâmetros | 15.06 Estágio | Estágio 4/7.

O relatório utiliza como filtro os campos CODCOLIGADA, RA e IDESTAGIOCONTRATO.

**Choque de horário com turma/disciplina vinculada**

```
Foi adicionado um novo parâmetro para permitir o cadastro sem choque de horário com a disciplina vinculada ao termo de compromisso. O mesmo pode ser encontrado através do caminho: Configurações | Parâmetros | 15.06 - Estágio | Estágio 4/7. Conforme documentação de parametrização.
```

O parâmetro permite que, quando marcado seja possível cadastrar o termo de compromisso sem interferência de choque de horário da turma/disciplina vinculada ao termo.

Quando desmarcado, o sistema validará o choque, não permitindo o cadastro do termo.

A partir da versão: 12.1.2406.186

Para alunos **emancipados**, será possível atribuí-los como responsáveis legais.

A Instituição de ensino poderá cadastrar o aluno (menor de idade), será exibida uma mensagem abaixo indicando que o mesmo é o responsável legal, embora seja menor de idade; ao marcar **'SIM'**, a solicitação de estágio será aprovada e o termo de compromisso gerado normalmente.

Plano de atividadefade

### **Plano de atividade**

O plano de atividade é a última parte do processo de estágio, onde é afirmado as datas de entrega e os objetivos a serem desenvolvidos ao longo do estágio. Essa interação é realizada entre aluno e professor via Portal.  
O plano de atividade é o resumo do que se é esperado no estágio. Vinculado ao plano de atividade, existem etapas que devem ser preenchidas pelos alunos e professores.  
Os status disponíveis nas etapas são: Aprovado, Pendente, Reprovado e Em Aberto. O professor é o responsável por definir qual é o status de cada etapa do plano de atividade.

Avaliação final do alunofade

### **Avaliação final do aluno**

A avaliação final do Aluno é um anexo (Termo Compromisso | Avaliação final do aluno) que permite que o Professor possa visualizar as avaliações finais de estágio cadastradas. Não há limite de avaliações cadastradas por aluno, mas existem regras que se baseiam no status da avaliação existentes.

Caso exista uma Avaliação cadastrada com o status pendente, não será possível cadastrar uma nova avaliação enquanto o status da mesma não for alterado para Aprovado ou Reprovado. Sendo assim necessário Aprovar ou Reprovar a avaliação antes de cadastrar uma nova.

Caso tente cadastrar uma nova avaliação com a situação demonstrada acima , exibirá o seguinte erro.

Em casos de alteração da Avaliação,  uma vez que **aprovada ou reprovada**, não é possível voltar para o status de **Pendente** ou **Em aberto** caso exista alguma outra Avaliação já cadastrada com o status **Pendente**.

Caso tente cadastrar uma avaliação com a situação demonstrada acima , exibirá o seguinte **erro**.

 Informações Complementares

---

[Processo de Inscrição](http://tdn.totvs.com/pages/viewpage.action?pageId=425458503)
