---
article_id: 1500006525202
category: 'Financeiro - Consultas a Receber '
content_hash: 6dd5cd7b036a96ae5f7ec25779f3ed3163cfb744e0f0e6e76eaa0e75cb2a8bf4
fetched_at: '2026-06-28T22:37:30.436460+00:00'
product: protheus
section_id: 35057682944919
source: central-protheus
title: Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - FINR130 - Como
  gerar o relatório
type: support-article
updated_at: '2025-12-05T13:59:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006525202-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-FINR130-Como-gerar-o-relat%C3%B3rio
---

**Dúvida**  
Conceitos gerias e exemplos de uso das parametrizações do relatório de Títulos a Receber **(FINR130)**?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

**UTILIZAÇÃO DA PERGUNTA:  Compõe Saldo Retroativo(MV\_PAR20)**

A pergunta Compõe Saldo Retroativo nos relatórios financeiros, é utilizada para verificar a situação da empresa numa determinada data passada é apresenta a situação de títulos a receber de maneira retrocedida.

**Exemplo:**

**Título a Receber:**

Emissão: 05/05/2019  
Vencimento: 10/05/2019  
Valor líquido: R$ 1000,00  
  
No dia 09/05/2019, é realizada uma baixa parcial deste título, no valor de R$ 600,00. Sendo assim, o saldo do título fica no valor de R$400,00.

*Extração do relatório: Data base do sistema: 06/05/2019.*

1. O resultado apresentado é o título acima no valor de R$ 1000,00, porém com saldo de R$ 400,00. Isto porque, no dia 09/05 já havia sido realizada a baixa parcial.

**Parâmetro Considera Saldo retroativo** = Não

![](https://tdn.totvs.com/download/attachments/471937135/param_consNao.jpg?version=1&modificationDate=1558377500400&api=v2)

![](https://tdn.totvs.com/download/attachments/471937135/rel_consNao.jpg?version=2&modificationDate=1558377930227&api=v2)

2. O resultado apresentado é o título acima no valor de R$ 1000,00, porém com saldo de R$ 1000,00. Mesmo que o título já tenha sofrido baixas no dia 09/05, o saldo é apresentado de acordo com o saldo do dia 06/05, onde ainda estava com seu valor totalmente em aberto.

**Parâmetro Considera Saldo retroativo** = Sim

![](https://tdn.totvs.com/download/attachments/471937135/param_consSim.jpg?version=1&modificationDate=1558378163687&api=v2)

![](https://tdn.totvs.com/download/attachments/471937135/rel_consSim.jpg?version=1&modificationDate=1558378167547&api=v2)

**EXTRAÇÃO DO RELATÓRIO COM TÍTULOS EM MOEDA ESTRANGEIRA**

Para gerar relatório de Títulos a Receber **(FINR130)**considerando um cenário com títulos em moeda estrangeira (dólar, por exemplo), os parâmetros abaixo devem ser considerados:

**MV\_PAR(17)** - Converte vencimento pela:

                        - "Data do vencimento"   A taxa a ser considerada será a do dia de vencimento de cada título **(E1\_VENCREA)**.

                        - "Data base"    A taxa a  ser considerada será a  informado na  Pergunta (36) "Data Base".

**MV\_PAR(20)** -  Compõe Saldo Retroativo:

                        - "Sim"  Os saldos dos títulos serão recompostos até a data de referência da Pergunta (36) "Data Base" .

                        - "Não" Os  saldos  serão mantidos na situação atual, independente da Pergunta (36) "Data Base".

**MV\_PAR(30)** -  Outras Moedas:

                        -  “Converter”       - os saldos serão convertidos para a moedas selecionada na Pergunta (15) "Qual Moeda".

                        - “Não imprimir”   - os saldos não serão convertidos .

**MV\_PAR(36)**  - "Data Base" Informe a data base do sistema a ser considerada para não ter que alterá-la antes de imprimir este relatório.

**Cenário:**

Quando utilizado parâmetro **“Compõe Saldo Retroativo” (MV\_PAR20) = SIM,** o sistema passa a considerar como Data Base do relatório a data informada no parâmetro **“Data Base**” **(MV\_PAR36)**.

Quando existir  títulos em **moeda estrangeira** para ser impresso e  o parâmetro **MV\_PAR30 “Outras Moedas” = CONVERTER**, o sistema verifica se existe taxa contratada **(E1\_TXMOEDA)** caso exista, esta será considerada como conversão.  Se não existir taxa contratada, o sistema busca a taxa de conversão no cadastro de Moedas**(SM2) .**

**Dúvidas Frequentes:**

Com a pergunta  **“Compõe Saldo Retroativo” =  SIM  e** **não** existir  uma taxa contratada no campo **(E1\_TXMOEDA)** e **não** existir  taxa de moeda cadastrada **(SM2)** na data informada na pergunta **"Data Base"** o saldo do titulo será impresso com o **valor 0,00 (zerado) na impressão do relatório.**

**Exemplo:**

 CONVERSÃO  U$  x R$

 TÍTULO          x      TAXA

U$ 1.000,00    x      0,00         =  R$ 0,00  -> Título é apresentado no relatório com uma legenda para que seja identificado que não existe taxa para que seja realizado a conversão da moeda.  
  
  
**Saiba Mais**  
[FINR130 - Títulos a Receber - Protheus 12](https://tdn.totvs.com/pages/releaseview.action?pageId=547226162)
