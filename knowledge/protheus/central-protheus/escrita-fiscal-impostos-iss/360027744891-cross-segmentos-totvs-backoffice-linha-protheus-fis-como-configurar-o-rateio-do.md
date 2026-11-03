---
article_id: 360027744891
category: Escrita Fiscal - Impostos - ISS
content_hash: 6b115d5cf56d2bab41e787c5220a809d43b1bfd11d46269293e3a9cf29ff9d88
fetched_at: '2026-06-28T22:39:35.277093+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o
  rateio do ISS no documento de entrada
type: support-article
updated_at: '2021-06-10T13:11:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027744891-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-rateio-do-ISS-no-documento-de-entrada
---

**Dúvida**

Como definir se o ISS - Imposto Sobre Serviços - será rateado ou não pelo número de títulos a pagar de uma nota fiscal de entrada?  
  
**Ambiente**

Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Por meio da configuração do parâmetro **MV\_RATISS** é possível definir se o ISS será rateado ou não. As configurações possíveis do parâmetro são:  
T - Rateia  
F - Não rateia

1 - Acesse o Configurador >Ambientes -> Cadastros -> Parâmetros   
2 - Localize o parâmetro MV\_RATISS  
3 - Clique em alterar e informe o conteúdo desejado, conforme a regra de negócio da empresa.
