---
article_id: 4410820350743
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: d19a82544c2c4ee71092d8e9a3f3f6fb3ef459ddce0d068ab36807a17d83a7e4
fetched_at: '2026-06-28T22:36:56.508855+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Tabela responsavel
  pela sequencia da Manutenção de OIC
type: support-article
updated_at: '2021-10-27T17:41:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410820350743-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Tabela-responsavel-pela-sequencia-da-Manuten%C3%A7%C3%A3o-de-OIC
---

**Dúvida**Como acerto a sequencia no cadastro da rotina **Manutenção de OIC´s** no Embarque de Exportação **(EECAE100)** uma vez que a informação foi digitada de forma errada?

**Ambiente***Cross Segmento - TOTVS Backoffice (Linha Protheus)  – Easy Export Control – Todas versões*  
  
**Solução**

Ao efetuar inclusão da Manutenção de OIC que o sistema sempre pega a sequência seguinte do maior registro na tabela. Exemplo : (Se o último é 200, o sistema vai pegar 201, e assim por diante).  
Se foi digitado uma numeração errada e foi entendido que não é o certo, é só excluir este OIC errado que o sistema vai entender o anterior que é a numeração maior.  Para excluir é só acessar o embarque de exportação (ECCAE100) :

1) Menu Outras Ações -> Manutenção de OIC ->Outras Ações -> Excluir.

2) Com isso será excluída a numeração errada.

**![MANUTEN__O_DE_OIC_-_EXCLUIR.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4411554959895/MANUTEN__O_DE_OIC_-_EXCLUIR.PNG)**

3) Cadastro responsável pela sequencia da OIC é a tabela **EXZ** (Organização Internacional Café) . Caso o cliente deseje fazer o ajuste da numeração em vez de excluir é só acessar via **APSDU** e fazer o ajuste da sequencia no campo **EXZ\_OIC**.

![exz.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410991668375/exz.png)

**Saiba Mais****[Quebra da Estufagem por OIC](https://tdn.totvs.com/display/public/mp/Quebra+da+Estufagem+por+OIC)**
