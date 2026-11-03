---
content_hash: 2777d5f9916c3cfca8be32004fd5775b7c1b1bd1b4b63e8e90dedfa794ff3990
fetched_at: '2026-06-29T00:12:07.972218+00:00'
page_id: '927547660'
product: rm
source: tdn-rm
title: Integração TOTVS Assinatura Eletrônica x Contratos TCOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=927547660
version: 10
---

A integração entre o TOTVS Construção Obras e Projetos com o TOTVS Assinatura Eletrônica, permite o gerenciamento de documentos que necessitam ser assinados eletronicamente por um ou mais destinatários.

Essa integração permite que relatórios do sistema e/ou outros documentos, possam ser enviados de forma manual ou automaticamente para assinatura, com base em critérios previamente definidos.

Atualmente, é possível enviar para assinatura informações dos seguintes processos do TCOP:

* Cadastro de contrato;
* Períodos do contrato;
* Aditivos contratuais;
* Adiantamentos de contrato.

Essa parametrização é feita por projeto, nos parâmetros de Integração > TOTVS .

Requisitos para Integração

Para funcionamento da integração, o usuário necessitará:

1 – Contratação de um plano de assinaturas através da TOTVS Store;

2 – Criação dos usuários no TAE, que realizarão as integrações através do TOTVS Construção Obras e Projetos;

Importante

A criação desses usuários é necessária no portal TOTVS Assinatura Eletrônica, pois estes usuários serão identificados como autores dos documentos enviados para assinatura, possuirão permissões para envio de documentos, consulta de status, exclusão de documentos e destinatários; e também a criação de outros usuários necessários durante a execução do processo.

3 – Parametrização do sistema para realização da comunicação com TOTVS Assinatura Eletrônica.

Parametrização inicial

Após a contratação do plano o usuário deverá acessar o sistema RM, e abrir a tela de Parâmetros Globais, disponível através do menu “Ambiente | Parâmetros | Parâmetros Globais” e na aba “Integração com TOTVS Sign” preencher os campos:

URL de autenticação:

Informe o endereço <https://totvssign.totvs.app/identityintegration>

URL da API de integração:

Informe o endereço [https://totvssign.totvs.app](https://totvssign.totvs.app/)

URL de login via formulário web:

Informe o endereço <https://totvssign.totvs.app/webapptotvssign/#/auth/login?external=true>

Usuário de serviço:

Usuário de serviço cadastrado no TAE

Senha do usuário de serviço:

Senha do usuário de serviço do TAE

Campo **Atualizar situação das assinaturas dos documentos ao carregar visão**

Este campo define o comportamento da atualização do status dos documentos enviados para assinatura ao abrir a tela de monitoramento dos dados. Caso este campo esteja marcado, ao abrir a tela de visão de monitoramento de documentos enviados para integração o sistema consultará os documentos que estão pendentes de assinatura e verificará se os mesmos sofreram alteração no seus status. Caso tenham sofrido alteração o sistema atualizará o status no RM. Caso o campo não seja marcado a atualização de status deverá ser feita através de um processo disponibilizado na tela de monitoramento.

Configuração de acesso

Os usuários que irão realizar a integração de documentos com o TOTVS Assinatura Eletrônica, deverão ter seus perfis de acesso ajustados para permitir o acesso às opções de Assinatura Eletrônica.

Recursos disponíveis

Os recursos para realização da integração com o sistema TOTVS Assinatura Eletrônica, estão disponíveis no TOTVS Construção Obra e Projetos através do ícone “TOTVS Assinatura Eletrônica”, disponível nos cadastros que utilizam essa integração. Na imagem abaixo, é o ícone destacado tanto no cadastro de contrato, quanto no anexo de períodos, já que ambos podem utilizar essa integração:

Ao clicar no botão, será exibida a aba de Integração com o TOTVS Assinatura Eletrônica, conforme imagem abaixo. Nela será possível enviar um documento para assinatura, saber qual o status da assinatura do documento, visualizar os arquivos e os envolvidos no processo.

Para enviar o documento para assinatura, basta preencher na aba Identificação, o campo Nome, e anexar o arquivo na segunda aba Documentos. Os destinatários serão carregados na aba de mesmo nome, de acordo com os contatos do contrato e do Cliente/Fornecedor cadastrados previamente.
