---
content_hash: 5973a6c24d3b5d012d35e16dc159d70a7469afc934c6d6bed753810d35046ea5
fetched_at: '2026-06-29T00:08:53.220355+00:00'
page_id: '344463708'
product: rm
source: tdn-rm
title: Como_Fazer_Aluguel Sobre Faturamento (Aluguel Complementar)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=344463708
version: 8
---

|  |  |
| --- | --- |
| **Produto:** | TOTVS Incorporação |
| **Versões:** | 12.1.19 |
| **Ocorrência:** | N/A |
| **Ambiente:** | RM |
| **Passo a passo:** | N/A |
| **Observações:** | Trata-se de recurso desenvolvido pelo modelo participativo |

O Aluguel Complementar é uma forma de cobrança adicional ao aluguel mensal, ou seja, além do aluguel mensal (que também é chamado de Aluguel Mínimo) será cobrado um valor a mais conforme o faturamento do inquilino (locatário).

Esta forma de cobrança geralmente é aplicada a locação de imóveis de varejo (lojas, supermercados, etc).

O cálculo é feito da seguinte forma:

**Fórmula**

*SE(((Valor Faturamento Mês)\* (% sobre Faturamento))>Valor Alug. Mensal)*

*ENTÃO Aluguel Complementar =0*

*SENÂO*

*((Valor Faturamento Mês)\* (% sobre Faturamento))-Valor Alug. Mensal*

*FIMSE*

Ex:

Aluguel mensal (ou Aluguel Mínimo Mensal)= R$ 10.000,00

% Sobre o Faturamento = 5%

| Mês | Valor Alug. Mensal  *(Aluguel Mínimo)* | % sobre Faturamento | Valor Faturamento Mês | Valor do Aluguel Complementar |
| --- | --- | --- | --- | --- |
| Jan | R$ 10.000,00 | 5% | R$ 200.000,00 | *(Valor Faturamento Mês)\* (% sobre Faturamento)*  (R$ 200.000,00)\* (0,05)= R$ 10.000,00  *((Valor Faturamento Mês)\* (% sobre Faturamento))-Valor Alug. Mensal*  R$ 10.000,00 -  R$ 10.000,00= **0**  portanto não haverá cobrança de aluguel complementar. |
| Fev | R$ 10.000,00 | 5% | R$ 210.000,00 | *(Valor Faturamento Mês)\* (% sobre Faturamento)*  (R$ 210.000,00)\* (0,05)= R$ 10.500,00  *((Valor Faturamento Mês)\* (% sobre Faturamento))-Valor Alug. Mensal*  R$ 10.500,00-  R$ 10.000,00 = R$ 500,00 |
| Mar | R$ 10.000,00 | 5% | R$ 220.000,00 | *(Valor Faturamento Mês)\* (% sobre Faturamento)*  (R$ 220.000,00)\* (0,05)= R$ 11.000,00  *((Valor Faturamento Mês)\* (% sobre Faturamento))-Valor Alug. Mensal*  R$ 11.000,00- R$ 10.000,00 = R$ 1.000,00 |

**PARAMETRIZANDO O CONTRATO DE LOCAÇÃO**

Ao cadastrar um contrato de locação que tenha a necessidade de cobrança do Aluguel Complementar, acesse a pasta Aluguel Complementar / Parâmetros e preencha.

Mais detalhes de cada campo acesse o Help <http://wikihelp.totvs.com.br/WikiHelp/IMB/IMB.ContratoLocacaoAlgCompl.aspx>

 Na aba de parâmetros é importante que o Tipo de Evento informado tenha a "Finalidade do Tipo de Evento"= "Locação Complementar".

O sistema permite ainda que sejam cadastradas faixas de valor com percentuis distintos no mesmo período, ou criar percentuais para períodos diferentes

Não é obrigatória a inclusão de uma data final, mas esta deve ser informada se houver um novo período.

No exemplo acima, temos no ano de 2018, 3 percentuais diferentes conforme a faixa de faturamento do inquilino, mas a partir de 2019 será um único percentual para qualquer valor.

Feito o cadastro dos parâmetros no contrato e demais dados necessários, (imóveis, locatários, regras de reajuste, etc) o contrato poderá ser efetvado e gerado os lançamentos financeiros mensais referente ao aluguel mensal (mínimo).

Os  **Valores de faturamento** do locatário serão informados depois  do contrato efetivado, e deve ser incluído mês a mês (não tem necessidade de lançar previsões).

Para informar o valor, acesse o Anexo ao contrato de Locação "Medições"

As medições podem ser inseridas manualmente ou podem ser importadas via arquivo. <http://wikihelp.totvs.com.br/WikiHelp/IMB/IMB.AluguelImportacaoMedicao.aspx>

Para a inclusão manual clique em Inserir

Preencha os campos de: Data da Medição, Competência de Cobrança e Valor do Faturamento. Os demais campos devem ser preenchidos automaticamente.

*Se os campos de Data de vencimento, Valor do Aluguel da Competência e Percentual do faturamento não estiverem preenchidos, provavelmente você se esqueceu de preencher a pasta de parâmetros, dentro do contrato de locação. Para preencher estes campos você deve voltar a situação do contrato.*

**Gerar Aluguel Complementar**

Acesse os Processos do Contrato de Locação → Gerar Aluguel Complementar

*Para gerar o aluguel complementar o sistema deve ter uma medição informada.*

Selecione os registros desejados e clique em executar.

O sistema gerará um Evento Financeiro (conforme parametrizado) para o Aluguel Complementar.

Para excluir um lançamento complementar, acesse o Evento Financeiro Gerado, acesse o Processo Excluir Lançamento Financeiro, e selecione o lançamento desejado.

Quando houver um valor escalonado o sistema deve considerar na formula de cálculo o valor do Aluguel Mínimo igual ao valor do Escalonamento no período, o mesmo quando houver reajuste.
