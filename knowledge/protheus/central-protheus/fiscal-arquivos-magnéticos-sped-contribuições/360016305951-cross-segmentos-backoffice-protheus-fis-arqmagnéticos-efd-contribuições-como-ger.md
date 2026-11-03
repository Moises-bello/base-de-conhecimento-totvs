---
article_id: 360016305951
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 4a9a3e72063987010caedfacf7d1de60f54da49b201a118ce9e21364602fe91c
fetched_at: '2026-06-28T22:42:06.565701+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  Como gerar os registros M400/M410 e M800/M810
type: support-article
updated_at: '2025-04-24T20:27:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016305951-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-gerar-os-registros-M400-M410-e-M800-M810
---

**Dúvida**Como gerar os registros M400/M410 e M800/M810 do Sped Contribuições?

**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Verifique os parâmetros abaixo:  
**MV\_GRBLOCM = T** -> para que geração do **Bloco M** seja feita pelo Protheus.  
**MV\_CFAREC** = informar o **CFOP** de Receita caso não esteja sendo considerado no padrão da rotina FISA001.

Para operações de SAÍDA, estes são os **CFOP’s** que o **Protheus** considera como Receita. Se o **CFOP** utilizado não constar nesta relação deverá ser informado no parâmetro **MV\_CFAREC**.   
**CFOP’s** que caracterizam Receita no **Protheus**:  
**Estadual:**  
5101,5102,5103,5104,5105,5106,5109,5110,5111,5112,5113,5114,5115,5116,5117,5118,5119,5120,5122,5123,5124,5125,5251,5525,5253,5254,5255,5256,5257,5301,5302,5303,5304,5305,5306,5307,5351,5352,5353,5354,5305,5306,5307,5351,5352,5353,5354,5355,5356,5357,5359,5401,5402,5403,5405,5651,5652, 5653,5654,5655,5656.  
**Interestadual:**  
6101,6102,6103,6104,6105,6106,6107,6108,6109,6110,6111,c6112,6113,6114,6115,6116,6117,6118,6119,6120,6122,6123,6124,6125,6251,6252,6253,6254,6255,6256,6257,6258,6301,6302,6303,6304,6305,6306,6307,6351,6352,6353,6354,6355,6356,6357,6359,6401,6402,6403,6404,6501,6502,6651,6652,6653,6654, 6655,6656.  
**Exterior:**  
7101,7102,7105,7106,7127,7251,7301,7358,7501,7651,7664.  
  
2. **Preenchimento da Conta Contábil**, segue link abaixo para a validação:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015964612-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-e-EFD-Contribui%C3%A7%C3%B5es-Preenchimento-da-Conta-Cont%C3%A1bil?source=search>  
  
3. Verifique a **configuração da TES** para **alíquota zero** (**CST 04,06** - Saída);  
 **TES** - Aba Impostos  
**Livro ICMS ou ISS** = diferentes de Não -> Deve ser configurado o campo de um dos livro com a opção diferente de não para geração dos valore de PIS COFINS nas tabelas **SF3** e **SFT.**

**PIS/COFINS** = Ambos   
**Cred. Pis/Cof** = Calcula

Aba Outros  
**Sit Trib Pis** = 04 ou 06  
**Sit Trib Cof** = 04 ou 06

**Importante:**Obs: Para notas fiscais de entrada deve ser preenchido o campo **F4\_CODBCC = ?** para o preenchimento do campo **FT\_CODBCC** referente a operação da **CFOP**.

Existe uma tabela disponibilizada pela Receita referente a base de crédito dos registros **M105/M505** - determinado pelo **CFOP** informado no documento fiscal.  
  
Segue *link* do site da Receita contendo a **tabela de CFOP x Operações geradoras de crédito**:  
<http://sped.rfb.gov.br/arquivo/show/1681>Nome do arquivo: **Tabela\_CFOPOperacoesGeradorasCreditos.xls**

4. Verifique a configuração da **TES** para **CST's** de operações **isentas** e **sem tributação** (**CST 07, 08 e 09**);

**TES -** Aba impostos **Livro ICMS ou ISS** = diferentes de Não -> Deve ser configurado o campo de um dos livro com a opção diferente de não para geração dos valore de PIS COFINS nas tabelas **SF3** e **SFT.**

**PIS/COFINS** = não considera   
**Cred. Pis/Cof** = não calcula  
**Sit Trib Pis** = 07, 08 ou 09  
**Sit Trib Cof** = 07, 08 ou 09

5. Para o preenchimento das tabelas de Natureza da Receita verifique os cadastros:  
**Pedido de Venda** (SC6), nos campos **C6\_TNATREC**, **C6\_CNATREC**, **C6\_GRPNATR** e **C6\_DTFIMNT**;  
OU  
**Exceção fiscal** (SF7), nos campos **F7\_TNATREC**, **F7\_CNATREC**, **F7\_GRUPONC** e **F7\_DTFIMNT**;  
OU  
**Produto** (SB1), campos **B1\_TNATREC**, **B1\_CNATREC**, **B1\_GRPNATR** e **B1\_DTFIMNT**;  
OU  
**Tipos de Entrada e Saída** (**SF4**), campos **F4\_TNATREC**, **F4\_GRPNATR**, **F4\_CNATREC**, e **F4\_DTFIMNT**.

**Obs1**.: Para o preenchimento da tabela **SF4**. esses campos são trazidos da tabela **CCZ** (a partir do que for preenchido na Tabela de Natureza da Receita), uma vez que você preencher lá e selecionar na **TES**, irá preencher de forma automática o conteúdo selecionado. E o campo de data não está visível na **TES** por estar visível no cadastro auxiliar. Em relação aos campos **F4\_GRPNATR, F4\_CNATREC, e F4\_DTFIMNT**, os mesmos não são abertos por serem somente campos de informações, com base no preenchimento de outra tabela.

**Obs2.:** O sistema seguirá a seguinte ordem de pesquisa dos valores:  
**Pedido de Venda;**  
**Exceção Fiscal;**  
**Produto;**  
**TES.**  
Se for utilizar um nível abaixo não preencha valores no nível anterior.

Por meio da exceção fiscal, ao preencher o campo **Tab.Nat.Rec**. (**F7\_TNATREC**) com a tabela escolhida pela consulta na tabela **CCZ**, os campos **Aliq.Pis** (**F7\_ALIQPIS**) e **Aliq.Cof**(**F7\_ALIQCOF**) são preenchidos automaticamente de acordo com as alíquotas cadastradas nos campos **Aliq. PIS** (**CCZ\_ALQPIS**) e **Aliq. COFINS** (**CCZ\_ALQCOF**), conforme o registro selecionado. Exceto para registros da **tabela 4.3.11**, onde os valores são preenchidos automaticamente nos campos de **PIS Pauta** (**F7\_VLR\_PIS**) e **COFINS Pauta** (**F7\_VLR\_COF**).

**Importante:**Após as configurações serão gravadas as informações nos campos da tabela **SFT** - **FT\_TNATREC**, **FT\_CNATREC**, **FT\_GRUPONC** e **FT\_DTFIMNT**, para a geração dos registro **M410** e **M810**.
