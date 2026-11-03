---
article_id: 360061112854
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 42e12ec9e9a82de3bf06493b9b40433c58af3f5408a635221007be9a241e6e43
fetched_at: '2026-06-28T22:37:22.692401+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - É possivel gerar mais
  de um Pedido ou Título em uma mesma Medição de Contrato ?
type: support-article
updated_at: '2026-05-08T14:39:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061112854-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-%C3%89-possivel-gerar-mais-de-um-Pedido-ou-T%C3%ADtulo-em-uma-mesma-Medi%C3%A7%C3%A3o-de-Contrato
---

**Dúvida**  
É possível gerar mais de um Pedido ou Título em uma mesma Medição de Contrato ?

**Ambiente**  
Protheus – Gestão de Contratos – A partir da versão 12.1.25  
  
**Solução**  
As possibilidades existentes para geração de mais de um Pedido ou Título em uma mesma Medição de Contrato podemos dizer que são as seguintes:

**1ª -** Possuir mais de uma planilha no Contrato e dessa forma, ao realizar uma medição neste contrato para mais de uma planilha ao mesmo tempo, serão gerados um documento (Pedido ou Titulo) para a mesma mediação, sendo um documento para cada planilha.

**2ª -** Caso na Medição de uma Planilha que possua mais de um item, pode ser utilizado o campo **CNE\_IDPED (Agrup. Doc)** nos itens da planilha

Abaixo mais detalhes:

O campo "Agrupador de Documentos" tem a funcionalidade de, quando em uma medição cuja planilha a ser medida possui mais de um item, caso no campo sejam incluídas um número de agrupador diferente para cada item, serão gerados Documentos diferentes ou separados para cada número de agrupador inserido.  
  
Por exemplo, numa medição que contém 5 itens, e nos três primeiros itens o campo **Agrup. Doc (CNE\_IDPED)** é preenchido com "1", nos dois seguintes é preenchido com "2" e no quinto item é preenchido com "3", ao realizar o encerramento desta Medição, serão gerados 3 documentos (Pedidos ou Titulo Financeiro) um para cada Agrupador inserido e não somente um Documento (como seria se este campo não houvesse sido preenchido).  
  
Obs.:  
Caso o campo não seja preenchido em um item da medição e seja preenchido e outro item, o sistema entende que possui informações diferente e também gera documentos diferentes no encerramento da Medição.  
  
Abaixo Imagem de exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103461293)

Neste exemplo de utilização do campo, em uma medição que possui 7 itens, serão gerados 3 documentos, um para conjunto de itens de mesmo Agrupador informado no campo.  
  
***Importante:***  
Essa é uma funcionalidade para "desagrupar" itens dentro de uma mesma planilha caso sejam inseridas informações diferentes no campo **Agrup. Doc (CNE\_IDPED)**,  
Caso o contrato possua mais de uma planilha, e seja feita medição dessas ao mesmo tempo, será sempre gerado Documentos diferentes, não havendo uma funcionalidade padrão para agrupar os itens em um mesmo documento nesta situação de Medição em Planilhas diferentes.

***Saiba Mais:***

* [Nova Medição - CNTA121 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=353284981)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
