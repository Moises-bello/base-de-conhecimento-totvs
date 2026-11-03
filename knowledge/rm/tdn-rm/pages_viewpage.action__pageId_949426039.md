---
content_hash: fa416bf3ce3ec69653b9b96e4de7bd36d2d2ea2559a8a046da909e27b401a73c
fetched_at: '2026-06-29T00:12:10.080148+00:00'
page_id: '949426039'
product: rm
source: tdn-rm
title: 'FISCAL01-25637 - NF-e - Rejeição 817: Unidade Tributável incompatível com
  o NCM informado na operação com Comercio Exterior'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=949426039
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão de Estoque |
| Função: | NF-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25637 |

## **02. SITUAÇÃO/REQUISITO**

Solicitação de validação do que pode ser feito no sistema para o cliente conseguir emitir a nota fiscal, gerando corretamente a tag **<cEANTrib>** , sem precisar alterar a sua Unidade de Controle. Visto que para atender exigências da Sefaz (como na tabela NCM), é necessário informar uma unidade específica (como KG) na nota fiscal e o cliente não pode alterar a sua Unidade de Controle\* (FD)\* , pois isso afetaria todo o controle de estoque e operações comerciais internas dele .

## **03. SOLUÇÃO**

Para tornar esse cenário possível de envio sem ocasionar rejeições, foi disponibilizado os campos Unidade de Medida e Código de Barras referente ao grupo Exterior no cadastro do produto:

Não é obrigatório o preenchimento dos campos para todos os produtos. Verifique a necessidade dos produtos da empresa e preencha a opção adequada a sua necessidade.

Os valores informados nos campos Código de Barras e Unidade Tributável dentro do grupo Exterior, serão levados para o XML e exibidos nas TAG <EANTrib> e  <uTrib> no grupo I - Produtos e Serviços da NF-e.

Lembrando que estes campos seguirão as regras de tamanho e quantidade definidos no manual do contribuinte

Disponível à partir da biblioteca 12.1.2406
