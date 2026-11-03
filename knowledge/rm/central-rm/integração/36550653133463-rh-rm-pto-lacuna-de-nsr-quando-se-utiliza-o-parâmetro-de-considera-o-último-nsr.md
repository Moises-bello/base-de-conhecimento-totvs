---
article_id: 36550653133463
category: Integração
content_hash: 78be2c7c16d659afb5f25bf8fccda8d9062792ab94a9b00f16d9c453414ed313
fetched_at: '2026-06-28T22:46:34.630297+00:00'
product: rm
section_id: 6045439793431
source: central-rm
title: RH - RM - PTO - "Lacuna de NSR" quando se utiliza o parâmetro de Considera
  o Último NSR Importado
type: support-article
updated_at: '2025-11-24T19:45:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36550653133463-RH-RM-PTO-Lacuna-de-NSR-quando-se-utiliza-o-par%C3%A2metro-de-Considera-o-%C3%9Altimo-NSR-Importado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36550653119895) Tempo aproximado para leitura: **00:03:30 min**  
  
**Dúvida**  
O sistema possui integração com a Carol Clockin, o funcionário possui marcação com NSR gerado, dispositivo está integrado, mas ainda sim as batidas não importaram, o que pode ser? O parâmetro Considera o Último NSR Importado está habilitado.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 12.1.28  
  
**Solução**  
Em relação ao "salto de NSR" durante o processo de importação de batidas, é necessário algumas considerações:  
  
Com o parâmetro **Considera o Último NSR Importado** **marcado**, a importação irá considerar o último NSR gerado pela Carol e não será permitida a importação por período.

A opção Período de importação ficará desabilitada.  
  
![importa2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36550766607127)  
  
O NSR (Número Sequencial de Registro) é gerado pelo Clockin a cada batida de ponto e serve como referência para o RM TOTVS Automação de Ponto identificar quais marcações já foram importadas.  
   
Entre a geração dessas batidas no Clockin e a chegada delas ao Automação de Ponto, existe o que chamamos de **pipeline**, que é um fluxo automatizado de etapas internas pelas quais os dados passam até ficarem prontos para serem consumidos (processos como validação, formatação e disponibilização das informações etc).  
   
Em alguns casos, determinados NSRs ainda não estão totalmente processados nesse pipeline no momento em que o sistema realiza a importação. Pode ser por falta de conexão a rede no dispositivo ao qual possui a marcação, por exemplo, entre outros fatores externos.  
  
Quando isso acontece, o Automação de Ponto entende que esses registros ainda não existem e segue para os próximos disponíveis, gerando o que chamamos de “salto” na sequência de NSRs.   
   
Esses registros acabam ficando disponíveis posteriormente, mas o Automação de Ponto já não os consome automaticamente.  
   
**Exemplo:**  
Suponha que as batidas com **NSR 1050, 1051, 1052 e 1053** tenham sido geradas pelo Clockin, mas no momento da importação apenas os **NSRs 1050, 1051 e 1053** estavam disponíveis na pipeline.  
  
O RM importará os NSRs 1050, 1051 e 1053, **“pulando” o 1052**, pois ainda não estava pronto para consumo.  
  
Quando o 1052 ficar disponível, o RM não o importará automaticamente, já que ele considera apenas os registros gerados após o **último NSR importado (no caso, o 1053)**.  
Com o parâmetro **“Considera o último NSR importado”** marcado, o sistema segue exatamente essa lógica — ou seja, apenas buscará os NSRs gerados após o último importado.  
  
Devido a isso, recomendamos a criação de um agendamento de job para o processo de importação de batidas diário adicional com **o parâmetro Considera o Último NSR Importado desmarcado**, para que o sistema revise todas as marcações do período e traga eventuais registros que ficaram de fora, sem depender da sequência. Sugerimos que este job execute em um horário em que não haja expediente. Ou se houver, que execute em um horário onde há menos funcionários em execução de jornada. Desta forma, o job irá contemplar o maior número possível de batidas.

**Saiba mais**

Para criar agendamento de importação de batidas, utilizando a integração, segue artigo de apoio:  
[RH - RM - PTO - Importação automática de batidas com integração via Clockin (Carol)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4427635287319-RH-RM-PTO-Importa%C3%A7%C3%A3o-autom%C3%A1tica-de-batidas-com-integra%C3%A7%C3%A3o-via-Clockin-Carol)

**Importante**

* Lembrando que para o artigo acima, ao efetuar o agendamento deverá manter o parâmetro de **Considera o Último NSR Importado desmarcado.** E, além disso, durante o agendamento, no campo Fim, do período de importação informar uma data futura. Por exemplo, 31/12/2050.  
    
  ![importa.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36550637374615)

  Será a mesma lógica aplicada para agendamento de importação de batidas quando se utiliza o arquivo AFD.txt (Arquivo de Fonte de Dados gerado pelo REP).  
  No passo 2 em diante irá conter os detalhes:  
  [RH - RM - PTO - Como agendar o processo para importar as batidas de forma automática](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014195451-RH-RM-PTO-Como-agendar-o-processo-para-importar-as-batidas-de-forma-autom%C3%A1tica)
* Somente ambientes em 3 camadas é que será possível efetuar agendamentos de job.
