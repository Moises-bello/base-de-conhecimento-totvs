---
article_id: 38919085750935
category: ADVPL - Classe e Função
content_hash: 62fbcb369d73583f6280370132dc9da0fa052d5f88712d60f516c533945bf66d
fetched_at: '2026-06-28T22:40:20.603473+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Diferenças entre
  Inicializador Padrão e Inicializados de Browse
type: support-article
updated_at: '2026-03-18T17:02:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38919085750935-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Diferen%C3%A7as-entre-Inicializador-Padr%C3%A3o-e-Inicializados-de-Browse
---

O Inicializador Padrão (X3\_RELACAO) define o valor inicial de um campo ao incluir um novo registro, preenchendo automaticamente o campo. Já o Inicializador de Browse (X3\_INIBRW) exibe um conteúdo virtual em listagens (browse) sem gravar dados na tabela, mostrando informações em tempo real. Ambos são expressões AdvPL configuradas no dicionário de dados via SIGACFG, com finalidades distintas.

**Dúvida**   
Qual a diferença entre o Inicializador Padrão e o Inicializador de Browse no Protheus?

**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões

**Solução**   
Ambos os inicializadores são expressões AdvPL configuradas no Dicionário de Dados (SX3) via módulo Configurador (SIGACFG), porém atuam em momentos e com finalidades diferentes no sistema:

* **Inicializador Padrão (X3\_RELACAO):**

  + **Objetivo:** Definir o conteúdo inicial e sugerido para um campo no exato momento da **inclusão** de um novo registro. A expressão é avaliada ao abrir a tela ou ao adicionar uma nova linha em um grid.
  + **Exemplo 1 (Utilizando IIF):** Sugerir um valor baseado no conteúdo de um parâmetro do sistema.  
    `IIF(GetMV("MV_MEUPAR") == "S", "1", "2")` *(Se o parâmetro for "S", o campo já nasce preenchido com "1", caso contrário, "2".)*
  + **Exemplo 2 (Utilizando Posicione):** Sugerir a descrição de uma condição de pagamento padrão gravada em outra tabela.  
    `Posicione("SE4", 1, xFilial("SE4") + "001", "E4_DESCRI")` *(Ao incluir o registro, o campo será preenchido automaticamente com a descrição da condição de pagamento de código "001".)*
* **Inicializador de Browse (X3\_INIBRW):**

  + **Objetivo:** Definir o conteúdo de exibição de um campo (**campo virtual**) durante a montagem da tela de listagem inicial (**Browse** / `FWmBrowse`). Ele não grava dados fisicamente na tabela corrente, apenas exibe a informação em tempo real na listagem.
  + **Exemplo 1 (Utilizando IIF):** Exibir um texto amigável no grid de listagem baseado em um campo de status interno da tabela.  
    `IIF(SC5->C5_TIPO == "N", "Normal", "Outros")` *(Na tela de browse, ao invés de exibir apenas "N", o sistema exibirá a palavra "Normal" na coluna do campo.)*
  + **Exemplo 2 (Utilizando Posicione):** Exibir o Nome do Cliente na listagem de Pedidos de Venda, sem precisar criar um campo físico de Nome no pedido.  
    `Posicione("SA1", 1, xFilial("SA1") + SC5->C5_CLIENTE + SC5->C5_LOJACLI, "A1_NOME")` *(Durante a renderização da tela de listagem, o sistema busca na tabela de Clientes (SA1) o nome correspondente ao código e loja gravados no Pedido (SC5), exibindo-o na coluna.)*

> **Observação Importante:** As expressões e funções AdvPL apresentadas acima são meramente ilustrativas. As lógicas, condições, tabelas e regras de negócio inseridas nos campos de inicializadores ficam inteiramente a critério do analista ou desenvolvedor responsável pela parametrização, devendo ser adequadas à realidade e necessidade de cada ambiente.

**Passos**

Para inserir essas expressões no dicionário:

1. Acesse o módulo **Configurador (SIGACFG)**.
2. Siga pelo menu em **Base de Dados > Dicionário > Base de Dados**.
3. Pesquise a tabela correspondente e acesse a área de **Campos**.
4. Edite o campo desejado e navegue até a aba **Opções**.
5. No bloco de propriedades, preencha os campos **Inicializador Padrão** ou **Iniciaizador de Browse** com as funções ou expressões AdvPL desejadas ou instruções fixas como caracteres ou numéricos, de acordo com o tipo do campo e dado que queira apresentar.
6. Salve a alteração e atualize o dicionário de dados (opção de atualização no SIGACFG) para a mudança ser aplicada.

**Saiba Mais**

[Dicas de desenvolvimento e como utilizar as plataformas TOTVS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4984257614615-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Dicas-de-desenvolvimento-e-como-utilizar-as-plataformas-TOTVS)  
[Linguagem AdvPL](https://tdn.totvs.com/display/tec/Fundamentos+da+linguagem+AdvPL)
