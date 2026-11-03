---
article_id: 12119292981271
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: c29fb22890371d4b511a52ab9fe85809eb0e08a2bf0ab5eb0b9f172948b88af8
fetched_at: '2026-06-28T22:42:09.173140+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Error log
  type mismatch on compare on MENUDEF(FISA095.PRW) 22/12/2022 19:13:25 line : 182'
type: support-article
updated_at: '2023-02-02T13:15:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12119292981271-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Error-log-type-mismatch-on-compare-on-MENUDEF-FISA095-PRW-22-12-2022-19-13-25-line-182
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min****Ocorrência**

Ao gerar o relatório de usuários **CFGR510** '**Usuários**' via **Configurador** está apresentando *error.log*:

**type mismatch on compare  on MENUDEF(FISA095.PRW) 22/12/2022 19:13:25 line : 182**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**O erro ocorre no ambiente porque ainda não está aplicado o pacote que ajustou o código fonte para que não ocorra *error.log* quando é chamado a rotina **FISA095 'Gnre\_Ws'** de outras funções.  
  
**Solução**Para correção do erro é preciso aplicar o pacote de correção abaixo:

A *Release* Oficial foi expedida e publicada na Central de *Downloads*.  
O pacote pode ser acessado no endereço:

12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1094734>; 12.1.27:<https://suporte.totvs.com/portal/p/10098/download?e=1094735>; 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1094736>;

Para acessar a documentação da solicitação acesse o *link*:

<https://tdn.totvs.com/pages/viewpage.action?pageId=734390057>
