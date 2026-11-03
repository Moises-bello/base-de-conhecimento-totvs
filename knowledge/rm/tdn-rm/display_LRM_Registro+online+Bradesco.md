---
content_hash: 53b2b65c7b3404aeae97b84da9a5a9049949b9e0a8909c55daee2b299ef49208
fetched_at: '2026-06-29T00:12:08.217091+00:00'
page_id: '929926509'
product: rm
source: tdn-rm
title: Registro online Bradesco
type: documentation
url: https://tdn.totvs.com/display/LRM/Registro+online+Bradesco
version: 12
---

# Conteúdo:

Conteúdo:

# 1. Registro online

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira para utilizar o serviço de registro online de cobrança registrada do banco Bradesco.

# 2. Procedimento para configuração

Através do cadastro do Convênio, localizado no menu 'Movimentações Bancárias', é necessário habilitar a opção "Permite registro de boleto online" e definir os parâmetros de acordo com os dados fornecidos pelo banco Bradesco. O TOTVS Gestão Financeira disponibiliza dois modelos de registro:

Cards2Modelo de Registro Online v1

* **Permite registro de boleto online:**Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **Modelo de Registro Online:**Define o modelo do registro online: v1 ou v2.
* **URL do serviço de registro de cobrança**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco. (<https://cobranca.bradesconetempresa.b.br/ibpjregistrotitulows/registrotitulo>)
* **URL de homologação do serviço de registro de cobrança**: Deve ser informada a URL de homologação do serviço de registro do boleto disponibilizada pelo banco. (<https://cobranca.bradesconetempresa.b.br/ibpjregistrotitulows/registrotitulohomologacao>)
* **Certificado digita**l: Informe o certificado digital obtido pela empresa.
3Modelo de Registro Online v2

* **Permite registro de boleto online*:***Define se o convênio permite utilizar o registro de boleto online.
* **Ambiente**: Define o ambiente que será feito o registro do boleto no banco.
* **URL do serviço de registro do boleto**: Deve ser informada a URL do serviço de registro do boleto disponibilizada pelo banco.
  + <https://openapi.bradesco.com.br/v1/boleto-hibrido/registrar-boleto>
* **URL do homologação do serviço de registro de cobrança**: Deve ser informado a URL de homologação do serviço de registro do boleto fornecida pelo banco.
  + <https://proxy.api.prebanco.com.br/v1/boleto-hibrido/registrar-boleto>
* **URL do sistema autorizador**: Deve ser informado a URL do sistema autorizador que retornará o token de acesso ao serviço de registro de cobrança.
  + <https://openapi.bradesco.com.br/auth/server/v1.1/token>
* **URL de homologação do sistema autorizador**: Deve ser informado a URL de homologação do sistema autorizador que retornará o token de acesso ao serviço de registro de cobrança.
  + <https://proxy.api.prebanco.com.br/auth/server/v1.2/token>
* **Client Id**: Código de acesso ao sistema autorizador fornecido pelo banco.
* **Certificado digital:**Informe o certificado digital obtido pela empresa.

**IMPORTANTE**: O Bradesco disponibiliza o serviço na API para geração do QR Code pix, porém não está implementado no produto padrão. Logo, o campo "cindcdCobrMisto" (responsável por gerar o QR Code PIX) será gerado por padrão com o valor "N". Para contratação deste recurso, verifique mais informações da nossa solução [TOTVS Boleto Híbrido](https://totvstechfin.com.br/pagamentos/). 

Conforme detalhado no [item 3](https://tdn.totvs.com/display/LRM/Registro+online+Bradesco#RegistroonlineBradesco-3.Customiza%C3%A7%C3%A3odedadosnoregistroonline) deste documento, é possível enviar os dados de forma flexível para o banco ao registrar online os boletos. O cadastro do layout do registro online do Bradesco deve ser feito conforme o manual de cobrança online do banco, onde contempla a descrição de cada campo a seguir.

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

# 3. Customização de dados no registro online

Pode ser utilizado o [Cadastro de Layout do Registro Online](https://tdn.totvs.com/display/LRM/Layout+Registro+Online), para enviar dados de forma flexível para o registro online dos boletos para o banco. Para isso deve ser feito o [Cadastro de associação de fórmulas e campos do registro online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759) de acordo com o manual de cobrança online do Bradesco. Demonstramos alguns exemplos de campos no [modelo v2](https://tdn.totvs.com/display/LRM/Registro+online+Bradesco#Cards-3).

**IMPORTANTE**:

* Deve ser adquirido um certificado digital ICP-Brasil, preferencialmente modelo A1. O certificado deverá ser incluído no [cadastro de Certificado Digital](https://tdn.totvs.com/display/LRM/Certificado+Digital) no TOTVS Gestão Fiscal.
* Quando o ambiente for 'Teste', o código de barras será gerado com uma sequência de 44 caracteres '9'.
* O campo "Data da Multa" será calculado a partir da Data de Vencimento do boleto, acrescido do parâmetro *Dias de Atraso* configurado na etapa 'Valor Líquido' nos parâmetros relacionados ao lançamento financeiro.
