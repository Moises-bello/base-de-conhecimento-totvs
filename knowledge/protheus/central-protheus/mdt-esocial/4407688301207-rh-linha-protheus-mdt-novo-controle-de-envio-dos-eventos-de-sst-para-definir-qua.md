---
article_id: 4407688301207
category: MDT - eSocial
content_hash: e5dbc0790ce54f099a097b7f3478d3a0566d69343c25fef065fc630729e3de3f
fetched_at: '2026-06-28T22:44:29.418826+00:00'
product: protheus
section_id: 360004428991
source: central-protheus
title: RH - Linha Protheus - MDT - Novo Controle de Envio dos Eventos de SST para
  definir quais categorias de funcionários do eSocial NÃO serão integrados com o SIGATAF/Middleware
type: support-article
updated_at: '2025-08-04T13:31:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407688301207-RH-Linha-Protheus-MDT-Novo-Controle-de-Envio-dos-Eventos-de-SST-para-definir-quais-categorias-de-funcion%C3%A1rios-do-eSocial-N%C3%83O-ser%C3%A3o-integrados-com-o-SIGATAF-Middleware
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25676655616535)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao gerar a carga inicial do evento **S-2240** (**MDTA881**) deseja-se ter controle sobre quais categorias de funcionários terão os eventos de SST comunicados ao SIGATAF/Middleware. Novo Controle de Envio dos Eventos de SST Parâmetro **MV\_NG2NENV**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Criação do parâmetro **MV\_NG2NENV**.  
O parâmetro irá definir quais categorias de funcionários do eSocial **NÃO** serão integrados com o SIGATAF/Middleware, ou seja, os funcionários que tiverem suas categorias (**RA\_CATEFD**) inseridas no parâmetro **MV\_NG2NENV** não serão comunicados. É importante frisar que o sistema irá realizar essa validação em todos os envios dos eventos de SST (**S-2210, S-2220 e S-2240**) e não apenas na carga inicial do evento **S-2240**, como por exemplo: o evento **S-2210** também não será comunicado caso a categoria do funcionário (**RA\_CATEFD**) que sofreu o acidente estiver contida no parâmetro **MV\_NG2NENV**.  
  
**Importante!**O parâmetro **MV\_NG2NENV** deve ser preenchido no padrão a seguir: "**701/711/712**" (sem aspas), ou seja, com o código da categoria do eSocial de três dígitos seguido de uma barra "**/**" (sem aspas). A configuração do exemplo indica que os eventos de SST **não** serão enviados para os funcionário que tiverem suas categorias (**RA\_CATEFD**) igual a **701, 711** ou **712**. Se a categoria do funcionário for igual a **101** por exemplo, os eventos de SST desse funcionário serão comunicados normalmente.

Caso o parâmetro não exista ou estiver em branco, todas os funcionários de qualquer categoria terão os eventos de SST comunicados normalmente.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407688294551)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407688299031)

**Exemplos de uso:**

* Parâmetro MV\_NG2NENV **inexistente** ou com conteúdo **em branco**:

O sistema efetuará o envio dos eventos de SST para todos os funcionários de qualquer categoria.

* Parâmetro MV\_NG2NENV com conteúdo igual a **701**:

O sistema efetuará o envio dos eventos de SST para todos os funcionários exceto os que tiverem a categoria igual a 701.

* Parâmetro MV\_NG2NENV com conteúdo igual a **701/711/712**:

O sistema efetuará o envio dos eventos de SST para todos os funcionários exceto os que tiverem a categoria igual a 701, 711 ou 712.

* Parâmetro MV\_NG2NENV com conteúdo igual a **999**:

O sistema efetuará o envio dos eventos de SST para todos os funcionários exceto os que tiverem a categoria igual a 999.

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
