---
article_id: 360041783513
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 44ddaf7b30d562e7c136b4277e3278d30e0badc9437a51bd186374add31a684f
fetched_at: '2026-06-28T22:42:00.945135+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Livro Fiscal
  - Como preencher o campo 9 COD_CONS do registro C500 no Sped Fiscal
type: support-article
updated_at: '2025-02-11T22:06:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041783513-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Livro-Fiscal-Como-preencher-o-campo-9-COD-CONS-do-registro-C500-no-Sped-Fiscal
---

**Dúvida**Como preencher o campo 9 - COD\_CONS do registro C500 no Sped Fiscal  
   
**Solução**

- Preencher o campo **Espécie** do Documento de Entrada ou Saída = **NFCEE**,**NFCFG** ou **NFFA**

- Entrar na MATA910 ou MATA920, pelo caminho > Ambiente: 09 (Livros Fiscais) > Atualizações > Movimentos > Nota Fiscal Manual de Entrada MATA910  ou  Nota Fiscal Manual de Saída MATA920  > Outras Ações > Complementos:

- Marcar a linha, referente o documento de entrada ou saída:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055921113/mceclip1.png)  
   
 ​  
 Se Espécie = **NFCEE**(Modelo: 06 Nota Fiscal/Conta de Energia Elétrica)  
 Preencher campos: **FU\_CLASCON, FU\_VALTERC e FU\_CONSTOT**  
   
 ​​![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055047834/mceclip2.png)  
  
   
 Se Espécie== **NFCFG**(Modelo: 28 Nota Fiscal/Conta de Fornecimento de Gás Canalizado)  
 Preencher campos: **CD3\_CLASCO e CD3\_VLTERC**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055924473/mceclip3.png)  
 ​  
 Se Espécie = **NFFA** (Modelo: 29 Nota Fiscal/Conta de Fornecimento de Água Canalizada)  
 Preencher campos: **CD4\_CLASCO e CD4\_VLTERC**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055048854/mceclip4.png)

Para as notas canceladas do modelo 29 (NFFA), existe o tratamento na tabela SF3 para gravar a classe de consumo. 

Como o complemento foi excluído ao deletar a nota, deve-se pegar o código na tabela SF3, pois na CD4 não irá existir mais.

Tratamento feito para evitar que o C600 seja gerado sem a classe de consumo, o que ocasiona erro no validador. 

If cSituaDoc$"02#04#05#03" .And. Empty(cCodCons) .And. aRegC500[1][5] == "29" .And. lClasCo  
cCodCons := SF3->F3\_CLASCO  
   
   
**Observação**: Campo 09 (COD\_CONS) - Valores válidos e validação: Se o modelo for 06 (energia elétrica) ou 28 (gás canalizado), os valores válidos são [01, 02, 03, 04, 05, 06, 07, 08]. Se o modelo for 29 (água canalizada), o valor deve constar da Tabela 4.4.2 da Nota Técnica, instituída pelo Ato COTEPE/ICMS nº 44/2018 e alterações. Se o modelo do documento for 66, o campo não deve ser preenchido.  
   
 - Código de classe de consumo de energia elétrica ou gás:  
 01 - Comercial  
 02 - Consumo Próprio  
 03 - Iluminação Pública  
 04 - Industrial  
 05 - Poder Público  
 06 - Residencial  
 07 - Rural  
 08 - Serviço Público.  
   
   
 - Link com o Código de classe de consumo:  
   
 <http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal>

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055919693/mceclip0.png)
