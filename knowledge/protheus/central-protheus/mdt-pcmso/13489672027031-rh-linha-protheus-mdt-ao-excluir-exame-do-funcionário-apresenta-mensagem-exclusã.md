---
article_id: 13489672027031
category: MDT - PCMSO
content_hash: bdcbd6fd96f9ccf7cadb4d0c983e445b5cde53b073dd1a4b9c79c32a08a19f61
fetched_at: '2026-06-28T22:44:28.277414+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Ao excluir exame do funcionário apresenta mensagem
  Exclusão não permitida
type: support-article
updated_at: '2025-09-03T14:21:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13489672027031-RH-Linha-Protheus-MDT-Ao-excluir-exame-do-funcion%C3%A1rio-apresenta-mensagem-Exclus%C3%A3o-n%C3%A3o-permitida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Ao excluir exame do funcionário é apresentado a mensagem "Exclusão não permitida". É possível excluir os exames?  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13489329654679)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as Versões  
  
**Solução**O sistema não irá permitir realizar a exclusão do exame se ele estiver vinculado a outra rotina, como por exemplo, Atestado ASO.  
  
Veja que no cadastro de Exames do Funcionário o campo "Num.ASO" contém informação e por ter relacionamento com outra rotina o sistema gera a mensagem.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13489427140503)  
  
Para retirar o vinculo é necessário acessar a rotina Atestado ASO (*Atualizações - Atendimento Médico - Atestado ASO*), localizar o registro e clicar no botão **Exames**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13489530978071)  
  
Será apresentado os exames relacionados e tire a seleção no exame que deseja excluir: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13489570865303)  
  
Ao retornar na rotina Exames do Funcionário o campo "Num.ASO" estará em branco e o sistema permite a exclusão:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13489670702615)  
  
**Observação**: É total responsabilidade da empresa em efetuar exclusão das informações, é necessário avaliar os impactos antes de excluir as informações.   
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos Sobre Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico)  
[Artigos sobre PCMSO](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945214-MDT-PCMSO)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
