---
article_id: 360034301913
category: RH – DIRF
content_hash: 1e4a222c801bba3c08270defdb08903e52a98425a4708743d4422f925648ca52
fetched_at: '2026-06-28T22:44:06.806921+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir abono pecuniário nos cenários que
  existe abono de férias pagos no mês anterior quando não existir o ID de cálculo
  1449?
type: support-article
updated_at: '2025-08-20T11:12:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034301913-RH-Linha-Protheus-GPE-Como-conferir-abono-pecuni%C3%A1rio-nos-cen%C3%A1rios-que-existe-abono-de-f%C3%A9rias-pagos-no-m%C3%AAs-anterior-quando-n%C3%A3o-existir-o-ID-de-c%C3%A1lculo-1449
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34312587520535)** Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Como conferir abono pecuniário nos cenários que existe abono de férias pagos no mês anterior quando não existir o ID de cálculo 1449?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quando o calculo for gerado sem a verba de ID 1449, os valores de abono mês seguinte serão deduzidos junto com os valores de férias mês seguintes pela a verba de ID 0164. Nesse caso, a conferência deve ser feita somando os valores de abono, abono mês seguinte e férias mês seguinte, e depois deduzindo o valor da verba de ID 0164.  
  
**Exemplo**  
Férias mês seguinte (ID 0073) = R$ 1.000  
Abono pecuniário (ID 0074) = R$ 3.333,33  
1/3 sobre férias mês seguinte (ID 0078) = R$ 333,33  
1/3 sobre abono pecuniário (ID 0079) = R$ 1.111,11  
Abono pecuniário mês seguinte (ID 0205) = R$ 3.333,33  
1/3 sobre abono pecuniário mês seguinte (ID 0206) = R$ 1.111,11  
**Total** : R$ 10.222,21  
**Desconto**Férias pagas mês anterior (ID 0164) = R$ 5.777,77  
**Valor abono pecuniário** **=** R$ 10.222,21 - R$ 5.777,77 = R$ 4.444,44  
  
![](https://tdn.totvs.com/download/attachments/454846958/image2019-2-11_17-21-35.png?version=1&modificationDate=1549920460090&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/454846958/image2019-2-11_17-24-56.png?version=1&modificationDate=1549920460043&api=v2)

**Saiba Mais**  
[Como conferir Abono quando existe Abono de férias pagos no mês anterior?](https://tdn.totvs.com/pages/releaseview.action?pageId=454846958)  
[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
