---
content_hash: e33fe53d29362f03895b7bbbbfcc959d343eee666032b9d359bdcb74cd2d291b
fetched_at: '2026-06-29T00:11:12.360306+00:00'
page_id: '652399054'
product: rm
source: tdn-rm
title: Dados Fiscais Município
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=652399054
version: 31
---

# Conteúdo

Conteúdonone

# 1. Visão Geral

Este cadastro tem como objetivo facilitar a integração entre os processos de emissão de NFS-e (Nota Fiscal de Serviço eletrônica) e o Módulo Financeiro do sistema, permitindo maior controle e aderência às exigências fiscais de cada município.

# 2. Integração Financeiro

Campos

|  |  |  |
| --- | --- | --- |
| **Campos** | **Obrigatório** | **Descrições dos Campos** |
| Cliente/Fornecedor | Não | Permitirá vincular um cliente/fornecedor padrão para o município em questão. |
| Data Vencimento do ISS | Não | Será possível definir a data de vencimento do ISS para o município em questão. |

# 3. NFS-e

Campos

|  |  |  |
| --- | --- | --- |
| **Campos** | **Obrigatório** | **Descrições dos Campos** |
| Não Remover Máscara IM Prestador | Não | É possível definir como será gerado na NFS-e a inscrição municipal do prestador. Quando o campo "Não Remover Máscara IM Prestador" estiver marcado o valor da inscrição municipal é gerado no XML conforme cadastrado, sem remover os caracteres de máscara. |
| Não Agrupar Itens | Não | É possível controlar se os serviços serão consolidados na NFS-e. O agrupamento só é feito para municípios que usam os layouts ABRASF, SIGISS ou XMLABRASF e os itens do movimento precisam ter o mesmo código de serviço. Ao marcar esta opção, para que a NFS-e seja gerada corretamente, é necessário ter os tributos cadastrados nos itens do movimento e não no movimento. |
| Não Fatura Movimento | Não | Este campo controla se o movimento será faturado automático ou não na autorização da NFS-e. Quando o mesmo estiver desmarcado e a NFS-e for autorizada, ela mudará o status do movimento para "**Faturada**". Caso contrario, quando estiver marcado e autorizar a NFS-e, o status do movimento ficara "**A Faturar**" e o processo deverá ser feito manualmente através do "**Gerar Movimento com número da Prefeitura**". |
| Envio Síncrono | Não | Permite configurar se o envio da NFS-e será realizado de forma síncrona, ou seja, com a autorização sendo processada no mesmo momento do envio ao TSS. Essa opção deve ser utilizada em casos onde a prefeitura exige esse tipo de comunicação imediata. Quando habilitado, o TSS receberá essa configuração por meio do serviço **[CfgAmbNfse001](https://tdn.totvs.com/pages/viewpage.action?pageId=562470315)**, conforme especificado na documentação do TSS.  **Importante:** Algumas prefeituras não aceitam o envio assíncrono e, por isso, é necessário ativar esse campo para garantir o correto processamento e autorização da nota fiscal. |
| Gerar Endereço do Projeto | Não | Define se o Endereço do projeto (Obra) será gerado no xml da NFS-e. Ao marcar esta opção serão gerados as tags: xLogObra, xComplObra, vNumeroObra, xBairroObra, xCepObra, cCidadeObra, xCidadeObra, xUfObra, cPaisObra, xPaisObra no grupo: construção.  **Importante**: Parametrização deve ser realizada no município da filial emitente da NFS-e e a prefeitura deve estar apta para receber tais informações. |
| Data de Ativação da NFS-e Nacional | Não | É utilizado para identificar se o município está integrado ao **Layout Nacional da NFS-e.**  Quando em branco, o município é considerado como **não integrado** ao Layout Nacional.  Quando preenchido, o município é considerado como**integrado** a partir da data informada. |

Ao selecionar estes campos "**Não Remover Máscara IM Prestador**" ou "**Não Agrupar Itens**",  os mesmos terão aplicabilidade no
