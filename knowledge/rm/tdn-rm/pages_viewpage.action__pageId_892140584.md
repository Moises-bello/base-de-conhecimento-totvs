---
content_hash: faaaf0149dabacc963e31dc18353d46e7de76ac29de87e60fc6d2fb58bdfe123
fetched_at: '2026-06-29T00:12:01.298145+00:00'
page_id: '892140584'
product: rm
source: tdn-rm
title: Parâmetros do Repasse para Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=892140584
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Repasse para Convênios**
3. **Liberação do Repasse**
4. **Exemplo**

## **01. VISÃO GERAL**

O documento tem objetivo de mostrar  o funcionamento das configurações  do Repasse para convênios.

## **02. REPASSE PARA CONVÊNIOS**

No TOTVS Gestão Hospitalar acesse Ambiente/Parâmetros/Gestão Hospitalar.

Campos:

* Ordenar relatórios, deverá ser selecionado o tipo de ordenação a ser exibido no relatório
* Liberação de repasse: são definidas as regras para liberação de repasse.

## **03. LIBERAÇÃO DO REPASSE**

Clique na guia Repasse Convênio.

No painel Liberação, são definidas as regras para liberação de repasse, que são

## **3.1. Controlado pelo usuário**

Existe um usuário que controla o repasse e este usuário vai fazer todo o processo de liberação.

## **3.2. Quando confirmar recebimento**

O repasse será realizado após recebimento.

## **3.3. Quando gerar faturamento**

O repasse só será liberado após a geração da fatura ou arquivo que será enviado ao Convênio.

**Utilização**:

Menu=> Repasse=> Repasses

Selecione um prestador para o repasse  e  visualize o item do repasse

Em Faturamento => Faturamento para convênio => pesquisar a remessa e execute o faturamento para convênio.

Após a execução ir para aba de liberados para pagamento.

**Utilização:**

Em menu **Faturamento=>Gestão de glosa**

Fatura abaixo, não foi liberada para pagamento, será feito o controle de glosa (Glosa por conta, glosa total ou liberação automática) deste item e ele será liberado para pagamento de acordo com os critérios definidos.

Em gestão glosa – remessa 8069

Ao executar a glosa total ou parcial, esta fatura será liberada para o pagamento com a data definida de acordo com os critérios.

Repasse=> liberado para pagamento

É possível visualizar a remessa foi liberada para pagamento

## **03.  EXEMPLO**

**Menu Faturamento=> Repasses**

Preencha o filtro de acordo com os critérios definidos, abra um dos repasses retornados.

Aba Repasse, selecione um item e vá em Processos=> Libera repasse

Ao abrir a tela do processo:

Senão preencher a data previsão do pagamento, parâmetro marcado:

* Controlado pelo Usuário ou Quando Confirmar Recebimento, será preenchida a data atual
* Quando Confirmar Recebimento com prazo definido para pagamento - será preenchida a regra definida para os dias de liberação, sempre usando a data mínima a partir da data atual.

Executar liberação, após o processo executado vá na aba **Liberados para pagamento** e a remessa será liberada.

Exemplo, para parâmetro o Quando Confirmar Recebimento com prazo definido para pagamento:

Dia 01, a partir da configuração definida menor data seria, o recebimento até dia 03 e a liberação após dia 5, sendo ele somado a data configurada.
