---
content_hash: c7a8cba1c88dcb81d8c9a6bb731fdfd0f46bffeb8358391f555e862e47976f8a
fetched_at: '2026-06-29T00:10:10.440783+00:00'
page_id: '452719838'
product: rm
source: tdn-rm
title: Código de Cálculo 378 - Adiantamento de Abono Pecuniário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719838
version: 2
---

Evento do tipo desconto, valor e sem incidências.  
 Para separar o adiantamento de abono pecuniário de férias do adiantamento de férias no mês, foi criado o CC 378, onde é lançando no evento com o CC 45 somente o líquido referente as férias no mês e, no evento de CC 378 o líquido referente ao abono pecuniário de férias.  
    
 **Exemplo**  
 Funcionário com 20 dias de férias e 10 de abono pecuniário, foram lançadas as seguintes no recibo de férias:

|  |  |  |
| --- | --- | --- |
| CC | Prov./Desc./Base | Referencia |
| CC 38 | 4.984,07 | 20 |
| CC 39 | 2.492,04 | 10 |
| CC 40 | 1.676,46 | 20 |
| CC 56 | 838.23 | 10 |
| CC 0 | 45,21 | 0 |
| CC 47 | 22,65 | 0 |
| CC 82 | 384,86 | 11 |
| CC 30 | 1.781,05 | 27,5 |

No envelope de pagamento foi lançada as verbas acima e os eventos de adiantamento ficou com os seguintes valores:  
 CC 378: R$ 3.352,92 - Que a soma dos eventos de CC 47, 56 e 39  
 CC 43: R$ 4.539,92 - Que a soma dos eventos dos demais eventos menos os eventos de desconto de INSS e IRFF.  
    
 **Observação**  
 Para que este evento seja lançado no Envelope de Pagamento do Funcionário, é necessário que o parâmetro 'Lança Adiantamento de abono separado dos valores de férias' esteja marcado em 'Configurações | Parametrizador | Folha de Pagamento | Férias | Controle.  
 Caso o parâmetro acima não esteja marcado, será lançado o valor do líquido de féria integral no evento de CC 45.  
    
 **Atenção**  
 Os eventos de desconto de INSS e IRRF serão abatidos somente no evento de CC 45, mesmo que no abono pecuniário tenha incidência em IRRF de Férias e INSS. Isto é feito desta forma, pois não tem como separar as bases de cálculo e caso seja separadas o valor da base será menor, podendo até mesmo não ter o desconto, no caso do IRRF de férias, ficando com valores de desconto dos encargos inconsistentes.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
