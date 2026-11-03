---
article_id: 360026045271
category: Gestão de Frotas
content_hash: f20220bc762a927cb75e57c360f05a7ada50587c09d984bc261b7a06f00d925c
fetched_at: '2026-06-28T22:42:39.578383+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Procedimento para abastecer um bem sem
  placa
type: support-article
updated_at: '2021-09-01T21:12:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026045271-Manufatura-Linha-Protheus-MNT-Procedimento-para-abastecer-um-bem-sem-placa
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como abastecer um **Bem** sem placa?  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Versão 12  
  
**Solução**Para a realização de abastecimentos por meio da rotina de **Abastecimento Manual - MNTA655** ou **Abastecimento em Lote Posto Interno - MNTA656** não é necessário que o **Bem** tenha placa, apenas **Tanque**. Isso é possível através do cadastramento do mesmo com campo **Categoria Bem - T9\_CATBEM** igual a **1 - Bem** e o preenchimento dos dados do **Tanque**.  
  
Para importações de abastecimento através de arquivo **.TXT** é necessário que o **Bem** possua placa e **Tanque**. Mesmo que o **Bem** em questão não seja um veículo, deve ser cadastrado com o campo **T9\_CATBEM** igual a **4 - Frota Não Integrada ao TMS** e a placa preenchida com até 7 **caracteres**. A placa não poderá repetir em nenhuma **Empresa**, **Unidade** ou **Filial do grupo**.**Importante**As empresas de convênio de abastecimento geram os arquivos **.TXT** de importação sem conhecer o **Código do bem** na **Empresa**, apenas sua placa, por isso o *layout* de importação de todos os convênios utilizam este mesmo padrão.
