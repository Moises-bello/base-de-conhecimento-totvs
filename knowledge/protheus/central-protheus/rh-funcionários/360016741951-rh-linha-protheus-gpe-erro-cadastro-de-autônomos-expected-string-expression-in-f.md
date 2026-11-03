---
article_id: 360016741951
category: RH - Funcionários
content_hash: dc8c7262e210473435ea1793fa78467391458375e4f656c1ef7bb86d45466ac7
fetched_at: '2026-06-28T22:43:27.727705+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: 'RH - Linha Protheus - GPE - Erro cadastro de Autônomos: expected string expression
  in FieldPut RA_CARGO'
type: support-article
updated_at: '2025-05-07T22:26:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016741951-RH-Linha-Protheus-GPE-Erro-cadastro-de-Aut%C3%B4nomos-expected-string-expression-in-FieldPut-RA-CARGO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257596055) Tempo aproximado para leitura: 00:02:00 min  
  
Ocorrência**Ao tentar realizar inclusão de **Autônomos** é apresentado o erro ***expected string expression in FieldPut RA\_CARGO***.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O erro ocorre devido **gatilho de campos incorretos na estrutura.**  
  
**Solução**Para ajuste, siga os passos abaixo:1 - Acesse o cadastro de **Gatilhos** através do **Configurador > Base de Dados > Dicionário > Gatilhos >** localize os gatilhos associados ao campo **RA\_CODFUNC** e valide se existem os registros conforme imagem:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257597719)

**2 -** Compare a quantidade e os valores dos gatilhos encontrados com os registros padrão. **Se estiver faltando algum gatilho ou algum valor estiver diferente**, altere para o padrão do sistema:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257598359)​​  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257598871)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947302634903)  
​![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257599511)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257599767)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947302637335)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947302638359)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257603095)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257604503)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257605783)

> TabSalIni(M->RA\_TABELA,M->RA\_ADMISSA,.f.,M->RA\_TABNIVE,M->RA\_TABFAIX)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257606679)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257607575)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31947257609239)   
  
  
**Saiba Mais:**  
[RH - Linha Protheus - GPE - Como cadastrar um Autônomo ou Pró-labore](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052067393-RH-Linha-Protheus-GPE-Como-cadastrar-um-Aut%C3%B4nomo-ou-Pr%C3%B3-labore)  
[RH - Linha Protheus - GPE - Como configurar os campos que serão apresentados no cadastro de Autônomos/Contribuinte Individual](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360009855832-RH-Linha-Protheus-GPE-Como-configurar-os-campos-que-ser%C3%A3o-apresentados-no-cadastro-de-Aut%C3%B4nomos-Contribuinte-Individual)
