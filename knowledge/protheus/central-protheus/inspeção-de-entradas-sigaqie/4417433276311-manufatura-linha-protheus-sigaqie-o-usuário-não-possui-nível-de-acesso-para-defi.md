---
article_id: 4417433276311
category: Inspeção de Entradas (SIGAQIE)
content_hash: c154736b92df6a66b56d84518c95c017358efc468b3a1de83d914dbe8c22f2f5
fetched_at: '2026-06-28T22:42:27.113096+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - O usuário não possui nível de acesso
  para definir o Laudo Final de Entrada
type: support-article
updated_at: '2022-01-10T11:16:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417433276311-Manufatura-Linha-Protheus-SIGAQIE-O-usu%C3%A1rio-n%C3%A3o-possui-n%C3%ADvel-de-acesso-para-definir-o-Laudo-Final-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:07 min****Ocorrência**No módulo **SIGAQIE - Inspeção de Entradas**, ao realizar a inspeção de resultado por meio da rotina **QIEA215 - Resultados** é exibida a mensagem **O usuário não possui nível de acesso para definir o Laudo Final da Entrada**.  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Causa**A mensagem é exibida quando o usuário que está realizando a inspeção não possui o acesso **100 - Def Laudo Final Entrega** marcado no cadastro do usuário no **SIGACFG - Configurador**.  
  
**Solução**Para solucionar esse *help*, realize os seguintes passos:  
1. Acesse o **SIGACFG**;  
2. No menu **Usuário/Senhas/Usuários** selecione o usuário em questão;  
3. Clique em **Alterar**;  
4. Na aba **Restrições de Acessos/Acessos** marque a opção **100 - Def Laudo Final Entrega**;  
5. **Confirme** esta alteração e realize novo teste.
