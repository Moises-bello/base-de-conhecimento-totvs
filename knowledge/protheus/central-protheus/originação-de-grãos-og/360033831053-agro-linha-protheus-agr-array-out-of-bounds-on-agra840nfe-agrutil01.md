---
article_id: 360033831053
category: Originação de Grãos (OG)
content_hash: 1444c171fc5a5453fb3ef75ae6e65f70bad7785d5c9b178033686423b05e950b
fetched_at: '2026-06-28T22:45:37.011503+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Array out of bounds on AGRA840NFE AGRUTIL01
type: support-article
updated_at: '2025-06-24T14:46:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033831053-Agro-Linha-Protheus-AGR-Array-out-of-bounds-on-AGRA840NFE-AGRUTIL01
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20066593207703)***Tempo aproximado para leitura: **00:01:10 min****Ocorrência**Ao dar entrada em uma nota fiscal e esta com seguinte erro **array out of bounds ( 0 of 38 ) on AGRA840NFE** **AGRUTIL01**  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
 **Causa**O erro de **array out of bounds 0 of** ... acontece quando algum campo do *array* não está em uso pelo Sistema ou tem nível superior ao do usuário não estando disponível para o usuário ou quando não está marcado o **Módulo** ou **Todos os Módulos** na configuração do campo no **Módulo Configurador**.  
  
 **Solução**Avalie os campos abaixo **NP9\_PRDDES** - **Desc Produto**, **B1\_DESC** - **Descrição do Produto**verifique se algum não está em uso ou se estão com nível **1** padrão ou outro nível ou se o **Módulo** não está marcado ou se falta marcar **Todos os Módulos**.   
Não estando marcado como **usado**, favor marcá-lo como **usado** e ou alterando o nível via **SIGACFG** - **C****onfigurador** e ou marcando **todos os módulos**, salve as alterações em modo exclusivo e faça uma nova validação, afim de verificar se o **error.log** foi corrigido.  
  
**Importante**Caso os procedimentos não resolvam o problema, faça o seguinte procedimento em modo exclusivo, sem usuários conectados

**1.** Faça *backup* das tabelas **SB1** - **Descrição Genérica do Produto** e **NP9** - **Lotes de Sementes**;

**2.** *Drop* as tabelas **SB1** e **NP9**;

**3.** Acesse o Sistema para criação das novas tabelas baseadas no dicionário **SX3** - **Campos das Tabelas**;

**4.** Volte os *backups* das tabelas **SB1** e **NP9**;
