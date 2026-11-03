---
content_hash: e25faab254f4b489554ae0500d2b569d8296a29e9df5368304839e767abdcb25
fetched_at: '2026-06-29T00:10:31.754311+00:00'
page_id: '522007791'
product: rm
source: tdn-rm
title: FISCAL01-11498 DT REGISTRO 0002 - SPED Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-11498+DT+REGISTRO+0002+-+SPED+Fiscal
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração do Arquivo SPED Fiscal (EFD ICMS\IPI) |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11498 |

## **02. SITUAÇÃO/REQUISITO**

O Registro 0002 deve ser gerado quando o campo 15 do Registro 0000 for informado com "**0 -** **Industrial ou equiparado a industrial**".

1. Criar o campo "Classificação do Estabelecimento" na tela de geração do SPED com as seguintes opções:

* Industrial - Transformação
* Industrial - Beneficiamento
* Industrial - Montagem
* Industrial - Acondicionamento ou Reacondicionamento
* Industrial - Renovação ou Recondicionamento
* Equiparado a industrial - Por opção
* Equiparado a industrial - Importação Direta
* Equiparado a industrial - Por lei específica
* Equiparado a industrial - Não enquadrado nos códigos 05, 06 ou 07
* Outros

2. Implementar a geração do Registro 0002 informando no campo 02 a opção selecionada no campo criado no item 1.

## **03. SOLUÇÃO**

Na tela de geração do SPED Fiscal foi adicionado um campo referente a “Classificação do Estabelecimento” e uma consistência para geração do Registro 0002, que será apenas gerado quando o Tipo de Atividade estiver parametrizado como “Industrial ou Equiparado a Industrial”.
