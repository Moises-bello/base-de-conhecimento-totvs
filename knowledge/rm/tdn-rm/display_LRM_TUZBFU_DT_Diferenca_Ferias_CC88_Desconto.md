---
content_hash: 03abd1c646bf008ec91a6b8bed19ba588d5477aad1f947bc76187e94ae660140
fetched_at: '2026-06-29T00:08:08.496396+00:00'
page_id: '238038455'
product: rm
source: tdn-rm
title: TUZBFU_DT_Diferenca_Ferias_CC88_Desconto
type: documentation
url: https://tdn.totvs.com/display/LRM/TUZBFU_DT_Diferenca_Ferias_CC88_Desconto
version: 2
---

# DIFERENÇA DE FÉRIAS ACUMULANDO VALOR DE DESCONTO NO CC 88

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Diferença de Férias* |
| **Situação/Requisito:** | *No cálculo da Diferença de Férias, quando existe no Recibo um evento sem a informação do evento de diferença parametrizado no cadastro, é utilizado o CC 88 para o lançamento do valor de diferença.*  *A orientação é que o evento de CC 88 seja criado como Provento.*  *Porém quando a diferença a ser lançada é referente a um Desconto, não está sendo tratado para subtrair o valor, ao invés de somar.* |
| **Solução/Implementação:** | *Ajuste no cálculo do CC 88 - DIFERENÇA OUTROS EVENTOS DE FÉRIAS, para consistir quando a diferença a ser lançada é referente a um Desconto.*  *Neste caso o valor acumulado no evento de CC 88 deve ser negativo..* |
| **Chamados   relacionados:** | *TUZBFU, TUZZGE* |
| **Versões/Release:** | *11.82.44, 12.1.12* |
