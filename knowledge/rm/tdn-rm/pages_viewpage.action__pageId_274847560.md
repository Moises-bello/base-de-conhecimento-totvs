---
content_hash: 49b78fff1c61b71cfdc25448ee73ce31e09dd79be58b61ba69c03e2d1a030165
fetched_at: '2026-06-29T00:08:34.860008+00:00'
page_id: '274847560'
product: rm
source: tdn-rm
title: NFCE0004_Identificacao_do_Destinatario_(dest)_e_endereco_do_Destinatário_(enderDest)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274847560
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | NFC-e - Nota Fiscal do Consumidor Eletrônica |
| **Versões:** | A partir da 12.1.7 |
| **Ocorrência:** | Identificação do Destinatário (dest) e endereço do Destinatário (enderDest): |
| **Passo a passo:** | Introdução: Este documento tem como finalidade orientar quanto a geração das tags referente ao destinatário e endereço do destinatário.    Regra para geração dos grupos de identificação do Destinatário (dest) e endereço do Destinatário (enderDest):    1 - Quando os campos CPF/CNPJ, IDEstrangeiro e Nome No menu "Integrações", aba "Dados da NFC-e" estiverem preenchidos, o destinatário do menu "Identificação", aba "Cabeçalho" será desconsiderado e o o grupo Dest no xml será gerado com os dados CPF/CNPJ, IDEstrangeiro e Nome informados na aba "Dados da NFC-e".            2 - Quando o destinatário do menu "Identificação", aba "Cabeçalho"Cliente/Fornecedor do movimento for DIFERENTE daquele informado como default no Tipo de Movimento (Parâmetros do tipo de movimento | Etapa 2 - Movimento - Emitente e Destinatário | campo Cliente/Fornecedor Destino Default), considera-se que o consumidor FOI identificado no momento da operação e os dois grupos serão GERADOS por completo no xml(Destinatário (dest) e endereço do Destinatário (enderDest)).                3 - Quando o destinatário do menu "Identificação", aba "Cabeçalho"Cliente/Fornecedor do movimento for IGUAL à aquele informado como default no Tipo de Movimento (Parâmetros do tipo de movimento | Etapa 2 - Movimento - Emitente e Destinatário | campo Cliente/Fornecedor Destino Default), considera-se que o consumidor NÃO FOI identificado no momento da operação e os dois grupos serão totalmente OMITIDOS na NFC-e.                IMPORTANTE: em ambiente de homologação a tag xNome sempre será:  NF-E EMITIDA EM AMBIENTE DE HOMOLOGACAO - SEM VALOR FISCAL. |
| **Observações:** | Para mais informações:  [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
