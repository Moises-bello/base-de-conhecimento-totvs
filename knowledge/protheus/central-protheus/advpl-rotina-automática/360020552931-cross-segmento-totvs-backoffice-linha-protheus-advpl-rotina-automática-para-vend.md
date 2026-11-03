---
article_id: 360020552931
category: ADVPL - Rotina Automática
content_hash: e1cf7e5254bccd02eb5a35c0f808a1868189e9a895dfbeb4283adfdf519571ad
fetched_at: '2026-06-28T22:40:25.050425+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Rotina automática
  para venda no Loja701
type: support-article
updated_at: '2022-06-21T17:19:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020552931-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-para-venda-no-Loja701
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:04:00 min  
  
Ocorrência**Ao executar a rotina automática do LOJA701 (Venda Assistida) para geração de uma venda (não orçamento) são exibidos os erros abaixo:  
  
ERRO 01

```
invalid field name in Alias SD2->D2_NUMSERIE on LJGRVTRAN(LOJXFUNC.PRW)
```

ERRO 02

```
Function GetClientDir() doesn't available in JOB. in file d:\bamboo-agent-5.7.2\xml-data\build-dir\tp11-buildv2appsrv-tec11win32rpo32\advtec9_tt11\advpl\arqdirfuncs.inl
```

**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**A rotina rotina automática do LOJA701 disponibiliza a inclusão de orçamento para futura finalização ou após manipulação (através de customizações) dos registros gerados para explosão no GrvBatch().

A rotina não está homologada com integração SIGACRD, assim como também não é homologada para finalização de venda, ou seja, o segundo parâmetro deve ser sempre 3 e não deve ser utilizado o 9º parâmetro (parâmetro i: lSalVen) como verdadeiro.

```
MsExecAuto({|a, b, c, d, e, f, g, h| LOJA701(a, b, c, d, e, f, g, h)}, .F., 3, "", "", {}, aHeader, aItems, aPayment)
```

Ou seja, os erros acima citados ocorrem pelos seguintes motivos:  
  
ERRO 01: O campo D2\_NUMSERIE não existe no banco ou na relação de campos (SX3), assim sendo, quando a rotina é executada sem interface gráfica (em *web services* ou rotina automática), o campo D2\_NUMSERIE não é ignorado e quebrado para D2\_NUMSERI, desta forma, gerando o erro acima reportado.

Contudo, o erro somente será reproduzido se o arquivo SIGAMAT.emp estiver contendo um grupo de CNPJ específicos (empresas utilizadas para testes internos), assim sendo, será necessário que o cliente altere o arquivo de empresas (para o seu próprio) para que o erro não seja reproduzido.  
  
ERRO 02: Este erro somente é reproduzido quando o cliente tenta utilizar a rotina automática do LOJA701 para efetuar a finalização de vendas, desta maneira, serão chamadas funções que não têm tratamento para execução sem interface gráfica (situações de IsBlind() == .T.).  
  
**Solução**Dado ao fato desta limitação/restrição já estar registrada na documentação oficial da rotina automática do LOJA701, será necessário que o cliente descontinue o uso da MsExecAuto() para operações de venda.  
  
**Observação**Não se deve utilizar a rotina automática FATA701, sempre utilize a rotina automática de Venda Assistida (LOJA701).  
  
**Saiba mais**[ROTINA AUTOMÁTICA LOJA701](http://tdn.totvs.com/pages/viewpage.action?pageId=6787264)
