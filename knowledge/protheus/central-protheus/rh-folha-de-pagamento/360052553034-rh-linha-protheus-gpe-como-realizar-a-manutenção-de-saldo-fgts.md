---
article_id: 360052553034
category: RH - Folha de Pagamento
content_hash: 84ce227b0665980e89d8965606c9fe3b4e8ad9537f449ec1377eb587587885e8
fetched_at: '2026-06-28T22:44:14.728973+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar a manutenção de saldo FGTS
type: support-article
updated_at: '2025-08-11T21:23:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052553034-RH-Linha-Protheus-GPE-Como-realizar-a-manuten%C3%A7%C3%A3o-de-saldo-FGTS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26346244408471) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Como realizar a manutenção de saldo FGTS?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**A rotina **Manutenção de Saldo de FGTS** (GPEM360) tem o objetivo de guardar o histórico de depósitos de FGTS e atualização de valores de cada um dos funcionários.

Nesta rotina deve ser incluído pelo usuário o valor inicial do funcionário, a não ser que seja o primeiro mês de trabalho do funcionário e que a rotina de atualização de saldo tenha sido rodada após realizar o cálculo da folha.

**Saldo Anterior** é o saldo do ultimo processamento realizado.

**Valor de Juros** será o valor que o sistema vai considerar como rendimento do valor depositado, ou seja, buscará o valor de saldo e a taxa de juros cadastrada para chegar na atualização do valor já depositado.

**Valor depositado** se dá ao valor de depósito do FGTS do mês. Quanto foi arrecadado no mês da atualização do saldo para gerar os novos valores.

**Valor do Saque** armazena o valor informado pelo usuário, que corresponde ao montante sacado pelo funcionário no mês em que ocorre a **Atualização de Saldo**, abatendo esse valor e abatendo do saldo anterior o valor de FGTS sacado pelo funcionário, antes da apuração de juros na Atualização de Saldo.

**Saldo Atual** é composto pela somatória do saldo anterior, valor juros e valor depositado no mês.

**Saldo Real** armazena o valor do **Saldo Anterior (RS\_SALANT)** mais o valor de **Juros (RS\_VALJUR)** mais o valor **Depósito (RS\_VALDEP)** menos o valor do **Saque (RS\_VALSAQ)**, abatendo do valor do saque realizado pelo funcionário, tendo em vista a necessidade de apuração do Saldo para fins rescisórios e do **Saldo Real** a ser considerado como saldo anterior do mês, realizando a atualização de saldo.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404619485975)

**Procedimentos para utilização:**

1) Entre na rotina **Manutenção de Saldo** (Miscelânea/ FGTS/ Manutenção de saldo), inclua o valor depositado até então no campo de **Saldo real** de um funcionário e confirme;

2) Realize o cálculo da folha e verifique se a verba de ID 0018-FGTS Depósito foi calculada;

3) Entre na rotina **Atualização de Saldo** (Miscelânea/ FGTS/ Atualização de saldo) e estipule os parâmetros de atualização e em seguida Confirme;

4) Entre novamente na rotina **Manutenção de saldo** e verifique o calculo realizado;

**IMPORTANTE**A atualização de saldo deve ocorrer sempre para meses que já estão fechados. Caso calcule com o mês ainda em aberto, o sistema não apresentará o valor do deposito realizado no mês.

**Saiba mais:**   
[GPE049RES\_Manutenção\_de\_saldo\_do\_FGTS](https://tdn.totvs.com/pages/releaseview.action?pageId=233761904)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
