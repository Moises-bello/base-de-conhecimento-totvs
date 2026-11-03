---
content_hash: 1fb2bfb70bb17e41823441c4d0d685c482cf13b8c09c94b3ad215154ecddc443
fetched_at: '2026-06-29T00:08:31.826285+00:00'
page_id: '273312406'
product: rm
source: tdn-rm
title: RMEDU00003_Relatório utilizando provedor de dados "Analise Curricular"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273312406
version: 8
---

# Exemplo de um relatório

# 

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional |
| **Versões:** | Todas as versões de mercado |
| **Observações:** | Utilização do Provider "Analise Curricular" |

A vida acadêmica do Aluno é atualizada sempre que acessarmos o cadastro do aluno / cursos Habilitações editarmos o curso desejado e clicarmos no ícone "Analise Curricular", assim o sistema faz todas as validações necessárias no currículo do aluno calculando disciplinas pendentes, concluídas, atividades acadêmicas pendentes concluídas e etc.

Agora imagem uma instituição tendo a necessidade de imprimir os históricos ou certificados de conclusão de todos os alunos, onde seu relatório é baseado nas tabelas que compõe a Analise Curricular.

Exemplo de algumas tas tabelas:  
SHISTALUNOCOL  
SHISTATVIDADEALUNO  
SHISTDISCAPROVESTUDOSORIGEM  
SHISTDISCEQUIVCONCLUIDAS  
SHISTDISCEQUIVEMCURSO  
SHISTDISCFAC  
SHISTDISCPENDENTES

Estas e outras tabelas da mesma família são atualizadas somente quando acessamos o sistema e clicamos no Ícone "Analise Curricular", agora imagine o tempo necessário para acessar aluno por aluno e clicar no ícone?  
Para facilitar a atualização das tabelas sem que ter fazer manualmente aluno por aluno é possível utilizar um provedor de dados em um relatório para atualização dos dados em massa conforme mostrado abaixo.

1º Criação do Relatório

Criar o relatório conforme especificações abaixo.

2º Criação de uma SQL para utilização no relatório

A execução do Provider é garantida por parâmetros este parâmetros pode ser passados de inúmeras formas, no exemplo abaixo vamos demostrar utilizando uma consulta SQL, o que também pode ser feito através de tabelas que retornem os campos solicitados pelo provider "CODCOLIGADA, IDHABILITACAOFILIAL, RA e RA"

Ok, a repetição do campo RA se faz necessário para passagem de parâmetros o que demonstraremos futuramente, paciência.

Criamos uma consulta SQL muito simples para demostração da funcionalidade.

O retorno = :CODCURSO foi proposital pois criaremos um parâmetro no relatório onde o usuário poderá informar o codigo do curso desejado, assim a atualização dos dados podem ser realizada curso a curso.

Execução da consulta, informado o código "7-1" do curso desejado

Retorno da consulta, neste cados relacionamos todos os alunos do cursos 7-1, cada instituição pode refinar a consulta conforme sua necessidade, lembrando que os campos CODCOLIGADA, IDHABILITACAOFILIAL, RA são obrigatórios.

3º Inserir a Consulta SQL no Detalhe 1 do relatório.

Editar o relatório -> Clicar na opção "Adicionar Fonte de Dados" - > Sentença SQL "Localizar a consulta criada" selecionar , clicar em Adicionar e OK.

Consulta SQL adicionada ao Relatórios

A consulta SQL deve ser a tabela Master do Relatório

4º Levar para o relatório os campos para vinculação com os parâmetros do Provider

Lembra que informamos acima que o campa RA deveria ser inserido duas vezes, veja como será feito.

Clicar nos campos e arrastar, o campo RA deve ser arrastado duas vezes para o Detalhe 1

5º Criação do Subdetalhe do relatório

6º Inserir Provider no SubDetalhe do relatório

 Clicar na opção "Adicionar Fonte de Dados" - > Provedor de Dados "Localizar o provedor "Analise Curricular" selecionar , clicar em Adicionar e OK.

O Provider precisa ser a tabela master do SubDetalhe

Apos garantir o Provider como tabela master é extremamente importante vincular os campos retornados no Detalhe 1 com os parâmetros para execução do provedor, agora vamos ver o motivo de haver 2 campos RA retornados no Detalhe 1.

1 - Clicar no Detalhe do SubDetalhe do Relatório

2 - Clicar na Grade de Propriedades

3 - Clicar nos Parâmetros

4 - Clicar nos Parâmetros do Provider

5 - Vincular os campos retornados no Grupo de Detalhe 1 com os parametros do Provider "Veja que exitem RA1 e RA2 por este motivo foi inserido 2 vezes o RA no detalhe 1"

Arraste alguns campos do provedor para o SubDetalhe assim garantiremos que o mesmo foi executado.

7º Criação de Parâmetro no Relatório

Como nossa consulta SQL foi criada com a condição CODCURSO= :CODCURSO criamos um parâmetro para que o usuário possa informar o código do curso na execução do relatório, não precisa ser necessariamente o código do curso mas o mesmo precisa ter o mesmo valor da condição informada na consulta SQL.

1 - Lista de Campos

2 - Parâmetros

3 - Botão direito do Mouse

4 - Adicionar Parâmetro

1 - Parâmetros

2 - Grade de Propriedades

1 - No campo Descrição informar o valor do campo para a consulta SQL

2 - No campo Design "Descrição" informar o campo do parâmetro da consulta SQL

Salvar o relatório

8º Teste de Execução

Selecionar o relatório

Gerar o Relatório

 Avançar o processo.

false

*Para atualizar informações do seu provedor de dados acesse o design do relatório, vá em "Adicionar Fonte de Dados", selecione a guia “Provedor de Dados”, pesquise pelo provedor utilizado no relatório, selecione o registro e clique no botão “Adicionar/Atualizar” para que as informações sejam atualizadas. Mais informações acesse: [Provedor de Dados](https://tdn.totvs.com/x/X_kPHw)**.*
