---
article_id: 360057151373
category: RH - Funcionários
content_hash: 1c92bde5eb444fd37d021e768ad9298ce888e276c0878d94357149418a400efe
fetched_at: '2026-06-28T22:43:27.632453+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como permitir que um usuário tenha acesso apenas
  a Funcionários Demitidos
type: support-article
updated_at: '2025-08-13T17:42:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057151373-RH-Linha-Protheus-GPE-Como-permitir-que-um-usu%C3%A1rio-tenha-acesso-apenas-a-Funcion%C3%A1rios-Demitidos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34157891751191) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como permitir que um usuário tenha acesso apenas a Funcionários Demitidos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para permitir que o usuário tenha acesso apenas as informações de funcionários demitidos, execute o seguinte procedimento:

1. Cadastrar um Usuário no SIGACFG - Usuários/Senhas/Usuário:  
   ![](https://tdn.totvs.com/download/attachments/235569727/image2016-7-11%2017%3A55%3A28.png?version=1&modificationDate=1468270528000&api=v2)  
   ![](https://tdn.totvs.com/download/attachments/235569727/image2016-7-11%2017%3A56%3A12.png?version=1&modificationDate=1468270572000&api=v2)  
   ![](https://tdn.totvs.com/download/attachments/235569727/image2016-7-11%2017%3A57%3A24.png?version=1&modificationDate=1468270644000&api=v2)  
   ![](https://tdn.totvs.com/download/attachments/235569727/image2016-7-11%2017%3A58%3A54.png?version=1&modificationDate=1468270733000&api=v2)
2. No SIGAGPE em Atualizações/Cadastros/Contr. Acess. Usuário, informe o código do usuário, a tabela SRA no campo Arquivo e configure da seguinte forma os campos Filtro Browse e Filtro Relatório:  
     
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095931013)  
     
   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095931133)  
     
   Neste procedimento está definido que o usuário bruno só terá acesso quando os funcionários estiverem com o campo Sit. Folha com D ou seja, demitidos. Caso tenha mais usuários para configurar, deve fazer o mesmo processo para eles.

**Saber Mais:**

[RH - Linha Protheus - GPE - Restringir acesso de usuário a determinada rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059006033-RH-Linha-Protheus-GPE-Restringir-acesso-de-usu%C3%A1rio-a-determinada-rotina?source=search)

[RH- Linha Protheus - GPE - Ao visualizar Cadastros de funcionários após aplicar a Restrição de Acesso ao Grupo de Usuário 192 - Dados Pessoais é Gerado ErrorLog - array out of bounds [3] of [0] on MSMGET:NEW(MSMGETPR.PRW)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059251933-RH-Linha-Protheus-GPE-Ao-visualizar-Cadastros-de-funcion%C3%A1rios-ap%C3%B3s-aplicar-a-Restri%C3%A7%C3%A3o-de-Acesso-ao-Grupo-de-Usu%C3%A1rio-192-Dados-Pessoais-%C3%A9-Gerado-ErrorLog-array-out-of-bounds-3-of-0-on-MSMGET-NEW-MSMGETPR-PRW-?source=search)

[RH - Linha Protheus - GPE - Configuração para que determinados usuários possam visualizar ou não um campo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059356113-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-para-que-determinados-usu%C3%A1rios-possam-visualizar-ou-n%C3%A3o-um-campo?source=search)
