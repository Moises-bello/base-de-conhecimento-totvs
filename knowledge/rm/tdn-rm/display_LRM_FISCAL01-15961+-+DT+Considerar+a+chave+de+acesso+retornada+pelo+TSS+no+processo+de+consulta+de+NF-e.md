---
content_hash: 111885bce541167d38293a2acee4860f59d4c45f03202d80cc122eeb27d84e71
fetched_at: '2026-06-29T00:11:04.306666+00:00'
page_id: '626149959'
product: rm
source: tdn-rm
title: FISCAL01-15961 - DT Considerar a chave de acesso retornada pelo TSS no processo
  de consulta de NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-15961+-+DT+Considerar+a+chave+de+acesso+retornada+pelo+TSS+no+processo+de+consulta+de+NF-e
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Consulta de NF-e |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15961 |

## **02. SITUAÇÃO/REQUISITO**

Após as implementações da issue [~~FISCAL01-15881~~](https://jiraproducao.totvs.com.br/browse/FISCAL01-15881 "Alterar IDTSS para não ser atualizado "), a chave de acesso para a nota autorizada pode ser diferente da ultima chave de acesso enviada pelo ERP. Inclusive, a própria nota pode estar diferente, pois como houve uma rejeição indevida o cliente pode ter modificado o movimento.

Para resolver o problema, da chave, o TSS passará a retornar a chave na qual a nota foi autorizada através do método RetornaNotasDepecNx e precisamos considerá-la no processo de consulta de NF-e atualizando o registro da TNFEESTADUAL

## **03. SOLUÇÃO**

Foi alterado o processo de Consulta da NF-e para que atualize a Chave de Acesso da NF-e caso esteja preenchida no retorno do TSS.

Caso a chave de acesso da Nota autorizada na SEFAZ seja diferente da chave de acesso do sistema, será exibido a seguinte mensagem orientando ao usuário a validação da Nota.

Disponível a partir das versões abaixo:

- 12.1.31.183  
- 12.1.32.120  
- 12.1.29 ainda não disponível
