---
content_hash: 889a6b788acd42e6c72fb353599b292d052088fdd1706941111106406f367a62
fetched_at: '2026-07-02T19:24:26.700266+00:00'
page_id: '6064409'
product: protheus
source: tdn-tec
title: ADS_ERR.DBF Como fazer para definir diretório de criação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=6064409
version: 3
---

BLOCK

ADS\_ERR.DBF Como fazer para definir diretório de criação

## ADS\_ERR.DBF: Como fazer para definir diretório de criação

### Para ADS - *Advantage Local Server* (ADS Local)

1. Localize e edite, no diretório de instalação do TOTVS | Application Server, o arquivo **adslocal.log.**
2. Altere o valor da chave **ERROR\_ASSERT\_LOGS**.  
      
    ERROR\_ASSERT\_LOGS - Diretório do arquivo de log (ADS\_ERR.DBF) e de "assert" (ASSERT.LOG).  
    Padrão = raiz do driver C:\  
    Valor mínimo: 1 KByte  
    Valor máximo: Não há limite  
      
    **Exemplo** ;Definir tamanho máximo de 3 MB  
    ERROR\_ASSERT\_LOGS= D:\ERP\logads

### 

### Para ADS - *Advantage Database Server* (ADS Server)

1. Execute o **ADS Configuration Utility**.
2. Acesse **Configuration** + **File Locations**.
3. Altere o valor de **Error and Assert Log Path**.
