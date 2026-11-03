---
article_id: 1500012787961
category: RH - Folha de Pagamento
content_hash: 4e5ac85b49d1b08d843656b11700151be03171c65e69291001956b7264470978
fetched_at: '2026-06-28T22:44:14.785489+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como separar na folha de pagamento o INSS terceiros
  entre Outras Entidades
type: support-article
updated_at: '2025-04-23T12:29:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012787961-RH-Linha-Protheus-GPE-Como-separar-na-folha-de-pagamento-o-INSS-terceiros-entre-Outras-Entidades
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25967798772119) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como separar na folha de pagamento o INSS terceiros entre Outras Entidades?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução** **1.** Entre na rotina **Manutenção Tabelas**, pelo caminho >**Atualizações** >**Definições de Cálculo** >**Manutenção Tabelas (GPEA320)**;  
**2.** Selecione a **Tabela S038** e em **Outras Ações** clique em **Alterar**:  
**3.** Desmembre os percentuais de Outras entidades conforme a necessidade de cálculo, com os percentuais em suas respectivas colunas:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500020005721)

Ao calcular a folha, o sistema desmembrará os percentuais conforme cadastrado na Tabela S038:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500020007121)  
  
**OBS.:** No exemplo acima, foi desmembrado apenas o percentual de outras entidades SENAI, mas se for necessário calcular o percentual separado das demais entidades, cadastre seus percentuais em suas colunas da Tabela S038, onde será calculado nos IDs abaixo:  
  
0184 - Contr. INCRA.   
0185 - Contr. SENAI   
0186 - Contr. SESI   
0187 - Contr. SENAC   
0188 - Contr. SESC   
0189 - Contr. SEBRAE.   
0190 - Contr. DPC.   
0191 - Contr. FAER.   
0192 - Contr. SENAR.   
0193 - Contr. SECONC.   
0200 - Contr. SEST  
0201 - Contr. SENAT  
0204 - Contr. Salario Educação

**Saiba Mais**  
Para adquirir mais conhecimento acesse o(s) *link*(s) abaixo:

[RH - Linha Protheus - GPE - Qual motivo do percentual de Terceiros não estar calculando para a folha de pagamento, verba de ID 0149](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060300713-RH-Linha-Protheus-GPE-Qual-motivo-do-percentual-de-Terceiros-n%C3%A3o-estar-calculando-para-a-folha-de-pagamento-verba-de-ID-0149?source=search)  
[RH - Linha Protheus - GPE - Outras entidades não estão sendo geradas na guia GPS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014263931-RH-Linha-Protheus-GPE-Outras-entidades-n%C3%A3o-est%C3%A3o-sendo-geradas-na-guia-GPS)
