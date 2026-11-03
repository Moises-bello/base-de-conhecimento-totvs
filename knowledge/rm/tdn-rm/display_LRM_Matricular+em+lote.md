---
content_hash: 3438005d147499e0e8ecc683e35945b81f7b77eef578f9a1f3c0aebf6718d5c1
fetched_at: '2026-06-29T00:10:35.604095+00:00'
page_id: '531022592'
product: rm
source: tdn-rm
title: Matricular em lote
type: documentation
url: https://tdn.totvs.com/display/LRM/Matricular+em+lote
version: 11
---

Aviso

Este processo está disponível à partir das versões 12.1.25.220, 12.1.26.165 e 12.1.27.105 mediante a um script (CN.2020.01\_03) de ajuste da base de dados.

No processo de matricular em lote o sistema irá listar todas as áreas de interesse vinculadas ao processo seletivo. Neste processo não serão exibidos os alunos, pois como o objeto é realizar a matrícula em lote, o sistema irá buscar em todas as áreas ofertadas selecionadas no processo os candidatos classificados e chamados.

No processo de matrícula, o Totvs Educacional irá aproveitar os documentos entregues no Processo Seletivo, ou seja, documentos marcados como entregue. Ao realizar a matrícula no Totvs Educacional, o sistema irá atualizar a quantidade entregue e a data de entrega será mesma data em que foi realizada a matrícula do candidato através da matrícula no Processo Seletivo RM.

Para que seja feita o aproveitamento dos documentos será necessário:

* Cadastrar o mesmo código do documento no Processo Seletivo e no Educacional;
* No Educacional, na parametrização do Curso (que foi associado na Área Ofertada), o tipo do documento a ser entregue deverá estar marcado como Ingresso;
* No processo Seletivo, no cadastro do Candidato, os documentos associados deverão estar marcados como entregue.

No processo de matricular em lote não serão exibidos os campos "turma", "campus" e "plano de pagamento" pois estes campos são definidos na matriz aplicada e o processo em lote permite a seleção de várias áreas ofertadas de matrizes aplicadas diferentes, estes campos devem ser definidos na parametrização por curso de cada matriz no período letivo que os candidatos serão matriculados.

Na regra de matrícula existem várias validações que podem gerar avisos ou erros dependendo das opções configuradas no perfil do usuário. No último passo do processo o usuário tem como interferir nestas questões, ou seja, se este tem no seu perfil a possibilidade de matricular um aluno inadimplente é possível neste passo permitir ou não este ação. Sempre que o usuário possuir pelo menos uma opção marcada no perfil do usuário para os itens "Matrícula / Rematrícula" e/ou "Biblioteca" uma nova aba será disponibilizada. Esta nova aba conterá todas as opões destes itens, no entanto apenas as opções que no perfil estiverem marcadas estarão habilitadas e permitirão modificação. Desta forma se neste perfil a opção "Matricular alunos inadimplentes" estiver marcada será possível alterar o seu valor antes da execução do processo acima mencionado.

Há uma opção de sobrescrever as informações de deficiência e/ou endereço do aluno dentro do processo. O intuito destes parâmetros é permitir ao usuário a possibilidade de sobrescrever ou não os dados de deficiência e/ou endereço.

Plano de pagamento e bolsa associado ao prospect

Para mais informações referentes à prospecções, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=702373785).

Sobrescrever dados

É possível através dos parâmetros de "Sobrescrever informações do aluno", marcando o grupo de dados que serão sobrescritos, são eles, deficiências, endereço e dados pessoais. 

**Importante**: A opção de Dados pessoas está disponível a partir da versão 12.1.2306 (Junho/2023).

Balanceamento de turma

É possível aplicar o balanceamento de turma marcando a opção "**Realizar enturmação aplicando o balanceamento de turmas**", para maiores informações [clique aqui](https://tdn.totvs.com/display/LRM/Balanceamento+de+Turma)
