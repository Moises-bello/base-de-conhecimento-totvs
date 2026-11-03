---
article_id: 4417432718487
category: Controle de Documentos (SIGAQDO)
content_hash: 0fb229c015c7b2879d34c72fac5c80f3db53357dca59815e359f277bd71b725f
fetched_at: '2026-06-28T22:42:29.180181+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Help QX040USRNP na rotina QAXA040
type: support-article
updated_at: '2022-01-10T11:18:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417432718487-Manufatura-Linha-Protheus-SIGAQDO-Help-QX040USRNP-na-rotina-QAXA040
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:16 min****Ocorrência**No módulo **SIGAQDO - Controle de Documentos**, ao tentar finalizar uma ausência temporária por meio da rotina **QAXA040 - Ausência Temporária** é exibido o *help* **QX040USRNRP - Usuário não tem permissão para fazer manutenção no Cadastro de Ausência Temporária**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**O *help* é exibido quando o usuário que está tentando finalizar a ausência temporária não possui o acesso **105 - Manuten. Aus. Temp. Todos** e **106 - Manuten. Aus. Temp. Usuário** marcados no cadastro do usuário no **SIGACFG - Configurador**.  
  
**Solução**Para solucionar esse *help*, realize os seguintes passos:  
1. Acesse o **SIGACFG**;  
2. No menu **Usuário/Senhas/Usuários** selecione o usuário em questão;  
3. Clique em **Alterar**;  
4. Na aba **Restrições de Acessos/Acessos** marque as opções **105 - Manuten. Aus. Temp. Todos** e **106 - Manuten. Aus. Temp. Usuário**;  
5. **Confirme** esta alteração e realize novo teste.
