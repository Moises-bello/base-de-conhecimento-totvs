---
article_id: 360052339894
category: RH - Soluções para error.log
content_hash: 5dc778a746d16cf936e0e911b93494ac9db1f3b3cc2d069a531cee3f91b13204
fetched_at: '2026-06-28T22:44:09.017909+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: MP - TRM - Ao entrar no cadastro de funcionários pelo módulo de Treinamento
  gera error log - array out of bounds [0] of [14]  on { |X, Y| X[NPOSCALEND]+X[NPOSCURSO]+X[NPOSTURMA]+X[NPOSTESTE]+X[NPOSQUEST]+X[NPOSALT]
type: support-article
updated_at: '2021-02-09T11:38:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052339894-MP-TRM-Ao-entrar-no-cadastro-de-funcion%C3%A1rios-pelo-m%C3%B3dulo-de-Treinamento-gera-error-log-array-out-of-bounds-0-of-14-on-X-Y-X-NPOSCALEND-X-NPOSCURSO-X-NPOSTURMA-X-NPOSTESTE-X-NPOSQUEST-X-NPOSALT
---

**Ocorrência**Ao tentar entrar no cadastro de funcionários pelo **módulo de Treinamento,** através da rotina **TRMA100** gera *error log:* "***array out of bounds*** **[0]** ***of*** **[14]*****on*** **{ |X, Y| X[NPOSCALEND]+X[NPOSCURSO]+X[NPOSTURMA]+X[NPOSTESTE]+X[NPOSQUEST]+X[NPOSALTERN] < Y[NPOSCALEND]+Y[NPOSCURSO]+Y[NPOSTURMA]+Y[NPOSTESTE]+Y[NPOSQUEST]+Y[NPOSALTERN]}(TRMA100.PRW)***"***Ambiente**Protheus - Treinamento - A partir da versão 12.1.17  
  
**Causa**O erro ocorre devido ao conflito do campo **Centro de Custo (RA8\_CC)** que no SIGATRM não o reconhece como **"usado"****Solução** **1.** Para solucionar esse erro deve ser aplicado o pacote acumulado do RH de acordo com as instruções do artigo abaixo:  
Pacote Acumulado do RH:  
[MP - GPE - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal?source=search)  
  
**2.** Executar o processo de UPDDISTR, procedimentos para Atualização de Dicionários: [Atualização de Dicionário Diferencial](https://tdn.totvs.com/pages/viewpage.action?pageId=366649057)  
  
**Saiba mais:**Para adquirir mais conhecimentos acesse o(s) *link*(s) abaixo:  
[6630843 DRHGCH-13270 DT Ao acessar a rotina TRMA130 pelo SIGAMDT](https://tdn.totvs.com/display/public/PROT/6630843+DRHGCH-13270+DT+Ao+acessar+a+rotina+TRMA130+pelo+SIGAMDT)
