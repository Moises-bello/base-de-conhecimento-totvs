---
article_id: 360051969333
category: RH - Benefícios
content_hash: ef134c6ef64c4978d8d4942a25d52538be09b0958af0881cf572cf8b96c00307
fetched_at: '2026-06-28T22:44:04.728005+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Pagamento Vale transporte em folha
type: support-article
updated_at: '2025-09-29T13:25:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051969333-RH-Linha-Protheus-GPE-Pagamento-Vale-transporte-em-folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33041090127255) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como é realizado o pagamento de vale transporte na folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões

**Solução**

Para clientes que desejam efetuar o pagamento do Vale Transporte em folha de pagamento é preciso **cadastrar** uma verba do tipo **Provento** com o **ID** de cálculo **0052**, caso esta verba exista o sistema irá gerar a verba com o valor total (parte empresa e funcionário) na folha.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11652476249495)

A verba é criada no momento da integração com a Folha de Pagamento na tabela RGB.

Caso o cliente passe a comprar Vale Transporte (cartão por exemplo) deve-se retirar o ID 0052 do cadastro da verba, assim a mesma não será gerada na folha do funcionário.

**Saiba Mais**[RH - Linha Protheus - GPE - Como descontar valor Fixo de Vale Transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406270401047-RH-Linha-Protheus-GPE-Como-descontar-valor-Fixo-de-Vale-Transporte?source=search)  
[RH - Linha Protheus - GPE - Desconto de Vale Transporte para Estagiários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036282453-RH-Linha-Protheus-GPE-Desconto-de-Vale-Transporte-para-Estagi%C3%A1rios?source=search)  
[RH - Linha Protheus - GPE - Como utilizar parâmetro MV\_CVTPROP para desconto de vale transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014665512-RH-Linha-Protheus-GPE-Como-utilizar-par%C3%A2metro-MV-CVTPROP?source=search)  
[RH - Linha Protheus - GPE - Controle de saldo de benefício ou compra da diferença faltante](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051035414-RH-Linha-Protheus-GPE-Controle-de-saldo-de-benef%C3%ADcio-ou-compra-da-diferen%C3%A7a-faltante?source=search)  
[RH - Linha Protheus - GPE - Como calcular percentual de desconto de Vale transporte inferior a 6% para todos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059488853-RH-Linha-Protheus-GPE-Como-calcular-percentual-de-desconto-de-Vale-transporte-inferior-a-6-para-todos-funcion%C3%A1rios?source=search)
