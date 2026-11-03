---
article_id: 360005055731
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: c1855b80dbce9513ff3b0e87462d41126c297b9fa11e93262e1f693f78ee6ee9
fetched_at: '2026-06-28T22:37:55.288356+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  CNAB - HELP: PAR150
  Verifique os parâmetros digitados, pois não foi possível , localizar o registro
  das parametrizações de transmissão (SEE)'
type: support-article
updated_at: '2023-11-29T18:20:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005055731-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-HELP-PAR150-Verifique-os-par%C3%A2metros-digitados-pois-n%C3%A3o-foi-poss%C3%ADvel-localizar-o-registro-das-parametriza%C3%A7%C3%B5es-de-transmiss%C3%A3o-SEE
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19279178220439)*Tempo aproximado para leitura: **00:05:00min**

**Ocorrência**Ao realizar a geração do CNAB - HELP: PAR150 Verifique os parâmetros digitados, pois não foi possível , localizar o registro das parametrizações de transmissão (SEE)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões

**Causa**Migração de versão e/ou manipulação de base de dados e dicionário incorreta e indevidamente.

**- Solução 1**

Geralmente esse erro ocorre ao gerar uma remessa CNAB, e apresenta o HELP abaixo

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19279186008855)**](https://totvssuporte.zendesk.com/guide-media/01HFY66DMGA4B5A6PXXTAQGWFP)

Esse Help ocorre geralmente quando temos diferenças de tamanho de campos entre:

1 -  Verificar o tamanho das tabelas SA6 banco e SEE parâmetros banco que está no dicionário (Tabelas SX3)

2 - Verificar o tamanho das tabelas no banco de dados SA6 banco e SEE parâmetros banco

3 - Verificar o tamanho dos pergunte (tabela SX1) "Código da Agência" e "Código da Conta" na rotina.

Exemplo abaixo é AFI420 (SX1), mas poderia ser AFI150

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19279186010135)](https://totvssuporte.zendesk.com/guide-media/01HFY962MYAFFWGMG0BT6BPW3N)

Segue um exemplo de como a empresa poderá avaliar se possui ou não um problema de tamanho de campo em seu ambiente.

**1 - Verificando  o tamanho das tabelas SA6 banco e SEE parâmetros banco que está no dicionário (Tabelas SX3)**

Abra a tabela de dicionário SX3 e valide os campos agência e contas das tabelas SA6 e SEE

SIGACFG > Base de Dados > Dicionário > Bases de dados

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19279186012055)](https://totvssuporte.zendesk.com/guide-media/01HFYA48SHVZBBEY3R480QYT2H)

Verificando a tabela SEE temos a

Agência de tamanho 6

conta de tamanho 14

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19279186014103)](https://totvssuporte.zendesk.com/guide-media/01HFY9G20JA0JK1F7NHEQ2RFB9)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19279186016535)](https://totvssuporte.zendesk.com/guide-media/01HFY9K2B0TSV4RJ7XSJYG49MJ)

Verificando a tabela SA6 temos:

Agência de tamanho 6

Conta de tamanho 20  (aqui já encontramos o primeiro erro de base)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19279186018583)](https://totvssuporte.zendesk.com/guide-media/01HFY9P56Q3A99R5Q9MRTR9C4W)

**2 - Verificando o tamanho das tabelas no banco de dados SA6 banco e SEE parâmetros banco**

Abrindo via APSDU

Abrindo a tabela SEE via Top Connect na opção Arquivo > Estrutura

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19279186022807)](https://totvssuporte.zendesk.com/guide-media/01HFY9TXQVR9XVHBKRAAXF6BRJ)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19279186035095)](https://totvssuporte.zendesk.com/guide-media/01HFY9XNPWFNQVWC72ZDZ9BSJC)

Verificamos que:

Agência tem tamanho 5 (podemos identificar o segundo erro)

Conta tem tamanho 10 (podemos identificar o segundo erro)

Abrindo a tabela SA6 via Top Connect na opção Arquivo > Estrutura

Agência tem tamanho 5

Conta tem tamanho 10

**3  - Verificando o tamanho dos pergunte (tabela SX1) "Código da Agência" e "Código da Conta" na rotina.**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19279178263703)](https://totvssuporte.zendesk.com/guide-media/01HFYA4QV5RGKQ1FQX5ZKG01H8)

Selecionar a opção

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19279186039831)](https://totvssuporte.zendesk.com/guide-media/01HFYA6DPW6T0F1980664SSZE4)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19279186041623)](https://totvssuporte.zendesk.com/guide-media/01HFYA84Q2FVTC1BRWAPRQKJ0C)

Podemos observar que a

Agência tem o tamanho de 6

Conta tem o tamanho de 14

**Resumindo**:

Neste exemplo temos um problema de tamanho de campo (base) pois o ideal seria todos os campos e pergunte da rotina tivessem o mesmo tamanho tanto no dicionário SX3 como no banco de dados, como no pergunte da rotina SX1

**- Solução 2**

Caso o tamanho do pergunte da rotina esteja com o tamanho diferente da tabela SX1 (gerenciados de perguntas), o que fazer?

No exemplo abaixo, vamos supor que o pergunte "Código da Conta ?" esteja com tamanho de 10 caracteres

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19428990204311)**

Mas no gerenciados de perguntas, o tamanho do campo "Código da Conta ?" esteja com tamanho de 14 caracteres

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19428977027863)**

Em base de homologação com a inconsistência reproduzindo, faça um backup da tabela de profile chamada

MP\_SYSTEM\_PROFILE

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19428977032983)](https://totvssuporte.zendesk.com/guide-media/01HGE48BNAJ6PJDGTXRC8TCM01)

No SIGACFG abra a rotina de profiler

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19428990234903)](https://totvssuporte.zendesk.com/guide-media/01HGE4AJD6X095EGC71WRDYJV0)

E faça a exclusão de todos os registros

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/19428977045527)](https://totvssuporte.zendesk.com/guide-media/01HGE4CCADERW2THE1H7A7D40G)

Já com o tamanho do campo correto que necessita alterar no campo "Código da Conta ?"  no gerenciados de perguntas (tabela SX1), faça uma simulação entrando na rotina, pois neste momento o sistema irá replicar os tamanhos dos campos dos perguntes para o profile (MP\_SYSTEM\_PROFILE)

Segue uma documentação sobre a manutenção de profile

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Excluir dados do profile (manutenção de profile)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018587832-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Excluir-dados-do-profile-manuten%C3%A7%C3%A3o-de-profile-)

**- Solução 3**

Verifique o cadastro **Parâmetros de Bancos (Fina130)** existe na **filial** que está logado, no caso de a tabela **SEE** (**Comunicação Remota**) seja exclusiva.

* Verificar se o código da **SUBCONTA** que está usando para processar, existe para o **Banco** informado nos Parâmetros da rotina.
* Verificar se a tabela **17** (**genérica**) existe na tabela **SX5** (**dicionário**) para filial que está realizando o processamento.
* Verificar no cadastro Parâmetros **Bancos** se no campo **Conta**(**EE\_CONTA**) já está informando o **número do dígito**Comparar o tamanho do grupo de perguntas **banco**, **agência** e **conta** correspondente a rotina que está processando, com a tabela **SX3** dos campos **banco**, **agência** e **conta** da tabela **SEE**.

**Veja mais**

* [Página Centralizadora do CNAB](http://tdn.totvs.com/display/PROT/CNAB)
* [Como Parametrizar o sistema para a geração do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006611532-MP-SIGAFIN-CNAB-Como-parametrizar-o-sistema-para-gera%C3%A7%C3%A3o-do-CNAB-)
* [Principais mensagens do CNAB](http://tdn.totvs.com.br/pages/viewpage.action?pageId=353280222)
