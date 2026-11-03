---
article_id: 4907877736855
category: Inspeção de Entradas (SIGAQIE)
content_hash: 5799dd6f623e48eeb1621dbc973a620b01db8a0583a98f1862d930a92ccba823
fetched_at: '2026-06-28T22:42:27.164255+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Relacionar um documento na especificação
type: support-article
updated_at: '2023-02-07T11:23:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4907877736855-Manufatura-Linha-Protheus-SIGAQIE-Relacionar-um-documento-na-especifica%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:40 min** **Dúvida**É possível relacionar um documento à inspeção de resultados?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**A única forma de um documento estar visível na rotina **QIEA215 - Cadastro de Resultados** é relacionar esta documento com a especificação do produto na rotina **QIEA010 - Especificação do Produto**, por meio do campo **Método**. Neste campo, deve ser selecionado um documento previamente cadastrado no módulo **SIGAQDO - Controle de Documentos**.  
Desta forma, ao realizar a inspeção do produto na rotina **QIEA215**, será possível consultar este documento pela opção **Outras Ações/Vis. Docto**.
