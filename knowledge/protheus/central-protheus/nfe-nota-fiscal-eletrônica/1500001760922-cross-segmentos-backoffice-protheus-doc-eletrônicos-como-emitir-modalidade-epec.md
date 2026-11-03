---
article_id: 1500001760922
category: NFe - Nota Fiscal Eletrônica
content_hash: 941f31708d27f6ffe74562631d4967f8e379856cddeed00b253ee3ee1909893d
fetched_at: '2026-06-28T22:40:05.686711+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como emitir modalidade
  EPEC
type: support-article
updated_at: '2025-07-09T12:30:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001760922-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-emitir-modalidade-EPEC
---

**Dúvida**Como emitir nota em modalidade EPEC?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A transmissão deve ser efetuada nesta modalidade somente se for orientação da própria SEFAZ.

**Importante não realizar esse tipo de transmissão quando outra modalidade de contingência estiver ativa.**

Sempre consulte a disponibilidade antes no portal da Sefaz.

Conforme informado pela SEFAZ a contingência que deve ser utilizada quando há problemas de comunicação é a SVC, verifique a contingência correta para seu estado conforme orientação da SEFAZ: <http://www.nfe.fazenda.gov.br/portal/webServices.aspx?tipoConteudo=Wak0FwB7dKs=>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001589342)

Acesse a rotina NFESEFAZ>outras ações>parâmetros>NFE> selecione a opção 5 DPEC/EPEC.

Seguir com processo normal de transmissão

![epc.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102652913)

A SEFAZ irá efetuar o registro do evento na NFE, após a SEFAZ autorizar a transmissão na modalidade normal, o cliente deverá efetuar a retransmissão da nota na modalidade EPEC para registrar a conciliação

Link de conciliação: <https://www.nfe.fazenda.gov.br/portal/consultaEPECConciliacao.aspx?tipoConteudo=QTlVUO4tycw=>

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001589362)

Ao monitorar a nota a mesma ira retornar o seguinte registro:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102653613)

Consulte a chave da nota no portal nacional da Sefaz conforme o link abaixo:

<http://www.nfe.fazenda.gov.br/portal/consultaRecaptcha.aspx?tipoConsulta=resumo&tipoConteudo=d09fwabTnLk=>

Quando o evento for autorizado ele vai retornar com o seguinte registro .

![b.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102652893)

Porém o vínculo do EPEC com a nota só será autorizado quando a disponibilidade da Sefaz retornar, para vincular o evento da NFE basta entrar no sistema em data retroativa e retransmitir a nota na mesma modalidade em EPEC. Esse processo de transmissão deve ser realizado 2 vezes.

A **DPEC** tem a particularidade é necessário alterar o parâmetro de transmissão além da modalidade para DPEC alterar a versão DPEC para 1.01

* ***Importante:***

**Lembrete a modalidade de contingência*****5- Contingência DPEC/ EPEC*****,** deve ser utilizada apenas caso seja orientado pela Sefaz, pois ao utilizar está opção indevidamente o **Evento fica registrado, mas não Vinculado, ou seja a nota não é autorizada.**

* **Importante:**

Para verificar melhor essas informações verifique o arquivo NotasEletronicas abaixo.

Baixar o arquivo [**NOTASELETRONICAS\_HELP.rar**](http://tdn.totvs.com/pages/viewpageattachments.action?pageId=47908989&highlight=NOTASELETRONICAS_Help.rar#Documentos+Eletr%C3%B4nicos-attachment-NOTASELETRONICAS_Help.rar)

Verificar a opção **contingência.**

Importante que seu TSS esteja atualizado conforme abaixo:  
[TSS - Atualizações do TSS - Totvs Spd Service](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)
