---
content_hash: 16bef680edafd449f9babb2b45b6a195143698c8e8682f3425a0833a849acbaf
fetched_at: '2026-06-29T00:05:54.200850+00:00'
page_id: '1075954266'
product: rm
source: tdn-rm
title: Tratamento para Acentuações e Caracteres Especiais - NFS-e com o TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1075954266
version: 3
---

Algumas prefeituras possuem restrições quanto ao uso de determinados caracteres especiais nas informações enviadas para a NFS-e. Para auxiliar nesses cenários, o RM disponibiliza o parâmetro **Retirar Acentuação** e **Texto para Sanitização do Doc-e**, que permite remover automaticamente caracteres configurados durante a geração do XML da nota fiscal.

Para mais informações sobre o parâmetro, consulte o tópico 2 - Parâmetro através da documentação:

No caso da **NFS-e com o TSS**, a sanitização será aplicada aos seguintes campos:

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

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=560653725

Campos:

| Tag XML | Descrição |
| --- | --- |
| `logradouro` | Logradouro onde foi realizada a prestação dos serviços do documento. |
| `complend` | Complemento do endereço da prestação dos serviços do documento. |
| `bairro` | Bairro da prestação dos serviços do documento. |

# Grupo de informações do intermediário do serviço

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=560653780

Campos:

| Tag XML | Descrição |
| --- | --- |
| `razao` | Razão social do intermediador. |

# Grupo de informações relativas ao Destinatário

#215a60Link do mapeamento do xml#

Campos:

| Tag XML | Descrição |
| --- | --- |
| `nome` | Nome do destinatário. |

# Grupo de informações do Endereço do Destinatário

#215a60Link do mapeamento do xml#

| Tag XML | Descrição |
| --- | --- |
| `logradouro` | logradouro do destinatário. |
| `complemento` | Complemento do endereço do destinatário. |
| `bairro` | Nome do bairro do destinatário. |

# Grupo de informações do tomador

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=560653794

Campos:

| Tag XML | Descrição |
| --- | --- |
| `razao` | Razão social do tomador. |
| `logradouro` | Logradouro do tomador. |
| `complend` | Complemento do endereço do tomador. |
| `bairro` | Bairro do tomador. |

# Grupo de informações do serviço

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=560653807

Campos:

| Tag XML | Descrição |
| --- | --- |
| `discr` | Discriminação do serviço. |

# Grupo de informações complementares

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=560653881

Campos:

| Tag XML | Descrição |
| --- | --- |
| `descricao` | Descrição/Dados complementares do documento. |
| `observacao` | Observações referentes ao documento. |

# Grupo de informações sobre construção civil do documento

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=560653923

Campos:

| Tag XML | Descrição |
| --- | --- |
| `xLogObra` | Logradouro da Obra. |
| `xComplObra` | Complemento do logradouro da Obra. |
| `xBairroObra` | Bairro da Obra. |

# Grupo de informações do destinatário

#215a60Link do mapeamento do xml#

Campos:

| Tag XML | Descrição |
| --- | --- |
| `nome` | nome do destinatário. |
| `logradouro` | logradouro do destinatário. |
| `complend` | Complemento do endereço do destinatário. |
| `bairro` | Nome do bairro do destinatário. |

# Grupo de informações do Serviços

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=560653807

Campos:

| Tag XML | Descrição |
| --- | --- |
| `discr` | Discriminação do serviço. |

# Grupo de informações de Eventos

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=1056144301

Campos:

| Tag XML | Descrição |
| --- | --- |
| `xLgr` | Tipo e nome do logradouro do endereço da atividade de evento. |
| `xCpl` | Complemento do endereço da atividade de evento. |
| `xBairro` | Bairro do endereço da atividade de evento. |

# Grupo de informações complementares

#215a60Link do mapeamento do xmlhttps://tdn.totvs.com/pages/viewpage.action?pageId=560653881

Campos:

| Tag XML | Descrição |
| --- | --- |
| `descricao` | Descrição/Dados complementares do documento. |
| `observacao` | Observações referentes ao documento. |
| `complend` | Complemento do imóvel. |
| `bairro` | Bairro do imóvel. |

# Grupo de informações sobre atividade portuária

#215a60Link do mapeamento do xml#

Campos:

| Tag XML | Descrição |
| --- | --- |
| `nomraz` | Nome/Razão social do proprietário/representante da atividade portuária. |
| `endereco` | Endereço da atividade portuária. |
| `compl` | Complemento do endereço da atividade portuária. |
| `bairro` | Bairro do endereço da atividade portuária. |
