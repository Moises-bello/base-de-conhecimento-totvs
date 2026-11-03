---
content_hash: fa5086dfb8272dd615ecf69fe63b4528b782759c4f6ac31cc8f3200d67b4c1c0
fetched_at: '2026-06-29T00:09:55.500214+00:00'
page_id: '447090056'
product: rm
source: tdn-rm
title: FISCAL01-7354 DT Lançamento Fiscal - Cálculo do FECP Próprio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=447090056
version: 2
---

# FECP Próprio e FECP ST

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Lançamento Fiscal |
| **Situação/Requisito:** | Calcular o FECP Próprio no Item e no Lançamento durante a inclusão. Nas versões anteriores, o campo de FECP continham juntos os valores de FECP Próprio e o FECP ST,  dificultando a informação e a conferência. Neste sentido, é necessário ajustar o FECP ST para subtrair o FECP Próprio. E além disso, deverá ser considerado o parâmetro da regra de ICMS para calcular ou não os FECP e FECP ST |
| **Solução/Implementação:** | Ajuste no sistema para calcular o ***FECP Próprio*** e o ***FECP ST***, exibindo-os em campos distintos, tanto no lançamento, quanto no item, na inclusão manual.     * **Item:**   Em Dados Fiscais → Valores ICMS são exibidos os valores discriminados de ***FECP Próprio*** e ***FECP ST***, conforme pode ser visto abaixo:    Observação: Os campos são somente informativos não podendo ser editados.   * **Situação Tributária:**  Em Dados Fiscais → ICMS e IPI o campo de ***FECP** **Próprio*** é exibido:     Em Dados Fiscais →Substituição Tributária o campo de ***FECP ST/Difal***  é exibido:       * **Informações importantes:**   Para o ***FECP Próprio*** ser calculado e o percentual (%) ser recuperado na tela, é necessário que a regra de ICMS esteja parametrizada como  **"Operação com FCP"**:      Para o ***FECP ST*** ser calculado, é necessário que a regra de ICMS esteja parametrizada como ***"Operação com FCP ST":***      O percentual (%) do***FECP Próprio*** será recuperado dos dados fiscais por UF do produto. Para a UF da Filial e o percentual(%) do ***FECP ST*** será recuperado dos dados fiscais da UF de destino: |
