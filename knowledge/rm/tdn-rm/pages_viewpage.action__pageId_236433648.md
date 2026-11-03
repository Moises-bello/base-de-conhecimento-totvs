---
content_hash: 0c67e6064fc2f1794308a7c94f9a94b713f1b31131912f630fd9dfe10c3313c6
fetched_at: '2026-06-29T00:08:06.116408+00:00'
page_id: '236433648'
product: rm
source: tdn-rm
title: RMFIS00001_Decreto nº 46.930/2015 – MG  Novo Calculo para a Base de Calculo
  do Diferencial de Alíquota
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236433648
version: 15
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Fiscal |
| **Versões:** | 12.1.10 |
| **Ocorrência:** | **Decreto nº 46.930/2015 – MG** **Novo Calculo para a Base de Calculo do Diferencial de Alíquota** |
| **Ambiente:** |  |
| **Passo a passo:** | O Governador do Estado de Minas Gerais, por meio do Decreto n° 46.930/15, alterou a base de cálculo do imposto para fins do cálculo da parcela do imposto correspondente à diferença entre a alíquota interna e a interestadual nas seguintes operações:   * Entrada, em estabelecimento de contribuinte, em decorrência de operação interestadual, de mercadoria destinada a uso, consumo ou ativo permanente; * Operação interestadual que destine mercadoria ou bem a consumidor final não contribuinte do imposto, localizado no Estado de Minas Gerais, relativamente à parcela do imposto correspondente à diferença entre a alíquota interna estabelecida para a mercadoria no Estado e a alíquota interestadual; * Prestação interestadual de serviço destinada ao Estado de Minas Gerais, tomada por consumidor final não contribuinte do imposto, relativamente à parcela do imposto correspondente à diferença entre alíquota interna estabelecida para a prestação no Estado e a alíquota interestadual.   **PARAMETRIZAÇÃO**  **Execução do script:**  **11.82**  [SCRIPTTTYHIN\_NOVABASEDIFERENCIALALIQUOTA\_11.82.ZIP](https://suporte.totvs.com/portal/p/10098/download#detail/514138)  **12.1**  [SCRIPTTTYHIN\_NOVABASEDIFERENCIALALIQUOTA\_12.1.ZIP](https://suporte.totvs.com/portal/p/10098/download#detail/514137)  Documento de auxílio para execução o script:  *([FAQ de auxílio para Executar o Script](http://tdn.totvs.com/display/public/rm/Executor+de+Scripts+RM))*  **Após execução do script serão criados na regra de ICMS os campos:**    Não Utiliza - Base de Cálculo Com ICMS - Base de Cálculo Sem ICMS    **Cadastro Regra de ICMS**    * Sub Pasta Dados ICMS ST criar o campo “**Utiliza ICMS por Dentro no D.A**” Utiliza ICMS por dentro na Base de Calculo do Diferencial de Alíquota com as opções abaixo:  -1 incomplete   40 complete  Não Utiliza   41 complete  Base de Cálculo Com ICMS  42 complete  Base de Cálculo Sem ICMS  43 complete  Base de Cálculo Sem ICMS - Interestadual      Esta forma de Calculo será realizada nas Operações:    * Operação de Entrada em que o Campo Operação Tributaria é **“Diferencial de Alíquota”;** * Operação de Saída, Interestadual, Venda a Não Contribuinte e Consumidor Final em que o Campo Operação Tributaria é **“Diferencial de Alíquota”;** * Deverá ser utilizado o campo **“% Redução de Base ICMS ST”**, disponível na Regra de ICMS\Sub Pasta ICMS ST, quando o Tipo de Tributação da Regra de ICMS for igual a**“Diferencial de Alíquota”.**O mesmo será considerado em uma eventual redução na Base de Calculo do Diferencial de Alíquota**;**  * Habilitado o calculo do **Diferencial de****Alíquota** nas Operações de saída, Interestadual, Venda a Consumidor final para os tipos de tributação 40-Isenta e  41Não tributada(Não Incidência) da Regra do ICMS;       * Nas Operações de **Entrada com Diferencial de****Alíquota**, Tipo de Tributação Outros, o Valor do ICMS Interestadual da tela do Diferencial de Alíquota, será calculado com Base no Valor da Mercadoria x Alíquota Interestadual.   Observações:   - O Valor do Rateio do Frete somente será considerado se na Natureza Fiscal estiver habilitado o Campo Afeta Base de Calculo do ICMS igual a “ Frete”.   - Sempre que houver IPI destacado não será considerado para compor o valor da Base de Calculo do Diferencial de Alíquota |
| **Observações:** | Detalhamento através do LINK abaixo: |
