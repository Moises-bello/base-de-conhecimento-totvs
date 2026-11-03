---
content_hash: 0522f5b38552c7155f1bcecc15fe3fd610a4adfc58c6b181242dbb30a5eec30a
fetched_at: '2026-06-29T00:10:59.854244+00:00'
page_id: '616768523'
product: rm
source: tdn-rm
title: Alterações ECF 2021 - Layout 7
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=616768523
version: 32
---

#f5f5f5#363636noneECF (Escrituração Contábil Fiscal) 2021

## **Conteúdo**



## **01. Sobre****Sobre**

O Layout 7 da Escrituração Contábil Fiscal - ECF foi introduzido pelo [Ato Declaratório Cofis no 86/2020](http://sped.rfb.gov.br/pagina/show/5714), e deve ser utilizado para transmitir as situações normais de 2020 e situações especiais de 2021.

AtençãoFique atento ao prazo de entrega da ECF através do [Portal da Receita](http://sped.rfb.gov.br/) ou em nosso [Espaço Legislação](https://espacolegislacao.totvs.com/)

## **02. Patches****Patches**

* *12.1.27.372 ou superior*
* *12.1.28 - Não disponível*
* *12.1.29.258 ou superior*
* *12.1.31.163 ou superior*
* *12.1.32.105 ou superior*

As alterações referentes ao layout 7 estão disponíveis no Totvs compartilhamento

**Dados do layout:**

* FISLAY0014 - ECF.TotvsGen
* Data 16/07/2021
* [Mais sobre o TOTVS Compartilhamento](https://tdn.totvs.com/display/LRM/TOTVS+Compartilhamento)

## **03. Documentação Geral****DocumentacaoGeral**

* [Atualização da Tabela Dinâmica](https://tdn.totvs.com/pages/viewpage.action?pageId=422546165)
* [Documentação geral da ECF](https://tdn.totvs.com/pages/viewpage.action?pageId=422545681)
* [Agenda Webinar](https://tdn.totvs.com/pages/releaseview.action?pageId=550328285#News-TOTVSGest%C3%A3oFiscaleDocumentosEletr%C3%B4nicos(LinhaRM)-Webinar)
* [Vídeos Webinar](https://tdn.totvs.com/pages/releaseview.action?pageId=550328285#News-TOTVSGest%C3%A3oFiscaleDocumentosEletr%C3%B4nicos(LinhaRM)-VWebinar)
* [Vídeos How To](https://tdn.totvs.com/pages/releaseview.action?pageId=550328285#News-TOTVSGest%C3%A3oFiscaleDocumentosEletr%C3%B4nicos(LinhaRM)-HWFiscal)

## **04. Vídeos de demonstração****Video**

Vídeo de demonstração648432none

## **05. O que foi alterado?****Alterado**

**Registro 0000: Abertura do Arquivo Digital e Identificação da Pessoa Jurídica**

O campo 3 - COD\_VER (Código da versão do leiaute) de acordo com o layout 7, para o ano-calendário 2020 e situações especiais de 2021, o leiaute a ser informado deverá ser = 0007.

**Campo 6** - IND\_SIT\_INI\_PER - Indicador do Início do Período:

Incluído mais uma Opção: 3 – Resultante de Mudança de Qualificação da Pessoa Jurídica.

**Observação:** Este campo é gerado conforme a parametrização do Cadastro da Filial – Parâmetros ECF – Pasta Identificação Campo **“Indicador do Início do Período”** criar a Opção.

**Campo 7** - SIT\_ESPECIAL - Indicador de Situação Especial e Outros Eventos:

Incluído mais uma Opção: 7 – Mudança de Qualificação da Pessoa Jurídica

**Observação:** Campo gerado conforme parametrização do Cadastro da Filial – Parâmetros ECF – Pasta Identificação Campo “**Indicador de Situação Especial**”

none

**Registro 0010: Parâmetros de Tributação**

Na geração do Registro 0010 no layout 7, o campo: Campo 04 - OPT\_PAES foi removido e não será mais gerado desta versão em diante.

none

**Registro 0020: Parâmetros Complementares**

Na geração do Registro 0020 no layout 7, os campos: Campo 14 - IND\_DOA\_ELEIT, Campo 16 - IND\_VEND\_EXP e Campo 19 - IND\_COM\_EXP foram removidos e não será mais gerado desta versão em diante.

none

## **06. Registros Removidos****RegistrosRemovido**

|  | Registro | Descrição |
| --- | --- | --- |
| 1 | [Y540](https://tdn.totvs.com/pages/viewpage.action?pageId=422546105) | Discriminação da Receita de Vendas dos Estabelecimentos por Atividade Econômica |
| 2 | [Y550](https://tdn.totvs.com/pages/viewpage.action?pageId=422545984#BLOCOY-Y550) | Vendas a Comercial Exportadora com Fim Específico de Exportação |
| 3 |  | Detalhamento das Exportações da Comercial Exportadora |
| 4 | [Y671](https://tdn.totvs.com/pages/viewpage.action?pageId=422545984#BLOCOY-Y671) | Outras Informações (Lucro Real) |
| 5 | Y690 | Informações de Optantes pelo Paes |
