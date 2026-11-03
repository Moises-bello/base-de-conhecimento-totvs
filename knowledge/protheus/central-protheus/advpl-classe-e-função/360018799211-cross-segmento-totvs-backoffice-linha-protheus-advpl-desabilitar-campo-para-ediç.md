---
article_id: 360018799211
category: ADVPL - Classe e Função
content_hash: 5b225cc247a86e44473387166cd905e8c5ebf928904f9b77a17a1e6fda28f493
fetched_at: '2026-06-28T22:40:15.757244+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Desabilitar campo
  para edição
type: support-article
updated_at: '2022-01-05T15:26:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018799211-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Desabilitar-campo-para-edi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como desabilitar um campo para edição em campo padrão ou customizado?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**No configurador:

* selecione o campo
* na aba opções
* retorne *True* ou *False* no **Modo Edição**.

```
Exemplos:  
  
IF(LogUserName() == 'usuario.xxxx',.T.,.F.) // validando com o usuário do sistema  
  
IF(RetCodUsr() == 'cod_usuario',.T.,.F.)// validando com o usuário corrente   
  
IF(Inclui,.T.,.F.) // validando com variável publica  
  
U_TesteValida() // retorno desta função de usuário é true
```

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014267491/mceclip0.png)

**Saiba Mais**  
[**LogUserName**](http://tdn.totvs.com/display/tec/LogUserName)  
[**RetCodUsr**](http://tdn.totvs.com/display/public/PROT/RetCodUsr)  
**[Funções de Cadastro de Usuários](http://tdn.totvs.com/pages/viewpage.action?pageId=6814847)**
