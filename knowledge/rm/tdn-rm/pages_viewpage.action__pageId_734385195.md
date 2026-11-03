---
content_hash: 3eb59bc0798442b4ad85190ee0c9d549c8ce9c6f1fff60842be4418bdd04cfaf
fetched_at: '2026-06-29T00:11:29.241008+00:00'
page_id: '734385195'
product: rm
source: tdn-rm
title: Cancelamento de Férias Pagas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=734385195
version: 10
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Cancelamento de Férias**
   1. **Outras Ações / Ações relacionadas**
5. **Tela Parametrizador - Férias - Controle 2/2 - Cancelamento de Férias**
   1. **Principais Campos e Parâmetros**
6. **Tabelas utilizadas**

## **01.****VERSÕES**

**A partir do Release:**

* **12.1.2302 e Superiores**

## **02. VISÃO GERAL**

Foi criado no processo de cancelamento de férias a possibilidade de cancelamento, gravando o valor do liquido de férias pagas. O cancelamento será possível somente para férias com a situação '**Marcadas**'. Ao ser canceladas as férias e marcado o novo parâmetro criado '**Armazena líquido como Evento Programado**', o sistema irá armazenar no anexo de funcionário '**Eventos Programados**', o evento criado no Cadastro de Eventos e informado no parametrizador, para que o usuário lance manualmente através do Grupo de Eventos.

**Observações:**

1. Os valores de diferença de Líquido de Férias não serão considerados;  
2. Serão armazenados somente os valores de líquido de férias canceladas, através do processo de cancelamento global de férias;  
3. Serão consideradas somente das férias com o status de 'Marcadas';  
4. Não será considerado o cancelamento individual de férias;  
5. Não será tratado o cadastro de centro de custo no evento desconto de Liquido de férias canceladas.  
6. Os Lançamentos Financeiros gerados a partir do cálculo das férias que foram canceladas, deverão ser alterados/cancelados de forma manual pelo próprio usuário.

## **03. EXEMPLO DE UTILIZAÇÃO**

**1º Passo:**

Criar em **RM | RH | Folha de Pagamento | Administração de Pessoal | Cadastros | Cadastros Globais | Tabelas Dinâmicas**, criar um item **'EVENTO DE DESCONTO DE LIQUIDO DE FÉRIAS CANCELADAS'** na tabela dinâmica de código **'TPEVTPROG - Tipo de Evento Programado'**, conforme exemplo:

**2º Passo:**

Criar em **RM | RH | Folha de Pagamento | Administração de Pessoal | Cadastros | Eventos,** criar um evento '**DESCONTO DE LIQUIDO DE FÉRIAS CANCELADAS**', do tipo **Desconto/Valor** **e****sem código de cálculo:**

**Observações:**

**1) O evento deverá ser do tipo Desconto, Valor, sem código de cálculo ou fórmula.**

**2) A distribuição do evento por centro de custo deverá ser feita, após o lançamento do evento no envelope do funcionário.**

**3º Passo:**

Informar em **RM | RH | Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Férias | Controle 2 | Cancelamento de Férias,** no campo criado **'Evento de desconto programado para ser lançado:'**, o evento '**DESCONTO DE LIQUIDO DE FÉRIAS CANCELADAS**', do tipo '**Desconto/Valor** **e****sem código de cálculo**'e no campo **'Tipo de Lançamento do evento programado:'**,o tipo de lançamento do evento programado **'DESCONTO DE LIQUIDO DE FÉRIAS CANCELADAS'** da tabela dinâmica de código **'TPEVTPROG - Tipo de Evento Programado'**, conforme exemplo:

**Observação:**

Caso o usuário não preencha os campos do parametrizador, ao tentar utilizar o recurso, marcando o parâmetro '**Armazena líquido como Evento Programado**', será apresentado no log do processo de **Cancelamento de Férias**, um erro informando a falta dos parâmetros de férias | Controle 2/2, conforme abaixo:

**4º Passo:**

O funcionário que terá as férias camceladas e armazenado o líquido de férias para desconto através do evento programado, deverá estar com a Situação das Férias '**Marcadas**':

**5º Passo:**

Efetuar o cancelamento das férias do funcionário, através do módulo de '**Cancelamento das Férias**', marcando o parâmetro '**Armazena líquido como Evento Programado**':

**6º Passo:**

Conferir no anexo de Eventos Programados do cadastro de funcionários, o evento de desconto de líquido de férias armazenado:

**7º Passo:**

O lançamento do evento programado deverá ser realizado através do módulo de Lançamentos de Grupo de Eventos, marcando a opção '**Lançar Eventos Programados**' e na aba '**Eventos Programados**' marcar o '**Tipo de Lançamento do evento programado'** criado e informado no parametrizador**:**

**8º Passo:**

Após o  lançamento do evento programado, poderá ser realizada a conferência no envelope de pagamento do funcionário o evento lançado**:**

## **04. TELA Cancelamento de Férias**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Marcar | Marcar o parâmetro '**Armazena líquido como Evento Programado**' |
| Desmarcar | Desmarcar o parâmetro '**Armazena líquido como Evento Programado**' |

## **05. TELA Parametrizador - Férias - Controle 2/2 - Cancelamento de Férias**

****Principais Campos e Parâmetros****

| Campo | Descrição |
| --- | --- |
| Permite armazenar líquido no mês seguinte ao pagto, no caso de lib. competência | Este parâmetro serve para que o sistema armazene o líquido de férias, quando as férias foram marcadas na competência anterior, antes da liberação da competência. |
| Evento de desconto programado para ser lançado | Destinado a informação do evento de desconto programado criado no cadastro de eventos, para ser lançado através do Grupo de Eventos - Eventos Programados. |
| Tipo de Lançamento do evento programado | Destinado a informação do tipo de lançamento de evento programado, criado na tabela dinâmica com o código **'**TPEVTPROG - Tipo de Evento Programado**'.** |

## **06. TABELAS UTILIZADAS**

* **GDINAM**
* **PFUNC**
* **PFEVENTOSPROG**
* **PFFINANC**
* **PTPEVENTOPROG**
* **PFUFERIAS**
* **PFUFERIASPER**
* **PFUFERIASVERBAS**
* **PPARAMADICIONAIS**

## **07. DEMAIS INFORMAÇÕES**

**[Cancelamento de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719950)**

**[Parametrizador](https://tdn.totvs.com/pages/viewpage.action?pageId=452718539)**
