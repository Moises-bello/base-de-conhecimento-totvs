---
article_id: 1500006016782
category: Financeiro - Contabilização
content_hash: c315abf7993c7896d958db03f311c42e9241882b6b0daa25244670342bfb47e4
fetched_at: '2026-06-28T22:38:05.361316+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBAFIN - Registro
  não possui correspondência com Contas a Receber ou Pagar
type: support-article
updated_at: '2022-08-17T23:58:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006016782-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBAFIN-Registro-n%C3%A3o-possui-correspond%C3%AAncia-com-Contas-a-Receber-ou-Pagar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**  
No módulo Financeiro, ao tentar realizar a contabilização (**CTBAFIN**) é apresentada a msg (**Foi encontrado um registro no arquivo SE5 que não possui correspondência nos arquivos de Contas a Receber ou Pagar. Você pode parar agora a contabilização ou continuar assim mesmo.**)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CTBAFIN - Todas as versões  
  
**Causa**É por padrão aparecer esta mensagem na contabilização, existem casos que são integrações de outros módulos e casos que são tramitados diretamente no financeiro e que não gera registro nas tabelas SE1 e SE2. Não se trata de erro, somente um alerta.  
  
![tela.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007911062/tela.JPG)  
  
**Solução**Caso não queira que a mensagem ocorra, altere o parâmetro **MV\_FINLOG = .F.** (este parâmetro desabilita a mensagem de "**NÃO CORRESPONDENTE**" na SE5, no momento da contabilização).

**Saiba mais:**  
[Parâmetro MV\_FINLOG](https://tdn.totvs.com/pages/releaseview.action?pageId=6070492)
