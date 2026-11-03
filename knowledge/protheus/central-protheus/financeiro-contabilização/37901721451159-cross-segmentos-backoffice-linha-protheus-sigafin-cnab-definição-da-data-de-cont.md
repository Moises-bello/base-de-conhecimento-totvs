---
article_id: 37901721451159
category: Financeiro - Contabilização
content_hash: 88969d16d82662ff946f866029e22876e9a8331ee19ce479a6358e7f366f494d
fetched_at: '2026-06-28T22:38:05.308634+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB: Definição da
  data de contabilização por disponibilidade ou Data Base'
type: support-article
updated_at: '2026-01-27T10:04:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37901721451159-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Defini%C3%A7%C3%A3o-da-data-de-contabiliza%C3%A7%C3%A3o-por-disponibilidade-ou-Data-Base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37901721444887) Tempo aproximado para leitura: **00:04 min**  
  
**Dúvida**  
No processo de retorno/remessa CNAB, existe parâmetro para definir se a contabilização será pela data da disponibilidade ou pela Data Base?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.33.  
  
**Solução:**

O processo de contabilização de arquivos CNAB segue o padrão das demais rotinas do módulo Financeiro, onde o comportamento é definido pelo modo de execução:

1. **Contabilização Online (no processamento da remessa ou retorno):** A contabilização utiliza nativamente a **Data Base** do sistema (campos **E1\_EMIS1/E2\_EMIS2**). Para este modo, não existe um parâmetro que altere a regra para data de disponibilidade.
2. **Contabilização Offline:** Pode ser definida através das perguntas da rotina de processamento, permitindo ao usuário selecionar a opção desejada.contabili  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37901699616407)
