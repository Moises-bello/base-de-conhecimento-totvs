---
content_hash: da73f79612a5bd80fabc7f65535fa35921904b23d4eeb40acb6395c3dd51bd02
fetched_at: '2026-06-29T00:08:18.809912+00:00'
page_id: '266969757'
product: rm
source: tdn-rm
title: Migração do Processo de Motivo por Referência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266969757
version: 12
---

# Inclusões na entrada do sistema / Migração de Legado

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | **RM** | | |
| ****Segmento Executor:**** | **Construção e Projetos** | | |
| **Módulo:** | **TOTVS Gestão de Estoque, Compras e Faturamento** | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Motivo Referência* | *MovMotivoRefMovAction.* | | | |
| **Chamado:** | *Informe o(s) chamado(s) relacionado(s)* | | |
| **Requisito (ISSUE):** | CPMOV001-668 | | |
| **País:** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

## Objetivo

 Realizar a migração do legado para a nova tecnologia .Net para a Inclusão do cadastro de Motivos de Referência de Cópia que são utilizados no processo de Cópia por Referência e nos parâmetros por Tipo de Movimento na Etapa 6 - Movimento - Outros Dados.

## Definição da Regra de Negócio

Será disponibilizado no cadastro de Motivos de Referência o processo para que seja possível realizar a inclusão de Motivos defaults por Coligada ou para todas as Coligadas do Sistema, quando o parâmetro Inclusão para todas as coligadas estiver marcado. Os motivos de referência são utilizados no Assistente de Cópia por Referência e nos parâmetros por Tipo de Movimento na Etapa 6 - Movimento  - Outros Dados.

Somente serão incluídos os motivos defaults caso não exista, considerando os campos Código da Coligada e Sequencial Motivo Referência, portanto, não serão alterados motivos de referência cadastrados.

O processo de Inclusão de Motivos será realizado automaticamente para a Coligada atual ao ser executados os processos abaixo:

1. Assistente de Cópia por Referência.
2. Cópia de Movimento a partir de outro Movimento.
3. Inclusão de Movimento.
4. Inclusão do Item de Movimento.
5. Na pesquisa de Motivo de Referência nos parâmetros por Tipo de Movimento na Etapa 6 - Movimento  - Outros Dados.

Para a Cópia de Movimento a partir de outro Movimento, os Movimentos e Itens de Movimento somente serão considerados para inclusão automática os mesmos que tiverem o Motivo de Referência parametrizados na Etapa 6 - Movimento  - Outros Dados. Sendo que somente serão incluídos os motivos caso não encontre nenhum motivo de referência cadastrado ou não satisfaça os valores defaults marcados.

Os valores defaults que serão incluídos são:

| Código | Descrição | Origem da Referência | Copiar Itens | Consistir Quantidade dos Itens | Permite Incluir novos itens no movimento destino | Consiste Cliente/Fornecedor | Permite seleção de n movimentos |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Cópia Simples | Entrada | Sim | Não | Sim | Não | Sim |
| 2 | Simples Remessa | Entrada | Sim | Sim | Não | Sim | Sim |
| 3 | NF Acompanhamento de Cupom Fiscal | Entrada | Sim | Sim | Não | Sim | Sim |
| 4 | Devolução de Compra de Mercadorias | Entrada | Sim | Sim | Não | Sim | Sim |
| 5 | Devolução de Venda de Mercadorias | Saída | Sim | Sim | Não | Sim | Sim |
| 6 | NF Complementar / Retificadora | Entrada | Não | Não | Sim | Não | Não |
| 7 | Remessa para Conserto | Entrada | Sim | Sim | Sim | Sim | Sim |
| 8 | Devolução material receb. conta e ordem | Entrada | Sim | Sim | Não | Não | Sim |
| 9 | Produção | Saída | Sim | Sim | Não | Sim | Não |
| 10 | Retorno de Remessa | Entrada | Sim | Sim | Sim | Sim | Sim |
| 11 | Retorno de Mercadoria não Aplicada na Industrialização | Entrada | Sim | Sim | Não | Sim | Sim |
| 12 | Retorno de Remessa para Industrialização | Entrada | Sim | Sim | Não | Sim | Sim |
| 13 | Devolução Simbólica de Mercadoria em Consignação | Entrada | Sim | Sim | Não | Sim | Sim |
| 14 | Venda Mercadoria Consignada | Entrada | Sim | Sim | Não | Sim | Sim |
| 15 | Devolução Mercadoria Consignada não Comercializada | Entrada | Sim | Sim | Não | Sim | Sim |
| 16 | Conhecimento Transporte Eletrônico (CT-e) - Anulação | Saída | Sim | Sim | Não | Não | Não |
| 17 | Conhecimento Transporte Eletrônico (CT-e) - Substituição | Saída | Sim | Não | Não | Não | Não |
| 19 | Substituição NFe - Serviço | Entrada | Sim | Não | Sim | Não | Não |
| 20 | Cópia Simples com Relacionamento | Entrada | Sim | Sim | Sim | Sim | Sim |
| 21 | Cópia NF-e de Ajuste - Cancelamento Indevido | Entrada | Sim | Sim | Não | Sim | Não |
| 22 | Cópia NF-e de Ajuste - Estorno de Venda | Saída | Sim | Sim | Não | Sim | Não |
| 23 | Cópia NF-e de Ajuste - Estorno de Compra | Entrada | Sim | Sim | Não | Sim | Não |
| 24 | NF-e Produtor Rural - Contra Nota | Entrada | Sim | Sim | Não | Sim | Não |
| 25 | Cópia Simples com relacionamento somente de Movimento | Entrada | Não | Não | Sim | Não | Não |
| 26 | Transformação de Itens - Movimentações Internas entre Produtos | Saída | Não | Não | Não | Não | Não |
| 27 | NF Complementar com Cópia de Itens | Entrada | Sim | Não | Sim | Não | Não |
| 28 | Cópia NF-e de Ajuste - Estorno de Transferência | Saída | Sim | Sim | Não | Sim | Não |

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Motivo de Referência | [Alteração] | [Tabelas Auxiliares -> Motivo Referência] | - |
| Inclusão de Motivos de Referência | [Criação] | [Tabelas Auxiliares -> Motivo Referência -> Inclusão de Motivos de Referência] | - |
| Assistente de Cópia por Referência | [Alteração] | [Movimentos -> Processos -> Assistente de Cópia por Referência] | - |
| Cópia de Movimento a partir de outro Movimento | [Alteração] | [Movimentos -> Processos -> Cópia de Movimento a partir de outro Movimento] | - |
| Inclusão de Movimento | [Alteração] | [Movimentos] | - |
| Inclusão de Item de Movimento | [Alteração] | [Movimentos] | - |
| Lookup de Motivo de Referência | [Alteração] | [Ambiente -> Parâmetros -> Tipo de Movimento -> Etapa 6 - Movimento  - Outros Dados] | - |

***Tabelas Utilizadas***

* *TMOTIVOREFMOV – Motivo de Referencias de Cópia*

### Procedimento para Utilização

*Para utilizar o processo é necessário acessa-lo através do cadastro de Motivo de Referência que está localizado em  **BackOffice/Gestão de Estoque, Compras e Faturamento/Cadastros/Estoque, Compras e Faturamento/Mais/Tabelas Auxiliares/Motivo Referência.***

1. Acessar a opção de Menu "Inclusão de Motivo de Referência" em Processos.

2. Serão atualizados todos os motivos de referência que não existem em todas as Coligadas ou apenas a Atual, conforme selecionado no parâmetro do processo.
