---
article_id: 8665131091223
category: Materiais - Compras (SIGACOM)
content_hash: 543e5cac9a7ca7b1988685c53242f9c3c10f8699401cb1c89ee456882d53a061
fetched_at: '2026-06-28T22:41:17.130218+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Deseja salvar as alterações
  inseridas até o momento na Pré-Nota de Entrada ?
type: support-article
updated_at: '2022-09-05T19:18:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8665131091223-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Deseja-salvar-as-altera%C3%A7%C3%B5es-inseridas-at%C3%A9-o-momento-na-Pr%C3%A9-Nota-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Ao realizar alterações sobre um Documento de Pré-Nota e Sair da rotina através da opção Fechar/Cancelar. Será apresentada a interface abaixo, porém as informações não são salvas.

**Ambiente**

![doc.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8665014658327/doc.png)

**Solução**

O recurso de gravação terá efeito somente para os dados dos itens do documento (campos da tabela SD1).

As demais informações (como despesas acessórias, livros fiscais, duplicatas, entre outras) não serão salvas.

#### **Exemplo:**

1. No módulo de Compras (SIGACOM), inclua uma Pré-nota (MATA140).
2. Na rotina Documento de Entrada (MATA103), posicione o cursor sobre o documento incluído na Pré-nota e clique em Classificar.
3. Realize as alterações e ajustes desejados.
4. Saia da rotina através da opção Fechar/Cancelar.  
   Será apresentada a interface abaixo:
5. Caso escolha a opção "Sim", as alterações realizadas no Cabeçalho (SF1) e Itens (SD1) da Pré-Nota serão salvas sem que o documento seja classificado.
6. Caso seja selecionada a opção "Não", o documento não sofrerá alterações.

***Saiba Mais:***

[Guarda Fiscal no Documento de Entrada](https://tdn.totvs.com/x/XXAzJg)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
