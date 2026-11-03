---
content_hash: 71579154d89c285232c7417eaafd9b7829399b21340b7b5ba08605c78f48b189
fetched_at: '2026-06-29T00:12:13.431147+00:00'
page_id: '955512085'
product: rm
source: tdn-rm
title: eduFlow 11.10 - Permissão para acessar Menu Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=955512085
version: 12
---

Para acessar o menu de pagamentos e realizar Negociação ou pagamento com PIX, CARTÃO, BOLETO o usuário deverá realizar algumas parametrizações.

Menu Pagamento

A permissão de acesso se dará da seguinte forma:

* O sistema habilitará a permissão do pagamento para todos os clientes, independentemente, desses clientes terem a licença ao TPC.
* Essa permissão se encontra dentro das permissão para o Meu eduCONNECT no perfil de usuário.
* Caso esteja habilitada, essa nova permissão é quem será responsável por habilitar ou não a visualização do pagamento para o usuário do Meu eduCONNECT.

Cadastro de Serviços

Para que seja exibida uma opção de pagamento, será necessário que a respectiva opção de pagamento ("Cartão de crédito", "Cartão de débito", "Boleto" ou "PIX") esteja marcada em **PELO MENOS UM** dos serviços do boleto.

Se uma opção de pagamento estiver **MARCADA** em um dos serviços do boleto, a mesma estará disponível no app, as opções estão localizadas no [Cadastro de Serviços](https://tdn.totvs.com/pages/viewpage.action?pageId=425458880)

Cartão de CréditoImportante

Para que a permissão "Permite acesso ao Meu eduCONNECT - TPC" esteja habilitada, é necessário ter licença do TPC.

Caso o parâmetro "Permite acesso ao Meu eduCONNECT (Payments)" não esteja setada, não será disponibilizada a permissão de pagamento com cartão, mesmo que o respectivo campo "Cartão de crédito" ou "Cartão de débito" esteja marcado no serviço do boleto selecionado para pagamento.

Essa comportamento refletirá na [negociação inteligente](https://tdn.totvs.com/pages/viewpage.action?pageId=527832872) que passará a habilitar o pagamento com cartão somente de usuário tiver acesso à permissão "Permite acesso ao eduCONNECT (Payments)"

Para saber sobre mais informações consulte:

* [Configuração de Perfil](https://tdn.totvs.com/x/B5QlE)
* [Perfil](https://tdn.totvs.com/x/bbAQG)
* [Segurança - Perfis](https://tdn.totvs.com/x/HJO2C)

## **TABELAS UTILIZADAS**

* GPERFIL - Cadastro de perfil
* GUSRPERFIL - Perfis de usuários

]]>
