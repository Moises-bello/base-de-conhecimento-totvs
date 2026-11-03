---
content_hash: a29581bf804ddbb3d0f381476ece9270437c7fa77348118d61a07aceb0d89ac6
fetched_at: '2026-06-29T00:08:05.927518+00:00'
page_id: '236423117'
product: rm
source: tdn-rm
title: RMFIS00002_Apuração ICMS DIFAL_FECP e Geração do SPED Fiscal (EC 87_15) - Exemplo
  Prático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=236423117
version: 9
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Fiscal |
| **Versões:** | 12.1.10 |
| **Ocorrência:** | Apuração ICMS DIFAL\_FECP e Geração do SPED Fiscal |
| **Ambiente:** |  |
| **Passo a passo:** | ****EXEMPLO PRÁTICO****  **Lançamento Fiscal**  Habilitado para os Lançamentos de Saída e Devolução o cálculo dos campos:   * % UF Destinatário * Valor Partilha Destinatário * Valor Partilha Remente * %FCP * Valor ICMS FCP UF Destinatário     Ao encerrar o período de Apuração do ICMS na aba Valores Diferencial de alíquota são exibidos os valores de sua filial,  remetente igual a Sim com valor correspondente aos 60%, e valores para as UF´s destino correspondente aos 40%  onde o remetente é igual a Não.      Para a geração do SPED FISCAL em relação a Emenda Constitucional 87/15 deverá criar lançamentos de outros débitos e créditos  para que os registros do Bloco E sejam gerados corretamente.  Na aba "Valores Diferencial de Alíquota" foi gerado um débito de 60% do Difal referente ao Remetente.  Assim, deverá incluir um lançamento de Outros Débitos e Créditos com o Tipo Crédito e o Subtipo DIFAL - Origem\Destino no valor dos 60% de Difal.    Dessa forma o valor referente ao seu estado da aba Diferencial de Alíquota no período de apuração ficará zerado.    Para que o valor dos 60% seja considerado na apuração e a guia normal seja gerada corretamente compondo esse valor,  inclua um lançamento de Outros Débitos e Créditos com o tipo Débito e o subtipo "Não se aplica" com o valor dos 60%.      Deverá inserir manualmente a guia GNR correspondente aos 40% do destino:      A Guia "Normal" será gerada automaticamente pelo sistema através do Menu: Processos - Geração de Guias Automaticamente.      Após encerrar o período de apuração o valor do DIFAL 60% será considerado na geração automática da guia.  O arquivo SPED FISCAL será gerado da seguinte forma: |
| **Observações:** |  |
