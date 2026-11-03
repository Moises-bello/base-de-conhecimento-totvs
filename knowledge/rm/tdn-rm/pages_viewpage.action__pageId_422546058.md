---
content_hash: 716a025414f8c1329ba6a4c7ff4cfdd5c8e3fd50e1c5e00e9f4362a17e5a0ff8
fetched_at: '2026-06-29T00:09:23.162433+00:00'
page_id: '422546058'
product: rm
source: tdn-rm
title: Parâmetros da ECF (Outras Informações)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546058
version: 5
---

**Forma de Tributação Lucro Presumido, Imune ou Isenta com Apuração Trimestral**

Este item deverá ser habilitado nos casos em que a apuração do tributo não coincide com o encerramento balanço, exemplo:  
Balanço encerrado anualmente e apuração do tributo trimestral. Neste caso os valores de Débitos X Créditos no Ativo e Passivo não irão fechar. Este recurso é utilizado para gerar no registro K155 uma linha com o valor do encerramento trimestral para que as colunas de Ativo e Passivo fechem ao importar e declaração no PVA da ECF.

Este processo não irá gerar lançamentos contábeis. Estes valores só existirão em tempo de execução da rotina para a geração do arquivo corretamente. Para os períodos que houver a suspensão do balanço estes valores não serão gerados.

Deverá ser informada uma estrutura de [Apuração Virtual](http://tdn.totvs.com/pages/viewpage.action?pageId=423938637) para que o processo seja executado.
