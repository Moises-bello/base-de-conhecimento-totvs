---
article_id: 30194905460375
category: Gestão organizacional
content_hash: 54313189936a2a711007136e25e6ce95b21a9af4607c7cff414ac71dac8b17d4
fetched_at: '2026-06-28T22:47:22.236718+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Processos Trabalhistas: Preenchimento do S-2500 quando houve
  inclusão ou alteração de data de desligamento'
type: support-article
updated_at: '2025-09-19T19:37:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30194905460375-RH-RM-RHU-Processos-Trabalhistas-Preenchimento-do-S-2500-quando-houve-inclus%C3%A3o-ou-altera%C3%A7%C3%A3o-de-data-de-desligamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30194885696279) Tempo aproximado para leitura: **00:01:50 min** **Dúvida**Como deve ser preenchido o Processo Trabalhista (S-2500) quando o trabalhador possui o vínculo formalizado com inclusão ou alteração de data de desligamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2402.245**, **12.1.2406.185**, **12.1.2410.121** e **superiores**.  
  
**Solução**Esta situação refere-se ao código **'3 - Trabalhador com vínculo formalizado, com inclusão ou alteração de data de desligamento'** no **'Tipo de Contrato'** e deve ser utilizado para o caso em que o trabalhador já tinha seu vínculo devidamente reconhecido, mas houve mudança em sua data de desligamento, mantendo-se inalterada a data de admissão. **Se o vínculo já tiver sido encerrado antes do início da obrigatoriedade de envio dos eventos não periódicos ao eSocial, deve ser utilizado o {tpContr} = [7];**

Com o campo **{tpContr}** do grupo **[infoContr]** deste evento ser preenchido com **[2]**, **[3]** ou **[4]**, quando o vínculo já se encontra encerrado, antes do envio do evento S-2500, o declarante deve:

***b)** nos casos de [tpContr] igual a [3] ou [4]:*

***b.1)** quando a modificação da data do desligamento não  implicar mudança do período de apuração, deve ser feita a retificação do evento S-2299 para modificar a data e o motivo de desligamento, se for o caso, bem como informar no campo {nrProcTrab} o número do processo, informado no evento S2500;*

***b.2)** quando a modificação da data do desligamento implicar mudança do período de apuração, o evento S-2299 deve ser excluído e reenviado, também referenciando o número do processo no campo {nrProcTrab}. É importante se atentar que:*

***b.2.1)** para que ocorra a exclusão do evento S-2299 é necessária a prévia exclusão do evento o S-1210 que lhe faz referência;*

***b.2.2)** os valores das verbas que constam no evento S-2299 excluído sempre devem ser informados num evento S-1200 relativo ao mês desse evento excluído, além do reenvio de um evento S-1210;*

***b.2.3)** se a nova data do desligamento é em mês anterior, deverá ser informado no evento S-2299, no campo {dtFimRemun} a data relativa ao último dia do mês referente ao último S-1200 existente e no campo {indRemun} o código [2].*

**Importante**As informações referente ao preenchimento correto estão presentes no [Manual de Orientação do eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-03-2025.pdf). Validem a documentação em casos de dúvidas e se necessário, devem acionar o eSocial - Governo para auxiliá-los melhor em dúvidas específicas do processo.   
  
[RH - RM - FOP - eSocial - Contato com o Governo para dúvidas sobre os eventos do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432)  
  
**Saiba Mais**

Para maiores informações, acesse:

- [RH - RM - RHU - Dúvidas frequentes: geração dos eventos de Processos Trabalhistas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17623656599575)
