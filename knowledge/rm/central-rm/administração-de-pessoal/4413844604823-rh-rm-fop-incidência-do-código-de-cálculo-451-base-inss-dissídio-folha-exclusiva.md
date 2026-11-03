---
article_id: 4413844604823
category: Administração de Pessoal
content_hash: 9e50b66097121357f4421e80c5ac2d1fe6d628f8a102699ab215d9895986e532
fetched_at: '2026-06-28T22:47:02.075264+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Incidência do Código de Cálculo 451 - BASE INSS DISSÍDIO FOLHA
  EXCLUSIVA EMPRESA
type: support-article
updated_at: '2025-03-05T18:46:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413844604823-RH-RM-FOP-Incid%C3%AAncia-do-C%C3%B3digo-de-C%C3%A1lculo-451-BASE-INSS-DISS%C3%8DDIO-FOLHA-EXCLUSIVA-EMPRESA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:05 min****Dúvida**O evento com código de cálculo 451 deve incidir em Incidência exclusiva do empregador. Em qual aba deve ser preenchido, **Inc. Descontos** ou **Inc. Proventos**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Esse evento será lançado automaticamente apenas quando houver diferença salarial por dissidio. Será um evento de **Base de cálculo** do tipo **Valor**.  Este evento será o somatório da diferença calculada dos eventos pagos, que tenham incidência em INSS folha e Incidência Exclusiva do Segurado.    
Deve possuir **Incidência exclusiva do empregador**. Não deve incidir em INSS em hipótese alguma.

O evento terá apenas incidência exclusiva do empregador na aba **Inc. Proventos**, conforme print abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10985378394135)

**Saiba mais**[Exemplo Base INSS Dissídio Folha Exclusiva Empresa e Base INSS Dissídio Folha Rescis. Exclusiva Empresa](https://tdn.totvs.com.br/pages/releaseview.action?pageId=628375896)  
[Código de Cálculo 451 - BASE INSS DISSÍDIO FOLHA EXCLUSIVA EMPRESA](https://tdn.totvs.com/pages/releaseview.action?pageId=628375538)
