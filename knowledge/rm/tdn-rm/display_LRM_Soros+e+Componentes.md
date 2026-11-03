---
content_hash: df4548de1f32c78d1d2e851d6711c7250ec6a708ab03b4bea125933c245095eb
fetched_at: '2026-06-29T00:11:03.299680+00:00'
page_id: '620768603'
product: rm
source: tdn-rm
title: Soros e Componentes
type: documentation
url: https://tdn.totvs.com/display/LRM/Soros+e+Componentes
version: 15
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Fluxo de infusão opcional**

Soros e componentesVisão Geral

## **01. VISÃO GERAL**

Possibilidade de prescrever soros e componentes para o paciente através da prescrição médica.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

No submenu de soros e componentes, o usuário poderá prescrever soros e componentes para o paciente. Existe a possibilidade de prescrever soros e componentes separadamente.

       É possível configurar o campo de Soros e Componentes para exibir os princípios ativos.

       Quando ativada, a configuração mostra os princípios ativos entre parênteses após o nome do item.

É possível definir o modo de visualização do campo de soros e componentes para exibir princípios ativos, podendo ser ativado na seguinte configuração abaixo.

**Campos Obrigatórios:**

* Via: definição de via que será utilizada para aplicação.
* Tempo de infusão: definição em horas e minutos. Quando preenchido, realiza automaticamente o cálculo do campo "fluxo de infusão inicial".
* Fluxo de infusão inicial: esse campo considera dois cálculos, que dependem do campo de definição se gotas/min ou se ml/hora. Quando preenchido, realiza automaticamente o cálculo do campo "Tempo de infusão".
* Campo de definição com duas opções: gotas/min e ml/hora.
* Frequência do item.

**Outros Campos:**

* Horário de início.
* Tempo de uso: número (dias). Este campo deve considerar a duração do tratamento.
* Duração do tratamento: número (dias).
* Opção para exibir os horários após definição de frequência e horário.
* Campo para inserir observação.

A partir da **versão 2209** também é possível indicar se será **"À Critério Médico"** ou **"Se Necessário"**:

Ao clicar em incluir, os itens deverão ser carregados para dentro do menu de "Soros e Componentes".

No menu de "Soros e Componentes", deverá ficar descrito os componentes, unidades e quantidades.

**Atualização de Regra – Campo Fluxo em Soro e Componentes opcional   
[Soros e Componentes - Linha RM - TDN](https://tdn.totvs.com/display/LRM/Soros+e+Componentes#Sorosecomponentes-574745402)**

Fluxo de infusão opcional

## **03. Fluxo de infusão opcional**

Funcionalidade disponível a partir da versão 12.1.2602.

Em **Cadastros → Unidade de Atendimento → Aba de Prontuário Eletrônico → Prescrição Médica**, está disponível a configuração de **"****Fluxo opcional na prescrição de Soro e Componentes"**.

Essa configuração permite definir se o fluxo de infusão inicial será opcional na inclusão de Soros e Componentes.

Quando esse parâmetro estiver marcado, o preenchimento do campo passa a ser opcional e o sistema permite que o prescritor inclua o registro sem determinar um fluxo de infusão:

Quando esse parâmetro estiver desmarcado, o campo permanece como obrigatório para informar o fluxo de infusão:
