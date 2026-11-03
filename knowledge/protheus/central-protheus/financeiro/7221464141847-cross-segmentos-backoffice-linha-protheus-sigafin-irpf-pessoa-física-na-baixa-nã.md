---
article_id: 7221464141847
category: Financeiro
content_hash: 23f379712eb939c4502379e36ea0a6bbb0b5c395b92610d5e80ad923578feb06
fetched_at: '2026-06-28T22:38:03.281638+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - IRPF ( Pessoa Física
  ) na Baixa não é apresentado na MATA100
type: support-article
updated_at: '2023-01-25T22:11:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7221464141847-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-IRPF-Pessoa-F%C3%ADsica-na-Baixa-n%C3%A3o-%C3%A9-apresentado-na-MATA100
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05 min** **Dúvida** IRPF ( Pessoa Física ) na Baixa não é apresentado na MATA100   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**No IRPF ( Pessoa Física ), não é possível apresentar essa informação no momento da inclusão do documento de Entrada, pois a base de cálculo do IRPF será composta por todos os rendimentos aferidos no período de pagamento e, por este motivo, a alíquota e os valores retidos podem variar.  
A gravação dos dados neste momento poderia fornecer informações imprecisas e até mesmo impactar negativamente no cálculo efetivo do tributo na realização do pagamento.

**Saiba**A função que faz o cálculo do IR chama-se **FCalcIrBx** e é uma função interna do Protheus, ela não é disponibilizada para customização pela equipe de desenvolvimento, consequentemente, não possui documentação disponível no portal TDN. O cálculo para pessoa física é feita de acordo com a tabela progressiva do IR, cadastrada no configurador, e de acordo os rendimentos dentro do período de pagamento.
