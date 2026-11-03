---
article_id: 40779432193687
category: Financeiro - Compensação entre Carteiras
content_hash: bc6f1b488416e38069d7ca10463d2aac152459b07bea32a407b06b29cbf399ed
fetched_at: '2026-06-28T22:37:27.004870+00:00'
product: protheus
section_id: 35058659965079
source: central-protheus
title: Cross Segmento - TOTVS Backoffice(Linha Protheus) - SIGAFIN - Regra de exibição
  e filtragem de títulos na rotina FINA450
type: support-article
updated_at: '2026-05-28T11:40:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40779432193687-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Regra-de-exibi%C3%A7%C3%A3o-e-filtragem-de-t%C3%ADtulos-na-rotina-FINA450
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40779432176663)** Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Por que a rotina FINA450 (Compensação entre Carteiras) não apresenta o título do tipo RA (Recebimento Antecipado) filtrado corretamente no momento da compensação?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as releases  
  
**Solução**

Na tela principal de acesso à rotina, os dados em aberto são exibidos de forma geral (reunindo NF, PA e RA). Contudo, no momento em que a ação de compensação é executada, é necessário a seleção via flag sobre quais tipos de titulos devem ser filtrados.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40779432177303)  
  
Com isso o sistema aplica uma filtragem automática e restritiva para garantir a integridade financeira, apresentando os mesmos tipos para as combinações permitidas, conforme exemplo abaixo:

* Compensação entre títulos do tipo NF com NF: **ocorre quando está selecionado o flag para compensar títulos de débitos.**
* Compensação entre títulos do tipo RA com PA: **ocorre quando está selecionado o flag para compensar títulos de créditos.**

Portanto, o sistema filtra e apresenta estritamente as relações NF com NF e PA com RA, não permitindo cruzamentos fora dessa estrutura parametrizada.
