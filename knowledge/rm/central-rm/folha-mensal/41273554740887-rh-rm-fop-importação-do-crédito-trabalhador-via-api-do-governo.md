---
article_id: 41273554740887
category: Folha Mensal
content_hash: d1d24e732e7154299d495595b760e5e353ebb4d3ce584ba1ef196329a740de9c
fetched_at: '2026-06-28T22:46:57.864635+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Importação do Crédito Trabalhador via API do Governo
type: support-article
updated_at: '2026-06-17T11:55:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41273554740887-RH-RM-FOP-Importa%C3%A7%C3%A3o-do-Cr%C3%A9dito-Trabalhador-via-API-do-Governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41273554712087) Tempo aproximado para leitura: **00:05:19 min**  
  
**Dúvida**  
Como realizar a importação do Crédito Trabalhador utilizando a integração via API do Governo (TAF ou Middleware), sem a necessidade de carregar arquivos manualmente?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

Lembrando que, será a partir dos patches:

* 12.1.2506.324
* 12.1.2510.253
* 12.1.2602.167
* 12.1.2606.1 e superiores

**Causa**  
Implementação de nova funcionalidade que permite a busca automatizada dos dados diretamente da API do Governo, otimizando o processo que antes era feito exclusivamente por importação de arquivos de texto/layout.

**Solução**  
1. Parametrização Inicial

Para habilitar o recurso, acesse: **Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Crédito Trabalhador**.

⚠️ **Importante:** O novo agrupador **"Integração"** só ficará visível na tela se houver configurações prévias e válidas de **TAF** ou **Middleware** no ambiente. Caso contrário, os novos campos não serão exibidos.

No agrupador **Integração**, configure os seguintes campos:

* **Chamada API utilizando paralelismo:** Se marcado, o sistema criará uma *thread* para cada coligada, executando as chamadas à API simultaneamente.

  + *Recomendação:* Utilizar apenas em cenários com elevado número de coligadas ou quando a API do governo apresentar lentidão.
* **Ambiente (Produção e Homologação):** Define o ambiente de destino.

  + *Default:* Se nenhuma flag estiver marcada, o sistema assumirá o valor **2 - Homologação**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273690629783)

### **2. Executando a Importação**

Acesse a tela de **Importação do Crédito Trabalhador**:

1. Marque o novo *checkbox* **"Importação via API"**.

   * *Nota:* Este campo só aparece se os parâmetros do TAF/Middleware estiverem ativos. Ao marcá-lo, os campos de carregamento de arquivo manual e suas respectivas validações serão **desabilitados**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273686956439)

        2. Avance na tela, selecione a(s) coligada(s) desejada(s) e clique em **Executar**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273690637463)

### **3. Como o processo funciona por trás?**

O sistema lê as coligadas selecionadas na tela e, para cada uma delas, busca as seguintes diretrizes em banco de dados para realizar a autenticação e busca na API:

O processo irá buscar as coligadas selecionadas na tela e, para cada uma delas, validará os dados parametrizados conforme as tabelas abaixo:

| **Do sistema:** |
| --- |
| Mês competência atual do sistema |
| Ano competência atual do sistema |
| Multi-Thread habilitado (bool) |

| **Dados TAF (Se configurado TAF)** |
| --- |
| Servidor e porta TAF |
| Filial TAF |
| Usuário e senha |
| Usa DePara Filial (RM X TAF) |

| **Dados Middleware (Se configurado Middleware)** |
| --- |
| Servidor e porta middleware |
| Usuário e senha |
| Ambiente (1 - Produção - 2 Homologação) |

📌 Observação: O retorno da API é o mesmo sendo TAF ou Middleware. O que muda são os parâmetros enviados: no caso do Middleware, são enviados dois parâmetros a mais (Servidor TSS e Ambiente). Mas o formato do retorno é idêntico.

### **4. O que a API retorna**

A API retorna dados no formato **JSON**. Dentre os vários campos que ela retorna, o mais importante que está sendo extraído pelo sistema é o campo **"Arquivo"**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273554715671)

Ao ser descriptografado, o campo arquivo se transforma no mesmo conteúdo do arquivo físico JSON já importado pelas empresas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273554716823)

* **Lógica de Processamento:** A partir deste ponto em diante, utiliza-se a mesma lógica já existente anteriormente, que é chamada na leitura dos arquivos.
* **Validação:** Esta lógica irá validar os mesmos campos obrigatórios da importação "manual" já existente, extrair os dados necessários, definir o evento e, no final, atualizar ou incluir o empréstimo.

Como resultado, ao final do processamento devemos visualizar os mesmos dados de quando está sendo feito via Arquivo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273554718103)

### **5. Como funciona o parâmetro "Habilitar Multi-Thread"**

Este parâmetro pega a lista de coligadas que foi selecionada na tela e dispara para todas elas a chamada na API do TAF e/ou Middleware de forma **simultânea**.

* A lógica fica aguardando o retorno de todas as chamadas.
* Quando todas finalizam, ele inicia a importação dos dados.
* *Recomendação:* Este recurso só deve ser utilizado em clientes que possuam elevados números de coligadas e/ou cuja chamada da API seja demorada.

⚠️ Importante: Caso seja necessário importar um arquivo para meses anteriores ou posteriores ao atual, será necessário a importação manual (Via arquivo), como era feito anteriormente.

**Saiba Mais**

[Crédito Trabalhador via API do Governo](https://tdn.totvs.com/pages/releaseview.action?pageId=1043694719)

[RH - RM - FOP - Empréstimo consignado Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30965515667607-RH-RM-FOP-Empr%C3%A9stimo-consignado-Cr%C3%A9dito-do-Trabalhador)
