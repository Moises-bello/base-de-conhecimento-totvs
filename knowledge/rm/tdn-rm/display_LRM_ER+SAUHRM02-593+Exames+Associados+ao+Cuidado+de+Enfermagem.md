---
content_hash: a211e7d7a8056ee6bff9b4e909335ef20d3a37bf4fb65c3bfc69882209828c8e
fetched_at: '2026-06-29T00:08:27.979482+00:00'
page_id: '271652496'
product: rm
source: tdn-rm
title: ER SAUHRM02-593 Exames Associados ao Cuidado de Enfermagem
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+SAUHRM02-593+Exames+Associados+ao+Cuidado+de+Enfermagem
version: 9
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Prontuário |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAUHRM02 | **IRM/EPIC1** | SAUHRM02-346 |
| **Requisito/Story/Issue1** | SAUHRM02-593 | **Subtarefa1** | SAUHRM02-611 |
| **Chamado/Ticket2** | 197618 | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Permitir que seja possível associar exames aos cuidados de enfermagem, para tratar os casos de teste de glicemia capilar, onde é necessário ter pedidos de exames a cada horário prescrito.

### (Obrigatório)

## Definição da Regra de Negócio

Ao prescrever o cuidado "Medição de taxa glicêmica" de 4 em 4 horas, o sistema deverá solicitar o exame "Glicemia de dextro" na mesma frequência. Para cada horário um novo pedido deve ser aberto.

Na Prescrição Médica do módulo do Prontuário, quando o médico prescrever um cuidado e este tiver um exame associado, o sistema deverá abrir um pedido de exame para cada horário. No caso de convênio que fatura TISS, o sistema deve lançar na mesma guia a quantidade de exames permitidos.

Para esta implementação, serão descritas as regras de negócio abaixo:

**RN01: Vínculo de exames ao Item de Enfermagem**

No menu Cadastros/Cuidados com o Paciente/Prescrição Médica/Itens de Enfermagem, criar um cadastro anexo somente para o tipo "Prescrição de Enfermagem" cujo campo TIPOITEM é igual a 4.

Este cadastro deve possuir os seguintes campos:

* O  código de exame associado (FK para a tabela SZLABEXAME)
* O código do item de enfermagem (FK para a tabela SZPEPENFERMAGEM)

Para este cadastro criar a tabela SZPEPENFSADT e as seguintes colunas:

* CODCOLIGADA do tipo smallint
* ID  do tipo inteiro (Sequencial da tabela)
* IDITEMENF do tipo inteiro

**RN02: Vínculo do Cuidado com o Item de enfermagem**

No menu "Cadastros/Cuidados com o Paciente/Prescrição Médica/Cuidados e Procedimentos com o Paciente/Dieta", o cuidado que é prescrito pelo médico deve estar vinculado o item de enfermagem do tipo 4 (Prescrição de Enfermagem). 

Neste caso o campo SZCUIDADOPROC.IDITEMENF deve estar preenchido e o **Cuidado** deve estar **ativo** para que ocorra o correto funcionamento desta implementação.

**RN03: Prescrição do Cuidado e **Geração dos Pedidos de Exames****

Na funcionalidade da Prescrição Médica dentro do Prontuário, após o médico clicar no botão "**Cuidados**" ou digitar na "**Pesquisa Rápida"** um cuidado do tipo "Cuidados e Procedimentos" e concluir a Prescrição, o sistema deve verificar as seguintes condições:

1. Verificar se o item é um cuidado (RN01)
2. Verificar se existe um item de enfermagem associado (RN02)
3. Se existir, deve verificar se este item de enfermagem é do tipo 4 (Prescrição de Enfermagem)
4. Se for do tipo 4, deve verificar se existem exames associados  a ele
5. Se existir exame associado, o sistema deve gerar os pedidos de exames

Criar a rotina GeraPedidoAssociadoAoCuidado() que faça as validações acima e que tratará da geração dos pedidos de exames.

Esta rotina deverá gerar o número de pedidos de acordo com a frequência prescrita para o cuidado, ou seja, se o sistema gerou 4 horários, a rotina gerará 4 pedidos de exames. Neste ponto deve-se atentar para a quantidade de exames que podem ser incluídos numa mesma guia TISS. Esta rotina deve verificar se o convênio fatura TISS e controlar a geração do número da guia. Por exemplo, se numa guia podem ter 3 exames, o sistema deve gerar 3 pedidos com o mesmo número de guia e depois gerar mais um número de guia e incluir o exame restante nesta nova guia.

Para criar o pedido, deve-se utilizar o método CriaPedidoExame da classe TPedidoExame, sendo a data e hora do pedido igual à data de cada aprazamento.

O número do guia deve ser gerado a partir do método getNumGuia que está presente na Unit SAdPedidoExamePEP.

A inclusão do exame deve ser feita pelo método SolicitaExame da mesma classe do Pedido (TPedidoExame). É neste método que deve ser passado o número da guia corretamente.

Para cada exame solicitado deverá ser gravado na nova tabela SZRELPRESCPEDIDO o relacionamento entre o item prescrito e o pedido gerado. É através desta tabela que um pedido será cancelado quando o cuidado for suspenso. Nesta tabela deverá ser gravado a data/hora do aprazamento.

Após a geração de todos os pedidos, deve-se gerar as amostras de cada pedido através do método GestaoAmostra da classe TPedidoExame, para que a gestão do módulo de Unidade de Diagnósticos funcione corretamente.

Para que as integrações dos pedidos de exames com sistemas terceiros siga corretamente, é necessário executar a rotina ExecutaIntegracaoSADT().

**RN04: Suspensão do Cuidado**

Na prescrição médica, quando o médico suspender um item, criar a rotina TrataSuspensaoDeCuidado() e utilizar o mesmo método que valida as condições da RN03. Satisfazendo as condições, verificar na tabela SZRELPRESCPEDIDO os itens que devem ser suspensos/cancelados.

A consulta para verificar quais itens devem ser cancelados é a seguinte:

SELECT SZPEDEXAMEITEM.ORDEMSERVICO, SZPEDEXAMEITEM.CODEXAME, SZPEDEXAMEITEM.SEQEXAME, SZPEDEXAMEITEM.STATUS   
FROM SZPEDEXAMEITEM (NOLOCK) JOIN SZRELPRESCPEDIDO (NOLOCK)  
 ON SZPEDEXAMEITEM.CODCOLIGADA = SZRELPRESCPEDIDO.CODCOOLIGADA AND  
 SZPEDEXAMEITEM.ORDEMSERVICO = SZRELPRESCPEDIDO.ORDEMSERVICO AND  
 SZPEDEXAMEITEM.CODEXAME = SZRELPRESCPEDIDO.CODEXAME AND  
 SZPEDEXAMEITEM.CODEXAME = SZRELPRESCPEDIDO.CODEXAME  
WHERE SZRELPRESCPEDIDO.CODCOLIGADA = :CODCOLIGADA  
 AND SZRELPRESCPEDIDO.CODPRESCRICAO = :CODPRESCRICAO  
 AND SZRELPRESCPEDIDO.SEQUENCIAL = :SEQUENCIAL  
 AND SZRELPRESCPEDIDO.DATAAPRAZ >= :DATAAGORA

Para cada registro retornado, utilizar os métodos CancelaExame e ExcluiOutrasInfoExame da classe TPedidoExame.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [SauItemEnfermagemAction – Itens de Enfermagem] | [Alteração] | Cadastros -> Cuidados com o Paciente -> Prescrição Médica -> Itens de Enfermagem | RN01 |
| [SauCuidadoProcAction – Cuidados e Procedimentos com o Paciente/Dieta] | [Envolvida] | Cadastros -> Cuidados com o Paciente -> Prescrição Médica -> Cuidados e Procedimentos com o Paciente/Dieta | RN02 |
| [SadProntuarioEletronico – Prontuário] | [Alteração] | Prontuário | RN03, RN04 |

Tabelas Utilizadas

* ```
  SZPEPENFERMAGEM  - Itens e Enfermagem
  ```
* ```
  SZPEPENFSADT - Exames vinculados ao Item de Enfermagem
  ```
* ```
  SZCUIDADOPROC - Cadastro de Cuidados e Procedimentos da prescrição médica
  ```
* ```
  SZITEMPRESCRICAO – Itens da Prescrição médica
  ```
* ```
  SZRELPRESCPEDIDO – Exames solicitados a partir do cuidado
  ```

### Opcional

## Dicionário de Dados

**Arquivo ou Código do Script:**

Tabela: SZPEPENFSADT – Exames associados ao Item de Enfermagem

|  |  |  |
| --- | --- | --- |
| **Índice** | **Chave** | Tabela de Referência |
| **01** | CODCOLIGADA + SEQ (PK) |  |
| **02** | CODCOLIGADA + IDITEMENF (FK) | ``` SZPEPENFERMAGEM   ``` |
| **03** | CODCOLIGADA + CODEXAME (FK) | SZLABEXAME |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório** | **Descrição** |
| SZPEPENFSADT | CODCOLIGADA | Smallint |  |  | Sim (X) Não ( ) | Código da Coligada |
| SZPEPENFSADT | SEQ | Inteiro |  |  | Sim (X) Não ( ) | Sequencial |
| SZPEPENFSADT | IDITEMENF | Inteiro |  |  | Sim (X) Não ( ) | Id. Item de Enfermagem |
| SZPEPENFSADT | CODEXAME | Inteiro |  |  | Sim (X) Não ( ) | Código do Exame |

Tabela: SZRELPRESCPEDIDO – Cuidados que geraram pedidos de exames

|  |  |  |
| --- | --- | --- |
| **Índice** | **Chave** | Tabela de Referência |
| **01** | CODCOLIGADA + SEQ (PK) |  |
| **02** | CODCOLIGADA + CODPRESCRICAO + SEQUENCIAL (FK) | ``` SZITEMPRESCRICAO ``` |
| **03** | CODCOLIGADA + ORDEMSERVICO + CODEXAME + SEQEXAME (FK) | SZPEDEXAMEITEM |
| **04** | CODCOLIGADA + CODPRESCRICAO + SEQUENCIAL + DATAAPRAZ (Índice) |  |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório** | **Descrição** |
| SZRELPRESCPEDIDO | CODCOLIGADA | Smallint |  |  | Sim (X) Não ( ) | Código da Coligada |
| SZRELPRESCPEDIDO | SEQ | Inteiro |  |  | Sim (X) Não ( ) | Sequencial |
| SZRELPRESCPEDIDO | CODPRESCRICAO | Inteiro |  |  | Sim (X) Não ( ) | Código da Prescrição |
| SZRELPRESCPEDIDO | SEQUENCIAL | Inteiro |  |  | Sim (X) Não ( ) | Seq. do item prescrito |
| SZRELPRESCPEDIDO | ORDEMSERVICO | Inteiro |  |  | Sim (X) Não ( ) | Código do Pedido de exame |
| SZRELPRESCPEDIDO | CODEXAME | Inteiro |  |  | Sim (X) Não ( ) | Código do Exame |
| SZRELPRESCPEDIDO | SEQEXAME | Inteiro |  |  | Sim (X) Não ( ) | Sequencial do Exame |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
