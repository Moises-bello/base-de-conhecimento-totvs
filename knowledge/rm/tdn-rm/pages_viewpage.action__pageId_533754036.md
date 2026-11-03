---
content_hash: 25a3f94063c496c4bc91c729aa33a8e830496fab2c0c736844041708713c2c90
fetched_at: '2026-06-29T00:10:37.040454+00:00'
page_id: '533754036'
product: rm
source: tdn-rm
title: '8075851 FISCAL01-12273 DT NFS-e - Duque de Caxias/RJ: E160 - Arquivo Enviado
  Fora da Estrutura do Arquivo Xml de Entrada.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=533754036
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Envio de NF-e |
| Ticket: | 8075851 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12273 |

## **02. SITUAÇÃO/REQUISITO**

A prefeitura de Duque de Caxias/RJ alterou recentemente o layout da NFS-e.

Ao consultar o cancelamento da NFS-e de Duque de Caxias/RJ ocorre a rejeição:  
E160 - ARQUIVO ENVIADO FORA DA ESTRUTURA DO ARQUIVO XML DE ENTRADA.

A equipe do TSS identificou que o RM não está enviando o código de cancelamento, com isto a prefeitura não realiza o cancelamento da NFS-e.

## **03. SOLUÇÃO**

Ajuste no processo de cancelamento para possibilitar ao usuário a informar o motivo de cancelamento da NFS-e.

1 - Erro Emissão;

2 - Serviço Não Prestado;

3 - Erro Assinatura ;

4 - Duplicidade Nota ;

5 - Erro Processamento;
