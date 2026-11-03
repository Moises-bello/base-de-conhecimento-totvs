---
content_hash: 2e1446dd1030bd826b30646b5463dc4f4f3c5d85b78d6f90407b6ee563b4a41a
fetched_at: '2026-06-29T00:09:45.871176+00:00'
page_id: '435099290'
product: rm
source: tdn-rm
title: 3665160 FISCAL01-6344 - SPED Fiscal C197/D197 com o cadastro de Códigos de
  Ajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435099290
version: 3
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | SPED Fiscal |
| **Situação/Requisito:** | Os Registros C197 e D197 passam a ser gerados com base nos novos Anexos de Código de Ajuste. |
| **Solução/Implementação:** | Foi modificado o SPED Fiscal para gerar os dados do código de ajuste (registros C197/D197) através do novo cadastro de Código de Ajuste (Verificar documentos relacionados) informados no lançamento Fiscal.    Código de Ajuste preenchido no Lançamento Fiscal (Pasta Ajuste Sped)    Código de Ajuste preenchido no Item do Lançamento Fiscal (Pasta Ajuste Sped)    Ao gerar o SPED os registros serão gerados conforme abaixo    No caso do C197 o registro não agrupou devido a chave do registro, já o D197 o registro agrupou desprezando a alíquota e a descrição.  Se o registro estivesse somente no item seria gerado conforme abaixo    Se estivesse somente no lançamento seria gerado conforme abaixo.   ATENÇÃO Os códigos de ajuste podem ser preenchidos automaticamente no Lançamento Fiscal, para isso é necessário vincular o código cadastrado ao CFOP verifique os documentos relacionados para melhor entendimento |
| **Documentos Relacionados:** |  |
