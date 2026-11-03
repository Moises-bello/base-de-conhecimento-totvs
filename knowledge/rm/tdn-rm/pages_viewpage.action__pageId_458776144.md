---
content_hash: ac409f2edfeb240c02c7269cb577b71e2ed468250948eb61f3f373af1f3d0109
fetched_at: '2026-06-29T00:10:14.319655+00:00'
page_id: '458776144'
product: rm
source: tdn-rm
title: 4729001 FISCAL01-7836 DT Código de serviço federal para Sped Fiscal e Sped
  contribuições
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458776144
version: 1
---

# Não cadastrar o código de serviço federal com zeros a esquerda

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | TOTVS Gestão Fiscal |
| **Função:** | Sped Fiscal e Envio de NF-e |
| **Situação/Requisito:** | Ao gerar a rotina SPED fiscal, é retornado o erro no validador quanto ao campo 11 do registro 0200: "O valor informado nesse campo deve possuir o formato NN.NN ". Observação, o erro é apresentado tanto no arquivo SPED FISCAL quanto no arquivo EFD Contribuições. |
| **Solução/Implementação:** | Inclusão da máscara para que o código do serviço federal complete com zeros a esquerda até preencher a máscara de ##.## no Sped Fiscal (Campo 11 - Registro 0200) e NF-e (tag cListServ).  **Assim,o código de serviço federal deve ser informado de acordo com a LC 116/2003, ou seja, SEM zeros não significativos à esquerda.** |
