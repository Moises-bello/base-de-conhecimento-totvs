---
article_id: 30763473463703
category: Relatórios
content_hash: 08f0fd7e01cfedec506fc48101b8e86384d6dea8debd147890283b7eb2ba09f2
fetched_at: '2026-06-28T22:46:39.209648+00:00'
product: rm
section_id: 1500000861642
source: central-rm
title: 'RH - RM - PTO - Código de erro : 1. Relatório AEJ (Arquivo eletrônico de Jornada)
  da portaria 671/2021'
type: support-article
updated_at: '2025-09-25T12:52:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30763473463703-RH-RM-PTO-C%C3%B3digo-de-erro-1-Relat%C3%B3rio-AEJ-Arquivo-eletr%C3%B4nico-de-Jornada-da-portaria-671-2021
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30763473446039) Tempo aproximado para leitura: **00:00:20 min  
  
Dúvida**  
Ao gerar o  Relatório AEJ (Arquivo eletrônico de Jornada) da portaria 671/2021, aparece o erro abaixo, o que fazer nestes caso?

*Foram feitas alterações nos registros originais/incluídos que impossibilitam a geração do relatório, conforme Portaria 671/2021.*  
*Conforme a Portaria 1510/2009, as batidas dos funcionários só poderão ser alteradas pelo sistema de automação de ponto. Foram identificadas batidas com alterações que não foram executadas pelo sistema:*

*Código de erro : 1. . (Coligada)|(Chapa)| DD/MM/AAAA HHMM:SS  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30763482328599)*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30763482329879)  
 **Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 12.1.  
  
**Solução**  
O erro apresentado indica que as batidas estão na tabela de arquivo morto e, para gerar o relatório, elas precisam estar na tabela de produção. No link abaixo, seguem os passos para enviar as batidas para a tabela de produção:

[RH - RM - PTO - Transferir dados para a tabela de produção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5695661925399)

Ao finalizar o processo de direcionar as batidas para a tabela de produção, gere novamente o relatório AEJ.

Após gerar o relatório, você pode voltar com os dados para a tabela de arquivo morto novamente, para ter uma melhor performance no RM. Abaixo, seguem os passos de como realizar o processo:

[RH - RM - PTO - Transferir dados para a tabela de arquivo morto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5695202103191)  
  
Se ainda não for possível gerar o relatório e aparecer o mesmo erro, torne o período no qual deseja gerar o relatório como ativo, e gere o relatório novamente. Abaixo, seguem os passos de como tornar um período anterior como ativo:

[RH - RM - PTO - Definir período anterior como ativo (Trocar de Período)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024507332)  
  
**Saiba mais:**[RH - RM - PTO - Relatório AEJ (Arquivo eletrônico de Jornada) da portaria 671/2021](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9301019623319)
