---
content_hash: 362803d5c890e6ba81a8fc0cf3da65f5ab8f0352f35e14b46281acf1cd180779
fetched_at: '2026-06-28T21:35:27.192925+00:00'
page_id: '501458323'
product: fluig
source: tdn-fluig
title: Identity | Política de retenção de backups
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=501458323
version: 16
---

# Falando de política de retenção de backups...

---

O banco de dados do Identity passa por rotinas diárias de *backup* para garantir a restauração dos dados em caso de inconsistência ou excepcional falha no ambiente ou de sistema. Esses arquivos de *backup* são armazenados por um determinado período e posteriormente excluídos.

Tanto no ambiente de produção quanto de homologação do Identity os *backups* do banco de dados são completos, não havendo a possibilidade de armazenamento ou restauração parcial da base.

## Backup de produção

---

As políticas de retenção de *backups* a seguir correspondem ao ambiente de produção do Identity (fluigidentity.com).

Um *backup* completo da base de dados de produção do Identity é executado a cada 4 horas e armazenado por 7 dias.

Além disso, um *backup* completo é gerado no 1º dia de cada mês e armazenado por 12 meses.

## Backup de homologação

---

As políticas de retenção de *backups* a seguir são aplicáveis ao ambiente de homologação do Identity (customerfi.com).

Um *backup* completo da base de dados de homologação do Identity é executado a cada 8 horas e armazenado por 3 dias.

Além disso, um *backup* completo é gerado no 1º dia de cada mês e armazenado por 3 meses.

]]>
