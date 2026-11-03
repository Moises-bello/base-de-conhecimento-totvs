---
article_id: 360016740911
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 5034b28f39aff4d6bda32673d92754f471297a5afa8c9ac7d25a3bbc6d536ece
fetched_at: '2026-06-28T22:39:20.496373+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Inscrição Estadual
  para apuração de ICMS ST e DIFAL
type: support-article
updated_at: '2021-07-13T17:28:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016740911-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Inscri%C3%A7%C3%A3o-Estadual-para-apura%C3%A7%C3%A3o-de-ICMS-ST-e-DIFAL
---

**Dúvida**  
 Como cadastrar as Inscrições Estaduais por UF para apuração de ICMS ST e Difal?

**Ambiente**  
Protheus – Fiscal – A partir da versão 11.80  
  
   
**Solução**  
A configuração da Inscrição Estadual para apuração de ICMS ST e Difal pode ser feita no parâmetro **MV\_SUBTRIB** ou na rotina **FISA097.**

Para mais informações sobre a rotina **FISA097** acesse a documentação técnica abaixo:

<http://tdn.totvs.com/pages/releaseview.action?pageId=235586220>

Caso a configuração seja necessária apenas para a apuração do Difal, a inscrição deve ser cadastrada na rotina **FISA115**:

Para atender o esperado pelo PVA da EFD-IMCS/IPI, é necessário o cadastro de Inscrição Estadual também para o Estado de origem.

Será necessário efetuar o cadastro das UFs que a filial contém inscrição estadual.

Dessa forma, no arquivo do SPED, será gerado um registro E300 para o Estado de origem, com um E310 diretamente ligado à ele com todos os valores zerados.

<http://tdn.totvs.com/pages/releaseview.action?pageId=224448537>
