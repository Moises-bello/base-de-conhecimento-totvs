---
content_hash: a276f2e1c6ebdabb07c0ef5486bfec88b4e0bf06a6b84b3b7f102044503951d1
fetched_at: '2026-07-02T19:24:26.703602+00:00'
page_id: '6064410'
product: protheus
source: tdn-tec
title: ADS_ERR.DBF Como fazer para definir o tamanho máximo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=6064410
version: 3
---

BLOCK

ADS\_ERR.DBF Como fazer para definir o tamanho máximo

## ADS\_ERR.DBF: Como fazer para definir o tamanho máximo

### Procedimento

1. Localize e edite, no diretório de instalação do TOTVS | Application Server, o arquivo **adslocal.log.**
2. Altere o valor da chave **ERROR\_LOG\_MAX**.  
      
    ERROR\_LOG\_MAX - Tamanho máximo do arquivo ADS\_ERR.DBF.  
    Padrão = 1000 KBytes  
    Valor mínimo: 1 KByte  
    Valor máximo: Não há limite  
      
    **Exemplo** ;Definir tamanho máximo de 3 MB  
    ERROR\_LOG\_MAX=3000

Esta chave define o tamanho máximo do arquivo ADS\_ERR.DBF.

Quando esse tamanho é atingido, os primeiros 1/3 dos registros, do arquivo, são marcados para exclusão e um 'PACK' é realizado automaticamente. As novas entradas são inseridas no final do arquivo.
