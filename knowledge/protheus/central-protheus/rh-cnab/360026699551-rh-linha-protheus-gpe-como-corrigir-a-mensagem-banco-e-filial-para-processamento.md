---
article_id: 360026699551
category: RH - CNAB
content_hash: d402972b86ddaf8062405eeb080cafaf7712608944c9733c73111a66138da9f1
fetched_at: '2026-06-28T22:43:39.174959+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: 'RH - Linha Protheus - GPE - Como corrigir a mensagem : Banco e Filial para
  processamento do CNAB não cadastrados na tabela S052'
type: support-article
updated_at: '2025-06-17T12:33:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026699551-RH-Linha-Protheus-GPE-Como-corrigir-a-mensagem-Banco-e-Filial-para-processamento-do-CNAB-n%C3%A3o-cadastrados-na-tabela-S052
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32867047819287)**Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**Como corrigir a mensagem: Atenção! Banco e Filial para processamento do CNAB não cadastrados na tabela S052! Favor verificar!?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
Na geração do arquivo CNAB (GPEM080), é apresentada a mensagem:

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025852091)  
  
Essa mensagem será apresentada nos seguintes casos:  
1) Ausência de cadastro de banco na tabela S052;  
2) O campo Processa Banco no grupo de perguntas da rotina, possuir informação diferente do cadastro;  
3) Houver alteração de parâmetros ou arquivo de configuração do arquivo CNAB, sem releitura da tabela S052.   
4) Compartilhamento exclusivo da RCC

Para solução deverá ser observado os seguintes procedimentos:  
1) Cadastrar informação de banco de convênio da empresa na tabela S052;  
2) Caso já exista o cadastro na Tabela S052, fazer a releitura da tabela, clicando na lupa e confirmando a conta cadastrada que deverá ser utilizada.  
3) Alterar o compartilhamento da tabela RCC, de modo que de forma compartilhada, seja possível validar que o banco existe nas demais filiais (lembrando que a tabela RCC possui todas as tabelas de manutenção de cálculo).   
  
**Obs.:** Na alteração do campo Processar banco, por segurança o sistema não considera a informação digitada, devendo ser aplicada a indicação de solução 2.

**Saiba Mais:**  
[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
