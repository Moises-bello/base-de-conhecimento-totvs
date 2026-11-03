---
content_hash: cfb8766df1ecc2d756f0d02c99e665a98fadebf6046e9ac9ab4bfe81b7637e2a
fetched_at: '2026-06-29T00:09:14.957890+00:00'
page_id: '421385318'
product: rm
source: tdn-rm
title: Detalhamento de Itens Contratados
type: documentation
url: https://tdn.totvs.com/display/LRM/Detalhamento+de+Itens+Contratados
version: 7
---

---

O Detalhamento de Itens é aplicado apenas em contratos do tipo à PAGAR, e pedidos de material que geram movimentos à pagar.    
Existe um anexo fixo na parte inferior da tela de associação de itens para exibição dos insumos, onde serão exibidos todos os insumos que são recursos da tarefa (item do contrato) conforme os insumos presentes na curva ABC. Este anexo será incluído dentro do processo de "Associação de itens ao contrato".

Importante:

Ao vincular os itens ao contrato, se ele estiver associado a uma ou mais tarefas do tipo Serviço, a classificação do item será preenchida automaticamente como ''Contrato Previsto'', assim como acontece em contratos gerados a partir da licitação e no processo "Gerar Contrato a partir do Movimento".

Informações técnicas: A tabela preenchida é a MITMCNT campo CLASSIFICACAO.

    
Caso o usuário marcar para o campo "Rateio automático dos produtos associados" o processo irá ratear os produtos de acordo com os valores informados no detalhamento da tarefa. A quantidade contratada de cada insumo, recurso do item associado pode ser informada das seguintes formas: Manualmente: a quantidade é inserida através da célula da grid de detalhamento de itens. Ao inserir o valor manualmente, a flag "Informado Manualmente" será habilitada.  
**Pela opção "Associação percentual dos insumos":** a quantidade contratada de cada insumo selecionado será definida pela expressão:  
   
**Quantidade Contratada=% de associação\*Quantidade orçada**  
**A partir da quantidade contratada do item (tarefa)**: ao informar a quantidade contratada de um item (tarefa), a quantidade contratada dos insumos recursos da tarefa serão calculados proporcionalmente a quantidade do item. O valor unitário contratado no anexo de detalhamento de itens é um campo informativo para armazenar o valor que um determinado insumo foi contratado em uma tarefa. O valor deste campo não irá interferir no valor contratado do item (tarefa). O valor unitário contratado de cada insumo pode ser informado das seguintes formas:  
**Manualmente:** o valor é inserido através da célula da grid de detalhamento de itens. Ao inserir o valor manualmente, a flag "Informado Manualmente" será habilitada.  
**Ao informar a "Quantidade contratada":** Ao informar a "Quantidade contratada" o campo "Valor unitário orçado" será preenchido com o valor presente no campo "Custo unitário orçado" ou "Valor unitário orçado" conforme a opção selecionada em "Valor a ser associado" ("Custo unitário" ou "Valor unitário").    
**Observação:**  
Ao associar itens ao contrato e o parâmetro de detalhamento de itens estiverem marcado será apresentado a mensagem sobre o cálculo do projeto, onde permitirá que o usuário escolha se deseja calcular o projeto, para realizar a associação de itens ao contrato sem que o sistema calcule o projeto o mesmo deverá estar com o cálculo do projeto atualizado no mínimo de 2 dias. É necessário realizar o cálculo do projeto para atualização dos valores da curva ABC, para que não haja desatualização de valores na hora da associação.

Observação:

Caso tenha alguma medição de tarefa e nenhum item detalhado, a janela de detalhamento não será exibida.  
Caso exista algum detalhamento de item, ela será exibida mesmo com medições de tarefa.
