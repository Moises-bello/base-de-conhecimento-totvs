---
article_id: 14153642287767
category: Financeiro - Compensação entre Carteiras
content_hash: 2817a0a51bd6143858468f394461f09d1a61649d385242b924d7a62588659556
fetched_at: '2026-06-28T22:37:26.990128+00:00'
product: protheus
section_id: 35058659965079
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  - FINA450  - Como alterar
  ou cadastrar taxa contratada na compensação entre carteiras
type: support-article
updated_at: '2026-02-23T12:48:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14153642287767-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA450-Como-alterar-ou-cadastrar-taxa-contratada-na-compensa%C3%A7%C3%A3o-entre-carteiras
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38573624364823)** Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**  
Como alterar ou cadastrar taxa contratada na compensação entre carteiras?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
A rotina de **Compensação entre Carteiras - FINA450**, não possui a funcionalidade de alterar ou informar a taxa contratada no momento da compensação.  
Porém, temos o ponto de entrada **MTXMOEDA**, que poderá ser utilizado para alterar a taxa a ser passada para a função que irá realizar a conversão dos valores, onde pode verificar se é aderente à necessidade e processo.   
  
Segue a documentação do ponto de entrada:  
[MTXMOEDA - Altera o valor de retorno da conversão](https://tdn.totvs.com/pages/viewpage.action?pageId=6085594)  
  
**Importante**  
Este ponto de entrada é executado por todas as rotinas e processos que realizam conversões de valores entre moedas, desta forma as validações e verificações devem ser implementadas validando a rotina e processo desejado.
