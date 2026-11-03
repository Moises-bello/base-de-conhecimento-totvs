---
article_id: 360021142512
category: Controle de Documentos (SIGAQDO)
content_hash: cb4e0f4f8ea333a577087a898175597e50f50e800a0f4ed09909eb10da11307c
fetched_at: '2026-06-28T22:42:29.236701+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Pendências não são baixadas no SIGAQDO
type: support-article
updated_at: '2021-09-08T12:58:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021142512-Manufatura-Linha-Protheus-SIGAQDO-Pend%C3%AAncias-n%C3%A3o-s%C3%A3o-baixadas-no-SIGAQDO
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao acessar a rotina **QDOA030 - Pendências** e baixar uma pendência, após a atualização da tela, a mesma permanece pendente para o usuário. O que pode ser feito para **baixar a pendência**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Em geral, esta situação ocorre quando as pendências em questão estão em duplicidade na tabela **QD1 - Distribuição por usuário**. A duplicidade pode ocorrer após a transferência do usuário de departamento, quando não foi feita a transferência das pendências dele para ele mesmo no novo departamento.   
  
Para solucionar, deverá ser feito o ajuste via banco de dados:  
  
Através do **APSDU**, realize um filtro na tabela **QD1** pelo documento em questão e verifique se existe alguma linha com o campo **QD1\_PENDEN=P** para o usuário que não está conseguindo baixar a pendência. Verifique se existe uma pendência baixada e uma pendência não baixada na tabela **QD1** para o mesmo documento.   
  
Caso após a verificação acima não identificar pendência em duplicidade, será necessário também comparar os campos de departamento e cargo das tabelas **QAA - Usuários e QD1.**Para que o Sistema funcione corretamente os campos devem estar iguais, isto é, com o mesmo conteúdo e mesmo tamanho, conforme linhas abaixo:

* **Código do departamento: QAA\_CC = QD1\_DEPTO**
* **Código da função: QAA\_CODFUN = QD1\_CARGO**
* **Matrícula: QAA\_MAT = QD1\_MAT**
* **Código da filial: QAA\_FILIAL = QD1\_FILMAT**
