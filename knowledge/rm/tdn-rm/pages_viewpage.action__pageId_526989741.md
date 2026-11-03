---
content_hash: 65ec74a786c355f7b43348709c3299d31a5f836c2bd3cc76409ca355e80e812e
fetched_at: '2026-06-29T00:10:32.497442+00:00'
page_id: '526989741'
product: rm
source: tdn-rm
title: RMFIS00001_REINF R-2010 / R-2020 – Serviços Tomados e Prestados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=526989741
version: 9
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Fiscal |
| **Versões:** | 12.1.27 |
| **Ocorrência:** | Eventos R-2010 / R-2020 – Serviços Tomados e Prestados |
| **Ambiente:** |  |
| **Passo a passo:** | **R-2010 - Retenções Contribuição Previdenciária – Serviços Tomados**  Evento que comporta as informações relativas aos serviços contratados, com as correspondentes informações sobre as retenções previdenciárias, e realizados mediante cessão de mão de obra ou empreitada, nos termos do art. 31 da Lei nº 8.212, de 1991, inclusive quando a empresa prestadora se sujeitar ao regime da contribuição previdenciária sobre a receita bruta – CPRB, consoante preconiza o art. 7º, §6º da Lei nº 12.546, de 2011.    Este evento deve ser enviado por filial. Caso o prestador possua determinação judicial que suspenda a retenção das contribuições previdenciárias, o declarante deve informar o respectivo processo no evento **[R-1070 - Tabela de Processos Administrativos/Judiciais](http://tdn.totvs.com/pages/viewpage.action?pageId=346500862)** e indicá-lo neste evento.  A origem dos dados para geração desses registros é Gestão Fiscal através dos lançamentos de **entrada** que possuem o tributo **INSS** associado e o campo **Classificação do Serviço** preenchido em anexos do produto\serviço vinculado ao lançamento.    **R-2020 -** **Retenção Contribuição Previdenciária - Serviços Prestados**  Esse evento deve ser enviado pelo prestador de serviços executados mediante cessão de mão de obra, empreitada e subempreitada, contendo as informações relativas aos tomadores dos serviços, com as correspondentes informações sobre as retenções previdenciárias destacadas no documento fiscal.  Este evento deve ser enviado por filial. Caso a filial possua determinação judicial que suspenda a retenção das contribuições previdenciárias, deve-se informar o respectivo processo no evento **[R-1070 - Tabela de Processos Administrativos/Judiciais](http://tdn.totvs.com/pages/viewpage.action?pageId=346500862)** e referenciá-lo neste evento.  A origem dos dados para geração desses registros é Gestão Fiscal através dos lançamentos de **saída** que possuem o tributo **INSS** associado e o campo **Classificação do Serviço** preenchido em anexos do produto\serviço vinculado ao lançamento.   121º Passo1º Passo R-2010: Necessário possuir lançamento de entrada com tributo INSS informado no item do lançamento.  R-2020: Necessário possuir lançamento de saída com tributo INSS informado no item do lançamento.   Imagem  32º Passo2º Passo R-2010: Necessário que o campo Classificação do Serviço esteja preenchido no cadastro do Produto\Serviço vinculado ao lançamento de entrada.  R-2020: Necessário que o campo Classificação do Serviço esteja preenchido no cadastro do Produto\Serviço vinculado ao lançamento de saída.   * Cadastros | Produtos | Selecione o produto\serviço | Anexos - Dados Fiscais do Produto | Aba Identificação.    Imagem    43º Passo3º Passo No final do período, encerrar o período de apuração do tributo INSS e criar o evento totalizador R-5011 conforme imagem abaixo:   * SPED | EFD-Reinf | Eventos Periódicos    Imagem  54º Passo4º Passo Selecione o evento, criado no passo anterior, acesse o menu "Processos | EFD-Reinf - Gerar Eventos" conforme imagem:   Imagem  65º Passo5º Passo Selecione o evento criado, R-2010/2020, menu "Processos | Transmitir Evento".   Imagem  76º Passo6º Passo Após transmitir o evento, selecione o evento transmitido e acesse o menu "Processos | Consultar Evento" para visualizar o retorno da receita.   Imagem |
| **Observações:** | Ao editar o evento é possível visualizar a Identificação, Xml de Envio, Xml de Retorno e as Origens do Evento |
