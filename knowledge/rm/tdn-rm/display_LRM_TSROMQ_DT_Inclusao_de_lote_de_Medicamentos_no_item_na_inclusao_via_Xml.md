---
content_hash: 680865ae6e9a7e8adb9905dfe0be7a3151de9a3988c7246db953052d9bbe581c
fetched_at: '2026-06-29T00:06:03.297466+00:00'
page_id: '198952777'
product: rm
source: tdn-rm
title: TSROMQ_DT_Inclusao_de_lote_de_Medicamentos_no_item_na_inclusao_via_Xml
type: documentation
url: https://tdn.totvs.com/display/LRM/TSROMQ_DT_Inclusao_de_lote_de_Medicamentos_no_item_na_inclusao_via_Xml
version: 1
---

# ME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | CLB.007 | TOTVS COLAB - INCLUSAO MOVIMENTO A PARTIR DE XML | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | Parâmetro de Integração com Neogrid com valor = Recebimento NF-e.  O Produto vinculado ao XML precisa ser controlado por lote. |
| **Ponto de Entrada:** | *N/A* |
| **Chamados relacionados** | TSROMQ |
| **Requisito (ISSUE):** | MOV000161 - TOTVS Colaboração |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas utilizadas:** | TLOTEPRD,, TITMLOTEPRD |
| **Sistema(s) operacional(is):** |  |
| **Versões/Release:** | 12.1.7 e 12.1.6 (Patch específico) |

## Descrição

Os valores de Lote de Medicamentos de uma Nota Fiscal de Entrada (tag Med), atualmente não são importados para o movimento criado VIA Totvs Colaboração. Após a implementação da funcionalidade, o sistema deverá preencher o Lote do Item de movimento no Movimento criado via Totvs Colaboração, caso exista essa tag no XML importado.

1. Somente XMLs de NF-e com a Tag <Med> devem impactar nesssa alteração. Outros, nada devem alterar no sistema.
2. A informações somente serão copiadas caso o Produto seja controlado por Lote.
3. O sistema deverá identificar o lote cadastrado e inseri-lo no item de Movimento.
4. Caso o Lote não exista, o sistema deverá inclui-lo automaticamente como um Lote para aquele produto e vincula-lo ao item de Movimento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações **12.1.7** deste chamado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

* No Totvs Gestão de Estoque, Compras e Faturamento acesse a aba **Ambiente**, clique em **Parâmetros -> Gestão de Estoque, Compras e Faturamento** e Ccique em avançar**.**Selecione o Tipo de Movimento para o qual se deseja importar o XML. Dentro dos parâmetros do tipo de Movimento, selecione a aba **Totvs Colaboração** e selecione, no parâmetro **Integração Neogrid** o valor **Recebimento NF-e**

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Integração Neogrid |
| **Tipo:** | Seleção |
| **Cont. Por.:** | Não utiliza |
| **Descrição:** | Parâmetro que define qual operação aquele tipo de movimento irá realizar na integração com o Totvs Colaboração |

* No cadastro do Produto, acesse a aba **Controle de Estoque** e marque a opção **Controlado Por Lote.**

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | Controlado por Lote |
| **Tipo:** | Checkbox |
| **Cont. Por.:** | desmarcado |
| **Descrição:** | Opção que define se aquele Produto é, ou não, controlado por lote. |

## Procedimento para Utilização

       1.            Acesse o visão de Movimentos selecionando o Tipo de Movimento configurado para Totvs Colaboração.

       2.            Selecione o processo **Inclusão de Movimentos com Arquivo XML**

       3.            Selecione o arquivo XML (que possua a tag <med>)

       4.            Selecione os Produtos para cada item do XML e execute o processo

       5.            No movimento que será aberto, os Lotes já estarão associados aos itens que possuem um produto controlado por lote.

## Ponto de Entrada

|  |  |
| --- | --- |
| **Descrição:** | Compras -> Recebimento de Materiais |
| **Localização:** | Processos -> Inclusão de Movimento com Arquivo XML |
| **Eventos:** | Inclusão de Movimento com Arquivo XML |
| **Programa Fonte:** | *N/A* |
| **Função:** | *N/A* |
|  |  |
