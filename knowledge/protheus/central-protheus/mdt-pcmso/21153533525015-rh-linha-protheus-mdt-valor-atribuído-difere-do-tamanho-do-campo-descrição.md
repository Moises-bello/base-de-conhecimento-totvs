---
article_id: 21153533525015
category: MDT - PCMSO
content_hash: 814115f542be1d3308b8c634d9a4f96b4abb2c071ab901bc4df989708a465a08
fetched_at: '2026-06-28T22:44:28.563591+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Valor atribuído difere do tamanho do campo Descrição
type: support-article
updated_at: '2025-09-03T14:15:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21153533525015-RH-Linha-Protheus-MDT-Valor-atribu%C3%ADdo-difere-do-tamanho-do-campo-Descri%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21153533518743) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao acessar a rotina de **Exames do Func**. (*MDTA120*) está apresentando a mensagem "Valor atribuído difere do tamanho do campo Descrição". O que avaliar?  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**A mensagem de erro ocorre por existir divergência entre o tamanho dos campos "**Resultado**" (**TMU\_RESULT)** e **(TM5\_RESULT)**  
  
**Solução**Alterado no compatibilizador o tamanhos dos campos para 50 e ajustado o fonte para que possa ser selecionado qualquer resultado de exame e não apresente problema.  
É necessário atualizar o dicionário em: [Expedição Contínua - Medicina e Segurança do Trabalho](https://tdn.totvs.com/pages/releaseview.action?pageId=557350060)  
A melhoria só estará disponível a partir da publicação do Pacote de Expedição Contínua data igual ou superior a 26/01/2024.  
  
Para fazer o processo de ajuste dos campos manualmente, é necessário seguir a FAQ: [MDT0130 Tamanho dos Campos TMU\_RESULT e TM5\_RESULT](https://tdn.totvs.com/display/public/PROT/MDT0130+Tamanho+dos+Campos+TMU_RESULT+e+TM5_RESULT)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
