---
article_id: 360018402211
category: ADVPL - Classe e Função
content_hash: 3c0571075aee3e88d1eee6c7ea6a59b41853cacd51bda507bfbc988394e072ce
fetched_at: '2026-06-28T22:40:16.979103+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Manipular pergunta
type: support-article
updated_at: '2024-09-30T18:37:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018402211-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Manipular-pergunta
---

**Dúvida**Gostaria de saber como manipular uma pergunta em uma rotina customizada?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**Neste caso é só chamar o Pergunte e atribuir .F. no segundo parâmetro e atribuir o novo valor para os **MV\_PAR** correspondentes.

```
Pergunte("sua pergunta",.F.)  
  
MV_PAR01:=1  
MV_PAR02:="TESTE"
```

**OBS.**Sempre que for necessário utilizar um **Pergunte** dentro de alguma customização é necessário guardar o grupo da **SX1** posicionado antes de iniciar as validações e retorná-lo após o término.  
Existem diversas formas para guardar e restaurar um pergunte, como as variáveis MV\_PAR são *privates* e compartilhadas em todo a execução do sistema, a mais utilizada é guardar essas variáveis e restaurá-las ao final de sua intervenção.

Exemplo:

```
//No início de sua customização, antes de qualquer validação  
aMvPar := {}  
  
For nX := 1 To 40  
 aAdd( aMvPar, &( "MV_PAR" + StrZero( nX, 2, 0 ) ) )  
Next nX  
  
  
//No final da customização  
For nX := 1 To Len( aMvPar )  
 &( "MV_PAR" + StrZero( nX, 2, 0 ) ) := aMvPar[ nX ]  
Next nX
```

**Saiba mais**

[ADVPL - Qual função permite acessar e editar um grupo de perguntas SX1 Pergunte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8188934752535-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Qual-fun%C3%A7%C3%A3o-permite-acessar-e-editar-um-grupo-de-perguntas-SX1-Pergunte)
