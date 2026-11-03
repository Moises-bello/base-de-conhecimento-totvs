---
content_hash: 62994c4ed1cdfcec940f9032c050340adb1707a4d92920350f21dc7a099dc5c0
fetched_at: '2026-06-29T00:11:03.417248+00:00'
page_id: '622496002'
product: rm
source: tdn-rm
title: Consulta Autorização (retornanotasdepecnx)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=622496002
version: 17
---

Ao consultar a autorização ou cancelamento de uma NF-e é realizada uma integração com o TSS através do  do retorno do TSS para o RM. De acordo com o retorno da nota, a mesma pode ser autorizada, cancelada ou rejeitada conforme regra abaixo.

0NFe PendenteQuando a NFS-e esta pendente o processo esta consultando uma autorização

Quando a NF-e estiver com o Status Pendente e for realizada uma consulta de autorização da mesma o processo irá verificar a regra abaixo.

* Regra geral: neste caso será verificado se o TSS retornou o Grupo **NFE** com os campos **PROTOCOLO,** **XML**e **XMLPROT** preenchidos.

Se ocorrer o comportamento anterior a nota será considerada autorizada.

Senão, se um dos 3 campos (mas não os 3) estiver preenchido (PROTOCOLO, XML ou XMLPROT) será considerado que o TSS ainda está processando a autorização da nota e a mesma permanecerá com o Status Pendente.

Senão, o processo irá executar o serviço  para analisar a situação da nota

Caso o TSS retorne na tag DOCCHV (Chave de Acesso que a nota foi autorizada na SEFAZ) a informação será atualizada no RM.

Comportamento disponível a partir das versões:

- 12.1.31.183  
- 12.1.32.120  
- 12.1.29 ainda não disponível

NFS-e Cancelamento Pendente

Quando a NF-e estiver com o Status Cancelamento Pendente e for realizada uma consulta de autorização do cancelamento da mesma o processo irá verificar a regra abaixo.

* Regra geral: neste caso será verificado se o TSS retornou o Grupo NFERETORNAEVENTO os campos **CSTATEVEN,** **PROT** , **STATUS, XML\_RET**e **XMLPROT** preenchidos.

Evento autorizado **CSTATEVEN**= 155 e **STATUS** = 6 significa que o cancelamento foi aceito fora do prazo

Se ocorrer o comportamento anterior a nota será considerada cancelada.

Senão, o processo irá executar o serviço  para analisar a situação da nota
