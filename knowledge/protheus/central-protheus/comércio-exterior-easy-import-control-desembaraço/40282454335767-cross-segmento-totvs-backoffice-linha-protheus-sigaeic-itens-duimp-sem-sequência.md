---
article_id: 40282454335767
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 5a4597a8ba4bab1f1859b8aed7a54bf3d0770238ad9d538f97dacc89c5731000
fetched_at: '2026-06-28T22:39:51.271364+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Itens DUIMP
  sem sequência de registro informada
type: support-article
updated_at: '2026-06-11T11:08:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40282454335767-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Itens-DUIMP-sem-sequ%C3%AAncia-de-registro-informada
---

O erro ao gerar a Nota Fiscal de Entrada no Protheus ocorre porque o campo "Seq. DUIMP" não está preenchido para todos os itens no Desembaraço, exigido para rastreio individualizado pela DUIMP. Para resolver, acesse o módulo SIGAEIC, vá em Atualizações, Desembaraço, Outras Ações, Itens DUIMP, gere a sequência automaticamente e confirme para salvar. Depois, gere a Nota Fiscal normalmente.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40282454319767) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida:**  
Ao tentar gerar a Nota Fiscal de Entrada através da rotina de Recebimento de Importação (EICDI154), o sistema apresenta o alerta: "***A sequência de registro da DUIMP não foi informada para todos os itens do processo. Deseja revisar a sequência dos itens?***". Caso o usuário prossiga sem o ajuste, o sistema impede a geração com a mensagem de erro: "***Problema: É necessário informar o campo sequência DUIMP de todos os itens para gerar a nota fiscal***".  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40282454320663)   
  
**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEIC - Todas as Versões  
  
**Solução:**  
A mensagem ocorre porque o campo "**Seq. DUIMP** (**WV\_SEQDUIM**)" não está preenchido para um ou mais itens no Desembaraço (EICDI500). Como a DUIMP (Declaração Única de Importação) exige o rastreio individualizado dos itens conforme o registro no Portal Único Siscomex, o Protheus bloqueia a geração da Nota Fiscal para garantir a conformidade fiscal e a correta integração dos dados.  
  
**Passos:**  
1-) No Módulo "**SIGAEIC**", acesse "***Atualizações > Desembaraço > Outras Ações > Itens DUIMP***";

3-) O sistema abrirá a tela "***Declaração de Importação - itens DUIMP***";

4-) Clique em "**Outras Ações > Gerar Sequência Automaticamente**";

5-) Após o preenchimento, clique em "**Confirmar**" para salvar as alterações.

6-) Retorne à rotina de Recebimento de Importação e proceda com a geração da Nota Fiscal (Pre-Nota/Classificação).  
  
**Saiba mais:**  
[**Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Itens DUIMP**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10930457324439-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Itens-DUIMP)
