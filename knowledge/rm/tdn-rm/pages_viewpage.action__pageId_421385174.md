---
content_hash: de30c0b104683fc1d9c25f9c6ba8467c44b7dd17f79bcd40362388cd08d3d44a
fetched_at: '2026-06-29T00:09:14.263808+00:00'
page_id: '421385174'
product: rm
source: tdn-rm
title: Aprovação via FLUIG de Pedido Extra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385174
version: 4
---

O workflow de aprovação de Pedidos Extra via Fluig irá incorporar ao TOP (Totvs Obras e Projetos) a opção de realizar a aprovação de Pedidos Extra através de um novo caminho além do próprio TOP. **O ambiente Fluig.**   
Através do Pedido de Extra com aprovação via Totvs Obras e Projetos, permite-se elaborar um Pedido ao sistema de BackOffice, sendo que este deverá ser aprovado por algum gestor com permissões para exercer tal ação. Neste pedido o usuário irá incorporar itens que serão solicitados em quantidades de acordo com a necessidade descrita. Ao termino da elaboração do pedido o operador irá submeter esse pedido a aprovação, e neste momento o pedido será encaminhado a quem deverá analisa-lo e aprovar/reprovar o mesmo.  
O workflow irá atuar fornecendo informações via Fluig para que seja possível realizar a aprovação dentro da sua plataforma. O operador aprovador munido de um usuário com permissões para aprovar o workflow irá visualizar no Fluig as mesmas informações visualizadas no TOP, tanto do pedido quanto de seus itens.

**Parametrização:**  
Nos parâmetros gerais aba "Fluig" foi disponibilizado dois novos parâmetros. Esses parâmetros indicarão qual será o processo relativo ao workflow de aprovação de contratos e também quais serão os estados que indicarão que o workflow está "Aprovado" e "Reprovado". Nos parâmetros do Projeto, aba "Integração Fluig" foi adicionado o parâmetro: "Utilizar workflow de aprovação de Pedido Extra".  Este indica ao TOP que os Pedidos Extra serão avaliados no Fluig.  
*Obs: Ao configurar para aprovação via Fluig, é importante salientar que a aprovação tradicional realizada no TOP não será mais efetuada, transferindo todo fluxo para o Fluig.*

**Aprovação total do pedido**  
O workflow de aprovação de Pedido Extra irá acontecer quando o usuário Fluig selecionar prosseguir o workflow para o estado final de "Aprovar", com todos os itens da listagem do formulário e com suas quantidades aprovadas em 100% da quantidade pedida, essa avaliação será feita no momento que o workflow estiver mudando para o estado aprovado.  
Caso seja zerada a quantidade aprovada de todos os itens, ou seja, 0% da quantidade pedida e o workflow prosseguir ao estado Aprovado, automaticamente o mesmo irá atribuir ao workflow o estado Reprovado, já que este é o real estado refletido pelas quantidades aprovadas dos itens.

**Reprovação total do pedido**  
Atribuirá a todos os itens do pedido o percentual associado de 0% e o status de reprovado. No workflow de aprovação de Pedido Extra esse comportamento será representado pelo estado "Reprovar", atribuindo o percentual da quantidade associada de 0% da quantidade pedida.

**Aprovação parcial do pedido e Aprovação parcial dos itens**  
A aprovação parcial de um item, acontece quando o mesmo não tiver sua quantidade aprovada integralmente (menos de 100% da quantidade solicitada).   
Nesse caso, o workflow de aprovação de Pedido Extra irá se comportar com estado de "Aprovar", irá finalizar o pedido e irá encaminhar ao TOP os itens do pedido no estado que o aprovador os deixou. Ao visualizar o workflow de aprovação de pedido, o usuário acessa a aba que irá exibir os dados dos itens, e nesta aba será possível atribuir a quantidade aprovada a um item. Existe também a opção de aplicar um percentual de aprovação sobre a quantidade pedida, bastando apenas informar esse percentual e selecionar quais itens deseja que seja aplicado o percentual na qual refletirá sobre a quantidade desses itens.
