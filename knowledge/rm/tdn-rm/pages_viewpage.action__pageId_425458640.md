---
content_hash: 6afe75dd2fec80fd06bfc88fa0c71eadfe0c0526ca3544dd4d438d8cf37fc3a9
fetched_at: '2026-06-29T00:09:31.339108+00:00'
page_id: '425458640'
product: rm
source: tdn-rm
title: Ocorrência de alunos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458640
version: 11
---

Antes de efetuar a matrícula de um aluno em um período letivo, são feitas algumas consistências, inclusive se o aluno possuir registro de ocorrências:

O sistema verificará a configuração do tipo da ocorrência. O tipo de verificação pode ser de uma das seguintes maneiras:  
**Não verificar:** o sistema ignora a ocorrência do aluno.  
**Alertar:** o sistema alerta o usuário sobre as ocorrências do aluno, mas não impede a matrícula.  
**Bloquear:** o sistema alerta o usuário sobre as ocorrências do aluno e impede a continuação da matrícula.

Caso o perfil do usuário possua permissão para matricular alunos com ocorrências que impedem a matrícula, o sistema pedirá uma confirmação do usuário e permitirá a continuação do processo.

O sistema deve verificar ocorrências do período letivo atual e do próximo.

No cadastro de ocorrência para o aluno, o sistema permite que seja inserido arquivo nas ocorrências, nos parâmetros, portal, Geral 3/3, podemos definir o tamanho dos arquivos que podem ser anexados.

**Professor:** Quando for informada a turma/disciplina, o campo para informar o professor será carregado automaticamente, de acordo com as seguintes condições:

* Se houver somente um professor na turma/disciplina, ele será informado como padrão;
* Se houver mais de um professor, o professor titular será informado como padrão;
* Se houver mais de um professor sem algum titular será selecionado um deles e caso não seja o correto, basta escolher manualmente.

### Alterar ou excluir uma ocorrência com aceite do responsável feito pelo portal

Á partir da versão 12.1.29, uma ocorrência do aluno não poderá ser alterada nem excluída quando possuir o aceite do responsável feito através do portal.

A alteração ou exclusão só poderá ser feita quando o usuário do TOTVS Educacional possuir um perfil que a permissão especial "Permitir alterar ou excluir ocorrências que possuam aceite do responsável" estiver marcada nos parâmetros educacionais do perfil educacional do usuário.

Caso possua permissão e ocorra uma alteração em uma ocorrência com aceite, o sistema irá alertar e pedirá uma confirmação que a alteração irá invalidar o aceite do responsável, assim o responsável deverá novamente aceitar a ocorrência pelo portal.

### Arquivos da ocorrência

O único parâmetro do sistema que é avaliado durante a inclusão de um novo arquivo é o parâmetro "Tamanho máximo dos arquivos das ocorrências do aluno (KB)", disponível "Parametrizador Educacional > Secretaria > Geral 1/7".

Todos os arquivos vinculados a uma ocorrência são armazenados exclusivamente na base de dados, tabela "SOCORRENCIAALUNOARQ".
