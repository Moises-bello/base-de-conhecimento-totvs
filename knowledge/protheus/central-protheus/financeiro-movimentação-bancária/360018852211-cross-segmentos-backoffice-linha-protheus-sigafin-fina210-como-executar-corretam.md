---
article_id: 360018852211
category: Financeiro - Movimentação Bancária
content_hash: 0ae557fbbec5c3b78929dbfd7db2f4c0b5312500a73e12912a14f0444f899dee
fetched_at: '2026-06-28T22:38:19.287606+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  – FINA210 – Como executar
  corretamente a rotina de recálculo de saldos bancários quando possui SA6, SE8 compartilhadas
  e a SE5 exclusiva?
type: support-article
updated_at: '2025-10-24T12:37:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018852211-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA210-Como-executar-corretamente-a-rotina-de-rec%C3%A1lculo-de-saldos-banc%C3%A1rios-quando-possui-SA6-SE8-compartilhadas-e-a-SE5-exclusiva
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33306226579479)** Tempo aproximado para leitura:**00:03:00 min**  
**Dúvida**  
Como executar corretamente a rotina FINA210 recálculo de saldos bancário quando possui SA6, SE8 compartilhadas e a SE5 exclusiva?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA210 - Todas as versões  
  
**Solução:**  
**Estrutura SIGAMAT EEUUFF**

* **EE** = Empresa
* **UU** = Unidade de negócio
* **FF** = Filial

**Exemplo de filiais:**

* 010101 = Empresa 01, Unidade de negócio 01, Filial 01
* 030101 = Empresa 03, Unidade de negócio 01, Filial 01

**Compartilhamento das tabelas:**

* **SA6 (Cadastro de bancos)** = Compartilhado somente por filial
* **SE8** (**Saldo Final Bancário**) Compartilhado somente por filial
* **SE5 (Movimentação bancária)** = Totalmente exclusiva (empresa/unidade/filial)

**Movimentações exemplo:**

* R$ 1.000,00 na filial 010101
* R$ 2.000,00 na filial 030101

**Recálculo de saldos bancários (FINA210)**  
Ao executar o recálculo de saldos para a empresa 030101, é necessário informar o intervalo correto de filiais que compartilham o cadastro de bancos, ou seja, as filiais da mesma empresa e unidade de negócio onde o banco é compartilhado.

**Por exemplo,** o intervalo válido é:  
030101 até 030199 (todas as filiais da empresa 03 e unidade de negócio 01), pois o cadastro de bancos está compartilhado dentro desse intervalo de filiais.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33306275869975)

**Atenção às restrições:**  
Seguindo o exemplo:

Não inserir no campo "Filial de? = 030101 / Filial até? = 03**02**04" , pois essa filial pertence à unidade de negócio **02**, e o compartilhamento do cadastro de banco não ocorre nesse nível.

Não inserir no campo "Filial de? = **01**0101 / Filial até? = 030199", pois essa filial 01 pertence à empresa **01**, e não pertence a empresa 03, o compartilhamento do cadastro de banco não ocorre nesse nível.

**Riscos ao informar intervalos incorretos:**  
Se forem inseridas filiais cujo cadastro de banco não esteja compartilhado no mesmo nível (empresa/unidade/filial), o recálculo poderá gerar valores incorretos na tabela SE8, causando sobreposição ou inconsistências nos saldos bancários.

Caso for necessário executar o recálculo de saldos da empresa **030101**, devemos inserir somente as filiais que estão compartilha o cadastro de banco que no caso são:

0301**01**, 030102, 030103 até a 0301**99,** pois da filial 01 até 99 o banco está compartilhado por filial

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33306226581015)

**A documentação técnica do TDN:**

**Comportamento do Sistema:** Apresenta o saldo das movimentações das filiais segregado por banco/agencia/conta. Não permite multi filial, devido ao saldo bancário ser único e estar compartilhado.  
Importante: As movimentações com mesmo banco/agencia/conta em filiais diferentes, serão acumuladas no saldo bancário (SE8).

Neste cenário, a pergunta "Processa filais?" deve ser sempre utilizada com a opção "SIM" e para as perguntas "Filial De ?" e "Filial Até ? " informar sempre o intervalo de filiais dentro da mesma empresa.  
**Caso contrário, poderá ocorrer sobreposição dos valores referentes aos saldos bancários devido ao compartilhamento das tabelas SA6 e SE8.**

**Saiba mais**  
[FIN0052 - Compartilhamento de tabela para reprocessamento de saldo bancário (FINA210)](https://tdn.totvs.com/pages/releaseview.action?pageId=327323352)
