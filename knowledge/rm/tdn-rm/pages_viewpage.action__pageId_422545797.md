---
content_hash: 9eb636be5c7ab8209f83923ec57f70b8274be301f07258824cd9fa319802b6ed
fetched_at: '2026-06-29T00:09:21.071443+00:00'
page_id: '422545797'
product: rm
source: tdn-rm
title: Reclassificar Saldo do Prejuízo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545797
version: 5
---

Por esta opção o sistema irá transferir um saldo do prejuízo não operacional para o prejuízo operacional. Gerando um decremento na origem e um incremento no destino.  
***Observação*:**O sistema irá gerar um registro no cadastro de prejuízo do Tipo Operacional e a origem do Tipo Reclassificação e irá gerar um registro no cadastro de Compensações do Tipo Não Operacional e o campo origem igual a Reclassificação. O registro de compensações só servirá para decrementar o saldo disponível para o prejuízo Não Operacional. Este registro não será considerado na soma das compensações do período apurado. Só pode existir uma reclassificação no mês/ Ano para o tributo. A reclassificação só pode ser realizada se o Período de Apuração do Mês / Ano, que está gerando a reclassificação, estiver "Encerrado". A reclassificação deve ocorrer no mês que se identificou o saldo do Prejuízo Não Operacional. Neste mês poderá ocorrer um registro do Prejuízo Operacional "Normal" e um registro do Prejuízo Operacional "Reclassificado". Isso para que este saldo se torne disponível para o período subseqüente. Prejuízos e Compensações do Prejuízo com a Origem "Reclassificação" só podem ser excluídos através da rotina de Estorno da Reclassificação. Isso para garantir a Integridade dos dados. Esta operação deverá excluir simultaneamente o registro de Prejuízo Operacional e da Compensação Não Operacional.

**Este processo deve ser controlado dentro dos eventos tributários do Lalur - Parte B, estando oficialmente descontinuado a partir da versão 12.1.28.**
