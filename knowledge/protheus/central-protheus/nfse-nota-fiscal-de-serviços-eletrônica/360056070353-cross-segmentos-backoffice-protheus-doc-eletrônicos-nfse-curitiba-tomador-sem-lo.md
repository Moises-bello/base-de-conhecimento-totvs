---
article_id: 360056070353
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: ea03a370540e3c17b18f939c8cc2cb44e41988f6a3c4ff165f4b3dd1d3d94d75
fetched_at: '2026-06-28T22:39:56.414360+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - CURITIBA:
  Tomador sem logradouro no TSS'
type: support-article
updated_at: '2025-07-14T21:05:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056070353-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-CURITIBA-Tomador-sem-logradouro-no-TSS
---

**Dúvida**Como emitir uma nota de serviços para a prefeitura de Curitiba sem os dados de endereço do tomador?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**Caso não deseje enviar os dados do endereço do tomador no layout da prefeitura, os campos relacionados ao logradouro do tomador devem conter a seguinte expressão "SEM ENDERECO".  
Com exceção da UF que deve ser preenchida como "XX" e o Número preenchido como "SN".

Veja o exemplo do cadastro do cliente no Protheus:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093870973)

Exemplo XML gerado pelo rdmake NFSEXMLENV:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360093868313)

Exemplo de XML convertido pelo TSS no layout de Curitiba - Sem os dados de endereço:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091706374)  
  
Para essa funcionalidade, é importante estar com o TSS atualizado:  
- [TSS - Atualizações do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)
