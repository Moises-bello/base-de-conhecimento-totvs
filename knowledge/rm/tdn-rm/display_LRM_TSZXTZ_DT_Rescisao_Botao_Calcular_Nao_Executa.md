---
content_hash: ec45ef4a9f9deb2f3c87287760d995144a3470e7a59b9528903fbd5dcdb5ca9e
fetched_at: '2026-06-29T00:06:03.589573+00:00'
page_id: '200901357'
product: rm
source: tdn-rm
title: TSZXTZ_DT_Rescisao_Botao_Calcular_Nao_Executa
type: documentation
url: https://tdn.totvs.com/display/LRM/TSZXTZ_DT_Rescisao_Botao_Calcular_Nao_Executa
version: 1
---

# RESCISÃO DE FUNCIONÁRIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão* |
| **Situação/Requisito:** | *Cálculo da rescisão está sendo feito somente caso a rescisão seja dos tipos 5 e 6. Em todos os outros tipos de rescisão, nada acontece ao clicar no botão de Cálculo/Recáluclo.* |
| **Solução/Implementação:** | *Corrigir a condição que está verificando se o tipo da rescisão é 5 ou 6 para só então avançar na execução do processo.* |
| **Chamados relacionados:** | *TSZXTZ* |
| **Versões/Release:** | *12.1.7* |
