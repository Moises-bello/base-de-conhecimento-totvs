---
article_id: 360017498572
category: SIGAACD - Automação e Coleta de Dados
content_hash: 9c2538351903e99ba02234f9724f4a96b9e7411f0eda8d67222f77da0646137a
fetched_at: '2026-06-28T22:39:11.057636+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD  Como configurar o EAN14
  no SIGAACD?
type: support-article
updated_at: '2026-06-24T20:48:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017498572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-configurar-o-EAN14-no-SIGAACD
---

No SIGAACD, o EAN14 é configurado na rotina Complemento de Produto (MATA180), vinculando o código de produto a até oito Operadores Logísticos, cada um com uma quantidade específica. O código EAN13 deve ser cadastrado com 12 caracteres mais o dígito verificador (total 13). O primeiro dígito do EAN14 representa o operador logístico e a quantidade configurada. O processo funciona apenas no ACD padrão, não no app Meu Coletor de Dados.

**Dúvida**  
Como configurar o ***EAN14*** no SIGAACD? Quais sao os tipos de codigo de barras permitido?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

 - Veja também no vídeo abaixo, um exemplo do processo simulado:

***- Passo a passo  abaixo:***

Primeiramente o Código EAN13 é informado no campo ***Código de Barras (B1\_CODBAR)*** no Cadastro de Produto digitando **12 caracteres**, o sistema tem um gatilho que faz o preenchimento automático do **13º caractere**.

Exemplo: **123456789012-8** o último caractere foi complementado pelo próprio sistema quando cadastramos o produto. No print de exemplo abaixo, 12 caracteres mais 1 digito verificador. Totalizando 13 caracteres.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13058693025559)

Agora o ***EAN14*** será configurado na rotina **Complemento de Produto (MATA180)**. Aqui você terá a possibilidade de amarrar o código de produto a oito (8) Operadores Logísticos. Assim terá oito opções para informar como será composto o seu ***EAN14***.

**Dica:** Utilize o [***MV\_CADPROD***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068032-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utilidade-e-configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CADPROD) para facilitar o acesso a MATA180 diretamente pela rotina MATA010 incluindo a tabela SB5 nesse parâmetro.

Os campos de configuração são eles;

**- B5\_EAN141**

**- B5\_EAN142**

**- B5\_EAN143**

**- B5\_EAN144**

**- B5\_EAN145**

**- B5\_EAN146**

**- B5\_EAN147**

**- B5\_EAN148**

Em cada operador logístico ***informe o saldo*** correspondente para o ***EAN14***. Veja exemplo abaixo:

**- B5\_EAN141** **= qtd. 5**

**- B5\_EAN142** **= qtd. 10**

**- B5\_EAN143** **= qtd. 15**

**- B5\_EAN144** **= qtd. 20**

**- B5\_EAN145** **= qtd. 25**

**- B5\_EAN146** **= qtd. 30**

**- B5\_EAN147** **= qtd. 35**

**- B5\_EAN148** **= qtd. 40**

Observe que ao final do código de cada campo tem uma representação da posição do Operador Logístico. Então, ao informar no coletor que irá usar o ***EAN14 de qtd. 5*** no **1º digito** colocar o operador logístico que o representa.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/13059002304663)

**Exemplo simulado abaixo:** Entre no coletor e faça uma movimentação Interna de Devolução. Digite o código do produto 1-123456789012- 8 , **observe que o primeiro caractere representa o campo** ***EAN14*** com a **quantidade 5** e os **13 últimos são compostos do EAN13**. Exemplo simulado no coletor abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13059378704791)

No coletor, ao digitar como exemplificado acima: **11234567890128** na tela apresenta a quantidade padrão 1, mas ao confirmar a **movimentação será de** ***5***, obedecendo o cadastro do **campo B5\_EAN141**.

 - **B5\_EAN142** de **qtde 10**, basta informar no primeiro caráter o número 2, veja: **2****1234567890128**.

 - **B5\_EAN143** de **qtde 15**, basta informar no primeiro caráter o número 3, veja: **3****1234567890128**.

 - **B5\_EAN144** de **qtde 20**, basta informar no primeiro caráter o número 4, veja: **4****1234567890128**.

 - **B5\_EAN145** de **qtde 25**, basta informar no primeiro caráter o número 5, veja: **5****1234567890128**.

 - E assim para os demais.

***Observação importante:*** Ao criar o código de barras no campo **B1\_CODBAR**, é necessário utilizar o **tamanho 12** mais o dígito verificador, que totaliza **tamanho 13**. Caso, utilizar um tamanho diferente de 13, não conseguirá utilizar a funcionalidade do EAN14. Apresenta o help de **Etiqueta Invalida**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13060194292887)

**OBS:** Processo funciona somente no ACD padrão(Emulador/Coletor físico) e não via app Meu Coletor de Dados.

***Saiba Mais:***  
[*Clique aqui e veja mais artigos sobre o módulo SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017498572/preview/eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MzYwMDE3NDk4NTcyLCJleHAiOjE2Nzg3MzQ5NzN9.TiaFwHli6haWXaeQkUGagxeLmg_dX2xufhmov32ozTQ)
