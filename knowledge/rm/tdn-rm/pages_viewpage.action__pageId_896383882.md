---
content_hash: cac9111794f3cc5fc2d07913539d76c8a62c26ac4d1f6139eceb217533548ce5
fetched_at: '2026-06-29T00:12:01.620229+00:00'
page_id: '896383882'
product: rm
source: tdn-rm
title: 6 – Tipos de testes automatizados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=896383882
version: 5
---

Entender quais tipos de testes automatizados existem é muito importante para definirmos a arquitetura dos testes que iremos criar.

Testes dependentes de base x independentes de base

Testes dependentes de base são automações que utilizam de dados já pré-cadastrados na base para a execução do teste.

* Ex: Automação que realiza a matrícula de um aluno que já está cadastrado na minha base de automação.  
  Este tipo de teste é mais fácil e rápido de ser criado, mas seu teste será dependente desta base onde o mesmo foi criado.

Já os testes independentes não utilizam nenhum dado da base. Cada teste cria e manipula seus próprios dados, o que permite testes mais isolados e independentes, mas serão testes maiores, mais complexos e exige mais tempo de execução.

* Ex: cadastro de uma disciplina nova no módulo Educacional.
Testes dependentes x independentes (Atômicos)

Testes dependentes são automações que dependem de:

- Algum ambiente ou recurso;  
- Outro teste automatizado para conseguir ser executada;  
- Da base de dados

* Ex: Automação que cadastra um aluno e uma outra automação que matricula este mesmo aluno. Automação que depende de algum arquivo no servidor para ser executada.

Já os testes independentes (Atômicos), não dependem de nada para serem executados.

* Ex: Cadastro de um Idioma no módulo Educacional.
Testes individuais

Testes individuais tem o propósito de testar somente uma funcionalidade mínima do sistema.

* Ex: No processo de internação de um paciente, temos várias etapas. A ideia de testes individuais é ter um teste para cada etapa, utilizando dados diferentes, e não utilizando o mesmo para testar o processo inteiro.

Ter testes individuais é uma excelente estratégia pois além de serem rápidos, você consegue testar todas as partes do sistema, visto que seus testes não são dependentes para serem executados, mas aumenta a sua dependência da base de dados.  
Neste caso, podemos restaurar a base de dados para a execução de cada teste automatizado ou restaurar somente uma vez e executar todos os testes.

Testes de Jornada

Testes de Jornadas tem o propósito de testar uma funcionalidade do sistema por inteira.

* Ex: No processo de internação de um paciente, temos várias etapas. A ideia de testes de Jornada é testar com o mesmo dado todas as etapas para conseguir realizar a internação deste paciente.

Ter testes de Jornada é uma excelente estratégia para testarmos um processo do início ao fim utilizando o mesmo dado, mas se encontrar problemas no primeiro passo, os demais passos não serão executados pois são testes dependentes.  
Neste caso, restauramos a base de dados para a execução de cada jornada de teste automatizado ou restauramos somente uma vez e executamos todas as jornadas de testes.

Teste Sistêmico

Teste Sistêmico tem o propósito de testar o sistema por inteiro, podendo utilizar testes individuais e de jornada para atingir este objetivo.  
Ex: No módulo de Saúde, temos vários processos e cadastros. O Teste Sistêmico testa tudo.  
Utilizamos o teste sistêmico quando queremos testar todo o sistema, para garantir que uma nova versão possa entrar para produção.  
Neste caso, restauramos a base de dados somente uma vez para a execução de todos os testes automatizados existentes.

[← Anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=896383866) | [Próximo →](https://tdn.totvs.com/pages/viewpage.action?pageId=896384665)
