---
article_id: 360025694974
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 028f14424e5df89e06f3fe0642575301559364fe03d8ebd440da146f0e466395
fetched_at: '2026-06-28T22:38:28.627727+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Poder DE / EM
  Terceiro e considerações importantes
type: support-article
updated_at: '2023-07-24T20:05:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025694974-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Poder-DE-EM-Terceiro-e-considera%C3%A7%C3%B5es-importantes
---

**Dúvida**Qual o conceito e Operações adequadas ao controle automático de Poder DE / EM Terceiro no Protheus e considerações importantes como entidade, retorno simbólico e remessa de comodato.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.  
  
**Solução**

Para entender um pouco mais do conceito de poder DE/EM terceiro veja nosso vídeo **How To**em: [How To | MP - SIGAFAT - Conceito: Poder De/Em Terceiros](https://youtu.be/oS5sdoZBdN8)

O controle de **Poder DE/EM terceiro** no sistema Protheus consiste na gestão automática de um **Saldo Físico** de Produto que se encontra **temporariamente** nas seguintes condições:

* Produto meu **EM** poder de **TERCEIRO** → Produto físico que me pertence mas ficará temporariamente em Poder de um Terceiro (Parceiro).
* Produto **DE TERCEIRO** em meu Poder → Produto físico que pertence ao Terceiro (Parceiro) mas ficará temporariamente em meu Poder.

A gestão automática permite um controle correto dos saldos de Estoque, de modo que a organização tenha disponível a informação de que determinado saldo precisa ser retornado. Essa gestão valida ainda diversos processos que movimentam o Estoque de modo a permitir ou não essa movimentação considerando a operação DE/EM terceiro garantindo assim a integridade do Saldo.

Alguns processos em que a gestão automática do Saldo DE/EM Terceiro se faz essencial são: consignação, conserto, beneficiamento, armazenamento, empréstimo, etc. (os quais abordaremos em detalhes a seguir).

**Considerações Importantes:**

* **Entidade Cliente ou Fornecedor**  
  Cadastro de Cliente OU Fornecedor é uma Classificação específica do Protheus. Para o SEFAZ ambos são considerados como ENTIDADE. Alguns processos no Protheus requerem o cadastro de uma Entidade em ambos os cadastros (Cliente e Fornecedor).
* **Retorno Simbólico**  
  Consiste na emissão de uma Nota para fins de ajuste dos controles internos. Não requer transmissão ao SEFAZ porém é um procedimento que o Fisco aceita.
* **Triangulação / Operação Triangular**  
  Consiste na Devolução de PD3 à uma Entidade diferente da que enviou (Remessa por Fulano, mas Retorno à Ciclano).  
  Para habilitar é necessário acessar os parâmetros via pergunte acionando a tecla F12 dentro das rotinas: Documento de Entrada - MATA103 e Pedidos de Venda - MATA4110

* **Relacionamento entre a Nota de Remessa e a Nota de Faturamento**  
  Essas Notas não se relacionam dentro do SIGAFAT, salvo quando o processo é realizado pela Rotina Contrato de Parceria - FATA400: [Relacionamento entre a Nota de Remessa e a Nota de Venda (Ex. Venda para Entrega Futura)](https://tdn.totvs.com/x/sUNtDQ)
* **Cliente de Entrega diferente**  
  Quando o cliente de Entrega é diferente, é necessário registrar no Pedido de Vendas os campos C5\_CLIENTE (que é o Cliente da Venda) e C5\_CLIENT (que é o Cliente de Entrega).

  No Pedido de Vendas há os campos C5\_CLIENTE (que é o Cliente da Venda) e C5\_CLIENT (que é o Cliente de Entrega).

  - O título (quando configurado para gerar no TES) é gerado para o Cliente da Venda C5\_CLIENTE  
  - A Tributação (quando configurado para gerar no TES) é gerada para o cliente de Entrega C5\_CLIENT  
  - É levado o Cliente da Venda C5\_CLIENTE no destinatário na tag *dest* ; e, o cliente de Entrega C5\_CLIENT na tag *entrega*.  
  - É levado o Cliente de entrega no DANFE quando o cliente da Venda e da Entrega são de estados diferentes (obs: neste caso é possível mencionar no campo C5\_MENNOTA o cliente da Venda também, para que seja mencionado nos dados complementares do Danfe)

* **Nota de remessa de comodato**: Para emitir uma nota de comodato, o que geralmente caracteriza por  um ***empréstimo*** de produto ou bem a terceiros.  Se o cliente é quem está emprestando, o processo que deverá ser efetuado:
  + ***pedido do tipo** **N- normal;***
  + **TES** que controla **poder de terceiros remessa**, movimentação de ***estoque igual a sim*** e ***não gera financeiro***;
  + O retorno do bem se dará através de uma ***nota de entrada do tipo B- benficiamento;***
    - O **TES** deverá controlar **poder de terceiros devolução**, movimentação de ***estoque igual a sim*** e ***não gerar financeiro***.
  + Em caso de cobrança do tempo do empréstimo, deverá emitir um ***pedido do tipo Normal;***
    - **TES** que **não controla poder de terceiros**, **não movimenta estoque** e **só movimenta financeiro.** Mais detalhes e exemplos do processo, acesse a FAQ de Poder DE/EM Terceiro, aba empréstimos.

**Saiba Mais: [Poder DE/EM Terceiro](https://tdn.totvs.com/x/xyCgGg)**
