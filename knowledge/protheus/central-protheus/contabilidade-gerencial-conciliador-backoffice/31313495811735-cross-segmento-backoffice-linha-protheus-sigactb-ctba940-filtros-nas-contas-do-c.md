---
article_id: 31313495811735
category: Contabilidade Gerencial - Conciliador BackOffice
content_hash: 0c337ea106196ffff04b9544d2e3e13b04b545f3096d10a8b3c41c0451df9c86
fetched_at: '2026-06-28T22:40:30.977403+00:00'
product: protheus
section_id: 31314114896791
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA940 - Filtros nas
  contas do conciliador não funcionam
type: support-article
updated_at: '2025-04-10T18:15:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31313495811735-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Filtros-nas-contas-do-conciliador-n%C3%A3o-funcionam
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31313472643095) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Quando aplicamos um filtro nas contas contabeis da rotina do conciliador, não retorna os resultados filtrados de forma correta.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contablidade Gerencial - a partir da release 12.1.2210  
  
**Solução**

O conciliador opera com uma **lógica de OU** nos filtros aplicados, diferentemente dos filtros contábeis tradicionais, que costumam seguir a lógica de E.  
   
Quando o usuário aplica um filtro, o sistema trará resultados que atendam a pelo menos uma das condições inseridas.

✅ Exemplo prático:  
Se o usuário filtrar pelo Débito = **Conta X** e pelo Crédito = **Conta Y**, o sistema exibirá:

* Todos os lançamentos onde o Débito seja na **Conta X**.
* Todos os lançamentos onde o Crédito seja na **Conta Y**.
* Mesmo que um lançamento não tenha ambos os critérios atendidos ao mesmo tempo, ele ainda será exibido **se atender um deles.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31313472644247)  
   
**Resultado:**  
Serão feitas validações das condições, e se uma ou mais retornarem verdadeiras, o sistema apresentará o resultado em tela:  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31313495796503)  
   
Atualmente, este é o conceito aplicável dos filtros inseridos.

**Saiba Mais**:

[CTBA940 - Configuração e Instalação](https://tdn.totvs.com.br/pages/releaseview.action?pageId=638741736)

[Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA940 - Conciliador BackOffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451317698583-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-BackOffice)
