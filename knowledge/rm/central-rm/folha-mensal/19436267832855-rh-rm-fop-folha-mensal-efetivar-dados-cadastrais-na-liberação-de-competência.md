---
article_id: 19436267832855
category: Folha Mensal
content_hash: 02c535715870953fc154566638bbcabd99a0fdf6054d2c548790716a2a27bdb6
fetched_at: '2026-06-28T22:46:58.176215+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Mensal: Efetivar Dados Cadastrais na Liberação de Competência '
type: support-article
updated_at: '2025-02-12T18:07:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19436267832855-RH-RM-FOP-Folha-Mensal-Efetivar-Dados-Cadastrais-na-Libera%C3%A7%C3%A3o-de-Compet%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19436332195991) Tempo aproximado para leitura: **00:01:05 min****Dúvida**Como realizar a efetivação dos dados cadastrais no processo de liberação de competência?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

* 12.1.2310.120
* e Superiores.

**Solução**A efetivação dos dados cadastrais será realizado pelo seguinte caminho: **Folha Mensal | Liberação de Competência:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19436277485079)**

Neste caminho, foi disponibilizado o parâmetro "**Efetivar Dados Cadastrais**", que ficará marcado como default, para que o usuário não esqueça de realizar a efetivação.

![](https://tdn.totvs.com/download/attachments/687158765/image-2023-11-9_16-28-53.png?version=1&modificationDate=1699558133413&api=v2&effects=border-simple,shadow-kn)

Quando o parâmetro estiver marcado, o sistema irá:

* Atualizar os dados cadastrais (PFUNC);
* Criar o registro nos anexos dos históricos (Salarial, Seção, Função)
* Limpar os dados do anexo "Histórico Dados Cadastrais Futuro".

Quando o parâmetro estiver desmarcado, o sistema irá apresentar a mensagem de alerta abaixo:

![](https://tdn.totvs.com/download/attachments/687158765/image2022-7-6_9-1-48.png?version=1&modificationDate=1657108911287&api=v2&effects=border-simple,shadow-kn)

**Saiba Mais:**

[Histórico Dados Cadastrais Futuro](https://tdn.totvs.com/pages/releaseview.action?pageId=687158765#1-6)
