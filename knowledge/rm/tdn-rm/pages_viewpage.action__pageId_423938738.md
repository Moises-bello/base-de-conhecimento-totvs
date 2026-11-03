---
content_hash: 8c0146d8b98e4b23f3eedbfb733b3ddcf2efd6c255661d63829ef1ca98ec5dff
fetched_at: '2026-06-29T00:09:28.651007+00:00'
page_id: '423938738'
product: rm
source: tdn-rm
title: Retorno da Cotação para o Backoffice
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938738
version: 3
---

**Objetivo**

Inserir os orçamentos de cotação vencedores no TOTVS Gestão de Estoque, Compras e Faturamento a partir dos dados inseridos no Portal de Compras Paradigma (WBC – Web Business Center).   
    
 **Sobre o processo**

O Portal de Compras Paradigma será responsável pela total gestão das cotações de requisições de compra, desde o cadastramento até a seleção do orçamento vencedor. Assim sendo, após finalizado o processo de cotação no Portal de Compras, o ERP TOTVS deve ser atualizado com os dados da cotação vencedora, informando o fornecedor ganhador, valor da cotação e outros dados para que possa ser então gerada o pedido de compra.

**Retorno das cotações vencedoras**  
    
 Após as requisições serem integradas ao Paradigma, a cotação ser incluída no portal, os fornecedores informarem o seu orçamento e os itens da cotação serem encerrados no portal, então esses dados deverão voltar ao Backoffice para compor a cotação. Para realizar o procedimento de retorno das cotações vencedoras é necessário selecionar a cotação no ERP TOTVS e acessar "Processo | Retorno de Cotações Orçadas no Portal de Compras Paradigma". Fazendo isso, se o processo for concluído com sucesso, a cotação no TOTVS Gestão de Estoque, Compras e Faturamento, será atualizada com a cotação vencedora do portal. Ao editar a cotação a aba "Orçamentos" será atualizada com os dados do orçamento vencedor como valor orçado, quantidade, fornecedor etc.   
***Importante!***Antes de executar o processo "Retorno de Cotações Orçadas no Portal de Compras Paradigma", os itens da cotação gerada no portal de compras Paradigma deverão ser encerrados, se isso não acontecer ao rodar o processo não será retornado nenhum orçamento.

***Atenção!***Todas as funcionalidades relacionadas ao Quadro Comparativo (geração, visualização, impressão e envio) serão bloqueados, visto que o cálculo de melhor oferta e seleção da mesma é efetuada no Portal de Compras Paradigma.  
    
 Serão inseridos no BackOffice somente os orçamentos vencedores retornados pelo Portal de Compras Paradigma. Assim sendo será desnecessária geração de quadro comparativo, processo de aprovação ou interferência por parte do módulo de Materiais já que todo este processo é realizado no portal de compras paradigma.
