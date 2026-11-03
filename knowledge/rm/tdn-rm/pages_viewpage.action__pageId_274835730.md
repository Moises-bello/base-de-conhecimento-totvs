---
content_hash: 16ddd28e051841dee5ca5b346630bbd112b34f5d30b6206017322fdbb10f98de
fetched_at: '2026-06-29T00:08:34.715590+00:00'
page_id: '274835730'
product: rm
source: tdn-rm
title: Envio de Usuários/Perfis Sob Demanda
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274835730
version: 8
---

# Envio de Usuários/Perfis Sob Demanda

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.17 |
| **Ambiente:** | RM.exe |
| **Passo a passo:** | **Objetivo:**  Ensinar como executar o envio de usuários e perfis sob demanda para o Fluig Identity.  **Introdução:**  O Processo de envio sob demanda tem como objetivo enviar para o Fluig IDENTITY **somente** os Usuários e Perfis selecionados que **cumprirem** o pré requisito de integração.   |  |  | | --- | --- | | **Item** | **Pré requisitos de integração** | | Usuário | Estar ativo e possuir e-mail configurado | | Perfil | Estar ativo |  Envio sob demanda de Usuário Acesse o cadastro de Usuário em menu "Serviços Globais | Segurança | Acesso | Usuários".    Selecione os usuários que serão enviados para o Identity e acesse a opção "Processo | Sincronizar Usuário com o Identity", e aguarde a conclusão do processo.    Depois de finalizado o processo caso a coluna "integrado" possua o ícone do fluig( ) significa que o usuário foi integrado.   Observação O processo de envio sob demanda de **usuário** funciona com os tipos de integração abaixo de acordo com o tipo de integração utilizada.   | Tipo de Integração | Comportamento | | --- | --- | | **Obrigatória / Opcional** | Envia o usuário e todas as suas associações de perfis | | **Somente SSO Obrigatória / Opcional** | Envia somente o usuário |   No caso do tipo **Obrigatória e Opcional** para que as permissões sejam enviadas é necessário que os perfis associados ao usuário **estejam** integrados com o identity. Envio sob demanda de Perfil Acesse o cadastro de Perfis em menu "Serviços Globais | Segurança | Acesso | Perfis".    Selecione os perfis que serão enviados para o Identity e acesse a opção "Processo | Sincronizar Perfil com o Identity", e aguarde o fim do processo.    Finalizado o processos caso a coluna "integrado" possua o ícone do fluig( ) significa que o perfil foi integrado.     Observação O processo de envio sob demanda de **perfil** funciona **somente** com o tipos de integração abaixo.   | Tipo de Integração | Comportamento | | --- | --- | | **Obrigatória / Opcional** | Envia o perfil e todas as suas permissões | |
| **Observações:** |  |
