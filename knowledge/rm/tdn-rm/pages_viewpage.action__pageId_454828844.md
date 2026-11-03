---
content_hash: 6838ff38f74e501bc6e66bda3efa62d2830e90caee35ad3d0fd010b4e6023b6d
fetched_at: '2026-06-29T00:10:12.531549+00:00'
page_id: '454828844'
product: rm
source: tdn-rm
title: 4068158 MATESTCNTFTOF01-4656 DT Custo Insumo Mão de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=454828844
version: 3
---

# CUSTO INSUMO MÃO DE OBRA (SERVIÇO)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | BackOffice. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Consulta Saldos e Custos. | EstPrdConsultaSaldosCustosAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Configurador de Integrações | ConConfiguraIntegracaoAction | | Transformação. | ConTransformacaoAction | | Consulta Saldo em Estoque. | SourceCode STOCKLEVEL | |
| **Tickets relacionados** | 4068158. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | TPRODUTO – Produtos.  TPRODUTODEF – Dados dos Produtos por Coligada.  TPRDLOC – Saldos de Produtos por Local de Estoque.  HCTRANSFORMACAO – Transformação Mensagem Única TOTVS.  HCMAPAINTEGRACAO – Tabela de mapeamento das entidades para cada Integração. |
| **Sistema(s) Operacional(is):** | Windows 7 ou superior. |

## Descrição

Melhoria realizada no adapter de integração de Consulta Saldo em Estoque (mensagem única STOCKLEVEL), para que seja retornado o custo médio e custo unitário de um serviço quando não existir controle de estoque dos serviços.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.22.179* deste chamado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **RM**, acesse **Integração/Mensagem Única/Transformação**. Selecione o registro de **Identificador** igual a **STOCKLEVEL**e realize as seguintes ações:  
   1. Edite o registro e no campo **DataServer** clique sobre o link.
   2. Ao abrir a janela de **Cadastro de códigos fontes** clique em excluir.
2. No **RM**, acesse **Integração/Mensagem Única/Integrações**. Abra o anexo **Mapeamento de Entidades** e realize as seguintes ações:
   1. Apague a Mensagem **STOCKLEVEL**
3. Retorne ao cadastro de **Transformação** e exclua a transformação ****STOCKLEVEL.****
4. No **RM**, acesse **Integração/Ferramentas/Configurar**.
   1. Na janela **Assistente de Configuração de Integração** avance para a etapa **Configuração do banco de dados** e informe Usuário e Senha supervisor. Teste a conexão e avance.
   2. Na etapa **Projetos de Integração** selecione o item **Manutenção de Ativos x BackOffice RM**, avance e execute o assistente.

## Procedimento para Utilização

A mensagem STOCKLEVEL é utilizada sempre que for necessário realizar alguma Solicitação para atender uma Ordem de Manutenção do módulo Manutenção de Ativos do Protheus (SIGAMNT). Iremos detalhar abaixo a sua utilização em uma ordem de serviço corretiva.

1. No Manutenção de Ativos (SIGAMNT), acesse Atualizações  / Controle de Oficina / Ordens de Serviço / Corretiva
   1. O sistema apresenta a janela de O.S. Corretiva.
2. Clique em Incluir
   1. O sistema apresenta a janela de seleção de Filiais. Selecione uma filial.
3. Na janela O.S. Corretiva informe os dados obrigatórios que são solicitados.
4. Clique no botão Insumos
   1. O sistema apresenta a janela Insumos - O.S. Corretiva
5. Posicione o cursor e realize informe dados nas seguintes colunas:
   1. Tipo Insumo: P-Produto
   2. Código do Produto
   3. Quantidade
   4. Destino
6. Posicione o cursor na segunda lina e informe:
   1. Tipo Insumo: M-Mão de Obra
   2. Código do Produto
   3. Quantidade
7. Na janela O.S. Corretiva altere a Situação para Liberado
8. Confira os dados e confirme.
