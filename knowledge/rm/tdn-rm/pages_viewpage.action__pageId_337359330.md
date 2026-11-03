---
content_hash: e9a051e5c9f446b550c53da79622324b9e2b9c4d46a4571beed169f771f47ebf
fetched_at: '2026-06-29T00:08:51.675922+00:00'
page_id: '337359330'
product: rm
source: tdn-rm
title: Como habilitar os logs de comunicação TSS?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337359330
version: 10
---

Para gerar os Logs de comunicação do TSS é necessário realizar as seguintes parametrizações :

**1)** No servidor do TSS acesse o diretório de instalação (EX: C:\totvssped\bin\appserver)

**2)** Ative no arquivo appserver.ini os parâmetros XMLSAVEALL=1 na sessão [JOB\_WS] e SPED\_SAVEWSDL=1 na sessão [SPED]. Reinicie o serviço do TSS.

**3)** Verifique se no diretório wslogxml e system do TSS tem arquivos XML´s criados. Em caso afirmativo, exclua **somente os arquivos XML** (extensões SRV e SND) e reinicie o serviço.

**4)** Com o debug ativado, simule a inconsistência e envie para equipe de suporte todos os arquivos **xmls** (extensões SND e RCV ) gerados nos diretórios **wslogxml** e **system**junto como arquivo **console.log** do TSS e o arquivo **appserver.ini** do TSS.

**IMPORTANTE!**   
Após fazer a simulação, altere novamente o arquivo **appserver.ini**, e volte os parâmetros para  XMLSAVEALL=0 e  SPED\_SAVEWSDL=0. Reinicie o serviço do TSS.
