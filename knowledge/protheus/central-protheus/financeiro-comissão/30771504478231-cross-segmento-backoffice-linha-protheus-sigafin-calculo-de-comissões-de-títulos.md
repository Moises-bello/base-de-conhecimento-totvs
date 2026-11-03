---
article_id: 30771504478231
category: Financeiro - Comissão
content_hash: e50baa83507b5271651bc3ee4c84641f36d5904c74b13208540722047e1392f0
fetched_at: '2026-06-28T22:37:50.689124+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Calculo de comissões
  de títulos com impostos
type: support-article
updated_at: '2025-03-19T18:40:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30771504478231-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Calculo-de-comiss%C3%B5es-de-t%C3%ADtulos-com-impostos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30771458470551) Tempo aproximado para leitura: **00:05 min** **Dúvida**Como fazer para considerar os impostos no cálculo de comissão?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Baixa variação cambial - Todas as versões   
  
**Solução**

Os parâmetros responsáveis pelo tratamento da retenção de impostos na comissão são:

* **MV\_COMISIR** – IRRF
* **MV\_COMIINS** – INSS
* **MV\_COMIPIS** – PIS
* **MV\_COMICOF** – COFINS
* **MV\_COMICSL** – CSLL

### **Configuração dos Parâmetros:**

a) Para que os valores de **retenção** dos impostos **não sejam incluídos** na base de cálculo da comissão, os parâmetros devem ser configurados com **"N" (Não)**. Dessa forma, a comissão será calculada sobre o valor líquido (**valor do título – impostos**).

b) Para que os valores de **retenção** dos impostos **sejam incluídos** na base de cálculo da comissão, os parâmetros devem ser configurados com **"S" (Sim)**. Nesse caso, a comissão será calculada sobre o **valor total do título**.

**Para mais detalhes**

[FINA440 - Calculo de comissões de títulos com impostos](https://tdn.totvs.com/pages/releaseview.action?pageId=550308062)

**Saiba mais**

[Recálculo de Comissões (FINA440 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528)
