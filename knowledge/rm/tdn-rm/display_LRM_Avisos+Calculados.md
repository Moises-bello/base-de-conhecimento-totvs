---
content_hash: db8a4b9a561b71101af4f2c8c9ef6a5f5ba1b7b90d70cb98167ea41662e4bcf7
fetched_at: '2026-06-29T00:10:03.181641+00:00'
page_id: '452719042'
product: rm
source: tdn-rm
title: Avisos Calculados
type: documentation
url: https://tdn.totvs.com/display/LRM/Avisos+Calculados
version: 11
---

**Avisos Calculados**

---

Os **avisos calculados** são gerados sempre que o sistema identifica alguma **inconsistência na jornada de trabalho**. Essas inconsistências podem ocorrer, por exemplo, por **falta de marcações de ponto (batidas)** ou por qualquer outra situação que **impeça o cálculo correto da jornada** de um funcionário.

Além disso, os avisos também têm a função de **alertar sobre situações que possam gerar problemas legais**, conforme previsto na **CLT**, como o **não cumprimento do tempo mínimo entre jornadas (interjornada)**.

De forma geral, esses avisos ajudam o usuário a **identificar e corrigir eventuais erros ou irregularidades** nas marcações de ponto, afastamentos, férias ou inatividade, garantindo que os cálculos e registros fiquem corretos e dentro das normas legais.

**Tipos de avisos calculados**

---

**1**             Tempo Mínimo Entre Jornadas (Inter jornada): Alerta quanto ao cumprimento de horas de Inter jornada parametrizado em Sindicato | Etapa 1 - Horários. ...   
**2**            Horas trabalhadas superior a 10 horas : Alerta quanto aos dias com execução de carga horária superior a 10 horas....  
**3**            Menos que 1 hora de Refeição : Alerta quanto aos dias em que não foram cumpridas pelo menos uma hora de refeição. Este tipo de aviso é especifico para horários onde há o   registro de ausência planejada como os horários flexíveis.  
**4**             Horas trabalhadas sem intervalo de Refeição: Alerta quanto aos dias em que não foram efetuadas batidas de refeição.  
**5**             Batidas sem Pares correspondentes: Alerta para dias em que as batidas efetuadas não contenham paridade.  
**6**             Funcionário Afastado : Alerta quando o funcionário está com situação de afastamento.  
**7**             Funcionário de férias: Alerta quando o funcionário está com situação de férias.  
**8**             Funcionário Inativo: Alerta quando o funcionário está inativo.  
**9**             Tempo menor que o mínimo do intervalo com tempo planejado: Alerta quanto ao tempo executado de planejado é menor que o mínimo definido no horário.  
**10**           Semana não possui 24 horas contínuas de descanso: Alerta quando na definição do horário existe descanso menores que 24 horas e/ou descansos não contínuos. Essa validação é feita de acordo com o horário e não com as batidas efetuadas. Maiores informações veja em: [Aviso Calculado - Descanso Noturno](https://tdn.totvs.com/pages/viewpage.action?pageId=900731347). O sistema passou a não gerar o tipo de aviso 10, **após a demissão do funcionário**.

**Validação dos Avisos Calculados**

---

A validação é a etapa em que o usuário confirma, corrige ou desconsidera os avisos apresentados pelo sistema, garantindo a precisão dos dados de ponto.

Após o aviso ser validado e o recálculo da jornada ser executado, o aviso é removido automaticamente da tela.

* **Importante**: Se o recálculo for executado novamente, o aviso será recriado com validação igual a 0, voltando a aparecer como não validado.

Esse processo assegura que o controle de ponto permaneça sempre atualizado, coerente e em conformidade com a legislação, além de facilitar futuras conferências e evitar inconsistências no sistema.
