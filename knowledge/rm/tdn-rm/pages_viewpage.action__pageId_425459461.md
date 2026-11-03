---
content_hash: 6ebce466b479e502bf7c829d3cb4923f28ba42c7c8bde939db528bc93ec62265
fetched_at: '2026-06-29T00:09:36.037116+00:00'
page_id: '425459461'
product: rm
source: tdn-rm
title: Transferência Interna Entre as Filiais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459461
version: 14
---

A transferência interna permite que alunos matriculados em uma determinada Matriz Aplicada sejam transferidos para outra Matriz Aplicada de outra Filial do mesmo Nível de Ensino.

|  |  |
| --- | --- |
| **Dados de Origem** | **Dados de Destino** |
| Filial = A Matriz Aplicada = A | Filial = A Matriz Aplicada = A |

|  |  |
| --- | --- |
| **Dados de Origem** | **Dados de Destino** |
| Filial = A  Matriz Aplicada = A | Filial = A  Matriz Aplicada = A |

A funcionalidade de transferência interna está disponível para os dois níveis de ensino (Básico e Superior) podendo ser acessada em: ***Atividades Acadêmicas / Transferência Interna / Transferência entre filiais***

**Preenchimento dos dados de origem:**  
A primeira etapa do processo compreende no preenchimento dos dados de origem dos alunos que serão transferidos.

* [Matriz Aplicada](http://tdn.totvs.com/x/dPtbGQ)

**Obs.****.:** Se o aluno estiver matriculado em mais de um curso ele será listado mais de uma vez na seleção.  
Após a seleção de alunos, é possível visualizar e agrupar os dados dos alunos para tomada de decisão baseado nas seguintes informações:

* Registro Acadêmico
* Nome
* Matriz Aplicada
* Situação de Matrícula

**Ensino Básico**  
A transferência somente será realizada se na filial destino possuir uma turma disponível com todas as disciplinas da filial origem.  
Ao selecionar a turma de destino, o sistema realiza a transferência do aluno mesmo que na turma de destino não tenha as disciplinas da turma de origem. Ao final do processo é informado no log as disciplinas que não foram encontradas na turma de destino.  
**Obs..:** O aluno é matriculado nas disciplinas existentes da turma de destino selecionada.

No contexto Básico do TOTVS Educacional a Transferência Interna somente é possível entre Filiais. Não há forma de realizar a transferência interna dos alunos para outro curso dentro da mesma Filial, como ocorre no Contexto Superior. Mudança de Matriz Aplicada no contexto básico é somente a mudança de Turno. Para mudança de Turno será necessário utilizar o processo de Mudança de Turma/Turno presente na matrícula do aluno no período letivo.  
   
**Ensino Superior**  
Ao selecionar o parâmetro "Transferir disciplinas em curso" para cada Turma/Disciplina que o aluno está matriculado na filial origem o sistema busca uma Turma/Disciplina disponível na filial destino. Se não houver Turma/Disciplina disponível é informado no log.  
Ao selecionar a turma de destino, o sistema realiza a transferência do aluno matriculando nas disciplinas existentes da turma de destino selecionada mesmo que na turma de origem exista disciplinas que não se encontram na turma de destino.  
Se o aluno tiver disciplinas em curso na filial origem ao realizar a transferência interna sem marcar o parâmetro "Transferir disciplinas em curso" ou se não for informado a turma de destino, a transferência é realizada criando apenas a matrícula na filial destino.  
Quando a turma de destino não é informada e o parâmetro "Transferir disciplinas em curso" estiver desmarcado, o sistema realiza somente a matrícula do aluno na filial destino.  
É possível que o aluno que tenha matrícula em duas disciplinas, por exemplo, seja matriculado na Matriz Destino em apenas uma disciplina, conforme disponibilidade de turma.  
Seja para Ensino Básico ou Superior, a busca por turmas disponíveis irá obedecer as parametrizações do sistema e as regras pré-definidas:

* Número de vagas
* Conflito de horários
* e etc

Importante

Quando o aluno já estiver matriculado em disciplina no período letivo de destino, o sistema irá atualizar a situação de matrícula desta disciplina.

**Exemplo**

Supondo que um aluno está matriculado no período letivo 2019/1 na filial 2 e na disciplina DISC1\_2 com o status de matriculado, estes são os dados de origem. Entretanto, na filial 1 o aluno possui matrícula no período letivo 2019/1, turma T1 e DISC1\_1, porém com a situação de matrícula de transferido. Na filial 1 existe mais uma turma T2 com a mesma disciplina DISC1\_1. Ao realizar o processo de transferência interna do aluno da filial 2 para filial 1 e informar a turma T2, o sistema irá localizar a DISC1\_1 e irá atualizar a situação de matrícula da mesma para a situação de matrícula selecionada no processo e além disso, o código da turma na matrícula do período letivo será alterada de T1 para T2, mas o aluno terá matrícula na disciplina DISC1\_1 na turma T1, ou seja, ele não irá mudar a turma na matrícula da disciplina.

* Opção: Manter o contrato original e alterar a matriz aplicada para matriz destino\*

Marcada: o contrato original será mantido e somente a matriz aplicada será alterada, desta forma nenhuma ação será aplicada sobre os lançamentos já gerados para as parcelas.  
Desmarcada: será gerado um novo contrato para a matriz aplicada de destino.   
Se a situação de matricula informada no campo "Situação dos alunos no curso após a transferência" estiver parametrizada para cancelar o contrato financeiro, o processo realizará o cancelamento do contrato original e também cancelará todos os lançamentos gerados para a parcela cuja a data de vencimento seja superior a data da realização da transferência.

* Opção: Manter campus/polo da origem

Marcada: O Campus/Polo da matriz aplicada de origem do aluno será migrado para a matriz aplicada de destino do aluno desde que a matriz aplicada de destino tenha esse Campus/Polo vinculado a ela com status ativo

* Opção: Informar campus polo

Marcada: É exibido um lookup de seleção de Campus/Polo ativo vinculado a matriz aplicada de destino do processo de transferência. Ao selecionar essa opção e informar um Campus/Polo ele será associado à matriz aplicada do aluno na filial destino.

Observação:  
Se o sistema estiver parametrizado para "Cancelar Remessa automaticamente ao cancelar o lançamento financeiro quando o boleto estiver com status Remetido ou Registrado", e o boleto do lançamento estiver com o status igual a remetido ou cancelado a remessa será cancelada e será apresentado uma mensagem de alerta no log do processo.

Só será possível concluir o processo de transferência caso o plano de pagamento do curso de origem for disponibilizado para a matriz aplicada do curso de destino.

Está condição somente acontece se marcar o parâmetro que irá aproveitar o contrato trocando a matriz aplicada.

* Parâmetro Verificar Inadimplência Transferência  Interna\*

Esta funcionalidade permite que um determinado usuário possa realizar a transferência de um aluno entre filiais ou coligadas  mesmo estando inadimplente.  
Para isto é necessário realizar algumas parametrizações*:*

***Para transferir:***  
Marque o parâmetro "Verificar inadimplência na transferência interna".

* Caminho: Configurações| Parâmetro| Matricula| Movimento 4/4

No parâmetro educacional marque a opção "Bloquear matrícula de inadimplentes".

* Caminho: Configurações | Parâmetro| Matricula| Movimento 1/4

No perfil do usuário logado marcar a opção Matricular alunos inadimplentes.

* Caminho: Serviços Globais |Segurança| Perfis| Usuário do perfil | Anexo| Parâmetros educacionais

A transferência é realizada com sucesso mesmo o aluno sendo inadimplente.  
***Para impedir a transferência:***  
Basta desmarcar o parâmetro: Matricular alunos inadimplentes.  
***OBS.****.*** Na transferência entre coligadas o processo é o mesmo. Mas para bloquear a transferência é necessário marcar também o parâmetro: Verificar débitos do aluno em outras coligadas, na coligada de destino.

Atenção

A transferência entre filiais realiza a:

* Matrícula do aluno no curso (SHABILITACAOALUNO)
* Matrícula do aluno no período letivo (SMATRICPL)
* Matrícula do aluno nas disciplinas (SMATRICULA)

Quaisquer informações dependentes ou correlacionadas a estas tabelas não são transferidas e devem ser cadastradas manualmente. Por exemplo:

* Notas/Faltas
* Contratos
* e etc

Ao realizar o processo de *Transferência Interna* para alunos que possuírem débitos ou créditos na conta corrente e que optarem por cancelar o contrato antigo (original) e gerar um novo contrato, o sistema atualizará automaticamente a matriz aplicada dos registros da conta corrente dos alunos com a informação da matriz aplicada utilizada como destino neste processo, assim os registros da conta corrente do aluno estarão sempre vinculados a contratos ativos.

Informações Complementares

---

[Cadastro de Curso](http://tdn.totvs.com/x/Af9bGQ)

[Turma/Disciplina](http://tdn.totvs.com/x/C-9bGQ)
