---
article_id: 34696422136343
category: Financeiro - Integrações (SIGAFIN)
content_hash: c40deaf71d5595788784a34fec54bc2401a42e0324f7aa37269978676d084ba8
fetched_at: '2026-06-28T22:38:18.501103+00:00'
product: protheus
section_id: 1500001539241
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA770 - Layout Mile
  Serasa
type: support-article
updated_at: '2026-01-22T18:37:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34696422136343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA770-Layout-Mile-Serasa
---

**Dúvida:**  
O sistema possui modelo de layout padrão para importação MILE de envio e retorno da Serasa?

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA770 - a partir do release 12.1.6.  
  
**Solução:**  
Sim, para utilização do envio e recebimento de arquivos da **Serasa**, podem ser importados os layouts padrão do MILE:

* **serasa\_layout\_envio.xml**
* **serasa\_layout\_retorno.xml**

Esses arquivos estão disponíveis no Portal do Cliente.

Para acessar, clique no link abaixo e você será direcionado ao portal:

[Download Mile - LAYOUT SERASA XML](https://suporte.totvs.com/portal/p/10098/download?e=981285)

[A rotina Serasa - Processos (FINA770)](https://tdn.totvs.com/pages/releaseview.action?pageId=496804345) possibilita a integração da base de dados de títulos do Protheus com o serviço [PEFIN](https://www.serasaexperian.com.br/conteudos/pefin-e-refin/) da empresa [Serasa Experian.](https://www.serasaexperian.com.br/)

O processo ocorre com a execução das seguintes etapas:

Geração do lote de títulos;  
Geração do arquivo de envio do lote de títulos;  
Leitura e processamento dos dados do arquivo de retorno do Serasa;  
Gravação do Log de processamento do arquivo

**Saiba mais:**

[SIGAFIN - SERASA - Layouts de envio e retorno utilizando MILE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026466172-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-SERASA-Layouts-de-envio-e-retorno-utilizando-MILE?utm_source=chatgpt.com)

[SERASA - Layouts de envio e retorno utilizando MILE](https://tdn.totvs.com.br/display/public/PROT/SERASA+-+Layouts+de+envio+e+retorno+utilizando+MILE)  
[SIGAFIN -FINA770 - Como a rotina do Serasa grava na tabela FWB as ocorrências: 1 Selecionado Serasa, 2 Enviado Serasa, 3 Reg. Incluído](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006358681-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA770-Como-a-rotina-do-Serasa-grava-na-tabela-FWB-as-ocorr%C3%AAncias-1-Selecionado-Serasa-2-Enviado-Serasa-3-Reg-Inclu%C3%ADdo?utm_source=chatgpt.com)  
[SIGAFIN - FINA770 - HELP: F771RETMANU](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007183821-Cross-segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA770-HELP-F771RETMANU?utm_source=chatgpt.com)
