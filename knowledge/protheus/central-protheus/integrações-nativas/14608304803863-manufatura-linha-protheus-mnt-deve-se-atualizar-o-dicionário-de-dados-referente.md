---
article_id: 14608304803863
category: Integrações Nativas
content_hash: c09a4206f7196e574e9485da190c0cefbe0cfd58c923d8e53a61418c8d74ef70
fetched_at: '2026-06-28T22:42:35.375460+00:00'
product: protheus
section_id: 360012117933
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Deve-se atualizar o dicionário de dados,
  referente a tabela SD4 utilizada na integração
type: support-article
updated_at: '2023-07-13T14:04:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14608304803863-Manufatura-Linha-Protheus-MNT-Deve-se-atualizar-o-dicion%C3%A1rio-de-dados-referente-a-tabela-SD4-utilizada-na-integra%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15906548032023)** Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao acessar a rotina **O.S Corretiva - MNTA420** retorna a mensagem de **Deve-se atualizar o dicionário de dados, referente a tabela SD4 utilizada na integração.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14607583333783)**

**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integrações Nativas - Todas as versões  
  
**Causa**A situação acontece porque os os processos do módulo passam a utilizar execuções automáticas das rotinas de outros módulos e o uso de campos não está disponível para o módulo.  
  
**Solução**  
Para solucionar a situação será necessário verificar / alterar os campos **D4\_COD**, **D4\_TRT**, **D4\_LOTECTL**, **D4\_NUMLOTE**, **D4\_LOCAL**, **D4\_OPORIG**, **D4\_SEQ** e **D4\_DTVALID**na **base de dados** no **SIGACFG**, se o c*heckbox* de **Usado** na aba **Uso** está marcado e se a opção de **Utilizado por todos os módulos está marcada** na **aba Módulos**.

* *Checkbox* de **Usado**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14608063851799)

* Opção de **Utilizado por todos os módulos**

![](https://tdn.totvs.com/download/attachments/666465698/222.PNG?version=1&modificationDate=1644585145460&api=v2)

Após realizar o ajuste em todos os campos, salve as alterações utilizando o **Atualizar base de dados...**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14608150464151)**

**Saiba mais**Para informações complementares, veja o boletim [13286970 DNG-15619 DT Alteração de armazém de produto empenhado](https://tdn.totvs.com/pages/viewpage.action?pageId=666465698)
