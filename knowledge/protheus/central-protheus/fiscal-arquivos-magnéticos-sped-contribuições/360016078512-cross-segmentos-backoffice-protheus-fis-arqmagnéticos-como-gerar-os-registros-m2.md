---
article_id: 360016078512
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 4f67375a7d0fcf0b20f1af3334aef23bb00d8360d8b98b0cfa9d1ac5ae817ee6
fetched_at: '2026-06-28T22:42:05.030112+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar os
  registros M205 e M605 do EFD Contribuições
type: support-article
updated_at: '2025-10-28T18:37:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016078512-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-os-registros-M205-e-M605-do-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar os registros M205 e M605 do Sped Contribuições?  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Para gerar os registros M205 e M605 do Sped Contribuições, realize primeiramente a **Apuração da EFD Contribuições** por meio da rotina **FISA001**.

2. Após a apuração, tendo saldo a recolher, preencha os campos **Código da Receita** e **Data de vencimento** na aba Apuração, conforme abaixo:

![captura.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35942323088791)

Para o **preenchimento automático** do Código da Receita, é possível, informar o código da receita no parâmetro **MV\_CDRCEC**. Mais detalhes:  
Orientações para o correto preenchimento do parâmetro: [Código\_Receita\_M205\_M605: parâmetro](http://tdn.totvs.com/pages/viewpage.action?pageId=238029762)  
  
O código da natureza a ser gravada nos títulos da apuração, poderão ser informados nos parâmetros:  
**MV\_PISAPC**- Informe a natureza a ser considerada para o título do **PIS** no **regime cumulativo**. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro **MV\_PISNAT**.  
  
**MV\_PISAPNC**- Informe a natureza a ser considerada para o título do **PIS** no **regime não cumulativo**. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro **MV\_PISNAT**.   
  
**MV\_COFAPC** - Informe a natureza a ser considerada para o título da **COFINS** no **regime cumulativo**. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro **MV\_COFINS**.  
  
**MV\_COFAPNC** - Informe a natureza a ser considerada para o título da **COFINS** no **regime não cumulativo**. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro **MV\_COFINS.**
