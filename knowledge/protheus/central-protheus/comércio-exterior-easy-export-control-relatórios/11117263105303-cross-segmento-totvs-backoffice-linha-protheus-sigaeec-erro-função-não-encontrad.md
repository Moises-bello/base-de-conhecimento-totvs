---
article_id: 11117263105303
category: Comércio Exterior - Easy Export Control - Relatórios
content_hash: 6b40b96abf49a50719e3f0ef97aba622a2bd573c2dab2f9d8aef6e05eefe1ce9
fetched_at: '2026-06-28T22:36:59.921752+00:00'
product: protheus
section_id: 1500001538161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Erro Função não
  encontrada H_
type: support-article
updated_at: '2022-12-21T14:38:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11117263105303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Erro-Fun%C3%A7%C3%A3o-n%C3%A3o-encontrada-H
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao tentar impressão da *commercial Invoice(*relatório 37*)* ocorre o erro "Função não encontrada H\_"  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – A partir da versão 12.1.33.  
  
**Solução**Conforme cenário apresentado, realizar a recriação das tabelas "**EWQ**" e "**EEA**" com carga padrão para solução do incidente de acordo com os passos abaixo :

1- Verificar e limpar o conteúdo do parâmetro "**MV\_EEC9999**";

2- Realizar o *backup* e *drop* das tabelas "**EWQ**" e "**EEA**" para recriação com carga padrão;

3-  Acessar o ambiente via **SIGAEEC** para ser feita a carga padrão e criação das tabelas "dropadas";

4-  Executar novamente a impressão do relatório 37.

**Observação:**Caso possua customizações dos relatórios(tabela "**EEA**"), se faz necessário acresce-las após a recriação das tabelas pela carga padrão.
