---
content_hash: 125c4070c3fb6be76973eed5b8cfb85e541364d92aa8faf9e22f7f22ee20fbd5
fetched_at: '2026-06-29T00:10:46.749507+00:00'
page_id: '555861219'
product: rm
source: tdn-rm
title: Escrituração de Lançamentos - Valor ICMS Dif. Alíquota do Frete
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=555861219
version: 13
---

Através do vínculo do CTRC/CT-e é possível preencher o campo “Valor ICMS Dif. Alíquota do Frete” originados do processo de Escrituração Fiscal do TOTVS Gestão de Compra, Estoque e Faturamento.

# Parametrizando o TOTVS Gestão Fiscal

Criar uma Regra de ICMS onde na guia Identificação possua as seguintes informações:

1. Tipo de Tributação = Outros
2. Operação Tributária = Diferencial de Alíquota

Na guia **Dados ICMS** preencher o campo Alíquota ICMS (%) que pode variar de acordo com o contexto a operação. Na pasta Afeta Base do ICMS marcar a opção “Frete”.

Na guia **Dados ICMS S.T.**  preencher o campo Alíquota S.T./ Interna D.A. (%) de e acordo com a alíquota válida do estado do contribuinte e também no campo "Utiliza ICMS por Dentro no D.A." selecione Base de Cálculo com ICMS

Em seguida na guia **Tributação ICMS/IPI** vincular a Regra de ICMS ao cadastro do CFOP

# Parametrizando o Movimento de Transporte - TOTVS Gestão de Estoque, Compra e Faturamento

Para que seja possível vincular o Conhecimento de Transporte ao movimento de Nota Fiscal é necessário os seguintes:

Na etapa **16 - Mov. – Rateio Val. Financeiros 1/2** na opção “Frete” selecionar uma das opções Aplicar Rateio Proporcional ou Aplicar Rateio Condicional

Selecionar o Tipo de Frete na etapa **19 - Mov. Transporte 2/2**

Selecionar o Tipo de Frete na etapa **62** **– Fis – Escrituração 1/2** marcar a opção Gerar Escrituração e informar também o Tipo Documento Escrituração que se aplica a CTRC/CT-e

Informar os tributos incidentes utilizando a tributação no “item” através da etapa **64** **– Fis – Tributação - Item**

Selecione o Tipo de Operação de Conhecimento de Transporte na etapa **68 - Fis – Conhecimento de Transporte**.

***Observação***: no campo “Fórmula do Valor de CTRC a Ratear” deve ser informada a mesma fórmula selecionada no campo “Fórmula do Valor do Documento” etapa **13** **- Mov – Valores Financeiros 2/4**

# Parametrizando o Movimento de Nota Fiscal - TOTVS Gestão de Estoque, Compra e Faturamento

Na etapa **68 – Fis – Conhecimento de Transporte** selecionar o Tipo de Operação de Conhecimento de Transporte selecione a opção “Indicar CTRC/CT-e”

# Criando o Movimento de Transporte

Na guia CTRC pasta Dados do CTRC informe a Quantidade de Notas e também o valor do transporte.

# Criando o Movimento de Nota Fiscal

Na criação do movimento na guia CTRC será listada todas as notas de transporte. Vincule a nota de transporte selecionando e depois a opção "Incluir".

***Observação***: só será possível vincular um CTRC na Nota Fiscal se o mesmo for do mesmo valor informado na nota. Caso contrário será apresentada a mensagem:

# Processo de Escrituração

No filtro de Escrituração deve ser informado os dados da nota fiscal que teve o CTRC vinculado.

# Lançamento Fiscal

Campo “Valor ICMS Dif. Alíquota Frete” preenchido.

Valor gerado corretamente

| Valor do Frete | 456,00 |
| --- | --- |
| Alíquota S.T./Interna D.A.(%) | 17% |
| Valor do ICMS sobre a alíquota 17% | 77,52 |
| Alíquota ICMS(%) | 12% |
| Valor do ICMS sobre a alíquota 12% | 192,52 |
| Valor ICMS Dif. Alíquota Frete | 114,00¹ |

**Onde¹**

192,52 - 77,52 = 114,00
