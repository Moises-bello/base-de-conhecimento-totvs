---
content_hash: f85b752d106b123d613b99de5b0488a335cb21acc879a1fcdfa264c8be29cfac
fetched_at: '2026-06-29T00:09:33.449487+00:00'
page_id: '425459030'
product: rm
source: tdn-rm
title: Processo para cadastrar ocorrência para os alunos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459030
version: 25
---

Este assistente permite a criação centralizada de ocorrências para múltiplos alunos simultaneamente, otimizando o processo de registro acadêmico. Ao final do processo, o sistema informará o total de novas ocorrências criadas, ressaltando que este assistente não realiza a atualização de registros já existentes.

Filtros e Identificação

Para listar os alunos, você deve definir os critérios de busca. O único campo obrigatório é o **Período Letivo**.

#### Regras de Filtros:

* **Matriz Aplicada vs. Filtro Genérico:** Estes filtros são excludentes. Não é possível utilizar a busca por Matriz Aplicada/Turma simultaneamente com o Filtro Genérico.
* **Hierarquia de Seleção:** Os campos de Turma, Disciplina, Etapa e Professor são interdependentes:

  + Ao selecionar uma **Turma**, o campo **Disciplina** é habilitado.
  + Ao selecionar uma **Disciplina**, os campos **Professor** ou **Etapa** tornam-se disponíveis.
* **Seleção Ampla:** Se nenhum filtro de Matriz ou Genérico for aplicado, o sistema listará todas as turmas vinculadas ao Período Letivo informado.

Seleção de Alunos e Status de Matrícula

A listagem dos alunos pode ser refinada com base em sua situação de matrícula, variando conforme o nível de ensino:

| **Nível de Ensino** | **Parâmetro de Filtro** | **Resultado esperado** |
| --- | --- | --- |
| **Básico** | "Somente aluno(s) com status 'Conta como aluno matriculado na turma'" | Exibe apenas alunos com esta definição no status de matrícula. |
| **Superior** | "Somente aluno(s) com status 'É uma disciplina em curso'" | Exibe apenas alunos cuja situação de matrícula corresponda a esta definição. |

Desconsiderar Turma/Disciplina do aluno

Agora é possível realizar o registro de ocorrências de forma individualizada, desvinculando o processo de uma turma ou disciplina específica.

* **Parâmetro:** `Desconsiderar turma/disciplina do aluno`
* **Comportamento:** Ao marcar este checkbox, o sistema permite que a ocorrência seja gerada diretamente para o registro do aluno, independentemente do vínculo dele com turmas ou disciplinas selecionadas nos filtros anteriores.

Detalhes da Ocorrência e Alunos

Nesta etapa, você define o conteúdo da ocorrência que será aplicado aos alunos selecionados no passo anterior.

### Definição da Ocorrência

* **Grupo e Tipo:** É obrigatório selecionar um **Grupo de Ocorrência** e, em seguida, a **Ocorrência** específica vinculada a esse grupo.
* **Data do Registro:** O campo de data é preenchido automaticamente com a **data atual do servidor**, garantindo a precisão cronológica do registro.

### Anexar Arquivos (Opcional)

O assistente permite a inclusão de documentos comprobatórios ou informativos (atestados, fotos, relatórios, etc.).

* **Replicação Automática:** Ao anexar um arquivo neste processo, o sistema irá **replicá-lo individualmente** para a ficha de cada aluno selecionado.
* **Praticidade:** Não é necessário anexar o mesmo documento várias vezes; o upload único no assistente garante que todos os alunos do lote recebam a documentação em seus respectivos históricos.

> Lembre-se que, uma vez gerada a ocorrência com anexo, o arquivo passará a fazer parte do prontuário individual de cada aluno.

Campos Complementares (Opcional e Condicional)

Se a sua instituição utiliza informações personalizadas para o registro de ocorrências, o sistema adaptará a interface automaticamente.

* **Visibilidade:** A aba **"Campos Complementares"** só será exibida se houver campos previamente configurados e habilitados para o Nível de Ensino correspondente.
* **Conteúdo:** Nesta aba, serão listados todos os campos adicionais (como check-boxes, listas de seleção ou campos de texto livre) definidos pela Secretaria Acadêmica ou TI.
* **Replicação:** Assim como os anexos, as informações preenchidas nestes campos serão aplicadas a **todos os alunos** selecionados no lote.

Observações Internas

As anotações inseridas neste campo servem apenas para **controle administrativo**.

> As informações de observação interna **não são visíveis** para os alunos ou seus responsáveis nos portais e relatórios externos.

Mensagens de Notificação

Para automatizar o aviso aos interessados após a conclusão do registro, o sistema permite o envio de notificações em lote.

* **Configuração de Mensagem:** Para habilitar este recurso, é necessário configurar previamente um modelo de mensagem do tipo **'Cadastro de ocorrência para o aluno'** no menu `Central de comunicação > Mensagens`. **Saiba mais** em
* **Disparo Automático:** Ao finalizar o assistente de cadastro, o processo disparará automaticamente a notificação para todos os destinatários (alunos, responsáveis, etc) vinculados ao modelo de mensagem cadastrado.

 Informações Complementares

---
