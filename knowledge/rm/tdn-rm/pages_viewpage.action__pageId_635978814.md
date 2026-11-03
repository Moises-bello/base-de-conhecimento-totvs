---
content_hash: 7a60e43c42a4051474b49deededae671d44ba8a1f702e169c9b7368024fc43b9
fetched_at: '2026-06-29T00:11:06.878916+00:00'
page_id: '635978814'
product: rm
source: tdn-rm
title: Exemplos de Customização de Reajuste de CM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=635978814
version: 12
---

Criar um plano de financiamento Price, com os componentes de Juros e Correção Monetária. Sendo que a CM deve ser anual. 

Premissas: 

**1 -** Caso o IGPM anual for superior a 10% ao ano, utilizar 10%, se não, usar o próprio índice;

      Cobrar o índice do IPGM proporcional, caso o cliente antecipe o pagamento de parcelas fora do período do aniversário;

**2 -** Reajustar o contrato apenas no anivérsario do contrato ou quando o cliente antecipar parcelas;

**3 -**  O valor da correção monetária será somente sobre o principal.

Configuração do componente de Correção Monetária com as prremissas implementadas via fórmulas seguindo a sua ordem

CardstrueContrato1 - Customização do Índice |Código da Fórmula

**/\*Se a periodicidade for o seu aniversário utilizo o índice anual, limitado a 10% ao ano,**   
**\*se não for o aniversário e for para aplicar a proporcionalização do CM, utilizo o índice mensal \*/**  
DECL INDICE;

**/\*Se for o aniversário do contrato, reajuste de ano em ano, então:\*/**  
Se EANIVERSARIOPERIODICIDADE = 1 Entao  
     /\* Busca o índice anual \*/  
     SETVAR(INDICE, GETVALORCMMENSAL('IGPM\_ANUAL', ADICIONAMESES(DATREAJUSTE,-1), DATREAJUSTE, 0));  
     **/\*Se índice maior que 10% ao ano, usa 10%, se não usa o da tabela\*/**  
     Se INDICE > 0.10 Entao  
           SETVAR(INDICE, 0.10)   
      FimSe  
Senao  
**/\*Se desejar cobrar o CM proporcional antes do aniversário e estiver configurado para isso, então\*/**  
      Se CALCULARJUROSCMPROPORCIONALANTECIPACAO = 1 Entao  
             **/\*busco o índice mensal acumulado do IGPM desde o último aniverário até a data do boleto\*/**  
            SETVAR(INDICE, GETVALORCMMENSAL('IGPM-M', DATAULTIMOANIVERSARIOPERIODICIDADE, DATREAJUSTE, 0))  
       Senao  
**/\*se não estiver configurado o CM proporcional, então não calcula a correção monetária deste período\*/**  
            SETVAR(INDICE, 0);  
        FimSe  
FimSe

INDICE

Global2 - Reajustar Anualmente |Código da Fórmula

**/\* Se for aniversário do reajsute ou o cliente está antecipando as parcelas, então reajsuta\*/**  
SE EANIVERSARIOPERIODICIDADE = 1 OU   
     CALCULARJUROSCMPROPORCIONALANTECIPACAO = 1 ENTAO  
  1  
SENAO   
  0  
FIMSE

Agendamento3 - Valor BaseCódigo da Fórmula

**/\*Buscar o saldo devedor do componente principal para calcular a correção monetária \*/**  
TABPARCELA('SALDOPRINCIPAL','V')

Reajuste realizado em   com base no valor original e com taxa de 10%

Log do Reajuste da Parcela, mostrando que encontrou o índice de 25,8% e utilizou 10%
