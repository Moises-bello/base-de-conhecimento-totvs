---
article_id: 360041758774
category: Portal de Gestão de Capital Humano
content_hash: 8e8d15a9bf4201b6b0db2e858de78bf867e13aafcc6b1112334f4084ccfdb51f
fetched_at: '2026-06-28T22:42:59.099782+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Ao solicitar desligamento e colocando Não
  no campo "Nova Contratação", o posto deve ser cancelado ou congelado
type: support-article
updated_at: '2021-04-07T12:57:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041758774-RH-Linha-Protheus-PORTAL-GCH-Ao-solicitar-desligamento-e-colocando-N%C3%A3o-no-campo-Nova-Contrata%C3%A7%C3%A3o-o-posto-deve-ser-cancelado-ou-congelado
---

**Dúvida**Ao solicitar desligamento e colocando **Não** no campo "Nova Contratação", o posto deve ser cancelado ou congelado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**Se faz necessário o uso do módulo SIGAORG (70) e utilizar controle de postos com o parâmetro **MV\_ORGCFG= 1**.  
  
Por padrão do sistema, ao calcular uma rescisão o posto será desocupado, mesmo selecionado a opção *Nova Contratação*= **Não**.  
  
Para alterar o status do posto com a opção cancelado ou congelado, deverá realizar a manutenção manual pelo módulo **SIGAORG** através da rotina Cadastro Movimento de Postos (*Atualizações > Movimento > Postos*).  
Abaixo segue um resumo do fluxo da rotina:  
  
Posto ocupado:

![](https://totvssuporte.zendesk.com/attachments/token/x7vX59pu7Fo67LTvxgfqYThi3/?name=inline-89423084.png)​  
  
Gerado solicitação de desligamento com a opção "Nova Contratação"= Não:

![](https://totvssuporte.zendesk.com/attachments/token/M4MXXxah3HUMwNptv8ucdK6N3/?name=inline1907735745.png)​  
  
Após o RH aprovar (TCFA040) e efetuar o cálculo da rescisão:  
​

![](https://totvssuporte.zendesk.com/attachments/token/5tyGU81qj6eA7769U0rHNvVBi/?name=inline969897894.png)​

![](https://totvssuporte.zendesk.com/attachments/token/uPsvVlydbBUViG8iyv4nkX8wL/?name=inline-2102877297.png)​  
  
O status do posto será apresentado como livre, é a **tratativa padrão do sistema**.  
  
Apenas será alterado para cancelado ou congelado se houver uma manutenção manual direto na rotina Movimento de Postos:  
  
Acessando o posto em Atualizar e na opção "Outras Ações" é possível escolher Congelar ou Cancelar:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094960574/mceclip0.png)​  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097263273/mceclip1.png)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
