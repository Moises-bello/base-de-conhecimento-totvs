---
content_hash: 106a3fcae858b3c16494e811e1c006562a6f60eb04efce2f8aedcc5648065a01
fetched_at: '2026-06-29T00:08:17.240197+00:00'
page_id: '254609766'
product: rm
source: tdn-rm
title: DT_Ajustes_Mapa_de_Dispensação_E_Movimentação_de_Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=254609766
version: 115
---

# Ajustes Mapa de Dispensação e Movimentação de Estoque

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Mapa de Dispensação | | Movimentação de Estoque | |
| **Cadastros Iniciais:** | Opções / Parâmetros / Parâmetros Gerais/Estoques II.  Cadastros / Estoque / Produto / Anexos > Informações TOTVS Saúde.  Cadastros / Cuidados com o Paciente / Prescrição Médica / Padrões de Prescrição. |
| **Parâmetro(s):** | Opções / Parâmetros / Parâmetros Gerais/Estoques II :   * "Utiliza Dispensação Horária por Requisição". * "Filtra Estoque do Paciente por Requisição". * “Modelo de Navegação”.   Em Cadastros / Estoque / Produto / Anexos > Informações TOTVS Saúde:   “Arredonda quantidade fracionada na movimentação de estoque”  “Arredonda dose fracionada na movimentação de estoque”: |
| **Chamados Relacionados** | TVNGMH |
| **Requisito (ISSUE):** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-506 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER® e ORACLE® |
| **Tabelas Utilizadas:** | SZAPRAZAMENTO, SZMOVIESTOQUEITEM, SZMOVITMAPRAZ |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Ajuste na atribuição do código do pacote no Mapa de Dispensação.

As funcionalidades de Alterar Item e "Desconfirmar" item migrados foram implementadas na Movimentação de Estoque.

## Procedimento para Utilização

* Em **Prontuário Eletrônico / Prescrição Médica**. Realize a prescrição para um paciente realizando aprazamento para os itens prescritos e conclua a prescrição.
* Acesse o **Estoques / Mapa de Dispensação**, clique em “Sim” para **Modelo de Separação Prévia** e gere um mapa para duas requisições diferentes (dois pacientes diferentes). Abra o mapa, confirme e processe os itens para gerar o código do pacote.

* Acesse a movimentação de estoques. Pode acessar as requisições feitas para o mapa ou crie uma nova.
* Abra a movimentação. Foram incluídos os botões com a mesmas funções do mapa. O “Alterar Item”, abrirá uma tela para selecionar um item similar ao que se encontra na movimentação. **(este item é pré-configurado).**

* Para configurar estes itens acesse o menu ‘Cadastros / Cuidados com o Paciente / Prescrição Médica / Padrões de Prescrição”.
* Selecione, ou crie um novo Principio Ativo:

* Na aba “Padrão de Prescrição”, crie um novo:

* Na aba “Itens de Estoque” Informe todos os itens de estoque que pertencem a este mesmo padrão de prescrição:
* Na aba “Padrão de Prescrição”, preencha um novo registro:

* Feito isto, estes itens estarão agrupados sob o mesmo princípio ativo e serão tratados como equivalentes, na funcionalidade de alteração de medicamento da Movimentação de Estoque.

* O botão  irá "desconfirmar" um item já confirmado.

divs
