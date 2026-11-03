---
article_id: 360043179034
category: RH – DIRF
content_hash: 7ac835c0531ed382137cce339b679f09a837f5104661a732a6ce6eca47230958
fetched_at: '2026-06-28T22:44:07.067003+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Não gera bloco INF no txt da DIRF referente a previdência
  complementar e plano de saúde
type: support-article
updated_at: '2025-08-19T17:29:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043179034-RH-Linha-Protheus-GPE-N%C3%A3o-gera-bloco-INF-no-txt-da-DIRF-referente-a-previd%C3%AAncia-complementar-e-plano-de-sa%C3%BAde
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34295862581271)**Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Não gera bloco INF no TXT da DIRF referente a previdência complementar e plano de saúde.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Regras do *layout* do arquivo magnético da DIRF.  
  
**Solução**A geração do bloco INF no arquivo de saída da DIRF destina-se exclusivamente à geração de informações complementares diversas, excetuando-se as previstas para geração em blocos específicos definidos no layout da DIRF.  
  
A previdência complementar, assim como o desconto de plano de saúde, por exemplo, tem registros próprios definidos dentro do layout da DIRF, e suas informações de contribuição à previdência e descontos dos planos de saúde são gerados em seus respectivos blocos e interpretados pelo PGDIRF.

Tanto que, ao imprimir o Informe de Rendimentos pelo PGDIRF onde há informações para o registro PSE, sem existir informações para o registro INF, as informações do PSE são interpretadas e o quadro 07 do Informe é preenchido.

No entanto, o mesmo não é realizado com as informações de previdência complementar, por uma característica do PGDIRF, não por uma suposta omissão da informação pelo Protheus.

Ainda assim, cabe ressaltar que o Informe de Rendimentos deve ser emitido pelo Protheus, onde todas as informações complementares serão geradas conforme o preenchimento das tabelas da DIRF (RCS, SM8 e SM9).

**Saiba mais**  
[RH - Linha Protheus - GPE - Passo a Passo para geração do Arquivo magnético da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022076092)

[Página centralizadora Protheus - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
