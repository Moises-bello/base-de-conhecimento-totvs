---
article_id: 360025887391
category: Gestão de Distribuição (SIGAOMS)
content_hash: 70f2a24b25813efa0f149e6e47347d0057f4ed4df2382dbc7f855524881cde4d
fetched_at: '2026-06-28T22:45:50.011021+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Placa de Veiculo Padrão Mercosul
type: support-article
updated_at: '2022-03-21T12:53:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025887391-Log%C3%ADstica-Linha-Protheus-OMS-Placa-de-Veiculo-Padr%C3%A3o-Mercosul
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:21 min****Dúvida**O **Cadastro de veículo - OMSA060** está preparado para informar a **Placa** do veiculo no **Padrão Mercosul**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**O **cadastro de veículo - OMSA060**, campo **Placa - DA3\_PLACA**, está preparado para o novo **Padrão de Placas do Mercosul**.  
  
Formato anterior:  **PRX2501**Formato Mercosul:  **PRX2F01**  
  
O campo possui o **tamanho igual a 8** e contém o **formato @!**  
Para permitir realizar alteração nesse campo, acesse o **SIGACFG-Configurador/Base de dados/Dicionário/**Localize a tabela **DA3**, altere o campo **Propriedade** para **Alterar**.  
  
Exemplo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003991141/mceclip1.png)
