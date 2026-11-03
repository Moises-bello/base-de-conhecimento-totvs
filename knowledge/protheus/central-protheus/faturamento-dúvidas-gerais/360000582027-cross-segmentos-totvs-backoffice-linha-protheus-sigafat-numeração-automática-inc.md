---
article_id: 360000582027
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 509e5cc0e19648332d815e116833cae7c2face1279c8ca23c4ecd01827e1a5cd
fetched_at: '2026-06-28T22:38:30.004063+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Numeração automática
  incorreta nas Tabelas do Protheus
type: support-article
updated_at: '2025-09-12T19:43:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000582027-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Numera%C3%A7%C3%A3o-autom%C3%A1tica-incorreta-nas-Tabelas-do-Protheus
---

**Ocorrência**

A sequencia de numeração automática esta incorreta nas tabelas do Protheus, como ajustar?  
  
**Ambiente**

Microsiga Protheus – A partir da release 11.80.  
  
**Causa**

Esse incidente ocorre quando as configurações para o Controle de Numeração do Protheus estão incorretas no ambiente, ou quando há numerações incorretas ou lacunas entre os registros já gravados no Banco de Dados para a Tabela.  
  
**Solução**

Veja nosso vídeo sobre o assunto no YouTube: [**Ajuste de Numeração automática das tabelas**](https://youtu.be/BhEo-9FFUIQ)

Para ajuste é necessário validar três pontos no sistema:

     1 - Validar que seu controle de numeração está devidamente configurado para utilizar o License Server;  
     2 - Validar que o Formulário (a tabela / rotina) em questão possui realmente a função de numeração automática;  
     3 - Ajuste da numeração automática.  
  
Na documentação abaixo é detalhado o procedimento para analise, realize os ajustes de seu ambiente seguindo criteriosamente as instruções.

**Saiba Mais:** [Ajuste de Numeração automática dos Formulários (Tabelas / ALIAS) no Protheus](http://tdn.totvs.com/pages/releaseview.action?pageId=235570751)
