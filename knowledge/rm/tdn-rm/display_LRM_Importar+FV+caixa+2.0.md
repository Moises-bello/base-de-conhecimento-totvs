---
content_hash: d337706844dfce764a117b42539be0bed44d84e17edd4ee47bb2093b63552194
fetched_at: '2026-06-29T00:05:47.284698+00:00'
page_id: '1010252766'
product: rm
source: tdn-rm
title: Importar FV caixa 2.0
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+FV+caixa+2.0
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Selecionar FV**
3. **Importar FV**
4. **Configurar FV**

Importar FVVisão Geral

## **01. VISÃO GERAL**

Esse documento tem o objetivo apresentar as fórmulas visuais para utilizar no TOTVS Gestão Hospitalar.

Selecionar FV

## **02. SELECIONAR FV**

Em Gestão > TOTVS Compartilhamento   
  
Selecione os campos abaixo

Tipo: Fórmula Visual  
Produto: Gestão de Hospitais, Clínicas e Centros de Diagnósticos

Selecione a Fórmula visual desejada, nesse caso **SAUWKF003 - Baixa Lançamento Financeiro - Alteração Status Painel Eletivo - Caixa 2.0**

Fórmula visual complementar

A fórmula visual **SAUWKF004 - Comlemento Baixa Financeiro - Alteração Status Painel Eletivo - Caixa 2.0** é uma fórmula complementar a **SAUWKF003**, caso não seja importada automaticamente o procedimento pode ser feito manualmente importando uma de cada vez.  
  
Caso a Query também não seja localizada automaticamente também deverá ser importada manualmente.

Após selecionar a fórmula visual clique em **Download**Na caixa de seleção clique em **Importar** para relizar importação direta ou **Salvar** para salvar no computador destino.

Importar FV

## **03. IMPORTAR FV**

Ao selecionar importar arquivo o wizard de importação irá abrir automaticamente com a fórmula visual selecionada.  
Caso alguma das opções abaixo estiver desmarcada basta marca-la.

SAUWKF003; ConsSQL; SAUWKF004; Código fonte; Gatilho

Selecione a coligada desejada

* Coligada Atual
* Todas Coligadas
* Lista de Coligadas

Selecione a aba parametros e defina a categoria desejada.\*

Fluxo opcional

Caso a opção anterior tenha sido Salvar o fluxo de seleção da FV passará inciamente por outro caminho.  
  
Selecione a opção de importação e logo após selecione

Clique em executar para importar a fómula visual.

Configurar FV

## **04. CONFIGURAR FV**

Após a importação da fórmula visual note que ficará disponivel as fórmulas SAUWKF0003 e SAUWKF0004.

Selecione a fórmula SAUWKF0004 e clique em editar.

Identifique o Id da fórmula

Atribuir a fluxo pai

É possivel atribuir a FV ao fluxo principal, caso não esteja preechido automaticamente em *Fómula Visual Pai* essa função poderá ser realizada manualmente.

Após obter o ID da fórmula (no exemplo é o 52)  
dê um duplo click em SAUWKF0003

A tela de configuração será exibida conforme imagem abaixo  
  
Clique com botão direito em **FvDeBaixaFinanc** e selecione a opçao "Selecionar fórmula visual"

Pequise pela fórmula cujo o id salvamos anteriormente e clique em **OK**  
  
  
Note que o id da fórmula irá alterar e depois clique em **Salvar** 

É necessário também realizar a verificação dos gatilhos da fórmula SAUWKF003. Sem o gatilho, a fórmula visual não irá funcionar

Caso o gatilho não esteja confiurado ele deve ser feito desta forma
