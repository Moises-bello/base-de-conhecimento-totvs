---
article_id: 4410193787415
category: Contabilidade Gerencial - Entidades
content_hash: f526297831aca838732baeab268599dbe6767ebc16ccd0d280626e3fa043fded
fetched_at: '2026-06-28T22:40:49.779777+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB CTBA140 MOEDANEXIS Problema
  : Campo CTx_CVDnn não existe (onde nn é o Código da moeda)'
type: support-article
updated_at: '2022-03-10T12:03:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410193787415-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA140-MOEDANEXIS-Problema-Campo-CTx-CVDnn-n%C3%A3o-existe-onde-nn-%C3%A9-o-C%C3%B3digo-da-moeda
---

**Ocorrência**

MOEDANEXIS

Problema : Campo CTx\_CVDnn não existe (onde nn é o Código da moeda)

Solução :ATENÇÃO !!!!!

Ao criar esta moeda , certifique -se de criar os campos relacionados a ela.  
Maiores detalhes poderão ser encontrados no Help do Programa

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410193585815/mceclip0.png)

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 11.80  
  
**Causa**

Help é apresentado quando o sistema não encontra os campos nas tabelas do contábil para a moeda a ser criada.  
  
**Solução**

Neste exemplo a mensagem é apresentada ao realizar o cadastro de uma moeda 06.  
  
Portanto verifique se o seu ambiente o campo CT1\_CVD06 existe, caso não o tenha, é um indicio de que não há os campos relacionados a moeda 06 no seu sistema, sendo necessário rodar o compatibilizador específico para a moeda conforme a documentação: [MP - SIGACTB - Criação de Moedas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014476031-MP-SIGACTB-Cria%C3%A7%C3%A3o-de-Moedas?source=search)  
  
\*Homologar em ambiente de testes  
  
OBS: Lembrando que após rodar o compatibilizador U\_CTBWIZMOED, os campos referente a moeda serão criados no dicionário e no banco, sendo necessário realizar backup completo do ambiente para se desejar retorno.
