---
article_id: 360052244053
category: RH - FGTS / SEFIP
content_hash: aa551bcf5156173a273927035db7fb9c6637c4e025c1d46cad97ed1864f18797
fetched_at: '2026-06-28T22:43:41.396971+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro ao validar a Sefip: Categoria do Trabalhador
  não classificada 300573'
type: support-article
updated_at: '2021-07-17T03:28:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052244053-RH-Linha-Protheus-GPE-Erro-ao-validar-a-Sefip-Categoria-do-Trabalhador-n%C3%A3o-classificada-300573
---

**Ocorrência**Erro ao validar a Sefip: Categoria do Trabalhador não classificada 300573.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**O erro ocorre pois é demonstrado o nome ou PIS do trabalhador em questão, provavelmente o PIS do mesmo esta duplicado em outro registro na no cadastro do funcionário ou na tabela SRA.  
  
**Solução**Faça uma consulta genérica da tabela **SRA** e filtre o campo **RA\_PIS** com o código em questão e verifique quais registros estão com o mesmo **PIS** e veja se está mesmo duplicado. Caso esteja basta alterar e gerar a SEFIP novamente.

Caso esteja duplicado, mas se tratar de funcionário com múltiplo vinculo, informe a **ocorrência "05"** no campo Ocorrência, da Aba "Funcionais" do cadastro de Funcionários.  
  
**Saiba mais:**<https://tdn.totvs.com/display/public/PROT/FGTS>
