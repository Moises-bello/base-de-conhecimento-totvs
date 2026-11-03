---
content_hash: 6a91bb66d57ccd24a09bd192b528b286b3456cfb50af77cb08520c4898b140ef
fetched_at: '2026-06-29T00:05:53.372676+00:00'
page_id: '1070063940'
product: rm
source: tdn-rm
title: Tratamento para Caracteres Especiais e Acentuações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1070063940
version: 13
---

# Conteúdo

1Conteúdononenone

# 1. Sobre

O sistema permite configurar, por filial, se os acentos e quais caracteres especiais devem ser removidos no Doc-e. Desta forma, é possível preservar informações como datas, valores monetários, percentuais e pontuações que fazem parte do texto do serviço, garantindo que o conteúdo transmitido reflita fielmente o que está formalizado em contrato ou edital — situação especialmente relevante em operações com órgãos públicos.

Tais configurações são realizadas nos parâmetros da filial, no campo Retirar Acentos e Sanitização Doc-e respectivamente.

# 2. Versões para atualização

A solução está disponível a partir dos patches:

Data: 

Biblioteca RM

* 12.1.2510
* 12.1.2602
* 12.1.2606

# 3. Como configurar

Marque a opção **Retirar Acentos** para que a acentuação seja removida.

Acesse os parâmetros da filial e, no campo **Sanitização DOC-e**, informe apenas os caracteres que deseja remover. Deixe o campo vazio para que nenhum caractere adicional seja eliminado além dos acentos.

# 4. Visão Geral dos Parâmetros

| Parâmetro | Comportamento |
| --- | --- |
| **`RetirarAcentos`** | Quando habilitado, remove acentos e caracteres especiais dos campos listados abaixo. |
| **`SanitizacaoDOCe`** | Define um conjunto de caracteres que serão substituídos por espaço. Este tratamento aplica-se aos campos listados abaixo.  O conteúdo deste campo deve ser informado de forma literal (uma lista de caracteres), por exemplo:   | ¨~'´`^ªº§¢£³²¹¬° | | --- | |

---

falsefalseTiposNFS-e — Layout Único (TSS / TPF)

## NFS-e — Layout Único (TSS / TPF)

Para o layout único, as tags que podem ter seu conteúdo removido acentos ou sanitizado são:

### Grupo de informações de identificação

| Tag XML | Descrição |
| --- | --- |
| `formpagto` | Forma de pagamento do documento. |
| `tipodocumento` | Tipo do documento. |

### Grupo de informações do prestador

| Tag XML | Descrição |
| --- | --- |
| `razao` | Razão social do prestador. |
| `logradouro` | Logradouro do prestador. |
| `compleend` | Complemento do endereço. |
| `bairro` | Bairro do prestador. |

### Grupo de informações da prestação

| Tag XML | Descrição |
| --- | --- |
| `logradouro` | Logradouro da prestação. |
| `complend` | Complemento do endereço. |
| `bairro` | Bairro da prestação. |

### Grupo de informações do intermediário

| Tag XML | Descrição |
| --- | --- |
| `razao` | Razão social do intermediário. |

### Grupo de informações do tomador

| Tag XML | Descrição |
| --- | --- |
| `razao` | Razão social do tomador. |
| `logradouro` | Logradouro do tomador. |
| `complend` | Complemento do endereço. |
| `bairro` | Bairro do tomador. |

### Grupo de informações do destinatário

| Tag XML | Descrição |
| --- | --- |
| `nome` | Nome do destinatário. |
| `logradouro` | Logradouro do destinatário. |
| `complend` | Complemento do endereço do destinatário. |
| `bairro` | Bairro do destinatário. |

### Grupo de informações do endereço do imóvel

| Tag XML | Descrição |
| --- | --- |
| `endereco` | Endereço do imóvel. |
| `complemento` | Complemento do imóvel. |
| `bairro` | Bairro do imóvel. |

### Grupo de informações do serviço

| Tag XML | Descrição |
| --- | --- |
| `discr` | Discriminação do serviço. |

### Informações complementares

| Tag XML | Descrição |
| --- | --- |
| `descricao` | Descrição/dados complementares. |
| `observacao` | Observações do documento. |

### Grupo de informações da atividade portuária

| Tag XML | Descrição |
| --- | --- |
| `nomraz` | Nome/Razão social do responsável. |
| `endereco` | Endereço da atividade portuária. |
| `compl` | Complemento do endereço. |
| `bairro` | Bairro da atividade portuária. |

### Grupo de informações da construção civil

| Tag XML | Descrição |
| --- | --- |
| `endereco` | Endereço da construção civil. |
| `compl` | Complemento do endereço. |
| `bairro` | Bairro da construção civil. |

### Grupo de informações da obra

| Tag XML | Descrição |
| --- | --- |
| `xLogObra` | Logradouro da obra. |
| `xComplObra` | Complemento do logradouro da obra. |
| `xBairroObra` | Bairro da obra. |

### Grupo de informações do imóvel

| Tag XML | Descrição |
| --- | --- |
| `logradouro` | Logradouro do imóvel. |
| `complend` | Complemento do imóvel. |
| `bairro` | Bairro do imóvel. |

NFS-e — Layout Nacional (DPS)

## NFS-e — Layout Nacional (DPS)

Para o layout nacional, as tags que podem ter seu conteúdo removido acentos ou sanitizado são::

### Grupo de informações do endereço

| Tag XML | Descrição |
| --- | --- |
| `xLgr` | Logradouro do endereço. |
| `xCpl` | Complemento do endereço. |
| `xBairro` | Bairro do endereço. |

### Grupo de informações do prestador

| Tag XML | Descrição |
| --- | --- |
| `xNome` | Nome/Razão social do prestador. |

### Grupo de informações do tomador

| Tag XML | Descrição |
| --- | --- |
| `xNome` | Nome/Razão social do tomador. |

### Grupo de informações do intermediário

| Tag XML | Descrição |
| --- | --- |
| `xNome` | Nome/Razão social do intermediário. |

### Grupo de informações do serviço

| Tag XML | Descrição |
| --- | --- |
| `xDescServ` | Descrição do serviço. |

### Grupo de informações do serviço

| Tag XML | Descrição |
| --- | --- |
| `infoCompl` | Informações complementares do serviço. |

### Informações complementares

| Tag XML | Descrição |
| --- | --- |
| `xInfComp` | Texto de informações complementares. |

### Grupo de informações do prestador

| Tag XML | Descrição |
| --- | --- |
| `razao` | Razão social do prestador. |
| `compleend` | Complemento do endereço do prestador. |
| `bairro` | Bairro do prestador. |

### Grupo de informações da prestação

| Tag XML | Descrição |
| --- | --- |
| `logradouro` | Logradouro da prestação. |
| `complend` | Complemento do endereço da prestação. |
| `bairro` | Bairro da prestação. |

### Grupo de informações do intermediário

| Tag XML | Descrição |
| --- | --- |
| `razao` | Razão social do intermediário. |

### Grupo de informações do tomador

| Tag XML | Descrição |
| --- | --- |
| `razao` | Razão social do tomador. |
| `logradouro` | Logradouro do tomador. |
| `complend` | Complemento do endereço do tomador. |
| `bairro` | Bairro do tomador. |

### Grupo de informações do destinatário

| Tag XML | Descrição |
| --- | --- |
| `nome` | Nome do destinatário. |
| `logradouro` | Logradouro do destinatário. |
| `complend` | Complemento do endereço do destinatário. |
| `bairro` | Bairro do destinatário. |

### Grupo de informações do endereço do imóvel

| Tag XML | Descrição |
| --- | --- |
| `endereco` | Endereço do imóvel. |
| `complemento` | Complemento do imóvel. |
| `bairro` | Bairro do imóvel. |

### Grupo de informações do serviço

| Tag XML | Descrição |
| --- | --- |
| `discr` | Discriminação do serviço. |

### Informações complementares

| Tag XML | Descrição |
| --- | --- |
| `descricao` | Descrição/dados complementares. |
| `observacao` | Observações do documento. |

### Grupo de informações da atividade portuária

| Tag XML | Descrição |
| --- | --- |
| `nomraz` | Nome/Razão social do responsável. |
| `endereco` | Endereço da atividade portuária. |
| `compl` | Complemento do endereço. |
| `bairro` | Bairro da atividade portuária. |

### Grupo de informações da construção civil

| Tag XML | Descrição |
| --- | --- |
| `endereco` | Endereço da construção civil. |
| `compl` | Complemento do endereço. |
| `bairro` | Bairro da construção civil. |

### Grupo de informações da obra

| Tag XML | Descrição |
| --- | --- |
| `xLogObra` | Logradouro da obra. |
| `xComplObra` | Complemento do logradouro da obra. |
| `xBairroObra` | Bairro da obra. |

### Grupo de informações do imóvel

| Tag XML | Descrição |
| --- | --- |
| `logradouro` | Logradouro do imóvel. |
| `complend` | Complemento do imóvel. |
| `bairro` | Bairro do imóvel. |
