---
article_id: 8660633914519
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: dd2732acb943f8e3e87154040cdc5dd2b963bd8c3876707bb239baa723e0b119
fetched_at: '2026-06-28T22:39:47.804045+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - TOTVS Comex Conteúdo
  O Sistema Não Pode Criar os Diretórios Necessários Para a Integração
type: support-article
updated_at: '2022-09-08T13:40:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8660633914519-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-TOTVS-Comex-Conte%C3%BAdo-O-Sistema-N%C3%A3o-Pode-Criar-os-Diret%C3%B3rios-Necess%C3%A1rios-Para-a-Integra%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Ao tentar integrar o Totvs Comex Conteúdo (**EICCD100**) no módulo do **SIGAEIC** é exibida a seguinte mensagem **"Atenção - O sistema não pode criar os diretórios necessários para a integração."** . Como faço para efetuar a  integração sem exibir esta mensagem?

![DIRETORIOS_-_COMEX_CONTEUDO.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8660020684439/DIRETORIOS_-_COMEX_CONTEUDO.PNG)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Por algum motivo o sistema não criou a pasta comexconteudo. Este diretório é o que fica responsável em armazenar os logs. O procedimento a ser feito nestes casos:

1. Caso seu ambiente seja on premise (ambiente local) verifique se existem estas pastas criadas **\protheus\_data\comex\totvscomexconteudo** . Caso contrário será necessário cria-las.
2. Caso seu ambiente seja Cloud peça para o time responsável da Totvs Cloud verificar se existem estas pastas criadas **\protheus\_data\comex\totvscomexconteudo** . Caso contrário o time do Totvs Cloud será necessário criar esta pasta.
3. Se o ambiente for cloud as pastas deverem serem minusculas pois o ambiente onde ficam as pastas são case sensitive.

Efetuado este procedimento faça um novo teste e a integração será feita com sucesso.
