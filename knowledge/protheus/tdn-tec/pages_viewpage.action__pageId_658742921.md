---
content_hash: afedd3b0c36b2fef2272593eeb0dff2ed5741c7afbddd3320d85d38091750b42
fetched_at: '2026-07-02T19:24:27.600075+00:00'
page_id: '658742921'
product: protheus
source: tdn-tec
title: Falha na geração dos relatórios em formato PDF utilizando o PDFPRINTER
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=658742921
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Ao executar a função File2Printer em um AppServer em ambiente Linux headless enviando o parâmetro "-RFS", ele é ignorado na chamada feita ao executável da pdfprinter. |
| Correção | Adicionado o parâmetro na construção da chamada do comando da pdfprinter feita pela função File2Printer. |
| Informações adicionais | * Referente ao chamado: DTAPPSRV-5057 * Disponível em builds iguais ou superiores a [13.1.3.53](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.53) e [13.2.3.53](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.53). |
