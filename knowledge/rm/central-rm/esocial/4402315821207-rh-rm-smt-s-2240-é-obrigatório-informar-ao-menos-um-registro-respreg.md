---
article_id: 4402315821207
category: eSocial
content_hash: 74c8b633305af16fe929da5cab42810624fabe91d8de22f1a2191d64cf07aecc
fetched_at: '2026-06-28T22:47:39.189549+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - S-2240: É obrigatório informar ao menos um registro ''respReg''.'
type: support-article
updated_at: '2025-09-25T14:50:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402315821207-RH-RM-SMT-S-2240-%C3%89-obrigat%C3%B3rio-informar-ao-menos-um-registro-respReg
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16038802210967) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Ao gerar o XML do evento 2240 aparece a mensagem de erro: **'É obrigatório informar ao menos um registro 'respReg'**, o que fazer ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - A partir da versão **12.1.28**  
  
**Solução**Acesse o módulo Segurança e Saúde Ocupacional e em seguida a guia **PPRA | Resp. Reg. Ambientais**  e faça um novo filtro com a condição **'Data de inicio'** e o Operador como **'IS NOT NULL**':   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26727326256279)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26727326261527)

Valide se existe algum registrado, caso não tenha deverá incluir um novo e preencher os campos **Responsável, Reg.Cons.Classe, Órgão de Classe e UF de expedição do CRM/COREN.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26727320559767)

Caso já tenha cadastro, verifique se o preenchimento de todos estes campos estão corretos.

**Importante**

- Os campos **'Responsável', 'Data de início', 'Reg. Cons. Classe' e 'UF Expedição do CRM/COREN'** são obrigatórios e devem estar preenchidos corretamente.

- O cadastro do Responsável deve estar com o CPF preenchido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26727320563479)

- Caso os campos **Filial** e/ou o **Seção** estejam preenchidos, significa que o responsável informado será específico para a filial e seção informada **e deverá ser realizado um novo cadastro para as demais filiais e seções desejadas.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26727326271511)**

**-** Para que um**responsável seja válido para toda a empresa,** ao realizar a inclusão do registro basta deixar os campos **Filial** e **Seção em branco:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26727320568855)**

**Obs:** Os campos **Data de inicio e Data término** são limitadores ao período informado. Dessa forma valide se estas datas compreendem o período que a consulta médica foi cadastrada. Exemplo: Se a **Data de início** está para 01/01/2023, mas a consulta médica é de 31/12/2022 significa que este responsável não será considerado para a data desta consulta no evento.

**Saiba Mais**

Para mais informações acesse:

- [Responsável pelos Registros Ambientais](https://tdn.totvs.com/pages/viewpage.action?pageId=452718849)
