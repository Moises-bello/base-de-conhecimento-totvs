---
content_hash: 03304711d473e84016898a1885f5bae0822ded18aeebb2fb3aae7d1a5263369c
fetched_at: '2026-06-29T00:10:59.800942+00:00'
page_id: '616205347'
product: rm
source: tdn-rm
title: TOTVS Segurança e Saúde Ocupacional - Totvs Assinatura Eletrônica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=616205347
version: 23
---

Para que seja possível a assinatura e guarda eletrônica de documentos, é imprescindível a utilização de uma solução especialista. Neste sentido, a Totvs lançou a sua própria solução de assinatura e guarda eletrônica de documentos denominada Totvs Assinatura Eletrônica. Para mais informações sobre a plataforma, [clique aqui](https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-totvs-assinatura-eletronica/). Dúvidas sobre a aquisição da plataforma, procure seu ESN.

**Importante:** As funcionalidades abaixo estão disponíveis nas versões 12.1.29; 12.1.31 e 12.1.32 expedidas a partir do dia 07/05/2021.

**Parametrização Global**

---

Para habilitar a integração com o TOTVS Assinatura Eletrônica é necessário informar as URLs de acesso. Para isso deve-se acessar o Totvs Segurança e Saúde Ocupacional | Ambiente | Parâmetros | Parâmetros Globais e acessar a aba Totvs Assinatura Eletrônica.

Mais informações sobre a aba, [clique aqui](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=562963400).

Caso o usuário não possua parametrização global preenchida com os endpoints do portal TOTVS Assinatura Eletrônica, será apresentado um banner informativo quando clicar no ícone da integração.

## **Liberação de Acesso**

---

Para liberar o acesso as funcionalidades do Totvs Assinatura Eletrônica deve-se acessar a tela Cadastro de Perfis, existente no Totvs Serviços Globais | Segurança | Perfis. Deve ser selecionado o sistema Segurança e Saúde Ocupacional.

Após a seleção do sistema serão exibidos os perfis existente para o mesmo, deve-se editar o perfil que terá acesso as funcionalidades do Totvs Assinatura Eletrônica e conceder a permissão de acesso.

## **Enviando Documento para o Totvs Assinatura Eletrônica**

---

Abaixo será demonstrado, um exemplo, de como é realizado o envio do documento/relatório para o Totvs Assinatura Eletrônica.

> É premissa que o documento/relatório que será enviado para o Totvs Assinatura Eletrônica esteja salvo em PDF.

No exemplo abaixo será gerado o relatório PGR em PDF:

Após a geração do relatório em PDF, deve-se clicar no menu  para abrir a tela do Totvs Assinatura Eletrônica

Ao clicar à primeira vez no menu  será exibida a tela de login do Totvs Assinatura Eletrônica

Após logar será exibida a tela de monitoramento como anexo:

#### As funcionalidades disponíveis na tela Monitor Integração Totvs Assinatura Eletrônica são:

* Atualização de status de documentos integrados

Ao ser executado esse processo o sistema verificará se o documento Pendente de assinatura ou Assinado parcialmente teve alguma alteração de status no portal TOTVS Assinatura  
Eletrônica e atualizará a informação no registro de monitoramento.

Essa opção de monitoramento será executada automaticamente para os registros pendentes caso o parâmetro global de atualização de status ao abri tela de visão esteja marcado.

Para os documentos com prazo de assinatura/validação o sistema verificará se o documento teve o prazo expirado, caso ele tenha o prazo espirado o sistema cancelará o documento.

* Aprovação de documentos para assinatura

Os documentos gerados com a opção de validação/aprovação não serão integrados automaticamente com o sistema de assinaturas. Eles serão integrados apenas após a execução desse processo, onde serão enviados os dados para assinatura caso o relatório tenha sido gerado corretamente.

Caso o usuário esteja associado ao documento como um dos destinatários ele poderá realizar a assinatura do documento através desse processo ao marcar a opção "Assinar documentos onde meu usuário esteja associado como assinador". Com isso o ser enviado o documento para o TOTVS Assinatura Eletrônica será enviado também sua assinatura. É importante que o usuário tenha validado o documento antes de realizar a assinatura. O usuário deverá se certificar de que o documento está correto e marcar a opção de ciente da tela.

* Assinar documentos

Esse processo permitirá que o usuário que esteja associado a um ou mais documentos possa realizar a assinatura desses, sem a necessidade de acessar o portal TOTVS Assinatura Eletrônica. É importante que o usuário tenha validado o documento antes de realizar a assinatura. O usuário deverá se certificar de que o documento está correto e marcar a opção de ciente da tela.

* Exclusão de documentos integrados

Através desse processo será possível excluir registros não integrados, integrados com erro ou não finalizados. No caso dos registros integrados e não finalizados (não assinados por todos) o sistema excluirá o documento do portal TOTVS Assinatura Eletrônica e da tela de monitoramento. Caso o documento já tenha sido assinado por todos os destinatários não será possível excluir o documento.

A exclusão do documento no portal de assinaturas dependerá do nível de acesso do usuário no documento.

* Envio de documento para assinatura

Esse processo permite o envio de documentos. O usuário poderá selecionar um arquivo PDF do disco local ou de um drive de rede e enviar para assinatura. As opções de aprovação e assinatura também estão disponíveis como no processo de integração normal. Será possível inserir um destinatário que esteja associado ao cadastro de Cliente/Fornecedor, Pessoa ou então um e-mail avulso.

No grid de destinatários é possível selecionar o tipo de participação do destinatário (Assinar, Validar ou Testemunhar) e na coluna "Prioridade assinatura" poderá ser utilizado o recurso de workflow, que funcionada da seguinte maneira:

Ao utilizar recurso de workflow pode-se definir uma ordem das assinaturas, onde uma prioridade menor só poderá assinar depois de as prioridades maiores tiverem assinado.

Exemplo:

[jose@integração.com](mailto:jose@integra%C3%A7%C3%A3o.com) - prioridade 0

[maria@integracao.com](mailto:maria@integracao.com) - prioridade 1

A Maria só conseguirá visualizar e assinar o documento depois que o José realizar sua assinatura. Caso o José rejeito o arquivo ele não aparecerá para a Maria.

Exemplo do envio do relatório PGR:

Ao clicar em Executar o destinatário receberá  um e-mail informando que existe um documento para assinar.

Após clicar no link "Acessar Totvs Assinatura Eletrônica" o usuário será direcionado à plataforma:

Quando o documento for assinado o mesmo pode ser visualizado pela tela de monitoramento:

Exibição do relatório

**É possível acessar a tela de Monitoramento através do menu de Relatórios, sem precisar acessar um relatório específico:**

**Colunas**

-        **Descrição**: Nesta coluna será exibida a descrição do relatório no monitoramento.

-        **Status**: Exibirá o status do documento/relatório.  Os registros de monitoramento poderão estar com um dos seguintes status:

-        **Job relatório**: Número do Job de execução do relatório.

-        **Id. Arquivo assinatura**: Identificador do arquivo na Api de assinatura.

-        **Remetente**: Usuário responsável pelo processo principal.

-        **Mensagem**: Mensagem de erro ou informação retornada pelo processo ou Api.

-        **Nome do arquivo**: Nesta coluna será exibido o nome do arquivo gerado.

-        **Campos chave**: Campos que compõem a chave para geração do relatório.

-        **Valores chave**: Valores que compõem o campo chave.

-        **Job Principal**: Identificador do Job responsável por disparar a geração dos relatórios (Diário de Classe ou Certificado) caso seja relacionado a um processo principal.

-        **Criado por**: Usuário de criação do processo.

-        **Criado em**: Data de criação do processo.

-        **Modificado por**: Usuário de modificação (alteração de status) do registro.

-        **Modificado em**: Data de modificação (alteração de status) do registro.
