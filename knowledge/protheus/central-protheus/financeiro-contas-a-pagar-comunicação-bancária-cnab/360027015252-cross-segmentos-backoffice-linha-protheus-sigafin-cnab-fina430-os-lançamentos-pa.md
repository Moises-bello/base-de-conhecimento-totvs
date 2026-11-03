---
article_id: 360027015252
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 1c1212244a384151bb0bd35677fef2a0002b1b6e4c6d38a8626d416a8284c5c3
fetched_at: '2026-06-28T22:37:55.030718+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - FINA430 - Os
  lançamentos padrões 530 e 532 contabiliza o Retorno de Pagamento
type: support-article
updated_at: '2026-01-28T16:58:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027015252-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-FINA430-Os-lan%C3%A7amentos-padr%C3%B5es-530-e-532-contabiliza-o-Retorno-de-Pagamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33206063574807)**Tempo aproximado para leitura: **00:05min**

**Dúvida**  
Os lançamentos padrões 530 e 532 contabiliza o Retorno de Pagamento (FINA430)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões  
  
**Solução**  
No padrão, será contabilizado o **Retorno de Pagamento** (**FINA430)** pelo **Lançamento Padrão: 530**, independentemente se o título está em borderô ou não.

Para contabilizar pelo **Lançamento Padrão**: **532**, deve-se utilizar o **ponto de entrada: FA430LP**, que altera a utilização do ponto de entrada do LP 530 para o LP 532.  
  
Ponto de Entrada

|  |  |
| --- | --- |
| **Descrição:** | Ponto de entrada FA430LP altera a utilização do LP530 para o LP532*.* |
| **Localização:** | Brasil |
| **Eventos:** | Retorno da comunicação bancaria - Pagar |
| **Programa Fonte:** | FINA430 |
| **Função:** | FINA430 |
| **Retorno:** | |  |  |  |  | | --- | --- | --- | --- | | **Nome** | **Tipo** | **Descrição** | **Obrigatório** | | **lTrocaLp** | logico | retorna .T. ou .F. | Sim | |

Na contabilização online via rotina FINA430, no LP 530, deve-se utilizar os campos da SE5->E5\_VALOR.

Também podemos usar variáveis para contabilização.  
  
**VARIÁVEIS CONTÁBEIS DISPONÍVEIS**  
**VALOR** - Variável totalizadora dos valores de pagamentos efetuados sobre os títulos do borderô - disponível na contabilização online e offline;  
**VALOR2** - Variável totalizadora dos descontos aplicados sobre o pagamento do(s) borderô(s) - disponível na contabilização offline;  
**VALOR3** - Variável totalizadora dos juros aplicados sobre o pagamento do(s) borderô(s) - disponível na contabilização offline;  
**VALOR4** - Variável totalizadora das multas aplicadas sobre o pagamento do(s) borderô(s) - disponível na contabilização offline;  
**VALOR5** - Variável totalizadora da correção monetária aplicada sobre o pagamento do(s) borderô(s) - disponível na contabilização offline;  
**STRLCTPAD** - Contém o(s) número(s) do(s) borderô(s) - disponível na contabilização offline;  
Na contabilização offline (CTBAFIN), caso o lançamento contábil seja o aglutinador de vários borderôs, essa variável será disponibilizada com uma lista de todos eles (separados por ponto e virgula);  
  
**Importante**

Referente a datas de contabilização, o comportamento do sistema segue abaixo.   
  
1 - **Contabilização Online 530** - Se houve contabilização online, sempre será pela **Data-base /** **E5\_DTDIGIT**  
2 - **Contabilização Offline 532**- Se houve contabilização Offline, sempre será pela data definida nos parâmetros da rotina **CTBAFIN**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33567867595159)

**Saiba mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA080 - Qual sintaxe em ADVPL deve ser utilizado na contabilização online do LP 530 e 531](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36728781992087-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Qual-sintaxe-em-ADVPL-deve-ser-utilizado-na-contabiliza%C3%A7%C3%A3o-online-do-LP-530-e-531)
