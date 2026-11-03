---
content_hash: 2b9b343581b84afa5cdabdf7401e9ccbe2108ef66b40f9eda236b13e3a81ba11
fetched_at: '2026-06-29T00:11:48.928445+00:00'
page_id: '829305503'
product: rm
source: tdn-rm
title: Aprazamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Aprazamento
version: 15
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Itens para aprazamento**
4. **Prescrição com itens de início imediato (Versão 2506)**
5. **Configurações**

Aprazamento V2406Visão Geral

## **01. VISÃO GERAL**

Recurso que permite ao usuário o planejamento do aprazamento de itens prescritos. Nesta tela estarão os itens da prescrição médica e prescrição de enfermagem. 

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao clicar no menu de "Processo de Enfermagem" e em "Aprazamento", será aberta a tela com os itens pendentes de aprazamento da prescrição médica e de enfermagem.

Selecione no combo de "Ciclo de prescrição" qual a vigência desejada para que os itens sejam exibidos na tabela.

Após selecionar o ciclo, será exibido na tabela os itens prescritos. Para filtrar um item específico, insira o nome no campo de busca.

Abaixo da lista será identificado o número total de itens prescritos. Para exibir mais itens da prescrição clique em "Carregar mais registros".

Após finalizar o aprazamento, selecione todos os itens ou clique no checkbox para demarcar os itens que não deseja liberar e clique no botão "Liberar Aprazamento". Apenas os itens selecionados serão liberados e exibidos na **tela de checagem.**

Botão **"Opções Avançadas":**

* Ao selecionar a opção **"Legendas"** é exibido uma janela contendo o significado de cada ícone dos status de um item na tabela de Planejamento Terapêutico, conforme imagem abaixo:

* Ao selecionar a opção **"Visualizar última liberação"**, é exibido em uma nova guia um PDF contendo os itens aprazados e liberados recentemente:

 

Itens para aprazamento

## **03. ITENS PARA APRAZAMENTO**

Ao abrir o menu de aprazamento, serão listados todos os itens da prescrição médica e de enfermagem pendentes de aprazamento por parte dos usuários.

Ao clicar em um item da tabela é apresentado o modal de **"Item para aprazamento"**. Neste modal encontramos as sessões de acordo com o item listado.

São exibidos também os horários para definição por parte do usuário. Nos itens com horários de frequência e início definidos, o sistema já listará a sugestão dos mesmos.

**Quando houver alteração do primeiro horário,** o sistema fará o recálculo dos demais horários. Se a alteração ocorrer nos horários do meio ou final, o sistema não fará o recálculo.

Para itens do tipo de **"Inalação"** da prescrição médica, devem ser listados os itens na sessão "itens da inalação" do PLT.

Já os itens de componentes, estão listados na sessão conforme imagem abaixo. Nesta sessão estarão listados todos os itens cadastrados como **"solução soro + componente da solução"** ou **"componentes da solução"** que foram prescritos nos submenus de medicamentos e **"Soros e Componentes"** na prescrição. Se o item fizer parte da diluição na prescrição, este deverá aparecer na sessão de **componentes** e não em **diluentes**. Os itens do tipo soros, diluentes e componentes **utilizam** a unidade de dosagem definida na prescrição, não sendo permitida sua alteração durante o processo de aprazamento.

Para finalizar as alterações clique no botão "Incluir".

Após finalizar o aprazamento, selecione todos os itens ou clique no respectivo checkbox para desmarcar os itens que não deseja liberar e clique no botão **"Liberar Aprazamento"**. Apenas os itens selecionados serão liberados e exibidos na tela de checagem.

Prescrição com itens de início imediato

## **04. PRESCRIÇÃO COM ITENS DE INÍCIO IMEDIATO**

##### **Funcionalidade disponível a partir da versão 12.1.2506.**

A funcionalidade foi desenvolvida para agilizar a administração de medicamentos prescritos com início imediato, eliminando a etapa de aprazamento. Dessa forma, o item segue diretamente para checagem após a liberação, garantindo rapidez e segurança no cuidado ao paciente. 

Para utilizar é necessário parametrizar a unidade de atendimento para que utilize o aprazamento automático dos itens de início imediato (RM → Cadastro → Unidade de Atendimento → Prontuário eletrônico → Aprazamento/Checagem → Utiliza aprazamento automático para itens com início imediato).

## **COMO FUNCIONA**

### Prescrição com início imediato

* Quando o médico seleciona a opção **“início imediato”** em um item da prescrição:

  + O sistema reconhece que o medicamento deve ser administrado **o quanto antes**.
  + Esse item **não passa pelo fluxo de aprazamento** (programação de horários).
  + Ele segue diretamente para a **tela de checagem da enfermagem**, respeitando a configuração da unidade.

### Com análise farmacêutica habilitada

* Caso a unidade de atendimento esteja parametrizada para **análise farmacêutica obrigatória**:

  + O medicamento **primeiro é direcionado ao farmacêutico**, que avalia a prescrição.
  + Após a **aprovação do farmacêutico**, o item é liberado para o painel de dispensação e aparece na **checagem da enfermagem**.
  + Somente após essa etapa o medicamento poderá ser administrado.

### Sem análise farmacêutica habilitada

* Caso a unidade **não exija análise farmacêutica**, o processo é mais rápido:

  + Assim que o médico libera a prescrição, o medicamento é liberado para o painel de dispensação e aparece **direto na checagem da enfermagem**.
  + O enfermeiro já pode confirmar a segurança e realizar a administração.

| Situação | Fluxo do item |
| --- | --- |
| **Início imediato + com análise farmacêutica** | Médico → Farmacêutico → Checagem |
| **Início imediato + sem análise farmacêutica** | Médico → Checagem |
| **Sem início imediato + com análise farmacêutica** | Médico → Farmacêutico → Aprazamento → Dispensação → Checagem |
| **Sem início imediato + sem análise farmacêutica** | Médico → Aprazamento → Dispensação → Checagem |

Configurações 

## **05. CONFIGURAÇÕES**

Em configurações por unidade de atendimento, no RM, é possível definir alguns parâmetros para comportamento do sistema. Na aba **"PEP RM"**, sub aba **"Aprazamento / Checagem"**:

Configuração para **aprazamento de itens com início imediato** com aprazamento realizado de maneira automática:
