---
content_hash: 0fd94ea3230985cc3a1b720b8bbd4d5366596a03be3cc0bd8c8710457f5da899
fetched_at: '2026-06-29T00:10:04.882183+00:00'
page_id: '452719264'
product: rm
source: tdn-rm
title: Layout Para Importação de Período de Ficha Financeira (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719264
version: 11
---

**Importante:**  
Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação de Período de Ficha Financeira;

- PFUNC  
   
 **Atenção!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
-  0 (zero) ou 1(um) em campos do tipo **Booleano**;  
-  Números (00) em campos do tipo**Inteiro**;  
-  Números com vírgulas ou Pontos (0,00 ou 0.00) em campos do tipo **Real**;  
- (ddmmyyyy) em campos do tipo **Data**;  
- (GRR20071514) em campos do tipo **String**;  
- Começam /@ e terminam com @/ em campos do tipo **MEMO**.  
Para o caso de importação de históricos a data da mudança deve sempre ser informada. Caso este campo não seja informado, o registro em questão não será importado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo** | **Tamanho** | **Posição** | **Campo** |
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFPERFF.CHAPA** |
| **Ano de Competência** | **Inteiro** | **5** | **2** | **PFPERFF.ANOCOMP** |
| **Mês de Competência** | **Inteiro** | **2** | **3** | **PFPERFF.MESCOMP** |
| **Número do Período** | **Inteiro** | **2** | **4** | **PFPERFF.NROPERIODO** |
| **Mês Caixa** | **Inteiro** | **2** | **5** | **PFPERFF.MESCAIXACOMUM** |
| Indicativo de Valores Forçados | Inteiro | 2 | 6 | PFPERFF.VALORESFORCADOS |
| Indicativo de Movimento Importado | Inteiro | 2 | 7 | PFPERFF.MOVIMPORTADO |
| Indicativo de Edição | Inteiro | 2 | 8 | PFPERFF.EDITADO |
| Indicativo de Alteração | Inteiro | 2 | 9 | PFPERFF.ALTERADO |
| Salário Comissão (Formato 999999999999,99) | Real | 15 | 10 | PFPERFF.SALCOMISSAO |
| Valor lançado de férias no mês (Formato 999999,99) | Real | 9 | 11 | PFPERFF.FERIASMES |
| Base INSS (Formato 999999,99) | Real | 9 | 12 | PFPERFF.BASEINSS |
| Base INSS de outro emprego (Formato 999999,99) | Real | 9 | 13 | PFPERFF.BASEINSSOUTROEMP |
| INSS (Formato 999999,99) | Real | 9 | 14 | PFPERFF.INSS |
| INSS de Férias (Formato 999999,99) | Real | 9 | 15 | PFPERFF.INSSFERIAS |
| INSS de outro emprego (Formato 999999,99) | Real | 9 | 16 | PFPERFF.INSSOUTROEMP |
| Base INSS do 13º (Formato 999999,99) | Real | 9 | 17 | PFPERFF.BASEINSS13 |
| Base INSS do 13º de outro emprego (Formato 999999,99) | Real | 9 | 18 | PFPERFF.BASEINSS13OUTRO |
| INSS do 13º (Formato 999999,99) | Real | 9 | 19 | PFPERFF.INSS13 |
| Base de salário família (Formato 999999,99) | Real | 9 | 20 | PFPERFF.BASESALFAMILIA |
| Salário família (Formato 999999,99) | Real | 9 | 21 | PFPERFF.SALFAMILIA |
| Base de vale transporte (Formato 999999,99) | Real | 9 | 22 | PFPERFF.BASEVALETRANSP |
| Vale transporte entregue (Formato 999999,99) | Real | 9 | 23 | PFPERFF.VALETRANSPENTR |
| Vale transporte descontado (Formato 999999,99) | Real | 9 | 24 | PFPERFF.VALETRANSPDESC |
| Base de IRRF (Formato 999999,99) | Real | 9 | 25 | PFPERFF.BASEIRRF |
| IRRF (Formato 999999,99) | Real | 9 | 26 | PFPERFF.IRRF |
| INSS caixa (Formato 999999,99) | Real | 9 | 27 | PFPERFF.INSSCAIXA |
| Dedutível em IRRF (Formato 999999,99) | Real | 9 | 28 | PFPERFF.DEDUTIVELIRRF |
| Base de IRRF participação (Formato 999999,99) | Real | 9 | 29 | PFPERFF.BASEIRRFPART |
| IRRF participação (Formato 999999,99) | Real | 9 | 30 | PFPERFF.IRRFPART |
| Base IRRF férias (Formato 999999,99) | Real | 9 | 31 | PFPERFF.BASEIRRFFERIAS |
| IRRF férias (Formato 999999,99) | Real | 9 | 32 | PFPERFF.IRRFFERIAS |
| Indicativo de INSS com CPMF (Formato 999999,99) | Real | 9 | 33 | PFPERFF.INSSCOMCPMF |
| Descrição do Período String | String | 250 | 34 | PFPERFF.DESCRICAO |
| Base de FGTS (Formato 999999,99) | Real | 9 | 35 | PFPERFF.BASEFGTS |
| Base de FGTS de 13º Salário (Formato 999999,99) | Real | 9 | 36 | PFPERFF.BASEFGTS13 |
| Salário pago (Formato 999999999999,99) | Real | 15 | 37 | PFPERFF.SALARIOPAGO |
| Calc. Ccusto Sincron. C/ Calc. Folha | Inteiro | 2 | 38 | PFPERFF.STATUSCCUSTO |
| Base de IRRF de 13º Salário (Formato 999999,99) | Real | 9 | 39 | PFPERFF.BASEIRRF13 |
| Salário usado no cálculo do periodo | Real | 9 | 40 | PFPERFF.SALARIODECALCULO |
| IRRF sob 13 Real | Real | 9 | 41 | PFPERFF.IRRF13 |
| INSS de férias com CPMF | Real | 9 | 42 | PFPERFF.INSSFERIASCOMCPMF |
| INSS Calculado pelo Usuário | Real | 9 | 43 | PFPERFF.INSSCALCUSUARIO |
| Base FGTS Dif salarial (Formato 999999,99) | Real | 9 | 44 | PFPERFF.BASEFGTSDIFSAL |
| INSS de diferença salarial (Formato 999999,99) | Real | 9 | 45 | PFPERFF.INSSDIFSAL |
| INSS de diferença salarial de 13 (Formato 999999,99) | Real | 9 | 46 | PFPERFF.INSSDIFSAL13 |
| INSS de diferença salarial de férias (Formato 999999,99) | Real | 9 | 47 | PFPERFF.INSSDIFSALFER |
| ID de execução do cálculo | String | 50 | 48 | PFPERFF.EXECID |
| IRRF Nro. Dependentes | Real | 5 | 49 | PFPERFF.NRODEPENDIRRF |
| Outros Líquido | Real | 12 | 50 | PFPERFF.LIQUIDO |
| Salário Família Nro.dependentes | Real | 5 | 51 | PFPERFF.NRODEPENDSALFAMILIA |
| ID dados do residente | Inteiro | 2 | 52 | PFPERFF.IDDADOSRESID |
| Indicativo de Retificação | Inteiro | 2 | 53 | PFPERFF.RETIFICACAO |
| Mês onde foi realizado o pagamento da retificação | Inteiro | 2 | 54 | PFPERFF.MESPAGTORETIF |
| Ano onde foi realizado o pagamento da retificação | Inteiro | 4 | 55 | PFPERFF.ANOPAGTORETIF |
| Período onde foi realizado o pagamento da retificação | Inteiro | 2 | 56 | PFPERFF.PERIODOPGTORETIF |
| Ano Caixa Comum | Inteiro | 4 | 57 | PFPERFF.ANOCAIXACOMUM |
| Ordem de cálculo de funcionários com múltiplos vínculos | Inteiro | 2 | 58 | PFPERFF.ORDEMCALCULOMV |
| Pagamento de dissídio na competência da demissão após envio do evento S-2299 | Inteiro | 2 | 59 | PFPERFF.DISSIDIOAPOSDEMISSAO |
| Número do benefício que se refere o pagamento | Inteiro | 5 | 60 | PFPERFF.NUMEROBENEFICIO |
| Base anual de IRRF PLR | Real | 12 | 61 | PFPERFF.BASEIRRFPARTANUAL |
| IRRFSIMPLIFICADO | Inteiro | 2 | 62 | PFPERFF.IRRFSIMPLIFICADO |
| IRRF13SIMPLIFICADO | Inteiro | 2 | 63 | PFPERFF.IRRF13SIMPLIFICADO |
| IRRFFERSIMPLIFICADO | Inteiro | 2 | 64 | PFPERFF.IRRFFERSIMPLIFICADO |
| DESCONSIDERAMESTRANSFDIRFINF | Inteiro | 1 | 65 | PFPERFF.DESCONSIDERAMESTRANSFDIRFINF |
| Base de FGTS do Aviso Previo | Decimal | 15 | 66 | PFPERFF.BASEFGTSAVPREVIO |
| Base de FGTS do Aviso Previo 13º | Decimal | 15 | 67 | PFPERFF.BASEFGTS13AVPREVIO |
| Indicativo de IRRF calculado com desconto Simplificado Caixa | Inteiro | 2 | 68 | PFPERFF.IRRFSIMPLIFICADOCAIXA |
| Indicativo de IRRF 13 calculado com desconto Simplificado Caixa | Inteiro | 2 | 69 | PFPERFF.IRRF13SIMPLIFICADOCAIXA |
| Indicativo de IRRF Férias calculado com desconto Simplificado Caixa | Inteiro | 2 | 70 | PFPERFF.IRRFFERSIMPLIFICADOCAIXA |
