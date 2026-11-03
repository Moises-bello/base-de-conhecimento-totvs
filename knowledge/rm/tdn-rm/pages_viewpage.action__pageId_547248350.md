---
content_hash: 1526d59e3f17d196f2955f49a6a748fa9977a09525f4fd3cec6ee1d148b95366
fetched_at: '2026-06-29T00:10:42.703182+00:00'
page_id: '547248350'
product: rm
source: tdn-rm
title: Cópia de Motivo entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547248350
version: 67
---

# Implementação da Cópia de Motivo entre Coligadas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *BackOffice* |
| **Módulo:** | *Totvs Gestão de Estoques, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Action** | **Nome Técnico** | | CmpMotivoAction | Cópia de Motivo entre coligadas | |
| **Tickets relacionados** | -- |
| **País(es):** | *BRA* |
| **Banco(s) de Dados:** | *SQL SERVER e ORACLE* |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Esse recurso facilita o processo de implantação de uma nova coligada no sistema. Com poucos cliques é possível copiar todos os registros de uma coligada de origem para qualquer outra cadastrada no sistema.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de 12.1.29.

## Procedimento para Utilização

-- Acessar o "Gestão de Estoque, Compras e Faturamento" → Executar → Digitar "Motivo" e Acessar o cadastro de Motivo.

O Processo estará disponível na lista de processos deste cadastro:

Ao ser executado, ele exibirá uma tela contendo a lista de coligadas cadastradas no sistema e a opção de substituir o registro caso o mesmo exista na coligada de destino.

**IMPORTANTE:**

Serão copiados apenas os registros selecionados na visão.

Após a execução do processo, será exibido um log detalhando todos os registros que foram copiados:

divs
