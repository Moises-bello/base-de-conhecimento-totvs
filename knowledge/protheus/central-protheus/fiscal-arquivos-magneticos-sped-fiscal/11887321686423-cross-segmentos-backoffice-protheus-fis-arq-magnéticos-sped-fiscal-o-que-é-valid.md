---
article_id: 11887321686423
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: dde830460df50a495399c1f05b2d91bc67bed63ececb8a47340a9443678deb91
fetched_at: '2026-06-28T22:42:02.361501+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - O que é validado para gerar o campo 02 - Centro de Custo do Registro 0305?
type: support-article
updated_at: '2023-01-24T13:07:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11887321686423-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-O-que-%C3%A9-validado-para-gerar-o-campo-02-Centro-de-Custo-do-Registro-0305
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**  
 **Dúvida**O que é validado para gerar o campo **02 - Centro de Custo** do registro **0305 - Informação sobre a utilização do bem?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Quando o parâmetro **MV\_F9SKPNF = .F.**, primeiramente,  o Protheus busca os dados do **Centro de Custo** informados na tabela **SN3 - Saldos e Valores.**  
  
Se não encontrar, busca as informações do **Centro de Custo** informado na nota fiscal, tabela **SD1 - Itens da NF de entrada.** Nesse caso,  há uma condição em que tanto o campo **C.Contabil -  D1\_CONTA** quanto o campo **Centro Custo - D1\_CC** precisam estar preenchidos. 

Não encontrando informações na **SD1** e conforme o conteúdo do parâmetro **MV\_F9CTBCC** utiliza a informação do produto (se houver) ou da **SF9 - Manutenção CIAP.**  
  
No entanto, se o parâmetro **MV\_FPSKPNF** estiver como **T**, a ordem acima é ignorada e todas as informações são validadas de acordo com a tabela **SF9**.
