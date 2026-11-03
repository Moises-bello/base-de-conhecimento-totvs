---
article_id: 360028833991
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: be6fde23cb505f445ed21bfe2e45dc1623c28be4d43e7ac4545df42d7b84108f
fetched_at: '2026-06-28T22:38:45.134231+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross SegmentosTOTVS- Backoffice (Linha Protheus)-SIGAFAT- A prefeitura informa
  que o numero da nota fiscal de serviço precisa de 15 posições e o Protheus só oferece
  a possibilidade ate 9, como alterar
type: support-article
updated_at: '2021-08-18T13:15:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028833991-Cross-SegmentosTOTVS-Backoffice-Linha-Protheus-SIGAFAT-A-prefeitura-informa-que-o-numero-da-nota-fiscal-de-servi%C3%A7o-precisa-de-15-posi%C3%A7%C3%B5es-e-o-Protheus-s%C3%B3-oferece-a-possibilidade-ate-9-como-alterar
---

**Ocorrência**

A prefeitura informa que o numero da nota fiscal de serviço precisa de 15 posições e o Protheus só oferece a possibilidade ate 9, como alterar?  
  
**Ambiente**

Cross SegmentosTOTVS- Backoffice (Linha Protheus)-SIGAFAT- Todas as versões.  
  
**Solução**

A transmissão de nota fiscal de serviço, devera ser adequado todos os campo. **NFELETR**do Protheus para tamanho '15'  
**SF1-> F1\_NFELETR****SF2-> F2\_NFELETR****SF3-> F3\_NFELETR****SFT-> FT\_NFELETR****SE1-> E1\_NFELETR**​  
  
Foi criado um novo grupo de campos específico para o número da nota fiscal eletrônica gerado pela prefeitura **GRUPO 124 COM TAMANHO DE 20**.

![](https://totvssuporte.zendesk.com/attachments/token/byZnPOdWmWS0e05GNeedroV08/?name=inline-123658301.png)

Verifique se os campos mencionados acima participam do grupo e estão com tamanho 20 para atender a solicitação.

Saiba mais sobre nota de serviço:

**[MP-FAT-Excluir-Nota-de-Serviço-após-prazo-do-município](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000617328-MP-FAT-Excluir-Nota-de-Servi%C3%A7o-ap%C3%B3s-prazo-do-munic%C3%ADpio)**

**[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Validação de exclusão do Documento de Saída com uso do JOB FATJOBNFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004391207-MP-FAT-FATJOBNFE-Job-para-validar-o-cancelamento-da-NFE-e-NFS-junto-ao-SEFAZ)**

**[MP - FAT - Configuração básica de nota de serviço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063295573-MP-FAT-Configura%C3%A7%C3%A3o-b%C3%A1sica-de-nota-fiscal-de-servi%C3%A7o)**
