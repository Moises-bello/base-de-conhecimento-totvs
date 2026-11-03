---
article_id: 360046326093
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: eb8da46f3fc7af7cb860d7375026d29e539c6b6840b953fd312e030de62357c6
fetched_at: '2026-06-28T22:42:03.858750+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - LIVROS FISCAIS - Registro 1900  e filhos EFD ICMS/IPI escriturando indevidamente
  no arquivo do SPED FISCAL
type: support-article
updated_at: '2021-04-28T14:25:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046326093-MP-LIVROS-FISCAIS-Registro-1900-e-filhos-EFD-ICMS-IPI-escriturando-indevidamente-no-arquivo-do-SPED-FISCAL
---

**Dúvida**Ao gerar o arquivo da EFD ICMS/IPI esta sendo escriturado o registro 1900 e filhos indevidamente.  
 **Ambiente**Microsiga Protheus - A partir da versão 12  
  
**Solução**

Se o campo "Nr. Livro"(F4\_NRLIVRO) no TES for deixado em branco e na geração da Apuração de ICMS (MATA953) e do arquivo Sped Fiscal não for informado no campo "Livro" asterisco (\*), para geração de todos os livros, os registros 1900 e filhos serão gerados considerando que livro em branco trata-se de uma sub-apuração.

Porém, caso haja necessidade de utilização dessa configuração do campo em branco e não seja necessária a geração dos registros 1900 e filhos, o parâmetro MV\_RLCSPD deve ser configurado somente informando {}, com esta configuração não serão gerados os registros referente a sub-apuração.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065409693/mceclip0.png)

Informações adicionais:

Manual Utilização SPEDFISCAL

<https://tdn.totvs.com/pages/releaseview.action?pageId=238035285>

FIS0005\_SPED\_FISCAL

<https://tdn.totvs.com/display/public/PROT/FIS0005_SPED_FISCAL>
