---
article_id: 360007302812
category: Gestão de Transportes (TMS)
content_hash: 8656b77296f4244389056a3c38f88b47dc1725679e10419e4b5b49742affc45d
fetched_at: '2026-06-28T22:45:27.724898+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Erro variable is not an object on FWSEEK:LOADSEEK
type: support-article
updated_at: '2023-02-28T13:16:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007302812-Log%C3%ADstica-Linha-Protheus-TMS-Erro-variable-is-not-an-object-on-FWSEEK-LOADSEEK
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:50 min**  
  
**Dúvida**Qual o procedimento a ser realizado quando ocorrer o erro:**variable is not an object on FWSEEK:LOADSEEK**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Se você estiver enfrentando problemas pontuais apenas com determinado usuário, pode ser alguma sujeira, no perfil do usuário. Pode-se tentar efetuar uma manutenção de **profile**, recriando apenas o perfil deste usuário específico, conforme passos abaixo:

* Faça um *backup* da pasta **Profile**, que fica dentro da pasta **Protheus\_Data**, efetue o *backup* com os serviços do **Protheus** parados;
* Acesse o **Configurador - SIGACFG**
* **Menu Ambiente / Cadastros / Manutenção Profile**, **Programa -** **PROFMGR**;
* Apague pontualmente os registros do usuário que está com problema, clique sobre o código do usuário, clique em **Excluir**, e selecione **Todos registros do usuário**.
