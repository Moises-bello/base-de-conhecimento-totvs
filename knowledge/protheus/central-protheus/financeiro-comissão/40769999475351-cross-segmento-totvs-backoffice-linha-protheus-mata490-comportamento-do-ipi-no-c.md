---
article_id: 40769999475351
category: Financeiro - Comissão
content_hash: 0c28ad6b7de9a6bbe91cc906df92e12282207209aa03fec68876b5550f137131
fetched_at: '2026-06-28T22:37:50.749353+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - MATA490 - Comportamento
  do IPI no cálculo de comissão
type: support-article
updated_at: '2026-05-27T18:59:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40769999475351-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-MATA490-Comportamento-do-IPI-no-c%C3%A1lculo-de-comiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40769988143127) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Qual é o comportamento do sistema em relação ao IPI na base de cálculo da comissão do vendedor?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
O cálculo da comissão em relação ao IPI depende da configuração estabelecida no **Cadastro de Vendedor**, através do campo **Base c/ IPI**. O sistema se comporta das seguintes maneiras de acordo com o preenchimento deste campo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40769988145815)

* **Quando configurado com "SIM":** O valor do IPI gerado no título é adicionado à base de cálculo da comissão. **Exemplo:** em uma venda em que o valor é de **R$ 10.000** e o IPI é de 3% (**R$ 300**), o valor total do título gerado será **R$ 10.300** A comissão será calculada sobre a base totalizada com o IPI **R$ 10.300**. Sendo a comissão do vendedor de 5%, o valor a ser pago será de **R$ 515**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40770025878039)

* **Quando configurado com "NÃO":** O valor do IPI gerado no título não é somado à base de cálculo da comissão. **Exemplo:** Na mesma situação de um título de **R$ 10.000** com IPI de 3% (**R$ 300**) totalizando **R$ 10.300**, a base para a comissão permanecerá sendo apenas os **R$ 10.000** originais. Aplicando os mesmos 5% de comissão, o valor a ser pago será de **R$ 500**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40770025881495)

**Importante**

Após gerar a comissão com uma das opções mencionadas acima, caso seja necessário realizar alguma alteração, basta ajustar o cadastro do vendedor e executar a rotina de **recálculo de comissão** **FINA440**.

**Saiba mais**

[Recálculo de Comissões (FINA440 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528#Rec%C3%A1lculodeComiss%C3%B5es(FINA440SIGAFIN)-Tratamentodeimpostos)
