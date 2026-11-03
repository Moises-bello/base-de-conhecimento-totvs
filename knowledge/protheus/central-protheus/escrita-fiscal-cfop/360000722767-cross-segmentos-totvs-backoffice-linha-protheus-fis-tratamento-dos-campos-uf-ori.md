---
article_id: 360000722767
category: Escrita Fiscal - CFOP
content_hash: b2e88781d78df8859767340c87b73a350c7508262334b5e081ed627303308ad9
fetched_at: '2026-06-28T22:39:35.941133+00:00'
product: protheus
section_id: 1500001538541
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Tratamento dos campos
  UF origem transporte (F1_UFORITR), município origem transporte (F1_MUORITR), UF
  destino transporte (F1_UFDESTR) e município destino transporte (F1_MUDESTR)
type: support-article
updated_at: '2021-07-01T13:28:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000722767-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Tratamento-dos-campos-UF-origem-transporte-F1-UFORITR-munic%C3%ADpio-origem-transporte-F1-MUORITR-UF-destino-transporte-F1-UFDESTR-e-munic%C3%ADpio-destino-transporte-F1-MUDESTR
---

**Dúvida**

Qual Tratamento dos Campos UF Origem Transporte (F1\_UFORITR), Município Origem Transporte (F1\_MUORITR), UF Destino Transporte (F1\_UFDESTR) e Município Destino Transporte (F1\_MUDESTR) ?

**Ambiente**

Protheus Fiscal - Todas Versões Protheus

**Solução**

Criado os campos UF Origem Transporte (F1\_UFORITR), Município Origem Transporte (F1\_MUORITR), UF Destino Transporte (F1\_UFDESTR) e Município Destino Transporte (F1\_MUDESTR) para o novo tratamento de escrituração de Conhecimento de transportes.

Estes campos estão localizados na aba Informações Adicionais do documento de entrada (MATA103).

Com a criação destes campos o tratamento para a gravação da UF (F1\_EST) e do CFOP foram alterados.

Observe que o campo "UF origem" no cabeçalho do documento será gatilhado com o mesmo conteúdo informado no campo UF Origem Transporte (F1\_UFORITR), pois este campo se refere a origem do transporte.

Quando não forem informados os estados nos campos UF Origem Transporte/ UF Destino Transporte no documento de entrada, será considerado o estado da filial processada e do Fornecedor para conversão do CFOP.

**Para maiores informações Consulte a documentação completa no Link abaixo:**

<http://tdn.totvs.com/display/PROT/DOC0055+Tratamento+dos+Campos+F1_UFORITR+e+F1_UFDESTR>
