---
article_id: 14522452522519
category: RH - Folha de Pagamento
content_hash: b90387201b7eca48d51f75492827242bdc104d224f075aa89682b6421ea7cd5f
fetched_at: '2026-06-28T22:44:12.209208+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular a verba de margem consignado na folha
  de pagamento
type: support-article
updated_at: '2025-09-15T14:45:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14522452522519-RH-Linha-Protheus-GPE-Como-calcular-a-verba-de-margem-consignado-na-folha-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26235893754263) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como calcular a verba de margem consignável na folha de pagamento referente ao Totvs Consignado?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12  
  
**Solução**Para calcular a verba de margem consignável na folha de pagamento que utiliza o Totvs Consignado, siga as orientações abaixo:  
  
-O parâmetro **MV\_CONSIG** deve estar habilitado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14609942623639)

-Habilite o mnemônico **P\_CSMARG**, para isso, entre na rotina Mnemônico pelo caminho **>Atualizações >Definições cálculos >Mnemônicos**, pesquise pelo mnemônico **P\_CSMARG** e deixe o conteúdo dele com **.T.**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14522219920791)

-Cadastre uma verba do tipo **Base Provento** e relacione ao ID **1857** e no campo Percentual informe o percentual a ser considerado para a margem consignado, limitando a **30%** (para saber como cadastrar uma verba [CLIQUE AQUI:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411677253783)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14522289267607)

-Tenha o campo **Marg. Cons. (RV\_TCMARG)** no cadastro de Verbas na aba Outros, caso não tenha o campo, será necessário atualizar o ambiente e dicionário de dados com a expedição contínua:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14522281543703)

-Configure cada uma das verbas que deseja que sejam consideradas no cálculo da margem consignável, mude o valor desse campo para 1-Sim. Serão consideradas apenas verbas dos tipos **Provento** e **Desconto:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14522348221207)  
  
  
  
Saiba mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
