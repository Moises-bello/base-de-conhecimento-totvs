---
article_id: 360016297411
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 833880fda225436a4f6d4fd0299fc2c0489063c63a617857de0fce81cd5fd34c
fetched_at: '2026-06-28T22:42:06.542102+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  como Gerar os Registros M205 e M605 do Sped Contribuições
type: support-article
updated_at: '2024-05-02T20:21:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016297411-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-como-Gerar-os-Registros-M205-e-M605-do-Sped-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar os registros M205 e M605 do Sped Contribuições?  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Para gerar os registros M205 e M605 do Sped Contribuições, realize primeiramente a **Apuração da EFD Contribuições** por meio da rotina **FISA001**.

2. Após a apuração, tendo saldo a recolher, preencha os campos **Código da Receita** e **Data de vencimento** na aba Apuração, conforme abaixo:

![Capturar KCSSSSS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/23219251191831)

Para o **preenchimento automático** do Código da Receita, é possível, informar o código da receita no parâmetro **MV\_CDRCEC**.

**Saiba mais:**  
Orientações para o correto preenchimento do parâmetro: [Código\_Receita\_M205\_M605: parâmetro](http://tdn.totvs.com/pages/viewpage.action?pageId=238029762)
