---
content_hash: aa1097be2958bcf307f5b4ad8af6499506e521833b501cf65f224f8d8a663066
fetched_at: '2026-06-29T00:08:18.693006+00:00'
page_id: '266966311'
product: rm
source: tdn-rm
title: Ocultar o menu “Esqueceu sua senha?" no RM Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266966311
version: 2
---

# Desabilitar a opção “Esqueceu sua senha?" no RM Portal

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.XX; 12.1.XX |
| **Ocorrência:** | Ocultar / Desabilitar o menu "Esqueceu sua senha?" no RM Portal - Gestão de Conteúdos |
| **Ambiente:** | RM Portal Web - Gestão de Conteúdos |
| **Passo a passo:** | Para ocultar o menu "Esqueceu sua senha?" no RM Portal, acesse o diretório:  C:\totvs\CorporeRM\Corpore.Net, localize o arquivo Web.config:    Altere o valor da tag abaixo para false:  <!--Informa se o controle "Esqueceu sua senha" estará visivel na página de login.-->                                 <add key="RecoverPassVisible" value="false" />    Print do menu padrão:    Após alteração da tag para valor false, o menu se torna oculto: |
| **Observações:** |  |
