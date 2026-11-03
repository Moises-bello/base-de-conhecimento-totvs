---
article_id: 4416885304471
category: Metrologia (SIGAQMT)
content_hash: 80ee5760ad1f9cc3de586206f9853de83458eff15723211775b51a5cf15489f9
fetched_at: '2026-06-28T22:42:24.860661+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - QMTA140 - Não existe nenhuma Escala
  relacionada com este instrumento, favor verificar para que possam ser digitados
  os resultados
type: support-article
updated_at: '2025-03-12T11:43:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416885304471-Manufatura-Linha-Protheus-SIGAQMT-QMTA140-N%C3%A3o-existe-nenhuma-Escala-relacionada-com-este-instrumento-favor-verificar-para-que-possam-ser-digitados-os-resultados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30586591993495) Tempo aproximado para leitura: **00:01:10 min****Ocorrência**No módulo **SIGAQMT - Metrologia**, ao realizar a calibração de um instrumento por meio da rotina **QMTA140 - Calibrações** ocorre a mensagem **Não existe nenhuma Escala relacionada com este instrumento, favor verificar para que possam ser digitados os resultados**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**Esta mensagem é exibida quando não existe faixa relacionada com o instrumento na opção **Faixas** da rotina **QMTA010 - Instrumentos** onde é validada a tabela **QMR - Tolerância e Redutor Faixas**.  
  
**Solução**Antes de realizar o cadastro do instrumento é necessário associar a faixa a uma família.   
Esta associação é realizada por meio da opção **Outras Ações/Associações/Faixas** da rotina **QMTA030 - Famílias**.  
Desta forma, quando já existe esta associação antes de cadastrar o instrumento, a opção **Faixas** da rotina **QMTA010** será carregada automaticamente, gerando a tabela **QMR**.  
E quando esta associação é realizada após o instrumento já estar cadastrado, a mensagem continuará sendo exibida porque a tabela **QMR** ainda não existe. Sendo assim, é necessário excluir o instrumento e cadastrá-lo novamente.
