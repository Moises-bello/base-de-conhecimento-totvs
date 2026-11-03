---
article_id: 32892378200087
category: Manutenção de Ativos (SIGAMNT)
content_hash: e9affd19b2bb24abe8e09660d6c6d5b5acace5b73e526048db51a5a85e41aea6
fetched_at: '2026-06-28T22:42:32.926549+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Como realizar a customização de um evento
  da Planta Gráfica
type: support-article
updated_at: '2025-06-18T13:11:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32892378200087-Manufatura-Linha-Protheus-MNT-Como-realizar-a-customiza%C3%A7%C3%A3o-de-um-evento-da-Planta-Gr%C3%A1fica
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32892378184343)***Tempo aproximado para leitura: **00:01:20 min****Dúvida**Como realizar a customização de um evento para o painel de gestão da rotina **Planta Gráfica**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) -Versão 12  
  
**Solução**Deve-se utilizar a rotina **Edição - MNTA905** para o cadastro do evento. Ao incluir um evento customizado, este obrigatoriamente deve utilizar o tipo **000 - Específico** no campo evento, e no campo função, informar a chamada de uma função de usuário que contenha a regra definida para o evento:

![](https://tdn.totvs.com/download/attachments/955505323/image-2025-6-17_15-49-3.png?version=1&modificationDate=1750186144053&api=v2)

```
#Exemplo de função customizada  
User Function FunTeste( cCodigo, cTipo )  
  
Local cQuery := ''  
  
cQuery := "SELECT "  
cQuery += "COUNT(*) TOTAL "  
cQuery += "FROM "  
cQuery += RetSqlName( 'STJ' ) + " STJ "  
cQuery += "WHERE "  
cQuery += "TJ_FILIAL = " + ValToSQL( FWxFilial( 'STJ' ) ) + " AND "  
cQuery += "TJ_SITUA3CA = 'C' AND "  
cQuery += "TJ_TIPOOS = " + ValToSql( cTipo ) + " AND "  
cQuery += "TJ_CODBEM = " + ValToSql( cCodigo ) + " AND "  
cQuery += "D_E_L_E_T_ = ' '"  
  
Return cQuery
```

**Importante**A função de usuário indicada no evento, deve obrigatoriamente possuir retorno de uma *query*. Sendo assim ao executar está *query* será validado se existe retorno do banco, caso sim é indicando que o evento deverá ser apresentado na **Planta Gráfica**. Sempre que utilizado uma função no evento, esta recebe dois parâmetros. Sendo estes: **P1 - Código do Bem/Localização** e **P2 - Tipo Bem/Localização**.
