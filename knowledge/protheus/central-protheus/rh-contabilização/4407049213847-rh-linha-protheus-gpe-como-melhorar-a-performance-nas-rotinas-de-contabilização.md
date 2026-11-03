---
article_id: 4407049213847
category: RH - Contabilização
content_hash: 83bdf73b4d9519bb2e0328949f1604957884087da4d6e73b12e861588b38e4ea
fetched_at: '2026-06-28T22:43:46.094245+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como melhorar a performance nas rotinas de Contabilização
  e Resumo da Folha - MV_SPGP110
type: support-article
updated_at: '2025-07-29T12:09:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407049213847-RH-Linha-Protheus-GPE-Como-melhorar-a-performance-nas-rotinas-de-Contabiliza%C3%A7%C3%A3o-e-Resumo-da-Folha-MV-SPGP110
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como melhorar a performance nas rotinas de Contabilização e Resumo da Folha - MV\_SPGP110?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.1.17.  
  
**Solução**O sistema possui uma *Stored Procedure* que tem por finalidade gravar os registros na tabela utilizada na Contabilização e Relatório de Resumo da Folha (SRZ).

A *Stored Procedure* está disponível para os bancos de dados mencionados e sua utilização deve ser habilitada por meio do parâmetro MV\_SPGP110, configurando-o como “T” (*True* - Verdadeiro).

A melhoria beneficiará a performance das seguintes rotinas: • “Miscelânea/Fechamentos/Contabilização” (GPEM110) • “Miscelânea/Títulos/Geração” (GPEM650) • “Relatórios/Mensais/GPS/GRPS” (GPER240) • “Miscelânea/Previdência/GPS Eletrônica” (GPEM240) • “Relatórios/Mensais/Folha de Pagamento” (GPER040) • “Relatórios/Mensais/DARF PIS” (GPER055)  
  
**Procedimentos para implementação:**1) No ambiente Configurador, opção “Ambientes/Cadastros/Parâmetros”, localize o seguinte parâmetro:

Nome da Variável: MV\_SPGP110  
Tipo: Lógico   
Cont. Por.: .T.  
Descrição: Indica se o sistema deve usar a procedure para gerar a tabela SRZ - Resumo da Folha. (T = Sim, F = Não)
