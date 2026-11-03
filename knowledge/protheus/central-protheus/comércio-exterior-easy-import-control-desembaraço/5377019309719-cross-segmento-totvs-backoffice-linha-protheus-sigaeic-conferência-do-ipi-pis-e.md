---
article_id: 5377019309719
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 8dfd6178a09958852aa98cb12de653d29c40fd74ec16c9bdd9bc7bb5bb25ce24
fetched_at: '2026-06-28T22:39:51.017747+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Conferência do
  IPI, PIS e COFINS
type: support-article
updated_at: '2022-04-26T12:18:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5377019309719-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Confer%C3%AAncia-do-IPI-PIS-e-COFINS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como realizar a conferência do IPI, PIS e COFINS?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Easy Import Control - Todas as versões  
  
**Solução**O cálculo realizado no recebimento de importação:   
**1.0 Imposto sobre Produtos Industrializados - IPI**  
É calculado da seguinte forma:

```
Bse do IPI = BASE II + II  
IPI = Base do IPI x alíquota IPI
```

**1.1 PIS e COFINS**  
É calculado da seguinte forma:

```
Base PIS/COFINS = (CIF + ICMS')/(1 - Alíquota PIS – Alíquota COFINS)  
ICMS'= [(CIF + II + IPI) /(1-Alíquota ICMS) ] – II – IPI – CIF  
Base ICMS = (CIF + II + IPI + PIS + COFINS + Desp Base ICMS) /(1 – Alíquota ICMS)
```

Para se chegar ao imposto, basta multiplicar a base pela alíquota.

**Observação****:**O valor da mercadoria, deve ser sempre igual a base do IPI, assim o valor total da primeira nota deve ser definido como:

```
Valor da nota = FOB +FRETE +SEGURO + Despesa base de imposto + II + IPI + Despesa base de ICMS + ICMS + PIS + COFINS
```

Ao apresentar os impostos IPI , PIS e COFINS com valores divergentes da Declaração de Importação (DI), deve-se verificar:

* Alíquotas dos impostos informados no cadastro de NCM, de acordo com a ncm informada no item. Acessar Atualizações-> Tabelas-> NCM-> Alterar.  
  ![CONFERENCIA_NCM.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5375910194583/CONFERENCIA_NCM.gif)
* Cadastro de majoração de PIS e COFINS: Caso o processo possuir majoração, verificar se o cadastro de majoração de PIS e COFINS está de acordo com o documento: [Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Majoração do PIS e COFINS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055118133)

* Regime de tributação: Caso o processo possuir regime de Tributação, necessário verificar se as aliquotas foram informadas de acordo com a DI.  
  ![regime_de_tribu__o.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5380006160791/regime_de_tribu__o.gif)
* Verificar a configuração do parâmetro **MV\_EIC0030** para a rotina de Receb. Importação (EICDI154) para o Sistema considerar as alíquotas de PIS e COFINS no cálculo da Base de PIS e COFINS quando o parâmetro apresentar conteúdo .T., e não considera-las quando o parâmetro apresentar o conteúdo .F..

**Saiba mais**  
[Cross Segmento - TOTVS Backoffice Linha Protheus -SIGAEIC - Divergência de Nota Fiscal de Importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021393491)
