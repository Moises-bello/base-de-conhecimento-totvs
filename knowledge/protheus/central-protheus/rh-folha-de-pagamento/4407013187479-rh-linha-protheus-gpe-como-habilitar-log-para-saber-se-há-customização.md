---
article_id: 4407013187479
category: RH - Folha de Pagamento
content_hash: 5b12ca3d0f7659d3ea6eb305b0590d2cacc45c70287b8008108630a540b16d49
fetched_at: '2026-06-28T22:44:13.540601+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como habilitar log para saber se há customização
type: support-article
updated_at: '2024-09-13T14:44:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407013187479-RH-Linha-Protheus-GPE-Como-habilitar-log-para-saber-se-h%C3%A1-customiza%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26350649335959) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como habilitar log para saber se há customização?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Para habilitar o LOG, deve-se criar a chave**IXBLOG=LOGRUN** no *environment* (INI do Server ) que se deseja monitorar.

Os arquivos de LOG são gravados por usuário no diretório \IXBLOG.

O nome do arquivo gerado será: **<nome do usuário>+\_NNNNN.LOG**.

Onde: NNNNN - corresponde a uma numeração aleatória.

          IXBLOG=LOGRUN

Este comando executa o ponto de entrada e grava um LOG na pasta IXBLOG com o arquivo -> Nome do Usuário + \_ + Sequencial.

         IXBLOG=NORUN

Este comando **NÃO** executa o ponto de entrada.

**Observação**Ao habilitar o LOG de *User function*, será exibida no servidor Protheus uma mensagem avisando que ao utilizar essa opção a performance do Sistema será afetada.

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
