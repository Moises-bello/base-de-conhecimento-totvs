---
article_id: 8665675490839
category: Materiais - Compras (SIGACOM)
content_hash: 610d02f7d875f9ad92a088ede6b5174e16ee017ecd7edf282b5a97b12ab3451e
fetched_at: '2026-06-28T22:41:24.057539+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Preenchimento obrigatório
  do campo Motivo do Retorno da opção "Retornar" do Documento de Entrada
type: support-article
updated_at: '2024-04-29T14:41:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8665675490839-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Preenchimento-obrigat%C3%B3rio-do-campo-Motivo-do-Retorno-da-op%C3%A7%C3%A3o-Retornar-do-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Existe algum parâmetro ou ponto de entrada que possibilite o preenchimento do campo Motivo do Retorno ficar obrigatório ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12  
  
**Solução**

É possível se o campo ***F1\_MOTRET*** estiver como obrigatório em seu cadastro no Dicionário de dados.

*Procedimento :*

1. Ambiente -> Configurador -> Base de Dados -> Dicionário -> Base de Dados;

Filtre por SF1 -> F1\_MOTRET-> Alterar -> Uso Obrigatório;

![f1_m.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8665415559959/f1_m.png)

2. Ao realizar o Retorno da do Documento, o help será gerado; 

![motivo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8665465315735/motivo.png)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Finalidade e utilização do Motivo do Retorno na função "Retornar" do Documento de Entrada (MATA103)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018321412-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Finalidade-e-utiliza%C3%A7%C3%A3o-do-Motivo-do-Retorno-na-fun%C3%A7%C3%A3o-Retornar-do-Documento-de-Entrada-MATA103-)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
