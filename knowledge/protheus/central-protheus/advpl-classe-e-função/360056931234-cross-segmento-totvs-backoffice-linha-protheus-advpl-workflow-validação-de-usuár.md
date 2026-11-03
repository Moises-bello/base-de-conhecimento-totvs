---
article_id: 360056931234
category: ADVPL - Classe e Função
content_hash: b27386c4b4b13cbbd2969dfd311c8320869b8f5a2436134b16374c3939e9f7a2
fetched_at: '2026-06-28T22:40:18.243253+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - WorkFlow: Validação
  de usuário'
type: support-article
updated_at: '2022-04-25T17:09:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056931234-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-WorkFlow-Valida%C3%A7%C3%A3o-de-usu%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como validar o usuário dentro do WorkFlow?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas as versões.  
  
**Solução**O retorno do Workflow, por comportamento padrão não retorna usuário, por esse motivo a função **RetCodUsr()** ou a variável global **cUser**, não terão valor nas validações, mesmo utilizando a função **[WFPREPENV](https://tdn.totvs.com/pages/viewpage.action?pageId=240980281).**Uma alternativa seria abrir uma nova thread fora do processo do **Workflow** e preparar o ambiente para realizar o processo desejado, porém será necessário passar valores fixos de usuário e senha no fonte em questão, o que não é uma boa pratica.  
A rotina pode ser implementada conforme as documentações do [**schedule**,](https://tdn.totvs.com/pages/viewpage.action?pageId=271167961) utilizando a função estática **scheddef.** Com isso o ambiente já se encontrará aberto, não existindo a necessidade de abrir o mesmo com RpcSetEnv.  
  
**Saiba Mais**  
[TWFProcess](https://tdn.totvs.com/display/public/PROT/TWFProcess)  
[Documentação de Configuração do Workflow](https://tdn.totvs.com/display/public/PROT/WF0006_Configurando_e_ativando_o_Scheduler_do_Workflow)  
[Schedule - Como agendar a execução de rotinas](https://tdn.totvs.com/pages/viewpage.action?pageId=271167961)
