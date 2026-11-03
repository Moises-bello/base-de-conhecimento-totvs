---
content_hash: d82a049f398551020391f5f14982a168bdedefd51900f78adfc53086059683dd
fetched_at: '2026-06-29T00:10:10.571847+00:00'
page_id: '452719879'
product: rm
source: tdn-rm
title: Evento para Pagamento Média de Férias Proporcional na Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719879
version: 2
---

Este cadastro somente ficará visível quando o parâmetro do sistema **"Separar médias de férias vencidas e proporcionais na rescisão a partir de XX/XX/XX"** estiver marcado, e não permite informar eventos no Grupo 0 (zero). Devem ser utilizados eventos **sem** código de cálculo nos grupos de 1 a 49.  
    
 **Atenção:**  
 A diferença de marcar ou não este parâmetro "Separar médias de férias vencidas e proporcionais na rescisão a partir de:" está na parametrização do Sindicato que será utilizada para calcular as médias de férias PROPORCIONAIS na rescisão.   
    
 No Sindicato existe uma pasta 'Eventos para pagamento e média para férias VENCIDAS e outra para eventos para férias PROPORCIONAIS.  
    
 O cálculo de média das férias PROPORCIONAIS nas rescisões ANTERIORES à data informada seguirá a parametrização   
 da pasta (do Sindicato) de férias VENCIDAS.   
    
 Nas rescisões IGUAIS ou POSTERIORES à data informada, serão consideradas as informações da pasta (do Sindicato)   
 específica de férias PROPORCIONAIS.  
    
 Caso seja marcado o parâmetro, e não seja informada nenhuma data, TODAS as rescisões irão considerar a pasta específica para férias PROPORCIONAIS.  
    
 Caso o parâmetro NÃO seja marcado, TODAS as rescisões irão considerar a pasta de média para férias VENCIDAS, ao calcular as médias de férias PROPORCIONAIS.  
    
 A informação desta data (que marca à partir de quando o parâmetro passou a ser utilizado) é muito importante no caso de uma rescisão complementar, que tem que seguir o mesmo cálculo da rescisão original.  
    
 No campo **Evento para Pagamento** deverá ser informado o evento que receberá o valor da média de férias proporcional pago na rescisão, e no campo **Evento para Diferença**, selecione o evento que concentrará o total da média de férias proporcional no cálculo de Rescisão Complementar.   
    
 Os eventos devem ser previamente cadastrados em Cadastro de Evento.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[Sindicatos](http://tdn.totvs.com.br/display/LRM/Sindicatos)
