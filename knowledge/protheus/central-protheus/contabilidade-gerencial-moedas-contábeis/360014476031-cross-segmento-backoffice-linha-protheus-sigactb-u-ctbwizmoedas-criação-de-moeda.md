---
article_id: 360014476031
category: Contabilidade Gerencial - Moedas Contábeis
content_hash: 0e8d49c1b63f996aa24a66650ccdcaf440892fd8341ec0917ddaa360bc7d3771
fetched_at: '2026-06-28T22:40:51.291473+00:00'
product: protheus
section_id: 1500001537601
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - U_CTBWIZMOEDAS - Criação
  de Moedas
type: support-article
updated_at: '2025-01-23T13:35:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014476031-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-U-CTBWIZMOEDAS-Cria%C3%A7%C3%A3o-de-Moedas
---

A criação de moedas é um recurso para efetuar os controles necessários à utilização de mais de **5 (cinco) moedas no sistema**, com a possibilidade de criação de até 99 moedas.

Essa ferramenta é **responsável** por:

* Criar os novos campos relacionados aos controles dessas moedas;
* Criar os novos parâmetros relacionados aos controles dessas moedas;
* Atualizar, para essas moedas, o dicionário de dados com as descrições adequadas aos idiomas;
* Atualizar campos de controle nos dicionários de dados, cujo tamanho estiver vinculado à quantidade de moedas em uso pelo Sistema.

|  |
| --- |
| **Importante 📢️:**   * O **Wizard de Configuração** de moedas apenas cria os campos necessários para o uso de mais moedas no Sistema. **Cabe ao usuário cadastrar as moedas contábeis e vinculá-las aos calendários contábeis**. |

---

### 

### **Procedimentos**

**Nenhum usuário deve utilizar o Sistema durante esta atualização.**

1. Acesse a tela de abertura do Protheus Remote e informe no campo **Programa inicial**, **U\_CTBWIZMOEDAS**;

Visualize a tela com os objetivos do **Assistente de Configuração**, ressaltando a importância de efetuar backup completo dos dicionários e da base de dados antes de iniciar a execução;

2. Parametrize o processo de geração de moedas, informando a quantidade de moedas para criar e se a descrição será comum aos três idiomas básicos suportados (Português, Inglês e Espanhol). A moeda inicial para configuração é determinada automaticamente pela rotina.

Esta tela apresenta os campos:

1. * + **Total de moedas para criar** – Informe quantas moedas são criadas pela atualização.
     + **Numeração da primeira moeda para criar** – Campo preenchido automaticamente pelo Sistema.
     + **Definir descrição da moeda em qual idioma** – Disponíveis as opções: **único** (idioma de instalação) e **todos** (todas as línguas).

3. Clique em Avançar.

4. Continuando com a parametrização, conforme os dados já informados, se informada a opção de descrição **Única**, será exibido somente um campo.

5. Se a opção foi por **todas** as moedas, o grid de digitação das informações apresenta um grupo de campos de descrição para cada tipo de informação solicitada para as moedas. Confirme para prosseguir.

6. A próxima etapa do assistente é a **atualização do módulo**.

7. O Sistema exibe a tela para confirmação da parametrização das novas moedas. Para confirmar, clique em Sim.

8. Visualize a tela de acompanhamento do progresso de atualização, indicada por uma barra de processamento.

9. Ao término visualize o log com as atualizações realizadas por empresa / filial.

10 .Utilize a opção **Salvar** para gravar a informação.

**Saiba Mais:**

[Cálculo de Depreciação Para Até 15 Moedas Com Procedures](http://tdn.totvs.com/pages/viewpage.action?pageId=347441403)

[Wizard para configuração de moedas](http://tdn.totvs.com/pages/viewpage.action?pageId=334343951)
