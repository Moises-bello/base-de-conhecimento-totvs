---
content_hash: 31484c1368b9894f207a3159b3545028c70a7164c00b805587a686c2ab9cdf06
fetched_at: '2026-06-29T00:11:31.430816+00:00'
page_id: '737568387'
product: rm
source: tdn-rm
title: Liberação da prescrição/itens (Prescrições avulsas)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=737568387
version: 21
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Funcionalidade**
3. **Processo de liberação**
4. **Exemplo de utilização**

Liberação da prescrição/itens (Prescrições avulsas)Visão Geral

## **01.** **VISÃO GERAL**

A liberação da prescrição e seus respectivos itens tem como objetivo efetivar os itens que estão em rascunho como parte das prescrições do paciente.

Funcionalidade

## **2. FUNCIONALIDADE**

1. A liberação da prescrição/itens pode ser feita nas seguintes situações:  
     
   * A prescrição ainda está em rascunho. Nessa situação, a prescrição estar em rascunho significa que será a primeira liberação dessa prescrição, então além dos itens que compõem essa prescrição passarem pelo **processo de liberação**, também será definido a **data de validade** dessa prescrição (que será de 24 horas a partir dessa primeira liberação, ou configurado na Unidade de Atendimento), e essa prescrição passará a ficar visível na listagem de **[prescrições anteriores](https://tdn.totvs.com/pages/viewpage.action?pageId=737568563)** para outros profissionais.
   * A prescrição já havia sido liberada. Nessa situação, os itens dessa prescrição que ainda estão em rascunho passarão pelo **processo de liberação.**
2. Não será possível liberar a prescrição/itens nos seguintes casos:  
     
   * A prescrição não for de responsabilidade do profissional realizando a liberação.
   * A prescrição estiver vencida.
Processo de liberação

## **03. PROCESSO DE LIBERAÇÃO**

* Os itens serão efetivados na prescrição do paciente como itens liberados.
* Os itens liberados serão enviados ao **Sistema de Hospitais e Clínicas** para serem processados. Por exemplo, os medicamentos liberados serão solicitados no **Painel de Dispensação, não passando pelo processo de aprazamento/checagem.**
* A liberação realizada ficará disponível na listagem de **Prescrições Anteriores** dessa prescrição.
* Será gerado o impresso da prescrição com os itens que foram liberados.
Exemplo de utilização

## **04. EXEMPLO DE UTILIZAÇÃO**

1. Liberação de uma prescrição ainda em rascunho**:**Será definido a data de validade da prescrição a partir dessa liberação, e a liberação também ficará disponível para outros profissionais nas **[Prescrições Anteriores](https://tdn.totvs.com/pages/viewpage.action?pageId=737568563)**.
2. Liberação de uma prescrição que já havia sido liberada anteriormente. O processo é similar a liberação de uma prescrição que estava em rascunho, porém não será feito a definição da validade da prescrição, e dessa forma, a validade dos novos itens será de acordo com a vigência da prescrição em que eles foram inseridos.
3. Após a liberação da prescrição (seja ela rascunho ou vigente), também será gerado o impresso da liberação da prescrição.  
     
     
     
   **IMPORTANTE:**  
   * Esse impresso contém apenas os itens que foram liberados naquele momento, mas caso haja a necessidade de visualizar a prescrição completa, pode ser feito através das **[Prescrições Anteriores](https://tdn.totvs.com/pages/viewpage.action?pageId=737568563)**.
   * Caso o sistema esteja parametrizado para utilizar assinatura digital, poderá ser solicitado a assinatura antes de concluir o processo de liberação e geração do impresso da prescrição liberada.
