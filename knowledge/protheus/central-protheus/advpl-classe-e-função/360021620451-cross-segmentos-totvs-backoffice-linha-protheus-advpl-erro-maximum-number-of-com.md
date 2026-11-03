---
article_id: 360021620451
category: ADVPL - Classe e Função
content_hash: 79e26e27bceeebd87c4a177ec236f888d43620f425ac21a2149fa26a88142733
fetched_at: '2026-06-28T22:40:19.246123+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Erro: Maximum
  number of components per window exceeded'
type: support-article
updated_at: '2022-01-10T13:57:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021620451-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-Maximum-number-of-components-per-window-exceeded
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:04:00 min  
  
Ocorrência**

Ao executar um programa **AdvPL**, cujo código fonte tenta criar mais de 999 componentes visuais, o **TOTVS Application** **Server** emite uma mensagem de erro.

**Exemplo:**

```
ERRO THREAD ([5244], user_teste, MAQ-TESTE)       
 Stack :  
Maximum number of components per window exceeded!
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**Esse erro ocorre, pois o fonte tenta criar mais de 999 componentes visuais.  
Você pode utilizar o **FreeObj**(), para limpar a memoria, porém sem o destrutor adequado, está sujeito a um   "*RunTime Leak*" (ou vazamento de memória em tempo de execução), onde cada criação de uma nova instância de uma determinada classe não é automaticamente limpa da memória no caso de saída de escopo ou até mesmo atribuindo NIL apenas na variável que contém o objeto, pois o fato dele ainda ter uma referência em uso o impede de ser eliminado da memória, mesmo que a referência esteja em uso por ele mesmo.   
  
**Solução**O programa **AdvPL** deve ser corrigido para não criar um número superior a 999 componentes visuais. Para isso, solicite a correção do programa a área responsável pelo programa/ambiente.  
O **TOTVS Application Server** foi corrigido para não parar a execução após o erro do programa.

```
Você pode tentar utilizar o End()  
oDialog:End() // exemplo
```

**ou**

```
User Function Exemplo()  
  Local oObj := MyClass():New()  
  
  oObj:DoSomething("Hello")  
  oObj:DoNothing("Goodbye")  
  FreeObj(oObj)  
  
Return
```

**Saiba mais**[Maximum number of components](http://tdn.totvs.com/pages/viewpage.action?pageId=6065138)  
[FreeObj](http://tdn.totvs.com/display/tec/FreeObj)  
[Classe TDialog](http://tdn.totvs.com/display/tec/TDialog)
