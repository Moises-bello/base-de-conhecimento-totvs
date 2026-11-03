---
article_id: 15003213922711
category: Financeiro - Viagens
content_hash: d22f80c544088a62ab28e84d34ffedec66cac3b7b1c5b0d50bb6920ed63e4b86
fetched_at: '2026-06-28T22:38:21.456899+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA679 - Relacionamento
  entre Despesas X Filiais
type: support-article
updated_at: '2025-04-08T20:11:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15003213922711-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA679-Relacionamento-entre-Despesas-X-Filiais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31268073624855) Tempo aproximado para leitura: **00****:05:00 min****Dúvida**Como relacionar a tabela de despesas com a de localização?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**  
Realize a amarração das tabelas **Despesas** x **Localização**  **FWC** e **Itens Despesas** x **Localização FWD.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15002833014039)

Pode adicionar algumas localizações especificas ou replicar para todas as localizações, conforme print a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15002828593687)

**Importante**  
Obrigatoriamente as despesas devem ter ao menos uma localização atrelada a mesma, para que seja possível a geração da prestação de contas.

Um dos motivos deste processo acima, é caso acesse uma filial que não esteja configurado todas essas amarrações obrigatórias, não será possível lançar a prestação em uma outra Filial, pois a despesa não estará vinculada a uma localização.

Por mais que a tabela **FLG " Tipos de despesa"**, por padrão seja compartilhada entre as filiais, as tabelas **Despesas** x **Localização**  **FWC** e **Itens Despesas** x **Localização FWD**são exclusivas, sendo necessário o cadastro desses pontos por filial. 

**Saiba Mais**[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA679 - Cadastro de Despesas e Despesas X Localização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033699394-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA679-Cadastro-de-Despesas-e-Despesas-X-Localiza%C3%A7%C3%A3o)

**[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA677- HELP: DESPINVLD - Despesa selecionada não é valida para este local ou tipo de prestação de contas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404709811095-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA677-HELP-DESPINVLD-Despesa-selecionada-n%C3%A3o-%C3%A9-valida-para-este-local-ou-tipo-de-presta%C3%A7%C3%A3o-de-contas?source=search)**
