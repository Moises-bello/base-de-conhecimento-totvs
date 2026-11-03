---
article_id: 4409020102679
category: eSocial - Parametrizador
content_hash: fca102dc1ffd8d1bc2fbea50eded0844256656297ffa9ad2e0d42dae747ff806
fetched_at: '2026-06-28T22:47:06.321949+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: RH - RM - FOP - eSocial - Mapeamento dos eventos eSocial
type: support-article
updated_at: '2026-04-08T18:42:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409020102679-RH-RM-FOP-eSocial-Mapeamento-dos-eventos-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39608697574423) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
De onde o sistema busca as devidas informações para geração dos eventos eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Para geração dos eventos eSocial, o sistema irá verificar informações previamente cadastradas e considerar regras constantes no leiaute eSocial para correta geração de cada tag presente no XML.

Considerando o evento **S-1010 - Tabela de Rubricas**, por exemplo, o leiaute indica que a *tag* **tpProc** do grupo **ideProcessoCP** poderá ser preenchida com os valores 1 ou 2. O sistema irá verificar então se na tabela **PEVENTO**, o campo **TPPROCESSOINSS** está preenchido como **A - Administrativo** ou **J - Judicial**, retornando então na *tag* o valor **1** ou **2**, respectivamente.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409017895703)

Para facilitar o entendimento e identificação da origem da informação, foi criado o mapeamento dos eventos eSocial, disponível na página abaixo:

* [Mapeamento dos Eventos](https://tdn.totvs.com/display/public/LRM/Mapeamento+dos+Eventos)

O mapeamento apresentará nas colunas **Tabela RM** e **Coluna RM** a tabela e campo de origem do dado ou na coluna **Informações do cálculo** a regra utilizada para preenchimento da informação.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409017985303)

**Importante**  
Ao selecionar o evento desejado, selecione o leiaute utilizado para correta apresentação das regras utilizadas.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409020030487)
