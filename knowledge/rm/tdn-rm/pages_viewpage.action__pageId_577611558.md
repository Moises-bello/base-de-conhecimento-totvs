---
content_hash: ce13c823b465ccf5633627572ac6398292d5dd2212365c1662c54f0dd269c789
fetched_at: '2026-06-29T00:10:53.165852+00:00'
page_id: '577611558'
product: rm
source: tdn-rm
title: Assinatura Eletrônica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=577611558
version: 10
---

No módulo de Contratos 1.0 do Totvs Gestão de Estoque, Compras e Faturamento com a ferramenta “[Totvs Assinatura Eletrônica](https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-totvs-assinatura-eletronica/)” para controle dos documentos gerados. O TOTVS Assinatura Eletrônica é um sistema capaz de gerenciar com máxima segurança e eficiência, de forma centralizada, todo o processo, tanto no modelo de assinatura eletrônica, quanto nas assinaturas digitais com certificados do tipo A1 e A3

Na visão de Contratos (Gestão de Estoque, Compras e Faturamento → Contratos → Manutenção de Contrato) o ícone de atalho do “Totvs Assinatura Eletrônica” será apresentado e quando acionado o anexo de integração abrirá para filtragem.

**Aba Identificação**

Nesta aba, é possível informar o nome do envelope e algumas opções de publicação.

**Aba Documentos**

Nesta aba, é possível selecionar os documentos que serão enviados. A seleção pode ser feita tanto por meio de arquivos quanto por relatórios.

Para relatórios deverá ser observado os tipos:

* Na tela de **Contrato**, estão disponíveis para seleção apenas relatórios do tipo **“Contratos”**.
* Nas telas de **Movimentos**, é possível selecionar relatórios dos seguintes tipos: **Tipo Genérico, Documento, Email Movimento, Email Compra** e **Email Venda**.

Observação: A opção de selecionar relatório está disponível a partir da versão 12.1.2510.

**Aba Destinatários**

Nesta aba será preciso informar o e-mail do responsável pela validação e outro responsável pela assinatura digital do documento. Quando a busca for por Cliente/Fornecedor o e-mail carregado será o informado no cadastro do Cliente/Fornecedor campo “E-Mail”.

**Importante**

* Ao inserir o e-mail dos assinantes e validadores, imediatamente estes e-mails serão associados ao documento no portal TOTVS Assinatura Eletrônica.
* Da mesma forma, ao excluir os e-mails nesta visão, os mesmos serão excluídos do Portal TOTVS Assinatura Eletrônica
* É importante lembrar que estes usuários não precisam possuir uma conta ativa no portal TOTVS Assinatura Eletrônica, mas deverão usar o mesmo e-mail de cadastro para ter acesso ao documento.

**Funcionamento do processo**

Ao salvar os dados o sistema valida se o usuário logado no RM está cadastrado no TOTVS Assinatura, se não estiver será apresentada tela que permite informar o CPF e ao confirmar o usuário do RM será cadastrado automaticamente no TOTVS Assinatura.

Toda a comunicação sempre será por e-mail, se atentem a utilizar e-mails válidos no cadastro do usuário.

O Totvs assinatura Eletrônica é acessado por meio de um portal web, onde será gerenciado a preparação dos documentos, controlada as assinaturas e a disponibilização dos arquivos assinados (manifesto). Desse modo, o sistema reduz custos com papel, impressão e com a logística de envio e devolução de documentos, tornando sua empresa mais sustentável

**Processos disponíveis**

Além do envio de documento para gerenciamento e controle foi disponibilizado no RM, pelo menu de Processos do anexo da Integração Totvs Assinatura Eletrônica, as opções de atualização de status e exclusão de documentos não validados e/ou assinados:

Atualizar status de documentos: este processo atualiza o status do documento na tela de visão do anexo quando o documento for validado e assinado no Totvs Assinatura, alterando o status de "Pendente" para “Finalizado” assim que a validação e assinatura for efetivada no Totvs Assinatura. Outra forma de atualizar o status é marcando o parâmetro “Atualizar situação das assinaturas dos documentos ao carregar a visão” nos parâmetros de Globais.

Exclusão de documentos: este processo vai executar a exclusão de um documento já enviado anteriormente e que não esteja com o status de finalizado.

 Veja Também

* [Integração com o Totvs Assinatura Eletrônica](https://tdn.totvs.com/x/yCOOIQ)
