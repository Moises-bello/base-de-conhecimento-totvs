---
content_hash: 8557b72ccac506019f8244aabc3b8a18c859c3e26d61f5d7e3fde7a2dab5a72d
fetched_at: '2026-06-29T00:08:31.031918+00:00'
page_id: '272711772'
product: rm
source: tdn-rm
title: RMFIS00001_Geração da rotina DeSTDA.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272711772
version: 6
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.15 |
| **Ocorrência:** | Geração da rotina DeSTDA. |
| **Ambiente:** |  |
| **Passo a passo:** | O programa da rotina não possui importador de arquivo texto e a única forma de imputar os dados é manualmente. Portanto, para auxiliar o usuário nessa digitação, está disponível na área de Download o relatório [FISREL0005\_DEC\_SUBSTRIB\_DIF\_ALIQ\_ANTECIPACAO.ZIP](https://suporte.totvs.com/portal/p/10098/download?e=552088) que deverá ser importado no Totvs Gestão Fiscal em Gestão / RM Reports.        Este relatório selecionará os lançamentos fiscais que geraram débito/crédito do imposto e sua totalização por Estado da operação, seguindo as regras abaixo.  **ICMS ST**   * Operações Subsequentes - Serão selecionados todos os lançamentos de saída que possuírem valor de substituição tributária cuja Regra de ICMS associada ao CFOP possua:  * + Tipo de Tributação “Tributado”;   + Situação da Retenção ICMS ST “Substituto Tributário”;   + E o Código do CFOP seja DIFERENTE de: “5.651 à 5.667, 6.551 à 6.667 e 7.651 à 7.667”. * Operações Antecedentes - Serão selecionados todos os lançamentos de entrada internas que possuírem valor de substituição tributária cuja Regra de ICMS associada ao CFOP possua:     + Tipo de Tributação “Tributado”;   + Situação da Retenção ICMS ST “Substituto Tributário”;   + E o Código do CFOP seja DIFERENTE de: “1.351 à 1.356, 1.360 à 1.931 à 1.932, 2.351 à 2.356, 2.931 à 2.932, 3.351 à 3.356”. * Operações Concomitantes (Transporte) - Serão selecionados todos os lançamentos de entrada que possuírem valor de substituição tributária cuja Regra de ICMS associada ao CFOP possua:    + Tipo de Tributação “Tributado”;   + Situação da Retenção ICMS ST “Substituto Tributário”;   + E o Código do CFOP seja: “1.351 à 1.356, 1.360 à 1.931 à 1.932, 2.351 à 2.356, 2.931 à 2.932, 3.351 à 3.356”.  * Operações com Combustíveis: Serão selecionados todos os lançamentos de saída que possuírem valor de substituição tributária cuja Regra de ICMS associada ao CFOP possua:    + Tipo de Tributação “Tributado”;   + Situação da Retenção ICMS ST “Substituto Tributário”;   + E o Código do CFOP seja: “5.651 à 5.667, 6.651 à 6.667, 7.651 à 7.667”.   **ICMS ENTRADA**  Serão selecionados os lançamentos de entrada interestaduais, conforme descrito no Manual do programa (página 29):   * Antecipação: Serão selecionados todos os lançamentos de entrada interestaduais que possuírem valor de substituição tributária cuja Regra de ICMS associada ao CFOP possua:     + Com encerramento da tributação:     - Tipo de Tributação “Outros” com Substituição Tributária;     - Situação da Retenção ICMS ST “Antecipação”;   + Sem encerramento da tributação:     - Tipo de Tributação “Tributado”;     - Situação da Retenção ICMS ST “Antecipação”;      * Diferencial de alíquotas: Serão selecionados todos os lançamentos de entrada interestaduais que possuírem valor de diferencial de alíquota cujo Código do CFOP seja:    + Ativo Fixo: 1.406, 2.406, 1.551, 2.551 e 3.551.   + Uso e Consumo: 1.407, 2.407, 1.556, 2.556 e 3.556.   Os lançamentos de entrada/saída referente operações de devolução que geraram crédito do imposto serão detalhados com valor negativo para destacar seu efeito na apuração dos tributos. |
| **Observações:** |  |
