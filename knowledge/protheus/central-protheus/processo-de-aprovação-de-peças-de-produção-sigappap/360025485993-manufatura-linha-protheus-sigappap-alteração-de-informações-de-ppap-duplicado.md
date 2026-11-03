---
article_id: 360025485993
category: Processo de Aprovação de Peças de Produção (SIGAPPAP)
content_hash: c52ca7774582322ef5138c8b535775bcb21102a9998d4446da55c48023af4a2b
fetched_at: '2026-06-28T22:42:24.097358+00:00'
product: protheus
section_id: 360005876714
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPPAP - Alteração de informações de PPAP duplicado
type: support-article
updated_at: '2021-09-08T12:58:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025485993-Manufatura-Linha-Protheus-SIGAPPAP-Altera%C3%A7%C3%A3o-de-informa%C3%A7%C3%B5es-de-PPAP-duplicado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:40 min**  
**Ocorrência**Na rotina **Diagrama de Fluxo - QPPA150**, ao tentar alterar um registro, é apresentada a mensagem **O usuário logado não é o aprovador/responsável, para alteração deverá estar logado com o usuário aprovado.**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) – Processo de Aprovação de Peças de Produção (SIGAPPAP) – Todas as versões  
  
**Causa**Esta mensagem ocorre quando o **PPAP - Processo de Aprovação de Peças de Produção** é duplicado por meio da rotina **Duplica PPAP - QPPM020** e o mesmo já estava aprovado antes da duplicação.   
  
O conceito desta rotina é que quando o parâmetro **Todo PPAP?** da tela de parâmetro da rotina **QPPM020**estiver como **Sim**, os demais parâmetros são desconsiderados e será duplicado todo o processo, incluindo a aprovação realizada na rotina **QPPA150**.  
  
Se estiver parâmetro **Todo PPAP?**estiver como **Não**, mas o parâmetro **Diagrama de Fluxo?**como **Sim**, irá acontecer o mesmo cenário, pois se já houve aprovação do processo utilizado como base para cópia, este novo processo também já estará aprovado. Desta forma, apenas o usuário aprovador poderá realizar alterações no **PPAP** que foi duplicado.  
  
**Solução**Quando o usuário que fez a duplicação é diferente do usuário que aprovou o diagrama, é necessário executar os passos a abaixo para que o mesmo consiga alterar o registro:  
1. Acessar a rotina **QPPA150** com o usuário que aprovou o diagrama;  
2. Selecionar o diagrama e clicar em **Alterar**;  
3. Acessar o botão **Outras Ações** > **Apro/Des**.  
  
**Importante**  
Após executar os passos acima, o diagrama será **desaprovado** e ficará disponível para alteração para qualquer usuário, incluindo o usuário que duplicou o processo.
