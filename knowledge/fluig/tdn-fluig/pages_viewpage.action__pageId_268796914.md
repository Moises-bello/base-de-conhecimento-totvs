---
content_hash: d5efa980a3b0245aaf29c32b2ba066420136a8eabde17c93824e840bfe28941d
fetched_at: '2026-06-28T21:35:24.035911+00:00'
page_id: '268796914'
product: fluig
source: tdn-fluig
title: ECM - Por que documentos com tabelas e imagens perdem a formatação com cópia
  controlada?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268796914
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto**: TOTVS Fluig Plataforma

# Ocorrência

Ao fazer a impressão de cópia controlada de um documento as tabelas e imagens que ele possui ficam desconfiguradas. Durante a visualização elas aparecem normalmente.

**Figura 1 - Documento desconfigurado na impressão de cópia controlada**

# Causa

A plataforma utiliza por padrão OpenOffice como ferramenta para a impressão de cópia controlada. Ele já está na instalação do produto padrão.   
  
O OpenOffice não é totalmente compatível com os documentos Microsoft Office, portanto é possível que alguns componentes ou formatação do documento não sejam exibidas corretamente no próprio OpenOffice e na impressão de cópia controlada.   
  
Para confirmar isso acesse o diretório **[diretório\_instalação\_plataforma]\OpenOffice\program.**Se o problema de formatação acontece com um arquivo **.DOC** ou **.DOCX**, execute o aplicativo **swriter.exe**. Se ocorre com um **.XLS** ou **.XLSX** execute o aplicativo **scalc.exe.**

Abra o documento com problema no OpenOffice e verifique como fica a formatação. Se ficar desconfigurada isso significa que o OpenOffice é que não está conseguindo manter o original e consequentemente a impressão também ficará assim.

**Figura 2 - Aplicativos do OpenOffice na instalação da plataforma**

**Figura 3 - Visualização do documento no OpenOffice**

**Figura 4 - Visualização do documento no Microsoft Office**

# Solução

A impressão pode feita ser utilizando o Microsoft Office no lugar do OpenOffice. Basta que você instale no servidor da plataforma o pacote do Microsoft Office e execute toda a configuração descrita na documentação .

A plataforma passará a utilizar o MS Office assim que ele for instalado no servidor. Se algum dia ele for desinstalado, a plataforma voltará a utilizar o OpenOffice.

Importante

Confira a  para saber quais versões do MS Office são homologadas.
