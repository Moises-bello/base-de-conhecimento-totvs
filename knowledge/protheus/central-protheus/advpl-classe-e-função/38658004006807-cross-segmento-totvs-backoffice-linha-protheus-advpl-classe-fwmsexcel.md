---
article_id: 38658004006807
category: ADVPL - Classe e Função
content_hash: 5ec008b04eaa1a0a7421134e8f83565772e773a2bdec19c8df77405de2ccc8d2
fetched_at: '2026-06-28T22:40:20.566127+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Classe FWMSExcel
type: support-article
updated_at: '2026-03-03T12:43:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38658004006807-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FWMSExcel
---

A classe FWMSExcel foi depreciada no TOTVS Protheus e não recebe mais suporte. Recomenda-se substituir seu uso pelas novas classes FwMsExcelEx ou FWMsExcelXlsx para garantir conformidade, melhor desempenho e evitar alto consumo de memória ao gerar planilhas extensas.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38658011086103) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**   
Utilização da classe [**FWMSExcel**](https://tdn.totvs.com/display/public/framework/FWMsExcel)?

**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - À partir da Release 12

**Solução**   
A classe `FWMSExcel` encontra-se **depreciada**. Ela não recebe mais manutenções, correções ou inovações.   
  
Além disso, a sua utilização para a geração de planilhas extensas não é mais recomendada, pois pode acarretar um alto uso de memória do servidor.

Para garantir a conformidade e o suporte das rotinas customizadas, é necessário substituir o uso da [`FWMSExcel`](https://tdn.totvs.com/display/public/framework/FWMsExcel) pelas novas classes disponibilizadas, que substituem a sua funcionalidade.

As opções atuais e suportadas para este cenário são:

* [**FwMsExcelEx**](https://tdn.totvs.com/display/public/framework/FWMsExcelEx)
* [**FWMsExcelXlsx**](https://tdn.totvs.com/display/public/framework/FWMsExcelXlsx)

**Passos**

1. Identifique nos códigos-fonte customizados (ADVPL) os pontos onde a classe `FWMSExcel` está sendo instanciada.
2. Substitua a classe depreciada por uma das opções recomendadas ([`FwMsExcelEx`](https://tdn.totvs.com/display/public/framework/FWMsExcelEx) ou [`FWMsExcelXlsx`](https://tdn.totvs.com/display/public/framework/FWMsExcelXlsx)).
3. Realize a adequação da sintaxe no código conforme a documentação técnica das novas classes.
4. Compile a rotina ajustada no seu ambiente de desenvolvimento/homologação e valide a geração do arquivo.

**Saiba Mais**   
[FwMsExcelEx](https://tdn.totvs.com/display/public/framework/FWMsExcelEx)  
[FWMsExcelXlsx](https://tdn.totvs.com/display/public/framework/FWMsExcelXlsx)  
[FWMSExcel](https://tdn.totvs.com/display/public/framework/FWMsExcel)
