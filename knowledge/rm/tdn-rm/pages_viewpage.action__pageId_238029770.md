---
content_hash: ba61b86a3e5056bffdc63833b1281c9c47d4a24f0dd60073fc27f73fa1f06435
fetched_at: '2026-06-29T00:08:08.306797+00:00'
page_id: '238029770'
product: rm
source: tdn-rm
title: RMFIS00003_ECF Geração do registro Y690
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=238029770
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO FISCAL |
| **Versões:** | 12.1.10 - ou superior e 11.82.43 - ou superior |
| **Ocorrência:** | Geração do registro Y690 |
| **Ambiente:** |  |
| **Passo a passo:** | **Geração do registro Y690**  Segue abaixo informações sobre o registro Y690 de acordo com o manual da ECF - Disponível no site da[**Receita Federal**](http://sped.rfb.gov.br/arquivo/show/1654),  **“Registro Y690: Informações de Optantes pelo PAES**  Este registro deve ser preenchido pela pessoa jurídica que optou pelo Parcelamento Especial (Paes), de que trata a Lei no 10.684, de 30 de maio de 2003, para os meses em que esteve submetida ao parcelamento.”    **1º Parametrização para geração dos registros:**  - Para geração dos registros será necessário executar o Script **“Registro\_Y600”.** Indicamos que inicialmente o Script seja executado em base teste.  - Para correta geração da rotina é imprescindível utilizar a versão de biblioteca e layout atualizados de acordo com o [**Portal do Cliente**](https://suporte.totvs.com/portal/p/10098/home).  - Após executar o Script será habilitado nos Parâmetros – Escrituração Contábil Fiscal, em anexos da Filial, a aba **“Mais Informações”.** O sistema utilizará as informações preenchidas nessa aba para geração do registro Y690.  \*\* Cadastros | Filial |Selecione a Filial | Anexos | Parâmetros – Escrituração Contábil Fiscal |Edite o Parâmetro | Aba Mais Informações    Para habilitar os campos da aba Mais Informações, é necessário marcar o flag **“Optante pelo PAES”,** aba Tributação dos Parâmetros – Escrituração Contábil Fiscal      **2º Registro gerado no arquivo:**  **Registro Y690: Informações de Optantes pelo PAES:** |
| **Observações:** |  |
