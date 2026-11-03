---
article_id: 37811869280663
category: RH – DIRF
content_hash: 6c4a5db4959298f083485479c046768b194b6995c4215fcc49774f7182f60690
fetched_at: '2026-06-28T22:44:07.866817+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir os valores do Informe de Rendimentos
  com a Ficha Financeira
type: support-article
updated_at: '2026-01-20T20:21:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37811869280663-RH-Linha-Protheus-GPE-Como-conferir-os-valores-do-Informe-de-Rendimentos-com-a-Ficha-Financeira
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37811869259671) Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Como Conferir os valores do Informe de Rendimentos com a Ficha Financeira?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

1. Acesse: Miscelanea / DIRF / Gerar Arquivo (GPEM550) e preencha as perguntas para que os valores sejam gerados. Saiba mais: [Como Gerar Arquivo DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012-RH-Linha-Protheus-GPE-Passo-a-Passo-para-gerar-dados-gerar-Arquivo-DIRF)
2. Acesse: Relatórios / Lançamentos / Ficha Financeira (GPER270) e preencha as perguntas conforme o exemplo abaixo:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37811896830871)

   Pergunta "Imp. Incidências?" : **Sim**   
   Pergunta "Incidencias a Impr:" : **1** e **4**  
   Pergunta "Ficha Financeira" : **Pagamento**  
   Pergunta "Roteiro" : **FOL, 132, PLR, AUT**  
   Pergunta "Destaca ADI.?" : **Sim**  
   Pergunta "Destaca FER.?" : **Sim**

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37811869262615)**Dica**: Para facilitar a conferência, gere a Ficha Financeira em Excel, selecionando o Tipo Planilha.
3. Acesse: Miscelanea / DIRF / Informe de Rendimento (GPEM580), e preencha as perguntas para gerar o Informe de Rendimento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37811869263639)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37811869264279)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37811869267479)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37811896834327)

Abaixo segue como os valores são montados no Informe de Rendimento de acordo com as incidências para a DIRF:

**Quadro 3** - Rendimentos tributáveis, deduções e imposto:

Linha 01 = Soma de Todas as verbas com incidência A  
Linha 02 = Soma de Todas as verbas com incidência B  
Linha 04 = Soma de Todas as verbas com incidência C  
Linha 05 = Soma de Todas as verbas com incidência D

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37811896835351)![](https://centraldeatendimento.totvs.com/hc/article_attachments/37811896835991)

**Quadro 4** – Rendimentos Isentos e Não Tributáveis:

Linha 09 = Soma de Todas as verbas com incidência I e 0

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37811896837527)

**Quadro 5** - Rendimentos sujeitos à tributação exclusiva:

Linha 01 = Valor líquido do 13º  
Linha 02 = Soma das verbas com Incidência L  
Linha 03 = Soma das verbas com incidência O

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37811869271575)

**Quadro 7** - Informações complementares:

* Listados os beneficiários de Pensão Alimentícia, desde que estejam cadastrados na tabela SRQ - Cadastro de Beneficiários.
* Listados todos os Dependentes/Agregados que possuírem plano de Assistência Médica e/ou odontológica (Incidência R), bem como, a Razão Social e o CNPJ do fornecedor dos Planos de Saúde, os valores são obtidos da tabela de Histórico de Plano de Saúde (RHS) e da tabela de Histórico de Coparticipação e Reembolso de Plano de Saúde (RHP).
* Listado o valor bruto e o líquido recebido de Participação nos Lucros ou Resultados (PLR).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37811869262615)**Dica**: Para facilitar a conferência dos valores de Plano de Saúde, Odontológico, Coparticipação e Reembolso, utilize o relatório GPER014. Saiba Mais: [Como emitir relatório Acumulados Assistência médica/Odontológica GPER014](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20177753900823-RH-Linha-Protheus-GPE-Como-emitir-relat%C3%B3rio-Acumulados-Assist%C3%AAncia-m%C3%A9dica-Odontol%C3%B3gica-GPER014)

**Saiba Mais:**

[RH-DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)

[Informações e atualizações sobre a Entrega Informe de Rendimento 2026 (Ano-Calendário 2025)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37729787696279-RH-Linha-Protheus-GPE-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-a-Entrega-Informe-de-Rendimento-2026-Ano-Calend%C3%A1rio-2025)
