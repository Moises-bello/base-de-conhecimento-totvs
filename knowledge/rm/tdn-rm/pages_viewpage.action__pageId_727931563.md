---
content_hash: d42ed6560475e9fde8019a196459ef66038183f334c7ebe9feee4db9e423cfd7
fetched_at: '2026-06-29T00:11:27.591519+00:00'
page_id: '727931563'
product: rm
source: tdn-rm
title: Guia de Migração angular-erp-integration para Common-Api
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=727931563
version: 1
---

# Guia de Migração

Este guia o ajudará nos passos necessários para alterar a implementação da biblioteca *angular-erp-integration* para a nova **[@totvs/common-api](https://npm.totvs.io/-/web/detail/@totvs/common-api)**.

## Passos para migração

1. **Altere o registro do modulo:**De **AEIModule** para **TCommonApiModule**
2. **Faça as alterações das classes conforme apresentado a seguir:**

| Anteriormente | Substituir por |
| --- | --- |
| AEIAuthService | **TErpAuthIntegrationService** |
| AEIAppConfigService | **TErpConfigAcessorService** |
| AEIAppContextService | **TErpContextAcessorService** |
| AEIAppCustomObjectsService | **TErpCustomObjectsAcessorService** |
