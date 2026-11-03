---
article_id: 360036448014
category: Financeiro - Contabilização
content_hash: 330e46b8a0eef48a3c8c24e71590539badd54147a23fc0636d103f4b46622643
fetched_at: '2026-06-28T22:38:05.551619+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: MP - SIGAFIN - Contabilização do PCC pelos títulos aglutinadores ao invés dos
  títulos de impostos
type: support-article
updated_at: '2021-04-28T15:56:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036448014-MP-SIGAFIN-Contabiliza%C3%A7%C3%A3o-do-PCC-pelos-t%C3%ADtulos-aglutinadores-ao-inv%C3%A9s-dos-t%C3%ADtulos-de-impostos
---

**Dúvida**Como realizar a contabilização do PCC pelos títulos aglutinadores?  
  
 **Ambiente**Microsiga Protheus – Financeiro - FINA378 - A partir da versão 11.80  
   
**Solução  
Características do Requisito**

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Protheus |
| **Segmento:** | Serviços |
| **Módulo:** | Financeiro |
| **Rotinas:** |  |
| Rotina(s) envolvida(s)       Nome Técnico |
| **FINA378**                                  **Aglutinador** **Pis**, **Cofins** e **Csll** |
| **FINA050**                                **Contas a Pagar** |
| **FINA080**                                **Baixa a Pagar** |
| **Cadastros Iniciais:** | **Fornecedor** e **Natureza** com cálculo de **PCC** |
| **Parâmetro(s):** | **MV\_BX10925** = 1 |
|  |
| **MV\_CTBAGP** = .T. |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Todos |
| **Tabelas Utilizadas:** | **SA2** - **Fornecedor**; **SED** - **Natureza**; **SE2** - **Contas a Pagar** |
| **Sistema(s) Operacional(is):** | Todos |

**Descrição:**  
Criado o parâmetro **MV\_CTBAGP** na rotina **Contabilização Off-line** (**CTBAFIN**) para realizar a contabilização dos títulos dos impostos do **PCC** pelos aglutinados, caso sejam, ao invés de contabilizar pelo título original do imposto. Para isto o conteúdo precisa ser .T.

**Procedimento para Configuração:**  
  
**CONFIGURAÇÃO DE PARÂMETROS**

1. No **Configurador (SIGACFG)**, acesse **Ambientes/Cadastros/Parâmetros (CFGX017)**. Configure o(s) parâmetro(s) a seguir:

|  |  |
| --- | --- |
| Itens/Pastas | Descrição |
| **Nome:** | **MV\_CTBAGP** |
| **Tipo:** | Lógico |
| **Cont. Por.:** | Define se os títulos do PCC são contabilizados pelos seus aglutinados ou não |
| **Descrição:** | .T. |

## **Procedimento para Utilização**

       1.   No módulo **Financeiro** (**SIGAFIN**), acessar a rotina de cadastro de **Naturezas** (**FINA010**) em **Atualizações** > **Cadastros** > **Naturezas**;

O sistema apresenta a janela de naturezas cadastradas.

       2.    Incluir uma **Natureza** que calcule **PCC**, caso não exista. Configure os campos **ED\_CALCCSL**, **ED\_CALCPIS** e **ED\_CALCCOF** = 'Sim' e **ED\_PERCCSL**, **ED\_PERCPIS** e **ED\_PERCCOF** com suas devidas porcentagens;

       3.    No cadastro de **Fornecedor** em **Atualizações** > **Cadastros** > **Fornecedores**, incluir um **Fornecedor** com cálculo de **PCC** (**A2\_RECPIS**, **A2\_RECCOF** e **A2\_RECCSL** = 'Não');

       4.    Incluir dois títulos a Pagar para esse mesmo **Fornecedor** em **Atualizações** > **Contas a Pagar** > **Contas a Pagar** - opção 'Incluir');

Depois, realizar a baixa dos títulos para que as taxas sejam geradas.

       5.   Aglutinar os impostos pela rotina **Aglutinação Pis. Cof. e Csll** (**FINA378**) em **Miscelâneas** > **Recálculos** > **Aglutinação Pis. Cof. e Csll**);

       6.   Baixar os títulos aglutinados nesse processo;

       7.   **Contabilizar *Off* Line** (**CTBAFIN**) esse período (importante ter o LP 510 e todos os dados contábeis necessários (calendário, moeda, etc) devidamente cadastrados);

       8.            Note que os títulos aglutinadores são contabilizados corretamente.
