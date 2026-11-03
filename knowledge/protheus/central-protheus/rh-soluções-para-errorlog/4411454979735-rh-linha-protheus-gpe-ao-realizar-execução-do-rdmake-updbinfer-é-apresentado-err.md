---
article_id: 4411454979735
category: RH - Soluções para error.log
content_hash: 7067d4738ea70eb5e5161932b5a664504bdd485f14e2b816d9d008ff76a7b8d8
fetched_at: '2026-06-28T22:44:08.762096+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Ao realizar execução do RDMake UPDBINFER é apresentado
  error log - Incorrect syntax near the keyword 'IN'.
type: support-article
updated_at: '2025-09-11T17:48:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411454979735-RH-Linha-Protheus-GPE-Ao-realizar-execu%C3%A7%C3%A3o-do-RDMake-UPDBINFER-%C3%A9-apresentado-error-log-Incorrect-syntax-near-the-keyword-IN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34873805010199) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao realizar a execução do **RDMake UPDBINFER**, através da chamada no Menu para a função **UPDBINFER**, é apresentado ***error log***: "***Incorrect syntax near the keyword 'IN'.***"  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Causa**Este erro ocorre devido à incorreta configuração do Grupo de Perguntas **UPDBINRES.**  
  
**Solução  
1.** Acessar o Módulo de **Configurador**, na rotina **Base de Dados/Dicionário/Base de Dados**;  
**2.** Acessar a funcionalidade de **Grupo de Perguntas**;  
**3.** Buscar pelo Grupo de Perguntas **UPDBINRES**;  
**4.** **Confirmar** que o **Grupo de Perguntas** esteja **cadastrado** conforme abaixo, principalmente quanto às propriedades "**Objeto**" e "**Conteúdo**":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411459996951)  
  
**Saiba Mais:**Documentação Técnica deste RDMake UPDINFER: <https://tdn.totvs.com/pages/releaseview.action?pageId=640699834>   
Pacote de Expedição Contínua do RH:<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>
