---
article_id: 360051943934
category: Financeiro - Contas a Receber
content_hash: 308d757cffe049b2c63f2ab8831e0db51dcb612e3c3f05aeeeb581b02c9e9910
fetched_at: '2026-06-28T22:38:12.662587+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - CTBAFIN - Lançamentos Contábeis Off-Line na baixa de arquivos
  CNAB
type: support-article
updated_at: '2025-10-13T21:51:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051943934-MP-SIGAFIN-CTBAFIN-Lan%C3%A7amentos-Cont%C3%A1beis-Off-Line-na-baixa-de-arquivos-CNAB
---

**Dúvida**Ao baixar o arquivo de **CNAB** na rotina **FINA200** não é contabilizado **Lançamentos** **Contábeis** - **off line** do LP521 ?

**Ambiente**Microsiga Protheus – Financeiro – CTBAFIN – A partir da versão 12.0  
  
**Solução**Validar se está sendo utilizada a LP correspondente à chamada do processo que deseja realizar.

**Exemplo**:   
Se utilizar o **Lançamento Padrão** 521 para o processo de baixa do **Cnab**, que se destina à contabilização de **Cobrança Simples** ou **Cartório** (1/H) e os títulos enviados na remessa foram de Cobrança Vinculada, não será chamada a contabilização, sendo o correto o LP 524.

**Importante:**Por tratar diversas situações de títulos no retorno do **Cnab**, poderão ser usados diversas LP´s no processo.

**Saiba Mais:**Lançamentos Padrão Financeiro Classificado por Macro Processos<https://tdn.totvs.com/display/public/PROT/FIN0026_LPAD_lancamento_padrao_por_macro_processo>

**Lançamentos Padrão Financeiro**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=235585410>
