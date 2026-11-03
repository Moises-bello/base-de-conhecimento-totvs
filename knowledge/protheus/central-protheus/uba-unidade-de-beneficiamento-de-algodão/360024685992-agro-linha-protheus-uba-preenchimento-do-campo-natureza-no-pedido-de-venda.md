---
article_id: 360024685992
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 9ba4f94e99a088bcbc3a76c518c3a721bbfe6cdc08253b3587c533c7ffe81ecc
fetched_at: '2026-06-28T22:45:35.651216+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - UBA - Preenchimento do campo natureza no pedido de
  venda
type: support-article
updated_at: '2025-06-20T19:08:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024685992-Agro-Linha-Protheus-UBA-Preenchimento-do-campo-natureza-no-pedido-de-venda
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22095548168727)** Tempo aproximado para leitura: **00:00:45 min****Dúvida**Como é possível que a informação referente ao campo **Natureza** seja inserida na rotina **AGRA750****- Romaneio de Saída** antes da geração do pedido de venda?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - Versão 12  
  
**Solução**O campo **Natureza** não existe na rotina**AGRA750**, mas há o ponto de entrada **AGR750PV** **- Alterar dados do Pedido de Vendas** que pode ser utilizado para manipular os dados que serão gerados na emissão do Pedido de Venda.  
  
**Importante**O parâmetro **MV\_1DUPNAT** - **Campo ou dado a ser gravado na natureza do título quando o mesmo for gerado automaticamente pelo modulo de faturamento** necessita estar configurado corretamente, para que seja definida a **Natureza Financeira** que será utilizada na venda.  
**Saiba mais**Mais informações sobre a utilização do parâmetro **MV\_1DUPNAT** podem ser analisadas na documentação abaixo:[Parâmetro MV\_1DUPNAT](http://tdn.totvs.com/display/PROT/FAT0038_A410NATVZO_A410NATUSO_A410NATCLI_A410NATPED_Cadastro_Natureza_MV_1DUPNAT)
