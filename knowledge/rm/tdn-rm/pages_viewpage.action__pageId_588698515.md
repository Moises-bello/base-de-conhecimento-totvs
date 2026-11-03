---
content_hash: fab60ed69149b66701fc011d411850f5b84cdb17856fe8dd417e813a26d40867
fetched_at: '2026-06-29T00:10:53.862490+00:00'
page_id: '588698515'
product: rm
source: tdn-rm
title: Consultar Autorização de NFS-e (retornanfse)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=588698515
version: 11
---

Ao consultar a autorização ou cancelamento de uma NFS-e é realizada uma integração com o TSS através do  através do retorno do TSS para o RM a nota pode ser autorizada, cancelada ou rejeitada conforme regra abaixo.

0NFS-e PendenteQuando a NFS-e esta pendente o processo esta consultando uma autorização

Quando a NFS-e estiver com o Status Pendente e for realizada uma consulta de autorização da mesma o processo irá verificar a regra abaixo.

* Regra geral: neste caso será verificado se o TSS retornou o Grupo **NFE** com os campos **PROTOCOLO,** **NUMNSE** e **XMLPROT** preenchidos.
* Estância Velha: neste caso será verificado se foi retornado Grupo **NFE** com os campos **PROTOCOLO** e **NUMNSE** preenchidos.

Se ocorrer o comportamento anterior a nota será considerada autorizada.

Senão, se um dos 3 campos (mas não os 3) estiver preenchido (PROTOCOLO, NUMNSE ou XMLPROT) será considerado que o TSS ainda está processando a autorização da nota e a mesma permanecerá com o Status Pendente.

Senão, o processo irá executar o serviço  para analisar a situação da nota

NFS-e Cancelamento Pendente

Quando a NFS-e estiver com o Status Cancelamento Pendente e for realizada uma consulta de autorização do cancelamento da mesma o processo irá verificar a regra abaixo.

* Regra geral: neste caso será verificado se o TSS retornou o Grupo **NFECANCELADA**com o campo **PROTOCOLO**preenchido.

Se ocorrer o comportamento anterior a nota será considerada cancelada.

Senão, o processo irá executar o serviço  para analisar a situação da nota
