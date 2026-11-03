---
article_id: 10898945512087
category: Financeiro - Viagens
content_hash: 6c4f636963888f43714e5db115e2e29cf178f45e71511eb1b24b41ffd4115fad
fetched_at: '2026-06-28T22:38:21.431045+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA677 - Conversão
  de taxa de moeda APP e Minha Prestação de contas
type: support-article
updated_at: '2024-09-11T16:29:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10898945512087-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA677-Convers%C3%A3o-de-taxa-de-moeda-APP-e-Minha-Presta%C3%A7%C3%A3o-de-contas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26300779580183) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**  
No módulo Financeiro , ao receber uma viagem do APP Minha prestação de contas, onde foi incluída a taxa de moeda, o sistema não converte.  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - SIGAFIN - [Todas as versões]  
  
**Causa**FINA677 recebe a Prestação mas não converte a taxa pelo valor em dólar Moeda 2 e a ao tentar liberar apresenta erro de VALOR em Reais vazio.   
  
**Solução**  
Para efetivar a aprovação da prestação de contas em moedas estrangeira e gerar título no financeiro (contas a pagar ou contas a receber), é necessário avaliarmos a configuração do parâmetro **MV\_TPTXPCT**.

1-Taxa Turismo;

2-Comercial, primeiro dia;

3-Comercial, ultimo dia;

**CENÁRIO 1-Taxa Turismo;**

**MV\_TPTXPCT = 1**  
Define o tipo de taxa de turismos a ser usado na prestação de contas para geração do título no financeiro.

Quando o parâmetro estiver configurado com o conteúdo **1** (**Taxa Turismo**), na aba outros deve-se preencher o campo **FLF\_TXTUR2** ou **FLF\_TXTUR3**.   
Para moeda dólar, preencher o campo: **FLF\_TXTUR2**.  
Para moeda euro, preencher o campo **FLF\_TXTUR3**.  
Para Outras Moedas, preencher o campo **FLF\_TXTUR2**com a taxa do DOLAR baseada na moeda utilizada

Por exemplo, para o aplicativo utilizando 9 - Outras Moedas, a taxa de conversão deve ser baseada no DÓLAR e não na taxa da própria moeda, por exemplo, PESO MEXICANO  
  
Exemplo 100 Pesos Mexicanos x a taxa do Dólar 19,98 = Equivalente a 5,00 Dólares

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26300802872471)

Ao gerar a prestação de contas pelo Protheus ou App, a taxa deve ser baseada na Moeda x Dolar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26300779589527)  
  
O Valor gerado na Prestação de Contas, será o valor da moeda exibido em Dólar

![](https://p23.zdusercontent.com/attachment/888110/LGslwKiIDC3rYDzuEWNwOo4fc?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..rXwGB1gQbYWOlE8Ff-05mg.O6Nv55PdmNFcq1hGKrsaODQTMlW4QzTYoLPsutmR4nUTUrC30TqQueCV0jH59bdJAWSEW_5iOhQ3IGX-pqIygSYpCOg68t5eUmeSGSIn1nR6MX4Ub3XgHD83HnWNK3MlKGhfZDxVsuhLOr-VlMybq0Z-xt-0Eic4h-IJlJjOb7ivlvxa5PhDzg4vUuuKYYWNjaQMaz4osXaJpoHe7ZpEJDcKksqK76gRCD1NfQkz5lliJpZbIeiKn0XzB_93ZSNILPUdxov7PyJ0cNP-J6L24h3ZoppuzYkpQvL52lE8q90.i1Fyh4S0x0Tj8mE9600pdA)

Como o parametro **MV\_TPTXPCT está igual a "1"**, hoje é necessário informar a taxa de conversão de turismo no momento da conferência da Viagem em Outros -  Dolar Turismo ou Euro Turismo  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26300802875799)  
  
Na geração do Financeiro, será gerado o valor com base no valor da taxa de Turismo, o valor de 5,01 x 5,6100 = 28,11 Reais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26300802878487)

**CENÁRIO 2 - Primeiro dia da viagem;**  
**MV\_TPTXPCT = 2**

Quando o parâmetro estiver configurado com o conteúdo **2** (**Taxa Comercial** **primeiro** **dia**), será usado a cotação cadastrada na tabela **SM2 (MATA090)** na data de saída da prestação de contas.

Como preencher automaticamente as moedas via JOB Schedule diariamente:  
  
**JOB FINXTAXA: [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - MATA090 - Cadastrar Taxas de Moeda automaticamente via Schedule FINXTAXA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11821936684183-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-MATA090-Cadastrar-Taxas-de-Moeda-automaticamente-via-Schedule-FINXTAXA)**

X6\_CONTEUD Moeda 2 para o DOLAR = 1

X6\_CONTEUD Moeda 3 para o EURO = 21620

**CENÁRIO 2 - Ultimo dia da viagem;**  
**MV\_TPTXPCT = 3**  
Caso o parâmetro esteja configurado com o conteúdo **3** (T**axa comercial último dia**),  
será usado a cotação cadastrada na tabela **SM2** na data de chegada da prestação de contas.

Portanto, é obrigatório que haja cotação cadastrada na data inicial (**saída**) ou data final (**Chegada**) da prestação de contas quando o parâmetro estiver configurado com o conteúdo **2** ou **3**.

O campo **Tx** Conversão (**FLE\_TXCON**) que fica no grid de despesa é usado apenas na conversão de moeda da própria linha de despesa do grid para gerar o totalizador das despesas.  
  
**Saiba mais:**  
**[Viagens - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12)**

**[Guia de uso - Minha Prestação de Contas](https://tdn.totvs.com/pages/releaseview.action?pageId=287057777#despesa--1332893246)**
