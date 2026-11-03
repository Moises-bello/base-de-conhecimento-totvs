---
content_hash: 93517dd8c2e1978b4f96886fe2b51d770811576b26b2e6635bb85a61f228e74b
fetched_at: '2026-06-29T00:11:21.225290+00:00'
page_id: '689070116'
product: rm
source: tdn-rm
title: Monitor de relatórios-Monitoramento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=689070116
version: 4
---

Após a geração do Relátório do Espelho do cartão de Ponto, será  possível acessar as informações referente aos relatórios gerados através do menu “Assinatura Eletrônica | Monitoramento | Monitor de Relatórios”, onde serão exibidos os resultados de cada job de relatório enviado para a integração e onde poderão ser realizadas operações de aprovação de registros pendentes de validação, atualização de status com base nas ações realizadas através do portal TOTVS Assinatura Eletrônica e também a exclusão de documentos não finalizados.

Para cada funcionário será gerado um registro de monitoramento conforme relatório gerado.

Ao editar um registro o usuário poderá visualizar as informações detalhadamente e ter algumas informações a mais como:

**Destinatários**

Serão exibidos os destinatários associados ao documento, a ação esperada do usuário e o status do usuário no documento. Será possível incluir e excluir destinatários caso o usuário tenha permissão de acesso ao documento e o documento não esteja finalizado. Na tela de inclusão de destinatários é possível realizar a seleção via digitação de e-mail, seleção de cliente/fornecedor ou pessoa.

**Prazo de assinatura**

Data limite para validação/assinatura do documento. Caso o documento utilize prazo de assinatura e não tenha sido assinado até a data, ao ser executado o processo de atualização de status o documento será cancelado.

**Download do arquivo**

Através dessa opção o usuário poderá ter acesso ao arquivo PDF do documento. Serão consideradas duas opções de download;

1 – Registro pendente de aprovação: ao clicar no botão será visualizado o arquivo a ser integrado, que ainda se encontra no sistema RM.

2 – Registro já integrado com o TOTVS Assinatura eletrônica: será realizado o download da última versão do documento no sistema de assinaturas. Caso ele já possua alguma assinatura realizada será exibido o documento de manifesto com as informações da assinatura.

**Processos relacionados ao monitoramento**

**Atualização de status de documentos integrados**

Ao ser executado esse processo o sistema verificará se o documento Pendente de assinatura ou Assinado parcialmente teve alguma alteração de status no portal TOTVS Assinatura Eletrônica e atualizará a informação no registro de monitoramento.

Essa opção de monitoramento será executada automaticamente para os registros pendentes caso o parâmetro global de atualização de status ao abri tela de visão esteja marcado.

Para os documentos com prazo de assinatura/validação o sistema verificará se o documento teve o prazo expirado, caso ele tenha o prazo espirado o sistema cancelará o documento.

**Aprovação de documentos para assinatura**

Os documentos gerados com a opção de validação/aprovação não serão integrados automaticamente com o sistema de assinaturas. Eles serão integrados apenas após a execução desse processo, onde serão enviados os dados para assinatura caso o relatório tenha sido gerado corretamente.

Caso o usuário esteja associado ao documento como um dos destinatários ele poderá realizar a assinatura do documento através desse processo ao marcar a opção "Assinar documentos onde meu usuário esteja associado como assinador". Com isso o ser enviado o documento para o TOTVS Assinatura Eletrônica será enviado também sua assinatura. É importante que o usuário tenha validado o documento antes de realizar a assinatura. O usuário deverá se certificar de que o documento está correto e marcar a opção de ciente da tela.

**Assinar documento**

Esse processo permitirá que o usuário que esteja associado a um ou mais documentos possa realizar a assinatura desses, sem a necessidade de acessar o portal TOTVS Assinatura Eletrônica. É importante que o usuário tenha validado o documento antes de realizar a assinatura. O usuário deverá se certificar de que o documento está correto e marcar a opção de ciente da tela.

**Exclusão de documentos integrados**

Através desse processo será possível excluir registros não integrados, integrados com erro ou não finalizados. No caso dos registros integrados e não finalizados (não assinados por todos) o sistema excluirá o documento do portal TOTVS Assinatura Eletrônica e da tela de monitoramento. Caso o documento já tenha sido assinado por todos os destinatários não será possível excluir o documento.

A exclusão do documento no portal de assinaturas dependerá do nível de acesso do usuário no documento.

**Envio de documento para assinatura**

Esse processo permite o envio de documentos que não são integrados através do processo de integração de relatórios (Processo de integração). O usuário poderá selecionar um arquivo PDF do disco local ou de um drive de rede e enviar para assinatura. As opções de aprovação e assinatura também estão disponíveis como no processo de integração normal. Será possível inserir um destinatário que esteja associado ao cadastro de Cliente/Fornecedor, Pessoa ou então um e-mail avulso.

No grid de destinatários é possível selecionar o tipo de participação do destinatário (Assinar, Validar ou Testemunhar) e na coluna "Prioridade assinatura" poderá ser utilizado o recurso de workflow, que funcionada da seguinte maneira:

Ao utilizar recurso de workflow pode-se definir uma ordem das assinaturas, onde uma prioridade menor só poderá assinar depois de as prioridades maiores tiverem assinado. Exemplo:

[jose@integração.com](mailto:jose@integração.com) - prioridade 0

[maria@integracao.com](mailto:maria@integracao.com) - prioridade 1

A Maria só conseguirá visualizar e assinar o documento depois que o José realizar sua assinatura. Caso o José rejeito o arquivo ele não aparecerá para a Maria.

Nessa tela não é possível gerar relatórios de forma automática, estando o recurso desabilitado para uso em outros módulos.

### Vídeo

80%80%
