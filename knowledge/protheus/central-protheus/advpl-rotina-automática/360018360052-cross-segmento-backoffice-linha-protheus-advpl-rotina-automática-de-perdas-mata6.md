---
article_id: 360018360052
category: ADVPL - Rotina Automática
content_hash: 596a17c0f4334a4aac3fb9b453de206e4f08ed61bdd6d677a6e575433a6c501d
fetched_at: '2026-06-28T22:40:24.186308+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Rotina Automática de perdas
  -MATA685 - Estorno
type: support-article
updated_at: '2021-12-29T19:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018360052-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Rotina-Autom%C3%A1tica-de-perdas-MATA685-Estorno
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Esta utilizando a rotina **mata685** para apontamento de perda , onde o mesmo esta realizando com a opção (6) para estorno de apontamento ocorre que foi feito a produção do produto utilizando por exemplo 10 item de um determinado produto componente de um produto acabado.  
Ao utilizar essa quantidade o estoque deste mesmo ficou negativo, porém ao realizar o estorno desse produto como perda esta dando a mensagem que não é possível o estorno por que o estoque do produto esta negativo .  
Efetuei um teste com o Parâmetro (**MV\_ESTNEG**) habilitado para trabalhar com estoque negativo dessa forma o sistema aceitou.  
Porém o caso do cliente este mesmo não pode trabalhar com o estoque negativo .  
Dúvida neste caso o correto seria o sistema reclamar pois de fato o estoque esta negativo ou pelo fato de ser um estorno não deveria visualizar dessa forma e aceitar o estorno.  
Qual seria o conceito desse processo.

EX:

```
#Include 'Protheus.ch'  
#Include 'Tbiconn.ch'  
User Function xMATA685()  
Local nOpc := 6 //-Opção de execução da rotina, informado nos parâmetros quais as opções possíveis  
Local aCabec := {}  
Local aItens := {}  
Local aLinha := {}  
local dDatabase  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "PCP"  
conout ("teste de pcp")  
aCabec := "BC_OP" ,"00005001001 ",NIL  
aItens := {{"BC_QUANT" ,1 ,NIL},;  
{"BC_PRODUTO" ,"F003 " ,NIL}  
,;  
{"BC_LOCORIG" ,"01" ,NIL}  
,;  
{"BC_TIPO" ,"R" ,NIL}  
,;  
{"BC_DTVALID" ,dDatabase ,NIL}  
,;  
{"BC_MOTIVO" ,"FH" ,NIL}}  
AAdd(aLinha ,aItens)  
lMSErroAuto := .F.  
MsExecAuto (  
{|x,y,z|MATA685(x,y,z) }  
,aCabec,aLinha,nOpc)  
If lMSErroAuto  
MostraErro()  
endif  
RESET ENVIRONMENT  
Retur
```

**Ambiente**Protheus – ADVPL - A partir da versão 11.80  
  
  
**Solução**

Conforme o retorno do cliente, no caso dele, o produto em questão controla endereço.  
Quando o produto controla endereço ou lote, o estoque nunca pode ficar negativo.  
Mesmo o parâmetro marcado para permitir estoque negativo, quando o produto controla endereço ou lote, não é possível ter estoque negativo.  
Todo o controle de estoque está preparado e consistindo essa regra, não é uma validação exclusiva do PCP.  
Para esse caso, em que o produto controla endereço, deve ser verificado a origem do problema, qual programa fez essa movimentação incorreta, deixando o estoque negativo.  
Para corrigirmos a origem do problema.  
E para os casos em que o produto já esteja com o saldo negativo, deverá ser feito um ajuste desse saldo.
