---
content_hash: bb6666d180b455070af78dbf9437da3c79b1a1433fd3a912e0d7b1ed46ff0613
fetched_at: '2026-06-29T00:11:42.946718+00:00'
page_id: '799272153'
product: rm
source: tdn-rm
title: 'Comparativo de Campos: Processos Jurídicos x Processos Trabalhistas'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=799272153
version: 7
---

Este documento tem como principal objetivo dissipar dúvidas e fornecer uma análise esclarecedora e comparativa das nuances existentes entre os dados do Processo Trabalhista e Processo Jurídico. Através de uma abordagem comparativa, busca-se oferecer uma visão clara e concisa, facilitando a compreensão das diferenças e semelhanças fundamentais entre esses dois conjuntos de informações. 

O processo de vinculação entre Processos Jurídicos e Processos Trabalhistas, realizado pelo [Assistente de Vinculação de Processos Jurídicos a Processos Trabalhistas](http://Assistente de Vinculação de Processos Jurídicos a Processos Trabalhistas), contempla a transferência de informações cruciais para uma integração eficaz.

Abaixo estão os campos migrados durante esse procedimento:

**1 - Informações do processo judicial ou demanda submetida à CCP ou NINTER:**

* + Origem do processo/demanda

*Se o processo possuir 15 caracteres alfanuméricos automaticamente será levado como Demanda submetida à CCP ou ao NINTER, caso possua 20 caracteres alfanuméricos Processo judicial.*

* + Tipo e Número do Processo
  + Observações

**2 - Informações complementares da demanda submetida à CCP ou NINTER:**

* + Data da Decisão
  + Unidade da Federação
  + Município
  + Vara

***Observação:** Os campos Unidade da Federação, Município e Vara levam os dados do cadastro da Vara conforme print a seguir.*

**3 - Informações do trabalhador:** *Dados provenientes do cadastro de funcionários*

1. * + CPF do trabalhador
     + Nome do trabalhador
     + Data de Nascimento do Trabalhador

**4 - Informações dos dependentes:** *Dados provenientes do cadastro de funcionários.*

***Importante! Exclusivo layout 1.1***

*No RM o CPF não é obrigatório, porém no eSocial é obrigatório. Se não foi informado no RM, o dependente não será importado.*

1. * + CPF
     + Grau de Parentesco

**5 - Informações do contrato de trabalho:**

* + Data de Admissão
  + Matrícula atribuída ao trabalhador pela empresa (CHAPA)
  + Código da categoria eSocial

Veja também

[Assistente de Vinculação de Processos Jurídicos a Processos Trabalhistas](https://tdn.totvs.com/pages/viewpage.action?pageId=799270888)

[Comparativo de Campos: Processos Jurídicos x Assistente de Vinculação de Processo Jurídico a Processo Trabalhista](https://tdn.totvs.com/pages/viewpage.action?pageId=799272048)
