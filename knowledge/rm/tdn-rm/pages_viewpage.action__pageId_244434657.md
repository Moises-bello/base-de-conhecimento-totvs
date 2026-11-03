---
content_hash: ef0c21b944364cd4aa61da0c2ed4efc0bb8d6e6c8686cac6d01dad3cd11d59ab
fetched_at: '2026-06-29T00:08:13.945470+00:00'
page_id: '244434657'
product: rm
source: tdn-rm
title: ER_SAUHRM01-499_Mapa de dispensação_Manutenção_de_Itens_e_Estoque_do_Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244434657
version: 112
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | Saúde |
| **Projeto** | * [SAUHRM01](http://jiraproducao.totvs.com.br/browse/SAUHRM01) | **IRM** | * [SAUHRM01-329](http://jiraproducao.totvs.com.br/browse/SAUHRM01-329) |
| **Requisito** | * [SAUHRM01-400](http://jiraproducao.totvs.com.br/browse/SAUHRM01-400) | **Subtarefa** | * [SAUHRM01-499](http://jiraproducao.totvs.com.br/browse/SAUHRM01-499) |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

   Este documento tem como objetivo a especificação das funcionalidades de manutenção de itens aprazados e estoque do paciente, na tela de mapa de dispensação.

## Definição da Regra de Negócio

**RN001**

1. Na tela de Mapa de Dispensação, após gerado um mapa, sistema deve permitir que os itens que integram este mapa tenham sua manutenção (inclusão, troca e exclusão) realizadas, desde que respeitadas as seguintes regras:
   1. O Item que será alterado ou excluído não pode estar confirmado;
   2. Somente Materiais podem ser adicionados ou alterados;

**RN002**

1. Comportamento da rotina de confirmação de itens deve ser modificada para que, quando confirmado um item cuja quantidade prescrita é fracionada, a quantidade remanescente seja contabilizada e adicionada ao estoque particular do paciente;
2. Ao realizar uma confirmação posterior, sistema deverá então verificar o estoque do paciente para a quantidade necessária a ser confirmada.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Mapa de Dispensação | Alteração | Estoques / Mapa de Dispensação | **RN001****, RN002** |

**RN001**

1. Acesse o menu "**Prontuário**" e selecione um paciente internado e  que esteja alocado em um leito;
2. Prescreva uma medicação para o paciente, definindo os horários aprazados e confirme a prescrição;
3. Acesse o menu "**Estoques / Mapa de Dispensação**" e inclua um filtro que contemple os aprazamentos realizados;
4. Selecione os horários para os quais deseja gerar um mapa e clique em "**Gerar Mapa**";
5. Dê um duplo clique em um dos registros que tenha mapa gerado;
6. Na tela aberta, teste a funcionalidade de inclusão, troca e exclusão de materiais.

**RN002**

1. Acesse o menu "**Cadastros / Estoques / Produto**" e busque pelo produto que será prescrito posteriormente;
2. Selecione o produto e clique em "**Anexos / Informações - TOTVS Saúde**";
3. Na aba "**Identificação**", marque as opções "**Arredonda quantidade Fracionada em Movimentação de Estoque**" e  "**Arredonda dose Fracionada na Movimentação de Estoque**";
4. Salve o Registro;
5. Acesse o menu "**Prontuário**" e prescreva este mesmo medicamento para o paciente, informando a frequência para que o aprazamento seja gerado;
6. Acesse o menu "**Estoques / Mapa de Dispensação**" e inclua um filtro que contemple os aprazamentos realizados;
7. Selecione os registros desejados e clique em "**Gerar Mapa**";
8. Dê um duplo clique em um dos registros que tenha mapa gerado;
9. Na tela que abriu, selecione um dos itens fracionados e clique em confirmar;
10. Ao confirmar o item, sistema deverá realizar o cálculo necessário para saber a quantidade necessária para a próxima confirmação.

**Tabelas Utilizadas**

1. **SZESTOQUEPACIENTE**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
