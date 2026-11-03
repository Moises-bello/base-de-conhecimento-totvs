---
article_id: 360052083833
category: RH - Funcionários
content_hash: 2612c427f87b8b7c95b75a02cbfd1a662160ea3e9c1238af5308fc71964b394e
fetched_at: '2026-06-28T22:43:27.549530+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o parâmetro MV_AUTPART
type: support-article
updated_at: '2025-06-09T18:10:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052083833-RH-Linha-Protheus-GPE-Como-configurar-o-par%C3%A2metro-MV-AUTPART
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27282490288151) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como configurar o parâmetro MV\_AUTPART?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

O parâmetro **MV\_AUTPART** existe para definir sobre a inclusão de participante a partir do cadastro de autônomos, e **deve conter** um dos valores abaixo de acordo com a necessidade de cada empresa:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27282505087511)

**1 = Pergunta se inclui.**

**2 = Sempre inclui.**

**3 = Nunca inclui.**

Como o parâmetro por padrão tem o valor indefinido, ou seja, esta em branco, o sistema **assume o valor 3** que no caso, nunca inclui o registro na tabela RD0 (participantes).   
Para ajustar o parâmetro acesse o **Configurador SIGACFG em Ambiente > Cadastros > Parâmetros (CFGX017)** pesquise o parâmetro e ajuste conforme a necessidade. 

**Saiba Mais**[RH - Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909593-RH-Funcion%C3%A1rios)  
[RH - Linha Protheus - GPE - Como realizar o cadastro/admissão de funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404568864151-RH-Linha-Protheus-GPE-Como-realizar-o-cadastro-admiss%C3%A3o-de-funcion%C3%A1rio)  
[RH - Linha Protheus - GPE - Como cadastrar um Autônomo ou Pró-labore](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052067393-RH-Linha-Protheus-GPE-Como-cadastrar-um-Aut%C3%B4nomo-ou-Pr%C3%B3-labore)  
[RH - Linha Protheus - GPE - Quais os Pontos de Entrada disponíveis na rotina GPEA010 - Cadastro de Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024786154-RH-Linha-Protheus-GPE-Quais-os-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-GPEA010-Cadastro-de-Funcion%C3%A1rios)
