---
content_hash: f6f9209abd506c295dd0b234aa5c93d0139eb8debce5f5c6411735598d7b9992
fetched_at: '2026-06-29T00:10:52.269215+00:00'
page_id: '571528266'
product: rm
source: tdn-rm
title: FISCAL01-12885 DT Persistência das preferências do usuário no SPED Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=571528266
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração do arquivo EFD ICMS\IPI |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12885 |

## **02. SITUAÇÃO/REQUISITO**

Implementação da persistência das preferências do usuário na parametrização da rotina EFD ICMS IPI "SPED Fiscal" por usuário.

## **03. SOLUÇÃO**

No formulário do SPED Fiscal foi adicionado a opção "Gravar Preferências do Usuário", com esta opção habilitada serão salvos todos os parâmetros definidos na execução do processo, e na próxima vez em que for executado os parâmetros serão carregados novamente automaticamente.
