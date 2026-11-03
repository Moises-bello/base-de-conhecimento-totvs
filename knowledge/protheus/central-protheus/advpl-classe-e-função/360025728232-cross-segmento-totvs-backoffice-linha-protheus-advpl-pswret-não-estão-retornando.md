---
article_id: 360025728232
category: ADVPL - Classe e Função
content_hash: e972322adb7c928d364c8461b9d7cb82677fbabcd79afbf5e3ab3118b4bf1f03
fetched_at: '2026-06-28T22:40:17.093409+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - PswRet não estão
  retornando as informações do usuário logado
type: support-article
updated_at: '2021-11-12T18:57:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025728232-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-PswRet-n%C3%A3o-est%C3%A3o-retornando-as-informa%C3%A7%C3%B5es-do-usu%C3%A1rio-logado
---

**Dúvida**Após a atualização da ultima LIB todos os nossos fontes que utilizam a função PswRet não estão retornando as informações do usuário logado.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**A função [PswRet](http://tdn.totvs.com/pages/viewpage.action?pageId=267792734) apresenta problemas quando utilizado a partir da versão 12 do Protheus, conforme informado na documentação. O recurso em questão foi desfragmentado em funções específicas para cada necessidade, disponível na árvore <http://tdn.totvs.com.br/pages/releaseview.action?pageId=6814847>

Seguem alguns exemplos básicos:

```
RetCodUsr( ) //Retorna o código do usuário logado
```

```
PswChave(RetCodUsr()) //Retorna o nome do usuário
```

```
FwGetUserName(RetCodUsr()) //Retorna o nome completo do usuário
```

```
UsrRetGrp(PswChave(RetCodUsr()),RetCodUsr()) //Retorna um array contendo todos os códigos dos Grupos de Usuário em que o Usuário, passado na função, pertence.
```

**Saiba mais**  
[RetCodUsr](https://tdn.totvs.com/display/public/PROT/RetCodUsr)
