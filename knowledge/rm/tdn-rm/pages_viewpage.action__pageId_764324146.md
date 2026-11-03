---
content_hash: 1b4fb913c87117cc446fba15105fc37038562dbe328a9b15f66a7fd40cf48165
fetched_at: '2026-06-29T00:11:33.975877+00:00'
page_id: '764324146'
product: rm
source: tdn-rm
title: Padrão Web PDC - Novo (12.1.2310)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=764324146
version: 1
---

1. Introdução Este documento estabelece as regras, diretrizes e melhores práticas a serem seguidas ao desenvolver um projeto web utilizando as tecnologias HTML, CSS, i18n, Angular, TypeScript e PO-ui. Essas orientações visam promover a padronização, legibilidade, manutenibilidade e escalabilidade do código.
2. Recursos

2.1. HTML

* Utilize tags semânticas do HTML5 para fornecer uma estrutura clara e significativa ao documento.
* Evite o uso de estilos inline e dê preferência à separação de estilos no arquivo CSS.
* Faça uso adequado dos atributos, fornecendo descrições relevantes e acessíveis.

2.2. CSS

* Utilize uma metodologia de organização de estilos, como BEM (Block Element Modifier) ou SMACSS (Scalable and Modular Architecture for CSS), para facilitar a manutenção do código.
* Evite a utilização de seletores de estilo muito genéricos, optando por classes específicas e descritivas.
* Comente seu código CSS para melhorar a compreensão e documentação do mesmo.

2.3. i18n

* Utilize bibliotecas ou frameworks de internacionalização (i18n) para tornar seu aplicativo multi-idioma.
* Separe os textos em arquivos de recursos específicos para cada idioma suportado.
* Mantenha um controle rigoroso sobre a tradução de textos, certificando-se de que as palavras e frases estejam corretamente localizadas.

Exemplo: l-comissionpercentage

2.4. Angular

* Siga as diretrizes de estrutura de projeto do Angular, como o uso de módulos, componentes, serviços e roteamento.
* Evite a lógica de negócios complexa nos componentes e delegue-a para serviços separados.
* Utilize a injeção de dependência para garantir a modularidade e a reutilização de código.

2.5. TypeScript

* Declare explicitamente os tipos de variáveis e parâmetros para melhorar a legibilidade e evitar erros.
* Utilize interfaces e tipos personalizados para definir contratos e estruturas de dados complexas.
* Faça uso adequado das características do TypeScript, como tipos union, tipos literais e tipos genéricos, para melhorar a expressividade do código.

2.6. PO-ui

* Siga as convenções e diretrizes da biblioteca PO-ui ao utilizar os componentes fornecidos.
* Utilize as classes CSS fornecidas pela biblioteca para estilizar os componentes e garantir a consistência visual.
* Consulte a documentação da biblioteca para obter informações detalhadas sobre o uso correto dos componentes e recursos disponíveis.

1. Nomenclatura

3.1. Nomenclatura de Métodos

* Utilize verbos no infinitivo para nomear métodos, seguindo o padrão de nomenclatura camelCase.
* Seja claro e descritivo ao nomear métodos, refletindo sua finalidade e ação realizada.

Exemplo: getUsuario(), salvarDados(), atualizarTarefa().

3.2. Nomenclatura de Variáveis

* Utilize nomes de variáveis descritivos e significativos para facilitar a compreensão do código.
* Siga o padrão de nomenclatura camelCase para nomes de variáveis.
* Evite nomes genéricos, optando por nomes que descrevam o propósito ou conteúdo da variável.

Exemplo: nomeCompleto, quantidadeItens, listaUsuarios.

3.3. Declaração dos Tipos de Variáveis

* Declare explicitamente os tipos de variáveis no TypeScript para melhorar a legibilidade e evitar erros.
* Utilize os tipos fornecidos pelo TypeScript, como string, number, boolean, etc., ou crie tipos personalizados quando necessário.
* Evite o uso excessivo de tipos any, preferindo especificar tipos mais precisos.

Exemplo: let nome: string = "John"; let idade: number = 25; let ativo: boolean = true;

1. Consumo de APIs REST

* Utilize os recursos e padrões fornecidos pelo Angular para fazer requisições HTTP às APIs REST.
* Separe a lógica de comunicação com a API em serviços separados, mantendo a responsabilidade única (Single Responsibility Principle).
* Trate os erros de forma adequada, fornecendo feedback ao usuário e registrando os erros para futuras análises.
