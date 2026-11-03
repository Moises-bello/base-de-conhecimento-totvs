---
content_hash: 10ef9e34a90be3a69838ad6fe50adc29e626708f092f9c748995d00df1a15bf5
fetched_at: '2026-06-29T00:05:50.908008+00:00'
page_id: '1045014658'
product: rm
source: tdn-rm
title: Nota Técnica Nº 007 - RTC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1045014658
version: 12
---

# Conteúdo

2Conteúdononenone

# 1. Sobre

A Nota Técnica SE/CGNFS-e nº 007 atualiza e corrige o layout da NFS-e Modelo Nacional, com foco no tratamento das informações de PIS e COFINS, no reforço das regras de validação e no esclarecimento de pontos operacionais que vinham gerando interpretações divergentes após a entrada em vigor da Reforma Tributária do Consumo (RTC).

A NT promove ajustes em domínios de campos, regras de cálculo e validação, atualiza a tabela de Indicador da Operação (cIndOp) e publica novos schemas, alinhando o preenchimento da NFS-e à legislação vigente e preparando o documento para a transição ao modelo de tributação do IBS e da CBS.

# 2. Cronograma

Esta Nota Técnica entra em vigor a partir de:

* Produção Restrita (homologação/testes):
* Produção:

# 3. Principais Alterações

A solução está disponível a partir dos patches:

Biblioteca RM:

* 12.1.2506.260
* 12.1.2510.180
* 12.1.2602.104

TSS:

* 12.1.2210:<https://r.totvs.io/p/1238272> ;
* 12.1.2310:<https://r.totvs.io/p/1238273> ;
* 12.1.2410:<https://r.totvs.io/p/1238274> ;
* 12.1.2510:<https://r.totvs.io/p/1238275> ;

Mais informações sobre atualizações do TSS: [Como atualizar o TSS para atender a NT 007](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38633010187543-Cross-Segmentos-TOTVS-Backoffice-Linha-RM-Doc-Eletr%C3%B4nicos-Como-atualizar-o-TSS-para-atender-a-NT-007)

OBS: A versão do TSS é independente da versão do RM.

Com estes patches foram realizadas as seguintes alterações na montagem do xml da Nota:

## 3.1 Grupo DPS/infDPS/valores/trib/tribFed/

Detalhes:

## 3.2 Grupo DPS/infDPS/valores/trib/tribFed/piscofins/

* O campo ***vRetCSLL*** passa a ser gerado com o somatório dos valores de retenções de PIS, de COFINS e/ou de CSLL.
* Novos CSTs passam a ser considerados na geração do grupo. O código é gerado conforme informado no tributo no item do movimento.
* Nos campos **vPis** e **vCofins** passam a ser considerados apenas os valores de PIS e COFINS não Retidos.
* Alterada a geração do campo ***tpRetPisCofins.*** Foram conservados os valores atuais aceitos para esse campo (1 e 2) e adicionados novos valores de 3 a 9 e 0.

A regra para geração do campo é a seguinte:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Se não houver os tributos IBS/CBS   | **Código** | **PIS Retido?** | **COFINS Retido?** | | --- | --- | --- | | **1** | Sim | Sim | | **2** | Não | Não |   Se houver IBS/CBS   | **Código** | **PIS Retido?** | **COFINS Retido?** | **CSLL Retida?** | | --- | --- | --- | --- | | **0** | Não | Não | Não | | **3** | Sim | Sim | Sim | | **4** | Sim | Sim | Não | | **5** | Sim | Não | Não | | **6** | Não | Sim | Não | | **7** | Não | Sim | Sim | | **8** | Não | Não | Sim | | **9** | Sim | Não | Sim | |

Detalhes:  e 

## 3.3 Grupo NFSe/infNFSe/DPS/infDPS/valores/trib/totTrib

Alterada a regra de geração do grupo para ser possível a geração do subgrupo vTotTrib mesmo que todos seus valores estejam zerados.

Detalhes:  e

# 4. Legislação

Este documento foi elaborado com base na [Nota Técnica SE\CGNFS-e nº 007](https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/rtc) publicada no Portal da Nota Fiscal de Serviço eletrônica.

# 5. Documentação completa

O Layout completo de integração com a NFS-e Nacional pode ser consultado .
