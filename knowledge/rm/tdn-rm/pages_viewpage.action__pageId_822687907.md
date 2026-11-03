---
content_hash: b17565e6d57590fc5d747ebf01b36d52c215e5c54c7fb81b53d13ea445575df1
fetched_at: '2026-06-29T00:11:46.504564+00:00'
page_id: '822687907'
product: rm
source: tdn-rm
title: serv/infoCompl
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822687907
version: 8
---

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **infoCompl** | **DPS/serv/** | **Não** | **Grupo** | **Grupo de informações complementares disponível para todos os serviços prestados.** |
| idDocTec | DPS/serv/infoCompl | Não | Não é gerado |  |
| docRef | DPS/serv/infoCompl | Não | Não é gerado |  |
| xInfComp | DPS/serv/infoCompl | Não | Gerado conforme a regra de . | Campo livre para preenchimento pelo contribuinte, limitado a 2000 caracteres.   O texto informado será submetido a expressão regular [^A-Za-z0-9\.\,], para remover os caracteres especiais não aceitos. O sistema também removerá espaços em branco ao final da frase.  Exemplo: Se antes a discriminação fosse: "Nota Fiscal referente ao serviço de educação superior " O conteúdo gerado no XML seria: <infoCompl>Nota Fiscal referente ao servico de educacao superior</infoCompl> |
