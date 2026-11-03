---
content_hash: 7017d4453f7c204bb75fd9ad683c34738deef5ad29fe04e8a7f588aae9fd6909
fetched_at: '2026-06-29T00:09:08.988555+00:00'
page_id: '390409104'
product: rm
source: tdn-rm
title: 3333790 FISCAL01-6028 DT Envio da NF-e  FCP ST Zerado
type: documentation
url: https://tdn.totvs.com/display/LRM/3333790+FISCAL01-6028+DT+Envio+da+NF-e++FCP+ST+Zerado
version: 8
---

# Envio da NF-e (Nota Fiscal Eletrônica)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Envio da NF-e |
| **Situação/Requisito:** | No envio da NF-e o valor da tag vICMSST está sendo apresentada com o valor do ST + FCP-ST e a tag vFCPST está sendo gerada zerada. |
| **Solução/Implementação:** | Conforme **[Nota Técnica 2016.002](http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=)** da NF-e o valor da tag vFCPST passou a compor o valor total da NF.  Foram criados os parâmetros abaixo no cadastro de regra de ICMS:   | Pasta Dados ICMS - Operação com FCP | Pasta Dados ICMS S.T - Operação com FCP ST | | --- | --- | |  |  |   *Em versões especificas 12.1.18, 12.1.19, 12.1.20 e 12.1.21 da biblioteca RM, os campos acima serão visíveis mediante a execução do script **"NF-e 4.0 FCP FCPST\_ICMS"** através da ferramenta de atualização (<http://tdn.totvs.com/display/public/LRM/Atualizador+RM>).*  Na geração da NF-e foi alterado a geração das tags:   * vBCFCP - Valor da Base de Cálculo do FCP * pFCP - Percentual do Fundo de Combate à Pobreza (FCP) * vFCP - Valor do Fundo de Combate à Pobreza (FCP) * vBCFCPST - Valor da Base de Cálculo do FCP retido por Substituição Tributária * pFCPST - Percentual do FCP retido por Substituição Tributária * vFCPST - Valor do FCP retido por Substituição Tributária   Foram criados dois novos campos na Regra de ICMS para identificar se a operação terá a incidência ou não do FCP, tanto para o ICMS como para o ICMS ST. As tags acima só serão geradas se os respectivos campos estiverem marcados na Regra de ICMS.    Exemplo de NF-e gerada com ambos os campos da regra de ICMS marcados.   | **Grupo ICMS10**  <ICMS10> <orig>0</orig> <CST>10</CST> <modBC>3</modBC> <vBC>105.00</vBC> <pICMS>4.00</pICMS> <vICMS>4.20</vICMS> <vBCFCP>105.00</vBCFCP> <pFCP>2.00</pFCP> <vFCP>2.10</vFCP> <modBCST>0</modBCST> <pMVAST>20.00</pMVAST> <pRedBCST>0.00</pRedBCST> <vBCST>126.00</vBCST> <pICMSST>18.00</pICMSST> <vICMSST>18.48</vICMSST> <vBCFCPST>126.00</vBCFCPST> <pFCPST>2.00</pFCPST> <vFCPST>0.42</vFCPST> </ICMS10> | **Totalizador da NF-e**  <ICMSTot> <vBC>105.00</vBC> <vICMS>4.20</vICMS> <vICMSDeson>0.00</vICMSDeson> <vFCP>2.10</vFCP> <vBCST>126.00</vBCST> <vST>18.48</vST> <vFCPST>0.42</vFCPST> <vFCPSTRet>0.00</vFCPSTRet> <vProd>105.00</vProd> <vFrete>0.00</vFrete> <vSeg>0.00</vSeg> <vDesc>0.00</vDesc> <vII>0.00</vII> <vIPI>0.00</vIPI> <vIPIDevol>0.00</vIPIDevol> <vPIS>0.00</vPIS> <vCOFINS>0.00</vCOFINS> <vOutro>0.00</vOutro> <vNF>123.90</vNF> <vTotTrib>0.00</vTotTrib> </ICMSTot> | | --- | --- |   **Geração da Tag** **vFCPST = (vBCFCPST \* (pFCPST/100)) - vFCP;**  **1 - Observação**: Neste caso a alíquota dos Tributos ICMS e ICMS ST foram majoradas em 2% referentes ao FCP na Natureza de Operação e as mesmas são reduzidas em 2% nos devidos campos no XML da NF-e  Então quando utilizar FCP ou FCP-ST a alíquota dos tributos ICMS e ICMS-ST devem ser majoradas conforme alíquota do FCP vigente e ainda será **OBRIGATÓRIO** informar a alíquota do FCP no Dados Fiscais por UF no cadastro do Produto.  **2 - Observação:** Está parametrização é para ocorrência de FCP sem Diferencial de Alíquota. |
| **Requisito:** | FIS000071 |
