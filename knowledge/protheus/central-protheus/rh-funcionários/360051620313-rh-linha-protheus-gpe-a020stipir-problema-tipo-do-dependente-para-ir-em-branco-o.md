---
article_id: 360051620313
category: RH - Funcionários
content_hash: a0dbd1a2702dabd38f884cb5c5bb35ceeb352f2037eff4b8b62970e10866708f
fetched_at: '2026-06-28T22:43:27.298679+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: 'RH - Linha Protheus - GPE - A020STIPIR Problema: Tipo do dependente para IR
  em branco ou inválido'
type: support-article
updated_at: '2025-08-20T17:33:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051620313-RH-Linha-Protheus-GPE-A020STIPIR-Problema-Tipo-do-dependente-para-IR-em-branco-ou-inv%C3%A1lido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31673113778839) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Ao efetuar a alteração de dependentes incluindo um novo, o Sistema emite mensagem que o IR está em branco ou inválido:

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078749494)**O campo **RB\_DTNASC** gatilha ano incorreto, quando ano é digitado com apenas 2 dígitos, o Sistema entende que o dependente nasceu em 1920.

Para que Sistema apresente os 4 dígitos referente ao ano de nascimento (2020), altere via Configurador em **Usuário > Senhas > Usuário** e ao localizar usuário, altere o número de dígitos conforme exemplo abaixo:   
  
![](https://totvssuporte.zendesk.com/attachments/token/P5k7efT18SroaSbcdWpQTwpA8/?name=inline1082020313.png)

Após procedimento realizado, acesse novamente a rotina **Atualizações > Funcionários > Dependentes** e preencha manualmente de acordo com as informações realizadas.

Sendo assim, para que os próximos lançamentos o Sistema não apresente a mensagem acima, e que o administrador não precise alterar novamente os dígitos via Configurador, a Release Oficial foi expedida e publicada na Central de Downloads.

O pacote pode ser acessado no endereço abaixo de acordo com a versão do cliente:  
<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO>

**Saiba Mais**:  
[RH - Linha Protheus - GPE - Cadastro de Dependentes "Tipo Dep. IR"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050880014-RH-Linha-Protheus-GPE-Cadastro-de-Dependentes-Tipo-Dep-IR)

[RH - Linha Protheus - GPE - Demonstração Dedução dependente na Base de IR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053938633-RH-Linha-Protheus-GPE-Demonstra%C3%A7%C3%A3o-Dedu%C3%A7%C3%A3o-dependente-na-Base-de-IR)

[RH - Linha Protheus - GPE - Como cadastrar dependente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411314686231-RH-Linha-Protheus-GPE-Como-cadastrar-dependente)
