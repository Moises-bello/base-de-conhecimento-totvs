---
article_id: 360045912053
category: RH - RAIS
content_hash: 189160deb274d8f0721f4728e1fd52707fc4dbabe1669e8cc9b226443ef035df
fetched_at: '2026-06-28T22:44:05.795980+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - Rais erro - 0940 - O empregado para ser declarado
  deve ter remuneração no ano-base
type: support-article
updated_at: '2025-08-06T14:53:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045912053-RH-Linha-Protheus-GPE-Rais-erro-0940-O-empregado-para-ser-declarado-deve-ter-remunera%C3%A7%C3%A3o-no-ano-base
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33987477486615) Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**

Rais erro - 0940 - O empregado para ser declarado deve ter remuneração no ano-base

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal –  Todas as versões  
  
**Solução**

Para que o Funcionário seja considerado na Rais é necessário que o mesmo possua movimentação durante o ano, então deve-se verificar se o mesmo se encontra afastado durante todo o ano e se o afastamento é devido;

Deverá verificar o cadastro de ausências tabela SR8 e verificar o período inicial e final do afastamento

Verificar se existe remuneração para o empregado na data do retorno

Dica: O validador acusa o erro, porque o colaborador não teve valores no ano base, devido a estar afastado em auxílio doença antes de aposentar-se.

No Protheus no grupo de perguntas do GPEM530 RAIS / Arquivo magnético existe a pergunta Considera Afastado s/ Remun? Sim ou não

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063258854)

Caso informe sim o GDRAIS irá gerar esta inconsistência  (ocorre devido a uma inconsistência no validador) e para corrigir deverá informar 0,01 centavo em algum mês como remuneração mensal. Este procedimento pode ser realizado diretamente no GDRais.

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
