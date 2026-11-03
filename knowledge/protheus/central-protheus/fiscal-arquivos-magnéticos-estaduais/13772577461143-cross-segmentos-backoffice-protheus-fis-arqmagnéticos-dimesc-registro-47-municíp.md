---
article_id: 13772577461143
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 1fd2423cedbd508f15e11460c10f64ab9b159b3390754807b8f752269695e0d9
fetched_at: '2026-06-28T22:42:10.802091+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DIMESC - Registro
  47 - Município não consta da tabela de municípios '
type: support-article
updated_at: '2023-04-12T16:42:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13772577461143-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DIMESC-Registro-47-Munic%C3%ADpio-n%C3%A3o-consta-da-tabela-de-munic%C3%ADpios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min****Ocorrência**Ao validar o arquivo txt da **DIME** gerado pelo Protheus, ocorre o erro de validação **Registro 47 - Município não consta da tabela de municípios**  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**  
O incidente ocorre, pois a parametrização do sistema está incorreta para o **Cadastro de Cliente/ Fornecedor** quanto ao **código de município** exigido pela **DIME**.  
  
**Solução**Tanto para o **registro 47 -Entradas de Extratores, Produtores Agropecuários e Pescadores**  quanto para o **48 -** **Informações para Rateio do Valor Adicionado,**  o *layout* da **DIME** exige **códigos de municípios** diferentes dos códigos dispostos no **IBGE**, conforme tabela no site da **SEFAZ SC**.  
   
<https://www.sef.sc.gov.br/servicos/servico/41/DIME_-_Declara%C3%A7%C3%A3o_do_ICMS_e_do_Mov._Econ%C3%B4mico>  
  
![](https://totvssuporte.zendesk.com/attachments/token/MU0pEgObgMIX3mgVo9fjdxnHS/?name=image.png)  
   
No Protheus, realize a  seguinte configuração:  
   
1. Crie os campos conforme especificação abaixo, os quais devem ser informados o respectivo município da tabela de municípios utilizado para **DIME**.  
   
![](https://totvssuporte.zendesk.com/attachments/token/CRyGQLyyL9PLGh1SO45qJFRCj/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/0ZpCqzcsnYI3chRhcOqcketca/?name=image.png)  
   
2. Após a criação, informe nos **parâmetros** abaixo:  
   
![](https://totvssuporte.zendesk.com/attachments/token/nBjngOdumKr1Xrpm1LTNq5YbT/?name=image.png)  
    
Importante:

Caso o fiscal da empresa, entenda que não é preciso  gerar o **registro 47**, configure o **parâmetro** abaixo:  
   
**MV\_CFREG47:** Indica quais **CFOPs** deverão ser desconsiderados no processamento do **Registro 47**.
