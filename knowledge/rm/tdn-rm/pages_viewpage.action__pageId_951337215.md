---
content_hash: 2798ab4b5639a5c7ff181a5b69786786d8fbc451b1f7520c710e8c3e6bb6b44d
fetched_at: '2026-06-29T00:12:10.124113+00:00'
page_id: '951337215'
product: rm
source: tdn-rm
title: 'FISCAL01-25944 - NFS-e - Os seguintes campos não podem ficar vazios: Código
  NBS não informado (Araras/SP)'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=951337215
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25944 |

## **02. SITUAÇÃO/REQUISITO**

O problema identificado é que a TAG codigo\_nbs não está sendo gerada conforme determina o comunicado da prefeitura. Essa TAG é essencial para o correto preenchimento da NFS-e  pois contém as informações referentes à Nomenclatura Brasileira de Serviços. A ausência ou o preenchimento incorreto dessa informação pode levar à rejeição do documento fiscal eletrônico .  
   
Essa inconsistência pode indicar falhas no sistema de emissão ou desconhecimento técnico das atualizações normativas, sendo necessário que os responsáveis pela emissão da NFS-e  revisem a configuração do sistema utilizado e se atualizem sobre os requisitos legais em vigor.  
   
Alterações no Arquivo XML do NFS-e  
Conforme a nova atualização do SIGISSWEB, foi definido o procedimento para o registro e a comunicação do código NBS, estabelecendo a obrigatoriedade de informar a TAG correspondente a partir de 01/04/2025.

## **03. SOLUÇÃO**

Inclusão da tag <codnbs>, que se refere ao Código NBS, no do grupo de serviços da NFS-e para todos os municípios.

Disponível a partir da biblioteca 12.1.2406
