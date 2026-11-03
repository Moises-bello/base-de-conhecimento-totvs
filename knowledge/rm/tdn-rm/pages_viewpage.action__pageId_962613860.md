---
content_hash: 06eb18b4b5c13a9ea3e7aa80440d23fe7698c43872c1accc81c98af8476354ca
fetched_at: '2026-06-29T00:12:13.989148+00:00'
page_id: '962613860'
product: rm
source: tdn-rm
title: FISCAL01-24721 - Local de prestação de serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=962613860
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Envio NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-24721 |

## **02. SITUAÇÃO/REQUISITO**

Ao enviar NFS-e, passar a gerar a tag <codmunibge> com base no campo "Local de Prestação" em: Anexo | dados fiscais do produto | sub pasta: Tributação.

## **03. SOLUÇÃO**

Ao  Enviar a NFS-e a tag <codmunibge> é gerada com a seguinte regra:

**Origem**: Município do Cadastro do Filial (Movimento de Venda\Lançamento de Saída)  ou município do cadastro Cliente\Fornecedor (Movimento de Compra\Lançamento de Entrada)

**Destino**:  Município do cadastro Cliente\Fornecedor(Movimento de Venda\Lançamento de Saída) e  Município do Cadastro do Filial (Movimento de Compra\Lançamento de Entrada)

**Local** **Incidência:**Município informado no movimento (Integrações | Fiscal | Município).

**Importante**: quando o movimento possuir mais de um item e os itens possuírem locais de prestação diferentes ou não possuírem local de prestação informado, a tag será gerada como **Local de Incidência.**
