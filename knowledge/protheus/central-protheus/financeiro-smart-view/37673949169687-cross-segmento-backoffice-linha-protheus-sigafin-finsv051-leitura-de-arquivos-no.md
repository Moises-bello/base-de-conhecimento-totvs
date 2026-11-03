---
article_id: 37673949169687
category: Financeiro - Smart View
content_hash: ab3c5b02201eeddc7c01524c43fa9c49613ca615d21372ac509b3694841f8a47
fetched_at: '2026-06-28T22:37:44.636558+00:00'
product: protheus
section_id: 32632656432151
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINSV051 - Leitura de
  arquivos no disco C:\
type: support-article
updated_at: '2026-06-05T14:26:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37673949169687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINSV051-Leitura-de-arquivos-no-disco-C
---

**Dúvida**  
Existe alguma alternativa de configuração para o StartPath utilizado no relatório FINSV051, como permitir a definição de um diretório local (Exemplo: C:\Relatorios)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as Versões  
  
**Solução**

Não existe alternativa de configuração para alteração e leitura a partir de um diretório local. Conforme apresentado na própria janela de parametrização do relatório, os arquivos informados nas perguntas **Arquivo de Entrada** e **Arquivo de Config** precisam, obrigatoriamente, estar dentro do **StartPath** (diretório raiz) do Protheus.

Desta forma, o sistema não permite a leitura de pastas locais da estação de trabalho (Exemplo: Unidade C:\ ou D:) ou mapeamentos de rede externos ao diretório configurado no *Appserver.ini*.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37673977684375)
