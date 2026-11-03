---
content_hash: 09e59d9a403cfe3222bd932cb2db7ad4ae3a19d611b898b821467ca76fb5ab2b
fetched_at: '2026-06-28T21:35:23.816364+00:00'
page_id: '265783394'
product: fluig
source: tdn-fluig
title: DES - WebService envia String para retornar resultado
type: documentation
url: https://tdn.totvs.com/display/fluig/DES+-+WebService+envia+String+para+retornar+resultado
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**TOTVS Fluig Plataforma

**Tipo de API:** Webservice

# Ocorrência

Método de webservice envia uma String que é preenchida e retorna do serviço, porém esse parâmetro, na criação do Web Service via Axis, espera um StringHolder ao invés de uma String comum.

# Causa

O Axis utiliza o StringHolder pra fazer a transmissão de valor na referência sem retorno.

# Solução

Enviar como parâmetro a String desejada encapsulada no objeto javax.xml.rpc.holders.StringHolder.

A API Axis está depreciada para uso.
