---
content_hash: 846b197444672354d2155e0f681acb75abc89e5cc28b43e96cd21e70a128ef53
fetched_at: '2026-06-29T00:09:35.861071+00:00'
page_id: '425459398'
product: rm
source: tdn-rm
title: Demissão de Funcionários
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459398
version: 3
---

**Demissão de Funcionários**

---

A Pré-Baixa também faz parte da solução de Integração TOTVS Folha de Pagamento x Gestor AVB (TOOLS) para Averbação (Empréstimo consignado em folha).

O processo de cálculo da demissão de um funcionário no TOTVS Folha será feito em duas etapas.

**Cálculo da Recisão do Contrato:** Esta etapa irá verificar através do CNPJ (coligada) e chapa (matrícula) se existe um contrato de averbação ativo (empréstimo do tipo AVBTOTVS). Caso afirmativo chamará um serviço "Calcular Saldo Devedor" (em modo síncrono) que irá determinar o saldo devedor do funcionário.  Caso o RH escolha lançar o saldo devedor do empréstimo do tipo averbação TOOLS ao cálculo de recisão de contrato e salvar essa configuração, o TOTVS Folha deverá executar um serviço do Business Conector passando o código da coligada e a chapa (matrícula) do funcionário.

***Nota:*** *As informações sobre o saldo devedor ficarão armazenadas no tabela PFEMPRT, onde o campo SALDOATUALIZADO será o saldo devedor do empréstimo de averbação TOOLS.*

**Efetiva Recisão de Contrato:** Na segunda etapa o TOTVS Folha buscará através do código da coligada a lista de funcionários demitidos no período (conforme parametrização). Para cada um desses registros, serão retornadas as seguintes informações:

Campos de retorno:

* Código da Coligada
* CGC/CNPJ da coligada
* CPF do funcionário
* Saldo devedor do empréstimo

O Business Conector será ativado toda vez que a liberação de competência for executada. Irá chamar o TOTVS Folha e enviará cada registro encontrado no retorno da consulta anteriormente feita para o Web Service da TOOLS. O saldo calculado será debitado do valor total da rescisão do contrato efetivando a demissão do funcionário. É importante salientar que esse valor é apenas para orientar o RH, pois ele pode ser alterado caso o RH não concorde em debitar a parcela ou não seja possível debitar o valor completo no momento da demissão.

***Nota:*** *Todas as mensagens dos processos de envio e recebimento de informações ficarão gravadas no Monitor da Fila de Integração.*
