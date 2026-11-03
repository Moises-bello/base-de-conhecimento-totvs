---
article_id: 360040993353
category: RH - 13º salário
content_hash: 1c60f59f88b66fe42f6167772f6b9f59bd6e033dd0b0c15e0526766f39061c23
fetched_at: '2026-06-28T22:44:00.823441+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Identificadores referente a insuficiência de saldo
  no 13° Salario
type: support-article
updated_at: '2025-08-13T14:45:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040993353-RH-Linha-Protheus-GPE-Identificadores-referente-a-insufici%C3%AAncia-de-saldo-no-13-Salario
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19058046923159) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Quais os Identificadores referente a insuficiência de saldo no 13° Salário?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

ID 0030 - Insuficiência de saldo 13° - **Tipo Provento**;   
ID 0025 - Desconto insuficiência de saldo 13° - **Tipo Desconto**;

Quando realizado o calculo no roteiro 132 - 2° Parcela, caso o total de descontos seja maior que o total de proventos, será calculada a verba de **Insuficiência de Saldo - ID 0030,** com o saldo faltante para que não ocorra Liquido com valor Negativo.   
Após fechado o roteiro 132, no roteiro FOL o sistema desconta esse valor lançando a verba de **Desconto Insuficiência de Saldo - ID 0025**, zerando assim o débito. Exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10964878818711)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10964922464663)

**Saiba Mais**  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>

[RH - 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)
