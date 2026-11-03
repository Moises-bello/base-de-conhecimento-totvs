---
content_hash: 3e48212914524ae323f9d03d7b6ef6fcc83fd15c26c105ad7a89e74c9a233716
fetched_at: '2026-06-29T00:10:10.553592+00:00'
page_id: '452719873'
product: rm
source: tdn-rm
title: Iniciar Processo de Seleção/Executar Triagem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719873
version: 2
---

**Iniciar Processo de Seleção/Executar Triagem**

A finalidade deste processo é aplicar a triagem vinculada ao perfil de vaga na seleção e encontrar as pessoas que atendam.

**Observação:**

Este processo somente será executado na primeira etapa da seleção. E após a realização da triagem, todos os candidatos encontrados pela triagem serão salvos no cadastro de candidatos do perfil de vaga.

**Candidatos internos:**

Pessoas da base (PPESSOA) que possuam registro na tabela de candidatos como funcionário (VCANDIDATOS com a coluna FUNCIONARIO = 1 e que na tabela de funcionário (PFUNC) possua no mínimo um registro com o código de situação (CODSITUACAO) igual a 'A' ou 'F'.

Neste caso o registro da PFUNC deverá ter também o tipo de funcionário que esteja na seguinte lista:

Diretor (D), Estatutário (E), Cedido (I), Misto (M), Normal (N), Comissionista (O), Rural (R), Expatriado (X) e Aprendiz (Z).

**Candidatos Externos:**

Pessoas da base (PPESSOA) que possuam registro na tabela de candidatos como candidato (VCANDIDATOS com a coluna FUNCIONARIO = 0 e que não possua um registro como funcionário (PFUNC), ou se caso possuir esteja todos com a situação igual a 'D'.

- Pessoas da base (PPESSOA) que possuam registro na tabela de candidatos como funcionários (VCANDIDATOS com a coluna FUNCIONARIO = 1 e que na tabela de funcionário (PFUNC) possua registro com o código de situação (CODSITUACAO) igual a 'A' ou 'F'. Neste caso o registro da PFUNC deverá ter também o tipo de funcionário que esteja na seguinte lista:

Autônomo (A), Temporário com redução de encargos (B), Conselheiro (C), Temporário/Comissionista (F), Temporário (P), Pensionista (S), Estagiário (T) e Outros (U).  
   
**Observações sobre a triagem de candidatos:**

* Para etapas NÃO iniciadas e SEM triagem associada, usuário terá duas opções de triagem:  
                        Triar todos os candidatos possíveis e iniciar a seleção com os candidatos triados;  
                        Não triar nenhum candidato e iniciar a seleção.
* Para etapas NÃO iniciadas e COM triagem associada, usuário terá duas opções de triagem:  
                        A seleção será dada como iniciada e os candidatos serão incluídos;  
                        A seleção será dada como iniciada sem nenhum candidato.
* Para etapas iniciadas e SEM triagem associada, usuário terá duas opções de triagem:  
                        Marcar o campo "Manter os candidatos já inscritos";  
                        Desmarcar o campo "Manter os candidatos já inscritos".  
  Sendo que as condições abaixo também serão consideradas:  
                        Triar todos os candidatos possíveis e iniciar a seleção com os candidatos triados;   
                        Não triar nenhum candidato e iniciar a seleção.
* Para etapas iniciadas e COM triagem associada, usuário terá duas opções de triagem:  
                        Marcar o campo "Manter os candidatos já inscritos": sistema irá manter os candidatos já inscritos e caso a triagem retorne mais candidatos, os mesmos serão adicionados à vaga;   
                        Desmarcar o campo "Manter os candidatos já inscritos": sistema exclui todos os candidatos da vaga e insere apenas os novos candidatos triados.  
  Sendo que as condições abaixo também serão consideradas:  
                        A seleção será dada como iniciada e os candidatos serão incluídos;  
                        A seleção será dada como iniciada sem nenhum candidato  
     
  Maiores informações sobre triagem, consultar o help Triagem.
