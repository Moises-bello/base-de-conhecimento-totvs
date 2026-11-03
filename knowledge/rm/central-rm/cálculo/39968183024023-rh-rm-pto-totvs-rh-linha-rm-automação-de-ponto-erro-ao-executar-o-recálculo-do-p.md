---
article_id: 39968183024023
category: Cálculo
content_hash: e3855d0eece64994e20cc7924c2f3220b608552c887af9c1387ef6a7a1d3158e
fetched_at: '2026-06-28T22:46:29.165746+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - TOTVS RH (Linha RM) - Automação de Ponto - Erro ao executar
  o recálculo do ponto individual ou global
type: support-article
updated_at: '2026-04-24T13:54:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39968183024023-RH-RM-PTO-TOTVS-RH-Linha-RM-Automa%C3%A7%C3%A3o-de-Ponto-Erro-ao-executar-o-rec%C3%A1lculo-do-ponto-individual-ou-global
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39968183014551) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao tentar realizar o recálculo do ponto (individual ou global), ocorre o erro  'The process cannot access the file 'C:\CorporeRM\RM.Net\ RMCHRONUS\_CALCULO\_LOG.txt' because it is being used by another process', impedindo o recalculo dos funcionários.  
  
**Ambiente**  
RH - RM - PTO - TOTVS RH (Linha RM) - Automação de Ponto - todas as versões  
  
**Causa**

O incidente geralmente é causado quando outro job ou processo esteja acessando o arquivo de log RMCHRONUS\_CALCULO\_LOG.txt simultaneamente ao recálculo do ponto. Esse arquivo de log é bloqueado enquanto está sendo escrito, e se outro processo tentar acessá-lo, o erro é disparado.

**Solução**

1. Verifique na guia **Ambiente | Gerenciamento de Jobs** se existe Jobs concorrente;
2. No módulo **Automação de Ponto**, acesse **Movimento | Calcular** | edite o perfil salvo e desmarque o parâmetro '**Gera arquivo de LOG técnico'**:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39968206693399)
3. Execute o recálculo novamente e valide se o recálculo será concluído com sucesso.

   **Saiba mais**  
   [Framework - Linha RM - Frame - Identificar job agendado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014009212-Framework-Linha-RM-Frame-Identificar-job-agendado)  
   [Calcular Movimentação](https://tdn.totvs.com/pages/releaseview.action?pageId=452719089)
