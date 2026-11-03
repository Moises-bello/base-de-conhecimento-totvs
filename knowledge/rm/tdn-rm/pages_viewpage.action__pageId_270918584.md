---
content_hash: 2e77ad2decc4ee354770ed35a892868c8186e9e2799b9704a7a280f6e17961f9
fetched_at: '2026-06-29T00:08:25.557589+00:00'
page_id: '270918584'
product: rm
source: tdn-rm
title: RMEDU00004_Numeração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270918584
version: 8
---

# Numeração

|  |  |
| --- | --- |
| **Produto:** | Gestão Educacional |
| **Versão:** | 12.1.14 |
| **Processo:** | Numeração |
| **Data da publicação:** |  |

A rotina de numeração, visa numerar os alunos nas turmas/disciplinas.

Requisitos:

Perfil associado ao usuário, deve ter permissão de acesso ao processo.

Alunos matriculados nas turmas/disciplinas.

Matrícula e avaliação | matrícula | numeração

Selecione o período letivo e as turmas que terão os alunos numerados.

O sistema mostra as turmas/disciplinas e os alunos da mesma.

Ao realizar o processo, é possível parametriza-lo de formas diferentes:

* Pode-se numerar toda a turma, ou atribuir o último número do diário, para o aluno novo;
* A numeração pode ser por: nome (ordem alfabética), número de matricula (RA), por sexo e por nome (homens primeiro) e por sexo e por nome (mulheres primeiro).

No caso, a numeração a ser feita, será por: por sexo e por nome (homens primeiro).

Após finalizado o processo, retornando a mesma tela, é possível verificar que a numeração obedeceu aos critérios marcados.

Currículo e oferta | aluno e professor | alunos

No caso o aluno: ES-000524 Ricardo Muniz Freire Vinha, não foi ordenado corretamente, pois no cadastro de aluno o sexo não havia sido informado. Após cadastrar o aluno corretamente como sexo masculino e refazer o processo, toda a numeração fica como esperado.

O sistema permite a numeração automática dos alunos, ao realizar a matrícula na turma/disciplina, sem a necessidade da realização do processo numeração.

Para tal, basta parametrizar corretamente o sistema.

Configurações | parâmetros | matrícula | geral

O parâmetro: numerar aluno automaticamente, deve estar marcado. Deve-se escolher também qual o tipo de numeração.

Currículo e oferta | oferta | parametrização por curso | guia: configuração de matrícula

Na parametrização por curso, é possível definir uma data limite para a numeração automática. Caso a data de matricula do aluno seja superior a data definida nesse parâmetro e a flag de numeração automática esteja marcada, o aluno é numerado com o ultimo número da turma, independentemente de ordem alfabética, sexo, ou RA.
