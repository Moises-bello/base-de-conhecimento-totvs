---
content_hash: 54812e19fd8c493330bd5e7cdf7ddb2a60f669153d88cc09d9f4efde7c2cb68b
fetched_at: '2026-06-29T00:09:24.477698+00:00'
page_id: '423937923'
product: rm
source: tdn-rm
title: Controle de Apontamento da Atividade 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937923
version: 6
---

Através desse processo é possível Realizar/ Finalizar o apontamento de uma atividade.  
Ao acessar esse processo será apresentada a tela de Controle de Apontamento da Atividade, na qual é possível inserir informações da quantidade realizada da atividade, materiais consumidos e perdidos, subprodutos gerados, data hora de alocação de recursos (posto, mão de obra e equipamento), índices de registro de produção e paradas da atividade.

**Cabeçalho**  
    
 Nessa aba serão apresentadas as informações referente a Estrutura Feita, Data Hora Início e Final da atividade, e Quantidades de Execuções previstas e Efetivadas para a atividade.  
Está disponível para ser informada a quantidade apontada da atividade, e quantidade de produtos apontados e perdidos (somente para atividade produtora).   
É possível definir se os materiais consumidos, subprodutos gerados e trabalho efetivo na atividade serão calculados proporcionalmente em relação a quantidade executada da atividade.  
***Observação*:**A produção apontada como perdida deverá ser enviada ao estoque através do tipo de movimento de perda de material parametrizado, os produtos apontados como perdidos entrarão no local de estoque parametrizado para perda de material.  
    
**Material Consumido**  
    
 Através dessa aba serão inseridos os materiais e suas quantidades consumidas na execução da atividade.   
Caso o produto consumido seja controlado por lote ou número de série será necessário informar tais dados na parte inferior da tela, que será habilitada somente para produtos com esses controles.  
**Importante:**Estarão disponíveis para seleção lotes e/ou números de séries empenhados ou disponíveis no [Estoque Imtermediário](http://tdn.totvs.com/pages/viewpage.action?pageId=423938071)  (baixados) para a ordem de produção que estiver sendo apontada. (Caso o sistema esteja parametrizado para trabalhar com [Empenho](http://tdn.totvs.com/pages/viewpage.action?pageId=423938069) ). Se o sistema NÃO estiver parametrizado para a utilizar [Empenho](http://tdn.totvs.com/pages/viewpage.action?pageId=423938069) estarão disponíveis para escolha lotes e/ou números de séries disponíveis no [Estoque Imtermediário](http://tdn.totvs.com/pages/viewpage.action?pageId=423938071) (baixados) para a ordem de produção apontada, e também os lotes e/ou números de série do produto disponíveis (e não consumidos em outras ordens de produção) nos [Locais de Estoque](http://tdn.totvs.com/display/LRM/Locais+de+Estoque) parametrizados no TOTVS Planejamento e Controle da Produção.  
    
 **Perda Material**

As informações dessa aba devem ser preenchidas caso algum material tenha sido perdido na execução da atividade, deve ser informando o produto que foi perdido, a quantidade e seus números de lote e série, caso o produto possua esse controle.  
***Observação*:**Todo material apontado como perdido deverá ser baixado do estoque e ao fim da produção deverá ser realizada a entrada  para estoque do mesmo através do tipo de movimento parametrizado para entrada de perda de material. O material perdido entrará para o estoque no local de perda de material parametrizado.  
**Importante:**Os materiais perdidos terão seu custo valorado de acordo com o custo do produto no TOTVS Gestão de Estoques, Compras e Faturamento, entretanto, esse custo não afeta a composição do custo da ordem de produção.  
     
 **Subproduto Gerado**  
    
 Nessa aba pode-se informar o(s) subproduto(s) e sua(s) respectiva(s) quantidade(s) que a execução da atividade gerou.   
Pode ser informado o percentual do custo da atividade que será determinado como custo do subproduto.  
Também é possível definir se o custo do subproduto será debitado do custo total de produção.  
     
 **Trabalho Efetivo**  
    
 Nessa aba deverá ser informada a Data Hora Início e Final de trabalho efetivo na atividade.   
A mão de obra e equipamento informados serão alocados na atividade e terão seu custo calculados conforme esse intervalo de Data/Hora.  
     
 **Índice de Registro de Produção**  
    
 Permite inserir Índice(s) de Registro(s) de Produção para a atividade e seu(s) respectivos(s) Registro(s) de Qualidade.   
Nessa aba é possível informar a quantidade de amostras e índice aferidos, além de comentários sobre o Índice de Registro de Produção que afetou a atividade.   
Caso o índice informado esteja fora da faixa cadastrada do [Índice de Registro de Produção](http://tdn.totvs.com/pages/viewpage.action?pageId=423938066) será habilitada na parte inferior da tela a inclusão do Registro de Qualidade.   
No Registro de Qualidade deverá ser informado o [Motivo da Não Conformidade](http://tdn.totvs.com/pages/viewpage.action?pageId=423937913), a atividade corretiva, o responsável e a ação corretiva realizada.  
   
 **Parada de Atividade**  
    
 Nessa aba é possível informar um intervalo de tempo em que a atividade ficou parada.  
Deve ser informada a [Razão da Parada](http://tdn.totvs.com/pages/viewpage.action?pageId=423937908), o agente da parada (caso exista), e o intervalo de tempo em que a atividade ficou parada, intervalo esse definido através dos campos Data Hora Início e Data Hora Final.

***Dica***É possível navegar entre as abas na tela de apontamento utilizando atalhos do teclado, os mesmos são:

|  |  |
| --- | --- |
| **Aba** | **Atalho** |
| Cabeçalho | ALT + D |
| Material Consumido | ALT + M |
| Perda Material | ALT + P |
| Subproduto Gerado | ALT + S |
| Trabalho Efetivo | ALT + T |
| Registro de Produção | ALT + Q |
| Parada de Atividade | ALT + I |
| Apontamentos (Habilitada na Correção) | ALT + A |
