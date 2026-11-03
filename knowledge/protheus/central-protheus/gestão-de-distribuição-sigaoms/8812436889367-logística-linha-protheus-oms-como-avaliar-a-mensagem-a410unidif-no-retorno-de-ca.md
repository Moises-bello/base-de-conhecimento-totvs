---
article_id: 8812436889367
category: Gestão de Distribuição (SIGAOMS)
content_hash: bc36fd2da8974c06cd813e28d582e20fe91b7154dd3520db3f0a1a5d2a03cf30
fetched_at: '2026-06-28T22:45:49.612748+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como avaliar a mensagem A410UNIDIF no Retorno
  de Carga - OMSA320
type: support-article
updated_at: '2022-09-12T21:01:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8812436889367-Log%C3%ADstica-Linha-Protheus-OMS-Como-avaliar-a-mensagem-A410UNIDIF-no-Retorno-de-Carga-OMSA320
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:24 min****Ocorrência**No **TOTVS OMS - Order Management System**, ao realizar o **Retorno de Carga - OMSA320** para gerar a **Nota Fiscal de Devolução,** é apresentado a mensagem **A410UNIDIF - Por se tratar de uma Nota Fiscal de Devolução, o valor unitário deve ser igual ao da Nota Fiscal de Origem.****Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Causa**Esse incidente ocorre devido **Retorno de Carga - OMSA320** utilizar **Execauto** para chamar os programas do **Módulo de Compras.**Para resolver a mensagem **A410UNIDIF** é necessário **validar os campos no dicionário referente ao Tamanho e Casas Decimais dos campos citados abaixo.  
  
Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Seguem os principais campos de **Quantidade** relacionados a este processo que deverão possuir o mesmo **X3\_TAMANHO**, **X3\_DECIMAL** e **X3\_PICTURE**:  
    **Quantidade - D1\_QUANT****Quantidade -** **D2\_QUANT  
   Quantidade - C6\_QTDVEN**    
   **Quantidade Liberada** - **C6\_QTDLIB  
   Quantidade Liberada  -**  **C9\_QTDLIB** Caso não possuírem as mesmas propriedades, deve-se alterar para padronizar.
2. Seguem os principais campos de **Valor Unitário** relacionados a este processo que deverão possuir o mesmo **X3\_TAMANHO**, **X3\_DECIMAL** e **X3\_PICTURE**:   
     
   **Valor Unitário - D1\_VUNIT**  
    **Valor Unitário - D2\_PRCVEN**  
   **Preço de Tabela  - D2\_PRUNIT**  
   **Preço Unitário Liquido  - C6\_PRCVEN**  
   **Preço Unitário de Tabela  - C6\_PRUNIT**  
   **Preço de Venda Liberado  - C9\_PRCVEN**  
   Caso não possuírem as mesmas propriedades, deve-se alterar para padronizar.
3. Seguem os principais campos de **Valor Total** relacionados a este processo que deverão possuir o mesmo **X3\_TAMANHO**, **X3\_DECIMAL** e **X3\_PICTURE**:   
     
   **Valor Total - D1\_TOTAL**  
    **Valor Total - D2\_TOTAL**  
    **Valor Total - C6\_VALOR**  
   Caso não possuírem as mesmas propriedades, deve-se alterar para padronizar, sendo o padrão indicado tamanho 2.  
     
   **Saiba mais**Mais informações poderão ser acessadas nos *links*:  
   [Cross Segmento - TOTVS Backoffice (Linha Protheus)- SIGAFAT - Ajuda: A410UNIDIF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028613392-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-A410UNIDIF?source=search)  
   [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O que fazer quando ocorre os Alertas A410UNIDIF / A100VALOR / A410TOTAL nos processos de nota fiscal ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004971371-MP-SIGACOM-O-que-fazer-quando-ocorre-os-Alertas-A410UNIDIF-A100VALOR-A410TOTAL-nos-processos-de-nota-fiscal-?source=search)  
   [Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na rotina Retorno de Cargas - OMSA320](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411608756631-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Retorno-de-Cargas-OMSA320)  
   [Logística - Linha Protheus - OMS - Quais funcionalidades compreende a rotina de Retorno de Cargas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063841253-Log%C3%ADstica-Linha-Protheus-OMS-Quais-funcionalidades-compreende-a-rotina-de-Retorno-de-Cargas-)
