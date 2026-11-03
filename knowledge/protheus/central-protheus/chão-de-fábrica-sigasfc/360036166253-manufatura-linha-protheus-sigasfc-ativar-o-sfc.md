---
article_id: 360036166253
category: Chão de Fábrica (SIGASFC)
content_hash: 9d5b9ce31acb9b3bd8bb0eeafafb5e32d8b3305283944c4994c0e05268eaa5d7
fetched_at: '2026-06-28T22:42:49.788783+00:00'
product: protheus
section_id: 360005696234
source: central-protheus
title: Manufatura - Linha Protheus - SIGASFC - Ativar o SFC
type: support-article
updated_at: '2025-02-24T11:32:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036166253-Manufatura-Linha-Protheus-SIGASFC-Ativar-o-SFC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20464592357911) Tempo aproximado para leitura: **00:02:47 min**  
**Dúvida**Como ativar o **SFC - Chão de Fábrica**?  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Chão de Fábrica (SIGASFC) - Versão 12  
  
**Solução**Para poder utilizar o módulo de **Chão de Fábrica** no **Protheus** a execução da função **CARGASFC** é obrigatória, isto porque além de copiar dados, a rotina acerta o compartilhamento das tabelas.  
Deve-se atentar aos seguintes pontos ao executar o **CARGASFC**:  
  
1 - Inclua um **CT - Centro de Trabalho** na rotina **MATA770 - Centro de Trabalho** e após relacione este **CT** nas operações de produção por meio da rotina **PCPA124 - Processo Produtivo** no campo **Centro Trab.**. Como as operações no **Roteiro** do **PCP - Planejamento e Controle da Produção** não são obrigatórias, é necessário fazer a manutenção dos mesmos antes de iniciar a **SIGASFC**;  
  
2 - Preencha os parâmetros **MV\_SFCCDCL - Calendário genérico SFC** e **MV\_SFCCDTN - Modelo Turno**. No parâmetro **MV\_SFCCDCL** deve-se informar um código de calendário genérico, cadastrado na rotina **SFCA013 - Calendário Genérico** e no parâmetro **MV\_SFCCDTN** um código de calendário cadastrado na rotina **MATA780 - Cadastro de Calendários.**Nesse segundo parâmetro como ainda não existe esta informação no **Chão de Fábrica**, deve-se preencher com o código do **PCP**.  
  
3 - Antes de efetuar a carga, ative o parâmetro **MV\_INTSFC - Define se existe integração entre o Módulo SIGASFC e outros módulos**, e caso ocorra erro na carga o parâmetro volta a ficar desativado. O parâmetro deve ser por filial;  
  
4 - Antes de efetuar a carga, crie ao menos uma **Área de Produção** no **SFC** na rotina **SFCA007 - Cadastro de Área de Produção**, para que ao criar os **CT's** a partir do **PCP**, seja buscada a área, que no **SFC** é obrigatória para o **CT;**  
  
5 - Na rotina **MATA610 - Recursos** relacionar o centro de trabalho incluído no item 1, nos recursos já cadastrados no **PCP**.  
  
**Importante**Antes de cadastrar o calendário genérico na rotina **SFCA013**, é preciso realizar o compartilhamento das tabelas, conforme mostra na documentação [Manufatura - Linha Protheus - SIGASFC - Compartilhamento tabelas para implantação do SFC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043260934-Manufatura-Linha-Protheus-SIGASFC-Compartilhamento-tabelas-para-implanta%C3%A7%C3%A3o-do-SFC)
