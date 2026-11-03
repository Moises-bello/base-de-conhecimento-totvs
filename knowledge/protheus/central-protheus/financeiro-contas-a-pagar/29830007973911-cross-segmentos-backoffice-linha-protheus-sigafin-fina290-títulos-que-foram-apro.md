---
article_id: 29830007973911
category: Financeiro - Contas a Pagar
content_hash: 7ba0a1dc1525125512ef19934d26496fb83129978076ae46f4cb2184d0e86700
fetched_at: '2026-06-28T22:38:07.130428+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA290 - Títulos que
  foram aprovados após gerar fatura necessitam de aprovação novamente
type: support-article
updated_at: '2025-02-07T18:08:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29830007973911-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA290-T%C3%ADtulos-que-foram-aprovados-ap%C3%B3s-gerar-fatura-necessitam-de-aprova%C3%A7%C3%A3o-novamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29829980935575) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**Títulos que foram aprovados após gerar fatura a pagar necessitam de aprovação novamente  
  
**Ambiente**Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Todas as versões  
  
  
**Solução**Quando realizado a liberação para pagamento a partir da rotina **(FINA580)** de um título, caso este seja usado para geração de fatura(s) **(FINA290)** é necessário realizar nova liberação, pois é um novo título gerado.  
  
É possível configurar valor mínimo para liberação através do parâmetro **MV\_VLMINPG**, no entanto, isso se aplicará a todos os títulos incluídos no sistema.  
  
Exemplo: Ao preencher o parâmetro **MV\_VLMINPG = 1.000** o sistema não validará nenhum valor de título menor que este **(para efeito da Liberação da Baixa)**.

**Saiba mais**

[Faturas a Pagar - FINA290 - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Faturas+a+Pagar+-+FINA290+-+Financeiro+-+P12)

[Liberação para Baixas no Contas a Pagar](https://tdn.totvs.com/pages/releaseview.action?pageId=239018515)
