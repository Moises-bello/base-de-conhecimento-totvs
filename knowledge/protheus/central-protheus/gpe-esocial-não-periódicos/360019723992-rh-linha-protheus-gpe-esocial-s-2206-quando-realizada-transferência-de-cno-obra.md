---
article_id: 360019723992
category: GPE - eSocial - Não Periódicos
content_hash: 123affd25f6f3b94a356bb23e0a433f4a3c7fd8e0af8ac0466753fbddea772b5
fetched_at: '2026-06-28T22:45:04.760104+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - Quando realizada transferência
  de CNO (obra) para funcionário, como atualizar informação no TAF
type: support-article
updated_at: '2026-06-16T11:25:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019723992-RH-Linha-Protheus-GPE-eSocial-S-2206-Quando-realizada-transfer%C3%AAncia-de-CNO-obra-para-funcion%C3%A1rio-como-atualizar-informa%C3%A7%C3%A3o-no-TAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28065486352279)** Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Quando realizada transferência de CNO (obra) para funcionário, como atualizar informação no TAF para posterior transferência ao governo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**No caso de transferências por centro de custo com alteração do CNO, podem ocorrer duas situações. Identificar em qual delas se encaixa o cenário, para solução:  
  
**1.** Transferência por centro custo referente a obra total (quando no centro custo consta o Tipo de Lotação como 01 com CNO preenchido e existir um evento S-1005 para a obra), ou seja, funcionário passará a ser vinculado a um outro registro S-1005 (como se estivesse sendo transferido para outro vínculo).  
Neste caso, ocorreria a transmissão primeiro da nova lotação tributária contendo o novo CNO (caso fosse novo) gerando evento S-1005 no TAF e em seguida o evento S-2206 referente a alteração no cadastro do funcionário.  
  
**2.** Transferência por centro custo com CNO mas sem ser obra total (não existe um registro S-1005 no TAF referente a obra, devido o tipo de lotação ser diferente de 01 por exemplo). Neste caso, há entendimento apenas da transferência por centro custo e esta não é transmitida, devido não existir vínculo do trabalhador a lotação tributária, mas sim a uma entidade (empresa/obra).  
Para mais informações referente ao evento de entidades/obras S-1005 ao qual o Trabalhador deve estar vinculado, segue link:  
<http://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais+-+S-1005>  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[Artigos S-2206](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055237854)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página *[TOTVS Informa](https://informa.totvs.com/)* selecione em categorias a área e pesquise por "Eventos".
