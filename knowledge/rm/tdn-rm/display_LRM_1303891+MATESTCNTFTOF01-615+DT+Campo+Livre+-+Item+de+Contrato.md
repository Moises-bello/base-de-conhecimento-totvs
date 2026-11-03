---
content_hash: 933ca78bc25f53c36c6ee4155e5281c43e20213f9fd55d7f84dc06d9896ddd9d
fetched_at: '2026-06-29T00:08:43.238286+00:00'
page_id: '301199730'
product: rm
source: tdn-rm
title: 1303891 MATESTCNTFTOF01-615 DT Campo Livre - Item de Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/1303891+MATESTCNTFTOF01-615+DT+Campo+Livre+-+Item+de+Contrato
version: 96
---

# ITEM DE CONTRATO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Itens de Contrato. | CtrItmCntAction. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Contrato. | CtrCntAction. | |
| **Cadastros Iniciais:** | Antes de iniciar o uso do módulo de Manutenção de Contratos é importante que o sistema esteja devidamente parametrizado e as tabelas utilizadas na elaboração do contrato sejam cadastradas.  Parâmetros de Contrato: <http://wikihelp.totvs.com.br/WikiHelp/EST/EST.Contratos.aspx>  Tabelas de Contrato: <http://wikihelp.totvs.com.br/WikiHelp/EST/EST.TabelasContratos.aspx> |
| **Parâmetro(s):** | Campos Opcionais do Item de Contrato. |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | TITMCNT - Itens de Contrato. |
| **Sistema(s) Operacional(is):** | Windows 7 Service Pack1 e superiores. |

## Descrição

Permitir aos usuários do módulo de Contratos, informar dados alfanuméricos nos campos opcionais do item de contrato.

**Observação: *os campos livres do item de contrato não serão copiados para o item de movimento ao Faturar um Contrato.***

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do Atualizador de Base de Dados TOTVS RM versão 12.1.19.

1. Aplique a BibliotecaRM - 12.1.19.1.
2. Execute o Atualizador de Base de Dados TOTVS RM

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Gestão de Estoque, Compras e Faturamento**, acesse **Ambiente >> Parâmetros >> Gestão de Estoque, Compras e Faturamento >> 04.05 - Contratos >> 04.05.03 - Campos Opcionais**. Configure em **Campos Opcionais 1/2**o(s) parâmetro(s) de **Item** a seguir:
   1. Campo Livre 1
   2. Campo Livre 2

## Procedimento para Utilização

1. No Gestão de Estoque, Compras e Faturamento, acesse Contratos / Manutenção de Contratos.

O sistema apresenta a janela de Filtros - Contratos. Selecione uma opção de filtro.

2. Posicione o cursor em um contrato e clique em Editar.

O sistema apresenta a janela de edição de Contratos.

3. Na pasta Itens selecione um item de contrato e clique em Editar.

O sistema apresenta a janela de edição de Item de Contrato.

4. Na pasta Informações Adicionais/Observações informe os dados nos campos opcionais definidos nos parâmetros de Contrato.

5. Confira os dados e confirme.

divs
