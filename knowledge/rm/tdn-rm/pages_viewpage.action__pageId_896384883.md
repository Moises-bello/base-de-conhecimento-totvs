---
content_hash: 5d6cd629ec4e08a382ed67a93fb30af31b41eab4d3f5768b54ff3f3f1280079a
fetched_at: '2026-06-29T00:12:01.625572+00:00'
page_id: '896384883'
product: rm
source: tdn-rm
title: 8 – Escolhendo a arquitetura dos testes automatizados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=896384883
version: 4
---

A escolha da arquitetura dos testes automatizados é crucial para a escalabilidade e a facilidade de manutenção dos testes e depende de fatores como os tipos de testes, a base de automação e os objetivos do projeto.

Agora que já entendemos alguns conceitos de tipos de testes e também sabemos como a base de dados se comporta quando executamos testes automatizados no **TOTVS Automação de Testes,**vamos falar sobre a escolha da **Arquitetura dos Testes**.

1. Definição da Base de Dados

O primeiro passo é a definição de como será o comportamento da base de dados de Automação e temos que responder as seguintes perguntas.

* Utilizaremos a base de produção para se tornar a base de Automação?
* Qual é o tamanho da sua base do RM de produção?
* Será necessário realizar uma limpeza na base de Automação para reduzir o seu tamanho?
* A base de automação será fixa ou a substituiremos de tempos em tempos? Com a resposta desta pergunta, teremos que responder também qual tipo de teste criaremos, testes dependentes ou independentes de base de dados?  
  Se a escolha for base fixa, podemos criar testes dependentes da base de dados, caso contrário, teremos que criar testes independentes da base de dados.
* A base de automação será restaurada para cada teste individual, para cada jornada ou somente uma vez na execução de todos os testes automatizados?
2. Definição do Tipo de Teste

O segundo passo é a definição de qual tipo de teste iremos criar. Individuais, Jornada ou Sistêmico. Se serão testes dependentes ou independentes de base.

Cada escolha tem as suas vantagens e desvantagens e é necessário colocar na balança o que melhor se encaixa para a sua empresa e a forma como você executa os testes.  
(Clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=896383882) para saber mais sobre os tipos de teste)

## 8.1 - Modelo Sugerido

O modelo que sugerimos, é a adoção de uma **Base Fixa de Automação**, criação de testes dependentes quando o custo de se fazer tudo do zero for alto e testes independentes quando for possível.  
Se não utilizarmos uma base fixa de automação, ou seja, se alterarmos a base de dados em que as automações rodam, podem ocorrer divergências de dados que resultarão em manutenções nos projetos de testes.

* Sempre que possível, crie testes individuais que sejam independentes de: bases, outros testes ou ambientes. Desta forma, ele poderá ser executado em qualquer lugar, será mais rápido para ser executado, mais fácil de cria-lo e também será mais fácil dar manutenções quando necessário.
* Para processos que dependem de uma grande massa de dados, crie testes que são dependentes da base de dados. Isso facilitará a construção das automações tendo os cenários já preparados para serem utilizados e não será necessário cadastrar tudo do zero. Neste caso, tem a necessidade de se adotar uma base fixa de automação para evitar manutenções.

[← Anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=896384665) | [Próximo →](https://tdn.totvs.com/pages/viewpage.action?pageId=896386855)
