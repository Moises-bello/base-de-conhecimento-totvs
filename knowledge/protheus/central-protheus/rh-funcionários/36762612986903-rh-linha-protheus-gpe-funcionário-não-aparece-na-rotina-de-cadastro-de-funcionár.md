---
article_id: 36762612986903
category: RH - Funcionários
content_hash: 12d11d5f43c24718192f35556268f0fe4d57157a86962c9b075a1212b37d87dc
fetched_at: '2026-06-28T22:43:28.505025+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionário não aparece na rotina de Cadastro de
  Funcionários (GPEA010)
type: support-article
updated_at: '2025-12-04T12:01:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36762612986903-RH-Linha-Protheus-GPE-Funcion%C3%A1rio-n%C3%A3o-aparece-na-rotina-de-Cadastro-de-Funcion%C3%A1rios-GPEA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36762644882839) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao realizar um cadastro de um novo funcionário, o cadastro não é localizado na rotina de Funcionário (GPEA010)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões  
  
**Causa**  
Funcionário foi cadastrado com a categoria **A - Autônomo ou P - Pró-Labore**  
  
**Solução**  
Se não localizar o cadastro de um funcionário acessando a rotina **GPEA010** pelo caminho **Atualizações > Funcionários > Funcionários**, é provável que este funcionário foi cadastrado com a **categoria de Autônomo ou Pró-labore**, e não como Mensalista.   
  
Para confirmar, acesse a rotina de **Contribuinte Individual (GPEA265)** pelo caminho **Atualizações > Funcionários > Contr. Individual** e verifique se o cadastro existe na rotina.   
  
Se o cadastro for encontrado nesta rotina e a categoria estiver incorreta (ou seja, ele deveria ser um mensalista), será necessário excluir o cadastro existente e realizar um novo cadastro. Isso é necessário porque o sistema **não permite alterar a categoria de Autônomo/Pró-labore para Mensalista.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36763273971351)

Para excluir o cadastro, posicione na matrícula desejada, vá em **Outras Ações > Excluir**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36763273972631)  
  
Verifique[**esta documentação**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051741233-RH-Linha-Protheus-GPE-Como-excluir-o-cadastro-de-um-Funcion%C3%A1rio) com mais informações de como excluir o cadastro de um funcionário.

**Obs.:** Na rotina de **Gestão de Funcionários (**Atualizações > Funcionários > Gestão de Funcionários) é possível visualizar o cadastros de todas as categorias

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36763258980631)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Documentações relacionadas ao cadastro de funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11311670958615-RH-Linha-Protheus-GPE-Documenta%C3%A7%C3%B5es-relacionadas-ao-cadastro-de-funcion%C3%A1rios)
