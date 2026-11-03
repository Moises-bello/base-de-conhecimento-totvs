---
article_id: 360058619654
category: RH - Definições de Cálculo
content_hash: 6f1409bb07dbcbcad899769a4f018db6ce55ae7cdc96acd46261a87d939f1961
fetched_at: '2026-06-28T22:43:22.262930+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - AUDESP - Como gerar Verbas Remuneratórias na Folha
  Ordinária
type: support-article
updated_at: '2025-06-17T18:42:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058619654-RH-Linha-Protheus-GPE-AUDESP-Como-gerar-Verbas-Remunerat%C3%B3rias-na-Folha-Ordin%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26168194473623) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**AUDESP - Como gerar Verbas Remuneratórias na Folha Ordinária?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Para que as verbas sejam geradas no **XML de integração para AUDESP**, é necessário seguir os passos abaixo:  
  
**1 -** Acesse o **SIGAGPE > Atualizações > Definições de Cálculo > Manutenção Tabelas > busque pela S124.**  
Esta tabela armazena as **Verbas Remuneratórias** que são padrão, e é possível também fazer a inclusão de novos tipos.  
Cabe ressaltar que as numerações da coluna CODIGO não correspondem ao código da verba do Protheus, e sim a um código que será vinculado ao cadastro da verba correspondente.  
Neste exemplo, será utilizada a opção **103** - Vencimentos e Vantagens Fixas Pessoal Civil e Militar, que estará vinculada à verba de Salário no Protheus:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32878119705751)  
  
  
**2 -** Em **Atualizações > Definições de Cálculo > Verbas** > localize a verba do Protheus que corresponde à verba de Salário e clique em Alterar > Outros > e no campo **Cod. Remuner.** vincule o código 103 da S124 e salve:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32878106997399)  
  
  
  
**OBS:**Para que os valores sejam gerados no XML, é necessário que o período da Folha de Pagamento já esteja **fechado**, pois as informações são geradas a partir da tabela **SRD**.

**Saiba Mais:**  
[Módulo de Remuneração - AUDESP](https://www.tce.sp.gov.br/legislacao/comunicado/atualizacao-modulo-remuneracao-fase-iii-sistema-audesp)  
[DT - Geração de Dados AUDESP](https://tdn.totvs.com/display/public/PROT/MRH-8278_DT_Audesp_Manutencao_Geracao_Dados)  
[Ponto de Entrada GP920TP7 - AUDESP](https://tdn.totvs.com/display/PROT/DT+PE++Audesp)
