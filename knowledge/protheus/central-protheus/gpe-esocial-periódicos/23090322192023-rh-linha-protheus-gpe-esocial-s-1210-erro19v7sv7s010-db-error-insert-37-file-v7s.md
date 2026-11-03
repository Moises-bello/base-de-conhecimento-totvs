---
article_id: 23090322192023
category: GPE - eSocial - Periódicos
content_hash: 3f5d0d1d4b0abcd7509a4aa22b85a28ec6f4be468d9128da27ef6db880bdb065
fetched_at: '2026-06-28T22:45:08.971532+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1210 - ERRO19|V7S|V7S010: DB error
  (Insert): -37 File: V7S010 - Error: 2601 (23000) (RC=-1)'
type: support-article
updated_at: '2024-06-04T19:38:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23090322192023-RH-Linha-Protheus-GPE-eSocial-S-1210-ERRO19-V7S-V7S010-DB-error-Insert-37-File-V7S010-Error-2601-23000-RC-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23090322174487) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo SIGAGPE, ao tentar realizar a geração e integração do evento S-1210 através da rotina **Eventos Periódicos (GPEM034)** é apresentada a mensagem **ERRO19|V7S|V7S010: DB error (Insert): -37 File: V7S010 - Error: 2601 (23000) (RC=-1)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23090368149655)**  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**A partir do Leiaute S-1.2, o evento S-1210 integra informações referente a dependentes e esse erro ocorre quando existe algum dependente cadastrado sem o CPF informado.  
  
**Solução**Verifique se existe algum dependente ativo com o CPF não preenchido. E caso tenha, realize o preenchimento do CPF, pois é uma informação obrigatória, e realize a integração e envio do S-2205 com competência anterior do S-1210.  
Caminho: SIGAGPE > Atualizações > Funcionários > Dependentes.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23125646839959)  
  
Para os casos onde está sendo integrado dependentes que deixaram de ser, já mapeamos e corrigimos na issue DRHROTPRT-16127, segue boletim: <https://tdn.totvs.com/pages/viewpage.action?pageId=838208329>   
Para ajuste do sistema aplique a [Expedição Continua RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
