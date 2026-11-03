---
article_id: 7806133156759
category: Metrologia (SIGAQMT)
content_hash: c5a5a85e7ecf0247b6edecc646c53c09c7f154aa72eaf7e1a4cad32d1aa4acff
fetched_at: '2026-06-28T22:42:24.808189+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Impressão do certificado de calibração
  em formato Word
type: support-article
updated_at: '2022-07-29T14:25:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7806133156759-Manufatura-Linha-Protheus-SIGAQMT-Impress%C3%A3o-do-certificado-de-calibra%C3%A7%C3%A3o-em-formato-Word
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min** **Dúvida**É possível emitir o certificado de calibração do instrumento em formato *Word*?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Solução**Quando realizada a calibração na rotina **QMTA140 - Medições** e o conteúdo do parâmetro **MV\_QICEWOD - Imprime Certificado de Calibração em formato Word** for **2 - Não**, o certificado de calibração será impresso por meio da rotina **QMTR030 - Certificado de Calibração**, porém se o conteúdo do parâmetro for igual à **1 - Sim**, será impresso por meio da rotina **QMTR280 - Certificado de Calibração - Word**, onde fará a leitura do conteúdo do parâmetro **MV\_QMTDDOT - Nome padrão do arquivo modelo (Word) a ser considerado na impressão do Certificado de Calibração**, para saber qual o *layout* utilizar para impressão do certificado em formato *Word*.  
No parâmetro **MV\_QMTDDOT** é preciso definir qual será o *layout* *Word* utilizado para esta impressão. Este *layout* não é padrão da **TOTVS**, e sim definido por cada empresa.  
As únicas restrições são que este arquivo tenha a extensão **.DOT** e esteja armazenado no diretório **/SYSTEM/MODELOS**.
