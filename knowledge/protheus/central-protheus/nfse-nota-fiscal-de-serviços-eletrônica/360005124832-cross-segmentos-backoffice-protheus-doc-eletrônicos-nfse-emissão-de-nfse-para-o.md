---
article_id: 360005124832
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: 3ca5fc5a2c136b06894000a229e8affb243eda7eb97b50feeff0215afbfbcf3f
fetched_at: '2026-06-28T22:39:57.409995+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Emissão de
  NFSE para o município de Aparecida de Goiânia-GO
type: support-article
updated_at: '2025-05-29T11:50:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005124832-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Emiss%C3%A3o-de-NFSE-para-o-munic%C3%ADpio-de-Aparecida-de-Goi%C3%A2nia-GO
---

**Dúvida**Alteração de layout de Aparecida de Goiania - GO para ISSNetOnline 2.04.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - a partir da release 12.1.2210.   
  
**Solução**

O município de Aparecida de Goiânia-GO (5201405) alterou o layout da nota fiscal de serviços para **2.04.**

 Agora para transmissão das notas utilize o rdmake NFSEXMLENV e a rotina FISA022:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16808651424407)

#### **O QUE DEVE SER ATUALIZADO?**

#### **TSS:** [Pacote pontual do TSS](https://suporte.totvs.com/portal/p/10098/download?e=1116595) **NEWNFSE:** [Passo a passo atualização NewNFSE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16784834285847-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletronicos-NFSe-Configura%C3%A7%C3%A3o-do-NEWNFSE) **PROTHEUS:** Rdmake NFSEXMLENV: [Download aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1083728) Acumulado Protheus Documentos eletronicos: [Download Aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1081419)

**DIFERENÇAS ENTRE VERSÃO 1.00 E 2.04:**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16862365332119)  
  
Abaixo a **documentação**de como poderá ser realizado a **implantação**e suas devidas **funcionalidades:**  
1 - [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSe - IMPLANTAÇÃO DE NFSE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006652632-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-IMPLANTA%C3%87%C3%83O-DE-NFSE?source=search)  
2 - [Cancelamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005593-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-IssNetOnline-Cancelamento-E160-Arquivo-enviado-fora-da-estrutura-)

**CANCELAMENTO**

        Identificação dos códigos de cancelamento:

       1 - Erro na emissão  
       2 - Serviço não prestado  
       3 - Erro de Assinatura (Uso restrito da Administração Tributária Municipal)  
       4 - Duplicidade da Nota  
       5 - Erro de processamento (Uso restrito da Administração Tributária Municipal)

      Dos código acima 1, 2 e 4 podem ser utilizados pelo contribuinte, porém a **prefeitura só esta aceitando cancelamentos com os código 2 e 4 , regra interna da prefeitura**.

Para a rejeição L074 no cancelamento temos a issue **DSERTSS2-13642**, entre em contato com o suporte para orientações:  
L074 - Código do município gerador informado no XML diferente da URL do webservice.
