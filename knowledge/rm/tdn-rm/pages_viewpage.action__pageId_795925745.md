---
content_hash: 715bb94c0e2235a59aa3b79ba616ac5b84599394ba44942b78301adb83c4c9d0
fetched_at: '2026-06-29T00:11:42.738030+00:00'
page_id: '795925745'
product: rm
source: tdn-rm
title: Registro Boleto Online Bradesco (v2)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=795925745
version: 8
---

## Descrição

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do banco Bradesco.

## Procedimentos para configuração

No TOTVS Gestão Financeira, menu *Movimentações Bancárias | Controle Bancário | Convênio,* devem ser feitas as configurações do convênio para o registro de boleto online:

* **Permite registro de boleto online*:***Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco.
* **URL do homologação do serviço de registro de cobrança**: Deve ser informado a URL de homologação do serviço de registro do boleto fornecida pelo banco.
* **URL do sistema autorizador**: Deve ser informado a URL do sistema autorizador que retornará o token de acesso ao serviço de registro de cobrança.
* **URL de homologação do sistema autorizador**: Deve ser informado a URL de homologação do sistema autorizador que retornará o token de acesso ao serviço de registro de cobrança.
* **Client Id**: Código de acesso ao sistema autorizador fornecido pelo banco.
* **Certificado digital:** Informe o certificado digital obtido pela empresa.

**IMPORTANTE**: O Bradesco disponibiliza o serviço na API para geração do QR Code pix, porém não está implementado no produto padrão. Logo, o campo "cindcdCobrMisto" (responsável por gerar o QR Code PIX) será gerado por padrão com o valor "N". Para contratação deste recurso, verifique mais informações da nossa solução [TOTVS Boleto Híbrido](https://totvstechfin.com.br/pagamentos/). 

## Cadastro de Layout de Registro Online

Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/pages/viewpage.action?pageId=311625508), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=307835775) de acordo com o manual de cobrança online do Bradesco. Conforme detalhado a seguir, é possível enviar os dados de forma flexível para o banco ao registrar online os boletos. O cadastro do layout do registro online do Bradesco deve ser feito conforme o manual de cobrança online do banco, onde contempla a descrição de cada campo. Exemplos:

 registrarTitulo  
 codUsuario  
 nroCpfCnpjBenef  
 filCpfCnpjBenef  
 digCpfCnpjBenef  
 tipoAcesso  
 cpssoaJuridContr  
 ctpoContrNegoc  
 nseqContrNegoc  
 cidtfdProdCobr  
 cnegocCobr  
 filler  
 codigoBanco  
 eNseqContrNegoc  
 tipoRegistro  
 cprodtServcOper  
 ctitloCobrCdent  
 ctitloCliCdent  
 demisTitloCobr  
 dvctoTitloCobr  
 cidtfdTpoVcto  
 cindcdEconmMoeda  
 vnmnalTitloCobr  
 qmoedaNegocTitlo  
 cespceTitloCobr  
 cindcdAceitSacdo  
 ctpoProteTitlo  
 ctpoPrzProte  
 ctpoProteDecurs  
 ctpoPrzDecurs  
 cctrlPartcTitlo  
 cformaEmisPplta  
 cindcdPgtoParcial  
 filler1  
 ptxJuroVcto  
 vdiaJuroMora  
 pmultaAplicVcto  
 vmultaAtrsoPgto  
 qdiaInicMulta  
 pdescBonifPgto01  
 vdescBonifPgto01  
 dlimDescBonif1  
 pdescBonifPgto02  
 vdescBonifPgto02  
 dlimDescBonif2  
 pdescBonifPgto03  
 vdescBonifPgto03  
 dlimDescBonif3  
 ctpoPrzCobr  
 pdescBonifPgto  
 vdescBonifPgto  
 dlimBonifPgto  
 vabtmtTitloCobr  
 viofPgtoTitlo  
 filler2  
 elogdrSacdoTitlo  
 enroLogdrSacdo  
 ecomplLogdrSacdo  
 ccepSacdoTitlo  
 ccomplCepSacdo  
 ebairoLogdrSacdo  
 csglUfSacdo  
 nroCpfCnpjSacdo  
 renderEletrSacdo  
 cdddFoneSacdo  
 cfoneSacdoTitlo  
 agenciaDeb  
 agenciaDebDv  
 contaDeb  
 agenciaDvCentPr  
 elogdrSacdrAvals  
 enroLogdrSacdr  
 ecomplLogdrSacdr  
 ccepSacdrTitlo  
 ccomplCepSacdr  
 ebairoLogdrSacdr  
 csglUfSacdr  
 nroCpfCnpjSacdr  
 renderEletrSacdr  
 cdddFoneSacdr  
 filler3  
 fase  
 caliasAdsaoCta  
 wqrcdPdraoMercd  
 filler4  
 qtdePgtoParcial  
 qdiaInicJuro  
 isacdoTitloCobr  
 imunSacdoTitlo  
 indCpfCnpjSacdo  
 bancoDeb  
 bancoCentProt  
 isacdrAvalsTitlo  
 imunSacdrAvals  
 indCpfCnpjSacdr  
 cfoneSacdrTitlo  
 ialiasAdsaoCta  
 iconcPgtoSpi

**IMPORTANTE**:

* Deve ser adquirido um certificado digital ICP-Brasil, preferencialmente modelo A1. O certificado deverá ser incluído no [cadastro de Certificado Digital](https://tdn.totvs.com/display/LRM/Certificado+Digital) no TOTVS Gestão Fiscal.
* Quando o ambiente for 'Teste', o código de barras será gerado com uma sequência de 44 caracteres '9'.
* O campo "Data da Multa" será calculado a partir da Data de Vencimento do boleto, acrescido do parâmetro *Dias de Atraso* configurado na etapa 'Valor Líquido' nos parâmetros relacionados ao lançamento financeiro.
