---
content_hash: 5504f3bc331018af5c14f9c603637ccc8c1da29ecbfeeb67958892027f716c59
fetched_at: '2026-06-29T00:06:16.266899+00:00'
page_id: '212894614'
product: rm
source: tdn-rm
title: DT_Melhorias_no_Processo_de_Conclusão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=212894614
version: 2
---

# Melhorias no Processo de Conclusão

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  | | --- | | **Rotina** | | Conclusão de Movimento | | Alteração de Movimento |  |  | | --- | | **Rotina(s) envolvida(s)** | | Inclusão de Movimento | | Concluir Pedido | | Faturar/Receber Movimento | | Permissões por Tipo de Movimento | | Cópia de Movimento | | Exclusão de Item de Movimento | | Estorno de item não recebido | | Integração TOP | |
| **Parâmetro(s):** | Alterar Item Integrado |
| **Requisito (ISSUE):** | N/A |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas utilizadas:** | TMOV – Movimento TITMMOV – Item de Movimento TMOTIVOCONCLPED - Motivo de Conclusão do Pedido TUSRTMV - Permissões por Tipo de Movimento |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superior. |
| **Versões/Release:** | 12.1.4 |

## Descrição

Permitir que o usuário conclua determinados itens de movimento que não serão mais faturados, desconsiderando os itens de movimento que foram integrados ao TOP (TOTVS Obras e Projetos).

**1 – Conclusão de Itens de Movimento**

Para os movimentos pendentes ou parcialmente faturados, caso o usuário não deseje receber os itens restantes ou algum item específico o mesmo poderá concluir estes itens através do processo de Conclusão de Itens de Movimento.

O processo de Conclusão de Itens de Movimento está disponível na visão de **Movimentos >> Processos >> Concluir Pedido.**

O campo quantidade concluída do item de movimento irá armazenar o valor da quantidade do item que está sendo concluída. Este campo estará disponível no anexo dos itens na visão do movimento e na edição do item de movimento.

Para cada processo de conclusão executado, na tabela de motivo de conclusão, será adicionado um sequencial para cada vez que o processo for executado, com a data e o motivo da conclusão.

Ao executar a conclusão de itens, será atualizado no movimento um flag que irá informar que este movimento já passou por um processo de conclusão. Este campo estará disponível na visão do movimento.

Itens de movimento que estão integrados ao TOP (TOTVS Obras e Projetos) não podem ser concluídos através deste processo, sendo necessário **estornar estes itens integrados** **(processo de estorno de itens não recebidos)**, através de processo específico, para que o saldo dos mesmos retorne ao Construção e Projetos.

**2 – Inclusão de Movimento**

Ao incluir um movimento através do módulo Construção e Projetos o conteúdo do campo **Aplicação de Origem** do movimento será copiado para o campo **Aplicação de Origem** de todos os itens do movimento.

**3 – Alteração de Movimento**

Ao alterar a quantidade de um item de movimento integrado ao módulo Construção e Projetos, será disparado uma integração com o módulo Construção e Projetos para que o mesmo atualize o valor da quantidade solicitada com a diferença que está sendo realizada com esta alteração no item de movimento.

**Permissão por Tipo de Movimento para Alterar Quantidade Integrada ao TOP (TOTVS Obras e Projetos)**

Na tela de **Permissões por Tipo de Movimento**, acessada através do **Cadastro de Usuário**, existe uma nova opção para permitir ao usuário alterar itens de movimentos integrados ao Construção e Projetos.

Acessar **RM >> Serviços Globais >> Segurança >> Usuários**. Selecionar o usuário mestre, contexto  de sistema Gestão de Estoque, Compras e Faturamento e abrir o anexo **Permissões por Tipo de Movimento**. Para os tipos de movimento que começam com 1.1.% será exibido o campo **Alterar Item Integrado.** Marcar este campo para o tipo de movimento 1.1.04 – Solicitação de Compra (RM Solum):

**4 – Faturamento**

Ao faturar um movimento o campo **Aplicação de Origem** do movimento original não será copiado para o movimento destino. Entretanto o campo **Aplicação de Origem** do item de movimento será copiado para o item de movimento destino.

 Durante o faturamento de um movimento quando o Item de Movimento for originado pelo módulo Construção e Projetos, não será possível aumentar a quantidade do item no movimento destino, sendo permitido apenas diminuir a quantidade para que seja possível realizar o Faturamento Parcial.

Gerar contrato através de movimentos de Pedido de compra gerados por cotação ou manualmente. Esse novo processo será elaborado para atender tanto a geração de contrato a partir da cotação como também a geração de contrato através de Pedidos de compra simples.

## Informações Adicionais

 

**Conclusão de Itens de Movimento**

Não permite que sejam concluídos itens de movimentos integrados ao TOP (TOTVS Obras e Projetos).

Na conclusão de itens de movimento, quando parametrizado para Faturamento Parcial por Valor – Movimento, será necessário concluir todos os itens de movimento.

**Alteração de Quantidade de Itens de Movimentos Integrados ao Construção e Projetos**

Não permite que seja alterada a quantidade, o projeto, a tarefa, o produto ou a unidade de medida de itens de movimentos integrados ao módulo Contrução e Projetos caso o usuário não possua permissão para este procedimento.

Fica definido que, caso o usuário tenha permissão para alterar a quantidade do item de movimento integrado ao Contrução e Projetos, o mesmo poderá tanto aumentar, quanto diminuir esta quantidade, sendo que a diferença desta alteração de quantidade será enviada para o serviço integrado ao Contrução e Projetos.

Não se pode realizar uma alteração no item que aumente a quantidade pedida pelo TOP (TOTVS Obras e Projetos).

A regra de permissão por tipo de movimento só será considerada para o primeiro movimento originado pela integração com o Construção e Projetos, sendo que os movimentos subsequentes originados pelos processos do Gestão de Estoque, Compras e Faturamento não podem ter seus campos do item de movimento alterados, caso o mesmo seja integrado ao TOP (TOTVS Obras e Projetos).

divs
