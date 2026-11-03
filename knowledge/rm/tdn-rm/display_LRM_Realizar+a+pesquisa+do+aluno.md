---
content_hash: 5038ed18eece5ee285318b44c696532e2429b3f33d1edcdd823d900a349d90f2
fetched_at: '2026-06-29T00:11:16.227666+00:00'
page_id: '665266334'
product: rm
source: tdn-rm
title: Realizar a pesquisa do aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/Realizar+a+pesquisa+do+aluno
version: 18
---

Ao acessar "Painel do aluno" no menu lateral, será exibida caixa de pesquisa para a localização do aluno. A pesquisa pode ser realizada pelo RA, nome do aluno ou partes do nome do aluno, tais como sobrenomes ou mesmo as primeiras letras do nome, com o mínimo de três letras. A pesquisa só acontece após o terceiro caractere digitado.

Ao iniciar a digitação, a pesquisa retorna até 10 registros. Caso nenhum registro corresponda aos caracteres digitados, a seguinte mensagem será apresentada:

Para facilitar a identificação dos alunos são apresentados os seguintes dados referentes aos resultados encontrados: Unidade, Curso, Período (quando o aluno for do ensino superior), Série (quando o aluno for do ensino básico ) , Tuma e Período Letivo.

Ao clicar na lupa ou pressionar ENTER, uma segunda tela é apresentada com a opção de até 20 registros por página, permitindo a navegação entre as páginas através dos botões "Anterior" e "Próximo", caso existam mais alunos que correspondam ao critério de pesquisa.

Caso nenhum registro corresponda à pesquisa, a segunda tela terá a seguinte apresentação:

Ao selecionar o aluno, será exibido um CARD com seus dados principais, e ao clicar nesse CARD, o usuário será redirecionado para o Painel do aluno, onde terá acesso a toda vida acadêmica desse estudante.

Importante

Para alunos do ensino básico, o sistema apresentará a matrícula mais recente do último período letivo do aluno, que possua o parâmetro "Aluno ativo" marcado, da aba "Status no período letivo", dentro da situação de matrícula.

Já para os alunos do ensino superior o portal mostrará a matrícula mais recente de cada curso.

## 

Ao clicar no CARD, o Painel do aluno é apresentado, conforme abaixo:

As informações apresentadas são de acordo com o período letivo selecionado, caso queria selecionar outro curso ou período letivo, basta escolher no combo de alteração de contexto.

Caso o aluno tenha nome social inserido em seu cadastro, a busca por nome terá prioridade ao campo nome social:

# **Restrição de acesso por Polo**

A partir da versão 12.1.2402, os resultados da pesquisa de alunos para o contexto de **Ensino Superior** serão restringidos pelo Campus/Polo associado ao curso/habilitação do aluno que correspondam ao(s) campus/polo a que o usuário logado no portal está associado no contexto Educacional da matriz do aluno.

Caso o usuário não esteja associado a nenhum campus/polo para um determinado contexto Educacional, ele conseguirá visualizar todos os alunos desse contexto no resultado da pesquisa de aluno no painel do Aluno.

* **A configuração do Campus/Polo do aluno é feita no registro de Curso/Habilitação do aluno:**

* **A configuração dos Campus/Polo do usuário é feita no módulo de Globais | Segurança | Usuários (Sistema: Educacional - Educacional) | Anexo Usuário/Filial:**

## **Pesquisa simples**

Ao realizar a pesquisa por aluno, o portal exibirá somente os alunos cujos Campus/Polo correspondem ao(s) Campus/Polo a que o usuário logado está relacionado para aquele contexto Educacional da matriz do aluno, ou exibirá todos os alunos de um determinado contexto, independente do Campus/Polo do aluno, caso o usuário não esteja associado a nenhum Campus/Polo para o contexto Educacional em questão:

## **Pesquisa avançada**

Na pesquisa avançada será habilitado o campo de filtro por Campus/Polo quando se tratar de nível de ensino Ensino Superior para permitir filtrar os alunos por Campus/Polo:

Se o usuário estiver associado e algum Campus/Polo no contexto que está sendo filtrado (coligada, filial, nível de ensino), no dropdown do Campus/Polo somente serão exibidos estes aos quais o usuário logado está associado.

Caso nenhum Campus/Polo esteja associado para o usuário logado no contexto que está sendo filtrado, no dropdown do Campus/Polo serão exibidos todos os Campus/Polo cadastrados no sistema.
