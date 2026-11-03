---
article_id: 360060238633
category: NFe - Nota Fiscal Eletrônica
content_hash: b372069c19aa3c4f28c6677eff61648ed63483d842eefbeedf38c93dbd4beb32
fetched_at: '2026-06-28T22:40:00.425817+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029- Falha de
  Schema referente a TAG vBC no grupo do II'
type: support-article
updated_at: '2021-10-11T15:05:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060238633--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-Schema-referente-a-TAG-vBC-no-grupo-do-II
---

**Dúvida**

Como corrigir a falha de Schema abaixo ?

029- Falha de Schema referente a TAG vBC no grupo do II  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Conforme o ***Manual do Contribuinte\_v\_6.00 página 211:***

[Manual de Orientação do Contribuinte - versão 6.00](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=URCYvjVMIzI=)

![TAG_do_valor_do_II.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360098836474/TAG_do_valor_do_II.JPG)

* Conforme o XML de exemplo abaixo, deve gerar conteúdo ***na TAG vBC e este valor, não pode ser negativo.***

![II_XML.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360101050493/II_XML.JPG)

**1-** Quando**não usa integração**com o***módulo SIGAEIC é necessário que o parâmetro MV\_EASY= N***

**![20201201_145829.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101050713/20201201_145829.gif)**

**2-**Acesse a rotina ***Livros Fiscais-> Atualizações->Movimentos->NF manual de Saída->Outras ações->Complementos->Importação:***

***![20201201_145142.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360101050853/20201201_145142.gif)***

3- ***Preencha ou corrija*** o campo CD5\_BCIMP ***Vlr. BC Importação:***

![CD5_II.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360101051353/CD5_II.JPG)

4- Após isso, ***exclua a nota e gere novamente.***
