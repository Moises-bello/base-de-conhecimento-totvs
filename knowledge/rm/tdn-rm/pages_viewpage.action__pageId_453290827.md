---
content_hash: 1f08ed05904ae1769f5f9e4fee3fed79dbd52f2be458ce0aaa96add1b2ea800c
fetched_at: '2026-06-29T00:10:11.846138+00:00'
page_id: '453290827'
product: rm
source: tdn-rm
title: '4584363 MATESTCNTFTOF01-4436 DT TOTVS Manutenção de Ativos x BackOffice RM
  - #REQUEST 1.010'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=453290827
version: 4
---

# BUSCAR SÉRIE PRINCIPAL NO TIPO DE MOVIMENTO DE SA/SC

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | BackOffice RM. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Solicitação de Armazém / Solicitação de Compras. | MovMovimentoTBCAction. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Movimento. | MovMovimentoTBCAction. | | Parâmetros Tipos de Movimento. | RMSParamsWizardAction. | | Configurador de Integrações. | ConConfiguraIntegracaoAction. | | Transformação. | ConTransformacaoAction. | |
| **Parâmetro(s):** | Parâmetros do Tipo de Movimento | Etapa Mov - Identificação | Séries. |
| **Tickets relacionados** | 4584363. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATESTCNTFTOF01-4436. |
| **País(es):** | Brasil. |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | TTMVEXT - Tipos de movimento.  TITMMOV - Itens de Movimento.  HCTRANSFORMACAO – Transformação Mensagem Única TOTVS.  HCMAPAINTEGRACAO – Tabela de mapeamento das entidades para cada Integração. |
| **Sistema(s) Operacional(is):** | Windows 7 ou superior. |

## Descrição

Melhoria realizada na mensagem Request para que ao gerar a Solicitação de Armazém / Solicitação de Compras o sistema sempre irá buscar a série principal parametrizada no tipo de movimento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.22.172* deste chamado.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **RM**, acesse **Integração/Mensagem Única/Integrações**. Abra o anexo **Mapeamento de Entidades** e realize as seguintes ações:
   1. Mensagem **REQUEST**: edite o registro, no campo **Eventos**clique sobre o link e ao abrir a janela de **Cadastro de códigos fontes** clique em excluir. Após, exclua o mapeamento REQUEST 1.010.
2. No **RM**, acesse **Integração/Ferramentas/Configurar**.
   1. Na janela **Assistente de Configuração de Integração** avance para a etapa **Configuração do banco de dados** e informe Usuário e Senha supervisor. Teste a conexão e avance.
   2. Na etapa **Projetos de Integração** selecione o item **Manutenção de Ativos x BackOffice RM**, avance e execute o assistente.
3. No módulo de **Gestão de Estoque, Compras e Faturamento** acesse os parâmetros do Tipo de Movimento de SA/SC | Mov - Identificação | Informar a Série Principal:
