---
article_id: 360015757512
category: RH - Cálculo Adiantamento
content_hash: 4150f50514fe5d2a315cd1e4d13a268d6cd65b23b9a0d4ed82d1f4c77d61ea34
fetched_at: '2026-06-28T22:43:14.258976+00:00'
product: protheus
section_id: 360011983213
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar o pagamento do Adiantamento Salarial
  para funcionárias afastadas por licença maternidade, para empresas que firmaram
  convênio com a Previdência e optaram pelo pagamento do Salário Maternidade em Folha
type: support-article
updated_at: '2025-04-14T20:33:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015757512-RH-Linha-Protheus-GPE-Como-efetuar-o-pagamento-do-Adiantamento-Salarial-para-funcion%C3%A1rias-afastadas-por-licen%C3%A7a-maternidade-para-empresas-que-firmaram-conv%C3%AAnio-com-a-Previd%C3%AAncia-e-optaram-pelo-pagamento-do-Sal%C3%A1rio-Maternidade-em-Folha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24786180720407) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida** **GPEM020**: Como efetuar o pagamento do Adiantamento Salarial para funcionárias afastadas por licença maternidade, para empresas que firmaram convênio com a Previdência e optaram pelo pagamento do Salário Maternidade em Folha?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Versão 12  
  
**Solução**Salário Maternidade: Conforme o Artigo 214 do decreto No. 3048/99 estabelece que o Salário maternidade é considerado salário e contribuição, assim sendo o salário maternidade pago pela Previdência Social, a empresa deverá efetuar o recolhimento de todos encargos legais e sociais ou seja (INSS Empresa e FGTS), para isso efetuamos as seguintes alterações:  
  
**1.** Parâmetro **MV\_PGSALMA:** define se o Salário Maternidade e o Adiantamento devem ser pagos ou não para funcionários afastado por Maternidade após 29/11/1999, a criação do parâmetro serve para as empresas que firmarem convênio com a Previdência optar pelo pagamento do Salário Maternidade em Folha.  
E esse parâmetro deve ser criado no configurador, caso não seja criado o sistema assumirá como "N" ou seja Salário Maternidade não será pago em folha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31411581686935)  
  
**2.** Roteiros de Cálculo: Foram alterados e criados novos roteiros de cálculo no Adiantamento e na Folha de pagamento utilizando o parâmetro **MV\_PGSALMA** para definição de Pagamento ou não em folha e adiantamento.  
Na folha foram criados novos roteiros para montar o Salário de Contribuição dos afastados em Maternidade, com pagamento feito pela Previdência, a empresa deverá recolher os encargos referente aos valores que serão pagos.  
  
**3.** Criação de Identificador de cálculo: Foi criado no sistema o **identificador de cálculo 0238** para demonstrar o Salário Maternidade que está entrando na Base de FGTS e Salário de Contribuição, para isso o usuário deve criar o novo identificador no **Configurador** Tabela 35 e criar uma verba de Base (Maior que 700 ), colocando o novo identificador de cálculo.  
  
![](http://tdn.totvs.com/download/attachments/233760587/image2016-3-18%2016%3A40%3A0.png?version=1&modificationDate=1458326967000&api=v2 "Linha Microsiga Protheus > PSIGAGPE0638 - GPEM020 - Pagamento do Adiantamento Salarial para funcionárias afastadas por licença maternidade, para empresas que firmaram convênio com a Previdência e optaram pelo pagamento do Salário Maternidade em Folha. > image2016-3-18 16:40:0.png")

**4.** Na tabela 35 (SX5) deve ser preenchido da seguinte maneira:  
**Tabela = 35**  
**Chave = BAS238**  
**Descrição = Base Salário Maternidade pago pela Prev. Social**  
  
![](http://tdn.totvs.com/download/attachments/233760587/image2016-3-18%2016%3A41%3A52.png?version=1&modificationDate=1458326968000&api=v2 "Linha Microsiga Protheus > PSIGAGPE0638 - GPEM020 - Pagamento do Adiantamento Salarial para funcionárias afastadas por licença maternidade, para empresas que firmaram convênio com a Previdência e optaram pelo pagamento do Salário Maternidade em Folha. > image2016-3-18 16:41:52.png")  
  
**5.** Na rotina d**e Ausências**, inserir o registro de licença maternidade para a matrícula, informando o **Cód. Ausênc = 006 - Afastamento Temporário por Motivo de Licença-Maternidade Pago pela Empresa**, neste momento o sistema irá preencher automaticamente o campo **Cód. Verba** com a verba que possui o ID 0040.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31411581689239)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31411593941143)

**6.** No cadastro de **Tipo de ausência**,  deve estar preenchido como 120 dias pagos pela empresa.  
  
**Saiba Mais**  
Para adquirir mais informações acesse o *link*: [MP - GPE0638 - Pagamento do Adiantamento Salarial para funcionárias afastadas por licença maternidade, para empresas que firmaram convênio com a Previdência e optaram pelo pagamento do Salário Maternidade em Folha.](http://tdn.totvs.com/pages/viewpage.action?pageId=233760587)

[RH - Cálculo Adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983213-RH-C%C3%A1lculo-Adiantamento)
