---
content_hash: 0b185f8c20d84bf9869d57ac7cb5d5ea2699aaca76655a1bbd58ecb52305bdea
fetched_at: '2026-06-29T00:10:41.864437+00:00'
page_id: '546673504'
product: rm
source: tdn-rm
title: 6149897 FISCAL01-9911 DT ECF - Registro 0930 - Própria Empresa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546673504
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | ECF |
| Ticket: | 6149897 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-9911 |

## **02. SITUAÇÃO/REQUISITO**

ECF Criar Cadastro de Signatários para geração do Registro 0930

## **03. SOLUÇÃO**

Ajustada a Geração do Registro 0930 da ECF para quando o Parâmetro "Segunda Assinatura - Própria Empresa"  
estiver marcado o sistema gere a segunda linha do registro 0930 com os dados da Filial e não  
com o do Representante como e hoje, com o Parâmetro desmarcado o comportamento do sistema mantém,  
com os dados do Contador e Representante.
