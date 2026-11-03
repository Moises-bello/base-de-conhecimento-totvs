---
content_hash: ae9ac281d1c8189e4897fd8dfaeb7c0fa3e1d71c4c3dd48b709cb75a99831f85
fetched_at: '2026-06-29T00:09:59.955402+00:00'
page_id: '452718463'
product: rm
source: tdn-rm
title: Conversão de Perfis (Delphi x .NET)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718463
version: 3
---

falseATENÇÃO:

A partir da release **12.1.2606**, esta rotina foi descontinuada, por não ser mais necessária no produto.

O **Conversor de Perfis (Delphi x .NET)** tinha como objetivo migrar os perfis configurados em Delphi para o formato .NET dos processos de **RAIS**, **DIRF**, **Folha Analítica**, **Lançamentos Financeiros** e **Geração de Encargos**.

Para executar a conversão, o usuário acessava Configurações | Conversão de Perfis (Delphi x .NET), selecionava o processo e os perfis desejados e, em seguida, clicava em **Executar**.

Ao final da conversão, um novo perfil era criado com o sufixo **\_convertido** no nome. Os perfis convertidos eram armazenados na tabela **PPARAMRELAT**, com **TIPORELAT = 501** e **IDRELAT = 1**.

> **Observação**
>
> Apenas as informações existentes no perfil Delphi eram migradas. Campos que não eram armazenados nesse formato, como o **período de referência**, não eram considerados durante a conversão.
