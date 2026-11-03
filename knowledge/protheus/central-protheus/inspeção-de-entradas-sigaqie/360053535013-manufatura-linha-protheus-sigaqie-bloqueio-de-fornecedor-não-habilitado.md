---
article_id: 360053535013
category: Inspeção de Entradas (SIGAQIE)
content_hash: 2c02706a262c58ff9373d0fec62b27fabc3a198660439330f74d47c32641f2a6
fetched_at: '2026-06-28T22:42:26.880796+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Bloqueio de fornecedor Não Habilitado
type: support-article
updated_at: '2024-02-02T17:35:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053535013-Manufatura-Linha-Protheus-SIGAQIE-Bloqueio-de-fornecedor-N%C3%A3o-Habilitado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20650926165527) Tempo aproximado para leitura: **00:00:48 min**  
**Dúvida**Como realizar o **bloqueio de fornecedor Não habilitado** no **SIGAQIE - Inspeção de Entradas**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**O **bloqueio de fornecedor não habilitado** ocorre se o parâmetro **MV\_QBLQFOR - Habilita o bloqueio do Produto x Fornecedor que estiver com status Não Habilitado no QIE (S= Habilita bloqueio, N= Não habilita Bloqueio)** quando habilitado, ou seja, com conteúdo igual a **S - Habilita bloqueio**, irá realizar o bloqueio de entradas de fornecedor não habilitado no módulo **SIGAQIE - Inspeção de Entradas**. Este bloqueio é realizado quando a situação do fornecedor informada no campo **Situação - A5\_SITU** da rotina **MATA061 - Produto x Fornecedor** estiver como **D - Não Habilitado**, relacionado a uma categoria igual à **4 - Não Recebe**, o que indica que este produto foi bloqueado devido o fornecedor estar bloqueado pela qualidade.  
Se o conteúdo deste parâmetro estiver configurado como **N - Não**, indica que não será realizado o bloqueio de entradas do fornecedor, e que o fornecedor será validado.
