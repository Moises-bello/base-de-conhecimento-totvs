---
content_hash: 4e1e46a1206e02248fc93cf903cb1cb3ef9218df1f3f04cc42869bf883c6e75b
fetched_at: '2026-06-29T00:09:23.959632+00:00'
page_id: '422546176'
product: rm
source: tdn-rm
title: Geração do Registro C176
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546176
version: 32
---

Conforme o manual, a obrigatoriedade e a forma de escrituração deste registro serão definidas pela UF de domicílio do contribuinte.  
  
A inclusão da Referencia do Item é somente para Gerar o Registro C176, por este motivo não vamos tratar no processo de Escrituração e no "TOTVS Gestão de Estoques, Compras e Faturamento".  A Referencia do Item deve ser incluída manualmente.  
  
Este Registro deve ser gerado para todos os lançamentos de saída interestaduais e que tenha destaque do valor do ICMS ST.  
O registro filho do Registro C170, então será necessário para o Tipo de Documento 55(NF-e), será necessário gerar o Registro C170 somente para os Item que tem referência preenchida.

****O****bservação*****:* Atualmente já geramos este registro para os lançamentos de entrada ou saída que possuem lançamento referenciados com os seguintes CFOP's: 5.603, 6.603, 1.603 e 2.603.

* **Lançamento Fiscal**

Habilitado no Item do Lançamento Fiscal, pasta a Sub Pasta Referencia (Tabela DITEMREFERENCIA) somente para: Lançamento de Saída; Com CFOP do Grupo 6.4xx - Saídas de Mercadoria Sujeitas ao Regime de Substituição; Regra de ICMS – Tipo de Operação "Substituição Tributaria";

* **Importação de Lançamento Fiscal Delphi**

Este novo campo não será importado no processo Delphi, apenas na importação .Net(Web Service).

* **Geração do Registro C176 no SPED Fiscal (código 01, 55)**

Alterada a consistência existente  na geração do Registro C176.  
Este Registro deve ser gerado somente para os Itens que geram direito ao Ressarcimento da ST e que a Referencia por Item esteja informada.  
Ao gerar os Registros C100 e C190 dos Lançamentos de Saída com o Tipo de Documento 55(NFe), será gerado o Registro C170 somente dos Itens que tem Referencia informado.  
Este registro deve ser informado quando da escrituração de documento fiscal, que acoberte operação que represente desfazimento de substituição tributária realizada em operações anteriores.  
O documento informado neste registro deverá ser diferente do documento informado no registro pai (C100), pois é o documento referente à(s) última(s) aquisição(ões) da mercadoria e à retenção do imposto.  
A obrigatoriedade e a forma de escrituração deste registro serão definidas pela UF de domicílio do contribuinte, inclusive sobre a apresentação dos campos: CHAVE\_NFE\_RET; COD\_PART\_NFE\_RET; SER\_NFE\_RET; NUM\_NFE\_RET;ITEM\_NFE\_RET.  
  
Este registro não se aplica a contribuintes que utilizam o SCANC. 

***Observação***: Os campos 09, 12, 13, 14, 15 e 17 do registro C176 são gerados com base no valor unitário do item. O valor final calculado será dividido pela quantidade de itens.  
Este registro será gerado para todas as referências do mesmo item.  
  
Este registro será gerado para todas as operações de saída em quem o parâmetro "Operação com Ressarcimento de ST na Compra" estiver habilitado na Natureza de Operação (CFOP) associado ao Lançamento ao Lançamento Fiscal.

**Novos campos Layout 2019:**

* **Registro C170: Itens do Documento (01, 1B, 04 e 55)**

Inclusão do campo 38 - VL\_ABAT\_NT (Valor do abatimento não tributado e não comercial).

Este campo será gerado com o valor do campo "ICMS Desonerado" do Item quando a flag  
"ICMS Deson. Não afeta Valor Contábil" não estiver marcada.

Obs.: Mesma Regra para preenchimento do campo no Registro C100.

* **Registro C176: Ressarcimento de ICMS e Fundo de Combate a Pobreza (FCP) Em operações com ST (Código 01, 55)**

Incluída a opção "6 – Venda interna para Simples Nacional" no campo 19 - COD\_MOT\_RES (Código do motivo do ressarcimento).  
  
O preenchimento desse campo é realizado junto a Referência informada no Item do Lançamento Fiscal:

Inclusão do campo 27 - VL\_UNIT\_RES\_FCP\_ST (Valor unitário do ressarcimento (parcial ou completo) de FCP decorrente da quebra da ST).  
Campo gerado de acordo com o campo VlrICMSItemFCPEstDEST do Item do Lançamento Fiscal.  
  
Gerado com a informação do campo "Valor ICMS FCP"

[Portaria CAT 158 de 2015 - Ressarcimento ICMS Retido por Sujeição Passiva de Substituição Tributaria](https://portal.fazenda.sp.gov.br/servicos/st/Paginas/Ressarcimento-de-Substitui%C3%A7%C3%A3o-Tribut%C3%A1ria-do-ICMS.aspx).
