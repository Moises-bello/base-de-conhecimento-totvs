---
content_hash: c0f6ff79fa84e8b5ebc397de953f069b5257883d21b8efcfd48aaa72b5c08c37
fetched_at: '2026-06-29T00:10:42.285525+00:00'
page_id: '547236437'
product: rm
source: tdn-rm
title: Cópia de Séries entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=547236437
version: 63
---

# Implementação da Cópia de Séries entre Coligadas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *BackOffice* |
| **Módulo:** | *Totvs Gestão de Estoques, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Action** | **Nome Técnico** | | MovProcCopySerieAction | Cópia de Séries entre coligadas | |
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

-- Acessar o "Gestão de Estoque, Compras e Faturamento" → Executar → Digitar "Série" e Acessar o cadastro de Séries do Movimento.

O Processo estará disponível na lista de processos deste cadastro:

Ao ser executado, ele exibirá uma tela contendo a lista de coligadas cadastradas no sistema e a opção de substituir o registro caso o mesmo exista na coligada de destino.

**IMPORTANTE:**

Serão copiados apenas os registros selecionados na visão.

Após a execução do processo, será exibido um log detalhando todos os registros que foram copiados:

divs
