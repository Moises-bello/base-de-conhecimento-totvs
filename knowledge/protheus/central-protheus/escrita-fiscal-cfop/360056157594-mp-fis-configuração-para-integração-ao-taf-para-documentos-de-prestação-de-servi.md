---
article_id: 360056157594
category: Escrita Fiscal - CFOP
content_hash: 54fef5d31915cf99b68a109f12ec330dd420aeb0cfb3ba54a60fe8623df0a8d0
fetched_at: '2026-06-28T22:39:35.950312+00:00'
product: protheus
section_id: 1500001538541
source: central-protheus
title: MP - FIS - Configuração  para integração ao TAF para documentos de prestação
  de serviços (RPS) conforme número da N.F. Eletrônica de Prestação de Serviços (FT_NFELETR)
  de retorno da prefeitura.
type: support-article
updated_at: '2021-04-28T15:09:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056157594-MP-FIS-Configura%C3%A7%C3%A3o-para-integra%C3%A7%C3%A3o-ao-TAF-para-documentos-de-presta%C3%A7%C3%A3o-de-servi%C3%A7os-RPS-conforme-n%C3%BAmero-da-N-F-Eletr%C3%B4nica-de-Presta%C3%A7%C3%A3o-de-Servi%C3%A7os-FT-NFELETR-de-retorno-da-prefeitura
---

**Dúvida**Qual a configuração para integração ao TAF para documentos de prestação de serviços (RPS) conforme número da N.F. Eletrônica de Prestação de Serviços (FT\_NFELETR) de retorno da prefeitura.  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**

Para efetuar integração TAF dos documentos de prestação de serviços somente se número da Nota Fiscal Eletrônica de Prestação de Serviços (FT\_NFELETR) retornado pela prefeitura.

Para implementar esta funcionalidade é necessário a criação/alteração do parâmetro MV\_ESPNFEL para informar as espécies consideradas nesta verificação conforme necessidade cenário específico.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097586893/mceclip0.png)

Informações Adicionais :

<https://tdn.totvs.com/display/public/PROT/FIS0001_Extrator_Fiscal_x_TAF>
