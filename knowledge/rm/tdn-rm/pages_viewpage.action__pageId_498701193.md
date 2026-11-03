---
content_hash: 12dee34be23bf1bcc8da94f6b643b86ecf605ef0269dfa7a8f52efba56cf7206
fetched_at: '2026-06-29T00:10:22.679978+00:00'
page_id: '498701193'
product: rm
source: tdn-rm
title: 'S-2299/S-2399 - Como gerar Retificação de desligamento? (Parâmentro: Não lançar
  Liquido de retificação no envelope da competência Atual marcado)'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498701193
version: 11
---

false

**A partir das Versões:**

* **12.1.23.225**
* **12.1.24.169**
* **12.1.25.109**

# Objetivo:

---

       O objetivo deste documento é trazer informações de como é o processo do novo cálculo da retificação de desligamento, mostrando desde a parametrização até o seu cancelamento.

---

13Retificação gerada pelo Cálculo de Rescisão ComplementarRetificação gerada pelo Cálculo de Rescisão Complementar21Execução do scriptExecução do script

Para a liberação do novo cálculo será necessário executar o script especifico "LB.2019.06\_06 e LB.2019.07\_11" no aplicativo  RM.Script.Executor.exe

3-1ParametrizaçãoParametrização

Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso 02.01.05.09 Retificação da Folha de Pagamento

Acesse o menu RH | Folha de Pagamento | Configurações | Parametrizador | eSocial | Configurações Gerais | Configurações Gerais 5/5

Cadastre o período inicial que será apresentado na tela do processo de rescisão complementar e marque o parâmetro "Não lançar Liquido de retificação no envelope da competência Atual"

3-2CálculoCálculoCalculotrue3-1CálculoCálculo

Na rescisão complementar marque o parâmetro “Retificar rescisão”. A “Data de Último Movimento” e o parâmetro “Pagamento de verbas de natureza salarial ou não salarial devidas após o desligamento” ficarão desabilitados quando o parâmetro “Retificar rescisão” estiver marcado. Escolha o período de lançamento que será gravado no mês competência da rescisão, ou seja, será inserido novo período no mesmo mês em que a rescisão original foi calculada. Este período será por default o período selecionado no parametrizador (conforme aba parametrização).

**Observação:**

* A diferença entre outras verbas de natureza salarial ou não salarial devidas após o desligamento e a retificação da rescisão é que na primeira o evento será devido por exemplo na apuração de comissão após a rescisão e no segundo foi alguma verba paga incorretamente e deve ser retificada.
* Quando ocorrer uma rescisão por dissidio sim e uma retificação de rescisão no mês competência, deverá ser lançado o calculo em períodos diferentes.

O parâmetro “Período sequencial” deverá ser utilizado quando tem várias retificações em períodos diferentes. Marcando este parâmetro o sistema busca o maior período existente com retificação calculada e lança no período posterior.

Cadastre o(s) evento(s) que deseja incluir ou alterar no período selecionado. Os eventos informados devem ser aqueles que se quer retificar. 

**Exemplo:**

Supondo que a competência atual está em setembro, foi paga uma rescisão em março, porém sem o valor de 300 horas do evento de Horas Extras para esse funcionário.

Após o calculo da retificação o sistema irá realiza o lançamento dos eventos no período 10000 da competência retificada com data de pagamento da competência atual.

Será gerado um gatilho do evento S-2299 – Desligamento no período de apuração do período original como retificação do envio anterior.

Deverá ser gerado um gatilho no período atual do evento S-1210 - Pagamentos de Rendimentos do Trabalho referente ao pagamento dessa retificação.

3-2Cálculo - Marcando o parâmetro "Calcular Somente Eventos Informados"Cálculo - Marcando o parâmetro "Calcular Somente Eventos Informados"

Na rescisão complementar quando é marcado o parâmetro “Calcular Somente Eventos Informados”, somente será calculado este evento que foi digitado.

.

**Observação:**

* A diferença entre outras verbas de natureza salarial ou não salarial devidas após o desligamento e a retificação da rescisão é que na primeira o evento será devido por exemplo na apuração de hora extra ou comissão após a rescisão e no segundo foi alguma verba paga incorretamente e deve ser retificada

Marcar “Retificar rescisão” e escolher o período de lançamento que será gravado no mês competência do fator gerador da rescisão, ou seja, será inserido novo período no mesmo mês em que a rescisão original foi calculada antes da rescisão complementar. Este período será por default o período selecionado no parametrizador anteriormente.

O parâmetro “Período sequencial” deverá ser utilizado quando tem várias retificações em períodos diferentes. Marcando este parâmetro o sistema busca o maior período existente com retificação calculada e lança no período posterior.

**Exemplo:**

Supondo que competência atual está em setembro, foi paga uma rescisão em junho com aviso prévio de 30 dias e era devido 90 dias.

Após executar o processo de cálculo parametrizando conforme acima será gerado um gatilho do evento S-2299 – Desligamento no período de apuração do período original como retificação do envio anterior;

Também será gerado o gatilho para retificar também o evento S-1210 - Pagamentos de Rendimentos do Trabalho no mês de apuração referente ao mês de pagamento da rescisão original

E na ficha financeira do mês da rescisão original é inserido um período de acordo com o parametrizado no processo de rescisão complementar

3-3CancelamentoCancelamento

Para o cancelamento da retificação da rescisão é necessário marcar o parâmetro "Retificação folha/rescisão",  selecione o período em que foi lançada a retificação da rescisão e informe a competência e o período que se quer cancelar.
