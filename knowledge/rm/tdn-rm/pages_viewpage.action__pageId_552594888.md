---
content_hash: 4c7dd305fc0f7e859718f86677df43bc4a30273876e843594c8e93505cc1b0e7
fetched_at: '2026-06-29T00:10:44.490998+00:00'
page_id: '552594888'
product: rm
source: tdn-rm
title: DT- Encargos - Campo “Ordem de cálculo”
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=552594888
version: 15
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Encargos |
| **Situação/Requisito:** | Cliente solicita que o sistema, passe a calcular os encargos  do tipo "A - Valor calculado através de fórmula" de acordo com uma prioridade ou ordem de cálculo, já que existem encargos que necessitam ser calculados antes dos demais, pois compõe a base de cálculo dos outros. |
| **Solução/Implementação:** | Criado o campo "Ordem de Cálculo" para encargos do tipo "A - Valor calculado através de fórmula".  Foi criada a variável de fórmula **VALENCARGOM** para recuperar o valor do encargo calculado anteriormente em memória.  Quando o cliente for calcular um encargo do tipo A - Valor calculado através de fórmula, que utilize o valor de outro encargo do tipo A - Valor calculado através de fórmula, deverá definir a 'Ordem de Cálculo' do primeiro encargo, menor que a 'Ordem de cálculo' do segundo encargo, que será utilizado no cálculo do primeiro encargo e utilizar a variável **VALENCARGOM** para recuperar o valor calculado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 6867349 |
| **Requisito:** | [FOPCALCULO01-10747](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-10747) |
| **Documento de Referência:** | [Encargos](https://tdn.totvs.com.br/display/LRM/Encargos+-+Folha+de+Pagamento)  [Geração de encargos com dependência de valores entre os encargos](https://tdn.totvs.com/pages/editpage.action?pageId=552598669) |
|  | N/A |
