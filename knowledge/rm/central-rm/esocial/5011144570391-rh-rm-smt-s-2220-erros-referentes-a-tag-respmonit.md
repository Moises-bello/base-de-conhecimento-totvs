---
article_id: 5011144570391
category: eSocial
content_hash: bbf0431e61ae8cc57ebb5da43f0fe95998827f8dfaa1f01837a0dcadb0e312ac
fetched_at: '2026-06-28T22:47:39.096922+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - S-2220: Erros referentes a tag ''respMonit'''
type: support-article
updated_at: '2025-09-25T14:50:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5011144570391-RH-RM-SMT-S-2220-Erros-referentes-a-tag-respMonit
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035701790871) **Tempo aproximado para leitura: 00:02:00 min** **Dúvida**Ao gerar o XML do evento S-2220, são mencionados erros referentes a tag 'respMonit'. O que fazer ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - A partir da versão 12.1.28  
  
**Solução**Acesse o módulo Segurança e Saúde Ocupacional e em seguida a guia **PCMSO | Resp. Monitoração Biológica** e faça um novo filtro com a condição '**Data de início**' e o operador como '**IS NOT NULL**':   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26647523775255)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26647523787415)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26647548763927)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26647548769687)  
  
Valide se há algum registro cadastrado, caso não tenha inclua um registro ou se já possuir um cadastro, avalie o preenchimento dos campos.

**Importante:**

- Os campos '**Responsável'**, '**Data de início**', **'Reg. Cons. Classe' e 'UF Expedição do CRM/COREN'** são obrigatórios e devem estar preenchidos corretamente.

- O cadastro do Responsável deve estar com o CPF preenchido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26647523802647)

- Caso os campos **Filial** e/ou o **Seção** estejam preenchidos, significa que o responsável informado será específico para a filial e seção informada **e deverá ser realizado um novo cadastro para as demais filiais e seções desejadas.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26647523805847)**- Para que um**responsável seja válido para toda a empresa**, ao realizar a inclusão do registro basta deixar os campos **Filial** e **Seção em branco**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26647523813015)

Obs: Os campos **Data de inicio** e **Data término** são limitadores ao período informado. Dessa forma valide se estas datas compreendem o período que a consulta médica foi cadastrada. Exemplo: Se a **Data de início** está para 01/01/2023, mas a consulta médica é de 31/12/2022 significa que este responsável não será considerado para a data desta consulta no evento.

**Saiba Mais:**

Para maiores informações, acesse:

- [Responsável pela Monitoração Biológica](https://tdn.totvs.com/pages/viewpage.action?pageId=452718850)
