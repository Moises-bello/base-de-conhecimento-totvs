---
article_id: 360021716291
category: Ativo Fixo - Procedures
content_hash: cb3e1a3501cfc54187e47e0442f51a1a7d68eb7608aa9ea3221e8f6867dd6452
fetched_at: '2026-06-28T22:41:40.465374+00:00'
product: protheus
section_id: 1500001536541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Utilização de procedure
  no cálculo de depreciação
type: support-article
updated_at: '2024-10-22T18:37:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021716291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Utiliza%C3%A7%C3%A3o-de-procedure-no-c%C3%A1lculo-de-deprecia%C3%A7%C3%A3o
---

**Dúvida**Porque o cálculo de depreciação para alguns usuários e/ou em alguns momentos distintos, não  utiliza procedure?

**Ambiente**Protheus – Ativo Fixo – Disponível em todas as versões do sistema.  
  
**Solução**Para que o cálculo de depreciação seja executado via procedure, é necessário garantir que a procedure 11 - Cálculo depreciação de ativos - esteja compatível com as atualizações aplicadas no sistema. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27253937595159)

Dessa forma o cálculo de depreciação utilizará a procedure para execução desde que a mesma esteja instalada e atualizada (**P12\_11.ZPS**), fazendo com que tenha um ganho significativo de performance.

Nesse formato a contabilização da depreciação deve ocorrer de forma Offline através da rotina **CTBAATF**.

**Central de Atualizações (Instalador das procedure):**  
[Central de Atualizações - Release Notes](https://tdn.totvs.com/pages/releaseview.action?pageId=532651679)  
  
**Acumulado Ativo(Atualização da procedure):**  
[Acumulado Módulo - SIGAATF](https://tdn.totvs.com/pages/releaseview.action?pageId=382557083)  
  
**LIB:**  
[**Pacotes LIB**](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/search/searchAll)

**Instalação Procedures:**

[Instalando/Atualizando pacotes de procedures](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes#StoredProceduresNovogerenciadordepacotes-instalando_pacotes)

Saiba Mais:  
[Stored Procedures - Novo gerenciador de pacotes](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes#StoredProceduresNovogerenciadordepacotes-instalando_pacotes)
