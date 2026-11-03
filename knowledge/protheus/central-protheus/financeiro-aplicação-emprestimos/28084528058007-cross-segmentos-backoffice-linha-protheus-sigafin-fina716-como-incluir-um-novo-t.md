---
article_id: 28084528058007
category: Financeiro - Aplicação / Emprestimos
content_hash: 446d409164ff7b4ecb6db1fd7982e75b1b250b8acf88bb20755ee320fa289656
fetched_at: '2026-06-28T22:37:59.383364+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN – FINA716 - Como incluir
  um novo tipo de Aplicação/Emprestimo
type: support-article
updated_at: '2025-01-24T20:23:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28084528058007-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Como-incluir-um-novo-tipo-de-Aplica%C3%A7%C3%A3o-Emprestimo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28084522705175) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como adicionar um novo tipo de emprestimo e ou aplicação na rotina FINA716?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33    
  
**Solução** **Passo 1:** Cadastrar um novo tipo de aplicação/Emprestimo em **Configurador** -> Base de Dados -> Dicionário -> Base de Dados -> Tabelas Genéricas -> No codigo da chave 11 - Aplicação  
Exemplo cadastrar o tipo **REN - Renegociação**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28084522708759)

**Passo 2:** No **Configurador -> Cadastros -> Parâmetros**, no parâmetro **MV\_EMPCAL3**, informa o novo tipo cadastrado exemplo de preenchimento **"EMP|REN"**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28084522712727)

**Passo 3:** Ao incluir um novo emprestimo na rotina FINA716 ira trazer o novo tipo cadastrado "REN"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28084573047575)

**Saiba mais** sobre os parâmetros para **empréstimo**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28084528017431)  
Para incluir um novo tipo de aplicação, seguir o **passo 1** e informar no parâmetro **MV\_APLCAL2** o novo tipo de aplicação.  
  
Saiba mais sobre os parâmetros de **aplicação**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28084528020887)  
  
**Saiba mais**

[Aplicações e Empréstimos - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=392500138)
