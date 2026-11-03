---
article_id: 360035900234
category: TAF - REINF
content_hash: b427ed2f1b19c5d30c6a6ce5503e1b45a92d7241051d8d34abb4d4e4091d11a7
fetched_at: '2026-06-28T22:41:34.858634+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Retificação de Eventos
  - Apuração dos eventos
type: support-article
updated_at: '2024-10-02T12:28:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035900234-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Retifica%C3%A7%C3%A3o-de-Eventos-Apura%C3%A7%C3%A3o-dos-eventos
---

**Dúvida**

Como realizar a retificação de eventos da Reinf?  
  
**Ambiente**

TAF - A partir da 12.1.17  
  
**Solução**

 Para realizar uma retificação de um período, é necessário avaliar que tipo de retificação será realizada e se o período está fechado.

Vamos tomar como exemplo o evento R-2010.

Se o período estiver fechado, verifique a **etapa 1**.

Caso o processo de retificação envolva a inclusão de notas, verificar a **etapa 2**.

Caso a retificação envolva somente alteração de notas já transmitidas, verifique a **etapa 3**.

Caso a retificação envolva**exclusão** de notas transmitidas, verifique a **etapa 4.**

**OBS: Caso a retificação envolva alteração de uma nota, não é necessário enviar o evento de exclusão. Aconselhamos a utilizar a exclusão do Evento nos casos em que uma nota foi transmitida indevidamente para a Receita.**

**Etapa 1**

Para retificar um período que se encontra fechado, é necessário realizar a reabertura do mesmo. Para isso, siga o procedimento a seguir:

[TAF - REINF - Evento R-2098 - Reabertura dos Eventos Periódicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027865891-TAF-REINF-Evento-R-2098-Reabertura-dos-Eventos-Peri%C3%B3dicos?source=search)

**Etapa 2**

Quando o período já estiver em aberto, é preciso incluir o documento no TAF que será transmitida para a Receita.

Após a inclusão do documento no card do evento no painel REINF o participante do documento incluído ou integrado ficará pendente para nova, apuração e transmissão.

**Etapa 3**

Caso a retificação envolva alterar informações de notas já transmitidas, acessar o menu Atualizações > Movimentos Reinf > Localize o documento deseja, faça o ajuste e salve a alteração.

Após salvar o evento terá o participante habilitado para no apuração no Painel REINF.

Para que não ocara erro na nova apuração é preciso que as transmissões anterior esteja como autorizada, caso gere um alerta de apuração cancelada, siga a documentação abaixo.

[Cross Segmentos - Backoffice Protheus - TAF - REINF -A apuração foi cancelada pois este registro já foi transmitido e está aguardando retorno do RET, portanto não pode ser modificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18995363632663-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-A-apura%C3%A7%C3%A3o-foi-cancelada-pois-este-registro-j%C3%A1-foi-transmitido-e-est%C3%A1-aguardando-retorno-do-RET-portanto-n%C3%A3o-pode-ser-modificado)

**Etapa 4**

Avalie a documentação abaixo:

[Cross Segmentos - Backoffice Protheus - TAF - REINF - Como gerar o evento R-9000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6174451916951-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-gerar-o-evento-R-9000?source=search)

OBS: Nos casos em que, por exemplo, um CNPJ possua 20 notas, sendo que dessas 20 transmitidas, 1 nota foi erroneamente, será necessário enviar o R-9000 desse CNPJ, excluir a nota do TAF e após, realizar a apuração e transmissão novamente do R-2010.

Nesse cenário acima, a apuração só irá habilitar novamente para esse CNPJ após o envio do R-9000, quando alguma das 19 notas forem 'alteradas', ou seja, ao acessar uma das notas dentro do TAF e efetuar uma alteração (seja digitando alguma informação novamente), para o TAF entender que deve ser transmitido novamente esse CNPJ.

Caso haja alguma dúvida no processo de Retificação, entre em contato com a Equipe TOTVS.
