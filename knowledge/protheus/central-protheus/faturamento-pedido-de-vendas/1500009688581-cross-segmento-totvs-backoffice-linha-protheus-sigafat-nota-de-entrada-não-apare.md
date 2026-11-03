---
article_id: 1500009688581
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: a8f723635d54dd216b0047af9bc4bd256c1e4b0f03ec7ccd72c5d5b177e5d125
fetched_at: '2026-06-28T22:38:38.575818+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota de Entrada
  não Aparece para Devolução
type: support-article
updated_at: '2021-09-10T14:37:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009688581-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-de-Entrada-n%C3%A3o-Aparece-para-Devolu%C3%A7%C3%A3o
---

**Dúvida**Estou tentando devolver uma nota de entrada, porem ao utilizar a opção retornar, a nota não aparece.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, orientamos que valide se já existe um pedido de vendas em aberto, com a nota de origem vinculada.

Para isso realize o passo a passo conforme vídeo abaixo:  
![buscar_nota_de_origem.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500015232761/buscar_nota_de_origem.gif)

**Passo a passo do vídeo acima:**1. Filtrar > Outras Ações > Relacionar;  
2. Selecionar o C5\_NUM > Ok;  
3. Criar Filtro > Desmarcar a tabela SC5 > Marcar a tabela SC6;  
4. Buscar o campo N.F Original > Escolher o Operador "Igual a" > Incluir na Expressão o numero da Nota *"Obs: O número da Nota deve estar completo, inclusive com os "0" à esquerda para que o Pedido seja localizado.";*  
5. Adicionar > Dê um nome ao Filtro > Salvar;  
6. Selecione o Filtro > Clique em Aplicar Filtros Selecionados.
