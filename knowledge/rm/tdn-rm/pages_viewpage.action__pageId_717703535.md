---
content_hash: 2bdd3c4d97fec502673cc2883b72e3d989460ee326d1f5eb2f290a6367fbd4a6
fetched_at: '2026-06-29T00:11:26.459841+00:00'
page_id: '717703535'
product: rm
source: tdn-rm
title: DT - Autônomos Externos - Opção para exclusão do cadastro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=717703535
version: 13
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Autônomos Externos |
| País: | Brasil |
| Release: | 12.1.2305 |
| Issue: | [DRHROTRM-4005](https://jiraproducao.totvs.com.br/browse/DRHROTRM-4005) |

## **02. SITUAÇÃO/REQUISITO**

Possibilidade para excluir o cadastro do cliente fornecedor.

## **03. SOLUÇÃO**

Para atender as solicitações onde é necessário excluir um cadastro importado ou ajustar dados no cadastro já existe. 

Implementamos o parâmetro "**Permite excluir** **autônomos** **externos**", ao marcá-lo será habilitado a opção de exclusão em Encargos | Autônomos Externos respeitando a permissão do perfil vinculada em cada usuário.

**ATENÇÃO:**

* Ao excluir o cadastro do Autônomo Externo, serão excluídos também todas as informações de vínculos empregatícios com outra(s) empresa(s).
* Para não haver incompatibilidade entre as informações do produto de origem com a folha de pagamento, não disponibilizamos a opção de edição, uma vez que a alteração deverá ser realizada na origem.

## **04. DEMAIS INFORMAÇÕES**
