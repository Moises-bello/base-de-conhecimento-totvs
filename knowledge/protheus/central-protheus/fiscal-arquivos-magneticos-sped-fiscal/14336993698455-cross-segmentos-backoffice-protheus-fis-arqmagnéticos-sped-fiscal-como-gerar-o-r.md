---
article_id: 14336993698455
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: f5351b0fdf0dd57e29e223c234a5e1abb23bc8ed41a960f776aa18b89003c049
fetched_at: '2026-06-28T22:42:03.579834+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Como gerar o registro E300 quando não IE no estado de destino?
type: support-article
updated_at: '2023-05-05T22:12:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14336993698455-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Como-gerar-o-registro-E300-quando-n%C3%A3o-IE-no-estado-de-destino
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00 min** **Dúvida**Como gerar o registros E300 quando não IE no estado de destino?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para atender o Cadastro Simplificado de Contribuintes do ICMS - DIFAL (EC 87/2015), foi criado o campo **F0L\_CGC (CNPJ do Contribuinte)** para que o Contribuinte que tenha apenas o CNPJ, também possa desfrutar do benefício.

É necessário realizar o Cadastro da Inscrição Estadual na rotina **Inscrição Estadual DIFAL -** **FISA115**, no ambiente **Livros Fiscais,** localizar o campo **CNPJ - F0L\_CGC** e preenchê-lo com o CNPJ da empresa.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/14336909966743)**

**Importante:** Com essa configuração feita, o registro 0015 não será gerado. E os registros E300, E310 e E316 do SPED Fiscal - EFD ICMS/IPI serão gerados normalmente.  
Conforme orientação do link a seguir: <https://tdn.totvs.com/x/pgU4Fw>

**Aviso:**Para atender o esperado pelo PVA da EFD-ICMS/IPI, é necessário o cadastro da Inscrição Estadual também para o Estado de origem. Dessa forma, no arquivo do SPED, será gerado um registro E300 para o Estado de origem, com um E310 diretamente ligado à ele, com todos os valores zerados.

Documentação completa

<https://tdn.totvs.com/pages/releaseview.action?pageId=695190614>
