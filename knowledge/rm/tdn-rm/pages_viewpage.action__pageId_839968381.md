---
content_hash: 8caf3b2db2126a31b00ff247fe26ccd78c6f8291824cbce3db3107985a51b60e
fetched_at: '2026-06-29T00:11:50.280083+00:00'
page_id: '839968381'
product: rm
source: tdn-rm
title: Ativação da integração com o SmartLink
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=839968381
version: 17
---

# **Índice**

---

Índice

# **Informações**

---

Este documento tem como objetivo instruir sobre a ativação da integração do RM com o SmartLink.

Apesar de utilizar a mesma tela, o *Wizard do Credential Helper*, este documento foca na configuração inicial de ambientes. Caso enfrente problemas com a integração, e seu intuito seja de reparar a integração, *acesse a documentação: [Solução de conflitos](https://tdn.totvs.com/x/kucxPw)*.

Ativação automática

A critério da TOTVS, alguns clientes tem a ativação com o SmartLink de seu ambiente feita de forma automática. Nestes casos, não é necessário seguir este processo.

Para verificar se a sua integração já está ativa, basta acessar a *[Tela de diagnóstico da integração com o SmartLink](https://tdn.totvs.com/x/YcnLPQ)*.

Observação

A tela de *Ativação SmartLink* é uma tela do produto do SmartLink. Qualquer mau funcionamento desta tela deve ser direcionado a equipe responsável do SmartLink.

Documentação da equipe do SmartLink sobre a funcionalidade:

# **Ativação**

---

O menu de ativação da integração SmartLink está localizado em: **Módulo Integração >> Totvs App >> Integração com Smart Link**.

Para acessar esta tela, é necessário que o usuário do RM seja **supervisor** do módulo de **Serviços Globais**.

A tela a seguir abrirá em seu RM:

Ao clicar em **iniciar**, será dada a opção para nomear a sua instalação. Esta instalação estará vinculada ao seu banco de dados.

Ao avançar, clicando em Próximo, será solicitado um nome para o ambiente a ser criado.

Importante ressaltar que o Tipo do ambiente (que, neste exemplo, está como Produção) é definido pelo tipo de ambiente do seu RM. Não é possível migrar um ambiente de Produção para Homologação, e vice-versa.

Ao inserir o nome do ambiente, e clicar em Criar e gerar credenciais, o processo de criação de ambientes começará.

Este processo pode durar por **vários minutos**. No entanto, é importante manter a tela aberta.

Após a conclusão da criação do ambiente, a tela a seguir será exibida.

É importante copiar os campos *Client ID* e *Client Secret*, pois são as credenciais que podem ser utilizadas em integrações.

É necessário clicar em **Finalizar**, antes de fechar a aba. O fechamento prematuro desta aba impedirá a integração do RM com o ambiente criado.

Após clicar em **Finalizar**, finalmente a configuração vai ter sido concluída, e a aba pode ser fechada.

# **Resultado**

---

Após a finalização deste processo, a integração deve estar ativa. É possível verificar isso acessando a tela de diagnóstico da integração. *Acessar a documentação: [Tela de diagnóstico da integração com o SmartLink](https://tdn.totvs.com/x/YcnLPQ)*.
