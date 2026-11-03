---
article_id: 36746412212887
category: RH - Definições de Cálculo
content_hash: dccaf19047aa55c9b8f38f6a2a1338eecfbd1cfbab03dccd2e11458b461d575c
fetched_at: '2026-06-28T22:43:22.251401+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Atenção! Filial inválida. Verifique o código informado
  no preenchimento do campo filial em Manutenção de Tabelas
type: support-article
updated_at: '2026-06-26T17:40:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36746412212887-RH-Linha-Protheus-GPE-Aten%C3%A7%C3%A3o-Filial-inv%C3%A1lida-Verifique-o-c%C3%B3digo-informado-no-preenchimento-do-campo-filial-em-Manuten%C3%A7%C3%A3o-de-Tabelas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36746427204247) Tempo aproximado para leitura: 00:00:40 min

**Ocorrência**  
Na rotina de Manutenção de Tabelas do sistema, ao tentar incluir uma nova filial em uma das tabelas, o Sistema não localiza a nova filial ao salvar a inclusão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36746412202903)

**Ambiente**  
TOTVS RH  TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12

**Causa**  
Esse incidente ocorre, pois a filial não foi corretamente **cadastrada** ou não foi realizado **acesso** no Sistema **logado** nesta nova filial para que as tabelas sejam **carregadas** devidamente.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse o módulo **SIGACFG** e confirme a configuração das Filiais - [Framework - Linha Protheus - Criação de Empresas e Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025147611-Framework-Linha-Protheus-Cria%C3%A7%C3%A3o-de-Empresas-e-Filiais)
2. Verifique se a nova filial BR2011 está devidamente cadastrada no sistema;
3. Acesse o módulo **SIGAGPE > Atualizações > Definições de Cálculo** logado na filial em questão e acesse as rotinas:
   1. Fórmulas
   2. Roteiros
   3. Mnemônicos
   4. Roteiros
   5. Processos
   6. Períodos
   7. Definições de Tabelas
   8. Manutenção de Tabelas
4. Inclua a filial na tabela S038 e salve as alterações.

**Saiba Mais**

[RH - Linha Protheus - GPE - Cálculo Terceiros não considera informação da tabela S038](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051271693-RH-Linha-Protheus-GPE-C%C3%A1lculo-Terceiros-n%C3%A3o-considera-informa%C3%A7%C3%A3o-da-tabela-S038)

[RH - Linha Protheus - GPE - O que verificar quando os encargos da empresa não são calculados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048711673-RH-Linha-Protheus-GPE-O-que-verificar-quando-os-encargos-da-empresa-n%C3%A3o-s%C3%A3o-calculados)

[RH - Linha Protheus - GPE - Percentual de terceiros está sendo calculado a menor, quando tem cadastro para outras entidades na S038](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058147293-RH-Linha-Protheus-GPE-Percentual-de-terceiros-est%C3%A1-sendo-calculado-a-menor-quando-tem-cadastro-para-outras-entidades-na-S038)
