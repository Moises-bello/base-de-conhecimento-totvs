---
content_hash: b667fd61c6f085152988a0679bea5ddee9f3bd24bd86f4036eb9c09fb97e0fcc
fetched_at: '2026-06-29T00:09:00.867290+00:00'
page_id: '370606703'
product: rm
source: tdn-rm
title: 2862394 MATFATCMPCRM01-3681 DT Funções de Fórmula para buscar informações de
  tributos do movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=370606703
version: 6
---

# Funções de Fórmula para Tributos do Movimento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** |  |
| **Situação/Requisito:** | Necessidade da criação de uma função de fórmula que retorne informações dos tributos do Movimento e Item. |
| **Solução/Implementação:** | Foram criadas duas funções de fórmula com o objetivo de retornar informações dos tributos do Movimento e Item, são elas:   * TABTRBITM - Retorna as informações de tributos do Item de Movimento. Parâmetros: Código do Tributo, Campo e Tipo de Retorno Exemplo: TABTRBITM('ICMS', 'VALOR', 'V') * TABTRBMOV - Retorna as informações de tributos do Movimento Parâmetros: Código do Tributo, Campo e Tipo de Retorno Exemplo: TABTRBMOV('ICMS', 'VALOR', 'V') * SOMATABTRBITM - Retorna o somatório dos tributos do Item de Movimento. Parâmetros: Código do Tributo, Campo e Tipo de Retorno Exemplo: SOMATABTRBITM ('ICMS', 'VALOR', 'V')     Segue abaixo um exemplo de aplicação da função de fórmula SOMATABTRBITM , para realizar a soma de um campo específico dos tributos dos itens do movimento. O campo utilizado foi o Valor do ICMS Desonerado, calculado para cada um dos items.  SOMATABTRBITM ('ICMS', 'VALORICMSDESONERADO', 'V')  Observação: Vale salientar que esta estrutura é aplicável apenas à valores que podem ser utilizados juntamente com operadores aritméticos. Não faz sentido sua utilização para campos cujo tipo de retorno seja Texto (String), ou que usualmente não são somados, como o Motivo de Desoneração do ICMS (MotDesICMS) e Alíquota do Tributo. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 2862394 |
| **Requisito:** | MATFATCMPCRM01-3681 |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
