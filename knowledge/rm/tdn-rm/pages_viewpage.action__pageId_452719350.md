---
content_hash: 11797d22e2f3e33eedb24e70c0f21ad2a07ee514983fdda1599f85722124b902
fetched_at: '2026-06-29T00:10:06.926920+00:00'
page_id: '452719350'
product: rm
source: tdn-rm
title: Layout Para Importação de Empréstimo (Versão 12.1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719350
version: 8
---

**Importante:**

Campos em **vermelho** foram inseridos nos arquivos de uma versão para outra.  
**Campos obrigatórios estão destacados em negrito.**  
DELIMITADOR DE CAMPOS: ";"  
Caso, não saiba os tipos de valores a serem informados para determinados campos, os mesmos deverão vir no arquivo de layout da seguinte forma:  
Entre ponto virgula ( ;; ) "Correspondendo um campo NULL".  
A tabela abaixo é premissa para a importação de Empréstimo;  
- PFUNC

**Observação:**

No campo código, se informado o valor -1, o sistema irá verificar qual o maior código de empréstimo cadastrado para o funcionário e, na inclusão do empréstimo no cadastro do funcionário, irá informar o próximo valor.

**Atenção I:**

* Esse tratamento só será feito quando a codificação dos empréstimos é feita utilizando somente números. Caso sejam utilizadas letras na definição do código do empréstimo, o sistema irá realizar a importação seguindo o próximo número do código de empréstimo, ignorando a definição de letras ou máscara.

**Exemplo I:**

* O funcionário possui os empréstimos com os códigos 1, 2 e 3. Ao realizar a importação do arquivo, o sistema irá, automaticamente, inserir o empréstimo de código 4.

**Exemplo II:**

* O funcionário possui somente um empréstimo com o código A1. No arquivo de importação, foi informado o valor -1 no campo código. Dessa forma a importação será realizada e o empréstimo importado terá seu código igual a 1.

**Exemplo III:**

* O funcionário possui 2 empréstimos de código 0001 e 0002, respectivamente. Utilizando o valor -1 para o código no arquivo de importação, o sistema irá inserir o empréstimo de código 3, e não o 0003.

**Atenção II!** Caso, possua dúvidas sobre os tipos de dados que serão inseridos nos campos, segue a baixo os exemplos:  
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
| **Chapa do Funcionário** | **String** | **16** | **1** | **PFEMPRT. CHAPA** |
| **Código do empréstimo** | **String** | **20** | **2** | **PFEMPRT.CODIGO** |
| **Código do evento** | **String** | **4** | **3** | **PFEMPRT.CODEVENTO** |
| Data do empréstimo | Data | 8 | 4 | PFEMPRT.DTEEMPRESTIMO |
| **Valor original** | **Real** | **15** | **5** | **PFEMPRT.VALORORIGINAL** |
| Nº de parcelas | Inteiro | 5 | 6 | PFEMPRT.NROPARCELAS |
| Periodicidade | Inteiro | 2 | 7 | PFEMPRT.PERIODICIDADE |
| Fórmula da correção | String | 8 | 8 | PFEMPRT.CODFORMCORRECAO |
| Saldo devedor | Real | 15 | 9 | PFEMPRT.SALDODEVEDOR |
| Nº de parcelas pagas | Inteiro | 2 | 10 | PFEMPRT.NROPARCPAGAS |
| **Início do desconto** | **Data** | **8** | **11** | **PFEMPRT.INICIODESCONTO** |
| **Tipo do empréstimo** | **String** | **10** | **12** | **PFEMPRT.TIPOEMPRESTIMO** |
| Fórmula de cálculo | String | 8 | 13 | PFEMPRT.CODFORMLANC |
| Observação | String | 80 | 14 | PFEMPRT.OBSERVACAO |
| Código do banco para compensação | String | 3 | 15 | PFEMPRT.CODBANCO |
| Código identificador do contrato | String | 40 | 16 | PFEMPRT.CONTRATO |
| Data final prevista para liquidação do contrato | Data | 8 | 17 | PFEMPRT.FINALDESCONTO |
| Data de exclusão do contrato (Liquidação) | Data | 8 | 18 | PFEMPRT.DTEXCLUSAO |
| Motivo de exclusão de operação PPE | String | 2 | 19 | PFEMPRT.CODMOTIVEXCLUSAO |
| Contrato empréstimo consignado garantia FGTS / eConsignado | Inteiro | 1 | 20 | PFEMPRT.EMPCONSGARANTFGTS |
| Matricula / Banco | String | 5 | 21 | PFEMPRT.MATINSTCONS |
| No. do contrato CEF / eConsignado | String | 40 | 22 | PFEMPRT.NUMCONTEMPCONS |
| Aplicar a margem consignável sobre a remuneração | Booleano | 5 | 23 | PFEMPRT.APMARGEMCONSIGREM |
| Percentual da margem consignável sobre a remuneração | Real | 15 | 24 | PFEMPRT.PERCMARGEMCONSIG |
| Valor da parcela do empréstimo crédito do trabalhador | Real | 15 | 25 | PFEMPRT.PARCEMPRCREDTRAB |
| Mês competência final do empréstimo | Inteiro | 5 | 26 | PFEMPRT.MESFINAL |
| Ano competência final do empréstimo | Inteiro | 5 | 27 | PFEMPRT.ANOFINAL |
