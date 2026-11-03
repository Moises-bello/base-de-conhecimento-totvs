---
article_id: 360040816954
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 389ebc24b8b305855d549cdf8d31cb4acee0ae285747e78f5bbfd5168596fab3
fetched_at: '2026-06-28T22:39:30.542304+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como gerar uma nota
  fiscal de ajuste?
type: support-article
updated_at: '2024-12-09T17:37:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040816954-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gerar-uma-nota-fiscal-de-ajuste
---

**Dúvida**Como gerar uma nota fiscal de ajuste?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Neste caso pode ser gerado uma nota de AJUSTE onde os campos quantidade, valor unitário, valor total, base de ICMS e base de IPI devem sair zerados no Danfe.  
  
No TES deixe o campo F4\_AJUSTE com SIM.  
  
Como o Sistema não tem um tratamento especifico para notas de Ajuste, gere uma nota de complemento de ICMS.

Na emissão da Nota Fiscal, por ser complemento de ICMS, informe no campo **Docto. Orig. (D1\_NFORI)**  qualquer texto que faça sentido.  
  
O TES utilizado não deve gerar nenhuma informação dos impostos, mas deve ter uma fórmula no campo F4\_FORMULA para que as tabelas Livros Fiscais (SF3) e Livros Fiscais por Item de NF (SFT) sejam preenchidas e a nota transmitida.  
  
**Configuração necessário de TES**:

Credita ICMS =Não  
Calcula ICMS = Não  
Gera Duplicata = Sim  
Livro Fiscal=Outros  
Agrega Solidário = Não  
Fórmula = Amarrar uma fórmula com conteúdo texto = **Complemento**, para que o Sistema não destaque o ICMS normal nos livros.  
  
Com isso a nota é transmitida e os valores no Danfe são zerados. Mas é necessário informar um valor para os campos Valor Unitário e Valor Total.
