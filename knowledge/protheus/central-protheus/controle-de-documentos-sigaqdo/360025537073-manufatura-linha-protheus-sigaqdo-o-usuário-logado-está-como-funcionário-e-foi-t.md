---
article_id: 360025537073
category: Controle de Documentos (SIGAQDO)
content_hash: d928d7f09b0bdd1401d3575649a6c3bfc2292661526007421cc3cfcfeb81fa26
fetched_at: '2026-06-28T22:42:29.213655+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - O usuário logado está como funcionário
  e foi transferido de departamento mas não teve a pendência transferida
type: support-article
updated_at: '2022-03-18T14:24:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025537073-Manufatura-Linha-Protheus-SIGAQDO-O-usu%C3%A1rio-logado-est%C3%A1-como-funcion%C3%A1rio-e-foi-transferido-de-departamento-mas-n%C3%A3o-teve-a-pend%C3%AAncia-transferida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min**  
**Ocorrência**Ao realizar a baixa na rotina de **QDOA030 - Pendências**, é apresentada a mensagem a seguir **O usuário logado está como funcionário e foi transferido de departamento mas não teve a pendência transferida**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**Esta mensagem ocorre quando o usuário logado foi transferido de departamento mas a **pendência** que estava com o mesmo **não foi transferida para um novo responsável**. Isto é, com a transferência de departamento, o usuário em questão ficou sem permissão para baixar esta pendência.  
  
**Solução**  
Para solucionar, é necessário **transferir** esta pendência para outro usuário.  
  
**Importante**  
O usuário destino deverá ter permissão para receber a pendência.   
**Exemplo**: Se a pendência for de elaboração, o usuário destino deve pertencer ao departamento e cargo que possui esta permissão. A configuração de permissão é realizada na rotina **QDOA020 - Cadastro de Tipo de Documento** por meio do botão **Outras Ações > Respons**.   
  
**Saiba mais**Para mais informações acesse a documentação: [Manufatura - Linha Protheus - SIGAQDO - Transferência de pendências para um novo usuário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021357911-MP-QUA-Transfer%C3%AAncia-de-pend%C3%AAncias-para-um-novo-usu%C3%A1rio?source=search)
