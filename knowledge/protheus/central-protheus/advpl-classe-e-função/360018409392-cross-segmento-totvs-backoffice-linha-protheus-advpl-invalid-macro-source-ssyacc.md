---
article_id: 360018409392
category: ADVPL - Classe e Função
content_hash: 4e4ee6d698e47f09d6499d6131206a69b611b6385c07bc8d5439bb33c68030fb
fetched_at: '2026-06-28T22:40:16.963100+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - invalid macro source
  (SSYacc0105e)  função de usuario no menu
type: support-article
updated_at: '2023-01-02T17:16:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018409392-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-invalid-macro-source-SSYacc0105e-fun%C3%A7%C3%A3o-de-usuario-no-menu
---

**Ocorrência**Ao acessar a rotina customizada no ACD gera o erro or

THREAD ERROR ([XXXX], XXXXXXX, XXXXXXX) XX/XX/XXXX XX:XX:XX   
invalid macro source (SSYacc0105e: Error token failed, no valid token)   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 12.1.17  
  
**Causa**Não foi configurado corretamente a chamada da sua *User Function* no menu.  
  
**Solução**O erro específico "invalid macro source (SSYacc0105e: Error token failed, no valid token) :(STATICCALL(#**FUNCAO\_DO\_USUARIO**,MenuDef)) on FWLOADMENUDEF(PROTHEUSFUNCTIONMVC.PRX)" no inicio de 201, o motivo é que foi realizado uma alteração no fonte FWLOADMENUDEF para, no caso de não estar como usuário administrador, macroexecutar as funções afim de validá-las, e como a função de usuário começa com '#' ele gera o erro. Anteriormente a essa alteração já havia sido implementado o TYPE 03, que é específico para funções de usuário, não mais utilizando o '#' para essa finalidade.

Para que não gere mais o erro verifique nos arquivos XNU a chamada de uma função de usuário se está com # ((#**FUNCAO\_DO\_USUARIO**) e TYPE como 01(função Protheus), retire o '#' e altere o TYPE para 03 conforme instruções a seguir:

Errado:

<Function>#**FUNCAO\_DO\_USUARIO**</Function>  
<Type>01</Type>

Certo:

<Function>**FUNCAO\_DO\_USUARIO**</Function>  
<Type>03</Type>

```
OBS:. Caso persista verifique se o nome do fonte está com caractere especial ou iniciando por número.
```

**PASSO A PASSO - ACD**

No ACD a há uma excessão o nome da função de usuario deverá ser iniciado por "U\_"

<Function>**U\_FUNCAO\_DO\_USUARIO**</Function>  
<Type>01</Type>

**Pelo configurador**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014123951/mceclip4.png)

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014120992/mceclip3.png)**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014121372/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014121772/mceclip1.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014123691/mceclip3.png)
