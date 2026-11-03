---
article_id: 8127416469143
category: RH - Cadastros
content_hash: 7bb4d56d54a23b32e38b1adbd04c37ec1f042e7bcf9dc3075f84ed03de2246fd
fetched_at: '2026-06-28T22:43:25.991591+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Utilização do Ponto de Entrada GP010VALPE no Cadastro
  de Funcionários - GPEA010
type: support-article
updated_at: '2025-07-15T16:40:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8127416469143-RH-Linha-Protheus-GPE-Utiliza%C3%A7%C3%A3o-do-Ponto-de-Entrada-GP010VALPE-no-Cadastro-de-Funcion%C3%A1rios-GPEA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26792456315927) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Utilização do Ponto de Entrada GP010VALPE no Cadastro de Funcionários - GPEA010  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.33  
  
**Solução**  
O ponto de entrada GP010VALPE  tem como objetivo checar os dados de inclusão e/ou alteração no cadastro de Funcionários. Seu retorno deve ser verdadeiro (.T.) ou falso (.F.).

**Sintaxe**GP010VALPE - Inclusão/Alteração de Funcionários ( ) --> .T. ou .F.

**Retorno**  
**.T. ou .F.** (logico)  
O retorno deste ponto de entrada deve ser lógico, se: .T. - o registro será incluído/alterado; .F. - o registro não será gravado, aguardando ação do usuário.

**Observações**  
Este Ponto de Entrada também é utilizado pela rotina de funcionários do SIGATRM (TRMA100.PRW).

  
**Saiba mais**

[GP010VALPE - InclusãoAlteração de Funcionários](https://tdn.totvs.com/pages/releaseview.action?pageId=6079099)

[Artigos Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)

[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
