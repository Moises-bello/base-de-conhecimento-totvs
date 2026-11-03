---
content_hash: 08e9f8abf0e0c7b9864e1312afc5c0ec279e34a8084b03120cef04f8291b9750
fetched_at: '2026-06-29T00:11:11.105152+00:00'
page_id: '645493629'
product: rm
source: tdn-rm
title: Reenviar Mensagens EAI
type: documentation
url: https://tdn.totvs.com/display/LRM/Reenviar+Mensagens+EAI
version: 8
---

**Objetivo**

Reenviar movimentos que, por algum motivo qualquer, não foram enviados para o Protheus.

**Disponibilidade**

Disponível a partir da versão 12.1.32 do RM.

**Atenção**:

Na versão 12.1.32, o menu com o processo de reenvio de mensagens só estará disponível se a base de dados estiver atualizada com o script do atualizador que habilita o parâmetro do tipo de movimento responsável por envio de mensagem de integração. (Deverá existir o campo CODTMVSOLICITACAONFSE na tabela TPAR - Código do script: NU.2021.06\_02).

**Pré-condições:**

Esse menu só estará visível para o usuário, se tiver alguma integração com o Protheus ativa para o **EAI 2.0.**

Na versão 12.1.32, além dessa condição, o script citado na seção "*Disponibilidade*" acima neste documento deverá ter sido executado. Caso queira utilizar a funcionalidade nessa versão e o menu não esteja aparecendo, deverá ser rodado o atualizador de base dados.

Para que o menu fique habilitado e a funcionalidade possa ser acessada, é necessário dar permissão no perfil do usuário: Gestão de Estoque, Compras e Faturamento → Integrações → Mensageria Única → Reenviar Mensagens EAI

Serão considerados para fins de processamento os movimentos que possuírem registro na tabela TMOVINTEGRACAOEAI conforme condições abaixo:

* Status do movimento cancelado: Se o movimento tiver cancelado (TMOV.STATUS = "C") e com status de integração da tabela TMOVINTEGRACAOEAI como "I" (Integrado), o processo irá disparar mensagem de exclusão (delete) para o Protheus.
* Status do movimento cancelado: Se o movimento **NÃO** estiver cancelado (TMOV.STATUS != "C") e tiver status de integração da tabela TMOVINTEGRACAOEAI diferente de "I" (Integrado), o processo irá disparar mensagem de inclusão / alteração para o Protheus.

**Descrição do funcionamento**

Criado um menu "Reenviar Mensagens EAI" dentro do grupo "Mensageria Única" responsável por executar o processo de reenvio de mensagens do **EAI 2.0**.

Usuário clicará nesse menu que exibirá um formulário de processo para que seja feito o filtro e processamento dos movimentos.

Os filtros considerados serão os mesmos filtros listados no filtro principal de movimentos.

Mesmo que sejam filtrados vários movimentos, desses movimentos filtrados, serão considerados somente os registros cujo tipo de movimento estiver parametrizado com algum valor diferente de "**Não integrado**" (Parâmetros do tipo de movimento → Integração Mensagem Única → Mensagem de Integração)

Após filtrar os registros, o usuário clicará no botão "Executar" que executará o processo de reenvio de mensagens EAI e mostrará o resultado do processamento dos registros no log do processo.

**Observações:**

O processo poderá trabalhar com fracionamento de jobs. Dúvidas com o funcionamento do fracionamento de jobs, consulte o link:   
<https://tdn.totvs.com/pages/viewpage.action?pageId=547231277>

A permissão para a funcionalidade no perfil do usuário sempre ficará disponível, independentemente de ter uma integração com o EAI 2.0 ativa, mas o acesso à mesma deverá obedecer os requisitos citados documento acima.

Importante ressaltar que serão processados somente os movimentos que possuam respectivo registro na tabela TMOVINTEGRACAOEAI.
