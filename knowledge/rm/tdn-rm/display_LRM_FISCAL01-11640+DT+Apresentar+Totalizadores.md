---
content_hash: 71224cc5fe7d102a8b3e65a5b2f26b8a76599c1b9ca13108fa20e87e745d6729
fetched_at: '2026-06-29T00:10:31.952456+00:00'
page_id: '525013616'
product: rm
source: tdn-rm
title: FISCAL01-11640 DT Apresentar Totalizadores
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11640+DT+Apresentar+Totalizadores
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cadastro de Evento da Reinf |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11640 |

## **02. SITUAÇÃO/REQUISITO**

Criar aba no Evento 5011 para apresentar os totalizadores recebidos na consulta do 2099, buscando os dados diretamente do xml.

Especificação: <https://tdn.totvs.com/pages/viewpage.action?pageId=501473448>

## **03. SOLUÇÃO**

**Funcionalidade: Apresentar Totalizadores da Reinf do Período**

**Cenário I: Apresentação da aba de Totalizadores**  
Dado que um evento é do tipo R-5011  
E o status é encerrado  
A aba "Totalizadores" estará visível

**Cenário II: Preenchimento dos valores totalizados R-2010**  
Dado que um evento é do tipo R-5011  
E o status é encerrado  
E o xml de retorno está no formato determinado no layout da reinf v. 1.4,  
R-5011 - Informações de bases e tributos consolidadas por período de apuração  
E existe a tag RTom  
Então será exibido o nó "Totalização de serviços tomados (R-2010)  
Cujo CNPJ é o correspondente a tag cnpjPrestador  
E o valor da base de cálculo (BC) será o correspondente a tag vlrTotalBaseRet  
E para cada infoCRTom, terá o Código de Receita, Valor e Valor com Exigibilidade Suspensa   
respectivamente às tag: CRTom, vlrCRTom e vlrCRTomSusp  
Sendo que os campos de valor serão exibidos com máscara monetária e separados de milhar e decimal.

**Cenário III: Preenchimento dos valores totalizados R-2020**  
Dado que um evento é do tipo R-5011  
E o status é encerrado  
E o xml de retorno está no formato determinado no layout da reinf v. 1.4,  
R-5011 - Informações de bases e tributos consolidadas por período de apuração  
E existe a tag RPrest  
Então será exibido o nó "Totalização de serviços prestados (R-2020)  
Caso o tpInscTomador for 1, exibirá o CNPJ, com máscara, correspondente a tag nrInscTomador,  
Caso o tpInscTomador for 4, exibirá o CNO, com máscara, correspondente a tag nrInscTomador,  
De modo que os campos serão preenchidos conforme:  
Base de Cálculo de Retenção: vlrTotalBaseRet  
Valor de Retenção Principal: vlrTotalRetPrinc  
Valor de Retenção Adicional: vlrTotalRetAdic  
Valor Não Retido Principal: vlrTotalNRetPrinc  
Valor Não Retido Adicional: vlrTotalNRetAdic

**Cenário IV: Preenchimento dos valores totalizados R-2040**  
Dado que um evento é do tipo R-5011  
E o status é encerrado  
E o xml de retorno está no formato determinado no layout da reinf v. 1.4,  
R-5011 - Informações de bases e tributos consolidadas por período de apuração  
E existe a tag RRecRepAD  
Então será exibido o nó "Totalização de Recursos Repassados a Associação Desportiva (R-2040)  
De modo que os campos serão preenchidos conforme:  
Código de Receita: CRRecRepAD  
Valor: vlrCRRecRepAD  
Valor com Exigibilidade Suspensa: vlrCRRecRepADSusp

**Cenário V: Preenchimento dos valores totalizados R-2050**  
Dado que um evento é do tipo R-5011  
E o status é encerrado  
E o xml de retorno está no formato determinado no layout da reinf v. 1.4,  
R-5011 - Informações de bases e tributos consolidadas por período de apuração  
E existe a tag RComl  
Então será exibido o nó "Totalização de Contribuições de Produtor Rural (R-2050)  
De modo que os campos serão preenchidos conforme:  
Código de Receita: CRComl  
Valor: vlrCRComl  
Valor com Exigibilidade Suspensa: vlrCRComlSusp

**Cenário VI: Preenchimento dos valores totalizados R-2060**  
Dado que um evento é do tipo R-5011  
E o status é encerrado  
E o xml de retorno está no formato determinado no layout da reinf v. 1.4,  
R-5011 - Informações de bases e tributos consolidadas por período de apuração  
E existe a tag RCPRB  
Então será exibido o nó "Totalização de Contribuições sobre Receita Bruta (R-2050)  
De modo que os campos serão preenchidos conforme:  
Código de Receita: CRCPRB  
Valor: vlrCRCPRB  
Valor com Exigibilidade Suspensa: vlrCRCPRBSusp
