---
article_id: 21481279394071
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: d1134e049d426f758492767e8df5e54540f7840c1c30e4f13c2a89c704cb5bd7
fetched_at: '2026-06-28T22:38:39.561581+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT –  Campos integrados
  via EAI no formato XML e JSON ao faturamento
type: support-article
updated_at: '2024-02-20T17:02:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21481279394071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Campos-integrados-via-EAI-no-formato-XML-e-JSON-ao-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21481279369367) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**

Gostaria de passar certos campos customizados ou, que a integração EAI JSON aceitasse os mesmos campos do padrão que a mensagem EAI XML aceita, como resolver?  
  
**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

O desenvolvimento das mensagens em diferentes formatos foi realizado em momentos distintos, sendo o formato JSON disponibilizado posteriormente.

Durante este desenvolvimento a criação do código para “leitura” do formato JSON seguiu com base na última versão disponível da mensagem em formato XML, sendo esta a versão 4.

Esta versão, mesmo via XML não trata certos campos, justamente por ser priorizado nas integrações EAI campos comuns em comportamentos de mercado, objetivando que a mensagem seja a mais simplificada para as integrações.

Sendo assim, existem essas duas opções:

* **1 -** Customizar o processo, todos os pontos de entrada estão no Saiba mais no fim do documento.  
    
  Ponto de entrada sugerido: [DT PE MT410EAI - Edição dos Arrays de cabeçalho e itens antes da gravação - Integração](https://tdn.totvs.com/x/D4TYCg)  
    
  Caso não encontre nenhum ponto de entrada, pode desenvolver um ponto de entrada participativo junto com a TOTVS ([saiba mais aqui](https://tdn.totvs.com/x/R1gjIw)).

* **2 -** Sugerir melhoria (Esse espaço é a nossa [Central Colaborativa TOTVS](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br). Para saber como criar uma sugestão de melhoria [clique aqui](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13), e para cadastrar uma nova sugestão, [aqui](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics/360001704573-TOTVS-Backoffice-Linha-Protheus-Faturamento-Faturamento).)

**Saiba mais:**

[Todos os pontos de entrada do módulo faturamento (SIGAFAT)](https://tdn.totvs.com/x/owQhH)
