---
content_hash: 73909c00ccc5bd3205ac2721565538ee38a9900e30fd69c94575265f817966fc
fetched_at: '2026-06-29T00:10:57.842251+00:00'
page_id: '600114195'
product: rm
source: tdn-rm
title: 10515404 FISCAL01-14552 DT Divergência na geração do EFD PIS/COFINS e EFD ICMS/IPI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=600114195
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS BackOffice |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Ticket: | 10515404 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14552 |

## **02. SITUAÇÃO/REQUISITO**

Cliente deseja que no SPED Fiscal e EFD Contribuições, o Registro 0200, no campo 3 (Descrição do Item) as informações dos caracteres especiais sejam geradas da mesma forma.

O cliente utiliza o TIF, e informou que o SPED Fiscal gera com caractere especial. Já o EFD Contribuições não.

Com isso, ao cruzar as informações no TIF é apresentada inconsistência.

## **03. SOLUÇÃO**

Criação de um check na tela de parâmetros de geração do SPED Fiscal, na pasta Personalização, para indicar que a descrição do item deverá ser gerada retirando os **caracteres especiais\*** conforme já ocorre na EFD Contribuições.

**\*** Lista de caracteres especiais que são substituídos por espaço:

| ~´`^ªº§¢£³²¹¬°>< |
| --- |

**Obs.:** Caracteres acentuados são substituídos por não acentuados.
