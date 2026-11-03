---
article_id: 1500008649581
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 52ad6fedc5ac067a9daca71d986169b3f296e26c77399325c9ef1aed5efea337
fetched_at: '2026-06-28T22:42:47.058742+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Tela de empenho não abre ao sair da
  rotina MATA650 para a filial que não estou logado
type: support-article
updated_at: '2021-05-26T11:39:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008649581-Manufatura-Linha-Protheus-SIGAPCP-Tela-de-empenho-n%C3%A3o-abre-ao-sair-da-rotina-MATA650-para-a-filial-que-n%C3%A3o-estou-logado
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:55 min**  
**Dúvida**Por que ao sair da rotina **MATA650 - Ordem de Produção** não é aberta a tela de **empenho** para a filial que não estou logado?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Essa situação ocorre quando está logado numa filial, porém **OP - Ordem de Produção** está sendo aberta para outra filial e o parâmetro **MV\_A650GEF - Gera empenho considerando todas as filiais** está desativado ou em branco.  
  
**Exemplo:**  
Acessei o **Protheus** na **filial 01**, mas no momento de abrir a **OP** estou abrindo ela para a **filial 02**.  
Neste caso se o parâmetro **MV\_A650GEF** não estiver ativado ao sair da rotina **MATA650** não é aberta a tela de geração de empenho  
  
**Saiba mais**  
Para mais informações sobre o parâmetro acesse a documentação: [Manufatura - Linha Protheus - SIGAPCP - Qual o objetivo do parâmetro MV\_A650GEF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028907272-MP-SIGAPCP-Qual-o-objetivo-do-par%C3%A2metro-MV-A650GEF)
