---
content_hash: 8621d092ffbd56745e7a167dd6140c191d0b9836bed79854de90406e9a8dc8f8
fetched_at: '2026-06-29T00:09:14.950040+00:00'
page_id: '421385314'
product: rm
source: tdn-rm
title: Definir Preços da Composição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385314
version: 2
---

Através dessa janela, pode-se definir o valor total de uma composição. Este valor pode ser maior ou menor do que o valor atual.

**Atenção:**  
O Processo de "Definir preço de composição" só será executado para composição do tipo CPU (Composição por Preço Unitário).  
Para se chegar no valor desejado, são feitos ajustes nos coeficientes dos recursos para atingir o valor solicitado. A distribuição é feita proporcionalmente. Por essa razão, vão ocorrer situações em que o valor não será idêntico ao valor solicitado. Portanto, ainda pode-se fazer uma nova aproximação do valor solicitado. Mas, chegará um momento em que não será possível efetuar novas aproximações. A cada aproximação é feito um recálculo e tenta-se chegar ao valor solicitado.

Preço unitário Atual:   
 Exibe o valor unitário da composição.   
 Preço Unitário Desejado: Informe para qual valor deseja-se modificar a composição.  
 Num. Max. Iterações: Informe quantas iterações devem ser feitas para se chegar no preço unitário desejado.  
 Margem de Erro (%): Informe o percentual de margem de erro aceitável.  
 Preço Unitário calculado: Exibe o valor unitário calculado da composição, após a simulação de acordo com o preço Unitário desejado.

Caso o número máximo de iterações seja atingido antes do % da margem de erro o cálculo poderá prosseguir para que você consiga atingir o valor desejado dentro da margem de erro.  
Caso a margem de erro seja atingida antes do número máximo de interações o cálculo é finalizada, pois foi atingida a precisão solicitada.  
Os seguintes recursos são invariáveis: Marque os recursos que não podem ter o coeficiente alterado pelo processo de definição do preço da composição.  
  
Os recursos que possuírem algum tipo de fórmula para o seu cálculo já virão marcados na listagem de recursos invariáveis. Estes recursos não poderam ser alterados.  
A visão disponibiliza:  
 Simular Cálculo – A simulação irá tentar propor um novo valor para a composição próximo ao valor desejado, mas os dados apenas serão salvos após clicar no botão Recalcular composição.  
Recalcular composição - Para confirmar a alteração do preço da composição, recalculando as quantidades dos recursos que não são invariáveis.

**Atenção:**  
Para recalcular uma composição com o preço unitário desejado, é necessário executar pelo menos uma simulação de cálculo antes.
