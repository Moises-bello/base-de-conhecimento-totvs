---
article_id: 360021429691
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 087ec29335bf57de52181c7b46d6eb5f2c1232395de4da2c9e69ebcd55f454f2
fetched_at: '2026-06-28T22:42:10.381612+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Configuração
  necessária para documento com retenção de ISS
type: support-article
updated_at: '2022-08-17T19:39:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021429691-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Configura%C3%A7%C3%A3o-necess%C3%A1ria-para-documento-com-reten%C3%A7%C3%A3o-de-ISS
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**  
Como configurar uma Nota com retenção de **ISS - Imposto Sobre Serviços**?  
  
**Ambiente**TOTVS Backoffice - Cross Segmentos (Linha Protheus) - Livros Fiscais – A partir da versão 11.80.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Cadastre a **Natureza:**  
**Calcula ISS -** **ED\_CALCISS** =Sim;  
  
2. Cadastre a **TES:**  
**Calculo ISS -** **F4\_ISS** = Sim; **L. Fiscal ISS** **- F4\_LFISS** = Tributado/ Outros/ Isento;  
  
3. Cadastre o **Produto:**  
**Aliq. ISS** **-** **B1\_ALIQISS** = Informe a alíquota- Caso este campo esteja sem preenchimento, será válido o conteúdo do parâmetro **MV\_ALIQISS**; **Cód. Serv. ISS -** **B1\_CODISS** = Informe o código de serviço do **ISS, c**aso não haja o código referente ao serviço deve ser incluído na tabela 60 do **Configurador**;  
  
4. Cadastre o **Fornecedor:**  
**Recolhe ISS** **-** **A2\_RECISS** = Não;  
  
5. Cadastre o **Cliente:**  
**Recolhe ISS -** **A1\_RECISS** = SIM - se este campo estiver como **SIM**, haverá retenção de ISS, Tít. Imposto no **SE1,** se configurado como não, o **ISS** poderá ser pago na apuração mensal;  
**ISS no preço -** **A1\_INCISS** = Sim - Não agrega o valor de **ISS** à base de cálculo. Não - Agrega o valor do **ISS** à base de cálculo;  
**F.Ret.ISS** **- A1\_FRETISS** = 1=Considera valor mínimo **MV\_VRETISS** ou 2= Sempre retém - Informe se o cliente deve respeitar o valor mínimo do **ISS**;  
  
6. Utilize os parâmetros referentes à retenção de **ISS**:  
**MV\_DESCISS -** Informa se o **ISS** deve ser descontado do valor do título financeiro, caso o cliente for responsável pelo recolhimento. Conteúdo **.T.** = verdadeiro ou **.F.** = falso;  
**MV\_MRETISS -** Modo de retenção do **ISS** nas aquisições de serviços. Conteúdo **1** = na emissão do titulo principal.  **2** = na baixa do título principal;  
**MV\_VRETISS -** Valor mínimo para dispensa de retenção de **ISS**;  
**MV\_PRETISS -** Definição do responsável pelo recolhimento do **ISS** por parte do Prestador ou Tomador do Serviço conforme limite conforme regulamento do **ISS** do município de Porto Alegre/RS;  
**MV\_MODRISS -** Indica qual o modo de retenção do **ISS**. Conteúdo **1** - por título **2** - mensal vencimento **3** - por base;             
**MV\_TPNFISS**- Caso esse parâmetro esteja sem conteúdo, **obrigatoriamente** o Cód. de Serviço de**ISS** deve estar preenchido no cadastro de produto para o correto cálculo do **ISS**. Informe os tipos de documentos que deverão realizar o cálculo de **ISS** somente pela Natureza em casos que o campo **Gera Duplicata - F4\_DUPLIC** no cadastro de **TES** estiver igual a sim. Utilize: E - para entrada e S - para saída. = E;  
**MV\_VENCISS -** Define o tipo de vencimento de **ISS**. Conteúdo **E**=Emissão ou **Q**=Quinzenal/ Emissão ou **V**=Vencimento ou **F** = Se a data de emissão for menor que 15, primeira quinzena, a data de vencimento será 15  somados ao conteúdo **MV\_DIAISS**, considerando o primeiro dia do mês na conta, se a data de emissão for maior que 15, segunda quinzena, será no dia informado no **MV\_DIAISS** do mês subsequente;  
**MV\_DIAISS -** Dia padrão para gerar os títulos de **ISS**;  
**MV\_DEDISS -** Define o momento do tratamento da dedução do **ISS**. Conteúdo **1**= Na baixa. 2= Na emissão;  
**MV\_ALIQISS -** Define a alíquota do **ISS** para cada município, Ex: 5.00%;  
**MV\_ISS** - Define a natureza dos títulos de **ISS**, Padrão: **ISS**;  
**MV\_MUNIC**- Indica o fornecedor do **ISS**. O Sistema gera títulos a pagar contra o município determinado neste parâmetro, no momento da inclusão do título a receber, no módulo **Financeiro**;  
**MV\_APURISS**- Define a natureza a ser utilizada na geração do título a pagar por meio da **Apuração de** **ISS**. Caso este parâmetro não esteja configurado, é assumido como padrão o conteúdo do parâmetro **MV\_ISS**;   
**MV\_TPABISS - Parâmetro exclusivo para notas de saída -** Conteúdo =**1** indica que é efetuado um desconto na duplicata quando o cliente recolhe **ISS**.  **2** = É gerado um título de abatimento;  
**MV\_DEISSBS - Parâmetro exclusivo para notas de saída -** Indica se o valor do **ISS** deve ser retirado da base de cálculo do **PIS/COFINS/CSLL**. Conteúdo **.T.** = não será descontado. Conteúdo **.F**. = será descontado;  
**MV\_RATISS** - Indica se deve ratear o **ISS** no lançamento do documento fiscal de entrada.            **T=**Rateio por parcela;  
**F=**Mantém na primeira parcela.  
  
**Importante**  
Na inclusão de Notas Fiscais de entrada, serão gerados títulos no **Financeiro** no **Contas a Paga**r. Para notas fiscais de saídas, serão gerados títulos no financeiro no contas a receber.  
Registro no Livro de **ISS** - Entrada/ Saída: O livro de **ISS** para notas fiscais de entrada é o Modelo 56 - Livros Fiscais/Relatórios/Livros Oficiais/Reg. **ISS** Modelo 56.  
Para nota fiscais de saída será utilizado o Modelo 51 - Livros Fiscais/Relatórios/Livros Oficiais/Reg. ISS Modelo 51.  
Para que as informações sejam consideradas no Livro de **ISS** é necessário o preenchimento dos campos **Cód. Serv. ISS** **-** **B1\_CODISS** e **L. Fiscal ISS** =  diferente de Não,para que na geração da nota o campo **F3\_TIPO**= S seja preenchido automaticamente.  
**ISS** no lugar do **ICMS** nos Livros: Caso o sistema considere no livro notas de serviço, mesmo com a pergunta do parâmetro **Destaca NF Serviço?** = Não, verifique o **TES** utilizado e configure o campo **L. Fisc. ICMS** = Não, senão os registros serão duplicados na tabela **SF3**, pois deve-se manter apenas o campo **L. Fiscal ISS** = diferente de Não para escrituração correta do documento.  
O sistema valida o campo **F3\_TIPO** = S para identificar que a nota fiscal é de serviço, sendo necessário o preenchimento dos campos **Cód. Serv. ISS** (**B1\_CODISS)**e **L. Fiscal ISS** =  diferente de Não.  
Após alterações deve-se executar a rotina de reprocessamento para que o livro fiscal possa ser recriado de maneira correta.
