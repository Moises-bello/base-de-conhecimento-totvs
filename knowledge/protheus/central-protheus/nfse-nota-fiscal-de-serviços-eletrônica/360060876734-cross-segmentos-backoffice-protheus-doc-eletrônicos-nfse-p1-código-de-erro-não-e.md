---
article_id: 360060876734
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 01f49e729198e2e01bd7282dbc03be6b59d23d7de16c7f57090e707f0020e37c
fetched_at: '2026-06-28T22:39:57.616085+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - P1 - Código
  de erro não encontrado - E163 (Salvador)
type: support-article
updated_at: '2025-06-25T21:12:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060876734-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-P1-C%C3%B3digo-de-erro-n%C3%A3o-encontrado-E163-Salvador
---

**Ocorrência**Ao realizar a transmissão de um RPS para Salvador ocorre a rejeição: *"**P1 - Código de erro não encontrado - E163**".*  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002214602/mceclip0.png)  
 **Ambiente**Cross Segmentos - TOTVS Backoffice Protheus - TOTVS Doc. Eletrônicos - Todas as versões.  
  
**Causa**Essa rejeição apesar de não ser tão clara pela mensagem em si, ocorre por conta da falta da informação dos novos códigos CTISS (Código de Tributação) da prefeitura na tag <CodigoTributacaoMunicipio >, a qual passou a ser uma nova validação.  
  
**Solução**Para corrigir essa rejeição, **deverá informar um CTISS no campo B1\_TRIBMUN** no Cadastro de Produto ou **BZ\_TRIBMUN** caso utilize [Indicador de Produtos.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026420011-MP-NFSE-Indicador-de-Produto?source=search)  
  
*Obs.: O **código informado no campo deverá conter somente números**, sem nenhum tipo de mascara (mesmo que na relação elas estejam presentes), exemplo: **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101423174/mceclip0.png)***  
  
A relação dos códigos CSTISS precisa também estar alinhada com Código de Serviço e Alíquota. Detalhes da lista abaixo:  
- [MP - NFSE - Código de Tributação / CTISS de Salvador - BA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060204994-MP-NFSE-C%C3%B3digo-de-Tributa%C3%A7%C3%A3o-CTISS-de-Salvador-BA?source=search)  
  
*Obs.: Vale lembrar que essa lista citada na documentação é a última que o suporte teve acesso, qualquer alteração ou falta de informação deverá ser solicitado diretamente para a prefeitura.*
