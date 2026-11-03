---
article_id: 31122125524247
category: TAF - REINF
content_hash: fc9d54039f28ef81801d647f5682c91aadf5c0d8cb63174f1f1e3fc24629f721
fetched_at: '2026-06-28T22:41:33.467313+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - MIT - Erro:
  DadosIniciais.RegimePisCofins: campo obrigatório não informado'
type: support-article
updated_at: '2025-04-03T13:58:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31122125524247-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-MIT-Erro-DadosIniciais-RegimePisCofins-campo-obrigat%C3%B3rio-n%C3%A3o-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31122125504663) Tempo aproximado para leitura: **00:02:00min****Ocorrência**  
MIT -  Arquivo Json erro de validação: DadosIniciais.RegimePisCofins: campo obrigatório não informado.  
**Ambiente**TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - A partir da versão 12.1.2310  
  
**Causa**Esse incidente ocorre quando não é informado o **Regime PIS/COFINS** no cadastro campo **CHD\_PISCOF** na Rotina **TAFA372** - Parâmetros de Cálculo  para geração do MIT.  
  
**Solução**

Para solucionar essa ocorrência, informe no campo Reg. Pis/Cof (**CHD\_PISCOF**) Regime de apuração do PIS/Pasep e/ou da Cofins para um dos códigos permitidos e faça um novo teste:

Cadastro  na Rotina TAFA372 - Parâmetros de Cálculo

![CHD_PISCOF.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31122684329111)

MIT - Módulo de Integração de Tributos:

<https://tdn.totvs.com/pages/releaseview.action?pageId=904594705>

De\Para (TAGS do layout **MIT** x Campos **TAF**)

|  |  |  |  |
| --- | --- | --- | --- |
| DadosIniciais | 10 | RegimePisCofins | **CHD\_PISCOF** |
