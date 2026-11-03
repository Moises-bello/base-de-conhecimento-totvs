---
article_id: 360025549632
category: RH - Folha de Pagamento
content_hash: 4e6cf9bc230cc4162b94caf35a90dbba64e1c3d033323313d09b678562b7ba6e
fetched_at: '2026-06-28T22:44:16.275249+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Registros não são gerados na folha de pagamento
  após a realização da integração do roteiro VEX
type: support-article
updated_at: '2025-10-06T13:24:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025549632-RH-Linha-Protheus-GPE-Registros-n%C3%A3o-s%C3%A3o-gerados-na-folha-de-pagamento-ap%C3%B3s-a-realiza%C3%A7%C3%A3o-da-integra%C3%A7%C3%A3o-do-roteiro-VEX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15819946198167) Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Ao executar o cálculo da folha, os registros não são apresentados mesmo após a integração do roteiro VEX.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**A tabela de lançamento não foi corretamente populada.  
  
**Solução**Para solucionar essa ocorrência, listamos abaixo o fluxo de gravação do roteiro VEX (quando opta-se por integrar este roteiro):  
  
Obs.: é necessário que seja informado no campo **Código Correspondente** da verba que será informada para cálculo no roteiro VEX, uma verba de contrapartida para que ao calcular a folha, seja apresentada a verba de **provento e desconto**. Por exemplo, se for lançado no roteiro VEX uma verba de provento, no campo código correspondente deve ser informado uma verba de desconto (sem id para cálculo)  
  
**1. Roteiro VEX**  
1.1. Ao informar uma verba para pagamento no roteiro VEX, é gravado na rotina de Lançamento Por Verba / Lançamento Por Funcionário (tabela RGB, roteiro VEX, rotina GPEA580);  
1.2. Ao executar o cálculo do roteiro VEX, o registro é gravado em Consultas por Funcionário (tabela SRC, roteiro VEX, rotina GPEA090);  
1.3. Ao realizar a integração com a folha, o registro é gravado nos lançamentos por funcionário (tabela RGB, roteiro FOL, rotina GPEA580);  
1.4. Ao calcular a folha, o registro é gravado em Consultas por Funcionário (tabela SRC, roteiro FOL, rotina GPEA090).  
  
Exemplo:  
1.1. Verba informada no roteiro VEX- Tabela RGB, roteiro VEX, rotina GPEA580;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025255691)  
  
1.2. Cálculo do roteiro VEX- Tabela SRC, roteiro VEX, rotina GPEA090;  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025256011)  
  
  
1.3. Integração com a folha- Tabela RGB, roteiro FOL, rotina GPEA580, RGB\_ROTORI= VEX  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025287471)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025265612)  
  
1.4. Cálculo da Folha- Tabela SRC, roteiro FOL, rotina GPEA090  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025265052)  
  
**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
