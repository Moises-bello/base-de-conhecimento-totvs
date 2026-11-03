---
content_hash: 9ca3423a2e9b1bd433cc1abc0e6aabc55260457a635197350059b67e70bd264b
fetched_at: '2026-06-29T00:10:31.901563+00:00'
page_id: '525011767'
product: rm
source: tdn-rm
title: Termo de Consentimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Termo+de+Consentimento
version: 11
---

Esta funcionalidade permite obter o consentimento do usuário do portal do aluno para o uso de seus dados pessoais e sensíveis e o uso de cookies nos dispositivos acessados pelo mesmo.

Atenção

Esta funcionalidade está disponível a partir da versão 12.1.27.

## Parametrização

Para configurar esta funcionalidade, basta acessar os parâmetros do **Educacional** e ir em **RM Portal** >> **RM Portal -Gerais** e avançar até a etapa abaixo.

Os relatórios de: Política de Privacidade e Política de utilização de cookies, deverão ser confeccionados pela Instituição de ensino.  
Obs: Na criação do relatório, não é necessário passar nenhuma condição de filtro, para que o mesmo seja exibido na parametrização dos termos de consentimento.

Nesta etapa, é possível:

* habilitar a solicitação do aceite dos termos de consentimento no portal do aluno, marcando a opção **Solicitar aceite de termos de consentimento.**
* configurar o relatório utilizado para a Política de Privacidade e sua versão, preenchendo os campos **Política de Privacidade** e **Versão política de privacidade**.
* configurar o relatório utilizado para a Política de utilização de cookies e sua versão, preenchendo os campos **Política de Utilização de Cookies** e **Versão política de utilização de cookies**.
* configurar o texto do termo de consentimento exibido no portal através do campo **Termo de Consentimento Portal**.

```

```

Caso haja alguma inconsistência nas configurações dos relatórios dos termos de aceite, a seguinte mensagem será exibida informando quais relatórios estão com as configurações inconsistentes:

Para corrigir a configuração dos relatórios é necessário vincular novamente o(s) relatório(s) na tela de configurações e salvar as configurações com a finalização do parametrizador.

## Como o termo de consentimento será exibido?

Após realizar o login e selecionar o contexto no portal do aluno, será exibido uma janela onde o usuário poderá visualizar os relatórios definidos na parametrização e efetuar o aceite. Os relatório utilizados no exemplo abaixo são meramente ilustrativos, e cabe a cada Instituição redigir os seus termos.

Ao clicar no link do relatório, caso haja alguma inconsistência na configuração dele que impeça que ele seja disponibilizado, a seguinte mensagem será exibida informando esta situação  e solicitando ao usuário para entrar em contato com a instituição:

O aceite dos termos de consentimento é obrigatório para o uso do portal do aluno. Sendo assim, se o usuário não conceder o aceite aos termos, ele será redirecionado para a tela de login e não poderá utilizar o portal.
