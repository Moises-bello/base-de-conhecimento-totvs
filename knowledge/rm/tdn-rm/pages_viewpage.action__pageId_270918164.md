---
content_hash: 9fa08c67cf49b854b6da34c38dab2aea5a126e5e3c152fd1729e204cdcfcdcde
fetched_at: '2026-06-29T00:08:25.548926+00:00'
page_id: '270918164'
product: rm
source: tdn-rm
title: FOP_0011_Parametrização DIRF/Conversão de Operadora Perfil x Cadastro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270918164
version: 25
---

# Parametrização do sistema para a geração da rotina DIRF/Informe de Rendimentos

|  |  |
| --- | --- |
| **Produto:** | TOTVS Folha de Pagamento |
| **Versões:** | Processo utilizado para Atender a DIRF/2017 - Processo descontinuado. |
| **Ocorrência:** | Como parametrizar o sistema para correta Conversão de Operadora Perfil x Cadastro |
| **Ambiente:** | DIRF -Conversão de Operadora Perfil x Cadastro |
| **Observações:** |  |
| **Passo a passo:** | Para atender a DIRF/2017 referente Reembolso Plano de Saúde, foi criado no RM Labore a opção de Conversão de Operadora Perfil x Cadastro.  Em Anuais>DIRF/Informe de Rendimentos>Conversão de Operadora Perfil x Cadastro.  Nesta opção, o sistema irá converter as Operadoras de Plano de Saúde e todos os eventos cadastrado em cada Operadora. Em Anuais>DIRF/Informe de Rendimentos/DIRF>Informe de Rendimentos>Parâmetros Específicos da coligada>Operadora de Assistência a Saúde.  **OBS 1 .: MESMO QUE O CLIENTE NÃO TRABALHA COM A OPÇÃO DE REEMBOLSO DE PLANO DE SAÚDE NA FOLHA DE PAGAMENTO, O MESMO TERÁ QUE REALIZAR ESTA** **OPÇÃO PARA QUE O SISTEMA LEVA AS INFORMAÇÕES REFERENTE A ASSISTÊNCIA MEDICA PARA A DIRF.**  **OBS 2 .: SÓ IRÁ APARECER AS OPERADORAS DE ASSISTÊNCIA A SAÚDE E OS EVENTOS CADASTRADAS NA PASTA "OPERADORA DE ASSISTÊNCIA A SAÚDE EM ANUAIS>DIRF/INFORME DE RENDIMENTOS>DIRF/INFORME DE RENDIMENTOS>PARÂMETROS DA COLIGADA, APÓS A REALIZAÇÃO DO CONVERSOR DE OPERADORA DE SAÚDE.**  **OBS 3 .: O SISTEMA SÓ IRÁ REALIZAR A CONVERSÃO SE TIVER UM PERFIL CADASTRADO, CASO NÃO TENHA, TERÁ QUE INSERIR AS OPERADORAS MANUALMENTE**          A conversão poderá ser realizada por coligada ou para todas as coligadas. Ao selecionar a coligada, o sistema irá converter todas as Operadoras referente a todos os perfis cadastrado, para a pasta:  Anuais>DIRF/Informe de Rendimentos>Operadora de Saúde.  A conversão será realizada de acordo com os Perfis cadastrados em Anuais>DIRF/Informe de Rendimentos>DIRF/Informe de Rendimentos  O sistema irá gerar um log com as informações da Conversão referente o registro de todos os Perfis e as Operadoras convertidas. |
