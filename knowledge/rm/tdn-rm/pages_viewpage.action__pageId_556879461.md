---
content_hash: fbbb6ffd14bfeb59cc865d0284ba71e7ed93fc93f4da375f8a14a1e37928b62d
fetched_at: '2026-06-29T00:10:47.392585+00:00'
page_id: '556879461'
product: rm
source: tdn-rm
title: DT- Calculo de INSS de Férias para Múltiplos Vínculos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=556879461
version: 1
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento - eSocial |
| **Função:** | Parametrizador |
| **Situação/Requisito:** | Quando existe funcionário com múltiplos vínculos dentro da mesma coligada e está marcado o parâmetro 'Calcular INSS conforme eSocial' em Configurações | Parametrizador | Folha Normal.  Ao calcular e lançar as férias para ambas as chapas o sistema calcula o INSS Férias de maneira isolada considerando uma alíquota para cada chapa, porém se somarmos os valores de INSS Férias ultrapassa o teto de INSS, mas quando finalizadas as férias o sistema lança automaticamente um evento de Restituição de INSS, assim o funcionário não fica no prejuízo.  A questão é que não é coerente que o sistema ultrapasse o teto de INSS, pois conforme legislação, não podemos descontar o valor do INSS acima do teto, mesmo com a restituição lançada pelo sistema, o funcionário está tendo um desconto acima do teto. Conforme manual do ESOCIAL, página 104 e 106, informa que não podemos descontar o valor do INSS para múltiplos vínculos acima do limite.  Além disso, esse processo dificulta até a conferência da folha pelo usuário e questionamento dos funcionários ao receberem o recibo de pagamento. |
| **Solução/Implementação:** | Alterado o cálculo do INSS de férias para verificar a situação de múltiplos vínculos, considerando também os parâmetros de INSS no Parametrizador em Férias pasta Descontos. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-8437](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-8437) |
| **Documento de Referência:** | [Descontos](https://tdn.totvs.com.br/display/LRM/Descontos) |
| **Pacote:** | N/A |
