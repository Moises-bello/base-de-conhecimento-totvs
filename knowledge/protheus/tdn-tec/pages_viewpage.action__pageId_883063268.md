---
content_hash: f5f90a72d1cdd02b57c4b0dbb18fc8194ee984b862dc8391c4ff852316488503
fetched_at: '2026-07-02T19:24:29.448338+00:00'
page_id: '883063268'
product: protheus
source: tdn-tec
title: Erro de timeout na inicialização do serviço do Application Server
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=883063268
version: 1
---

Erro de timeout na inicialização do serviço do Application Server

Caso do serviço do true não seja inicializado e seja apresentada a mensagem abaixo.

É preciso verificar se algum processo, geralmente antivírus, está fazendo checagem nos arquivos do true.

Caso isso ocorra é necessário registrar os componentes do true como exceção no software de antivírus.

No caso do antivírus padrão (Windows Defender) do sistema operacional Windows a exceção pode ser realizada seguindo as instruções: [Adicionar uma exclusão ao Segurança do Windows](https://support.microsoft.com/pt-br/windows/adicionar-uma-exclus%C3%A3o-ao-seguran%C3%A7a-do-windows-811816c0-4dfd-af4a-47e4-c301afe13b26), para outros softwares favor consultar a página do fornecedor.

O mesmo se aplica quando da inicialização do true via console e é apresentada a tela abaixo por um determinado tempo.

No caso da inicialização em console do true, após um período o processo é retomado.
