---
article_id: 360057418593
category: Suricato
content_hash: c45e987a687d66d0f77c4ebdaf60de028a3e99777630791fa1584b4e9222503c
fetched_at: '2026-06-28T22:44:57.403835+00:00'
product: protheus
section_id: 360004073231
source: central-protheus
title: RH - Linha Protheus - PON x Suricato - Como cadastrar um relógio que integra
  com o Suricato
type: support-article
updated_at: '2024-11-13T14:13:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057418593-RH-Linha-Protheus-PON-x-Suricato-Como-cadastrar-um-rel%C3%B3gio-que-integra-com-o-Suricato
---

**Dúvida**Como cadastrar um **relógio que integra com o Suricato?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**Quando existe a integração ativa com o **Suricato**, as marcações de Ponto são lidas através de uma **tabela intermediária** do processo, que pode ser a tabela **MSA\_CONTROL\_MARCAC** ou a tabela **RR1**, portanto, não há um arquivo TXT.  
  
Para que o Protheus localize os registros nas tabelas, é necessário que exista um **cadastro de Relógio** **específico**, para isso, acesse **Atualizações - Cadastro do Ponto - Relógios**.  
  
Para este cadastro, é importante que na **primeira aba** chamada **Geral,** e na **última aba** chamada **Outros**, os campos abaixo estejam desta forma:  
  
- o campo **Tipo Arquivo** deve ser preenchido como **R**;  
- será gatilhado automaticamente no campo **Nome Arquivo** a palavra **REP**. O conteúdo **não deve ser alterado;**  
- o campo **REP** deve ser preenchido **exatamente** da mesma forma que foi cadastrado no **Suricato**, ou seja: se no **Suricato** o relógio tiver 10 caracteres, no **Protheus** deverá estar da **mesma forma**. Caso exista **divergência nos cadastros**, o Protheus **não conseguirá identificar as marcações nas tabelas** para processar a leitura dos dados. O campo comporta até 17 caracteres, mas não se faz obrigatório completar os caracteres restantes com zeros. Por exemplo: se o código de fábrica do relógio for 1234567 e for cadastrado desta forma no Suricato, esta numeração deverá ser informada desta forma no Protheus, e não 00000000001234567. Em caso de dúvidas, é possível consultar como  as marcações foram gravadas nas tabelas MSA\_CONTROL\_MARCAC ou RR1, no campo **CODREP**;  
- o campo **Incremental** deve estar como **SIM**;  
- o campo **Tipo do REP** deve estar preenchido com o **tipo correto do relógio**, levando em consideração por qual **Portaria** ele é **homologado**, ou seja: **1 - 1510** = para relógios homologados pelas antigas portarias 1510 e 373, onde a leitura é feita através do **PIS** do funcionário; **2 - REP C** = para relógios homologados pela portaria 671, onde a leitura é feita através do **CPF** do funcionário;  
- o campo **Novo Relógio** deve estar como **SIM**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16701832916887)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16701835703959)  
  
É possível também cadastrar um relógio para **leitura** de **marcações de Refeição**. Neste caso, apenas o conteúdo do campo **Controle** deve ser informado como **R**.  
  
**Saiba Mais:**[Acesso e Segurança by Suricato](https://www.youtube.com/watch?v=UH57zVuDh7E)[Integração Protheus x Suricato](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=546695095)  
[Migração da tabela MSA\_CONTROL\_MARCAC para RR1](https://tdn.totvs.com/pages/releaseview.action?pageId=566486186#dicionario-sx3)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
