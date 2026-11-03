---
content_hash: 876cd0de45df0bb47c655e31c946200eeafb4685d53468c93c297b842d10ccd9
fetched_at: '2026-06-29T00:09:19.463514+00:00'
page_id: '422543460'
product: rm
source: tdn-rm
title: 3930451 FISCAL01-6577 - DT - DEISS Indaiatuba SP
type: documentation
url: https://tdn.totvs.com/display/LRM/3930451+FISCAL01-6577+-+DT+-+DEISS+Indaiatuba+SP
version: 3
---

Tempo aproximado para leitura:**02 min**

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | Gestão Fiscal |
| Função: | DEISS Indaiatuba SP |

**02. SITUAÇÃO/REQUISITO**

- O campo 20 não considera a opção "Optante pelo Simples" do cadastro do Cliente\Fornecedor.

- O campo 23 "Regime Especial" não é gerado.

**03. SOLUÇÃO**

**CAMPO 20:** Realizada alterações no Layout  para que o campo 20 seja gerado com base na informação "Optante pelo Simples" informado no cadastro   
do Cliente\Fornecedor.

**CAMPO 23:** Realizada alterações no Layout e Contexto para que o campo 23 seja gerado através do campo "Regime Especial de Tributação" disponível nos dados fiscais da Filial.

O campo 23 vai ser gerado quando for informado as seguintes opções:

Opções:

*1 → Microempresa Municipal;*  
*2 → Estimativa;*  
*3 → Sociedade de Profissionais;*  
*4 → Cooperativa;*  
*5 → Microempresário Individual (MEI);*  
*6 → Microempresário e Empresa de Pequeno Porte (MEEPP).*

Caso seja informado uma opção não aceita pela DEISS Indaiatuba o campo será gerado em branco.
