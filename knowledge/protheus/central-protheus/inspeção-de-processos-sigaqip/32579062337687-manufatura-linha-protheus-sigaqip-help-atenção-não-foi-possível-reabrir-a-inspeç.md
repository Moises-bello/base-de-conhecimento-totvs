---
article_id: 32579062337687
category: Inspeção de Processos (SIGAQIP)
content_hash: 70c45701566a01d1c7a5aad3403dd59ed93eba069d186ab007edf3a953d6bc54
fetched_at: '2026-06-28T22:42:25.763572+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Help Atenção - Não foi possível reabrir
  a inspeção
type: support-article
updated_at: '2025-06-04T21:02:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32579062337687-Manufatura-Linha-Protheus-SIGAQIP-Help-Aten%C3%A7%C3%A3o-N%C3%A3o-foi-poss%C3%ADvel-reabrir-a-inspe%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32579062300695) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Na rotina QIPA215 - Resultados, ao selecionar a inspeção e ir em **Outras Ações > Reabrir Inspeção,** é retornado o *help* Atenção - Não foi possível reabrir a inspeção. Verifique se o seu usuário tem acesso a todos os níveis da inspeção e repita o processo.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Causa**O *help* **Atenção** pode ocorrer nas situações abaixo:1. quando usuário **não tem acesso liberado ao módulo SIGAQIP - Inspeção de Processos e aos laudos** na rotina **QIEA050 - Usuários**;   
2. quando o **nível do usuário** definido na **QIEA050** e no**SIGACFG - Configurador** está inferior ao conteúdo do parâmetro **MV\_QPLDNIV - Define o nível que o usuário deve possuir, para emitir os laudos de laboratório, operação e geral, respectivamente;**3. quando o parâmetro **MV\_QPLDNIV** não tem conteúdo informado**.**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Na rotina **QIEA050** valide se o usuário **possui acesso ao módulo SIGAQIP e aos laudos**, sendo: **1 = Com Acesso,  2 = Sem Acesso, 3 = Apenas Consulta, Vazio = similar a opção 1, com acesso**;  
2. Na rotina **QIEA050** avaliar o **nível do usuário** cadastrado;  
3. No **SIGACFG** avaliar o **nível do usuário** cadastrado;  
4. Avaliar se o parâmetro **MV\_QPLDNIV** possui **conteúdo**, caso possua conteúdo deverá avaliar se o **nível do usuário** cadastrado na rotina **QIEA050** e **SIGACFG** está **inferior** à exigência cadastrada no parâmetro.  
  
**Observação**  
Artigo complementar sobre a funcionalidade do parâmetro **MV\_QPLDNIV**: [Manufatura - Linha Protheus - SIGAQIP - Definir nível de usuário para emissão de laudo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/16006925992855-Manufatura-Linha-Protheus-SIGAQIP-Definir-n%C3%ADvel-de-usu%C3%A1rio-para-emiss%C3%A3o-de-laudo)
