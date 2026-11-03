---
article_id: 360051317913
category: RH - FGTS / SEFIP
content_hash: c4ccc4566880d01d4573e24b7d942595f3e026fd511ba5e9f47d0dde7d929c24
fetched_at: '2026-06-28T22:43:41.214510+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o mnemônico P_LINSSOUT para geração
  de SEFIP para múltiplos vínculos
type: support-article
updated_at: '2025-08-07T13:20:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051317913-RH-Linha-Protheus-GPE-Como-parametrizar-o-mnem%C3%B4nico-P-LINSSOUT-para-gera%C3%A7%C3%A3o-de-SEFIP-para-m%C3%BAltiplos-v%C3%ADnculos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26998146221463) Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Como parametrizar o mnemônico P\_LINSSOUT para geração de SEFIP para múltiplos vínculos onde o funcionário não tem ocorrência de múltiplo vinculo no cadastro de Funcionários (campo Ocorrência - RA\_OCORREN)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Efetuada melhoria no processo para possibilitar o envio de ocorrência de Múltiplo Vínculo para a Sefip, alterando a ocorrência na SEFIP se a verba de ID **0288-INSS Outras Empresas** for lançada para o funcionário.  
  
Para a melhoria, foi criado o mnemônico **P\_LINSSOUT**, que após ativado possibilitará o envio de múltiplo vinculo, alterando a ocorrência desde que exista verba de ID 0288-INSS Outras Empresas para o funcionário no mês.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26998161896855)  
  
**Importante**O mnemônico vem desativado por padrão, com conteúdo **GetValType("L")**, como todo mnemônico lógico (o retorno desta função é .F.), para que a melhoria surta efeito o mnemônico deverá ser alterado, para **.T.**. Para alterar o mnemônico acesse **Atualizações > Definições de cálculos > Mnemônicos (GPEA300)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26998161898647)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26998146228631)  
  
**Saiba mais:**

[RH - Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011913513-RH-Defini%C3%A7%C3%B5es-de-C%C3%A1lculo)

[RH - FGTS /SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
