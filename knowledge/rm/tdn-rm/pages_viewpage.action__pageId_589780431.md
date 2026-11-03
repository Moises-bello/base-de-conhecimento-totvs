---
content_hash: 4a599e04388632baeeee210097baa88762056e6dd418b57161dca518142eaced
fetched_at: '2026-06-29T00:10:53.921915+00:00'
page_id: '589780431'
product: rm
source: tdn-rm
title: Totvs Assinatura Eletrônica - Acordo Gestão Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=589780431
version: 4
---

**Disponível a partir da versão 12.1.31**

Implementada integração da entidade Acordo do Totvs Gestão Financeira com a ferramenta “[Totvs Assinatura Eletrônica](https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-totvs-assinatura-eletronica/)” para controle dos documentos gerados na negociação. O TOTVS Assinatura Eletrônica é um sistema capaz de gerenciar com máxima segurança e eficiência, de forma centralizada, todo o processo, tanto no modelo de assinatura eletrônica, quanto nas assinaturas digitais com certificados do tipo A1 e A3

Na visão de Acordo o ícone de atalho do “Totvs Assinatura Eletrônica” será apresentado e quando acionado o anexo de integração abrirá para filtragem.

**Aba Identificação**

Para um novo documento será necessário informar o nome do mesmo e o caminho do documento que será enviado ao Totvs Assinatura. Só será aceito documento com extensão pdf e tamanho máximo de 10Mb.

**Aba Destinatários**

Nesta aba será preciso informar o e-mail do responsável pela validação e outro responsável pela assinatura digital do documento. Quando a busca for por Cliente/Fornecedor o e-mail carregado será o informado no cadastro do Cliente/Fornecedor campo “E-Mail”.

**Importante**

* Ao inserir o e-mail dos assinantes e validadores, imediatamente estes e-mails serão associados ao documento no portal TOTVS Assinatura Eletrônica.
* Da mesma forma, ao excluir os e-mails nesta visão, os mesmos serão excluídos do Portal TOTVS Assinatura Eletrônica
* É importante lembrar que estes usuários não precisam possuir uma conta ativa no portal TOTVS Assinatura Eletrônica, mas deverão usar o mesmo e-mail de cadastro para ter acesso ao documento.

**Funcionamento do processo**

Ao salvar os dados o sistema valida se o usuário logado no RM está cadastrado no TOTVS Assinatura, se não estiver será apresentada tela que permite informar o CPF e ao confirmar o usuário do RM será cadastrado automaticamente no TOTVS Assinatura.

Toda a comunicação sempre será por e-mail, se atentem a utilizar e-mails válidos no cadastro do usuário.

O Totvs assinatura Eletrônica é acessado por meio de um portal web, onde será gerencido a preparação dos documentos, controlada as assinaturas e a disponibilização dos arquivos assinados (manifesto). Desse modo, o sistema reduz custos com papel, impressão e com a logística de envio e devolução de documentos, tornando sua empresa mais sustentável

**Processos disponíveis**

Além do envio de documento para gerenciamento e controle foi disponibilizado no RM, pelo menu de Processos do anexo da Integração Totvs Assinatura Eletrônica, as opções de atualização de status e exclusão de documentos não validados e/ou assinados:

Atualizar status de documentos: este processo atualiza o status do documento na tela de visão do anexo quando o documento for validado e assinado no Totvs Assinatura, alterando o status de "Pendente" para “Finalizado” assim que a validação e assinatura for efetivada no Totvs Assinatura. Outra forma de atualizar o status é marcando o parâmetro “Atualizar situação das assinaturas dos documentos ao carregar a visão” nos parâmetros de Globais.

Exclusão de documentos: este processo vai executar a exclusão de um documento já enviado anteriormente e que não esteja com o status de finalizado.

Arquivo armazenado: Para visualizar um documento do TOTVS Assinatura Eletrônica e consultar seu status, basta clicar no link "Visualizar", na aba identificação:

Desta forma,  o sistema irá mostrar o documento e o seu status atual (pendente, finalizado ou rejeitado), possibilitando salvar o mesmo em PDF ou realizar uma impressão, além de outros controles.

 Veja Também

* [Integração com o Totvs Assinatura Eletrônica](https://tdn.totvs.com/x/yCOOIQ)
