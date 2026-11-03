---
article_id: 15919208313623
category: Integrações Outros BackOffice
content_hash: 3bb111bf8d825bae6db801426dccad5c3f066ec0ec7d304654a79fe5a9fe1399
fetched_at: '2026-06-28T22:46:42.109768+00:00'
product: rm
section_id: 4410716084503
source: central-rm
title: RM - FOP - Integração RM Labore x BackOffice Protheus - Erro ao integrar lançamento
  financeiro AJUDA:E2_TIPO Tipo do título
type: support-article
updated_at: '2024-09-09T17:33:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15919208313623-RM-FOP-Integra%C3%A7%C3%A3o-RM-Labore-x-BackOffice-Protheus-Erro-ao-integrar-lan%C3%A7amento-financeiro-AJUDA-E2-TIPO-Tipo-do-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15919215346839) Tempo aproximado para leitura: **00:02:55 min****Ocorrência**Ao realizar a integração do lançamento financeiro proveniente do RM ao BackOffice Protheus, é retornado o erro **AJUDA:E2\_TIPO** Tipo do título. Relacionado a tabela de parametrização (para maiores informaçöes vide opção Validação). Faz parte da cha-ve de acesso.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro acontece pois o Tipo de Documento enviado pelo RM não existe no ambiente do Protheus.  
  
**Solução**Para solucionar este erro, o deverá informar o mesmo código do **Tipo de Documento** do RM, conforme o exemplo abaixo o código é FGTS:

![](https://totvssuporte.zendesk.com/attachments/token/SniLXuS0zGu0vLh32kU6krsQA/?name=image.png)  
   
Obtendo o código do RM, acesse o ERP Protheus no configurador **SIGACFG** e navegue em **Base de Dados | Dicionário | Bases de Dados |  Tabelas Genéricas e Edite o registro 05 - "Tipos de Títulos"**, para incluir um novo registro.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15918939533975)  
   
Navegue até a ultima linha da tabela e tecle seta para baixo para incluir um novo registro, esse novo registro deverá possuir no campo chave o mesmo código que está sendo enviado pelo RM, conforme exemplo anterior utilizamos o cadastro FGTS.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15918997328023)

Verifique o**tipo de documento** em seu ambiente RM e realize o cadastro com a mesma chave, a descrição poderá ser a de sua preferência porém, o a coluna **Chave** deverá obrigatoriamente ser o código que existe no RM.
