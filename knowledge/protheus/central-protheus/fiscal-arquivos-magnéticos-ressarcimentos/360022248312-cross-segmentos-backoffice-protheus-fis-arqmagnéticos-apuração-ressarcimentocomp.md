---
article_id: 360022248312
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: 1fef42b6fa27dbbff898e7683f1b02c0e2496eca6c4c6a04d26201c426e04e9b
fetched_at: '2026-06-28T22:42:12.676580+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Apuração Ressarcimento/Complemento
  ICMS ST  - FISA190 - Rotina de carregar saldos iniciais não grava informações do
  produto
type: support-article
updated_at: '2022-08-18T17:52:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022248312-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Apura%C3%A7%C3%A3o-Ressarcimento-Complemento-ICMS-ST-FISA190-Rotina-de-carregar-saldos-iniciais-n%C3%A3o-grava-informa%C3%A7%C3%B5es-do-produto
---

**Dúvida**Quando carregamos os saldos dos produtos através da opção "**Carregar saldos iniciais**" na rotina **FISA190**, alguns produtos não são gravados na tabela **F2V**. Por quais motivos estes produtos não são carregados?

**Ambiente**

Protheus - Livros Fiscais - A partir da versão 12.1.17

**Solução**Existem diversos motivos pelo qual um produto não é carregado através da opção "**Carregar saldos iniciais**". Abaixo listamos algumas delas.

1. O campo **B1\_CRICMS** está com conteúdo diferente de 1:Só são considerados na **CAT 42**, os produtos que estão com o campo **B1\_CRICMS** = 1. Este campo fica na aba Outros no cadastro de produtos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019472832/mceclip2.png)

2. O tamanho do campo **F2V\_DESPRO** é diferente do tamanho **B1\_DESC:** O campo **F2V\_DESPRO** vem como padrão tamanho 30 (mesmo tamanho padrão do campo **B1\_DESC**).

Se o conteúdo do campo **B1\_DESC** estiver com tamanho maior que o tamanho do campo **F2V\_DESPRO** o produto não será gravado na tabela **F2V**. Para solução deste erro, altere o tamanho do campo **F2V\_DESPRO** para que fique igual ao tamanho do campo **B1\_DESC**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019470912/mceclip1.png)

3. O arquivo gerado pelo **P7** não trouxe os valores do produto:Neste cenário, ao gerar o arquivo do **P7**, o produto não foi carregado na tabela **H\_aaaammddeeff**, onde:

aaaammdd = ano/mes/dia de geração do **P7**

eeff=codigo da empresa + codigo da filial no **Protheus**.

 Certifique-se de que o produto está nesta tabela do **P7** e caso não esteja, será necessário executar o relatório **MATR460** para que os saldos sejam carregados.

![H010.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360019472292/H010.gif)

Mais informações sobre o processo de geração do **P7**, consulte nossa documentação: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019765272-MP-FIS-SPED-FISCAL-Como-gerar-o-Bloco-H-do-Sped-Fiscal>

4. A quantidade apresentada no arquivo do **P7** é menor que a quantidade de compras escrituradas na **SFT.**

Nesta situação, o arquivo não é gerado se a quantidade apresentada na tabela do **P7** (o nome da tabela está descrito no item 3) é maior que o resultado da *query* abaixo:

*SELECT* *Sum*(**SFT**.**ft\_quant**) QUANT   
*FROM* **sftt10 SFT**  
*INNER* *JOIN* f2wt10 **F2W**  
*ON* ( **F2W**.f2w\_filial = 'M SP 01 ' -> Substitua pelo código da sua filial  
*AND* **F2W**.f2w\_cfop = **SFT**.ft\_cfop   
*AND* F2W.d\_e\_l\_e\_t\_ = ' ' )   
*INNER* *JOIN* f3mt10 **F3M**  
*ON* ( **F3M**.f3m\_filial = 'M SP 01 ' -> Substitua pelo código da sua filial  
*AND* **F3M**.f3m\_idf2w = **F2W**.f2w\_idtab   
*AND* **F3M**.f3m\_csticm = *RIGHT*(**SFT**.ft\_clasfis, 2)   
*AND* **F3M**.d\_e\_l\_e\_t\_ = ' ' )   
*WHERE* **SFT**.ft\_filial = 'M SP 01 '  -> Substitua pelo código da sua filial  
*AND* **SFT**.ft\_produto = '**CAT42**'  -> Substitua pelo código de seu produto  
*AND* **SFT**.ft\_tipo *NOT IN* ( 'D', 'B', 'S' )   
*AND* **SFT**.ft\_tipomov = 'E'   
*AND* **SFT**.ft\_dtcanc = ' '   
*AND* **SFT**.ft\_entrada <= '20181231' -> Substitua pela data de fechamento que foi informado na rotina "**Carregar Saldos Iniciais**"  
*AND* **SFT**.d\_e\_l\_e\_t\_ = ' '

Caso a quantidade retornada nesta consulta seja menor que o valor apresentado no **P7**, a rotina não irá retornar dados. Certifique-se de que há notas suficientes na **SFT** respeitando os filtros acima para que a quantidade das notas fiscais seja maior ou igual o apresentado no **P7** para que seja possível buscar as notas fiscais suficientes para compor o saldo que será alimentado na **F2V**.

5. A *query* que busca os documentos de entrada com os valores de ICMS próprio, retido e recolhido anteriormente não trouxe informações

A *query* abaixo é executada para trazer os valores de **ICMS** dos produtos. Caso não encontre documentos, os valores de **ICMS** não será calculado e consequentemente não será gravado a tabela **F2V**:

*SELECT* **SFT**.**FT\_CLASFIS**,  
**SFT**.**FT\_ENTRADA**,  
**SFT**.**FT\_NFISCAL**,  
**SFT**.**FT\_SERIE**,  
**SFT**.**FT\_CLIEFOR**,  
**SFT**.**FT\_LOJA**,  
**SFT**.**FT\_ITEM**,  
**SFT**.**FT\_PRODUTO**,   
**SFT**.**FT\_CFOP**,  
*CASE**WHEN* **SFT**.**FT\_VALICM** = 0  
*AND* (**SFT**.**FT\_BASEICM** + **SFT**.**FT\_OUTRICM**) > 0 *THEN* **SD1**.**D1\_VALICM**  
*ELSE* **SFT**.**FT\_VALICM**  
*END AS* **VALORICMS**,  
**SFT**.**FT\_ICMSRET** + **SFT**.**FT\_VALANTI AS** VALORST,  
*CASE**WHEN RIGHT*(**SFT**.**FT\_CLASFIS**, 2) = '60'  
*AND* (**SFT**.**FT\_ICMSRET** + **SFT**.**FT\_VALANTI**) = 0 *THEN* **SFT**.**FT\_ICMNDES**  
*ELSE* 0  
*END **AS*** VALORANT,  
**SFT**.**FT\_TOTAL** + **SFT**.**FT\_FRETE** + **SFT**.**FT\_SEGURO** + **SFT**.**FT\_DESPESA** - **SFT**.**FT\_DESCONT AS** BASE,  
**SFT**.**FT\_QUANT AS** QUANT,  
**SD1**.**D1\_VALICM**,  
**SD1**.**D1\_BASEICM**,  
**SD1**.**D1\_ICMSRET**,  
**SD1**.**D1\_ICMNDES**,  
**SD1**.**D1\_ICMSCOM**,  
**SB1**.**B1\_PICMENT**,  
**SD1**.**D1\_ALIQSOL**,  
**SD1**.**D1\_PICM**  
*FROM* **SFT030** (*NOLOCK*) AS **SFT**  
*INNER JOIN* **SD1030** (*NOLOCK*) *AS* **SD1** *ON* **SD1**.**D1\_FILIAL** = '01' -> Substitua pelo código da sua filial  
*AND* **SD1**.**D1\_DOC** = **SFT**.**FT\_NFISCAL**  
*AND* **SD1**.**D1\_SERIE** = **SFT**.**FT\_SERIE**  
*AND* **SD1**.**D1\_FORNECE** = **SFT**.**FT\_CLIEFOR**  
*AND* **SD1**.**D1\_LOJA** = **SFT**.**FT\_LOJA**  
*AND* **SD1**.**D1\_COD** = **SFT**.**FT\_PRODUTO**-> Substitua pelo código de seu produto  
*AND* **SD1**.**D1\_ITEM** = **SFT**.**FT\_ITEM**  
*AND* **SD1**.D\_E\_L\_E\_T\_ = ' '  
*INNER JOIN* **F2W030** (*NOLOCK*) *AS* **F2W** *ON* **F2W**.**F2W\_FILIAL** = '01' -> Substitua pelo código da sua filial  
*AND* **F2W**.**F2W\_CFOP** = **SFT**.**FT\_CFOP**  
*AND* **F2W**.D\_E\_L\_E\_T\_ = ' '  
*INNER JOIN* **F3M030** (*NOLOCK*) *AS* **F3M** *ON* **F3M**.**F3M\_FILIAL** = '01' -> Substitua pelo código da sua filial  
*AND* **F3M**.**F3M\_IDF2W** = **F2W**.**F2W\_IDTAB**  
*AND* **F3M**.**F3M\_CSTICM** = *RIGHT*(**SFT**.**FT\_CLASFIS**, 2)  
*AND* **F3M**.D\_E\_L\_E\_T\_ = ' '  
*INNER JOIN* **SB1030** (*NOLOCK*) *AS* **SB1** *ON* **SB1**.**B1\_FILIAL** = '01' -> Substitua pelo código da sua filial  
*AND* **SB1**.**B1\_COD** = **SFT**.**FT\_PRODUTO**-> Substitua pelo código de seu produto  
*AND* **SB1**.D\_E\_L\_E\_T\_ = ' '  
*WHERE* (**SFT**.**FT\_FILIAL** = '01') -> Substitua pelo código da sua filial  
*AND* (**SFT**.**FT\_PRODUTO** = '010002') -> Substitua pelo código de seu produto  
*AND* (**SFT**.**FT\_TIPO NOT** **IN** ('D','B','S','P','I', 'C'))  
*AND* (**SFT**.**FT\_TIPOMOV** = 'E')  
*AND* (**SFT**.**FT\_DTCANC** = '')  
*AND* (**SFT**.**FT\_ENTRADA** >= '20181201') -> mes que ouve a entrada do documento fiscal  
*AND* (**SFT**.**FT\_ENTRADA** <= '20181230') -> mes que ouve a entrada do documento fiscal  
*AND* (**SFT**.**FT\_NFORI** = ' ')  
*AND* (**SFT**.**FT\_SERORI** = ' ')  
*AND* (**SFT**.**FT\_ITEMORI** = ' ')  
*AND* (**SFT**.**FT\_FORMUL** <> 'S')  
*AND* (**SFT**.D\_E\_L\_E\_T\_ = ' ')  
*AND* **FT\_CLASFIS** *LIKE* '%60'  
*ORDER BY* **SFT**.**FT\_ENTRADA** DESC,  
**SD1**.**D1\_NUMSEQ** DESC

Atenção: A *query* irá buscar as notas fiscais em ordem decrescente do mês do fechamento de estoque para trás, caso não encontre notas ou o saldo não seja suficiente para compor a quantidade apresentada no estoque, o sistema irá executar a mesma *query*, porém filtrando o mês anterior. Iremos repetir a *query* até encontrar notas fiscais suficientes para compor a quantidade em estoque. Exemplo:

Quantidade em estoque 12/2018 = 40  
Compras no mês 12/2018 = 5  
Compras no mês 11/2018 = 20  
Compras no mês 07/2017 = 15

O sistema irá executar a *query* acima todos os meses até o mês de julho de 2017 para compor a quantidade suficiente do que está em estoque.

 A rotina soma o valor dos campos **SFT**.**FT\_VALICM** + **SFT**.**FT\_ICMSRET** + **SFT**.**FT\_VALANTI** + **SFT**.**FT\_ICMNDES** e realiza a média dos valores até chegar na quantidade que está no saldo de estoque e registro de inventário. Exemplo:

Quantidade em estoque = 30  
**FT\_QUANT** = 40  
**FT\_VALICM** = R$ 446,90  
**FT\_ICMSRET** = R$ 156,42  
ICMS + **ICMSRET** = R$ 603,32  
603,32 / 40 (**FT\_QUANT**) = 15,08  
Com base no exemplo acima, será gravado estes valores na **F2V**:  
**F2V\_QTDSLD** = 30  
**F2V\_VUNSLD** = 15,08  
**F2V\_VTOSLD** = 452,4
