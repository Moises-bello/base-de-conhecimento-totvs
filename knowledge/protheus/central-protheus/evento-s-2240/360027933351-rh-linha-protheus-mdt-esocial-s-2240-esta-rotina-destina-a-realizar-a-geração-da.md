---
article_id: 360027933351
category: Evento S-2240
content_hash: f1da47c84014c7b7ea9ed44d92ab9dae0d833b221b397bbef758e7e04873b4ee
fetched_at: '2026-06-28T22:45:23.506556+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial  - S-2240 - Esta rotina destina a realizar
  a geração das informação iniciais de Condições Diferenciadas de Trabalho (Evento
  S-2240) para o módulo do TAF. Desta forma, é necessário habilitar a integração com
  o SIGATAF
type: support-article
updated_at: '2025-03-03T18:00:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027933351-RH-Linha-Protheus-MDT-eSocial-S-2240-Esta-rotina-destina-a-realizar-a-gera%C3%A7%C3%A3o-das-informa%C3%A7%C3%A3o-iniciais-de-Condi%C3%A7%C3%B5es-Diferenciadas-de-Trabalho-Evento-S-2240-para-o-m%C3%B3dulo-do-TAF-Desta-forma-%C3%A9-necess%C3%A1rio-habilitar-a-integra%C3%A7%C3%A3o-com-o-SIGATAF
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372197627927)** Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**  
Ao acessar rotina de Gerar Riscos **(****MDTA881)**, ocorre mensagem: Esta rotina se destina a realizar a geração das informação iniciais de Condições Diferenciadas de Trabalho **(Evento S-2240)** para o módulo do TAF. Desta forma, é necessário habilitar a integração com o **SIGATAF** para envio.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**  
A rotina Gerar Riscos **(****MDTA881)**, serve exclusivamente para fazer a carga inicial dos Riscos (**S-2240**) para o **TAF**. Ela deve ser utilizada quando iniciar a entrega dos eventos **SST** no **eSocial** para enviar os dados dos riscos que ocorreram antes do inicio da obrigatoriedade estipulado pelo governo.   
  
**Solução**Caso deseje utilizar a rotina Gerar Riscos **(****MDTA881)**, deve ser configurado o parâmetro **MV\_NG2ESOC com 1** para habilitar a integração com o **TAF** e o parâmetro **MV\_NG2DTES** deve estar com a data de inicio do evento **S-2240** no **eSocial**.  
  
**Observações**  
Abaixo deixo documentações relacionadas ao S-2240:

* [RH - Linha Protheus - MDT - eSocial - Quais são os parâmetros utilizados nos eventos SST (Medicina) do eSocial no modulo SIGAMDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027665951)
* [RH - Linha Protheus - MDT - eSocial - Onde encontrar a documentação do protheus de geração dos eventos SST (Medicina e Segurança do Trabalho) para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009642481)
* [Documentação Gerar Riscos eSocial (MDTA881)](https://tdn.totvs.com/x/WrG5HQ)

**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
