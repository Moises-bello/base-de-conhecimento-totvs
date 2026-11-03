---
content_hash: eb09e6cecb8f459caaa8b26037565eda417fa7e53672d93cce7793fe9e9875dc
fetched_at: '2026-06-29T00:08:48.597687+00:00'
page_id: '327322485'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-1131 DT Edição de Valores de Integração no Lançamento e na
  Baixa Manual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=327322485
version: 2
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Baixa de Lançamento* |
| **Cadastros Iniciais:** | *O comportamento da baixa está condicionado à configuração de valores de integração no Educacional, devidamente estabelecidos os valores de integração para pagamento a maior e a menor.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FIN000040 |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | FLANINTEGRACAO, FLANBAIXAINTEGRACAO |

## Descrição

Foi alterada a baixa manual de lançamentos financeiros para compatibilizar com os valores de integração para pagamento a maior e pagamento a menor. 

## Procedimento para Implantação

Não é necessário nenhum procedimento específico para implantação no Financeiro.

## Atualizações do Compatibilizador

Não é necessário nenhuma conversão de base de dados no Financeiro.

## Procedimento para Configuração

Os valores de integração devem ser configurados diretamente no Educacional. Caso existam valores de integração associados a pagamento a maior, e pagamento a menor, estes valores poderão ser editáveis no lanamento financeiro e na baixa manual.

## Procedimento para Utilização

1. Ao editar um lançamento financeiro, gerado pelo Educacional, caso exista valores de integração definidos como pagamentos a maior e a menor, estes poderão ser editáveis. Quaisquer outros valores de integração gerados pelo educacional estarão bloqueados para edição pelo Financeiro:
2. Valor de integração editado pelo financeiro:
3. Efeito no valor líquido do lançamento financeiro:
4. Valor líquido inicial no momento da baixa manual:
5. Editando valor de integração durante a baixa manual:
6. Efeito da mudança do valor de integração durante o procedimento de baixa:
7. Item de Baixa gerado:
8. Detalhe dos valores de integração informados no item de baixa gerado:
