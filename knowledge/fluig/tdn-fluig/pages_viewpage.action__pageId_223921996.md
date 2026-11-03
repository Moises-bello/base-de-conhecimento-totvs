---
content_hash: acf3c60419fdf211c53a1dd66c52790de35cf8e740cc3dfa1a8058d1e3849e01
fetched_at: '2026-06-28T21:35:19.825803+00:00'
page_id: '223921996'
product: fluig
source: tdn-fluig
title: ARQ - Por que após renomear artefatos da pasta apps ocorre erros em alguns
  recursos da plataforma?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223921996
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Alguns artefatos da pasta *apps*, localizado em [diretório\_instalação]/appserver/apps, foram estava desatualizados, portanto novos artefatos atualizados foram incluídos, sendo que os antigos foram mantidos como backup nesta mesma pasta, porém foram renomeados. Após este procedimento, alguns recursos do sistema não funcionam mais. O devo fazer para que os recursos voltem a funcionar?

# Causa

Isto ocorre porque o servidor tentará realizar o *deploy* de qualquer arquivo '.war' ou '.ear' que estiver na pasta *apps*, portanto artefatos duplicados ou renomeados podem causar mal funcionamento do sistema.

# Solução

1. Parar os serviços do fluig;
2. Remover os artefatos antigos da pasta apps. Caso queira manter um backup dos artefatos, copie-os para outra pasta, fora deste diretório.
3. Iniciar os serviços do fluig na ordem correta.
