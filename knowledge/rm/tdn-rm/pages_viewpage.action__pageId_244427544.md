---
content_hash: f26d642d185f48e6f6ff25b7f7418b984b2a62c58a1af091a779c29283c129c9
fetched_at: '2026-06-29T00:08:13.569591+00:00'
page_id: '244427544'
product: rm
source: tdn-rm
title: ER_SAUHRM01-537_Migração_Utilitário_Atualização_de_preço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244427544
version: 114
---

**Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.**

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | Saúde |
| **Projeto** | SAUHRM01 | **IRM** | SAUHRM01-404 |
| **Requisito** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-405 | **Subtarefa** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-537 |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

Este documento tem como objetivo especificar o requisito de Migração - Utilitário Atualização de preço, onde a rotina reescrita e disponibilizada na nova MDI do sistema.

## Definição da Regra de Negócio

**RN001**

1. Através desta migração a rotina de Atualização de Valores, será transformada em um processo (*wizard)*do TOTVS Gestão Hospilar.
2. No processo de Atualização de Valores, ao selecionar Materiais e Medicamentos é possível selecionar caso deseja-se atualizar além dos valores dos itens, os códigos específicos do mesmo.
3. Pode-se selecionar também Taxas e Serviços para atualização de valores e Diárias.
4. A atualização de valores pode se dar por **Remessa** específica ou por **Contas.**
5. Se a opção **Contas** é selecionada, pode-se definir se a atualização se aplicará em contas **Em Elaboração,**ou somente nas contas **Liberadas** ou em ambas as opções.
6. Pela opção **Contas**deverá ser informado também um período de datas de início e fim para as parciais a serem atualizadas.
7. Para iniciar o processo de Atualização de Valores é necessário informar uma **Unidade de Faturamento** e **Convênio.**
8. Nesta migração foram incluídas as opções de atualização de **Exames** e **Honorários** que seguirão a mesma lógica das opções citadas anteriormente.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Atualização de Valores | Criação | Faturamento > Atualização de Valores | **RN001** |

**Exemplo de Aplicação**

1. Acessar a nova MDI.
2. Acessar menu **Faturamento > Atualização de Valores**
3. Informe os tipos a serem atualizados (Taxas e Serviços, Diárias, Exames, Honorários, Materiais e Medicamentos).
4. Informe se deseja atualizar uma remessa específica ou somente por contas em elaboração, ou somente liberadas ou ambas.
5. Informe um intervalo de datas desejado.
6. Informe uma unidade de faturamento.
7. Informe um convênio e clique em **Processar.**
8. Ao final do processo os itens deverão ter sido atualizados com sucesso.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
