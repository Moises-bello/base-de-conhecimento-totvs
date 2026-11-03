---
content_hash: 412fc03bd3e7d0f0e0c2d9115201664ddd3f8b593c9ab3abb7d875c464296108
fetched_at: '2026-06-29T00:11:56.394654+00:00'
page_id: '865412460'
product: rm
source: tdn-rm
title: 2.2 - Agrupadores
type: documentation
url: https://tdn.totvs.com/display/LRM/2.2+-+Agrupadores
version: 14
---

# O que é?

Os agrupadores, também conhecidos como Coleções de Atividades, são utilizados para reunir várias atividades em uma única atividade.

# Para que serve?

Esta Atividade serve para agrupar outras Atividades ou Projetos que precisem ser executados em conjunto, mas que não podem ou não devem estar contidos dentro de um único Projeto. Vale ressaltar que Coleções de Atividades não devem ser confundidas com Projetos. É ideal executar as coleções quando as atividades contidas nelas são independentes e não necessitam de recursos de outras atividades.

# Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro

 1. Navegue no menu do TOTVS Automação de Testes e clique em: **Atividades** → **Agrupadores** → **Coleção de Atividades.**

 2. Na tabela que será mostrada, clique no botão verde em destaque.

2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição

Fornece uma descrição detalhada da atividade, explicando seu propósito e operações, facilitando a compreensão e manutenção futura.

Adicionar Atividades

Utilize esse campo para adicionar as atividades à sua coleção. A ordem em que as atividades são colocadas está diretamente relacionada a ordem em que as atividades serão executadas.

Para adicionar qualquer atividade, ela deve ter sido criada anteriormente.

É possível reordenar as atividades e removê-las, como é demonstrado abaixo.

Exemplo prático

Para ilustrar o cenário, imagine que sua equipe é responsável por atender diversos clientes, cada um com sua própria base de dados. Dada a complexidade e o volume de clientes, você recebeu a responsabilidade de restaurar as bases de dados desses clientes no servidor de banco de dados utilizado pela equipe.

Para otimizar esse processo e garantir que as restaurações ocorram de maneira ágil e eficiente, é possível configurar uma atividade de coleção. Esta atividade de coleção deve incluir todas as atividades dedicadas à restauração da base de dados de cada cliente específico. Desta forma, o processo de restauração será conduzido de forma automatizada e rápida.

# Saiba mais

Ao configurar uma Coleção de Atividades, certifique-se de definir claramente o propósito de cada atividade incluída e considerar as suas dependências.

Antes de adicionar atividades a uma Coleção, é essencial garantir que elas possam ser executadas de forma independente. Caso contrário, considere organizá-las em um Projeto onde a sequência de execução possa ser controlada.

# FAQ

**P: Quais tipos de atividades eu posso incluir na minha coleção?**

R: É possível incluir qualquer tipo de atividade em uma Coleção, inclusive Projetos de Testes.

**P: O que devo considerar ao adicionar Atividades a uma Coleção?**  
R: Ao adicionar Atividades a uma Coleção, é importante observar as particularidades de cada Atividade. Certifique-se de que não há dependências críticas entre as Atividades, como por exemplo, atividades que dependem de recursos das demais. Esses recursos não são providos nas atividades de coleção.
