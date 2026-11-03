---
content_hash: 75106166614aa77ab3ca3cf99b65f371aaeb98e48565b29f2c2c36887d9812b3
fetched_at: '2026-06-29T00:11:22.000925+00:00'
page_id: '698286898'
product: rm
source: tdn-rm
title: Excluir / Cancelar bolsas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=698286898
version: 29
---

---

O Assistente para exclusão ou cancelamento de bolsas de contratos permite selecionar os contratos dos alunos que terão bolsas excluídas ou canceladas do período letivo informado. O processo permite a seleção de alunos por registro acadêmico, consulta sql ou filtro. 

Após adicionar os alunos é possível identificar os contratos correspondentes ao período letivo informado. A partir disso, é possível definir quais contratos estarão no processo de exclusão ou cancelamento de bolsas. 

Uma vez que os contratos estejam adicionados, basta selecionar as bolsas e os serviços correspondentes que serão excluídas ou canceladas do contrato dos alunos.

Avançando para a última etapa do processo, temos as opções para que as bolsas selecionadas sejam excluídas ou canceladas. **Obs.**: Também temos esse processo dentro do contrato do aluno em *Anexo |* *Bolsas |* *Processos | Excluir/Cancelar bolsas.*

* Caso realize o procedimento de excluir, as bolsas serão excluídas do contrato dos alunos e as bolsas utilizadas em lançamentos ou contabilizações não serão excluídas.
* Caso realize o procedimento de cancelar, as bolsas serão canceladas do contrato dos alunos e os lançamentos anteriores ao cancelamento das bolsas não sofrerão alterações.

Caso deseje realizar os procedimentos de excluir ou incluir bolsas que já foram utilizadas na geração de contabilização por competência o processo irá se comportamento da seguinte forma:

* Não será possível realizar o procedimento de exclusão de bolsas que possuam contabilização por competência. O processo exibirá a seguinte mensagem "*Não foi possível excluir a bolsa  '4 - GRUPO BMG', do contrato '661'. Bolsa já utilizada na geração de lançamentos do contrato ou na contabilização por competência"*

* Caso realize o procedimento de cancelamento de bolsa onde a bolsa foi contabilizada em lançamentos e competências anteriores, o sistema permitirá a cancelamento e fechará o valor da bolsa até o momento do cancelamento, gerando um estorno de cancelamento no contrato. Além disso, o sistema permitirá contabilizar os períodos após o cancelamento da bolsa

*O cancelamento de bolsa com contabilização por competência está disponível a partir das versões 12.1.2205 apenas o modelo de contabilização novo revitalizado*

**Exemplo de cancelamento de bolsa com contabilização por competência:**

A contabilização irá se comportar da seguinte forma no cancelamento de bolsas que já foram utilizadas na geração de contabilização por competência. Temos um cenário onde o contrato está no valor de R$ 12.000,00 e possui uma bolsa de 50% totalizando R$ 6.000,00 com contabilizações até o mês 5 das 12 competências. Ao gerar o cancelamento após a contabilização da bolsa do mês 5, será gerado um estorno de cancelamento no valor de R$ 3.500,00 na contabilização do contrato do aluno. Além disso, o sistema irá permitir a contabilização das competências seguintes desconsiderando a bolsa cancelada.
