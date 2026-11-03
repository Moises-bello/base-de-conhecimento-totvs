---
content_hash: 4947aaa15233b98cab9fa01f741ebbd1615f917148e6606b2d6263b0fbeffaa0
fetched_at: '2026-06-29T00:12:00.129342+00:00'
page_id: '880063153'
product: rm
source: tdn-rm
title: Editar atividade ofertada
type: documentation
url: https://tdn.totvs.com/display/LRM/Editar+atividade+ofertada
version: 8
---

##### Esta documentação detalha o processo de edição de uma atividade ofertada na qual um aluno foi inscrito, incluindo as validações necessárias para garantir a consistência dos dados.

---

### **Descrição Geral**

A edição de uma atividade ofertada permite a atualização de informações relacionadas a datas, carga horária, créditos, e outros dados específicos da oferta. Entretanto, algumas dessas atualizações estão sujeitas a validações de prazo, especialmente para preservar a integridade do período de inscrição.

### Campos Sujeitos a Validações

Certos campos acionam validações relacionadas ao período de inscrição quando editados:

* Data de Início
* Data de Fim
* Carga Horária (CH)
* Créditos

Quando um desses campos é editado, o sistema verifica se a edição está sendo realizada dentro do período de inscrição da atividade. A lógica subjacente é que, ao modificar esses dados, o usuário está alterando informações fundamentais da atividade, e tais mudanças não devem ser permitidas fora do prazo de inscrição.

Para realizar essas edições, o usuário deve **primeiramente ajustar o período de inscrição para que inclua a data atual.** Isso garantirá que o sistema permita a edição dos campos mencionados.

### Campos Sem Restrição de Validação de Período

Os campos a seguir podem ser editados a qualquer momento, mesmo após o término do período de inscrição:

* CH Aproveitada:  
    Este campo representa a carga horária aproveitada da atividade e impacta diretamente a análise curricular do aluno.
* Data de Conclusão:   
  Indica a data em que a atividade foi concluída.
* Inscrição confirmada:  
  Indica que a inscrição do aluno foi confirmada.
* Cumpriu atividade:  
  Indica que de fato o aluno cumpriu a atividade e também irá impactar na análise curricular do aluno.
* Documentação entregue:  
  Indica que o aluno entregou a documentação necessária para a atividade.

Esses campos são independentes das validações do período de inscrição e podem ser atualizados sem restrições, pois refletem informações de aproveitamento e conclusão, que não influenciam diretamente a oferta ou o período de inscrição.

### Impacto na Análise Curricular

As alterações realizadas no campo CH Aproveitada são refletidas diretamente na análise curricular do aluno, afetando o histórico de aproveitamento acadêmico. Portanto, qualquer modificação deve ser realizada com atenção, pois influencia o registro curricular.
