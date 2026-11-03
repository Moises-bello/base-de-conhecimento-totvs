---
content_hash: 7b91a24cb11f8a752d7727c3b7429c171190576411bd376147ff774ae88ec668
fetched_at: '2026-06-29T00:09:22.566469+00:00'
page_id: '422546005'
product: rm
source: tdn-rm
title: Calculo do Crédito de 1/48 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546005
version: 3
---

Para o cálculo do Lançamento Fiscal de 1/48 primeiramente o sistema irá calcular o Percentual de Tributação:   
 **Percentual  Total Tributado do Mês** : Total de Saída do Mês  
 **Cálculo do Total Tributado**: Base reduzida ICMS, exceto as naturezas de exportação  Valor contábil de todas Naturezas de saída exportação.  
 **Cálculo do Total de Saída**: Total Contábil de todas as saídas associadas às Naturezas de Operação com o campo ICMS/IPI Habilitado.

Em seguida calcula o Fator do mês:  
 **Fator do mês(=)****Percentual** : 1/48  
 **Calculo do Percentual**: Esse percentual já foi calculado anteriormente.  
 **1/48**: Significam 1/48 avos das compras relativas ao Ativo Imobilizado, conforme o [Decreto Lei 41.218 de 23/08/2000](http://www.fazenda.mg.gov.br/utilidades/resultado.htm?query=presta%E7%E3o&inicio=6244).   
 **Valor Lançamento 1/48 de cada Bem no mês**(=)**** Fator do mês  Valor Crédito ICMS Integral.  
 Fator do Mês: esse fator já foi calculado anteriormente.  
 **Valor Crédito ICMS**: O valor de crédito do imposto relativo à aquisição, acrescido, quando for o caso, do ICMS correspondente ao serviço de transporte e ao diferencial de alíquotas, vinculado à aquisição do bem.  
 **Valor Total Crédito ICMS no mês** ****(=)**Valor Crédito ICMS de cada bem no mês** **Valor Crédito ICMS de cada bem no mês ... (até quantos bens forem)**   
 Valor Total Crédito ICMS no mês: esse valor já foi calculado anteriormente.   
 Feito isso o sistema gera um único Lançamento Fiscal com esse Valor Total Crédito ICMS, exemplo :   
 Um equipamento adquirido no valor de R$ 1000,00.  
 Total das Saídas do mês...............................................4.084,00  
 Total Tributada do mês..................................................3.950,00  
 Crédito do Imposto  
 (1.000,00  18% **(=)** 180,00)  
 (3.950,00  4.084,00) **(=)** Fração Mensal ........................ 0,9671  
 Cálculo:  
 1) 3950,00  4.084,00 **(=)**0,9671  
 2) 0,9671  48 **(=)** 0,0201  
 3) 0,0201  180,00 **(=)** 3,62

***Observação*:**

* Cada mês terá um coeficiente diferente;
* Cada mês terá um valor à ser Apropriado diferente;
* Essa Apropriação tem prazo de 48 meses ou 4 anos;
* Vencido o prazo de 48 meses, o bem não pode mais ser apropriado. É vedada a Apropriação;

Alienação do Bem: Se o bem sofrer alienação antes de completado o prazo de 1/48 avos, à partir do momento da alienação é vedada a Apropriação do crédito do ICMS, referente à fração que corresponderia ao restante do quadriênio ( Conforme [art. 66 da Parte Geral do RICMS/96](http://www.fazenda.mg.gov.br/empresas/legislacao_tributaria/ricms_2002_seco/partegeral2002_4.htm)).
