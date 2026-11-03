---
article_id: 1500000358881
category: MDT - PPRA
content_hash: cae92b312ca2b6d4671a5cd38f48b845313736a55d375f0dade20dfb64143a54
fetched_at: '2026-06-28T22:44:27.239050+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: RH - Linha Protheus - MDT - Ao acessar a rotina de risco (MDTA180) apresenta
  a mensagem HELP SEMPERM Problema Usuário sem permissão para utilizar esta rotina
type: support-article
updated_at: '2025-07-31T14:27:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000358881-RH-Linha-Protheus-MDT-Ao-acessar-a-rotina-de-risco-MDTA180-apresenta-a-mensagem-HELP-SEMPERM-Problema-Usu%C3%A1rio-sem-permiss%C3%A3o-para-utilizar-esta-rotina
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20002990147991)** Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao acessar a rotina de Riscos (MDTA180), está aparecendo a mensagem - HELP: SEMPERM.   
Problema: Usuário sem permissão para utilizar esta rotina. Solução: Solicite permissão ao Administrador do Sistema.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000404241)  
 **Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Este erro pode ocorrer em duas situações:  
  
**1.** Se o usuário não possuir todas as **permissões de acesso a rotina**.  
Para realizar a verificação das permissões liberadas ao usuário acesse o Configurador **(SIGACFG)**, localize o cadastro do usuário, no seguinte caminho: **Atualizações > Usuários > Senhas**> posicione no usuário e clique em **alterar.   
  
A.** Posicione na opção Restrição de Acesso, verifique na **ABA FILAIS**, se o usuário possui acesso a todas as filiais envolvidas na avaliação dos riscos.  
  
**B.** Posicione na opção  Restrição de Acesso, verifique na **ABA AMBIENTES**,  certifique-se que o usuário possui acesso ao módulos relacionados.  
  
**C.** Ainda na **ABA AMBIENTES,**posicione no Módulo **SIGAMDT** (35) clique em **Outras Ações > Restrição de rotina do Menu,**certifique-se que o usuário possui liberação para as rotinas de risco.  
  
![ESK9nhJJBT.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000400602)  
  
**2.** Se o **usuário estiver logado na Filial, diferente do cadastro do risco**. Exemplo usuário esta logado na filial 01 e o risco esta cadastrado na filial 02, ao tentar alterar o risco na filial diferente de sua criação será apresentado a mensagem.   
  
Solução para este cenário deverá logar na filial onde o risco foi cadastrado, somente assim será possível realizar sua alteração, se necessário.   
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
