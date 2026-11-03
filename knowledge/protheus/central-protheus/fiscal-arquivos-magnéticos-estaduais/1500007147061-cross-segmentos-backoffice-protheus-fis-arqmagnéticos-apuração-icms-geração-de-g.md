---
article_id: 1500007147061
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: e42c9002c8ae3585e2ef01a3e963e712e305d6ccfa6255a47ab3a1f63ed306d1
fetched_at: '2026-06-28T22:42:09.239102+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - APURAÇÃO ICMS
  - GERAÇÃO DE GUIAS SEPARADAS POR CÓDIGO '
type: support-article
updated_at: '2022-08-17T19:45:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007147061-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-APURA%C3%87%C3%83O-ICMS-GERA%C3%87%C3%83O-DE-GUIAS-SEPARADAS-POR-C%C3%93DIGO
---

**Dúvida**  
Como configurar o Protheus para gerar as guias de GNRE separadas por código na apuração de icms?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Foi implementado um campo no cadastro do código de lançamento, este campo irá determinar se deverá gerar **GNRE** separada por código de lançamento na apuração de ICMS.

Para isso, deverá acessar o cadastro de código de lançamento (**MATA964** Apuração e/ou **MATA985** de Nota Fiscal), e informar no campo **GNRE Apur. (CDO\_GNRESE/****CDO\_GNRESE)** e informar opção **1=Sim**.

 

Desta forma os códigos de lançamentos que estiverem com este campo com conteúdo igual a Sim, terão **GNRE** geradas separadamente do valor total, possibilitando assim geração de **GNRE** com datas de vencimentos e código de receita diferentes, conforme definido na legislação.

Exemplo de utilização com valores na aba de débitos especiais:

Código **GO71101001** com valor de 100,00, este código tem o campo **GNRE Apur**com opção 1=Sim

Código **GO71101002** com valor de 100,00, este código tem o campo **GNRE Apur**com opção 2=Não

Código **GO71101003** com valor de 100,00, este código tem o campo **GNRE Apur**com opção 2=Não

Desta maneira serão geradas duas **GNRE**, uma com valor de 100,00 referente ao código **GO71101001** , e outra com valor de 200,00 referente a soma dos códigos **GO71101002** e **GO71101003**.

Somente serão geradas **GNRE** separadas para os códigos com o campo **GNRE Apur**preenchido com opção**1=Sim,**se este campo estiver vazio ou com opção **2=Não**não terá **GNRE** gerada de forma separada.

Estas regras também se aplicam para as abas de ICMS Próprio e ICMS ST da rotina MATA953.

Mais detalhes no link abaixo:

<https://tdn.totvs.com/display/public/PROT/822281+DSERFIS2-1478+DT_GERACAO_GNRE_SEPARADA_APURACAO>
