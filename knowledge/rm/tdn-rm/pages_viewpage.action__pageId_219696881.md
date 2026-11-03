---
content_hash: 05162a002bd29cb9dd369ca3a8679242f833311708c8b1be2fc4710f0f530c2e
fetched_at: '2026-06-29T00:06:19.369888+00:00'
page_id: '219696881'
product: rm
source: tdn-rm
title: TOTVS Colaboração 2.00
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219696881
version: 8
---

# Objetivo

Este documento tem por objetivo fornecer as parametrizações e informações necessárias para funcionamento do TOTVS Colaboração 2.0, englobando todos os serviços disponibilizados pelo mesmo:

* NF-e (Envio, Recebimento, Cancelamento, Consulta)
* NFS-e (Envio, Recebimento, Cancelamento, Substituição, Consulta)
* CT-e (Envio, Recebimento, Cancelamento, Consulta)
* MDF-e (Envio, Cancelamento)
* MD-e (Envio, Cancelamento )

Ele pode ser utilizado para a implantação do TOTVS Colaboração em um novo cliente ou para auxiliar a configuração de um serviço específico, para aqueles que já utilizam a solução.

O documento possui uma visão geral, e  logo após, a parametrização padrão necessária para funcionamento de todos os serviços. As especificidades de cada serviço são detalhadas em tópicos logo a seguir.

# Introdução

A solução TOTVS Colaboração 2.0 é composta basicamente pela integração entre o ERP e a Neogrid. Diferente do TC 1.0, não existe o intermédio do TSS, o que trouxe uma arquitetura mais enxuta. Para o cliente, a nova arquitetura resulta em uma melhor performance, mais simples e com maior automatismo.

A integração entre a NeoGrid e os ERPs TOTVS deve seguir uma padronização, com premissas que reafirmam os benefícios citados:

a)      Solução de integração simples e padronizada para todos os tipos de documentos e ERPs, com foco na performance da solução para o cliente final e na agilidade de atendimento para as equipes de suporte;

b)      O padrão de comunicação entre os ERPs TOTVS e a NeoGrid é realizado de forma assíncrona com troca de documentos no formato XML em diretórios;

c)       Existem dois tipos de integração do ponto de vista dos ERPs: envio de documentos e recebimento de documentos;

d)      A NeoGrid deve instalar um aplicativo client denominado ‘ClientEDI NeoGrid’ no ambiente de cada cliente;

e)     Para cada tipo de documento todos os ERPs TOTVS devem utilizar o mesmo layout de integração com a NeoGrid.

Os processos de envio/recebimento são estruturados em arquivos XML e disponibilizados em diretórios definidos. A solução NeoGrid  processa a leitura dos arquivos XML, faz a comunicação com os webservices da SEFAZ e retorna as consultas destes documentos. Estes, por sua vez, deverão ser lidos e interpretados através da execução de JOBs específicos pelo ERP TOTVS Linha RM para a devida atualização dos dados no sistema.

No diretório parametrizado para o ClientEDI Neogrid teremos a seguinte estrutura para a manipulação de arquivos XML:

|  |  |
| --- | --- |
| **Subpasta** | **Descrição** |
| \IN | Arquivos retornados pelo ClientEDI a serem processados |
| \OUT | Arquivos disponibilizados pelo ERP a serem enviados |
| \SENT | Arquivos enviados com sucesso pelo ClientEDI à SEFAZ |
| \TMP | Arquivos em manipulação pelo ClientEDI |
| \ERROR | Arquivos processados com erro pelo ClientEDI |
| \RM\TMP | Arquivos em manipulação pelo JOB ERP |
| \RM\ERROR | Arquivos processados com erro pelo JOB ERP |
| \RM\RECEBIDAS | Arquivos processados com sucesso pelo JOB ERP – são excluídos se houver sucesso |

A nomenclatura dos arquivos XML nos diretórios, tanto para envio como retorno, deve seguir a padronização:

[Tipo do Documento]\_[Timestamp]\_[Coligada]\_[IdMov]\_[Número sequencial].xml

Onde:

* [Tipo de Documento] é o código do tipo de documento
* [Timestamp] é a data e hora no formato “yyyyMMddHHmmssSSS”
* [Coligada] é o código da Coligada do documento
* [IdMov] é o código Identificador do Movimento

[Número sequencial] é um número sequencial de quatro dígitos (**opcional**)
