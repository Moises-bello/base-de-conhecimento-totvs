---
content_hash: 1d8832e7490b8566662c07f7318eac9141b9bae7f762c853f8e8cbc90d590548
fetched_at: '2026-06-29T00:11:50.862906+00:00'
page_id: '84541633'
product: rm
source: tdn-rm
title: RMFIS00007_Parametrização Base de Cálculo (PIS/COFINS) Registro F100
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=84541633
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:**11.5x \11.8x |
| **Processo** | **:** | Rotina EFD Contribuições |
| **Subprocesso** | **:** | Parametrização Base de Cálculo (PIS/COFINS) Registro F100 |
| **Data da publicação** | **:** | 02/08/2013 |

**Introdução:**

Este documento tem por objetivo orientar na parametrização do Processo do **EFD PIS COFINS** na geração do registro **F100** referente a base de cálculo.

* **É imprescindível ter o sistema TOTVS Gestão Financeira(RM Fluxus) instalado e parametrizado no ambiente de geração.**

Acesse o menu: Opções | Parâmetros | Processos, edite o processo do EFD PIS COFINS:

No processo do registro “**F100 –Tipo de Documentos Considerados**”, acesse a aba Filtros, edite o tipo de documento vinculado. Na aba identificação será apresentado o campo “**Base de Calculo**”, onde pode ser configurado como será calculada a base de calculo dos Tributos inseridos nos lançamentos Financeiros:

**Estas opções podem ser:**

Escolhendo pela base de calculo como “Valor Baixado” o sistema vai utilizar o valor baixado do lançamento para compor a base de cálculo do PIS e COFINS. Veja que no exemplo abaixo o valor Original é R$2000,00 e o valor baixado R$1907,00. Como foi parametrizada a base pelo valor baixado o sistema utiliza este valor para compor a base de calculo (é necessário que o lançamento esteja baixado)

**F100 – Juros e Multa**

Será criado na tela Identificação do Filtro por Tipo de Documento, Processo F100 - Tipo de Documentos Considerados, um *flag* para identificar se o item é referente aos valores de juros e multas de

Lançamentos Financeiros. Este Flag NÃO será criado no BD, somente na tela.

Se o flag abaixo estiver marcado o campo para definição de Base de Cálculo será fixado em "(**Valor dos Juros + Valor da Multa**)” e não será possível sua alteração.

Além disso, serão habilitados para preenchimento apenas os campos **Tipo da Operação** (com as opções 1 e 2 do manual: receitas auferidas sujeitas ou não ao pagamento do PIS e COFINS) e o campo  
**Operação** (filtro de lançamentos pela Emissão, Baixa ou Vencimento).

Na pasta **Tributos** devem ser inseridos os Tributos PIS e COFINS e seus respectivos CSTs.

Os demais campos do Registro serão preenchidos da seguinte forma:

**a**. O campo 05 - **DT\_OPER** receberá o último dia do período selecionado para a rotina;

**b**. O campo 06 - **VL\_OPER** receberá o total dos juros e multas dos lançamentos financeiros a receber somado ao total de descontos dos lançamentos financeiros a pagar, ambos baixados no período selecionado para a rotina;

**c**. Os campos 08 - **VL\_BC\_PIS** e 12 - **VL\_BC\_COFINS** serão preenchidos com o mesmo valor do campo 06 - **VL\_OPER**.

**d**. Os campos 09 - **ALIQ\_PIS** e 13 - **ALIQ\_COFINS** serão preenchidos com as respectivas alíquotas dos tributos informados na pasta Tributos.

**e**. Os campo 10 - **VL\_PIS** e 14 - **VL\_COFINS** serão preenchidos com a aplicação da alíquota sobre a base de cálculo.

**f**. O campo 19 - **DESC\_DOC\_OPER** será preenchido com texto padrão "*Total de juros e multas recebidos no período*".

**Exemplo:**

|F100|1|||29022012|67,00|06|67,0000|0,6500|0,44|06|67,0000|7,60|5,09||1|||Total de juros e multas recebidos no período|

Os campos abaixo não serão gerados no registro F100 de juros de multas:

03 - **COD\_PART**

04 - **COD\_ITEM**

15 - **NAT\_BC\_CRED**

16 - **IND\_ORIG\_CRED**

17 - **COD\_CTA**

18 - **COD\_CCUS**

**OBSERVAÇÕES:**

a) Para atender essa demanda é imprescindível que seja criado um Tipo de Documento (fictício) para ser associado ao Processo. Isso é necessário porque o campo é parte da chave primária do cadastro, tornando seu preenchimento obrigatório. Esse Tipo de Documento não será utilizado em nenhum outro processo e não afetará nenhum cálculo do sistema.

b) O processo **Cálculo das Contribuições Dcts Não Escriturados** (*Utilitários*) irá desconsiderar este registro. Ou seja, não serão inseridos nos Tributos do Lançamento Financeiro, os tributos **PIS** e  
**COFINS** sobre juros e multas, que serão identificados através do *flag* criado no Processo. Isto é, os registros que estiverem com o *flag* “*Juros e Multa*” marcados serão desconsiderados no processo **Cálculo das Contribuições Dcts Não Escriturados** (*Utilitários*).

**Para maiores informações:**

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE **[R@Fiscal](https://totvs.byyou.com/?space=rfiscal)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 3 – (Fiscal), 2 – (Fiscal)
