---
article_id: 360061466174
category: Escrita Fiscal - Error.log
content_hash: 9b6b5c6521e2ebd8ee79b1664c74c4e980a897cc7172a95ccf2c0ecb55043d19
fetched_at: '2026-06-28T22:39:32.941163+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: 'MP - GPE - Erro de duplicidade na tabela SR4 ao gerar a DIRF - Cannot insert
  duplicate key row in object ''dbo.SR4XXX'' with unique index ''SRXXX_UNQ''. '
type: support-article
updated_at: '2021-04-28T15:43:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061466174-MP-GPE-Erro-de-duplicidade-na-tabela-SR4-ao-gerar-a-DIRF-Cannot-insert-duplicate-key-row-in-object-dbo-SR4XXX-with-unique-index-SRXXX-UNQ
---

**Ocorrência**Ao tentar **gerar a DIRF** através da rotina **GPEM550** gera **error log de chave duplicada na SR4: "*Cannot insert duplicate key row in object* 'dbo.SR4XXX' *with unique index* 'SR4XXX****\_UNQ"**  
  
**Ambiente**Protheus - Gestão de Pessoal - à partir da versão 12.1.17  
  
**Causa**O erro ocorre devido ao tamanho do campo R4\_TIPOREN estar com tamanho incorreto  
  
**Solução**Para solucionar o problema será necessário efetuar a **correção do tamanho do campo R4\_TIPOREN**, conforme padrão abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003040281/mceclip0.png)  
  
O tamanho deste campo foi alterado para 2 após a expedição da versão 12.1.23 e 12.1.25, por este motivo, para estas versões, é possível utilizar o Dicionário Diferencial da versão, do módulo de RH, conforme link abaixo:  
[MP - GPE - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal?source=search)  
  
Obs.: Por se tratar de um campo padrão do sistema, é possível que não seja possível alterar o tamanho do campo via Módulo de Configurador, sendo necessário alterar através de dicionário SX3.  
Obs. II: Caso um campo seja alterado fora do Módulo de Configurador, é necessário recriar a tabela, para o campo assumir as novas propriedades.  
  
**Saiba mais**Pacote Acumulado e-Social:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234>
