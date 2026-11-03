---
content_hash: 262ce81b167b592391ff6ac0e400446d781c9b0b7eb66b866fe5a31ceeb42521
fetched_at: '2026-06-29T00:09:21.077650+00:00'
page_id: '422545799'
product: rm
source: tdn-rm
title: Regerar Contabilidade (Fiscal)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545799
version: 7
---

Através deste processo o usuário poderá regerar a contabilização do lançamento, poderá ser utilizada se alterar a forma de contabilização de determinado [Evento Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=423938693)[l](http://tdn.totvs.com/pages/viewpage.action?pageId=422545751)ou ainda se os lançamentos foram incluídos sem contabilização, e agora deseja contabiliza-los   
Neste processo é apresentado um filtro onde o usuário poderá definir como sua contabilização será regerada, são eles:

* **Por status do lançamento:**Somente os lançamentos que estiverem com o campo "Contábil" marcado. É necessário possuir o Código do [Evento Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=423938693) l informado na tela de Integração Contábil do lançamento.
* **Por Natureza:**Somente os lançamentos cuja natureza esteja integrada com a Contabilidade. Nesta opção, o sistema irá remontar a contabilização dos lançamentos utilizando o Código do [Evento Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=423938693)  Default da Gestão Fiscal informado neste cadastro.

*****Observações*:****Somente serão remontadas a contabilização de Lançamentos fiscais Contábeis, que não estejam cancelados e que não tenham sido gerados pela rotina de estorno de Lançamentos Fiscais do Sistema de Gestão Fiscal, que pertençam ao Período de Apuração com status aberto. Caso a remontagem não seja executada com sucesso o sistema apresenta um Log de erros.

Ao Regerar Contabilização de Lançamentos ainda não contabilizados o sistema irá respeitar as seguintes informações:  
**Usa Lotes Fiscais Habilitado:**O sistema estará preenchendo com o [Lote Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=423938593) associado ao Lote Fiscal. Se o Lote Contábil do Lote Fiscal não se encontra preenchido, o sistema estará preenchendo com o [Lote Contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=423938593) da Natureza de operação e em último caso o Lote do parâmetro contábil.  
**Usa Lotes Fiscais Desabilitado:**O sistema estará preenchendo com o Lote Contábil selecionado na tela de Remontagem Contabilização. Se este não for preenchido, o sistema estará preenchendo com o Lote Contábil informado na natureza de operação e em último caso o Lote do parâmetro contábil.  
*****Atenção*:****Para a correta execução dos procedimentos acima é necessário o preenchimento do campo Código do Lote Contábilem Ambiente | Parâmetros | TOTVS Gestão Fiscal | 03.05 - Integrações | 03.05.01 - Contábil.  
Se o Lançamento já é contábil, ao regerar a contabilização o sistema preservará o [Lote Contábi](http://tdn.totvs.com.br/pages/viewpage.action?pageId=422546046)[l](http://tdn.totvs.com/pages/viewpage.action?pageId=423938593), da inclusão do Lançamento Fiscal. Neste caso deve-se utilizar a opção Desfazer Contabilização para que a rotina Regerar Contabilização funcione corretamente.
