---
content_hash: 43bfc754a07d7b0f02c2c8068b0647b6d35413624a8df28cf106b39e7becb9ee
fetched_at: '2026-06-29T00:10:43.008528+00:00'
page_id: '549490577'
product: rm
source: tdn-rm
title: Cópia de Parâmetros por Tipo de Movimento Entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=549490577
version: 65
---

# Implementação da Cópia de Parâmetros por Tipo de Movimento Entre Coligadas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM.* |
| **Segmento:** | *BackOffice* |
| **Módulo:** | *Totvs Gestão de Estoques, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Action** | **Nome Técnico** | | MovTMvCopiaTMvAction | Cópia de parâmetros por tipo de movimento entre coligadas | |
| **Tickets relacionados** | -- |
| **País(es):** | *BRA* |
| **Banco(s) de Dados:** | *SQL SERVER e ORACLE* |
| **Tabelas Utilizadas:** |  |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Esse recurso facilita o processo de implantação de uma nova coligada no sistema. Com poucos cliques é possível copiar todos os parâmetros por tipo de movimento de uma coligada de origem para qualquer outra cadastrada no sistema.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de 12.1.29.

## Procedimento para Utilização

-- Acessar o "Gestão de Estoque, Compras e Faturamento" → Ambiente → Parâmetros → Gestão de Estoque, Compras e Faturamento, acessar qualquer visão dos tipos de movimento → Processos → Cópia de Tipo de Movimento:

Ao ser executado, será exibida uma tela contendo a lista de tipos de movimento cadastrados na coligada em que o usuário estiver logado:

A primeira etapa do processo é dividida em duas partes, sendo elas:

* Tipos de Movimento a Serem Copiados: Onde o usuário deve selecionar quais tipos de movimento ele deseja copiar para a(s) coligada(s) de destino.
* Dependências por tipo de movimento: Exibe toda dependência do tipo de movimento selecionado, ou seja, todos os tipos de movimento que devem ser importados juntos para evitar problemas de relacionamento.

Ao selecionar qualquer registro que possua dependências, o sistema permite que o usuário selecione todas de forma automática:

Caso alguma dependência não seja selecionada, o sistema informa que elas serão removidas do registro na coligada de destino:

Caso existam dependências que caracterizem uma referência circular, o sistema exibe o registro em vermelho e não permite que o mesmo seja selecionado:

Ao clicar em avançar no Wizzard do processo, o usuário tem acesso ao segundo passo:

Nesta etapa é possível definir se a cópia será realizada na coligada atual ou entre coligadas. Caso seja selecionada a opção "Entre Coligadas" o sistema permite que o usuário informe se é para manter ou sobrepor o registro de destino. Independente da opção selecionada, é possível alterar o código e nome do tipo de movimento na coligada de destino.

No caso de cópia entre coligadas, o sistema exibe uma nova etapa do processo, onde é possível selecionar para quais coligadas os registros serão copiados:

Após a execução do processo, será exibido um log detalhando a situação de cada tentativa de cópia:

divs
