---
content_hash: 53cbad3c9e5a96d04c22c846456f884b697b3a977117d0eb420c742f470524e7
fetched_at: '2026-06-29T00:08:39.792806+00:00'
page_id: '286021380'
product: rm
source: tdn-rm
title: Data de emissão - Lançamento financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286021380
version: 104
---

# ATA DE EMISSÃO - LANÇAMENTO FINANCEIRO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Educacional* |
| **Rotina:** | Geração de lançamentos |

## Descrição

Melhoria para permitir a parametrização da forma que será obtida a data de emissão de um lançamento financeiro, gerado através do TOTVS Educacional.

**Configuração no Totvs Gestão Educacional**

Os parâmetros estão disponíveis em: **Totvs Gestão Educacional | Configurações | Parâmetros | Integração | Financeiro | Educacional | Fin - Geral 4/4**

**Parâmetros**

* **Utilizar**  
  Informa se a data de emissão do lançamento será a data do sistema na geração do lançamento ou se será assumido a data do contrato. Essa parametrização é utilizada para qualquer lançamento gerado através de uma parcela do plano de pagamento.  
  Caso a opção selecionada seja a data do contrato, nos casos onde o campo "Data do Contrato" não esteja devidamente preenchido no contrato em que a parcela pertence, não será possível a geração do lançamento;

* **Utilizar em parcela extra**  
  Informa se a parametrização  realizada será aplicada para lançamentos gerados através de parcelas extras;
* **Utilizar em parcela adicional**  
  Informa se a parametrização realizada será aplicada para lançamentos gerados através de parcelas adicionais;

* **Em dia não útil**  
  Como proceder quando a data de emissão obtida através da parametrização irá se comportar quando não for um dia útil;

* **Mantém data de emissão ao regerar lançamento**  
  Se a data de emissão obtida anteriormente, na geração do lançamento, será mantida ao regerar o lançamento;

## Vídeo

divs
