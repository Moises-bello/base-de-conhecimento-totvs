---
article_id: 360011007231
category: PCMSO / Exames
content_hash: 284434c182848e0e306549e7b4c9fc440c894ed2ee44356582c39d943a32dabe
fetched_at: '2026-06-28T22:47:42.194223+00:00'
product: rm
section_id: 1500000861462
source: central-rm
title: 'RH - RM - SMT - Erro ao gerar relatorio ASO: Preencha as informações faltantes
  no cadastro de Responsável pela Monitoração Biológica'
type: support-article
updated_at: '2025-10-30T18:12:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011007231-RH-RM-SMT-Erro-ao-gerar-relatorio-ASO-Preencha-as-informa%C3%A7%C3%B5es-faltantes-no-cadastro-de-Respons%C3%A1vel-pela-Monitora%C3%A7%C3%A3o-Biol%C3%B3gica
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035845124887) Tempo aproximado para leitura: 00:01:30 min  
  
Ocorrência**Ao gerar o relatório ASO é apresentada a mensagem:  
  
**"O Atestado de Saúde Ocupacional não pôde ser gerado, pois não consta a informação referente ao Coordenador(a) do Programa de PCMSO. Preencha as informações faltantes no cadastro de Responsável pela Monitoração Biológica, incluindo o número do registro no órgão de classe, e execute o processo novamente!"**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008419291)  
   
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - Todas as versões  
  
**Causa**Inconsistência no cadastro do responsável pela monitoração biológica.  
  
**Solução**

Realize a verificação se há um responsável de monitoração biológica cadastrado.

Para conferir acesse o módulo de **Segurança e Saúde Ocupacional |** menu **PCMSO | Resp. Monitoração biológica**, e valide se existe o cadastro do responsável respeitando as seguintes regras:

* A data de início do cadastro deve ser menor ou igual a data da consulta cadastrada.
* As informações referente a **Responsável**, **Reg. Cons. Classe** e **UF de expedição do CRM/COREN** devem ser preenchidas.
* O CPF do responsável deve estar preenchido.
* Caso os campos **Filial e/ou o Seção** estejam preenchidos, significa que o responsável informado será específico para a filial e seção informada e **deverá ser realizado um novo cadastro para as demais filiais e seções desejadas.**
* Para que um **responsável seja válido para toda a empresa,** ao realizar a inclusão do registro basta deixar os campos **Filial e Seção em branco.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26834138651287)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26834196080791)

**Saiba mais**Para maiores informações, acesse:

- [RH - RM - SMT - S-2220: Erros referentes a tag 'respMonit'](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5011144570391)

- [Atestado de Saúde Ocupacional.](https://tdn.totvs.com/pages/viewpage.action?pageId=452719163)
