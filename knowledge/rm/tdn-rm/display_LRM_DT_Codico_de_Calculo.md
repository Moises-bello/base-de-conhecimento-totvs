---
content_hash: d5f982bba40ab5e898e05bfcd4d8f6531315a02d7823c8774fa74fe9eb5c5cb9
fetched_at: '2026-06-29T00:06:14.672150+00:00'
page_id: '210048529'
product: rm
source: tdn-rm
title: DT_Codico_de_Calculo
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Codico_de_Calculo
version: 3
---

# CÓDIGO DE CÁLCULO

## Características do Requisito

  

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *-* | **Melhorias no código de cálculo** | |
| **Versões/Release:** | *12.1.5* |

## Descrição

O usuário pode customizar os tipos de ocorrências de presença e ausência do horário do funcionário, onde ao calcular seu ponto ou realizar compensação do banco, o usuário consiga visualizar o total de cada ocorrência customizada, seja no banco de horas ou no movimento.

## Procedimento para Utilização

O usuário pode cadastrar os tipos de ocorrências customizados específicos ao seu escopo

**Obs.:** Os tipos de ocorrência internos são disponibilizados apenas para visualização, não é possível realizar nenhum tipo de operação, visando à estabilidade do cálculo.

Ex.: de tipo de ocorrência interna (A – Atraso, F – Falta, EN – Extra Normal,...)

## **Cadastro de Eventos**

Com a criação do cadastro de Tipo de Ocorrência, o usuário pode vincular seus tipos customizados ao código de cálculo 0043.

Débito ou Crédito: Se o código de cálculo do evento é de crédito ou débito. Essa informação é importante para definir a atitude do evento: pagar, descontar ou compensar, para o movimento e para o banco de horas.

## Eventos – Parametrizador Sindicato

Para que os eventos com código de cálculo 0043 sejam lançados para o banco de horas,é necessário definir sua atitude e mapeá-lo nos parâmetros do Sindicato. Portanto o usuário irá marcar a atitude do evento, conforme imagem abaixo:

Na associação dos eventos no parametrizador do sindicato, são  informadas as formas de definição de totalização para os eventos com código de cálculo 0043:

Uma validação no parametrizador garante que os eventos não estejam com faixas sobrepostas. Caso o evento esteja, não será possível cadastrá-lo.

Exemplo: Extra Fixa Faixa 1 = Inicial = 0h Final = **5h**; Extra Fixa Faixa 2 = Inicial = **4h** Final = 10 

## Cadastro de Horário por Intervalo

Com o cadastro de Tipo de Ocorrência,  o usuário tem a possibilidade de definir qual tipo de ocorrência será gerado para presença e ausência, para cada intervalo planejado da jornada de trabalho.

 

## Cadastro de Horário por Jornada

O usuário pode definir qual tipo de ocorrência será gerado para presença e ausência, para cada montante de horas de acordo com a quantidade de batidas.

Gestão do Banco de Horas

 Com a evolução do cadastro de eventos, onde o usuário define se o código de cálculo 0043 é débito ou crédito, é possível totalizar e compensar os novos tipos de ocorrência cadastrados pelo usuário.

 As seguintes rotinas passarão a apresentar essas novas informações:

• Compensação/Lançamento do Banco de Horas; É possível definir a atitude desses eventos: pagar, descontar, compensar.

 • Banco de Horas detalhado; Foi incluída uma coluna para mostrar se o evento é de débito ou crédito.

 • Histórico do Banco de Horas

 • Saldo do Banco de Horas

## Abono

Com a  parametrização do cadastro de Tipo de Ocorrência, é possível definir se os tipos criados pelo usuário são abonáveis ou não; assim a validação para o lançamento de abono será se o tipo de ocorrência é abonável, e não mais se é falta ou atraso.

## Cálculo

A máquina de cálculo passa a gerar ocorrências de tipos cadastrados pelo usuário, através do código de cálculo 0043. Os eventos irão ser vinculados no sindicato, e o cálculo irá considerá-los ao gerar as ocorrências calculadas, e lançá-las para o banco de horas ou para o movimento.  
Com a possibilidade de cadastrar faixas para os eventos de código de cálculo 0043, o cálculo irá considerar o montante de faixa do evento, assim como considera as faixas de extras no sindicato.

## Visualização de Ocorrências Calculadas no RM Portal

Os tipos de ocorrência cadastrados pelo usuário podem ser visualizados. Essa visão está disponibilizada no Portal para os usuários.

## Configuração do Espelho

O usuário pode criar colunas customizadas, e pode vincular as ocorrências que desejar à coluna. Cada coluna totalizará as ocorrências vinculadas a ela:

**RM Chronus**

****Nova MDI****

******Configuração do Espelho******

**Coluna do Espelho**

**Tipos de Ocorrência**

## Espelho RM Portal

melhorias no espelho do cartão do portal.

## Espelho Winforms

Melhorias no espelho do cartão winforms, onde o usuário consegue visualizar   
• Totais do dia   
• Ocorrências, onde o usuário pode visualizar os tipos de ocorrência cadastrados, junto com sua atitude.  
• Movimento Diário, onde o usuário pode visualizar o código de cálculo 0043 no movimento diário.  
• Movimento, onde o usuário pode visualizar o código de cálculo 0043 totalizado no movimento.  
• Banco de horas, onde o usuário pode visualizar código de cálculo 0043 que foi lançado ou compensado.  
• Saldo banco de horas analítico, onde o usuário pode visualizar o saldo do banco de horas pelo código de cálculo 0043.
