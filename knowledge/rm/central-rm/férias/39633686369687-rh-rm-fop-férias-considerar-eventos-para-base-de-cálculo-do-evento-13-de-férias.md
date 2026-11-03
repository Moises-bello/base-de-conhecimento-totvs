---
article_id: 39633686369687
category: Férias
content_hash: 6922d97a9c96f65797a811c8a3f3599fca724d8eb55d5b285a34038fab359359
fetched_at: '2026-06-28T22:46:56.130775+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: 'RH - RM - FOP - Férias: Considerar eventos para base de cálculo do evento
  1/3 de férias'
type: support-article
updated_at: '2026-04-09T20:24:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39633686369687-RH-RM-FOP-F%C3%A9rias-Considerar-eventos-para-base-de-c%C3%A1lculo-do-evento-1-3-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39633641908759) Tempo aproximado para leitura: **00:01:36min**  
  
**Dúvida**  
Como configurar o sistema para que determinados eventos de provento componham a base de cálculo do evento de 1/3 de férias (Código de Cálculo 40)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para que um evento seja considerado no cálculo do Adicional de Férias (1/3), é necessário que o evento de origem possua a incidência específica marcada em seu cadastro. O sistema utiliza essa flag para identificar quais valores devem somar para a base do Código de Cálculo 40.

1. Vá em **Administração de Pessoal | Eventos | Eventos**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39633641910551)

2. Localize e edite o evento que deve compor a base;

3. Acesse a aba **Inc. Proventos**;

4. Marque a opção **Adicional de Férias** conforme a imagem abaixo: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39633806938903)

 5. Clique em **Salvar** e realize o recálculo do recibo de férias para que os valores sejam atualizados.

⚠️ Importante:   
  
Caso o evento ainda não componha a base de 1/3 após a configuração do parâmetro, é necessário revisar a ordem de prioridade. Para que um evento integre a base de cálculo de outro, ele deve possuir uma prioridade menor (sendo calculado antes). Por exemplo: se o evento de 1/3 tem prioridade 8, qualquer evento com prioridade 9 será ignorado por ser processado posteriormente.

**Saiba mais:**

[RH - RM - FOP - Dúvidas frequentes: Processo de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23673187786007-RH-RM-FOP-D%C3%BAvidas-frequentes-Processo-de-F%C3%A9rias)
