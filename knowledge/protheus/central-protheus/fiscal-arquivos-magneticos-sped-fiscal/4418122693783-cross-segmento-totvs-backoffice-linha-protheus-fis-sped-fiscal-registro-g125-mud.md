---
article_id: 4418122693783
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 55e6c72c6542037a81a9d764fe03cf164d1aaff0b0bb0a684b39a7a7ab2da1e3
fetched_at: '2026-06-28T22:42:00.802826+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - SPED FISCAL - Registro
  G125 -  mudança no Regime de Tributação de Normal para Simples Nacional
type: support-article
updated_at: '2022-01-19T18:42:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418122693783-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-SPED-FISCAL-Registro-G125-mudan%C3%A7a-no-Regime-de-Tributa%C3%A7%C3%A3o-de-Normal-para-Simples-Nacional
---

**Dúvida**

Cliente adquiriu ativo imobilizado de fornecedor o qual na data de emissão do documento fiscal era optante do **Regime Normal de Apuração**, se creditando de \*ICMS PROPRIO e \*Diferencial de alíquotas no Livro CIAP na apropriação realizada através da rotina **MATA906** e gerando os registros do **SPEDFISCAL Bloco G (G125...G140)** corretamente.

Durante o período no qual esta se apropriando das parcelas, houve uma alteração no cadastro de Fornecedor (**campo A2\_SIMPNAC = 1-Sim**), devido a mudança de regime do fornecedor para Simples Nacional, fazendo com que o Registro G125 Campo 05 não fosse escriturado conforme o valor da parcela de apropriação calculado na entrada da nota fiscal, ou seja, antes do Fornecedor sofrer alteração de regime de tributação.

Isto ocorria porque na hora de geração do SPED Fiscal, para identificar se o fornecedor estava enquadrado no Simples Nacional era lido o conteúdo do campo A2\_SIMPNAC que pode ser alterado a qualquer momento.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - Todas as versões  
  
**Solução**

De modo que o contribuinte adquirente da mercadoria destinada ao ativo imobilizado, possa se creditar do valor do ICMS constante no documento fiscal que acobertou a operação de aquisição, independentemente do novo regime de tributação e da alteração do campo A2\_SIMPNAC no Cadastro de Fornecedor, foram ajustadas as regras e rotinas **MATA906.PRW** (Estorno do CIAP), **SPEDXFUN.PRW** e **SPDBLOCOG.PRW** (SPEDFISCAL) para considerar como Simples Nacional o **novo campo F9\_SIMPNAC** (Optante Simples Nacional) criado na Tabela SF9 - Manutenção CIAP.   
  
Para a geração dos registros G125 e G140 do SPEDFISCAL contemplando as alterações acima será necessária a criação do campo F9\_SIMPNAC (Optante Simples Nacional).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418138600599/mceclip0.png)

**Preenchimento do campo**

Quando criado o campo F9\_SIMPNAC, o mesmo será preenchido de forma automática na funcionalidade **Apropriar da rotina MATA906 - Estorno do CIAP**, conforme regras a seguir, executada na primeira apropriação realizada após criação do campo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418116685591/mceclip2.png)

1. **Bem inserido através de Documento de Entrada**, o sistema irá buscar no Documento de Entrada correspondente a informação constante no campo F1\_SIMPNAC, para identificar se o Fornecedor na ocasião de lançamento do Documento Fiscal de Entrada estava configurado como Simples Nacional (F1\_SIMPNAC = "1-Sim"), preenchendo o campo F9\_SIMPNAC = "1 - Sim" caso F1\_SIMPNAC = "1 - Sim" ou caso contrário preencherá o campo F9\_SIMPNAC = '2 - Não'.
2. **Caso não localize o Documento de Entrada** correspondente, geralmente inclusão direta na rotina MATA905 - Manutenção do CIAP, irá buscar a informação no campo A2\_SIMPNAC do Cadastro de Fornecedor, preenchendo o campo F9\_SIMPNAC = "1 - Sim" caso A2\_SIMPNAC = "1 - Sim', caso contrário preencherá o campo F9\_SIMPNAC = '2 - Não'.

**Importante!**

**É muito importante e extrema atenção quando o bem foi incluído pela Tabela de Manutenção CIAP, inclusão pelo Ativo Fixo ou Integração entre sistemas,** para estes casos o sistema irá considerar a informação do campo A2\_SIMPNAC do Cadastro do Fornecedor, e isto não quer dizer que quando foi realizada a aquisição do bem esta informação era daquele momento. Por este motivo, será possível a alteração do campo F9\_SIMPNAC diretamente através da rotina MATA905 - Manutenção do CIAP.

Entendimento formalizado pela Consultoria Tributária de Segmentos  
  
![](https://tdn.totvs.com/download/attachments/657538746/image2021-12-29_15-57-23.png?version=1&modificationDate=1640804243677&api=v2)

[EFD-ICMS/IPI - Registro G125 - Alteração de Regime do Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=642948725)

## 

## **ASSUNTOS RELACIONADOS**

[FIS0009\_Manual\_Utilização\_SPEDFISCAL#REGISTROSG110,G125,G130EG140](https://tdn.totvs.com/pages/viewpage.action?pageId=238035285#FIS0009_Manual_Utiliza%C3%A7%C3%A3o_SPEDFISCAL-REGISTROSG110,G125,G130EG140).

[SPDFIS - Sped Fiscal](https://tdn.totvs.com/display/PROT/SPDFIS+-+Sped+Fiscal)
