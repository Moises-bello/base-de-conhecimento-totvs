---
article_id: 360053885593
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: c7b0a79787ed98c4a64e52947c4fa510ad659ddf4bb35e983d4ed73158d70cb9
fetched_at: '2026-06-28T22:45:21.121193+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: MP - TAF - Inconsistência na criação da interface de integração TAFST1
type: support-article
updated_at: '2021-04-28T14:28:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053885593-MP-TAF-Inconsist%C3%AAncia-na-cria%C3%A7%C3%A3o-da-interface-de-integra%C3%A7%C3%A3o-TAFST1
---

**Dúvida**  
- TAFST1 | Criação da tabela >> Encontrada uma inconsistência na criação da interface de integração TAFST1: [Não foi possível utilizar a conexão ODBC/dbAccess fornecida; avaliar a inconsistência apresentada no item anterior "Validação de Conexão".] >> [Sem informações complementares]  
  
 **Ambiente**  
Protheus – TAF – A partir da versão 12  
  
**Solução**  
O erro apresentado acima no momento de tentativa de criação da tabela TAFST1 e por motivo do Alias do banco e porta não estarem informados corretamente, para correção, será necessário revisar as configurações dos parâmetros abaixo:

MV\_VAUTCON = EM BRANCO  
MV\_TAFTALI = "Deve ser informado no nome do TOPALIAS do seu ambiente dentro do appserver.ini"  
MV\_TAFTDB = "Deve ser informado nome do banco do seu ambiente Exemplo MSSQL ou MSSQL7 informado no seu TOPBASE dentro do appserver.ini"  
MV\_TAFPORT - Indica o numero da porta do serviço do TopConnect  
MV\_TAFVER - Release corrente do TAF  
MV\_TAFWIZ =.T.  
MV\_TAFINT = .T.  
  
Execute a Wizard dentro do TAF Atuazações >Config.TAF> Wizard de Configuração  
  
Caso ocorra algum incidente por favor encaminhar o console.log e console.bak abaixo encaminho a configuração para ativar o console.log
