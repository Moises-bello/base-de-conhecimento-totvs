---
article_id: 360005050031
category: Materiais - Compras (SIGACOM)
content_hash: c1cd382ef598c62b39560bbe12f4f91cb769a542bc96e90bdec87ca3fd20fb4e
fetched_at: '2026-06-28T22:41:08.924447+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A120RSPED ao Incluir/Alterar
  um Pedido de Compras e/ou alterar/excluir uma Solicitação de Compras
type: support-article
updated_at: '2025-11-17T18:18:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005050031-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A120RSPED-ao-Incluir-Alterar-um-Pedido-de-Compras-e-ou-alterar-excluir-uma-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**  
O que verificar quando gera mensagem de help A120RSPED no momento de incluir um pedido de compras, e/ou excluir uma Solicitação de Compras que pode estar vinculada a uma solicitação de importação pelo módulo EIC.

O usuário do sistema tentou Incluir/Alterar um Pedido de Compras e/ou alterar/excluir uma Solicitação de Compras e ao clicar em Salvar, gerou a mensagem A120RSPED.

Help: A120RSPED

Problema: Usuário sem permissão para alterar este pedido. Apenas o usuário abaixo pode alterar/excluir este pedido. Usuário: XXXX

**Ambiente**  
Protheus – Compras – A partir da versão 11.80  
  
**Solução**

No padrão do sistema é realizada a seguinte verificação quando **MV\_RESTPED=S (Pedido de Compras) / MV\_RESTCOM = S (Solicitação de Compras):**

Verificar se o campo C7\_GRUPCOM / C1\_GRUPCOM está preenchido  
|\_ Se o campo está preenchido, verificar se o usuário atual logado pertence ao grupo de compras do C7\_GRUPCOM / C1\_GRUPCOM  
| |\_ Se o usuário pertencer ao grupo de compras permitirá a modificação  
| |\_ Se não pertencer retorna o help "A120RSPED"  
|  
|\_ Se o campo não está preenchido verifica se o usuário atual é o mesmo do campo C7\_USER / C1\_USER  
|\_ Se é o mesmo usuário permite a modificação.  
|\_ Se não é o mesmo usuário retorna o help "A120RSPED"

Com base neste tratamento, abaixo recomendação que pode ser realizada para que o seu usuário em questão possa alterar também o pedido de compra:  
• Via Consulta Genérica abrir a tabela SC7 / SC1 e localizar o pedido de compra / SC que o usuário não tem acesso.  
• Verificar o valor do campo C7\_GRUPCOM / C1\_GRUPCOM.  
• Via Client, no módulo de compras, acessar a rotina Atualizações>Adm.Compras>Compradores e cadastrar o usuário desejado como comprador.  
• Acessar a rotina Atualizações>Adm.Compras>Grupo de Compras, e com o valor encontrado anteriormente no campo C7\_GRUPCOM / C1\_GRUPCOM localizar o grupo de compras e altera-lo, incluindo o comprador cadastrado anteriormente. Dessa forma o usuário conseguirá alterar os pedidos de compra / SCs incluídos pelos usuários deste grupo de compras.

***Obs1:***

O campo C7\_GRUPCOM só é gravado quando se utiliza a configuração completa para o Controle/Restrição de Solicitantes, utilizando Grupo de Compras amarrado aos Solicitantes cadastrados.

Informações sobre restriçoes de solicitantes podem ser verificadas, no artigo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é definido cadastro de Solicitantes ( MATA084 ) no Módulo de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007049611) 

No processo de Solicitantes, de forma geral, o campo C7\_GRUPCOM é gravado apenas, quando é seguido o processo de cotação completamente do caminho: Inclusão de SC (por um solicitante cadastrado) |--> Geração de Cotação |--> Analise da Cotação |--> Geração do PC. Neste processo serão gravados os campos: C1\_GRUPCOM, C8\_GRUPCOM e C7\_GRUPCOM.

Caso o processo utilizado for diferente destes relatados, a possibilidade seria através da utilização de ponto de entrada para gravar C7\_GRUPCOM.  
  
Seguem opções de pontos de entrada, caso seja o caso.  
MT120APV - <http://tdn.totvs.com/pages/viewpage.action?pageId=6085466>  
MTA120G1 - <http://tdn.totvs.com/pages/viewpage.action?pageId=6085571>  
MTA120G2 - <http://tdn.totvs.com/pages/releaseview.action?pageId=6085572>  
MTA102G3 - <http://tdn.totvs.com/pages/releaseview.action?pageId=6085573>

***Obs2:***

Caso o campo C7\_GRUPCOM/C1\_GRUPCOM esteja em branco a única forma de os outros usuários terem acesso aos pedidos de compra/solicitações de compras será desativando o parâmetro MV\_RESTPED=N (Pedido de Compras) / MV\_RESTCOM=N (Solicitação de Compras).

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como o Campo C1\_GRUPCOM é Gravado ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414413329687-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-o-Campo-C1-GRUPCOM-%C3%A9-Gravado)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é definido cadastro de Solicitantes ( MATA084 ) no Módulo de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007049611) 

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
