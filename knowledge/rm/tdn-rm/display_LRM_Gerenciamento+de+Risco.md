---
content_hash: 52f7826b471098766d3cdadd02e5321b2a385a104435fc20c2bbe535cf28be06
fetched_at: '2026-06-29T00:11:55.071965+00:00'
page_id: '860252265'
product: rm
source: tdn-rm
title: Gerenciamento de Risco
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerenciamento+de+Risco
version: 18
---

## **CONTEÚDO**

1. **Painel de Gerenciamento de Risco**
   1. **Visão Geral**
   2. **Funcionalidade**
   3. **Exemplo de utilização**
2. **Recebimento de alertas - Scores e Escalas**
   1. **Visão Geral**
   2. **Funcionalidade**
   3. **Exemplo de utilização**
3. **Ativação de recursos em tempo real**
   1. **Visão Geral**
   2. **Funcionalidade**

Gerenciamento de RiscoPainel de Gerenciamento de Risco

## **01. PAINEL DE GERENCIAMENTO DE RISCO**

Visão Geral

## **a.** **VISÃO GERAL**

O Painel de Gerenciamento de Risco permite ao profissional uma visualização dos alertas recebidos que caracterizam risco para o paciente que esteja apresentando um resultado fora da faixa de normalidade cadastrada.

Funcionalidade

## **b. FUNCIONALIDADE**

1. O painel pode ser acessado através do menu **Painéis / Painel de Gerenciamento de Risco**.
2. Os alertas exibidos são referentes aos alertas encaminhados para o profissional utilizando a aplicação, sendo assim **não serão exibidos alertas direcionados para outros profissionais.**
3. Os alertas podem ser filtrados de acordo com a **Unidade de Atendimento** em que houve a ocorrência, pelo **Tipo de alerta** (ex. scores), ou pelo **Paciente** que apresentou o alerta de risco.
4. Os alertas apresentam ações para "**Adicionar observação"** e "**Visualizar"**:  
     
   * **Adicionar observação** irá abrir uma tela para incluir uma observação (texto livre) e também marcará o alerta com o status de "**Visualizado".**
   * **Visualizar** o alerta irá marcá-lo com o status de "**Visualizado"** e direcionará o profissional, através de uma nova aba, para o registro preenchido que deu origem a ocorrência.

**IMPORTANTE:**Uma vez que um alerta é visualizado, o status de **visualizado e a data de visualização** serão gravados no sistema e **não poderão ser alterados**.

Exemplo de utilização

## **c. EXEMPLO DE UTILIZAÇÃO**

1. Tela inicial do **Painel de Gerenciamento de Risco:**
2. Ações para os alertas do **Painel de Gerenciamento de Risco:**

Recebimento de alertas - Scores e Escalas

## **02. RECEBIMENTO DE ALERTAS - SCORES E ESCALAS**

Visão Geral

## **a.** **VISÃO GERAL**

A configuração de recebimento de alertas para scores e/ou escalas permite definir quais scores e/ou escalas o profissional será alertado em caso de resultados fora da faixa de normalidade.

Esses alertas ficarão disponíveis no **[Painel de Gerenciamento de Risco](https://tdn.totvs.com/pages/viewpage.action?pageId=860252304)**, e caso o sistema esteja configurado para [**permitir recursos em tempo real**](https://tdn.totvs.com/pages/viewpage.action?pageId=861274171), também exibirão uma notificação no canto inferior da aplicação.

Funcionalidade

## **b. FUNCIONALIDADE**

1. Cada profissional poderá configurar, de acordo com sua preferência, quais scores e/ou escalas ele será alertado em caso de **resultados fora da faixa de normalidade**.
2. A configuração pode ser feita através do menu **[Minhas Configurações](https://tdn.totvs.com/pages/viewpage.action?pageId=555864145).**
3. Para que o score e/ou escala fique disponível para enviar alertas, ele precisará estar cadastrado no RM com a opção "**Alerta para usuário"** habilitada.
4. Os scores e/ou escalas que forem preenchidos para o paciente, por outros profissionais, apresentando um resultado fora da faixa de normalidade cadastrada e que estiverem configurados para gerar notificações de alertas:  
     
   * Ficarão visíveis no **[Painel de Gerenciamento de Risco](https://tdn.totvs.com/pages/viewpage.action?pageId=860252304)**
   * Exibirão uma notificação em tempo real no canto inferior da aplicação alertando sobre a ocorrência **[(](https://tdn.totvs.com/pages/viewpage.action?pageId=861274171)[quando o recurso estiver habilitado](https://tdn.totvs.com/pages/viewpage.action?pageId=861274171)[)](https://tdn.totvs.com/pages/viewpage.action?pageId=861274171)**.

Exemplo de utilização

## **c. EXEMPLO DE UTILIZAÇÃO**

1. Na tela de **Minhas Configurações,**configure quais scores e/ou escalas deverão gerar notificações de alertas:
2. Quando outro profissional fizer o preenchimento de um score e/ou escala para o paciente, e o resultado estiver fora da faixa de normalidade, terá a ocorrência registrada no **Painel de Gerenciamento de Risco,**e caso o sistema esteja habilitado com o recurso em tempo real, também será exibido uma notificação.
3. Exemplo de um profissional com as configurações para geração de notificações de alertas para o score e/ou escala recebendo a notificação:

   **IMPORTANTE:**

   A notificação apresenta o recurso de "**Ir para Scores e Escalas".** Esse recurso direciona o profissional, através de uma nova aba do navegador, para a funcionalidade de **Scores e Escalas**do atendimento do paciente que apresentou o resultado alterado, e automaticamente marca a ocorrência como "**Visualizado".**

1. Exemplo de ocorrência registrada no **Painel de Gerenciamento de Risco** do profissional com a configuração para recebimento de alertas:

Ativação de recursos em tempo real

## **03. ATIVAÇÃO DE RECURSOS EM TEMPO REAL**

Visão Geral

## **a.** **VISÃO GERAL**

A configuração para ativação de recursos em tempo real possibilita um nível maior de interação entre os usuários acessando a aplicação, habilitando o envio de informações do servidor de aplicação para os usuários.

Funcionalidade

## **b. FUNCIONALIDADE**

1. Para habilitar esse recurso, é necessário adicionar uma chave no arquivo de configuração em que está instalado o servidor de aplicação (**RM.Host** ou **RM.Host.Service**).
2. Localize o arquivo de configurações referente a instalação do **RM.Host** ou **RM.Host.Service**, e dentro da sessão **configuration /** **appSettings**inclua a chave **EnableRealtime**com o valor **"true"**.
3. Com a chave habilitada, o sistema permitirá o envio de informações no sentido servidor de aplicação -> usuários, possibilitando que uma rotina processada no servidor envie notificações para os usuários acessando o sistema.

**Veja também:**
