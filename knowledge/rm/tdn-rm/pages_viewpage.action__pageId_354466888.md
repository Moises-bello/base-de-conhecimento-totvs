---
content_hash: 42f4d4ec01b0d50deccf1642d3acab524fa338aabcddb838bc561b13c7f4a3e1
fetched_at: '2026-06-29T00:08:57.686090+00:00'
page_id: '354466888'
product: rm
source: tdn-rm
title: 2290177 FISCAL01-3983 DT Geração do registro D197 com dois códigos de ajustes
  distintos, FECP e Dif. Alíquota.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=354466888
version: 5
---

# Geração do registro D197 com dois códigos de ajustes distintos, FECP e Dif. Alíquota.

|  |  |
| --- | --- |
| **Linha de Produto:** | Informe a linha de produto. |
| **Segmento:** | Informe o segmento. |
| **Módulo:** | Informe o módulo. |
| **Função:** | Informe a função. |
| **Situação/Requisito:** | Cliente solicita que seja implementado a mesma consistência do documento abaixo (C197) para o registro D197:  [http://tdn.totvs.com.br/pages/releaseview.action?pageId=173084139](http://tdn.totvs.com.br/pages/releaseview.action?pageId=173084139 "Follow link") |
| **Solução/Implementação:** | O sistema de Gestão Fiscal foi alterado para tratar o registro D197 quando existir situação onde é necessário informar o código de ajuste FECP referente ao diferencial de alíquotas: RJ70000006 e também o código de ajuste ICMS Diferencial de Alíquota: RJ70000002 no mesmo lançamento fiscal.    Essa alteração será aplicada para atender a nova sistemática dos débitos extra apuração. Os seguintes débitos passaram a ser feitos no Registro D197 (nota a nota):  - Imposto de Importação (RJ70000001) e seu FECP (RJ70000005)  - Diferencial de ICMS Ativo (RJ70000003), Diferencial Uso Consumo (RJ70000002) e seus respectivos FECP's (RJ70000006)    **Parametrização Necessárias:**  **1.****Cadastro de Campo Complementar**  É necessário criar os seguintes campos complementares no Lançamento Fiscal:    Nome da Coluna: CODAJUSTESPEDFECP  Descrição: Código Ajuste FECP  Tipo: Alfanumérico  Tamanho: 10  Tipo Texto: Texto    Nome da Coluna: CODAJUSTESPED  Descrição: Código de Ajuste SPED  Tipo: Alfanumérico  Tamanho: 10  Tipo Texto: Texto      **2.****Realizar o lançamento que possui Dif. Alíquota e FECP sobre o Dif. Alíquota.**  Realizar o lançamento onde existe FECP sobre o Dif. Alíquota e informar os dois Códigos de Ajustes nos campos complementares criados:           **Geração da Rotina**  Gerar a rotina SPED Fiscal no período do lançamento fiscal criado. Como resultado o sistema gera o arquivo com dois registros D197, cada um com seu código de ajuste e valores específicos. |
