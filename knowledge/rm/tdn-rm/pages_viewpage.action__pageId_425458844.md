---
content_hash: c9508b07c75234f095cd51b46f3c17f35aed07cf41e36fe5cb4d72f002bedbed
fetched_at: '2026-06-29T00:09:32.417514+00:00'
page_id: '425458844'
product: rm
source: tdn-rm
title: Transferência Interna entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458844
version: 8
---

O processo de Transferência interna entre coligadas tem como objetivo realizar a transferência dos alunos entre as Coligadas da IE. A funcionalidade está disponível para o Contexto Ensino Básico e Superior.

Antes de executar o processo de transferência interna é preciso que a Instituição cadastre informações nas duas coligadas (Origem e Destino). O cadastro corretos das informações é fundamental para o funcionamento do processo.   
Veja quais informações serão usadas no processo para as duas coligadas 'origem e destino'

* Atividade
* Disciplina
* Modernidade
* Período Letivo
* Situação
* Tipo de Aluno
* Tipo de Ingresso
* Tipo de Ocorrência
* Tipo de Participação

Antes da execução do processo de transferência é preciso realizar o relacionamento "de- para" , isto é, o relacionamento entre os dados da Coligada de Origem e da Coligada de Destino.  
Este relacionamento é realizado no caminho  
***"Currículo e Oferta / Acadêmico / Auxiliares / Relação de Cadastro / Entre Coligadas (Origem e Destino)"***  
Para mais informações [clique aqui](http://tdn.totvs.com/x/nvxbGQ)).  
Após o relacionamento dos dados da Coligada de Origem para a Coligada de Destino, execute o processo de transferência dos alunos.   
***"Atividades Acadêmicas / Transferência Interna / Transferência Interna Entre Coligadas"***  
O processo de transferência entre coligadas é composto por 3 etapas:

* Informar os dados de origem (Coligada de Origem)
  + Nesta etapa informe os dados da matriz de origem do aluno, o motivo da transferência e a situação de matricula após a finalização do processo.
* Informar os dados de destino (Coligada de Destino)
  + Nesta etapa informe os dados da matriz de destino, a situação de matricula no curso após a transferência, e defina os dados vinculados ao aluno que deseja transferir.
* Seleção dos alunos
  + Escolha os alunos que deseja transferir para a coligada e a matriz de destino

Para transferir as disciplinas em curso do aluno basta ativar o parâmetro **Transferir disciplinas em curso**. Com ele habilitado o processo irá tentar matricular todas as disciplinas de origem em uma disciplina correspondente ao destino, que foi parametrizado na relação de cadastro no item de disciplina, ou seja, automaticamente irá procurar a disciplina correspondente bem como uma oferta ativa para matricular, caso não encontre não será realiza a transferência desta disciplina. Vale lembrar que uma disciplina em curso é aquela disciplina que possui em sua situação de matrícula marcado o parâmetro **É uma disciplina em curso**para o nível de ensino superior e para o nível básico o parâmetro **Conta como aluno matriculado na turma** deverá estar marcado.

Por outro lado se informar a turma de destino, o aluno será matriculado em todas as disciplinas da turma informada, neste caso não será levado a relação de cadastro.

Não é possível informar uma turma e marcar o parâmetro **Transferir disciplinas em curso**, o comportamento do sistema é um ou outro ou a turma vazia e o parâmetro desmarcado.

**IMPORTANTE:** Se alguma turma não for informado ou a opção **Transferir disciplinas em curso** estiver desmarcada, o aluno será transferido, porém não será matriculado em uma turma.

**OBS:** O processo de transferências interna entre coligadas realizará apenas transferências de disciplinas em curso, disciplina aprovadas não serão levadas.

Ao finalizar o processo de transferência será criado na coligada de destino um novo RA para o aluno, e todas as informações vinculadas selecionadas durante o processo de transferência   
   
**Parâmetro Verificar  Inadimplência Transferência  Interna**  
Esta funcionalidade permite que um determinado usuário possa realizar a transferência de um aluno entre filiais ou coligadas  mesmo estando inadimplente.  
Para isto é necessário realizar algumas parametrizações*:*  
***Para transferir:***  
Marque o parâmetro "Verificar inadimplência na transferência interna".

* Caminho: Configurações | Parâmetro | Matricula | Movimento 4/4

No parâmetro educacional marque a opção "Bloquear matrícula de inadimplentes".

* Caminho: Configurações | Parâmetro | Matricula | Movimento 1/4

No perfil do usuário logado marcar a opção Matricular alunos inadimplentes.

* Caminho: Serviços Globais |Segurança | Perfis | Usuário do perfil | Anexo| Parâmetros educacionais

A transferência é realizada com sucesso mesmo o aluno sendo inadimplente.  
**Para impedir a transferência:**  
Basta desmarcar o parâmetro: Matricular alunos inadimplentes.  
***OBS.*** Na transferência entre coligadas o processo é o mesmo. Mas para bloquear a transferência é necessário marcar também o parâmetro: Verificar débitos do aluno em outras coligadas, na coligada de destino.
