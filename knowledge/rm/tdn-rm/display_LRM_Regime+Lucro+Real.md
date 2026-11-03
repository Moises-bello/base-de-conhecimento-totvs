---
content_hash: 678d544989b6a0366afe31bad6203b53d51d2bff30a3a93e616cb05e986fba01
fetched_at: '2026-06-29T00:09:21.096395+00:00'
page_id: '422545811'
product: rm
source: tdn-rm
title: Regime Lucro Real
type: documentation
url: https://tdn.totvs.com/display/LRM/Regime+Lucro+Real
version: 7
---

O Lucro Real é a sistemática de apuração da base de cálculo do IR, que considera os registros contábeis e fiscais efetuados de acordo com as leis comerciais e fiscais. O lucro real é o lucro contábil depois de considerados os ajustes de adições, exclusões e compensações prescritas e autorizadas pela legislação fiscal. Esses ajustes são valores de receitas e despesas que a legislação tributária entende que podem ou não ser consideradas na determinação da base de cálculo dos tributos em tela.  
 Para que os valores sejam apurados corretamente todas as Contas Contábeis precisam estar conciliadas, ou seja, lançamentos no Lote Zero.  
 As pessoas jurídicas deverão apurar trimestralmente o imposto de renda com base no Lucro real.   
O **Lucro Contábil** será retornado pela  [TOTVS Gestão Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=198948832) através da parametrização da DRE e Fatos Contábeis no [Evento Tributário](http://tdn.totvs.com/pages/viewpage.action?pageId=422545748), assim como os resultados operacional e não operacional. Esses últimos serão utilizados no controle da Compensação de prejuízo.   
 Ao Lucro Contábil deve ser adicionado o resultado do Grupo "**Adições e Adições por Doação**" e excluído o resultado do grupo "**Exclusões**".   
 Com isso temos o **Lucro Real antes da Compensação de Prejuízos**. Desse resultado deduzimos o valor do prejuízo que foi calculado no Grupo "**Compensação de Prejuízo**" e chegamos ao **Lucro Real**.  
 Se for apurado prejuízo, o sistema deve apresentar ao usuário um log ao final do processo de apuração, informando que foi apurado prejuízo e seu valor, separado em prejuízo operacional e não operacional. O usuário deverá, manualmente, cadastrar as contas de compensação de prejuízo na Parte B do LALUR.  
    
 **Calculo do Tributo**  
    
   
    
 **Imposto a Pagar**   
    
   
***Observação*:**No caso do Adicional só se aplica ao tributo IRPJ. O imposto devido será calculado mediante a aplicação da alíquota (informada no cadastro de período pasta Apuração) sobre a base de cálculo.

***Atenção!*** Para apuração dos tributos IRPJ e CSLL Lucro Real será apresentado um SubGrupo **Adições por Doação**. Ao encerrar o período de  apuração do IRPJ o CSLL o sistema irá fazer o seguinte cálculo:

* **Adição por Doação: (DOAÇÕES  (RESULTADO OPERACIONAL  DOAÇÕES)** ¹ Doação){\*}

***Observação***: O imposto de renda devido será calculado mediante a aplicação da alíquota (informada no cadastro de período, Pasta Detalhamento) sobre a base de cálculo.

Para apuração dos tributos IRPJ e CSLL Lucro Real será apresentado um SubGrupo **Adições por Doação**.  
Ao encerrar o período de  apuração do IRPJ o CSLL o sistema irá fazer o seguinte cálculo:

**Adição por Doação: (DOAÇÕES (RESULTADO OPERACIONAL  DOAÇÕES)** ¹ Doação)\*  
**Onde¹** = sinal de divisão "/"
