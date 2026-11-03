---
article_id: 4413532289047
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 84af7e3310b1f57ba73259afea61863c3d20595c87199ba0d847a6aa9ef34f7c
fetched_at: '2026-06-28T22:38:38.440192+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - array out of
  bounds ( 0 of 115 ) on A410BLQREG(MATN410.PRW) '
type: support-article
updated_at: '2021-11-19T16:46:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413532289047-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-array-out-of-bounds-0-of-115-on-A410BLQREG-MATN410-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar a cópia do Pedido de Vendas e clicar em salvar, o sistema apresenta o erro:  
**array out of bounds ( 0 of 115 ) on A410BLQREG(MATN410.PRW)**   
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Causa**

Erro de array out of bounds ocorre quando algum campo do array não existe no dicionário de dados (sx3), não está como usado ou teve seu nível mudado de 1.  
  
Neste erro, o  array está apontando para o campo **c6\_descont**, que pode ser que esteja com o uso demarcado ou com o nível diferente de 1.

Dentro deste array, também fazem parte os campos: **c6\_prunit, c6\_prcven, c6\_produto e c6\_item.**

**Solução**

Para solucionar:

1- Acessar o modulo**SIGACFG - Configurador→ Base de Dados → Dicionário → Base de Dados;**

2 - Pesquisar a tabela **SC6** e buscar pelo campo **c6\_descont**;

3 - Alterar o campo ,selecionar a ABA **USO**, deixar o campo como  **USADO** e  o nível de campo igual **1**.

4 - Salvar o campo, salvar a tabela e atualizar o dicionário de dados.

5 - Reinicie o smartclient e efetue o procedimento novamente.

***Obs:  caso ajustando o c6\_descont, o problema permaneça, valide os demais campos que pertencem ao array (c6\_prunit, c6\_prcven, c6\_produto e c6\_item) , ajustando conforme as orientações acima.***
