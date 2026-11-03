---
article_id: 1500003365722
category: RH - Cadastros
content_hash: 300396e33ad40ab2c2389c50fe67ff1ad9a1f96864224b1422bcdebc45a6d57c
fetched_at: '2026-06-28T22:43:25.923212+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Habilitar a chave IXBLOG
type: support-article
updated_at: '2026-06-25T11:09:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003365722-RH-Linha-Protheus-GPE-Habilitar-a-chave-IXBLOG
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33790132823319)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**Como habilitar a chave **IXBLOG**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**No **servidor** que o Sistema está instalado, acesse a pasta **Appserver** e localize o arquivo **appserver.ini**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33790142048663)  
  
Abra o arquivo e crie a chave **IXBLOG** conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33790132824087)

Essa chave tem duas funções:  
  
**IXBLOG=LOGRUN**  
Executa e armazena informações dos **P.E.** encontrados durante a execução do Sistema.  
 **IXBLOG=NORUN**  
Armazena as informações no **LOG**, porém não executa o **P.E.**  
  
Após, configurar o comando, baixe e suba o *server.*  
Ao acessar o Sistema, abra o programa inicial como **SIGAADV** ou **SIGAGPE**.

**Saiba Mais**[Artigos Cadastros](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781894-RH-Cadastros)  
[Artigos Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)  
[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
