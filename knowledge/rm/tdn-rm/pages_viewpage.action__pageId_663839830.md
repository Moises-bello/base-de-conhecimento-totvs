---
content_hash: 14234efa5801e05f09c70d8aac27c0017697253f5a6061bfc7093599864ada43
fetched_at: '2026-06-29T00:11:16.190278+00:00'
page_id: '663839830'
product: rm
source: tdn-rm
title: Gerenciamento de Memória
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=663839830
version: 1
---

# Indice

---

# Introdução

---

O RM trabalha em cima da plataforma .NET, de autoria da Microsoft, e utiliza dessa plataforma para realizar as comunicações entre aplicação e Sistema Operacional. Dessa forma, a manipulação de recursos fica por conta do .NET, eximindo o RM da responsabilidade de manipular o uso da memória por exemplo.

Esta documentação explicará como é realizada a alocação e liberação de memória, considerando as documentações próprias da Microsoft acerca de como o .NET manipula a memória alocada às aplicações, mas adaptando-as ao contexto do RM.

# O Garbage Collector

---

Primeiramente, é necessário entender que o gerenciamento da memória da aplicação é feito pelo próprio .NET e não há interferência do RM neste processo. Para realizar a limpeza e realocação de memória, o .NET utiliza do chamado **Garbage Collector (GC)**, para limpar a memória destes objetos não mais utilizados (*Como as informações presentes em uma visão recém-fechada dentro do RM*).

O **GC** rodará quando a memória alocada pela aplicação estiver cheia ou quando a quantidade de objetos alocados na memória ultrapasse um limite considerado aceitável, limite esse definido pelo próprio GC. Como o processo de *Garbage Collection* possui um custo de performance, quanto maior a quantidade de objetos alocados na memória, maior o trabalho que ele terá para limpá-la.

Exemplificando, ao abrir uma visão dentro do RM, como por exemplo a de ***Usuários** (Serviços Globais)*, uma quantidade de dados é retornada e esta, por se tratar de dados que podem se manter por muito tempo utilizados, são alocados em uma área da memória própria para objetos longínquos (Que não devem ser descartados rapidamente, por serem necessários em outras diretivas de uso), a chamada ***Geração 2*** [¹](https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals#generations) (*A alocação de memória do **.NET** trabalha com **Gerações** para definir quais os dados que podem ser limpos mais rapidamente, sendo 0 as informações mais temporárias, 1 as que ficam por um pouco mais de tempo e 2 as informações quer perduram por mais tempo sendo utilizadas*). Por se tratar de objetos que devem ser mantidos na memória por mais tempo, essa área da memória leva mais tempo para sofrer interferência do Garbage Collector e por isso, demora mais para ser liberada, ocasionando, caso a visão retorne uma quantidade alta de registros, no alto consumo de memória da aplicação, o que pode passar a impressão de haver um vazamento de memória.

Não é possível prever quando o GC irá rodar, e dessa forma, apenas é possível observar que, com o tempo, após o término de um processo ou fechamento de uma aba de visão, a aplicação irá liberar a memória que foi alocada para exibir a visão ou realizar o processo por exemplo, porém *esta tratativa é realizada diretamente pelo **.NET** ao **S.O***.

# Analisando algumas execuções

---

|  |  |  |
| --- | --- | --- |
| Quantidade alocada (Em MB) | Quantidade liberada (MB) | Quantidade de registros retornados nas tabelas de Visão |
| 247.7 MB | 89.86 MB | 15360 |
| 295.3 MB | 44.13 MB | 49280 |
| 464.44 MB | 557.45 | 62976 |

Acima está uma análise feita com base nos em alguns **DUMP’s** [²](https://pt.wikipedia.org/wiki/Despejo_de_mem%C3%B3ria) de execuções do RM, onde foram abertas e fechadas diversas visões retornando diversos registros, simulando um uso padrão do sistema. Pode se notar que um padrão se repete em relação aos **DUMP’s**; *a quantidade de memória alocada para a aplicação em relação à quantidade de registros retornados nas tabelas de Visão*.

O que ocorre é que, ao realizar a abertura de uma visão utilizando filtros que buscam muitos registros do banco de dados, esses dados necessitam de ser alocados na memória da aplicação para serem manipulados corretamente pelo usuário, sendo este o comportamento padrão da aplicação.

Pode ser notado que, ao fechar as visões que foram abertas, a aplicação não libera a memória previamente alocada imediatamente, o que poderia ser aparentar ser um vazamento de memória (*Memory Leak*)[³](https://pt.wikipedia.org/wiki/Vazamento_de_mem%C3%B3ria), porém, conforme explicado acima essa memória não é liberada imediatamente sendo esse o comportamento diretamente pelo **.NET**, de responsabilidade da Microsoft.

É possível notar que, na tabela acima, a coluna **Quantidade** **liberada** **(MB)** demonstra quanto de memória já foi liberada pelo processo e numa eventual necessidade, será liberada pelo GC ao Sistema Operacional, pois não está mais sendo utilizada.

 “Para fins de conhecimento, quando o Garbage Collector é acionado, ele interpreta que a memória está toda ocupada por objetos inutilizados. O processo então junta os objetos utilizados atualmente e remove os objetos inutilizados, chamados de ‘lixo’” – Microsoft - [LINK](https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/fundamentals#generations).

# Conclusão

---

É válido sempre notar que o RM permite que seus filtros e visões retornem quantidades de dados muito altas, mas esse, como todo processo dentro de um ambiente computacional, possui custos de performance. Caso o uso de memória da máquina pelo RM esteja muito alto, considere modificar seus filtros de visão para retornar menos dados por consulta ([LINK](https://tdn.totvs.com/pages/viewpage.action?pageId=403746935)) ou realizar uma melhoria no hardware. Para realizar análises acerca do consumo e de outros aspectos do RM, existem ferramentas dentro da própria plataforma, para realizar essas análises, conforme descrito na página: [LINK](https://tdn.totvs.com/x/aIvgDQ)

**Fontes:**

<https://docs.microsoft.com/pt-br/dotnet/standard/garbage-collection/fundamentals>

<https://docs.microsoft.com/en-us/dotnet/standard/garbage-collection/large-object-heap>

<https://pt.wikipedia.org/wiki/Despejo_de_mem%C3%B3ria>

<https://pt.wikipedia.org/wiki/Vazamento_de_mem%C3%B3ria>

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Gerenciamento de Memória

falsefalse

**Status:** Finalizado

false

**Data:** 02/02/2022

false

**Autores:**
