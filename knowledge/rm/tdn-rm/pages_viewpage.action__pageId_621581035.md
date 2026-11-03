---
content_hash: e8c8f11efbafc2b73f5e7d32f34db291e8e3231ace7f18993c984e3020c5c9cd
fetched_at: '2026-06-29T00:11:03.375338+00:00'
page_id: '621581035'
product: rm
source: tdn-rm
title: Atualização de versão ou release Portal RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=621581035
version: 2
---

Para realizar a **atualização do Portal RM**, tomando com exemplo que a versão atual é 12.1.19 e versão a ser atualizada é 12.1.21, siga uma das opções abaixo:

Importante

Esta documentação deve ser seguida após a atualização da biblioteca RM, no mesmo contexto para a versão 12.1.21.  
Para informações sobre a atualização da biblioteca RM siga os passos do link abaixo:

**Opção 1 - Utilizando instalador .MSI**

1. Verifique na documentação de portabilidade se o seu ambiente esta homologado para a instalação da nova versão ou release do Portal;  
   Para verificar a homologação do ambiente Portal RM acesse o link: <http://tdn.totvs.com/display/LRM/PORTABILIDADE>
2. Acesse o servidor onde esta instalado o Portal RM;
3. Acesse o diretório **UNIDADE:\totvs\CorporeRM**;
4. Caso tenho customizações, realize o backup das mesmas;
   1. Realize **backup** das **customizações** de seu portal;  
      **Importante**  
      Em nosso exemplo, temos customizações na página de login do Portal [Corpore.net](http://Corpore.net), então copiamos a pasta onde realizamos as alterações:
5. Acesse a **central de** **downloads**;
6. Realize o download do instalador TOTVSRMPortal.xxx.**MSI** (se necessário baixe o instalador do Patch também);
7. Acesse o **Painel de Controle** do Windows;
8. Abra o **Programas e Recursos** do Windows;
9. **Desinstale** o TOTVSRMPortal12.1.19;
10. **Instale** o TOTVSRMPortal12.1.21.MSI;
11. **Copie** as **customizações** que realizou backup (Passo 4), para as mesmas pastas na **nova instalação do Portal, substituindo os arquivos.**

**Opção 2- Utilizando o instalador .exe**

1. Verifique na documentação de portabilidade se o seu ambiente esta homologado para a instalação da nova versão ou release do Portal;  
   **Saiba mais**Para verificar a homologação do ambiente Portal RM acesse o link: <http://tdn.totvs.com/display/LRM/PORTABILIDADE>
2. Acesse o servidor onde esta instalado o Portal RM;
3. Acesse a central de **downloads**;
4. Realize o download do instalador TOTVSRMPortal.xxx.**EXE** (se necessário baixe o instalador do Patch também);
5. **Instale** o TOTVSRMPortal12.1.21.EXE;
6. Reinicie o serviço RM.Host.Service;
