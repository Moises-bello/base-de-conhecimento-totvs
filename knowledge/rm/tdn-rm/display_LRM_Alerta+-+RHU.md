---
content_hash: 33301460f4c77cff52f7b0ef015dcb283d1bf80b840950c8381460dbe81ccbc0
fetched_at: '2026-06-29T00:10:00.975140+00:00'
page_id: '452718660'
product: rm
source: tdn-rm
title: Alerta - RHU
type: documentation
url: https://tdn.totvs.com/display/LRM/Alerta+-+RHU
version: 3
---

**Alerta**

Neste anexo será possível cadastrar um alerta para cada tipo de requisição existente no TOTVS Gestão de Pessoas. O alerta será disparado na criação das requisições, no TOTVS Gestão de Pessoas ou no Totvs Portal.

**Procedimento**:

O usuário deverá editar o tipo de requisição desejado, acessar Anexos| Alerta para efetuar a configuração do alerta.

Campos a serem preenchidos:

**Consulta SQL**: A condição para disparar o alerta será configurada em uma consulta SQL, previamente cadastrada. A consulta SQL deverá retornar obrigatoriamente a CHAPA e a COLIGADA do funcionário.

**Tipo -** Os campos ALERTA e RESTRIÇÃO indicam se o alerta será apenas informativo para o usuário, ou se impedirá a criação da requisição, caso o funcionário seja retornado na consulta SQL, respectivamente.

**Mensagem -** No campo mensagem o usuário irá inserir o texto que será exibido para o usuário ao criar uma requisição, caso o alerta seja disparado.

*Exemplo de uma consulta SQL que valida se o funcionário está de férias:*

*SELECT CODCOLIGADA, CHAPA FROM PFUNC (NOLOCK) WHERE CODCOLIGADA = :CODCOLIGADA AND CHAPA = :CHAPA AND CODSITUACAO = 'F'*
