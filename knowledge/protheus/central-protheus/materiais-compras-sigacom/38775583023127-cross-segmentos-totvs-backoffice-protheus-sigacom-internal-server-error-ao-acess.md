---
article_id: 38775583023127
category: Materiais - Compras (SIGACOM)
content_hash: eb930af762026f1f3450256fcc732b647d2af757aa5d324cfbcc20230b42021f
fetched_at: '2026-06-28T22:41:08.982076+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Internal Server Error
  ao acessar o Novo Fluxo de Compras.
type: support-article
updated_at: '2026-03-03T18:07:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38775583023127-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Internal-Server-Error-ao-acessar-o-Novo-Fluxo-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38776119530903) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
Ao acessar a rotina do Novo Fluxo de Compras ocorre o Internal Server Error, impossibilitando a utilização da rotina.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38775566868375)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - A partir da Versão 12.

**Solução**

Uma possível causa para esse erro é o parâmetro MV\_NFCDESC estar com o tipo incorreto (X6\_TIPO).   
Para evitar o problema ao acessar a rotina, é necessário que ele esteja definido como “Caracter”.

O parâmetro deve estar configurado conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38775583017239)

**Observação:**

O Internal Server Error é um erro genérico e não indica a causa exata do problema, caso o erro persista após realizar a validação acima é necessário que contate o suporte.

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
