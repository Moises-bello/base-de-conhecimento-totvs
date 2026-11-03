---
content_hash: d8108fa842ccfdbdfa9254dc126c5389e1380d39c4c9493e2c1175132d7b578d
fetched_at: '2026-06-29T00:09:36.182911+00:00'
page_id: '425459478'
product: rm
source: tdn-rm
title: Alocação de salas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459478
version: 6
---

Este processo consiste na alocação de salas para turmas/disciplinas disponíveis em um mesmo período letivo.   
 De acordo com os horários elas serão alocadas conforme configuração da prioridade, disponibilidades e outras parametrizações do processo. A alocação das salas pode ser feita manual ou automaticamente.  
    
 É possível definir a prioridade pela habilitação e pelos blocos.   
 O curso de Medicina tem prioridade sob o curso de Sistemas de Informação, ao passo que, dentro do curso de Medicina é possível definir que o Bloco 1 terá prioridade de alocação sob o bloco 2.  
    
 Veja o seguinte exemplo:

|  |  |  |
| --- | --- | --- |
| **Campus:** Raja Gabaglia | | **Prioridades das Habilitações** |
| **Prédio:** Raja Top | |
| Bloco 1 | Sala 1 | Direito |
| Sala 2 |
| Sala 3 |
| Bloco 2 | Sala 4 | Engenharia Civil |
| Sala 5 |
| Sala 6 |

| **Turma** | **Turma/Disciplina** | **Dia / Horário** |
| --- | --- | --- |
| Turma  Y Curso: Direito | A | Segunda (19:00 - 20:40) |
| B | Segunda (19:00 - 20:40) |
| C | Segunda (19:00 - 19:50) |
| Turma X Curso: Engenharia Civil | D | Terça (19:00 - 20:40) |
| E | Quarta (19:00 - 20:40) |
| F | Quinta (19:00 - 19:50) |

***Observação****: os cursos possuem apenas estas prioridades e todas as salas estão disponíveis. Veja que as turmas do curso de direito possuem o mesmo dia e horário. Já as turmas do curso de Engenharia Civil possuem horários distintos.*  
 Quando é executado o processo de alocação automática, é esperado que o sistema aloque as turmas/disciplinas e seus horários da seguinte forma:

|  |  |  |  |
| --- | --- | --- | --- |
| **Turma** | **Turma/Disciplina** | **Dia / Horário** | **Bloco/Sala** |
| Turma  Y Curso: Direito | A | Segunda (19:00 - 20:40) | Bloco 1 - Sala 1 |
| B | Segunda (19:00 - 20:40) | Bloco 1 - Sala 2 |
| C | Segunda (19:00 - 19:50) | Bloco 1 - Sala 3 |
| **Turma** | **Turma/Disciplina** | **Dia / Horário** | **Bloco/Sala** |
| Turma  Y Curso: Engenharia | A | Terça (19:00 - 20:40) | Bloco 2 - Sala 4 |
| B | Quarta (19:00 - 20:40) | Bloco 2 - Sala 4 |
| C | Quinta (19:00 - 19:50) | Bloco 2 - Sala 4 |

As turmas do curso de Direito foram alocadas em salas distintas devido à incompatibilidade de horários e as turmas do curso de Engenharia Civil foram alocadas na mesma sala por que possuem horários distintos. Restando, ainda, as salas 5 e 6 do bloco 2 para serem alocadas para outras turmas/disciplinas.  
 O processo realizado, manualmente, permite que o usuário defina o próprio destino das turmas/disciplinas.  
    
 Considerações importantes:

* Este processo se aplica ao nível de ensino básico e superior.
* Devem existir horários nas turmas/disciplinas a serem alocadas e, além disso, salas disponíveis.
* Para que a alocação automática seja realizada é obrigatório o cadastro das prioridades.

Veja Também

---

[Blocos](http://tdn.totvs.com/x/kf1bGQ)
