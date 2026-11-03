---
article_id: 10930457324439
category: Comércio Exterior - Easy Import Control - Siscomex
content_hash: 41bbb442af147631f633d2bc9b5b5cf3c534e690cfded24d2040962c1b33a5ae
fetched_at: '2026-06-28T22:39:45.350416+00:00'
product: protheus
section_id: 1500001538441
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Itens DUIMP
type: support-article
updated_at: '2022-12-13T21:52:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10930457324439-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Itens-DUIMP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como efetuar a vinculação de LPCO e Itens DUIMP?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control*- a partir da versão 12.1.27  
  
**Solução**Neste novo processo é possível efetuar a vinculação de **LPCO** (Licenças, Permissões, Certificados e Outros) aos itens do embarque; Utilizando quebra por Lote ou **LPCO** de acordo com o resultado da consulta de todos os formulários de **LPCO**, associados aos itens das *invoices* do processo do Tipo **DUIMP** (Declaração Única de Importação) pela rotina **Form LPCO** **x** **NCM** (para processos de importação), agrupados por formulário.  
São objetivos da rotina **Itens DUIMP**:

* Vincular um ou mais **LPCO's** ao itens do embarque de Importação.
* Possibilitar quebrar os itens por **LPCO** e/ou Lote.
* Possibilitar vincular tributação Federal e Estadual ao item.
* Efetuar controle de quebra, buscar reservas e **LPCO's** disponíveis.

**Exemplo de utilização**Na rotina de **Desembaraço** no browser da tela foi inserida a opção **"Itens DUIMP"** disponível em **Outras Ações.****Itens DUIMP:**

1. Acesse o Menu Atualizações\Embarque ou Atualizações\Desembaraço
2. Em Outras Ações escolha a opção '**Itens DUIMP**'
3. Neste momento caso não existam Itens de *Invoices* informadas no processo, será mostrada a mensagem alertando para a necessidade de cadastrar Itens de *Invoice;* Será também informado que para utilizar a rotina de "**Itens DUIMP**" o Processo deve ser do tipo '**DUIMP**'.
4. Atendendo aos critérios, será aberta a tela de '**Capa Declaração de Importação - Itens DUIMP**'. (**Obs**.: a primeira vez ao acessar a rotina será feita a carga inicial.)

**Importante**Para a utilização dessa funcionalidade é necessário que o embarque e/ou desembaraço tenha uma ou mais *Invoices* vinculadas ao processo, e que na aba "**DI**" o campo **"Tipo de Registro"** esteja igual a **"DUIMP".**

**Exemplo do procedimento**

**Saiba mais**[Itens DUIMP](https://tdn.totvs.com/display/PROT/Itens+DUIMP)   
[Procedimento para Implantação DUIMP](https://tdn.totvs.com/pages/viewpage.action?pageId=657762135)
