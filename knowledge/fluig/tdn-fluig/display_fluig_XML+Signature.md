---
content_hash: 412b1c78ce2090f823b7707f766ada735af25a190d847feea7340df6510febcc
fetched_at: '2026-06-28T21:35:28.072629+00:00'
page_id: '6066570'
product: fluig
source: tdn-fluig
title: XML Signature
type: documentation
url: https://tdn.totvs.com/display/fluig/XML+Signature
version: 7
---

Fique atento!

O TOTVS ESB não é mais ofertado por se tratar de uma solução legada. A nova solução para realizar integrações é o TOTVS iPaaS. Saiba mais detalhes **[aqui](https://www.totvs.com/totvs-ipaas/)**.

A finalidade desse componente é assinar digitalmente documentos XML. Os campos comuns são discriminados abaixo.

| Campo | Descrição |
| --- | --- |
| Name | Inserir uma identificação para a configuração do componente. |
| Type | Selecionar o tipo de assinatura, podendo ser Hardware (TrueAccess ou PKCS11) ou Software. |

A assinatura digital em documentos XML poderá ser realizada utilizando três tipos de algoritmos: **Software**, **TrueAccess** e **PKCS11**. As tabelas abaixo descrevem os campos utilizados para cada tipo em modo respectivo.

| Campo | Descrição |
| --- | --- |
| Keystore | Inserir o caminho completo para o diretório no qual se encontram os certificados. |
| Password | Inserir a senha do repositório de certificados. |
| Alias | Inserir o apelido do certificado dentro do KeyStrore. |
| Alias Password | Inserir a senha do certificado. |
| Reference URI | Inserir o filtro da assinatura por software (namespace ou tag). |
| Certificate | Inserir o caminho completo para o diretório onde está gravada a chave pública do cliente. |

| Campo | Descrição |
| --- | --- |
| Host | Endereço de host e porta do HSM da True Access. |
| User | Nome do usuário para acesso ao HSM. |
| Password | Senha do usuário no HSM. |
| Key | Inserir a chave de segurança privada para o certificado. |
| Certificate | Inserir o caminho completo para o local no qual está armazenado o certificado. |
| Filter | Quando selecionado, é possível realizar assinatura digital somente de parte do XML, através do uso de filtros (Namespace + Tag + Id). Quando não selecionado, indica que a assinatura deve abranger todo o documento XML. |
| Namespace | Inserir o namespace do XML. |
| Tag | Inserir o nome da tag que será realizada a assinatura digital. |
| Id | Inserir o identificador da assinatura. |

| Campo | Descrição |
| --- | --- |
| Keystore Pwd | Inserir a senha de acesso ao HSM. |
| Key Alias | Inserir o alias da chave privada do cliente. |
| Key Password | Inserir o PIN do usuário. |
| Certificate Alias | Inserir o alias do certificado do cliente. |
| Reference URI | Inserir o filtro da assinatura do XML (namespace ou tag). |
