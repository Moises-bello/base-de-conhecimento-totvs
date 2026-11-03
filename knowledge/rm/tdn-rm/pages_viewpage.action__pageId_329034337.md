---
content_hash: 95867389eb8ba13c4f8ae90d3fdfaf1a9138e81ffb8e8a3f9a5a6571d3c217ca
fetched_at: '2026-06-29T00:08:48.999236+00:00'
page_id: '329034337'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-1275 DT Tratamento de Valores de Integração do Educacional
  no Acordo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329034337
version: 2
---

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão Financeira* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FINTRF000269 |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | **FLANBAIXAINTEGRACAO** |

## Descrição

Os valores de integração apresentados no processo de Acordo passam a respeitar os valores calculados pelo valor líquido.

## Procedimento para Implantação

Não é necessário nenhum procedimento para implantação.

## Procedimento para Configuração

Os valores de integração devem ser configurados diretamente no Educacional. Caso existam valores de integração associados a pagamento a maior, e pagamento a menor, os respectivos valores de integração serão incluídos nos lançamentos gerados pelo acordo, sempre com o valor 0 (zero).

## Procedimento para Utilização

       1.           A partir da versão 12.1.20, passa a ser possível definir novos valores de integração no Financeiro, onde podem ser definidas fórmulas que serão executadas durante o procedimento de baixa/acordo:

       2.            O Educacional poderá associar um valor de integração do Financeiro, com fórmula, para definir uma bolsa condicional:

       3.           O respectivo valor de integração é incluído no lançamento, onde é apresentado com o valor 0,00 (zero), indicando o respectivo código da fórmula.

       4.            Ao executar o valor líquido, o valor de integração é calculado:

       5.            Da mesma forma durante o processamento do Acordo:

       6.            Os lançamentos gerados por acordo trarão os respectivos valores de integração para pagamento a maior, e para pagamento a menor. De modo que possam ser usados em uma baixa futura.
