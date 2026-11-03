---
content_hash: 96e7695bfd79a22374da0333b295fd5a6ff32e9a85b15bc78cd724e58e4939be
fetched_at: '2026-07-02T19:24:21.303920+00:00'
page_id: '266972405'
product: protheus
source: tdn-tec
title: 4GL - Alteração do tamanho limite da string
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266972405
version: 2
---

4GL - Alteração do tamanho limite da string

|  |  |
| --- | --- |
| Situação | 4GL - Alteração do tamanho limite da string |
| Ocorrência | Limite do tamanho da string de 1MB era insuficiente para a linguagem 4GL |
| Melhoria | Implementado para o Logix ( ServerType = 4GL) o limite default de 10MB para o tamanho de string. Este limite está condicionado a definição da chave de ambiente SERVERTYPE=4GL na seção GENERAL do arquivo de ini do AppServer. Caso a chave MAXSTRINGSIZE esteja definida, está tem prioridade sobre a SERVERTYPE. |
| Informações adicionais | * Referente ao chamado: Não há chamado associado * Referente à ocorrência: TTEC-657 * Disponível em builds superiores a 7.00.131227A - 1.0.3 |
