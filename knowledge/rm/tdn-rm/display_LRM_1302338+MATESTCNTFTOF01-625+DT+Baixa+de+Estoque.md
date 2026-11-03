---
content_hash: 281180c727e6112f8362b94078d836e6d235bdd9653b8fd37bba7616136cd2c7
fetched_at: '2026-06-29T00:08:44.927020+00:00'
page_id: '309408420'
product: rm
source: tdn-rm
title: 1302338 MATESTCNTFTOF01-625 DT Baixa de Estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/1302338+MATESTCNTFTOF01-625+DT+Baixa+de+Estoque
version: 98
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Baixa de Estoque. |
| **Situação/Requisito:** | Ao realizar a “Baixa de Estoque” no BackOffice integração (SigaMNT) não é possível informar baixa de mais de uma Ordem de Serviço ao mesmo tempo. Também é necessário informar manualmente os itens que serão baixados.  O processo deve ser evoluído para permitir a baixa de múltiplas OS reportando insumo para SigaMNT. |
| **Solução/Implementação:** | Ao reportar baixa de insumo do BackOffice para o SigaMNT agora deve-se utilizar o processo “Assistente de cópia por Referência – Reporta Insumo MNT”.  Esse novo processo permite reportar baixa de insumo utilizando dois motivos de referência 25 ou 32.  Motivo de referência “25 - Cópia Simples com relacionamento somente de Movimento”:  O processo é identifico ao anterior.  Motivo de referência “32 – Reporta Insumo MNT”:  É possível reportar o consumo de múltiplas OS.   1. Na página inicial para seleção de movimentos, selecione um ou mais movimentos. 2. Na página de seleção dos itens de movimento (nova)  * + Os itens presentes nas solicitações de armazém serão carregados.   + Selecione um ou mais item/produto que vai ter a baixa reportada, na linha é possível ver o identificador da OS e seu número de movimento.   + O preço unitário e o cliente/fornecedor é levado carregado de acordo com os itens selecionados.   + A quantidade é distribuída automaticamente baseado no que foi recebido de cada item.   + Qualquer diferença para mais ou menos na quantidade é lançada na última ocorrência do produto na lista.   3. Executar  4. Os itens são agrupados por OS e para cada grupo de itens é aberto um movimento com os itens já carregados.  5. É criado o relacionamento do movimento e dos itens referenciando a Nota Fiscal. |
| **Conversores e Parâmetros:** | Para atualizar o adapter no RM realize os seguintes passos:   1. Acesse RM \ Integração \ Integração \ Mensagem Única \ Integrações. Selecione a integração de Identificador 1001 e abra o anexo Mapeamento de Entidades. Edite o registro STOCKTURNOVER, acesse o link do evento e clique em excluir. 2. No anexo Mapeamento de Entidades exclua o registro STOCKTURNOVER. 3. Acesse Ferramentas \ Configurar, avance até a etapa Projetos de Integração. Selecione o item TOTVS Manutenção de Ativos x BackOffice RM e execute o processo para atualizar o adapter CancelRequest.   Para atualizar a fórmula visual no RM realize os seguintes passos:   1. Remover a formula visual ’10.Mensagem Única – Baixa Estoque' 2. Importar novamente a formula em sua versão atualizada, marcando importar gatilhos. |
| **Tickets relacionados:** | 1302338. |
| **Requisito:** | Integração Manutenção de Ativos x BackOffice RM. |

divs
