---
article_id: 10790990612375
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: 6d226e2a931456bf12b3e73556fd5b198ba4ec96dc569174775f2c4c1b7be26f
fetched_at: '2026-06-28T22:39:48.880373+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Como gerar uma
  única adição para produtos que possuem a mesma NCM e NVE?
type: support-article
updated_at: '2022-12-14T20:15:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10790990612375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-gerar-uma-%C3%BAnica-adi%C3%A7%C3%A3o-para-produtos-que-possuem-a-mesma-NCM-e-NVE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:05:00 min** **Dúvida**Como gerar uma única adição para produtos que possuem a mesma NCM e NVE?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Não é possível, pois a NVE é critério de quebra de adições, desta forma o sistema irá considerar esta diferença de informação para realização da quebra da adição.

Por não  ter o tratamento por NCM  orientamos  que não seja carregada a NVE do cadastro de produto ao incluir o desembaraço quando apresentada a mensagem pelo sistema, deve ser criada manualmente (por NCM) na fase de Desembaraço, associando os itens que forem sugeridos e que fazem sentido para a operação à NVE criada.

**Exemplo:**

1- No Easy Import Control (SIGAEIC) acesse Atualizações/Desembaraço/Manutenção. (EICDI502), clique em incluir

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10959376850711)

2 - Preencha os dados da capa do Desembaraço e Pedido Base e clique em Salvar.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10959477213847)

3 - Em Outras Ações, marque os itens e selecione salvar.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10959591763095)

4 Selecione Outras Ações Invoices.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10959635104023)

5 - Em Outras Ações - Incluir, informe os dados da capa e clique em Salvar.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10959678500631)

6 - Caso o produto possua NVE vinculada, o sistema informa mensagem questionando se o usuário deseja importar os dados. Clique em Não.

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10959737258391)

7 - Em Outra Ações, selecione Marca/Desmarca todos e clique em salvar.  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10959776330135)

8 - Em Outra Ações, clique em   N.V.E.

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10959823596567)

9 - Em Relações do N.V.E selecione incluir

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10959901061527)

10 - Informe o numero da NCM que possui NVE e salvar.

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10959962695191)

11 - Em manutenção de **NVE's**, preencha o campos  **EIM\_ATRIB Atributo** , **EIM\_ESPEC** Espec. Atri e Tab. N.V.E e selecione salvar  e confirme a inclusão

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10960006977175)

12 - Posicione sobre o processo, selecione alterar

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10960130715415)

13 - Selecione  Outras Ações - Adições

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10960134397079)

14 - Em Adições - Outras Ações - Gerar

![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10960211223319)

Vale a pena reforçar, que com o surgimento da DUIMP, este cadastro da NVE deverá cair em desuso, uma vez que para a DUIMP  teremos o catálogo de produtos.

**Saiba Mais**[Tratamento de NVE (Nomenclatura de Valor Aduaneiro e Estatística) por Produto](https://tdn.totvs.com/pages/releaseview.action?pageId=368905706)
