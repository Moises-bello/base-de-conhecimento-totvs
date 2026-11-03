---
content_hash: 08bc5c6ae5973afd6e86945a8cb185d13c0f636b05c83a06478cda904c715363
fetched_at: '2026-06-29T00:08:22.719077+00:00'
page_id: '269439162'
product: rm
source: tdn-rm
title: ER_SAUHRM02-331_Avaliações_complementares_PEP_com_kit_de_lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269439162
version: 119
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM02 | **IRM** | SAUHRM02-346 |
| **Requisito** | SAUHRM02-331 | **Subtarefa** | SAUHRM02-432 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

 

### Objetivo

*Este documento tem como objetivo especificar o uso de grupos de exames nas solicitações pelo Prontuário do Paciente. A rotina existente até o momento tem o problema de utilizar os itens de débito para cadastrar os exames que pertencem a um grupo (Kits de lançamento com o atributo Utilizado no PEP marcado). Como alguns itens de débito podem pertencer a mais de um exame, na rotina dentro do PEP, são exibidos exames que não pertencem ao kit selecionado. O objetivo é utilizar o cadastro de Classificação de exames para montar o kit de exames sem a repetição ou o surgimento de exames não desejados.* 

 

## Informações Gerais

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR | **Módulo** | RM Saúde |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM02 | **IRM** | SAUHRM02-346 |
| **Requisito** | SAUHRM02-331 | **Subtarefa** | SAUHRM02-432 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

 

### Objetivo

*Este documento tem como objetivo especificar o uso de grupos de exames nas solicitações pelo Prontuário do Paciente. A rotina existente até o momento tem o problema de utilizar os itens de débito para cadastrar os exames que pertencem a um grupo (Kits de lançamento com o atributo Utilizado no PEP marcado). Como alguns itens de débito podem pertencer a mais de um exame, na rotina dentro do PEP, são exibidos exames que não pertencem ao kit selecionado. O objetivo é utilizar o cadastro de Classificação de exames para montar o kit de exames sem a repetição ou o surgimento de exames não desejados.*

### Definição da Regra de Negócio

RN001 - Criar um campo no cadastro de Classificação de Exames, para indicar quais exames serão utilizados na solicitação de exame do PEP. Somente essas classificações serão considerados na combo de “Padrão Propedêutico”. Os exames cadastrados nesta classificação serão os que serão solicitados. Com o uso deste cadastro, o usuário não precisará desmarcar itens que não pertencem ao grupo selecionado.

RN002 – Criação do parâmetro ‘Utiliza Classificação de Exames no PEP’. O valor default para este parâmetro deve ser igual a ‘F’, indicando a não marcação do mesmo. Caso o cliente opte por utilizar o cadastro de Classificação de Exames, ele deve marcar o novo parâmetro. A alteração deve ocorrer na combo Padrão Propedêutico: quando o parâmetro não estiver marcado, o sistema deve continuar igual. Com o parâmetro marcado, o conteúdo desta combo deve ser alterado para o cadastro de Classificação de exames. Ao clicar no botão para listar os exames, se o parâmetro estiver marcado, os exames a serem listados serão os da cadastro de “Classificação de exames”.

RN003 - No Prontuário, na aba Avaliações Complementares, solicitação de exames será mostrado somente os exames que forem vinculados ao cadastro do regra de negócio RN001 caso o parâmetro da regra de negócio RN002 esteja desmarcado, caso contrário, o comportamento segue o mesmo.

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Classificação de Exames | [Criação] | Cadastros\ Unidade de Diagnóstico \ Classificação de Exames | RN001 |
| Parâmetros Gerais | [Alteração] | Opções\Parâmetros\ Parâmetros Gerais | RN002 |
| Avaliações Complementares - Solicitação de Exames | [Criação] | Prontuário | RN003 |

Tabelas Utilizadas

* SZCLASSEEXAME - Classificação de Exames
* SZGRUPOEXAMES – Exames pertencentes à Classificação de exames
* SZKITLANC – Kit de lançamentos
* SZKITLANCITEM – Itens do kit

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
