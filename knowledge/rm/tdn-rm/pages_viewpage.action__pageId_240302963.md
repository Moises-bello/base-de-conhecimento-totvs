---
content_hash: df593c69d6392ca4f7fe9dfe1fd20ab1e81d6a98b80f289fe135b9e898c5f7b1
fetched_at: '2026-06-29T00:08:10.185136+00:00'
page_id: '240302963'
product: rm
source: tdn-rm
title: ER_SAUHRM01-10_Revisão_dos_Tempos_de_Sala_e_Vínculo_Folha_de_Sala
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240302963
version: 116
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS HOSPITALAR | **Módulo** | RM SAÚDE |
| **Segmento Executor** | SAÚDE | | |
| **Projeto1** | SAUHRM01 | **IRM1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-6 |
| **Requisito1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-10 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM01-94 |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

    Esta especificação tem como objetivo detalhar a melhoria à ser implementada na funcionalidade 'Registro de Informações cirúrgicas'  visando verificar e validar o vínculo entre o tempo de sala,o tempo de anestesia, e o tempo de cirurgia. Além disso a melhoria engloba a funcionalidade de vincular a folha de sala automaticamente.

## Definição da Regra de Negócio

**RN001 -** As seguintes entradas de dados relacionadas ao tempo do Registro de informação cirúrgicas devem obedecer o respectivo enquadramento: O 'tempo de sala' deve ser maior que o 'tempo de anestesia' que deve ser maior que o 'tempo de cirurgia', conforme **Figura 01**.

**Figura 01 - Enquadramento dos tempos de sala/anestesia/cirurgia**

****RN002****- Quando houver apenas uma movimentação de estoque do tipo Folha de sala, o sistema vinculará ao registro de informação cirúrgica automaticamente.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Registro de informação cirúrgica | [Alteração] | Cuidados com Paciente > Registro de informação cirúrgica > [Selecionar registro] > Aba Identificação | RN001 |
| Registro de informação cirúrgica | [Alteração] | Cuidados com Paciente > Registro de informação cirúrgica > [Selecionar registro] > Aba Folhas de Sala | RN002 |

***Exemplo de Aplicação:***

* *No caso do usuário atribuir um tempo de anestesia maior que o tempo de sala, o sistema irá informar que o tempo de sala deve ser maior que o tempo de anestesia.*
* *No caso do usuário já ter um movimento de estoque do tipo Folha de sala para a respectiva conta do registro de informação cirúrgica e esse movimento for o único que pode ser associado, o sistema irá associar automaticamente.*

***Tabelas Utilizadas***

* *SZREGINFCIRURGIA - Registro Inf. Cirurgia*
* *SZMOVIESTOQUE - Movimentacao de estoque*

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
