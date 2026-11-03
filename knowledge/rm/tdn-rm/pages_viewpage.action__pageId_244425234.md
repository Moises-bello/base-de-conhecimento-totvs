---
content_hash: 631afbebcec64a267bb0fff102c92143be318a0ff31755d1942fe44626e46243
fetched_at: '2026-06-29T00:08:13.525322+00:00'
page_id: '244425234'
product: rm
source: tdn-rm
title: Telas de Edição RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244425234
version: 25
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parametrização**
3. **Usabilidade**

## **01. VISÃO GERAL**

            Implementação para que as telas de edição do RM fiquem subordinadas à visão e não mais "travem" a interface visual (MDI) ao serem abertas. Na prática o usuário poderá abrir N edições ao mesmo tempo e continuar trabalhando.

Dica

Como a tela de visão continua disponível, se ela for fechada a edição subordinada será fechada também.

## **02. PARAMETRIZAÇÃO**

* Parâmetros | Globais | Aba Configurações Publicas | Parâmetro "Edição como Diálogo".

|  |  |
| --- | --- |

Observação:

Por default o parâmetro "Edição como Diálogo" vem marcado, ou seja, telas modais desabilitadas.

## **03. USABILIDADE**

falseImplementaçõesAbrindo duas Guias ao Mesmo Tempo

Visualmente a tela de edição continua parecida como era antes. O diferencial é que apesar de estar na frente da visão e de outras abas ela é apenas parte da tela, ela não toma todo o foco e os itens que estão atrás continuam funcionais.

          É possível trocar o registro selecionado, abrir outra tela, enfim, realizar qualquer operação que se realizaria sem a tela de edição aberta mesmo que ela esteja ativa. Como toda a interface estará disponível é possível inclusive abrir duas ou mais telas de edição ao mesmo tempo:

          Isso abre um novo universo de possibilidades, aumentando a produtividade e permitindo que os usuários comparem informações de registros de cadastros distintos com agilidade.

Edição Subordinada

          Criada também a possibilidade de se manter a tela de edição subordinada à sua visão, para melhor organização dos dados e visualização das informações da visão, permitindo alternar entre visões distintas sem que seja necessário fechar as edições, fazendo com que a edição fique dentro do contexto ao qual pertence, sem impactar na utilização do sistema. Ela ficará aberta enquanto a visão também estiver e será atualizada automaticamente conforme o usuário interagir na visão.

Posicionando a Visão

          Ao se clicar na barra de título da janela e arrastar, aparecerão ícones que permitem que a edição seja anexada a qualquer um dos quatro pontos de sua visão: Direita, esquerda, topo ou inferior.

Anexando a Visão a outro Anexo

          Ao arrastar a tela de edição na direção de um anexo já existente, será exibido também o ícone central, que permite que ela conviva no mesmo espaço que o anexo, sem reduzir o espaço disponível para os dados da visão.

Navegando Entre Anexos e Visões Anexadas

          Poderá ser alternado entre a tela de edição e os anexos utilizando-se as abas que por padrão ficam na parte inferior.

Dica

 Para que a edição volte a ficar flutuando sobre a visão basta dar um duplo-clique na barra de título.

Atenção

Ao ativar a Edição como Diálogo o mecanismo de AutoComplete dos LookUps, que ficam dentro de um Grid, serão desabilitados.

false

**Versão:** 12.01.XX
