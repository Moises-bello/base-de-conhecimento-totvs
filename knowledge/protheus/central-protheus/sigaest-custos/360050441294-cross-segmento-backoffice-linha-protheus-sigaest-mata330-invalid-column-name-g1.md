---
article_id: 360050441294
category: SIGAEST - CUSTOS
content_hash: 7db558dd2346e35a4f0a90f6c194e2869bb5093df5cba851ab4e13550ef29cf8
fetched_at: '2026-06-28T22:39:02.176406+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Invalid
  Column Name G1_FILPROC
type: support-article
updated_at: '2025-03-12T12:17:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050441294-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Invalid-Column-Name-G1-FILPROC
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30503860859159)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao executar a rotina de Recálculo do Custo Médio ou instalar as Procedures de Custos, gera-se o error.log **"Invalid column name 'G1\_FILPROC"**. O que fazer para resolver?

**Ambiente**Protheus – Estoque/Custos – A partir da versão 11.1.17

**Solução**

É importante salientar que o campo **G1\_FILPROC** é temporário por isso não tem na tabela **SX3**, nem no Configurador.

Porém, caso este contenha este campo na SX3 ou no banco de dados (isso causa o problema), efetue os procedimentos a seguir:

- Realizar um backup da tabela SG1;

- Dropar a tabela SG1;

- Deletar o campo G1\_FILPROC na SX3;

- Acessar à rotina MATA200 (para recriar a tabela SG1 sem o campo G1\_FILPROC);

- Importar (realizar append) do backup na tabela SG1;

- reinstale as Procedures 19 e 20

- Executar o Recálculo do Custo Médio com parâmetros "**Gerar Estrutura pela Movimentação = Sim**" e "**Recalcula Nível de Estrutura = Sim**".

**OBS:** Executar os processos em um momento fora do fluxo de trabalho para não gerar problemas na operação, recomendamos fortemente que faça o procedimento fora do horário de expediente dos usuários.

**Procedimento alternativo**

- Desinstale as Procedures 19 e 20;  
- Verifique no seu APSDU se possui a tabela TRBXXSPSG1, igual o exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077270694)

- Faça um backup dessa tabela;  
- Dropar essa tabela;  
- Execute o Recálculo do Custo Médio com os parâmetros "Gerar Estrutura pela Movimentação = Sim" e "Recalcula Nível de Estrutura = SIM".

Após isso, reinstale novamente as procedures 19 e 20

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)
