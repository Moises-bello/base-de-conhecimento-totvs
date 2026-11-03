---
article_id: 360015767591
category: eSocial - Tabelas/Não Periódicos
content_hash: cffa94684e4869ffc33e01f1483a50838df1092ba102635ca124818d23bd6cda
fetched_at: '2026-06-28T22:47:10.269743+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Cadastro e envio do S-2300 de estagiários ao eSocial
type: support-article
updated_at: '2024-07-25T17:47:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015767591-RH-RM-FOP-eSocial-Cadastro-e-envio-do-S-2300-de-estagi%C3%A1rios-ao-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24445958987031)** Tempo aproximado para leitura:**00:02:30 min  
  
Dúvida**  
Como enviar corretamente a admissão de um estagiário para o eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Conforme a **Tabela 1 - Categoria de Trabalhadores**, disponibilizada pelo Governo, os estagiários devem ser admitidos com o código da Categoria eSocial igual a 901.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24445958997783)

**Cadastro**

1. Em **Registro |** **Tipo de Funcionário** preencha a o **Tipo de Funcionário** como **T - Estagiário**e **Código da Categoria eSocial**como 901;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24445959008663)

2. Os **Dados do Estágio** são habilitados apenas quando o campo **Tipo de Funcionário for T;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24445959015575)

3. Confira se todos os demais campos obrigatórios foram preenchidos e salve o cadastro;  
4. Após concluído o cadastro, confira se a Matrícula foi preenchida automaticamente;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24445945553815)

4.1. Será necessário o [**Preenchimento de Matrícula**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9188778633879-RH-RM-FOP-eSocial-Como-preencher-Matr%C3%ADcula-eSocial), caso o campo não esteja preenchido. Pois para novos estagiários, desde o leiaute S-1.0, o preenchimento da matrícula é obrigatório.   
  
**XML**  
1. Após concluído o cadastro, acesse eSocial | Eventos de Tabelas/Não Periódicos | Fila de Eventos | Identifique o gatilho do evento S-2300;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24445959028247)

2. Selecione o evento desejado e Gere o XML;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24445959032215)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24445945571479)

3. Após a conferência das informações no XML, integre o evento.

**Importante**  
- **Alterações de dados cadastrais** dos Estagiários são geradas no evento **S-2205**.  
- **Alterações contratuais** dos Estagiários são geradas no evento **S-2306**.  
- **Desligamentos** dos Estagiários são gerados um evento **S-2399 com os dados do desligamento** e um evento **S-1200 com as verbas rescisórias**.

**Saiba mais**[RH - RM - FOP - Cadastro de Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13608492825239-RH-RM-FOP-Cadastro-de-Funcion%C3%A1rios)
