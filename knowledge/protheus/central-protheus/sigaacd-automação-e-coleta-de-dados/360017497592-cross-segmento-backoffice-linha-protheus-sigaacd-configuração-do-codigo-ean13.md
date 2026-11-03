---
article_id: 360017497592
category: SIGAACD - Automação e Coleta de Dados
content_hash: c81837b6b0423de851b26ea9ee84d0acde939bcd1609eed95d180a23ba1f58d0
fetched_at: '2026-06-28T22:39:10.974169+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Configuração do codigo
  EAN13
type: support-article
updated_at: '2025-07-24T17:31:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017497592-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configura%C3%A7%C3%A3o-do-codigo-EAN13
---

O artigo explica como configurar o código EAN13 no sistema SIGAACD, utilizado no TOTVS Backoffice (Linha Protheus) para o módulo de Estoque/Custos. Para configurar o EAN13, o usuário deve inserir 12 caracteres no campo B1\_CODBAR na rotina MATA010 – Cadastro de Produto. O sistema calcula automaticamente o 13º dígito, conhecido como dígito verificador, usando o algoritmo de validação EAN. É essencial que cada produto tenha um EAN13 exclusivo para evitar problemas em processos automáticos, como leitura incorreta por coletores e falhas em validações de movimentação. O limite de caracteres é determinado pela configuração do grupo de campo 030.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24762520449559) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como configura o codigo **EAN13** no **SIGAACD**?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

O código **EAN13** deve ser informado no sistema através do campo `B1_CODBAR` (localizado na rotina **MATA010 – Cadastro de Produto**). O preenchimento segue a seguinte regra, considerando que o tamanho maximo do campo esteja configurado como 13

* O usuário deve digitar **12 caracteres.**
* O **13º dígito é calculado automaticamente pelo sistema**, com base no algoritmo de validação **EAN**, também conhecido como **dígito verificador**.

Esse código identifica **unicamente a unidade do produto**. Portanto, recomenda-se fortemente que **cada produto possua um EAN13 exclusivo**, evitando reutilizações. O uso do mesmo código EAN para produtos distintos pode comprometer processos automáticos no módulo **SIGAACD**, como:

* Leitura incorreta de produtos por coletores;
* Falhas em validações de movimentação;
* Divergência em inventários ou entradas automatizadas.

A capacidade de armazenamento do tamanho do B1\_CODBAR está diretamente ligada à configuração do **grupo de campo 030**. O tamanho máximo configurado nesse grupo determina o limite de caracteres permitidos.

* Exemplo: se o grupo de campo 030 estiver configurado com **tamanho 13**, isso significa que:

  + Apenas **12 caracteres** poderão ser preenchidos manualmente.
  + O sistema reservará **1 caractere adicional** para o **dígito verificador (13º dígito do EAN13)**.

**Caso voce tente digitar exatamente 13 caracteres, sera apresentado um HELP na tela:**

* B1\_CODBAR Digite no máximo 12 caracteres, pois o último dígito do código de barras será preenchido automaticamente (dígito verificador).
* Help: Cod Barras | Problema: Valor inválido (Cod Barras)

### **Sobre o campo B1\_CODBAR:**

Código de barras do produto. O último digito do código (digito verificador) será preenchido automaticamente após informar o código de barras. O campo é utilizado pelo módulo SIGAACD.

**Validação padrão do campo:**

```
Funçäo:A010CodBar(M->B1_CODBAR)
```

**Saiba Mais:**  
[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas#:~:text=Saiba%20Mais%3A,Coleta%20de%20Dados)
