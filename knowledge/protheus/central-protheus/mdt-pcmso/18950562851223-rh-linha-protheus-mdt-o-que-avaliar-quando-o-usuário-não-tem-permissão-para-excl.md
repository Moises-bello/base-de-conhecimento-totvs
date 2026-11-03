---
article_id: 18950562851223
category: MDT - PCMSO
content_hash: 239ffc699195a8e5891306b951fd43c8812c8e2359e4c85f2cca37054489f94b
fetched_at: '2026-06-28T22:44:28.253161+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - O que avaliar quando o usuário não tem permissão
  para excluir um exame
type: support-article
updated_at: '2025-09-03T13:47:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18950562851223-RH-Linha-Protheus-MDT-O-que-avaliar-quando-o-usu%C3%A1rio-n%C3%A3o-tem-permiss%C3%A3o-para-excluir-um-exame
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18950531653271) Tempo aproximado para leitura: **00:03:00min** **Dúvida**O que avaliar quando o usuário não tem permissão para excluir um exame?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Este erro pode ocorrer em duas situações:  
  
**1.** Se o usuário não possuir todas as **permissões de acesso a rotina no configurador do Protheus**.  
  
![usuario.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18951622171415)  
  
Para realizar a verificação das permissões liberadas ao usuário acesse o Configurador **(SIGACFG)**, localize o cadastro do usuário, no seguinte caminho: **Usuário > Senhas**> **Usuários**posicione no usuário e clique em **alterar.  
  
A.**Posicione na opção Restrição de Acesso, verifique na **ABA FILIAIS**, se o usuário possui acesso a todas as filiais envolvidas na avaliação dos riscos.  
  
**B.**Posicione na opção  Restrição de Acesso, verifique na **ABA AMBIENTES**,  certifique-se que o usuário possui acesso ao módulos relacionados.  
  
**C.**Ainda na **ABA AMBIENTES,**posicione no Módulo **SIGAMDT** (35) clique em **Outras Ações > Restrição de rotina do Menu,**certifique-se que o usuário possui liberação para a rotina de exames.  
  
**D.** Na **ABA ACESSOS,** verifique se a opção **"Excluir Cadastros"** esta marcada.  
  
![ExamesExcluir.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18950546894231)  
  
**2.** Se o **usuário estiver logado na Filial diferente do cadastro do exame**. Exemplo usuário esta logado na filial 01 e o exame esta cadastrado na filial 02, ao tentar alterar o exame na filial diferente de sua criação será apresentado a mensagem.   
  
Solução para este cenário deverá logar na filial onde o exame foi cadastrado, somente assim será possível realizar sua alteração, se necessário.   
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
