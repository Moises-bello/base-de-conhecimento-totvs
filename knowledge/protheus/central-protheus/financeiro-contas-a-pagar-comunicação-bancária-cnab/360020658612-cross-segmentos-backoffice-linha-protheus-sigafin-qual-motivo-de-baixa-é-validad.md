---
article_id: 360020658612
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 4939f35949e1c123d4dddcf23385711a7f4766000be9936636bc891acd0e9a89
fetched_at: '2026-06-28T22:37:56.423558+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Qual motivo de baixa
  é validado no Retorno de Pagamento (FINA430)
type: support-article
updated_at: '2022-07-22T15:52:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020658612-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Qual-motivo-de-baixa-%C3%A9-validado-no-Retorno-de-Pagamento-FINA430
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00min**

**Dúvida**Qual motivo de baixa é validado no Retorno de Pagamento (FINA430)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da versão 11.80]  
  
  
**Solução**  
No padrão o motivo de baixa que é definido nas baixas pela rotina Retorno de Pagamento (FINA430) é: "Debito CC". Ou seja, assim que efetuar o retorno de pagamento será gravado na movimentação bancária o Motivo de Baixa: Debito CC, não é possível selecionar qual o motivo de baixa que será considerado.

Acesse: Miscelânea> Arquivos> Tabela Motivos de Baixa   
(Padrão)  
Sigla: DEB  
Descrição:DEBITO CC  
Carteira: P  
Mov. Bancaria: S  
Comissão: N  
Cheque: N

**Saiba mais**O ponto de entrada: F430BXA**,** grava complemento na baixa no retorno de pagamento (FINA340): **[F430BXA - Grava complemento de baixa](https://tdn.totvs.com/display/PROT/F430BXA+-+Grava+complemento+de+baixa)**
