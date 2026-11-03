---
article_id: 360018682352
category: Movimento
content_hash: 834ca02c7f12dc9f79c59613bed701291bc70a2a5d3edca372232cf61da2f457
fetched_at: '2026-06-28T22:46:36.077430+00:00'
product: rm
section_id: 1500000861602
source: central-rm
title: RH - RM - PTO - Cancelar movimento
type: support-article
updated_at: '2025-09-25T16:24:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018682352-RH-RM-PTO-Cancelar-movimento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19409018861079) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como cancelar o movimento dos funcionários?  
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 11.80  
  
**Solução**Para cancelar o movimento dos funcionários, acesse o módulo de **Automação de Ponto** e siga os passos abaixo:

1. Acesse a guia **Movimento** e selecione a opção **Cancelar Movimento;**  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13732782581655)
2. A janela de cancelamento será aberta. Selecione a data ou período desejado, clique no **botão de Seleção de Funcionários** para realizar o cancelamento global (geral ou determinado grupo de funcionários) ou selecione a chapa do funcionário para realizar de forma individual e faça a parametrização conforme o desejado:   
     
   **Informações importantes sobre os parâmetros:**  
     
   - O sistema não permite gerenciar batidas de períodos anteriores ao período atual informado no módulo de períodos do sistema.  
     
   - **Na seleção de tipos de pessoas:** há a possibilidade de desconsiderar batidas de funcionários, visitantes ou dos dois tipos de pessoas ao mesmo tempo.  
     
   - O **Status** da batida deve ser informado no cancelamento, sendo:  
   **Coletadas** - Coletadas pelo relógio.  
   **Digitadas** - Incluídas ou alteradas pelo usuário.  
   **Trânsito** - Coletadas pelos terminais de coleta e que não são consideradas pelo cálculo.  
   **Abonos** - onde serão cancelados os abonos do período informado, além do movimento.  
     
   **- Cancela batidas de refeição:** onde serão desconsideradas as batidas coletadas pelo relógio de refeitório que estão cadastradas no cadastro do funcionário, na pasta Refeições, subpasta Batidas de Refeições.  
   **Batidas normais:** onde serão desconsideradas as batidas;  
   **Batidas da ausência planejada :** onde serão desconsideradas as batidas lançadas para a pasta de Espelho do período do funcionário que coincidirem com o intervalo de refeição cadastrado no horário do funcionário. O sistema também verificará a tolerância cadastrada no parâmetro Sindicato RM Chronus do funcionário para efetuar o processo.  
     
   **Observação:** Caso o recálculo para o usuário logado esteja travado  ou recálculo do funcionário contido no filtro de seleção esteja bloqueado, o processo de cancelamento de batidas não será executado.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13733090360087)
3. Ao definir toda a parametrização, clique no botão **Executar**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/13733076837015)

**Saiba Mais**  
Para mais informações sobre os parâmetros da rotina, acesse a documentação [Cancelar Movimento](https://tdn.totvs.com/display/LRM/Cancelar+Movimento).
