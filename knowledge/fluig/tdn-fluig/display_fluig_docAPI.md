---
content_hash: e8732dd25b4cac692c38f9e07c85afc896ffd241bae55f4423513204622040a6
fetched_at: '2026-06-28T21:35:24.533355+00:00'
page_id: '270918599'
product: fluig
source: tdn-fluig
title: docAPI
type: documentation
url: https://tdn.totvs.com/display/fluig/docAPI
version: 16
---

Para ter acesso a funções relacionadas a documentos é possível utilizar nos eventos a variável global **docAPI**. Os métodos disponíveis através da **docAPI** são:

Lembre-se

Utilizamos padrões de desenvolvimento de mercado portanto, ao utilizar os métodos e classes abaixo, atente-se às boas práticas de desenvolvimento JAVA.

| Método | Especificação |
| --- | --- |
| copyDocumentToUploadArea(documentId, version) | Copia os arquivos físicos de um documento existente para a área de upload do usuário logado, onde:   * documentId: id do documento a ser copiado; * version: versão do documento a ser copiado;   Retorno: Array de Strings contendo os nomes dos arquivos que foram disponibilizados na área de upload. |
| createDocument(document, attachments, securityConfig, approvers, relatedDocs) | Cria um novo documento no GED de acordo com os parâmetros informados, onde:   * document: documento a ser criado; * attachments: lista de anexos do documento; * securityConfig: lista de configurações de segurança do documento; * approvers: lista de aprovadores do documento; * relatedDocs: lista de documentos relacionados ao documento;   Retorno: DocumentDto do documento criado.  Exemplo de utilização desta função em conjunto com a função copyDocumentToUploadArea:  jstrue |
| createFolder(document, securityConfig, approvers) | Cria uma nova pasta no GED de acordo com os parâmetros informados, onde:   * document: pasta a ser criada; * securityConfig: lista de configurações de segurança da pasta; * approvers: lista de aprovadores da pasta;   Retorno: DocumentDto da pasta criada.  Exemplo de utilização desta função:  jstrue O parâmetro publisherId do objeto [DocumentDTO](http://tdn.totvs.com/display/fluig/Guia+de+Propriedades+dos+Objetos#GuiadePropriedadesdosObjetos-DocumentDto) não será considerado quando a publicação for realizada via *script* em um evento de processo. Esse parâmetro só pode ser definido na criação do objeto via [WebService](http://tdn.totvs.com/pages/viewpage.action?pageId=73084007).  Confira um exemplo de como criar pastas definindo sua segurança por grupos e usuários [clicando aqui](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/create-advanced-folder). |
| getDocumentVersion(documentId, version) | Retorna o DocumentDto de um documento com base no seu id e sua versão, onde:   * documentId: id do documento a ser retornado; * version: versão do documento a ser retornado; |
| getUserPermissions(documentId, version) | Retorna o nível de permissão do usuário logado no documento informado, onde:   * documentId: id do documento; * version: versão do documento; |
| isUserInGroup(group) | Retorna se o usuário logado faz parte do grupo informado, onde:   * group: código do grupo a ser verificado; |
| newAttachment() | Retorna uma nova instância de Attachment. |
| newRelatedDocumentDto() | Retorna uma nova instância de RelatedDocumentDto. |
| newDocumentSecurityConfigDto() | Retorna uma nova instancia de DocumentSecurityConfigDto. |
| newApproverDto() | Retorna uma nova instância de ApproverDto. |
| newDocumentDto() | Retorna uma nova instância de DocumentDto, com o tipo 2 (Documento) como padrão. |

Veja o exempo (**create-advanced-folder**) em nosso repositório **[aqui](https://git.fluig.com/projects/SAMPLES/repos/projetos/browse/create-advanced-folder)**.
