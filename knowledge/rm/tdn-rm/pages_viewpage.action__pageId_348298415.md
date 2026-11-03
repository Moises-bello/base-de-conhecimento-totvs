---
content_hash: 14f94f13d653dbd5b67bfae38e2df997da7a591d9dd718d0d7e1dbaed5d3bef0
fetched_at: '2026-06-29T00:08:55.373059+00:00'
page_id: '348298415'
product: rm
source: tdn-rm
title: RMFIS00003_REINF R-2010 / R-2020 – Serviços Tomados e Prestados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=348298415
version: 13
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal x TAF Totvs Automação Fiscal |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Eventos R-2010 / R-2020 – Serviços Tomados e Prestados |
| **Ambiente:** |  |
| **Passo a passo:** | **R-2010 - Retenções Contribuição Previdenciária – Serviços Tomados**  Evento que comporta as informações relativas aos serviços contratados, com as correspondentes informações sobre as retenções previdenciárias, e realizados mediante cessão de mão de obra ou empreitada, nos termos do art. 31 da Lei nº 8.212, de 1991, inclusive quando a empresa prestadora se sujeitar ao regime da contribuição previdenciária sobre a receita bruta – CPRB, consoante preconiza o art. 7º, §6º da Lei nº 12.546, de 2011.    Este evento deve ser enviado por filial. Caso o prestador possua determinação judicial que suspenda a retenção das contribuições previdenciárias, o declarante deve informar o respectivo processo no evento **[R-1070 - Tabela de Processos Administrativos/Judiciais](http://tdn.totvs.com/pages/viewpage.action?pageId=346500862)** e indicá-lo neste evento.  A origem dos dados para geração desses registros é Gestão Fiscal através dos lançamentos de **entrada** que possuem o tributo **INSS** associado e o campo **Classificação do Serviço** preenchido em anexos do produto\serviço vinculado ao lançamento.    **R-2020 -** **Retenção Contribuição Previdenciária - Serviços Prestados**  Esse evento deve ser enviado pelo prestador de serviços executados mediante cessão de mão de obra, empreitada e subempreitada, contendo as informações relativas aos tomadores dos serviços, com as correspondentes informações sobre as retenções previdenciárias destacadas no documento fiscal.  Este evento deve ser enviado por filial. Caso a filial possua determinação judicial que suspenda a retenção das contribuições previdenciárias, deve-se informar o respectivo processo no evento **[R-1070 - Tabela de Processos Administrativos/Judiciais](http://tdn.totvs.com/pages/viewpage.action?pageId=346500862)** e referenciá-lo neste evento.  A origem dos dados para geração desses registros é Gestão Fiscal através dos lançamentos de **saída** que possuem o tributo **INSS** associado e o campo **Classificação do Serviço** preenchido em anexos do produto\serviço vinculado ao lançamento..    As informações, tanto do R-2010 como do R-2020, são enviadas para o TAF através do Registro T013 e "filhos" do Layout TAF.   121º Passo1º Passo R-2010: Necessário possuir lançamento de entrada com tributo INSS informado no item do lançamento.  R-2020: Necessário possuir lançamento de saída com tributo INSS informado no item do lançamento.   22º Passo R-2010: Necessário que o campo Classificação do Serviço esteja preenchido no cadastro do Produto\Serviço vinculado ao lançamento de entrada.  R-2020: Necessário que o campo Classificação do Serviço esteja preenchido no cadastro do Produto\Serviço vinculado ao lançamento de saída.   * Cadastros | Produtos | Selecione o produto\serviço | Anexos - Dados Fiscais do Produto | Aba Identificação.    43º Passo2º Passo Realizar a integração conforme documento:   * [Integração RM x TAF](http://tdn.totvs.com/pages/viewpage.action?pageId=336404337)   Após integração realizar a apuração e transmissão seguindo a partir do 6º Passo do documento abaixo:   * [RMFIS00002\_REINF R-1000 – Informações do Contribuinte](http://tdn.totvs.com/pages/viewpage.action?pageId=346500860) |
| **Observações:** | Video do Processo: [HOW TO - TAF - Apurações para geração de XML´s REINF - R2010 e R2020](https://youtu.be/mdJyESTCG88) |
