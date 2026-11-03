---
article_id: 17625424306711
category: TAF - REINF
content_hash: 0d5b9a27b7de5e90a1dbf416c0d0a975a47331ba6085c1f8d16cd8a4b5a86133
fetched_at: '2026-06-28T22:41:33.768981+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como preencher o tipo
  de serviço para as notas que geram a Reinf?
type: support-article
updated_at: '2023-09-18T18:40:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17625424306711-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-preencher-o-tipo-de-servi%C3%A7o-para-as-notas-que-geram-a-Reinf
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17625392788759) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como gerar corretamente os dados do tipo de serviço, campo necessário para os eventos R-2010 e R-2020 da Reinf?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - Todas as versões  
  
**Solução**

O Tipo de Serviço é um código necessário para a transmissão dos eventos da Reinf de notas fiscais que possuem **retenção de INSS**, como o**R-2010 ou R-2020**.

Essa informação **não é obrigatória** para o **bloco 40**, a não ser que a nota possua **retenção de INSS** que deve ser gerado no **bloco 20.**

Hoje há duas formas de trazer o tipo de serviço vinculado a nota: pela rotina MATA963 - Relacionamento Código de serviço e pela rotina FISA180 - Complemento Fiscal do Produto. Segue abaixo em qual situação é usado cada rotina:

**NFS:** notas fiscais de serviço que possuem código de serviço e retenção de INSS devem ser vinculadas a um tipo de serviço pela rotina MATA963, onde o código inserido no campo **CDN\_TPSERV** é validado para a Reinf.

Mais informações e como efetuar o cadastro: <https://tdn.totvs.com.br/pages/releaseview.action?pageId=346488949>

**Outros Documentos:** Notas em que há tributação no ICMS e INSS, como por exemplo CTE ou CTE-OS não possuem código de serviço, portanto, não devem ser vinculadas a um tipo de serviço pela MATA963. Esse vínculo deve ser feito utilizando o campo F2Q\_TPSERV, pela rotina FISA180 ou Complemento Fiscal do Produto.

Mais informações e como efetuar o cadastro: <https://tdn.totvs.com.br/pages/releaseview.action?pageId=454832926>

Obs: As informações acima não se aplicam a títulos gerados diretamente no Financeiro, somente a documentos fiscais.

Caso ocorrer alguma dúvida na escrituração desses documentos, acionar o time de Escrita Fiscal.
