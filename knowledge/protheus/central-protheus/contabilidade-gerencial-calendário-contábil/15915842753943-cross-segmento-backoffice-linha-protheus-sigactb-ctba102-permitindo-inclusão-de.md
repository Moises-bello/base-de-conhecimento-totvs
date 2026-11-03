---
article_id: 15915842753943
category: Contabilidade Gerencial - Calendário Contábil
content_hash: 523b09e52c81dd46d283a08775df74af5103a3263d16e92e6adb2c91d46c6b49
fetched_at: '2026-06-28T22:41:03.411639+00:00'
product: protheus
section_id: 1500001537301
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Permitindo
  inclusão de lançamentos em períodos que não possuem calendário cadastrados.
type: support-article
updated_at: '2026-01-15T20:46:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15915842753943-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Permitindo-inclus%C3%A3o-de-lan%C3%A7amentos-em-per%C3%ADodos-que-n%C3%A3o-possuem-calend%C3%A1rio-cadastrados
---

**Ocorrência**

Sistema Permitindo Inclusão/Alteração de lançamentos em períodos que não possuem calendário cadastrado.

**Ambiente**

Microsiga Protheus – Contábil – A partir da versão 12.1.2210

**Solução:**

Para que o calendário seja validado corretamente é necessário que esteja atualizado com o pacote atualizado do módulo CTB.

Segue pacotes para atualização.

<https://tdn.totvs.com/pages/releaseview.action?pageId=334342777>

Além da atualização é necessário verificar os passos abaixo:

**1º Verifique o Status do calendário e amarração a moeda**

* [O intervalo de datas informadas não poderá ser processado.](https://centraldeatendimento.totvs.com/hc/pt-BR/articles/360020540691-MP-SIGACTB-CTBA102-O-intervalo-de-datas-informadas-n%C3%A3o-poder%C3%A1-ser-processado-?source=search)
* [Como abrir período contábil bloqueado/fechado para movimentação?](https://centraldeatendimento.totvs.com/hc/pt-BR/articles/360006722952-MP-SIGACTB-CTBA010-Como-abrir-per%C3%ADodo-cont%C3%A1bil-bloqueado-fechado-para-movimenta%C3%A7%C3%A3o-?source=search)

Para o correto funcionamento se faz necessário que as tabelas abaixo estejam devidamente populadas e com o mesmo compartilhamento

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15915839493783)  
Para mais detalhes verifique :

<https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB>  
[Como alterar o compartilhamento de tabelas após bloqueio realizado a partir da LIB versão 20181015](https://centraldeatendimento.totvs.com/hc/pt-BR/articles/360026077191-MP-SIGACTB-Como-alterar-o-compartilhamento-de-tabelas-ap%C3%B3s-bloqueio-realizado-a-partir-da-LIB-vers%C3%A3o-20181015?source=search)

**2º verifique se possui os parâmetros MV\_CTFBLOQ e MV\_CTVBLOQ e se estão configurados corretamente conforme abaixo:**

**MV\_CTFBLOQ:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=867808442>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15915501333783)

**MV\_CTVBLOQ:**

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=536715163>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15915557007255)

Caso não estejam desta forma deveram configura-los que o sistema realize a validação de todas as rotinas ou das rotinas especificas conforme menciona as documentação referencias na evidencia acima.

**Obs**: Se após estes procedimentos os sistema permitir a inclusão de lançamentos em calendário com períodos bloqueados seguir a documentação abaixo:

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Permitindo inclusão de lançamentos mesmo com calendário bloqueado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14766971052951-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Permitindo-inclus%C3%A3o-de-lan%C3%A7amentos-mesmo-com-calend%C3%A1rio-bloqueado-)

**Saiba mais :**

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 Help: CTGDTCOMP : O STATUS DESTE PERÍODO NÃO PERMITE DIGITAÇÃO](https://centraldeatendimento.totvs.com/hc/pt-BR/articles/360053754813-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Help-CTGDTCOMP-O-STATUS-DESTE-PER%C3%8DODO-N%C3%83O-PERMITE-DIGITA%C3%87%C3%83O)

[MV\_CTFBLOQ - Funcoes Bloqueio Moeda Cal. Cambio CTB](https://tdn.totvs.com.br/pages/releaseview.action?pageId=6068567)

[MV\_CTVBLOQ Bloqueio de validações de Moeda, Calendário Contábil e Câmbio SIGACTB](https://tdn.totvs.com.br/pages/releaseview.action?pageId=536715163)
