---
article_id: 32109932224151
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: dfe94332ef1256c6344fcc538cc9ed9d17ac31b1ad7124113fa6523d5a324147
fetched_at: '2026-06-28T22:42:02.441213+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Registros C195 e C197 via Configurador de Tributos (FISA170)
type: support-article
updated_at: '2025-05-14T20:36:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32109932224151-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registros-C195-e-C197-via-Configurador-de-Tributos-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32109957079319) Tempo aproximado para leitura: 00:05:00 min**Dúvida**Como gerar os registros **C195** e **C197** via **Configurador de Tributos** (**FISA170**)?  
  
**Ambiente**

Cross Segmentos - TOTVS BackOffice (Linha Protheus) - A partir da versão **12.1.2310**

**Solução**

Para iniciar a configuração de códigos de lançamentos via **FISA170** é necessário que exista cadastrado o **Perfil do Produto, Perfil de Operação, Perfil de Participante, Perfil de Origem/Destino** e todas as regras de cálculo de tributos conforme a necessidade fiscal da empresa.

Ao possuir os cadastros, realize os seguintes passos:

**1**. Acesse a aba "**Regra de Ajustes de Lançamento**"  
**2**. Na aba "**Cadastro de Mensagem**" configure a mensagem que deverá apresentar no registro **C195:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109957085335)

**3**. Acesse a aba abaixo "**Regra de Ajuste de Lançamento**" e inclua um cadastro com os seguintes itens:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109957085975)

ABA 1 - **Lançamento**:

**Tabela de Lançamento** = Tabela 5.3

**Código de Lançamento** = Código que deverá gerar no registro **C197**

**Inicio da vigência** = data de inicio do código de lançamento

**Regra Tributária** = Regra criada pelo usuário de acordo com a necessidade Fiscal

**Tipo de Mensagem** = Período, nota ou item

**Operação** = Entrada, saída ou Devolução

**UF da operação** = Origem ou Destino.

ABA 2 - **Valores**:

Base

Alíquota

Valor

Valor Outros

ABA 3  - **Mensagens**:

**Código Mensagem de Complemento** = Alimente com a mensagem desejada (todos os campos)

Após esse procedimento, salve a **FISA170** e escriture o documento que deverá gerar esses registros **C195/C197**; Na aba "**Lançamento de Apuração**" deverá apresentar o código que configurou na rotina anterior:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109957087895)

A partir deste momento, salve a nota e gere o arquivo do **Sped Fiscal**, segue apresentação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32109957093399)

O procedimento completo poderá ser consultado com o anexo abaixo:
