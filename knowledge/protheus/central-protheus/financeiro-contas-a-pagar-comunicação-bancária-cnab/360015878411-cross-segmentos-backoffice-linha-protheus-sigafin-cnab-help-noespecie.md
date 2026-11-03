---
article_id: 360015878411
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 221f71dc10bdc994d71a1292e24a68771d601cab7f6241e2074875d81e44228a
fetched_at: '2026-06-28T22:37:55.370451+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB Help: NOESPECIE'
type: support-article
updated_at: '2023-05-31T02:00:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015878411-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CNAB-Help-NOESPECIE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00min  
  
Ocorrência**No módulo **Financeiro**, ao tentar realizar **Retorno de cobrança (FINA200)** é apresentada o Help: **NOSPECIE.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CNAB - Todas as versões

**Causa**É apresentado este Help quando não está cadastrado na **tabela 17 (SX5)** o conteúdo que consta no arquivo de retorno na posição da espécie informado no arquivo de configuração.   
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o **módulo Financeiro**, **Atualizações**, **Cadastros**> **Parâmetros Bancos**;  
2. Acesse o cadastro correspondente ao Banco do Retorno;  
3. Verifique se o campo: **Tabela (EE\_TABELA)**estar com conteúdo: 17;  
4. Acesse o **Configurador** (**SIGACFG**), **Ambiente**, **Cadastro**, **Tabelas**;  
5. Acesse a **Tabela 17** e informe o código de acordo com a ordem numérica atrelando ao tipo de título que será gerado no retorno. Conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012702632/mceclip0.png)

**Saiba mais.**<http://tdn.totvs.com/pages/releaseview.action?pageId=240288856>
