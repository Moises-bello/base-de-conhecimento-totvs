---
article_id: 10112735030295
category: Gestão de Transportes (TMS)
content_hash: 8710156ee03024b8564defb557dc3474bc029c2d249a1ba93e39a86723b77c33
fetched_at: '2026-06-28T22:45:33.360253+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Série CT-e
type: support-article
updated_at: '2024-08-05T20:40:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10112735030295-Log%C3%ADstica-Linha-Protheus-TMS-S%C3%A9rie-CT-e
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25427425561239) Tempo aproximado para leitura: **00:01:20 min** **Dúvida**Como cadastrar a série do **CT-e**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões.  
  
**Solução**Para criar uma série para utilizar no **CT-e** **- Conhecimento de transporte eletrônico** é necessário acessar as **Tabelas Genéricas - SX5** no **Configurador** e pesquisar pela **tabela 00**, **chave 01**, conforme demonstra imagem abaixo:

![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10112909403159)

No campo **Chave - X5\_CHAVE** deve ser informada a série que será utilizada para o **CT-e** e no campo **Descrição - X5\_DESCRI** a numeração inicial com 9 dígitos que deseja para esta série.  
  
Lembrando que, conforme definido pela **SEFAZ - Secretaria de Estado da Fazenda**, a série do **CT-e** deve conter 3 dígitos.  
  
Após efetuar a criação da série, ela será atrelada no cadastro **Configuração de Documentos - TMSA150** para o documento desejado.  
  
Para tratar regras mais específicas que precise utilizar séries diferentes da configuração de documento, o Sistema também possui o ponto de entrada **TM200SER** que permite a troca da série do documento de transporte.  
  
**Saiba mais**Verifique mais detalhes sobre o Ponto de entrada **TM200SER:** [Logística - Linha Protheus - TMS - Ponto de entrada TM200SER - troca da série do documento de transporte](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007302672-Log%C3%ADstica-Linha-Protheus-TMS-Ponto-de-entrada-TM200SER-troca-da-s%C3%A9rie-do-documento-de-transporte)
