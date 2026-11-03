---
article_id: 25918280796055
category: Financeiro - Aplicação / Emprestimos
content_hash: b4df0dc6eaf7fc133a42e30e033cbc380202084616f2cdf081dabd203b50f59f
fetched_at: '2026-06-28T22:37:59.465867+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA018  - Atualização
  / Importação / Exportação de Índices
type: support-article
updated_at: '2024-08-26T20:36:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25918280796055-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA018-Atualiza%C3%A7%C3%A3o-Importa%C3%A7%C3%A3o-Exporta%C3%A7%C3%A3o-de-%C3%8Dndices
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25918280748055) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como realizar a atualização, importação e exportação dos índices através da rotina FINA018 (Atualização de índices)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2310  
  
**Solução**

1 - Atualização pelo **JOB FINXTAXA**

Inicialmente deve acessar a rotina **FINA017 - Cadastro Índices Financeiros** e cadastrar a série da moeda conforme site do BACEN - **[SGS - Sistema Gerenciador de Séries Temporais - v2.1](https://www3.bcb.gov.br/sgspub/localizarseries/localizarSeries.do?method=prepararTelaLocalizarSeries)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25922770179991)

Rodar o **JOB FINXTAXA**, para mais informações, verifique a documentação abaixo:   
**-- [Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - MATA090 - Cadastrar Taxas de Moeda automaticamente via Schedule FINXTAXA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11821936684183)**

Os dados serão gravados na rotina **FINA018 - Atualização de Índices Financeiros**   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25918309468055)

2 - Importação - **FINA018 - Atualização de Índices**  
Os dados de índices podem ser importados através de uma planilha .csv, podendo ser usado o modelo anexo dessa documentação  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25918331471895)

3 - É possível exportar os dados de **índices financeiros** para ter controle dos índices, para isso, utilize a opção de **Exportar** através da rotina **FINA018 - Atualização de Índices**   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25918309469463)

4 - É possível utilizar a **FINA018** através de ***ExecAuto*** fazendo a importação dos **índices** automaticamente

[FINA018 Atualização de Índice - Rotina Automática.](https://tdn.totvs.com/pages/releaseview.action?pageId=6070750)

**Saiba mais**  
[Aplicações e empréstimos - FINA716 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=680254799)  
[Índices Financeiros - FINA017 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=270916329)

[FINA018 Atualização de Índice - Rotina Automática.](https://tdn.totvs.com/pages/releaseview.action?pageId=6070750)
