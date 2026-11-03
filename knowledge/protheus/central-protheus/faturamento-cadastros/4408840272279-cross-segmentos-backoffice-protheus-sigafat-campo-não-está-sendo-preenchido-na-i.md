---
article_id: 4408840272279
category: Faturamento - Cadastros
content_hash: 7997cffda30f9113ff5ac05e99a43f12e1de994b8d90839c673d762ffec8d8b0
fetched_at: '2026-06-28T22:38:35.419598+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Campo não está sendo preenchido
  na integração API CAROL x Cadastro de Clientes
type: support-article
updated_at: '2026-03-26T14:21:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408840272279-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Campo-n%C3%A3o-est%C3%A1-sendo-preenchido-na-integra%C3%A7%C3%A3o-API-CAROL-x-Cadastro-de-Clientes
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39307433017239) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Na integração da API Carol x Cadastro de Clientes, não esta sendo preenchido os campos "Nome - A1\_NOME" ou "Nome Fantasia - A1\_NREDUZ".  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - A partir da versão 12  
  
**Solução**  
Este comportamento ocorre quando as informações retornadas pela Receita Federal excedem o tamanho configurado para os campos no sistema. Nesses casos, para evitar o preenchimento incompleto ou truncado, o sistema mantém o campo em branco, permitindo que o usuário realize o preenchimento manual correto.

**Observação:**  
O comportamento de deixar o campo em branco ocorre exclusivamente no cadastro de Clientes em MVC, a partir da release 12.1.33, quando o parâmetro **MV\_MVCSA1** estiver habilitado.

---

Após o preenchimento do CNPJ, caso os campos **Nome** ou **Nome Fantasia** não sejam carregados automaticamente, recomenda-se verificar os seguintes pontos:

* Confirmar se o CNPJ está regular e com cadastro válido na Receita Federal;
* Verificar se houve alguma alteração cadastral recente (inferior a 90 dias), considerando que este é o prazo necessário para atualização das informações na API Carol.

[Consulta Receita Federal](https://solucoes.receita.fazenda.gov.br/servicos/cnpjreva/cnpjreva_solicitacao.asp)

---

#### **Validação do tamanho dos campos**

Verifique se a quantidade de caracteres retornada pela Receita Federal é compatível com o tamanho configurado dos campos no Protheus. Caso a informação exceda o limite permitido, o sistema poderá não preencher o campo automaticamente.

#### **Tamanho padrão dos campos**

* **Nome (A1\_NOME):** 40 caracteres
* **Nome Fantasia (A1\_NREDUZ):** 20 caracteres
* **Endereço (A1\_END):** 80 caracteres
* **Bairro (A1\_BAIRRO):** 40 caracteres

---

#### **Observação**

Recomenda-se que o campo **Nome Fantasia (A1\_NREDUZ)** possua o mesmo tamanho do campo **Nome (A1\_NOME)**.

Isso se deve ao fato de que, na ausência de Nome Fantasia na Receita Federal, o sistema utiliza automaticamente o conteúdo do campo **A1\_NOME** para preenchimento. Caso o campo **A1\_NREDUZ** tenha tamanho inferior, a informação poderá ser truncada ou não preenchida.

---

#### **Como ajustar o tamanho do campo**

Para realizar o ajuste do tamanho dos campos, siga o caminho abaixo no sistema:

Acessar o Configurador (SIGACFG), com um usuário que tenha acesso "Admin".

**Configurador → Base de Dados → Dicionário → Bases de Dados → Tabela SA1 (Clientes)**

Localize os campos desejados e realize a alteração conforme a necessidade.

**Saiba Mais**

[**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Cadastro de Clientes (MATA030) x CAROL (Integração via API)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009140342-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Cadastro-de-Clientes-MATA030-x-CAROL-Integra%C3%A7%C3%A3o-via-API-)
