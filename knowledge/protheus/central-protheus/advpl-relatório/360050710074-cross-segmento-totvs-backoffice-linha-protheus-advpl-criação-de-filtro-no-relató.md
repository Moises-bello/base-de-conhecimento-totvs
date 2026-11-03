---
article_id: 360050710074
category: ADVPL - Relatório
content_hash: 9bab0ee8527f2056b0819453af1ff99018cf82cf049685dcc627ac53d5c71c7a
fetched_at: '2026-06-28T22:40:22.784170+00:00'
product: protheus
section_id: 1500001549062
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Criação de filtro
  no Relatório Totvs (Totvs Report) com função de usuário
type: support-article
updated_at: '2021-08-25T23:44:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050710074-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Cria%C3%A7%C3%A3o-de-filtro-no-Relat%C3%B3rio-Totvs-Totvs-Report-com-fun%C3%A7%C3%A3o-de-usu%C3%A1rio
---

**Dúvida**Como criar filtro no Totvs Reports com Função de usuário?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Para a criação e utilização de Parâmetros para Filtro no Totvs Reports realize os seguintes passos:

1. Abrir o relatório o Relatório do Totvs Reports e colocar para incluir o Parâmetro;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012773032/mceclip1.png)

2. Configurar as Perguntas e seus retornos.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078099574/mceclip2.png)

 3. Aplica o filtro no relatório no relacionamento, utilizando a opção **Expressão** e em seguia utilizar informar a função de usuário U\_\*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078099374/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360079258833/mceclip1.png)

No exemplo, fará o filtro por código de Produtos e Descrição que será verificada na função de usuário a partir do parâmetro MV\_PAR03 criado.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078100014/mceclip3.png)

 A função de usuário deverá efetuar a tratativa retornando um lógico .T. caso atenda a validação.

Exemplo:

```
User Function GATILHO ()  
LRET:=.F.  
cProd:= ALLTRIM(MV_PAR03)    
if cProd $ B1_DESC     
   lRet:=.T.  
EndIf         
Return lRet 
```

Retorno gerado ao executar o relatório

**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078100494/mceclip5.png)**

**Saiba Mais**  
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Criação de parametros no totvs reports](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016748571)
