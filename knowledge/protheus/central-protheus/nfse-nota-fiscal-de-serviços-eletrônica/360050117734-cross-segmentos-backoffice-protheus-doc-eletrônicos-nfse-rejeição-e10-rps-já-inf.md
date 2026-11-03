---
article_id: 360050117734
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: e02cdcf498e4c57aef455091cc8a28bc25229f31166269cefa005a1966f8a6f0
fetched_at: '2026-06-28T22:39:58.450438+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - Rejeição
  E10: RPS já informado'
type: support-article
updated_at: '2023-05-16T12:16:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050117734-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Rejei%C3%A7%C3%A3o-E10-RPS-j%C3%A1-informado
---

**Dúvida**Como corrigir a rejeição abaixo, para nfse?  
E10 - RPS já informado.

**Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Solução**  
Ao transmitir um RPS para prefeitura e realizar o monitoramento é apresentado a rejeição **E10 - RPS já informado**, porém essa nota está autorizada na prefeitura.

Essa rejeição, geralmente, ocorre quando houve uma retransmissão do RPS de mesmo número e série.  
Por exemplo: O TSS faz a transmissão de uma nota fiscal X no lote 01, mesmo que ainda não tenha recebido a autorização desta primeira transmissão, o usuário faz uma retransmissão da nota gerando o lote 02. Então, na prefeitura como já registrou o recebimento da nota fiscal no lote 01, é retornada a rejeição de que esse RPS já existe em sua base de dados.

Para os municípios que possuem a funcionalidade de **Consulta RPS**, se a rotina **FISA022** estiver atualizada, basta realizar o procedimento abaixo:  
-Acesse Rotina **FISA022** e posicione o cursor sobre o RPS rejeitado;  
-Clique em **Outras Ações** >**Consulta RPS**;  
-Será apresentado o status atual dessa nota junto a prefeitura e os dados no TSS serão atualizados;  
-Em seguida realize o Monitor deste documento, para que o retorno de autorização seja atualizado nas tabelas do Protheus.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360076306054/mceclip0.png)

Nem todas as prefeituras possuem esta funcionalidade, consulte no link abaixo, os municípios que possuem a **Consulta RPS**.

[TSS0009\_Relação\_de\_Municípios\_Homologados\_para\_Emissão\_de\_NFS-e](http://tdn.totvs.com/pages/viewpage.action?pageId=4814340) 

\*Se este incidente ocorrer para um município que não possui Consulta RPS, será necessária a abertura de um ticket junto ao suporte do TSS, solicitando orientação para correção.
