---
article_id: 12434337298583
category: MIDDLEWARE eSocial
content_hash: 6c9ae3ad8e6865d9fe438307a581dd4195f4b60b61a7240d0c8e4ef1c1d055fc
fetched_at: '2026-06-28T22:43:05.088084+00:00'
product: protheus
section_id: 360005445753
source: central-protheus
title: 'RH - Linha Protheus - Middleware - GPE - Erro ao transmitir eventos utilizando
  Middleware: No XML de retorno não consta informações de erros, consulte XML no TSS'
type: support-article
updated_at: '2025-03-03T20:15:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12434337298583-RH-Linha-Protheus-Middleware-GPE-Erro-ao-transmitir-eventos-utilizando-Middleware-No-XML-de-retorno-n%C3%A3o-consta-informa%C3%A7%C3%B5es-de-erros-consulte-XML-no-TSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24422731866647) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao transmitir eventos através do monitor **TAFA552C** do *Middleware* é retornado o erro: **No XML de retorno não constam informações de erros, consulte o XML no TSS.**  
  
![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12434140221975)  
**Ambiente**TOTVS RH (Linha Protheus) - Gestão de Pessoas - Todas as versões  
  
**Causa**O erro apresentado pode ser detalhado dentro das tabelas **SPED400**, **SPED400A** e **SPED400B** no campo **XMLERRORET** e costuma ocorrer devido a configurações incorretas no *Wizard*:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12434035782935)  
  
Podemos utilizar de exemplo o campo **CNPJ/CPF Transmissor (Dif. Empregador):**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12433982861335)  
Caso este campo seja preenchido com um CPF/CNPJ, sem que, a empresa tenha um procurador judicialmente responsável e que o CPF/CNPJ do mesmo não esteja informado no certificado da empresa, irá ocasionar os erros demonstrados acima.  
  
**Solução**Analise a configuração do *Wizard* e a necessidade de preenchimento de todos os campos.

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
