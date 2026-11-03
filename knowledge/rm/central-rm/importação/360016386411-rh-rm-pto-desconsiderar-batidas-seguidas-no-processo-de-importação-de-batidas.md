---
article_id: 360016386411
category: Importação
content_hash: 7d6204d9aea651edf1c8b357ef9747f78ff9cefe9dfe6f83aa326461858c43b3
fetched_at: '2026-06-28T22:46:33.736499+00:00'
product: rm
section_id: 6045469428631
source: central-rm
title: RH - RM - PTO - Desconsiderar batidas seguidas no processo de importação de
  batidas
type: support-article
updated_at: '2026-04-17T21:10:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016386411-RH-RM-PTO-Desconsiderar-batidas-seguidas-no-processo-de-importa%C3%A7%C3%A3o-de-batidas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16782299809431) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**  
Como desconsiderar batidas seguidas no processo de importação de batidas?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**  
Para desconsiderar as batidas seguidas no processo de importação de batidas, siga os passos abaixo.

1. Acesse o módulo de **Automação de Ponto**, selecione a guia **Configurações** e o menu **Parametrizador**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39835994088599)
2. Selecione o processo **Sindicato** e avance.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39835994089623)
3. Selecione o sindicato que deseja fazer esta alteração e clique no botão **Parametrizar**.   
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39835994090263)
4. Na etapa **Importação de batidas** do **Parametrizador do Sindicato**, preencha o campo **Tempo mínimo entre batidas** com o tempo mínimo desejado para a importação. As batidas seguidas, cuja diferença seja menor que o tempo estipulado, serão desconsideradas na importação.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39835994090391)

**Importante**  
Ao marcar a opção **Considera tempo mínimo para batidas de acesso**, no momento da importação de batidas de um terminal que as batidas serão consideradas para o cálculo, irá considerar o tempo mínimo entre as batidas.

Para a opção **Considera tempo mínimo para batidas de refeição**, o sistema no momento da importação de batidas de um terminal de refeição irá considerar o tempo mínimo entre as batidas.

Essa parametrização também contempla as batidas importadas pelas integrações da  **Carol Clockin** e  do **Suricato** .

O parâmetro não será validado para registros de ponto que não utilizem o fluxo padrão de importação (exemplo marcações via **Meu RH)**.
