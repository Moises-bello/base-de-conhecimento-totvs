---
content_hash: 800ac252aeeead4b84ebe0084823e2598b89e9fa3d8dbc16ea58362a94a22ea5
fetched_at: '2026-06-29T00:06:19.939464+00:00'
page_id: '221545817'
product: rm
source: tdn-rm
title: ER_PCREQ-8790_Definicao_de_Municipios_para_Recolhimento_de_Impostos_sem_a_Necessidade_de_se_Definir_um_Percentual
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8790_Definicao_de_Municipios_para_Recolhimento_de_Impostos_sem_a_Necessidade_de_se_Definir_um_Percentual
version: 142
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP009 | **IRM1** | PCREQ-8788 |
| **Requisito1** | PCREQ-8790 | **Subtarefa1** | PDR\_CP\_TOP009-46 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |
| **Integração** **Protheus** | Não se aplica | | |

## Objetivo

O Objetivo desta especificação é demonstrar abaixo como será implementado o cadastro de município sem obrigatoriedade de informar um percentual, no intuito de restringir esta informação no rateio de estado e município.

## Definição da Regra de Negócio

Foi realizado pelo comitê de inovação, uma análise de mercado para identificar a necessidade de melhorias nos módulos do TOTVS Obras e Projetos. Durante esta análise foi identificado a necessidade de se modificar o cadastro de estado e município no módulo de contrato.

Em alguns contratos existe a necessidade de se realizar medição por trecho, que  consiste na criação de um rateio por estado/município para as medições de períodos de contratos onde, ao serem faturados, os impostos sejam apurados corretamente para cada estado/município, ou seja, cada município terá a emissão do faturamento em separado.  

Os usuários sentiram a necessidade na medição de contrato informar no rateio de estado/município, apenas os estados e municípios cadastrados no anexo de Estado e Município, sendo assim, ao se cadastrar um estado e município para o contrato as medição relativas a este contrato terão a opção de rateio de estado/município filtradas.

Para esta implementação é necessário criar um campo check (% informado na medição) no anexo de estado/município de contrato, que terá a função de filtrar os estados/municípios na medição do período do contrato. Caso o usuário cadastre o estado/município para a medição não marcando o novo check, o TOTVS Obras e Projetos não mudará o comportamento nas medições, o sistema irá exibir para o usuário todos os estados e municípios que farão parte do rateio. Mas caso o usuário cadastre o estado/município e selecione o check de *% informado na medição* os dados serão filtrados no momento de inclusão do rateio especifico na medição. (Protótipo 1) 

Quando o usuário define os estados e municípios que serão filtrados na medição através do check, o TOTVS Obras e Projetos não listará os estados e municípios no grupo "Rateio Default" vide protótipo 2, serão exibidos apenas rateios com percentual padrão cadastrado. Os estados e municípios não estarão no grupo "Rateio Default", pois quando o check é marcado o percentual de rateio é zero, assim o usuário precisará informar qual será o percentual de rateio do estado e município.

Esta melhoria também estará implementada no ambiente TOTVS HTML, na medição de contrato. (protótipo 03)

## Protótipo de Tela

**Protótipo 01**

**Protótipo 02**

****Protótipo 03****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
