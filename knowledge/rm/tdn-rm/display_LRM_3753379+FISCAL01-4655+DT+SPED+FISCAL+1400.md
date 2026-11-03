---
content_hash: 7e88de74a4d47e4e25395231be7d2613deda08b76f4d1e5ab440a287117e0f4d
fetched_at: '2026-06-29T00:09:11.655484+00:00'
page_id: '415695177'
product: rm
source: tdn-rm
title: 3753379 FISCAL01-4655 DT SPED FISCAL 1400
type: documentation
url: https://tdn.totvs.com/display/LRM/3753379+FISCAL01-4655+DT+SPED+FISCAL+1400
version: 2
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | Geração do Arquivo SPED Fiscal |

**02. SITUAÇÃO/REQUISITO**

Cliente solicita que o sistema gere o registro 1400, com base na legislação do Estado da Bahia abaixo

**03. SOLUÇÃO**

No cadastro de Natureza da Operação aba Outros Dados e campo Tipo Natureza (Rotinas Legais) foi adicionado a opção "Adicionado por Município".

Na geração do registro 1400 do Sped Fiscal será considerado lançamento fiscal com Natureza que tenha a opção Tipo Natureza (Rotinas Legais) selecionado como "Adicionado por Município".
