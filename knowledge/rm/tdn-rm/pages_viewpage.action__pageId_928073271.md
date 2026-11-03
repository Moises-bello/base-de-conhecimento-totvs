---
content_hash: af63e40fdd2e04313260f4ef67fbad6b01a363cc92d57117e851364a48922e96
fetched_at: '2026-06-29T00:12:08.021718+00:00'
page_id: '928073271'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Desconcatenação da Coligada no Sindicato e Eventos/Verba
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=928073271
version: 6
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Ahgora - Desconcatenação da Coligada no Sindicato e Eventos/Verba |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-12819](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12819) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.257
* 12.1.2410.200
* 12.1.2502.121

## **03. SITUAÇÃO/REQUISITO**

Adequação da integração do TOTVS Folha de Pagamento com o produto Ponto Web da Ahgora, removendo a concatenação do prefixo do código da coligada ao código do sindicato e às verbas.

## **04. SOLUÇÃO**

O produto foi ajustado para remover a concatenação do prefixo do código da coligada no cadastro de sindicato (Api Funcionários) e verbas (Api Resultado) integradas entre o TOTVS Folha de Pagamento e o Ponto Web da Ahgora.

**Json enviado na integração com o PW.**

**Informação apresentada na plataforma do Ponto Web Ahgora.**

**ATENÇÃO:**

* As verbas são integradas do produto Ponto Web da Ahgora para o TOTVS Folha de Pagamento. A tratativa para o recebimento dessas verbas, sem a concatenação do prefixo do código da coligada, está disponível a partir das versões mencionadas no início deste documento.

* A concatenação do código da coligada ao código do sindicato e eventos foi removida devido à implementação de uma melhoria no processo de cadastro desses itens no Ponto Web da Ahgora. Com essa alteração, os códigos passarão a ser vinculados diretamente aos respectivos CNPJs, evitando problemas de duplicidade entre diferentes CNPJs. Para mais detalhes sobre essa mudança, recomendamos entrar em contato com o time do Ponto Web Ahgora.

## **05. DEMAIS INFORMAÇÕES**

**[Integração RM X Ahgora](https://tdn.totvs.com/pages/viewpage.action?pageId=877866931)**

**[Integração RM X Ahgora - API Resultados - Documentação Técnica](https://tdn.totvs.com/pages/viewpage.action?pageId=867812432)**
