---
article_id: 22165375629975
category: Originação de Grãos (OG)
content_hash: d505a6f85ba8573eb27c9187392d95c6b78cf95e7f1148b00b575c8709a331f0
fetched_at: '2026-06-28T22:45:38.887386+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Cotação - Moedas Diferentes na Nova Comercialização
type: support-article
updated_at: '2024-07-03T21:17:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22165375629975-Agro-Linha-Protheus-AGR-Cota%C3%A7%C3%A3o-Moedas-Diferentes-na-Nova-Comercializa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22165375602199) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Como realizar uma Cotação de Moedas Diferentes na Nova Comercialização?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para solucionar essa dúvida, a **fixação de preço ou componente** devem ocorrer em outra moeda, sendo assim o Sistema realizará as conversões necessárias.   
Na tabela de componentes, o valor tem que ser informado na **moeda do componente**. Caso ela seja diferente da **moeda do contrato**, ocorre a conversão utilizando a taxa do campo Cotação.  
O valor convertido é exibido no campo **R$ / UN** (**UN é a unidade de medida do componente que é exibida dinamicamente**).  
O componente de resultado sempre assume a moeda que foi definida para o contrato, nesse caso hajam componentes que façam parte da sua formação com moedas diferentes, a conversão também é realizada.  
Já na **regra fiscal** do contrato, quando este é definido como interno, mas a moeda do contrato é em dólar, os valores são apresentados nas seguintes **moedas da tabela**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22165379293975)
