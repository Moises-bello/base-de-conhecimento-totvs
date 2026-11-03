---
article_id: 360053137914
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: b204aacf4b5db684ca979b141170f1b71abfea310c6bdbda73d4456635ffe674
fetched_at: '2026-06-28T22:39:47.766945+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Integração Taxa
  de Câmbio
type: support-article
updated_at: '2024-03-05T21:11:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053137914-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Integra%C3%A7%C3%A3o-Taxa-de-C%C3%A2mbio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Gostaríamos de saber se é possível sincronizar/automatizar o cadastro de "Cotação de Moeda" do Módulo SIGAEIC com o portal do Banco Central?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.  
  
**Solução**Temos a rotina Int. Taxa de Cambio” (INTBCOCENT) no módulo Easy Import Control (SIGAEIC), que é responsável pela integração das taxas de Câmbio na rotina de Cotação de Moedas (EECAT140).   
Segue abaixo as premissas para a utilização da rotina:  
**Parâmetro**  
MV\_INTTX -> "Define qual taxa será integrada na integração de taxas de câmbio VENDA ou COMPRA” - Conteúdo padrão = "VENDA"

**Pré-Requisitos:**É necessário possuir um arquivo (.csv) de taxas de Conversão de Cambio no layout do site do Banco Central do Brasil.   
  
Segue abaixo o link:  
[Site Banco central](https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes)  
  
**Sequencia 001:**

1. No módulo “Easy Import Control” (SIGAEIC), acesse as opções “Miscelânea/ Int. Taxa de Cambio” (INTBCOCENT).  
   2. Clique em Selecione o Arquivo, escolha um arquivo e clique em OK.  
   3. Clique em Ler arquivo para carregar os itens.  
   4. Selecione os registros para efetuar a integração e clique em OK, e confirme a integração clicando em Sim.  
   5. Será apresentada a mensagem Integração efetuada com sucesso, após clique em OK.  
   6. Será retornado para o menu principal.

**Sequencia 002:**  
1. No módulo “Easy Import Control” (SIGAEIC), acesse as opções “Atualizações/ Cadastros/ Cotação das Moedas” (EECAT140).  
2. Visualize as novas taxas inseridas através da integração.  
3. Será exibido as moedas que foram importadas do arquivo csv.
