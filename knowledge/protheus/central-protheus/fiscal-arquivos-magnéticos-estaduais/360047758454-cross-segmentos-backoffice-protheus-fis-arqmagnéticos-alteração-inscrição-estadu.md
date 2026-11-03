---
article_id: 360047758454
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 971e01d0ab739299d05d29b6d421560372b3a0aa8126a5e2b308d6b6591ddbd1
fetched_at: '2026-06-28T22:42:09.227611+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Alteração Inscrição
  Estadual nas Obrigações Fiscais
type: support-article
updated_at: '2026-04-01T20:09:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047758454-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Altera%C3%A7%C3%A3o-Inscri%C3%A7%C3%A3o-Estadual-nas-Obriga%C3%A7%C3%B5es-Fiscais
---

**Dúvida**  
  
Foi alterada Inscrição Estadual para uma filial, mas ao gerar os arquivos magnéticos GIA SP, Sped Fiscal, Apuração do ICMS, Registro Apuração do ICMS entre outros envolvendo obrigações fiscais, está sendo apresentando a Inscrição Estadual antiga.   
  
**Ambiente**  
  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

O sistema verifica a Inscrição Estadual do cadastro de empresas (SIGAMAT - SM0).

O ideal é que quando a inscrição estadual seja alterada, seja criado uma nova filial e a filial com a inscrição estadual antiga seja deletada.   
  
Porém caso este processo não tenha sido realizado, é necessário alterar a Inscrição Estadual no cadastro da filial, gerar a obrigação com a IE antiga e depois voltar para a nova IE.
