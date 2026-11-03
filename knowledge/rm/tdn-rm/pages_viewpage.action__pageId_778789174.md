---
content_hash: 6a9686a7e5d66fef97c434b49c774fafe064b42618914cc415c15a6915dfa2ad
fetched_at: '2026-06-29T00:11:37.894291+00:00'
page_id: '778789174'
product: rm
source: tdn-rm
title: Cópia de prescrição com ciclos alternados/horário para data futura (a partir
  da 12.1.2310)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=778789174
version: 7
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Funcionalidade**
3. **Exemplo de utilização**

Cópia de prescrição com ciclos alternados/horário para data futura (a partir da 12.1.2310)Visão Geral

## **01.****VISÃO GERAL**

A cópia de prescrição com ciclos alternados/horário para data futura possibilita o uso de frequências cujo intervalo de tempo entre os horários supera o tempo de vigência da nova prescrição.

Funcionalidade

## **02. FUNCIONALIDADE**

1. Não é necessário nenhuma configuração adicional.
2. A rotina de **[cópia de prescrição](https://tdn.totvs.com/pages/viewpage.action?pageId=615383235)**, após recalcular o horário de início para a nova prescrição, identificará se o novo horário trata-se de um horário vigente ou um horário futuro(ou seja, com horário de início **posterior** a data de validade da nova prescrição).
3. Caso o item copiado seja identificado como um horário futuro, o sistema permitirá que ele seja [**liberado**](https://tdn.totvs.com/pages/viewpage.action?pageId=619754712) mesmo tendo o seu horário de início posterior a data de validade da prescrição.
4. Caso a unidade de atendimento utilize a rotina de **[aprazamento/checagem](https://tdn.totvs.com/pages/viewpage.action?pageId=615383253)**, o item com horário futuro ficará disponível para visualização no painel de checagens sem a necessidade da liberação dos aprazamentos
5. **IMPORTANTE:** o item com horário futuro é utilizado apenas para fins de **controle/visibilidade** dentro do sistema, indicando a existência de um item a ser utilizado em data futura e permitindo que ele seja copiado para as novas prescrições intercalando os dias que deverá ser utilizado ou não.
Exemplo de utilização

## **03. EXEMPLO DE UTILIZAÇÃO**

1. Utilizando como exemplo um medicamento prescrito com a frequência de **48x48** horas, iniciando as **15:00**,para uma unidade de atendimento configurada com prescrições válidas por **1 dia(s),**das **13:00** às **12:59:**
2. Esse mesmo medicamento foi sendo copiado/liberado ao longo de 3 novas prescrições (**23/07/2023**, **24/07/2023** e **25/07/2023**) de maneira contínua e sem nenhuma alteração:
3. Por se tratar de uma frequência de **48x48** horas, é correto assumir que o medicamento deverá ser utilizado em dias alternados, ou seja:
   * **22/07/2023 às 15:00**
   * **23/07/2023** **não será utilizado**
   * **24/07/2023 às 15:00**
   * **25/07/2023 não será utilizado**
4. Visualizando todos os ciclos das prescrições no menu de [**aprazamento/checagem**](https://tdn.totvs.com/pages/viewpage.action?pageId=615383253), é possível verificar que o item está disponível em todos os eles, e informando nos dias/horários que **não será utilizado** que o horário trata-se de um **horário para data futura:**
