---
content_hash: f8a0ff8a9cd5b602c6f33087a39711fe8c52ae1e4713f4f24a126a3e7b5ccff2
fetched_at: '2026-06-28T21:35:22.997831+00:00'
page_id: '243631521'
product: fluig
source: tdn-fluig
title: ARQ - Por que ocorre a mensagem de erro FileAlreadyExistsException ao iniciar
  a plataforma?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243631521
version: 6
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** A partir da 1.5.9

# Ocorrência

Por que ocorre a mensagem de erro FileAlreadyExistsException ao iniciar a plataforma?

javaEclipseserver.logtruetrue R:\TOTVS\FLUIG\PRODUCAO\jboss\apps\social-ecm-totlets-widgets-communities-all.war
ERROR [stderr] (Thread-77) at sun.nio.fs.WindowsException.translateToIOException(WindowsException.java:81)
ERROR [stderr] (Thread-77) at sun.nio.fs.WindowsException.rethrowAsIOException(WindowsException.java:97)
ERROR [stderr] (Thread-77) at sun.nio.fs.WindowsFileCopy.move(WindowsFileCopy.java:387)
ERROR [stderr] (Thread-77) at sun.nio.fs.WindowsFileSystemProvider.move(WindowsFileSystemProvider.java:287)
ERROR [stderr] (Thread-77) at java.nio.file.Files.move(Files.java:1347)
ERROR [stderr] (Thread-77) at com.sun.nio.zipfs.ZipFileSystem.sync(ZipFileSystem.java:1297)
ERROR [stderr] (Thread-77) at com.sun.nio.zipfs.ZipFileSystem.close(ZipFileSystem.java:277)
ERROR [stderr] (Thread-77) at com.totvs.technology.wcm.WCMService.processSimpleDeploys(WCMService.java:884)
ERROR [stderr] (Thread-77) at com.totvs.technology.wcm.WCMService.doStartUp(WCMService.java:429)
ERROR [stderr] (Thread-77) at com.totvs.technology.wcm.WCMService.access$300(WCMService.java:88)
ERROR [stderr] (Thread-77) at com.totvs.technology.wcm.WCMService$StandAloneScanner.run(WCMService.java:934)
ERROR [stderr] (Thread-77) at java.lang.Thread.run(Thread.java:745)]]>

# Solução

Durante o processo de *deploy* dos artefatos na inicialização da plataforma, vários arquivos temporários são criados e removidos na pasta [diretório\_instalação]\jboss\apps.

Em algumas situações, no entanto, pode acontecer de o antivírus bloquear a remoção destes arquivos temporários, gerando duplicidade.

É necessário desabilitar o módulo de varredura de arquivos ou desligar o antivírus completamente.

Atenção!

Em atualizações 1.6 e superiores, o diretório em que ocorre a criação e remoção de arquivos temporários durante o processo de *deploy* dos artefatos é [diretório\_instalação]\appserver\apps.

# Observações

Até o momento, este problema foi observado apenas em servidores com o antivírus Intel Security-McAfee.
