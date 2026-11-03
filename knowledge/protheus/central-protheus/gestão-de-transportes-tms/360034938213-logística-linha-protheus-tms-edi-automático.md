---
article_id: 360034938213
category: Gestão de Transportes (TMS)
content_hash: 80767f14ff8517c460ada1d9b5f4dbd6243c5919740824476ecd16a72afb59c6
fetched_at: '2026-06-28T22:45:27.652347+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - EDI Automático
type: support-article
updated_at: '2023-08-28T11:45:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034938213-Log%C3%ADstica-Linha-Protheus-TMS-EDI-Autom%C3%A1tico
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17081328756503)** Tempo aproximado para leitura: **00:01:20 min****Dúvida**Quais os procedimentos para configurar o **EDI - *Electronic Data Interchange Automático***?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Implementada melhoria no módulo **Gestão de Transportes - SIGATMS** com ajustes na rotina **EDI Nota Fiscal - TMSAE55** e a criação da rotina **Lote EDI - TMSAE56**, com o objetivo de atualizar as funcionalidades da rotina **EDI Automático - TMSAE75**.   
  
Seguem abaixo, os ajustes realizados no Sistema:

* Ajuste na rotina **EDI Nota Fiscal - TMSAE55** para permitir a inclusão demais de um produto por nota fiscal, facilitando o processo de inclusão de nota fiscal. O vínculo com tipos de veículos agora é realizado na mesma tela, não sendo necessário acessar o menu **Ações Relacionadas**;
* Criação da rotina **Lote EDI - TMSAE56** que permite efetuar o cadastro do valor de frete fechado para uma determinada quantidade de notas fiscais de clientes, denominado de **Lote EDI**. Esta rotina substitui a opção **Composição do frete**, que se encontrava dentro da rotina **EDI Nota Fiscal - TMSAE55**.

**Anexo**Anexo boletim técnico explicando os procedimentos para utilizar o processo de **EDI Automático**.
