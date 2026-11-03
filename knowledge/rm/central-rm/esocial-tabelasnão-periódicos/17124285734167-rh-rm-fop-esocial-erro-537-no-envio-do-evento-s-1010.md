---
article_id: 17124285734167
category: eSocial - Tabelas/Não Periódicos
content_hash: aa930445591f304b156477cbbd3d9f099874dfdfbf316c7affb6f3866029d365
fetched_at: '2026-06-28T22:47:10.572647+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP- eSocial- Erro 537 no envio do evento S-1010
type: support-article
updated_at: '2024-04-03T11:37:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17124285734167-RH-RM-FOP-eSocial-Erro-537-no-envio-do-evento-S-1010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17124329454615) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**  
Ao realizar o envio do evento S-1010 do eSocial, é retornado erro de código **537: Já existe no sistema registro com mesmo código de identificação (chave) em período de vigência conflitante com o período informado no registro atual. Ação Sugerida: O evento somente pode ser recepcionado se não existir outro evento para a tabela com o mesmo código de identificação (chave) em período de vigência conflitante com o período informado no evento atual. Certifique-se que o código de identificação e os períodos informados estejam corretos.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17283336260119)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro geralmente ocorre quando já existe um registro do evento S-1010 no eSocial Web com início de validade igual ou posterior ao do XML e constando os mesmo dados (código, número inscrição, etc.).  
  
**Solução**Para ajuste deste incidente, verifique se no eSocial Web (ambiente do governo) consta um registro S-1010 para a verba utilizada:

* **Registro posterior existente**

A primeira coisa a ser observada é se os dados de código de rubrica, identificador da rubrica, incidências, nº de processos, etc., não podem ser exatamente iguais aos do registro existente, pois não caracterizaria uma mudança/alteração do registro.

Em relação à validade, caso o início de validade seja **igual** ao do registro já existente, verifique se o XML atual consta o **Tipo de Operação** como **Alteração**. O mesmo serve para o texto do XML, que deve então possuir o grupo **alteração**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17462861161751)

Já se o início de validade for **posterior** ao do registro já existente, o **Tipo de Operação** continuará como **Alteração**, mas no texto do XML haverá o grupo **inclusão** com os dados a serem registrados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17462863205143)

* **Não existe registro cadastrado no ambiente do governo**

Se for encontrado nenhum registro dessa verba no ambiente do eSocial, tanto o **Tipo de Operação** quanto o grupo do XML deverão constar como **Inclusão**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17462856169495)

Se ambos estiverem corretos, e ainda sim o erro for apresentado, deve-se realizar contato com o governo através do [Fale Conosco](https://www.gov.br/esocial/pt-br/canais_atendimento/contato) para avaliação.  
  
**Importante**Caso você identifique alguma divergência de informações conforme descritivos acima, entre em contato com o suporte técnico apresentando as evidências avaliadas.
