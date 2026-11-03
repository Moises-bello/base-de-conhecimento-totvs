---
content_hash: 3a32d390a359ceab18e96ba44f985a7a4e563a6c98922b5f2e9aa2a3bbe754d0
fetched_at: '2026-06-29T00:05:54.187237+00:00'
page_id: '1075954003'
product: rm
source: tdn-rm
title: Tratamento para Acentuações e Caracteres Especiais - NFS-e com o TPF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1075954003
version: 4
---

Algumas prefeituras possuem restrições quanto ao uso de determinados caracteres especiais nas informações enviadas para a NFS-e. Para auxiliar nesses cenários, o RM disponibiliza o parâmetro **Retirar Acentuação** e **Texto para Sanitização do Doc-e**, que permite remover automaticamente caracteres configurados durante a geração do XML da nota fiscal.

Para mais informações sobre o parâmetro, consulte o tópico 2 - Parâmetro através da documentação:

No caso da **NFS-e com o TPF**, a sanitização será aplicada aos seguintes campos:

1nonenone

# Grupo de informações do prestador

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=1056144007

Campos:

| Tag XML | Descrição |
| --- | --- |
| `razao` | Razão social do prestador. |
| `logradouro` | Descrição do logradouro do prestador. |
| `compleend` | Complemento do endereço do prestador. |
| `bairro` | Nome do bairro do prestador. |

# Grupo de informações da prestação

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=1056144053

Campos:

| Tag XML | Descrição |
| --- | --- |
| `logradouro` | Logradouro onde foi realizada a prestação dos serviços do documento. |
| `complend` | Complemento do endereço da prestação dos serviços do documento. |
| `bairro` | Bairro da prestação dos serviços do documento. |

# Grupo de informações do intermediário do serviço

#215a60Link do mapeamento do xml#

Campos:

| Tag XML | Descrição |
| --- | --- |
| `razao` | Razão social do intermediador. |

# Grupo de informações do tomador

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=1056144098

Campos:

| Tag XML | Descrição |
| --- | --- |
| `razao` | Razão social do tomador. |
| `logradouro` | Logradouro do tomador. |
| `complend` | Complemento do endereço do tomador. |
| `bairro` | Bairro do tomador. |

# Grupo de informações do serviço

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=1056144146

Campos:

| Tag XML | Descrição |
| --- | --- |
| `discr` | Discriminação do serviço. |

# Grupo de informações complementares

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=1056938702

Campos:

| Tag XML | Descrição |
| --- | --- |
| `descricao` | Descrição/Dados complementares do documento. |
| `observacao` | Observações referentes ao documento. |

# Grupo de informações da informações sobre construção civil do documento

#215a60Link do mapeamento do xml#

Campos:

| Tag XML | Descrição |
| --- | --- |
| `xLogObra` | Logradouro da Obra. |
| `xComplObra` | Complemento do logradouro da Obra. |
| `xBairroObra` | Bairro da Obra. |

# Grupo de informações do destinatário

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=1027822163

Campos:

| Tag XML | Descrição |
| --- | --- |
| `nome` | nome do destinatário. |
| `logradouro` | logradouro do destinatário. |
| `complend` | Complemento do endereço do destinatário. |
| `bairro` | Nome do bairro do destinatário. |

# Grupo de informações de operações relacionadas a bens imóveis, exceto obras

#215a60Link do mapeamento do xml#

Campos:

| Tag XML | Descrição |
| --- | --- |
| `logradouro` | Logradouro do imóvel. |
| `numend` | Número do imóvel. |
| `complend` | Complemento do imóvel. |
| `bairro` | Bairro do imóvel. |
