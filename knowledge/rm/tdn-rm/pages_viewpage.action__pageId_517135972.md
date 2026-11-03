---
content_hash: 319d27865963a0dc2aea774c600f6fba9b212ec1f65e782f7bba970d2bf17598
fetched_at: '2026-06-29T00:10:27.955098+00:00'
page_id: '517135972'
product: rm
source: tdn-rm
title: FISCAL01-10384 DT EFD-REINF Implementação do Anexo de Histórico dos Eventos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=517135972
version: 2
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Anexo - Histórico dos Eventos |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-10384 |

**02. SITUAÇÃO/REQUISITO**

Implementação do Anexo de Histórico para os Eventos da EFD-Reinf.

**03. SOLUÇÃO**

Foi implementado o histórico dos eventos da EFD-Reinf.

- Implementado o anexo de Histórico de Eventos e associado aos Eventos Cadastrais e Periódicos.  
- Disponibilização da Api Reinf para consulta de histórico de um evento através da url.   
Exemplo de Url: <http://localhost:12130/api/fiscal/v1/eventoreinf/historico/1|1>  
- Ajuste na Api Reinf de exclusão de Eventos para excluir o histórico quando o evento periódico ou cadastral for excluído  
- Implementação do serviço para Inclusão\Exclusão de Histórico.
