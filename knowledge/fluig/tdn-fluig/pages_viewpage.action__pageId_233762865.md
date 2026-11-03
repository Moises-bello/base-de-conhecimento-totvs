---
content_hash: c9ea1c9b302a47a6834aa6c0f6221cf0bbb95aabd33e52f45dbe799c16ccbed4
fetched_at: '2026-06-28T21:35:20.113205+00:00'
page_id: '233762865'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Busca
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233762865
version: 35
---

.\*ndice

# Falando de busca...

---

A busca permite pesquisar objetos sociais, documentos, pastas, formulários, registros de formulários, pessoas influentes em determinados assuntos – Influenciadores –, artigos, publicações e pessoas a partir de qualquer página da plataforma.

Ela permite que pesquisas possam ser personalizadas e proporcionar critérios de busca definidos pelo usuário, permitindo restringir os locais, tipos, tempo sobre os recursos que estão sendo pesquisados.

Precisa de ajuda?Acesse a **Central de ajuda** da plataforma clicando no ícone **Assistente** – localizado no lado superior direito do cabeçalho – e, em seguida, clicando na aba **Central de ajuda** para obter informações específicas sobre este recurso, além de *links* com documentações relacionadas. [Saiba mais](http://tdn.totvs.com/x/ZMhSDg).falseBuscatrueCampo de buscaResultado da busca

## Realizar busca

---

**01.** No menu principal, clique em  **Buscar**.

**02**. Informe o termo que deseja buscar.

#f2f2f2#f2f2f2

Uma lista de sugestões será exibida. É possível selecionar uma palavra da lista ou digitar uma palavra qualquer.

Por padrão, o indexador da plataforma (Solr) faz a indexação da busca por até 15 caracteres. Essa característica foi definida para não ocupar muito espaço em disco no momento da indexação.

Dica!

Utilize para uma busca mais precisa.

**03**. No teclado, pressione **ENTER**.

#f2f2f2#f2f2f2

A tela de resultado da busca será exibida com a aba **Tudo** selecionada. 

trueimageVeja a imagem#0897E9INLINE

## Filtrar resultados

---

**01.** Acesse o resultado da busca conforme o item .

**02.** No resultado apresentado, clique em  **Filtrar**.

#f2f2f2#f2f2f2

A área de filtros será expandida e serão exibidos os filtros disponíveis.

**03.** Selecione o filtro a ser considerado.

#f2f2f2#f2f2f2

Os filtros disponíveis são:

* **Buscar no período**: é possível escolher os seguintes filtros:
  + **no último dia**;
  + **na última semana**;
  + **no último mês**;
  + **no último ano**;
  + **informar período**: permite especificar um **período** informando a data de início e fim da pesquisa.

Para cada filtro selecionado, uma etiqueta com o filtro selecionado é exibida acima do filtro, facilitando a visão do que está sendo filtrado. Esta etiqueta possui um botão para remover o filtro, refazendo a busca novamente sem filtro.

**04.**  Se o filtro escolhido foi Informar período, depois de definir as datas inicial e final, clique em **Filtrar**.

#f2f2f2#f2f2f2

Toda busca apresenta o resultado ordenado por relevância. É possível alterar a ordenação do resultado para mais recente ou mais antigo. Para isso, acione a caixa de seleção no canto superior direito da tela de resultado e selecione uma opção.

## Ordenar resultados da busca

---

**01.** Acesse o resultado da busca conforme o item .

**02**. No resultado apresentado, selecione a ordenação desejada na caixa de seleção localizada no lado superior direito.

#f2f2f2#f2f2f2

As opções de ordenação disponíveis são:

* **Ordenar por relevância**: determina que os documentos favoritos serão apresentados primeiro;

* **Ordenar por mais recente**: determina que os documentos serão apresentados pela data de criação de forma decrescente, ou seja, criados mais recentemente primeiro;

* **Ordenar por mais antigo**: determina que os documentos serão apresentados pela data de criação de forma crescente, ou seja, mais antigos primeiro.

## Adicionar aos favoritos

---

**01.** Acesse o resultado da busca conforme o item .

**02.** No resultado apresentado, clique sobre o ícone **Favorito** , localizado ao lado direito da pasta ou documento desejado.

trueimageVeja a imagem#0897E9INLINE

**03.** Uma janela de confirmação será exibida demonstrando que a ação foi realizada com sucesso.

#f2f2f2#f2f2f2

Para mais detalhes sobre esse recurso, acesse a documentação .

## Consultar caracteres curinga

---

Na tabela abaixo são listados os caracteres curingas e termos especiais que podem ser utilizados na busca do TOTVS Fluig Plataforma.

| ARGUMENTO | EFEITO | EXEMPLO |
| --- | --- | --- |
| **#**  **Hashtags** | Permite efetuar a busca por hashtags que contenham a tag digitada. | #benefícios  Retorna publicações com a tag benefícios trueimageVeja a imagem#0897E9INLINE |
| **?** | Permite efetuar a busca por palavras que tenham qualquer caractere no lugar do sinal de interrogação. Não pode ser utilizado no começo de um termo. | li?ão Retorna Limão e Lição. |
| **\*** | Permite efetuar busca com partes de uma palavra. Não pode ser utilizado no começo de um termo. | li\*ão Retorna limão, lição e ligação. |
| **~**  **Proximidade** | Permite efetuar a busca de documentos que tenham termos próximos. | “Juros BACEN”~5 Retorna todos os documentos onde os termos Juros e BACEN estejam até 5 palavras distantes um do outro. |
| **^**  **Prioridade** | Permite definir prioridade a um termo na busca. | Juros ^2 BACEN Retorna primeiro os documentos que tenham mais referência ao termo Juros. |
| **OR** | Permite efetuar a busca nos documentos que tenham algum dos termos especificados. | Juros OR BACEN Retorna os documentos que tenham a palavra Juros ou BACEN. |
| **AND** | Permite efetuar a busca nos documentos que tenham todos os termos especificados. | Juros AND BACEN Retorna os documentos que tenham a palavra Juros e BACEN. |
| **+** | Torna um termo requerido na busca. | Juros + BACEN Garante que todos os documentos retornados tenham o termo BACEN. |
| **NOT** | Exclui um termo da consulta. | Juros NOT BACEN Retorna os documentos que tenham o termo Juros mas não tenham o termo BACEN. |
| **-** | Exclui um termo da consulta. | Juros -BACEN Retorna os documentos que tenham o termo Juros mas não tenham o termo BACEN. |
| **() Agrupamento** | Permite agrupar argumentos. | (Juros + BACEN) OR COPON Retorna os documentos que tenham o termo Juros (opcional) e BACEN ou que tenham o termo COPON. |
| **“”**  **Frase Exata** | Permite efetuar a busca nos documentos que contenham a frase exata. | “Juros definidos pelo Banco Central” Retorna somente os documentos que tenham essa frase exata e nessa sequência. |

Fique atento!

Esta documentação é válida a partir da atualização **Voyager (2.0)**. Se você utiliza uma atualização anterior, ela pode conter informações diferentes das quais você vê na sua plataforma.
