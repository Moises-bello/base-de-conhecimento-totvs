---
article_id: 360020345532
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: ac21f4f75c7fbd912716cd37f89d607750327941becd65adb57cec325a1f131e
fetched_at: '2026-06-28T22:42:02.414919+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Registro C120: Complemento de Documento - Operações de Importação (Codigos 01
  e 55)'
type: support-article
updated_at: '2026-01-23T14:25:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020345532-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registro-C120-Complemento-de-Documento-Opera%C3%A7%C3%B5es-de-Importa%C3%A7%C3%A3o-Codigos-01-e-55
---

**Dúvida**  
Como gerar o registro C120: Complemento de Documento - Operações de Importação (Codigos 01 e 55)?  
  
**Ambiente**  
Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Realize lançamento de nota fiscal de entrada com fornecedor EX – “Estrangeiro”.  
Para mais orientações sobre o lançamento de nota de importação, acesse: [DOC0010\_Nota\_ Fiscal\_ de\_ Importação](http://tdn.totvs.com/pages/releaseview.action?pageId=6076840)  
  
2. Após o lançamento de nota fiscal de Importação realize o complemento de importação para geração do registro C120:

![image-2025-11-6_12-15-34.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37883500527383)

**Atenção!** Para geração do registro C120 deve ser gerado registro Pai C110 - Informações complementares.

**Importante:**  
**Complemento de Nota Fiscal Automático**

Utilizado para alterações automáticas nos complementos dos documentos fiscais após a emissão das Notas Fiscais.

Para informações sobre o Ponto de entrada MATUCOMP, acesse: [MATUCOMP - Alterações automáticas](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)

O parâmetro MV\_ATUCOMP deve ser configurado para que seja possível utilizar o Ponto de Entrada MATUCOMP,  MV\_ATUCOMP = T
