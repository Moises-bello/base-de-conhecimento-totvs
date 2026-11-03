---
content_hash: 6308b116a50d0c82cb1ff6618982dffcc0cb21b5f26e53274dffd1036dcdcdb8
fetched_at: '2026-06-29T00:10:10.478238+00:00'
page_id: '452719848'
product: rm
source: tdn-rm
title: Código de Cálculo 208 - Base IRRF RRA Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719848
version: 2
---

É a soma das Bases de IRRF Férias sobre a diferença de Férias processada, somente quando as férias for referente ao ano anterior, considerando que o cálculo é executado no ano atual.   
 Este evento é do tipo base de cálculo, valor e com incidência de desconto em "Estorna IRRF de Férias".  
    
 **Exemplo**  
 Funcionário com cálculo de férias em 01/10/2017 a 30/10/2017  
 Em Junho de 2018 o Funcionário teve um aumento de salário retroativo ao mês 10/2017  
 Executando o processo de Cálculo de Diferença de Férias referente ao período de 2017  
 O sistema calculou os eventos abaixo:  
 CC 86 - R$ 129,40  
 CC 87 - R$ 43,13  
 CC 208 - R$ 172,53  
    
 **Observação**  
 É necessário que o parâmetro "Utiliza Cálculo RRA" esteja marcado no Parametrizador em Configurações | Parâmetros | Parametrizador | Folha de Pagamento | Folha Normal | Geral para que o sistema calcule a base de IRRF de Férias.  
 Quando calculado a diferença utilizando o Cálculo de RRA, é inserido no histórico de RRA vinculado ao funcionário, o valor do evento no campo Valor Total Rend. Tributável, que é informado na DIRF no campo correspondente e deduzido base de rendimentos tributáveis.  
    
 **Atenção**  
 Caso o Funcionário tenha dois períodos de gozo de férias para serem recalculados as diferenças e um deles foi calculado no ano atual, mesmo com o parâmetro marcado, não é somado na base de cálculo IRRF de RRA de Férias o valor da diferença correspondente ao período de gozo do ano atual.  
  

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
