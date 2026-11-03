---
article_id: 39745116154903
category: Meu RH - Férias
content_hash: 45be47ec21051b44f03129a6fb4a493056843a1193f9f09a3e668264b971de51
fetched_at: '2026-06-28T22:47:31.574246+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: 'RH - RM - Meu RH - Erro ao solicitar férias: A Marcação de férias está desabilitada'
type: support-article
updated_at: '2026-04-14T20:50:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39745116154903-RH-RM-Meu-RH-Erro-ao-solicitar-f%C3%A9rias-A-Marca%C3%A7%C3%A3o-de-f%C3%A9rias-est%C3%A1-desabilitada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39745109150359) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao realizar solicitação de férias pelo Meu RH, é apresentado a mensagem de erro: **"A Marcação de férias está desabilitada".**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Este problema ocorre, quando o parâmetro "**Desabilitar marcação de férias**" está marcado no grupo de Quiosque dos funcionários.  
  
**Solução**  
Para liberar a solicitação de férias no Portal, acesse o módulo **Folha de pagamento** > **Configurações** > **Parametrizador** > **RM Portal** > Edite o quiosque dos funcionários > **Férias**. Desmarque o parâmetro "**Desabilitar marcação de férias**".

![image.png](https://totvssuporte.zendesk.com/attachments/token/YsD6JE6TQrsmfJMhloj3FsZSz/?name=image.png&lotus_request=true)

**Importante:** Caso possua mais de um Grupo de Quiosque, exemplo um para funcionários e outro para gestores, é necessário realizar a conferência de ambos os grupos e desmarcar este parâmetro. Para identificar qual o grupo de quiosque está vinculado, acesse o cadastro do funcionário e na aba **Identificação** confira o campo **"Código do grupo de Quiosque".**

**Saiba mais**  
[**RH - RM - Meu RH - Como desabilitar a Sugestão de Férias do Meu RH e manter o acesso ao recibo de férias**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058188054-RH-RM-Meu-RH-Como-desabilitar-a-Sugest%C3%A3o-de-F%C3%A9rias-do-Meu-RH)
