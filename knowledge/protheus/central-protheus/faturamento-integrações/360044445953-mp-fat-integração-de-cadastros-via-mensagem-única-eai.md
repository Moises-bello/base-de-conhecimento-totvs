---
article_id: 360044445953
category: Faturamento - Integrações
content_hash: bf6b0c0d8f57db6e9deb0209d2cf8aa9574413525f2caffba4da92eff1fe6faa
fetched_at: '2026-06-28T22:38:26.579974+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: MP - FAT - INTEGRAÇÃO DE CADASTROS VIA MENSAGEM ÚNICA (EAI)
type: support-article
updated_at: '2022-11-23T12:22:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044445953-MP-FAT-INTEGRA%C3%87%C3%83O-DE-CADASTROS-VIA-MENSAGEM-%C3%9ANICA-EAI
---

**Ocorrência**INTEGRAÇÃO DE CADASTROS VIA MENSAGEM ÚNICA (EAI).  
  
**Ambiente**

Microsiga Protheus – A partir da release 11.80.  
  
**Solução**

Primeiro deve avaliar se realmente não tem o registro no ERP Protheus, não tendo o registro, as soluções para excluir os registros são:

1. Entender o motivo do registro não estar no ambiente Protheus, pois se o **Adapter** estiver correto e a sincronização de carga inicial (**APCFG020A**) foi realizada de forma correta, o cadastro tem que estar no Protheus.

2. Se a carga inicial não foi rodada para estes cadastros ainda, rode para que o sistema leve os cadastros do Sistema A para o Protheus. Não se esqueça de configurar o Adapter do cadastro que deseja integrar.

-Configurador - Menu: Ambiente, Schedule, Sinc. Carga Inicial EAI

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059396274/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060278153/mceclip1.png)

3.  Caso a Carga Inicial já tenha sido realizada uma vez para estes registros e por alguma motivo o cadastro X não foi levado para o Protheus, a única maneira de excluir um registro é desabilitar o envio e recebimento do Adapter (**em um horário que ninguém esteja utilizando**) e realizar a exclusão do registro no Sistema A.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060279693/mceclip2.png)

**Obs: Tomamos como exemplo o cadastro de cliente,  porém é o mesmo conceito para todos os cadastros  do sistema , exemplo: Produto, Fornecedor, Natureza...**
