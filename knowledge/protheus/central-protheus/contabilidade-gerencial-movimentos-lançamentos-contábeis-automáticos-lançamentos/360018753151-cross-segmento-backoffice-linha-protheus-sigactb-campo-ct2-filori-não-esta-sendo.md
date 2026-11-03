---
article_id: 360018753151
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 996b6e876c4ad919bf206354165d631791282646fc88eef82e9e590e97357a55
fetched_at: '2026-06-28T22:40:32.416277+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - campo CT2_FILORI não
  esta sendo preenchido.
type: support-article
updated_at: '2025-08-27T11:24:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018753151-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-campo-CT2-FILORI-n%C3%A3o-esta-sendo-preenchido
---

**Ocorrência**

Ao realizar contabilizando  onde pergunta " Aglutina =Sim " sistema gerar erro log abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360014212432)

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus  – contabilidade gerencial– A partir da versão 11.80 **Causa**

* O campo CT2\_FILORI não esta sendo preenchido pelo sistema , com isso caso possua lançamento  que se diferem com o preenchimento do campo o sistema irá gerar chave duplicada

**Solução**

* Caso este campo esteja marcado como **Usado** no **Configurador (SIGACFG)**, virá em branco, sendo necessário o preenchimento manual.

Veja mais :

[CTB0022\_Campo\_Filial\_de\_Origem\_(CT2\_FILORI)](http://tdn.totvs.com/pages/releaseview.action?pageId=233753442)

Obs: caso esse campo não seja preenchido o sistema não irá realizar a limpeza de flag durante a exclusão do lançamento contábil

<https://tdn.totvs.com/pages/releaseview.action?pageId=842697736>
