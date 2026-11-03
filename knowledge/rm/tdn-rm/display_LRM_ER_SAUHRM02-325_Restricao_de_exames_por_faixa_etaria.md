---
content_hash: a049e19604c55f3a3487ab42ff6126659c874849e7146018bc09c8f6f6bcac0c
fetched_at: '2026-06-29T00:08:23.355484+00:00'
page_id: '270081041'
product: rm
source: tdn-rm
title: ER_SAUHRM02-325_Restricao_de_exames_por_faixa_etaria
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_SAUHRM02-325_Restricao_de_exames_por_faixa_etaria
version: 113
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Unidade de Diagnóstico |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAUHRM02 | **IRM1** | SAUHRM02-346 |
| **Requisito1** | SAUHRM02-325 | **Subtarefa1** | SAUHRM02-370 |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Esta implementação tem  como objetivo, solucionar a questão de que determinados exames não podem ser realizados em alguma faixa etária.

### (Obrigatório)

## Definição da Regra de Negócio

**RN01: Cadastro das faixas etárias não permitidas para o exame**

Disponibilizar um cadastro anexo ao cadastro de exames. Este cadastro devem conter apenas as faixas em que o exame selecionado não poderá ser realizado. As faixas serão vinculadas ao sexo do paciente para solucionar casos em que as faixas são diferentes por sexo.

O cadastro deve possuir os seguintes campos:

* Lookup para a faixa etária
* RadioGroup para a escolha do sexo, possuindo as opções: Ambos, Feminino e Masculino

**RN02: Validação**

A regra para a validação é a seguinte:

* com o código de exame a ser lançado, verificar se existe alguma faixa cadastrada
  + Se existir, verificar a unidade da faixa para que a idade do paciente seja convertida na mesma unidade
    - Se a idade do paciente estiver dentro da faixa, não permitir o lançamento deste exame.
    - Verificar a condição acima para todas as faixas cadastradas para o exame
  + Se não existir, permitir o lançamento do exame no pedido

A validação deve ser feita nas seguintes partes do sistema:

* Pedido de exames para pacientes internos
* Pedido de exames para pacientes externos
* PEP, Avaliações Complementares
* PEP 2.0 ao integrar com o RM
* Agendamento de exames simples, quanto no Wizard de agendamento de exames

[]

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Restrições por faixa etárias | [Alteração] | Cadastros ->  Unidades de Diagnóstico -> Exames e Serviços | RN01 |
| Pedido de Exames para pacientes internos | [Alteração] | Unidades Diagnóstico | RN02 |
| Pedido de Exames para pacientes externos | [Alteração] | Unidades Diagnóstico | RN02 |
| Avaliações Complementares | [Alteração] | Prontuário | RN02 |
| Prescrição médica | [Envolvida] | PEP 2.0 | RN02 |
| Agenda de Atendimentos | [Alteração] | Atendimento -> Agendamento | RN02 |
| Agenda de exames | [Alteração] | Atendimento -> Agendamento | RN02 |

**Tabelas Utilizadas**

* SZEXAMERESTRIDADE – Restrição de  exames por faixa etária

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
