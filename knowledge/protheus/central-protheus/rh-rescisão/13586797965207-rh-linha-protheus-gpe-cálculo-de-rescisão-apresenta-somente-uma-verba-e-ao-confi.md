---
article_id: 13586797965207
category: RH - Rescisão
content_hash: 6e11551f00b365bbd6a093fcc81da16b7f494df0c9107565ee5a18330954a35e
fetched_at: '2026-06-28T22:43:51.930187+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Cálculo de rescisão apresenta somente uma verba
  e ao confirmar o cálculo é gerado aviso: FWNOWIDTH Valor atribuído difere do tamanho
  campo (Seq. Verba)'
type: support-article
updated_at: '2023-04-04T12:25:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13586797965207-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-apresenta-somente-uma-verba-e-ao-confirmar-o-c%C3%A1lculo-%C3%A9-gerado-aviso-FWNOWIDTH-Valor-atribu%C3%ADdo-difere-do-tamanho-campo-Seq-Verba
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Por que cálculo de rescisão apresenta somente uma verba e ao confirmar o cálculo é gerado aviso: FWNOWIDTH Valor atribuído difere do tamanho campo (Seq. Verba)?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13586549712407)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**O problema ocorre pois o tamanho do campo Seq. Verba entre as tabelas SRR e RGB estão diferentes.

É necessário ajustar o tamanho do campo Seq. Verba entre as tabelas SRR e RGB .  
Após validação e correção do tamanho do campo Seq. Verba, o cálculo da rescisão apresentará todas a verbas.

**SRR - campo RR\_SEQ**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13606738451863)

**RGB - campo RGB\_SEQ**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13606777546647)

**Após editar os campos, clique no disquete (atualizar banco de dados), assim as edições serão salvas.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13606786318743)

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo

[MP - GPE - Cálculo de rescisão apresenta somente uma verba e ao confirmar o cálculo é gerado aviso: FWNOWIDTH Valor atribuído difere do campo (C. de Custo)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005380601-MP-GPE-C%C3%A1lculo-de-rescis%C3%A3o-apresenta-somente-uma-verba-e-ao-confirmar-o-c%C3%A1lculo-%C3%A9-gerado-aviso-FWNOWIDTH-Valor-atribu%C3%ADdo-difere-do-campo-C-de-Custo-?source=search)  
   
[RH - Linha Protheus - GPE - Cálculo de rescisão apresenta somente uma verba e ao confirmar o cálculo é gerado aviso: FWNOLIST Valor atribuído difere da lista de valores válidos (Tipo)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6674466519319-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-apresenta-somente-uma-verba-e-ao-confirmar-o-c%C3%A1lculo-%C3%A9-gerado-aviso-FWNOLIST-Valor-atribu%C3%ADdo-difere-da-lista-de-valores-v%C3%A1lidos-Tipo-?source=search)
