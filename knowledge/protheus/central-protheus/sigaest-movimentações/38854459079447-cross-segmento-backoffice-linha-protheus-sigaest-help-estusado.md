---
article_id: 38854459079447
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 570be0ebb8c5756a91a77650abe2aedf561d3e52b59004fc081de697c8be7143
fetched_at: '2026-06-28T22:38:55.575316+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP ESTUSADO
type: support-article
updated_at: '2026-03-06T16:34:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38854459079447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-ESTUSADO
---

Ao tentar incluir uma Nota Fiscal de entrada no TOTVS Protheus, pode ocorrer o HELP ESTUSADO devido a campos essenciais (como lote, grade ou segunda unidade de medida) estarem desabilitados no dicionário de dados (SX3). Para resolver, é necessário habilitar o uso desses campos no módulo Configurador (SIGACFG) em Base de Dados Dicionário SD1. Após a alteração, reinicie a rotina para aplicar as mudanças.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38854433923735) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Ao tentar incluir uma Nota Fiscal, o sistema interrompe o processamento e apresenta o help **ESTUSADO**.

**Mensagem de Exemplo:**

> *"O Produto XPTOP possui controle de rastreabilidade e o campo Lote (XX\_CAMPO), esta desabilitado o USO! para prosseguir, habilitar o uso na base de dados no configurador!"*

![helpestusad.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38854459070359)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Para prosseguir, habilitar o uso na base de dados no configurador, sobre o campo mencionado no HELP.

### **Causa Raiz**

A função interna realiza uma validação de integridade entre as **características do Produto** (Cadastro SB1) e a **estrutura do Dicionário de Dados** (SX3) da tabela de Itens da **Nota Fiscal de Entrada (SD1).**

O HELP ocorre quando o produto exige um controle específico (Lote, Grade ou Segunda Unidade de Medida), mas os campos necessários para informar esses dados estão marcados como **"Não Usado"** (propriedade `X3_USADO` = .F.) no Configurador.

O sistema identifica três cenários de bloqueio:

#### **Cenário A: Controle de Rastreabilidade (Lote)**

* **Condição:** O produto possui controle de Rastreabilidade/Lote ativo.
* **Erro:** O sistema verifica que um ou mais dos seguintes campos estão desabilitados na SD1:

  + `D1_LOTECTL` (Lote Controle)
  + `D1_LOTEFOR` (Lote Fornecedor)
  + `D1_NUMLOTE` (Sub-Lote)
  + `D1_DTVALID` (Data de Validade)

#### **Cenário B: Controle de Grade**

* **Condição:** O produto utiliza Grade de Produtos.
* **Erro:** O sistema verifica que os campos de grade estão desabilitados na SD1:

  + `D1_GRADE` (Código de Grade)
  + `D1_ITEMGRD` (Item de Grade)

#### **Cenário C: Segunda Unidade de Medida**

* **Condição:** O produto possui Segunda Unidade de Medida configurada (`B1_SEGUM` preenchido e `B1_CONV` maior que zero).
* **Erro:** O sistema verifica que os campos de conversão estão desabilitados na SD1:

  + `D1_SEGUM` (Segunda Unidade de Medida)
  + `D1_QTSEGUM` (Quantidade na 2ª UM)

Para corrigir essa inconsistência, é necessário habilitar o uso do campo mencionado na mensagem de erro através do módulo **Configurador (SIGACFG)**.

1. Acesse o módulo **Configurador (SIGACFG)**.
2. Vá em **Base de Dados > Dicionário > Base de Dados**.
3. Selecione **Dicionário de Dados**.
4. Pesquise pela tabela **SD1 - Itens das Notas Fiscais de Entrada**.
5. Clique em **Editar** e localize o campo mencionado na mensagem de erro (Ex: `D1_LOTECTL`).
6. Edite o campo e vá para a aba **Uso**.
7. Marque a caixa de seleção **"Usado"** (para que o campo fique disponível na tela e no banco de dados).
8. Salve as alterações e confirme a atualização da base de dados.

> **Importante:** Após realizar a alteração no dicionário, é necessário sair e entrar novamente na rotina para que as alterações surtam efeito.

---

#### **Fiz o processo mas o HELP persiste?**

* Valide se voce possui algum ponto de entrada que possa estar interferindo e desative:
* Gere uma Pilha de chamadas com o HELP em tela e envie para o suporte, juntamente com o ID da central, bem como um print dos campos na SX3 ou anexe a SX3 dos campos contidos no boletim em formato SQLITE para avaliação e analise do suporte padrão.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como enviar dados pela Central de Diagnóstico?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33711098138007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-enviar-dados-pela-Central-de-Diagn%C3%B3stico)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O que fazer quando aparecer um HELP na rotina?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33992870078615-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-O-que-fazer-quando-aparecer-um-HELP-na-rotina)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Saldos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033462-SIGAEST-SALDOS)
