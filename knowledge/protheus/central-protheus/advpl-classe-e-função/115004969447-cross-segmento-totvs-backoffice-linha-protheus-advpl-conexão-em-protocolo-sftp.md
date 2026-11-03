---
article_id: 115004969447
category: ADVPL - Classe e Função
content_hash: 528e7b22bb3be647a14645899486a7f5597385af4772448051bd210303408832
fetched_at: '2026-06-28T22:40:15.636057+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Conexão em protocolo
  SFTP
type: support-article
updated_at: '2023-11-10T14:20:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004969447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Conex%C3%A3o-em-protocolo-SFTP
---

**Dúvida**É possível realizar uma conexão por meio dos protocolos SFTP?  
  
**Ambiente**Protheus – ADVPL – A partir da versão 12.1.27  
  
**Solução**Sim, atualmente é possível realizar transferências de arquivos utilizando o protocolo  **SFTP**( SSH). através das funções:

* [SFTPDirLs](https://tdn.totvs.com/display/tec/SFTPDirLs)
* [SFTPDwld1](https://tdn.totvs.com/display/tec/SFTPDwld1)
* [SFTPDwld2](https://tdn.totvs.com/display/tec/SFTPDwld2)
* [SFTPUpld1](https://tdn.totvs.com/display/tec/SFTPUpld1)
* [SFTPUpld2](https://tdn.totvs.com/display/tec/SFTPUpld2)

**Nota.:**

* Atualmente não é possível comunicação através do Protocolo **FTPS** (SSL/TLS).
* Para comunicação através do protocolo **FTP**, utilizar a classe **TFtpClient**.

**Saiba mais**[Interface SFTP](https://tdn.totvs.com/display/tec/Interface+SFTP)  
[TFtpClient](https://tdn.totvs.com/display/tec/Classe+TFtpClient)
