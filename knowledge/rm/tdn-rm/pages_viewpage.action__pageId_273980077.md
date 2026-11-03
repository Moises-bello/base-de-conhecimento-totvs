---
content_hash: ca80f21a8e8203e139ff6ec5aa6ba9aba9ccecc5899d08afbe1d85993c3d7d04
fetched_at: '2026-06-29T00:08:31.995839+00:00'
page_id: '273980077'
product: rm
source: tdn-rm
title: 473251 MSAU-6140 DT Filtrar Lotes por Local de Estoque na Geração de Código
  de Barras
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273980077
version: 98
---

# Filtrar lotes por local de estoque na geração de código de barras

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Estoque | Etiquetas de código de barras | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle® e SQL Server® |

## Descrição

Realizado ajuste no sistema para filtrar os produtos e lotes por local de estoque.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.16.004 do RM Saúde

Procedimento para Utilização

       1.            No TOTVS Gestão Hospitalar, acesse o menu Cadastros > Estoque > Produtos;

       2.            Selecione um produto e clique no botão Anexo > Informações TOTVS Saúde;

       3.            Na aba de identificação, no campo "Bloqueio por centro de custo" marque a opção "Pesquisa Prescrição/Requisição (Libera os selecionado)";

       4.            Após marcar o parâmetro, será habilitada a aba "Bloqueio/Liberação por centro de custo" deve-se adicionar um centro de custo vinculado a uma unidade de atendimento;

       5.           Em seguida, acesse o menu estoque > Etiqueta de código de barras;

       6.           Selecione um local de estoque e em seguida, clique em pesquisar e busque todos os produtos da unidade de estoque;

                     O sistema deve trazer somente os produtos vinculados a unidade de estoque e os itens que não possuem bloqueio por centro de custo;

        7.         Selecione um medicamento e clique em OK, o sistema deve trazer somente o saldo e lotes do produto existentes no local de estoque selecionado.

      OBS: Se não for selecionado o local de estoque, o sistema vai trazer todos os produtos cadastros no sistema.

divs
