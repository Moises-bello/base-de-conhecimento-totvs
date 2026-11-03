---
content_hash: a91238b08bfc3a85d02529b96ab44a3d3119e55f7a48229125d258eb848b2523
fetched_at: '2026-06-29T00:11:50.534821+00:00'
page_id: '842272518'
product: rm
source: tdn-rm
title: DT - Relatório de Conferência de INSS Patronal - Tratativa de quebra de FPAS
  na mesma filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=842272518
version: 8
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Relatório de Conferência de INSS Patronal - Tratativa de quebra de FPAS na mesma filial |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-10187](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10187) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2306.262
* 12.1.2310.209
* 12.1.2402.150 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Implementar no produto TOTVS Folha de Pagamento a possibilidade em gerar o Relatório de Conferência de INSS Patronal, levando em consideração a quebra de FPAS dentro da mesma filial. 

## **04. SOLUÇÃO**

Foram implementadas melhorias no produto para gerar o Relatório de Conferência de INSS Patronal, garantindo maior precisão e eficiência na gestão dos registros de INSS. Agora, é possível quebrar o FPAS dentro da mesma filial, permitindo que clientes informem diferentes percentuais de INSS no histórico, adaptando-se às necessidades específicas de cada empresa.

1) Foi liberado no cadastro de seção o "Histórico de percentual do INSS", levando em conta a quebra de FPAS, conforme demonstrado abaixo:

Menu Parametrizador | eSocial | Lotação Tributária

Menu Administração de Pessoal | Cadastros | Seções | Aba Histórico de Percentuais para INSS:

2) Após a configuração detalhada dos valores de terceiros na seção por quebra de FPAS, o relatório patronal será gerado considerando cada valor de terceiros cadastrado na aba "Histórico de Percentuais para INSS".

O cálculo será realizado da seguinte forma:

Para a base de INSS correspondente à seção indicada na quebra de FPAS, serão aplicados os valores de terceiros cadastrados na aba "Histórico de Percentuais para INSS".

**Exemplo:**

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| CNPJ Estabelecimento | Cod. Lotação | Descrição | FPAS Folha | FPAS Ret | Cod. Terceiros Folha | Cod. Terceiros Ret |
| 00.000.000/0000-01 | Z103.01 | Departamento 03.01 | 540 | 540 | 0131 | 0131 |
| 00.000.000/0000-01 | Z103.02 | Departamento  03.02 | 515 | 515 | 0115 | 0115 |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| CNPJ | Cod. Lotação | Categoria | TAG | Descrição | Valor Folha | Valor RET |
| 00.000.000/0000-01 | Z103.01 | 101 | vrBcCp00 | base de cálculo da contribuição previdenciária sobre a remuneração | 20105,00 | 20105,00 |
| 00.000.000/0000-01 | Z103.02 | 101 | vrBcCp00 | base de cálculo da contribuição previdenciária sobre a remuneração | 20105,00 | 20105,00 |

| Seção 03.01 | | | | Base Aplicada | | |
| --- | --- | --- | --- | --- | --- | --- |
| FPAS | 540 | Cod. Terceiros Folha | 0131 | R$20.105,00 | | |
| SEGURADOS | | VALOR DESCONTADO R$876,95 | | | | |
| SALÁRIO EDUCAÇÃO | | 2,5% | | Valor | R$502,63 | |
| INCRA | | 0,2% | | Valor | R$40,21 | |
| SENAC | | 1,0% | | Valor | R$201,05 | |
| SESC | | 1,5% | | Valor | R$301,57 | |
| SEBRAE | | 0,6% | | Valor | R$120,63 | |
| CP PATRONAL | | 20% | | Valor | R$4.021,00 | |
| GILRAT AJUSTADO | | 2% | | Valor | R$402,10 | |

| Seção 03.02 | | | | Base Aplicada | | |
| --- | --- | --- | --- | --- | --- | --- |
| FPAS | 515 | Cod. Terceiros Folha | 0131 | R$20.105,00 | | |
| SEGURADOS | | VALOR DESCONTADO R$876,96 | | | | |
| SALÁRIO EDUCAÇÃO | | 2,5% | | Valor | R$502,62 | |
| INCRA | | 0,2% | | Valor | R$40,21 | |
| FDEPM | | 1,0% | | Valor | R$502,62 | |
| CP PATRONAL | | 20% | | Valor | R$4.021,00 | |
| GILRAT AJUSTADO | | 2% | | Valor | R$402,10 | |

| Total filial 03 | | | | Base Aplicada | | |
| --- | --- | --- | --- | --- | --- | --- |
| SEGURADOS | | VALOR DESCONTADO R$1.753,91 | | | | |
| SALÁRIO EDUCAÇÃO | | 2,5% | | Valor | R$1.005,25 | |
| INCRA | | 0,2% | | Valor | R$80,42 | |
| SENAC | | 1,0% | | Valor | R$201,05 | |
| SESC | | 1,5% | | Valor | R$301,57 | |
| SEBRAE | | 0,6% | | Valor | R$120,63 | |
| FDEPM | | 1,0% | | Valor | R$502,62 | |
| CP PATRONAL | | 20% | | Valor | R$8.042,00 | |
| GILRAT AJUSTADO | | 2% | | Valor | R$804,20 | |
| TOTAL | | | | 12.811,65 | | |

No Relatório de Conferência de INSS Patronal, todos os valores são apresentados somados por filial, conforme demonstrado abaixo:

No processo de lançamento financeiro, os valores mencionados acima também serão considerados. Veja:

## **IMPORTANTE:**

1. Após o cadastro, o Relatório de Conferência INSS Patronal passará a considerar os percentuais cadastrados em cada "Histórico de percentual do INSS", aplicando-os nas bases correspondentes de cada quebra.
2. No caso de ausência de percentuais cadastrados, o sistema buscará os dados do "Histórico de percentual do INSS" da seção Pai.
3. O Relatório de Conferência INSS Patronal continuará sendo apresentado na tela inicial, exibindo os valores por filial para uma rápida visualização e acompanhamento.

## **5. DEMAIS INFORMAÇÕES**
