---
content_hash: 4299a182a5886ba0337ebeec02f5c54e13a69b6508506f709816b8290181d7e5
fetched_at: '2026-06-29T00:09:23.186579+00:00'
page_id: '422546063'
product: rm
source: tdn-rm
title: 12.1.17
type: documentation
url: https://tdn.totvs.com/display/LRM/12.1.17
version: 4
---

* Implementação do Município de Taubaté - SP para envio da
* Implementação do Município de Ubá - MG para envio da
* Implementação do Município de Santa Rita do Sapucaí - MG para envio da
* Incluído parâmetro na tela de Geração da Rotina "Benefício do Prodepe (Registro 0025)"
* Melhoria para que os registros E020 e E100 sejam gerados de acordo com o CFOP, conforme regras de geração da rotina. SEF II.
* Efetuada melhoria no processo de Fechamento/Abertura do período fiscal para que seu processamento interno ocorra mês a mês.
* Implementados os status "Aberto parcial" e "Fechado parcial".
* Efetuada melhoria nas rotinas fiscais EFD Contribuições, SPED Fiscal, ECF – Escrituração Contábil\Fiscal, TAF, DAPI, SINTEGRA para não serem geradas quando suas datas de geração estiverem compreendidas dentro de um período fiscal aberto/fechado parcial.
* Inserido log dos lançamentos fiscais que foram selecionados para geração do registro.
* Na seleção dos lançamentos fiscais para geração do registro Y570 será filtrado somente o Cli/For "Pessoa Jurídica".
* O valor do grupo [Compensação do Tributo](http://tdn.totvs.com/pages/viewpage.action?pageId=422546018) foi tratado para que não ultrapasse o valor do imposto a pagar.
* Melhoria na geração da rotina CAT 79/2003 para que sejam gerados todos os arquivos para cada combinação do Código Modelo de Documento e série.
* Implementação do [Registro C176](http://tdn.totvs.com/pages/viewpage.action?pageId=422546176) - Portaria CAT 158 de 2015 - Ressarcimento ICMS Retido por Sujeição Passiva de Subs. Tributaria  
  .
* Implementação da rotina [RMD - Registro de Materiais Dedutíveis - São Paulo](http://tdn.totvs.com/pages/viewpage.action?pageId=422546141).
* Efetuada melhoria no registro F100 do EFD contribuições, para que o campo 16 - IND\_ORIG\_CRED tenha valor apenas para os seguintes CST's: "50", "51", "52", "53", "54", "55", "56", "60", "61", "62", "63", "64", "65", "66", "67".

* Alterado o processo de consulta da NF-e, para que quando a nota for denegada, que o movimento seja cancelado automaticamente no processo de consulta autorização da NF-e.
* [Apuração DIFAL - Por nota Fiscal](http://tdn.totvs.com/pages/viewpage.action?pageId=422545905).
