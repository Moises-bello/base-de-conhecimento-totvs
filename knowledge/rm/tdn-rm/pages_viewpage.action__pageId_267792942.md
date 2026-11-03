---
content_hash: 63f6a8ad999041e28aa45e16dc62ccb37393af28d1224c30bf17e45a17a30dff
fetched_at: '2026-06-29T00:08:19.559490+00:00'
page_id: '267792942'
product: rm
source: tdn-rm
title: ER_SAUHRM02-50_Transferir paciente entre UNIDADES + Configuração PEP ("Unidades
  AMIGAS")
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=267792942
version: 110
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | Saúde |
| **Projeto** | SAUHRM02 | **IRM** | SAUHRM02-67 |
| **Requisito** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-42 | **Subtarefa** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-50 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

 Este documento tem como objetivo especificar o requisito de mover os itens de uma requisição de estoque para uma nova requisição com novo local de estoque e centro de custo quando o paciente for transferido de unidade para outra e estas unidades de atendimento forem compatíveis. 

## Definição da Regra de Negócio

#### RN001

1. Ao fazer a transferência de um paciente de um leito para outro será incluída uma rotina para verificar se estas unidades são compatíveis.
2. Em caso afirmativo (unidades de atendimento compatíveis), será verificado o local de estoque e centro de custo de ambas as unidades.
3. Caso seja o mesmo local de estoque a movimentação de estoque será atualizada pelo centro de custo da unidade de destino.
4. Se as unidades não forem do mesmo local de estoque, há a necessidade de transferir os itens pendentes de uma prescrição para uma nova movimentação de estoque no novo local de estoque da nova unidade de atendimento que consta o paciente.
5. Os itens da movimentação de estoque antiga serão suspensos pois foram transferidos. Os itens da prescrição corrente agora serão aplicados ao paciente sendo dispensados de outro local de estoque pela nova requisição gerada.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Mudança de Leito | Envolvida | Atendimento / Internação / Mudança de Leito | **RN001** |

#### Exemplo de Aplicação

1. Acesse o RM Saúde.
2. Acesse o menu **Atendimento / Internação / Mudança de Leito.**
3. Clique em **Incluir** e selecione um paciente.
4. Preencha os dados necessários e selecione o novo leito.
5. Ao gravar, será verificada a unidade de atendimento do novo leito.
6. Se forem compatíveis e de locais de estoque diferentes será criada uma nova movimentação de estoque com os itens pendentes da anterior.
7. Se forem compatíveis e de mesmo local de estoque, a movimentação de estoque será atualizada pelo centro de custo.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
