---
content_hash: db108d0e7e10e7aaa08e324b984860baec821bcd50d66eb009b349c3d4b76add
fetched_at: '2026-06-29T00:11:03.516692+00:00'
page_id: '623893685'
product: rm
source: tdn-rm
title: Parâmetros - Empreendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=623893685
version: 8
---

---

Lista dos parâmetros que determinam o comportamento do processo de simulação de propostas para as unidades de empreendimento.   
Segue a descrição destes:

* **Situação:** ativo ou não. Ativo o empreendimento contabiliza a licença. Idem o campo situação da grid inicial do cadastro de empreendimentos.
* **Estágio da obra:** estágios possíveis da obra. Este cadastro pode ser feito através do menu backend> globais > estágios da obra.
* **Permite parcelas após entrega:** se habilitado permitirá que uma proposta tenha parcelas a vencer após a data de entrega do empreendimento.
* **TMA:** Taxa Mínima de Atratividade ou Taxa de Desconto que será aplicada no cálculo do VPL.
* **Percentual de VPL para aprovação**: por padrão é 100%, indicando que não existe nenhum desconto na comparação do VPL da proposta com a tabela de preços deste empreendimento, ou seja, o VPL da proposta tem que ser igual ou superior o VPL da tabela. Se desejar que todas as propostas feitas, por qualquer usuário do PVI, possa ser aprovada com 2% de desconto sobre o VPL da tabela, então neste campo indicamos 98% que significa que aceita-se uma proposta que seja 98% do VPL da tabela**.**

* **Tipo de cálculo de VPL:** existem duas possibilidades, a primeira e a recomendada para 99% dos casos é o tipo BRUTO, que indica que o cálculo do VPL será realizado com o valor declarado na tabela de preço. O tipo LIQUIDO, elimina do calculo do VPL o valor da comissão para depois fazer o VPL (sugerimos não usar este tipo LIQUIDO pois este parâmetro será eliminado do sistema em versões futuras).
* **Unidades por linha no bloco:** este parâmetro deve ser preenchido somente se o PVI não conseguir dividir corretamente e de forma automática as unidades por andar. Sendo assim aqui deve-se colocar quantas unidades por andar existem ou quantas unidades por andar deseja demonstrar.
* **Blocos lado a lado:** idem ao parâmetro acima só deve ser preenchido se o PVI não conseguiu dividir os blocos corretamente na tela. Normalmente preenchido quando um empreendimento possui vários blocos e a quebra das unidades por andar está comprometida na tela, então pode-se quebrar que deseja ver 3 blocos lado a lado na tela, determinando esta quebra de visão da tela.
* **Dias de vencimento parcelas:** pode-se determinar os dias que deseja que as parcelas negociadas nas propostas tenham de vencimento, exemplo: 5,10,15.
* **Período de retenção da reserva:** quantas horas as reservas feitas neste empreendimento duram. Se não preenchido usa o parâmetro global  (backend>parâmetros).
* **Período de retenção da reserva (em proposta):** quantas horas as propostas feitas neste empreendimento duram. Se não preenchido usa o parâmetro global  (backend>parâmetros).
* **Visão de vagas de garagem:** Define a exibição ou não da descrição e quantidade nos campos relacionados às vagas de garagem. Este parâmetro é aplicado tanto no mapa de disponibilidade quanto na tabela de preços.
* **URL Youtube:** url de vídeo no youtube sobre o empreendimento.
* **Ocultar data de entrega:** Não mostra a data de entrega no quadro do empreendimento.
* **Quantidade de propostas simultâneas por unidade:** opção não utilizada, será descontinuada.
* **Ocultar coluna de data no plano de pagamento:** elimina a coluna data na impressão do plano de pagamento.
* **Cálculo de desconto da comissão:** forma de desconto da comissão quando paga pelo cliente, decrescente (retira tudo valor possível na ordem decrescente dos componentes), proporcional (realiza regra de proporcionalidade para descontar o valor da comissão dos componentes que participam do calculo), parcelas iguais (divide igualmente o valor da comissão entre os componentes de onde se desconta a comissão).
* **Permite reservas:** se marcado este empreendimento permite reservas.
* **Permite propostas:** se marcado este empreendimento permite propostas **.**
* **Ordem de disposição do mapa de disponibilidade:** opção valida somente quando se possui uma imagem de disponibilidade do empreendimento. Neste podemos definir o que aparecerá primeiro a imagem ou o mapa construído pelo portal.
* **Avisar a obrigatoriedade de parcelas mensais simulação:** quando marcado, exibirá mensagem quando o plano de pagamento proposto não possuir parcelas consecutivas mensalmente. Mensagem apenas informativa. Não impedirá de realizar a proposta.
* **Mostrar preço inicial das unidades na página de empreendimentos:** no frontend no menu empreendimentos, demonstrará ao lado de cada imagem do empreendimento o preço inicial das unidades deste.
