---
article_id: 23235092437143
category: SIGAACD - Automação e Coleta de Dados
content_hash: db9bb32e049c5fd0897d1b4bcc22148da71e60eb5a27876da308a2254bc62ee0
fetched_at: '2026-06-28T22:39:13.795269+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Quando estorno a ordem
  de separação por OP, deveria também estornar o Movimento RE0 gerado dessa OP?
type: support-article
updated_at: '2024-05-03T17:04:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23235092437143-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Quando-estorno-a-ordem-de-separa%C3%A7%C3%A3o-por-OP-deveria-tamb%C3%A9m-estornar-o-Movimento-RE0-gerado-dessa-OP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23235092425623) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Quando faço uma Ordem de Separação po OP e requisito esse Material, e desfaço a separação deveria também estornar o movimento **RE0** gerado?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Em um cenário onde:

1. Crio um produto Matéria Prima (MP) e Produto Acabado (PA);

2. Cadastro um Saldo Inicial ao MP criado;

3. Cadastro uma Estrutura 1:1 do Produto Acabado e Matéria Prima.

4. Gera-se uma Ordem de Produção do PA e em seguida gera os empenhos corretamente na tabela **SD4**.

5. Na rotina Ordem de Separação, gera-se uma O.S por OP.

6. Via emulador **VT100** do **ACD**, separo a Ordem de Separação por OP, e requisito o material gerando um movimento interno na rotina **MATA241**.

7. Continuando no emulador VT100, desfaço a separação, deletando os registros da tabela **CB8** e **CB9** daquele produto.

8. Na rotina Ordem de Separação, clicando em  "Outras Ações" > "Estornar", o processo do estorno da Ordem de Separação por OP termina nesse processo, sem que haja o estorno do Movimento Interno de requisição do passo 6.

**Este cenário é um erro?**

O fato do Estorno da Ordem de Separação (ACDA100) após desfazê-la, não estornar o movimento interno, é considerado conceito, pois a opção "Requisita material", gera uma execução automática do movimento interno. O estorno da Ordem de Separação, gera apenas o estorno dela (e suas tabelas (CB8 e CB9). Para deletar o Movimento Interno gerado é necessário acessar à rotina Movimento Interno (**MATA241**), clicar em "Outras Ações" -> Estornar.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
