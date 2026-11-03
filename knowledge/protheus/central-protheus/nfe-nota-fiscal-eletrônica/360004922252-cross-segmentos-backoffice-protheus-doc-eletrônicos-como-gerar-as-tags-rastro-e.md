---
article_id: 360004922252
category: NFe - Nota Fiscal Eletrônica
content_hash: 23eb77a91670ef0941f73a8013d32551b0bb17b6364ff9764c76cd9505b3d4ff
fetched_at: '2026-06-28T22:39:59.902470+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar as
  TAGs rastro e med  (Detalhamento Específico de Medicamento e de matérias-primas
  farmacêuticas) '
type: support-article
updated_at: '2021-07-23T17:27:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004922252--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-as-TAGs-rastro-e-med-Detalhamento-Espec%C3%ADfico-de-Medicamento-e-de-mat%C3%A9rias-primas-farmac%C3%AAuticas
---

**Dúvida**Como gerar o Grupo de TAGs de Rastro e Med (tabela F0A e CD7) ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Importante:**

* Foi criado na tabela **CD7 um novo campo CD7\_MOTISE**  referente a nova **NT2018.005**:

Lembrando que a TAG xMotivoIsencao **não** é obrigatória.

O preenchimento desse campo é apenas Manual.

**O pacote de Dicionário que cria o NOVO campo na CD7  está disponível.**

* **Baixar o pacote através do link abaixo:**

[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/765125)

**Para mais detalhes acessar o link:**

[4549901 DSERFIS1-10903 DT Apuração para Ressarcimento, Restituição e Complemento do ICMS e a geração do arquivo DRCST - SC](http://tdn.totvs.com/pages/releaseview.action?pageId=484700869)

Dentro deste pacote acima, há o pacote que deve ser colocado dentro da pasta **Systemload** para atualização do campo.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026893931/mceclip1.png)**

* Há duas formas de gerar as TAGS no XML Manual e Automático:

1- Preencha os campos no módulo dos **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos.**

![20201117_103818.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360098145494/20201117_103818.gif)

* **Na opção Medicamento**

**![](https://totvssuporte.zendesk.com/attachments/token/8MVUCE0kZ3UXw4l24Wsw5AAWi/?name=inline-1151364664.png)​**

2**-** Para habilitar a rotina acima,**Configurar** o parâmetro no configurador conforme os **exemplos abaixo:**

* Configurar o parâmetro no configurador **MV\_MEDICA = (Com o código do grupo de produto)**

3- **Informe no campo B1\_GRUPO** no Cadastro de produto o conteúdo informado **no parâmetro acima.**

![B1_GRUPO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100403113/B1_GRUPO.png)

**IMPORTANTE:**

* **Para o preenchimento automático** dos dois campos abaixo:

* **CD7\_PRECO**
* **CD7\_CODANV**  
  **Configurar conforme os Boletins Técnicos:**
* [2539564 DSERTSS1-8413 DT NFe 4.0 TAG Medicamentos](http://tdn.totvs.com/display/TSS/2539564+DSERTSS1-8413+DT+NFe+4.0+TAG+Medicamentos)
* [DMANMAT01-10271 DT\_FISA180 - Complemento Fiscal do Produto em modelo MVC](http://tdn.totvs.com/display/PROT/DMANMAT01-10271+DT_FISA180+-+Complemento+Fiscal+do+Produto+em+modelo+MVC)
* [PEST018 - MV\_CADPROD - Parâmetro para informar quais cadastros complementares devem ser apresentados no cadastro de produto](http://tdn.totvs.com/pages/viewpage.action?pageId=317003310)

* **Saiba mais:**

Conforme o fonte do NFESEFAZ abaixo, os campos que devem estar preenchidos na tabela CD7:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404848145303/mceclip0.png)

Além disso, para gerar apenas o grupo de Rastro **sem Med** verificar o artigo abaixo:

[MP - NFE - NT4.00 TAG rastro tabela F0A](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004942192)

* **Para controlar lote no produto segue abaixo o link da FAQ:**

<http://tdn.totvs.com/display/public/PROT/PEST10008+-+RASTREABILIDADE+CONTROLE+DE+LOTE>

* **Saiba mais:**

O Lote é gerado apenas no XML.

Até o momento, não existe um layout da Sefaz para que seja apresentada a informação do Lote, ou seja, não foi criado um novo campo no Danfe, e não há nenhuma informação na nota técnica sobre a obrigatoriedade de mensagem.

Caso seja uma solicitação da Sefaz do seu estado, poderá utilizar um campo padrão para gerar a mensagem em informações complementares, como exemplo **C5\_MENNOTA e F4\_FORMULA.**

**Baixe o vídeo para verificar o preenchimento desde o configurador da forma Manual e automático:**
