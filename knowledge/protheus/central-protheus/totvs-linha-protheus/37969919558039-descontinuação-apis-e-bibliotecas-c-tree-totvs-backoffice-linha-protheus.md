---
article_id: 37969919558039
category: TOTVS Linha Protheus
content_hash: c059fa8f1ce8d2704421527c1df778a1faadac1db64fda60ebd16c4205989afa
fetched_at: '2026-06-28T22:36:18.780024+00:00'
product: protheus
section_id: 360001794451
source: central-protheus
title: 'Descontinuação - APIs e bibliotecas C-tree - TOTVS Backoffice (Linha Protheus) '
type: support-article
updated_at: '2026-01-27T17:33:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37969919558039-Descontinua%C3%A7%C3%A3o-APIs-e-bibliotecas-C-tree-TOTVS-Backoffice-Linha-Protheus
---

Prezado Cliente,

Os produtos TOTVS estão em constante evolução para acompanhar cada etapa da jornada digital da sua empresa.

Diante disso, comunicamos que as **APIs e bibliotecas C-tree - TOTVS Backoffice (Linha Protheus)** serão descontinuadas em **19/10/2026.**

A seguir, esclarecemos as possíveis dúvidas sobre a descontinuação.

**O que vai acontecer com os meus dados?**

O Protheus padrão já migrou todos dados e dicionários que usavam c-tree para o banco de dados e atualmente não depende das bibliotecas c-tree.

Os pontos de atenção são as customizações AdvPL que foram codificadas para usar a RDD CTREECDX ou CTREETMP, pois, essas dependem diretamente das bibliotecas c-tree.

Para garantir uma transição fácil, recomendamos que:

* Seja feita a revisão dos códigos fontes customizados com objetivo de assegurar que não façam uso das RDDs CTREECDX ou CTREETMP;
* Caso faça uso da RDD CTREECDX, altere o código para DBFCDX e no INI do AppServer utilize a configuração LOCALFILES=SQLITE;
* Caso faça uso da RDD CTREETMP, altere o código para SQLITE\_TMP;

**Documentação de apoio:**

LocalFiles: <https://tdn.totvs.com/x/fopc>

RDDs suportadas: <https://tdn.totvs.com/x/DXVvHw>

Documentação com mais informações sobre a descontinuação do c-tree: <https://tdn.totvs.com/x/BtwNOw>

Lembrando que a TOTVS sempre atuará observando toda e qualquer legislação aplicável e eventuais deveres de confidencialidade existentes.

**O que vai acontecer após a data da descontinuação?**

Conforme nossa Política de Ciclo de Vida de Software, a partir da data de descontinuação, a TOTVS não irá evoluir, prestar suporte ou dar manutenção para o produto descontinuado.

 

Um abraço,

Equipe TOTVS.
