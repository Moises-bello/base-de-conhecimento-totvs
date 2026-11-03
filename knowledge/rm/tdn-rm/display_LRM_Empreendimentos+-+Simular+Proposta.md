---
content_hash: 7f8ab7d7504231b5ece0403f6adc839327f66014e0b05929180d1c0faa46f8b4
fetched_at: '2026-06-29T00:10:51.635392+00:00'
page_id: '569486351'
product: rm
source: tdn-rm
title: Empreendimentos - Simular Proposta
type: documentation
url: https://tdn.totvs.com/display/LRM/Empreendimentos+-+Simular+Proposta
version: 40
---

---

A opção "Simular Proposta" é uma funcionalidade que serve para auxiliar corretores e potenciais compradores durante o processo de avaliação e planejamento de uma proposta de compra em um empreendimento imobiliário. Ela tem como objetivo fornecer uma estimativa dos valores, condições de pagamento e disponibilidade de unidades, permitindo uma análise prévia antes de efetuar a reserva.  
  
Quando você acessar a opção "Simular Proposta", como corretor, será necessário seguir os seguintes passos:

1. Selecione a tabela de venda: Escolha a tabela de venda adequada para a proposta que você está simulando. Essa tabela define os preços, condições de pagamento e outras informações relacionadas às unidades disponíveis.
2. Escolha a subunidade: Após selecionar a tabela de venda, você precisará escolher a subunidade específica na qual deseja reservar a proposta. Isso envolve identificar a unidade desejada dentro do empreendimento, levando em consideração características como localização, metragem, disposição e outros aspectos relevantes.

Ao seguir esses passos, você poderá simular uma proposta com base na tabela de venda selecionada e reservar a subunidade escolhida. Essa funcionalidade proporciona uma experiência mais ágil e eficiente para realizar simulações e reservas de propostas dentro do empreendimento.

**Importante:** Ao salvar a simulação de proposta, o Portal de Imóveis irá respeitar o [parâmetro](https://tdn.totvs.com/display/LRM/PVI+-+Backend+-+Globais+-+Componentes+de+Venda) de percentual máximo retido de comissão definido no componente.

Caso a comissão esteja sendo paga pelo cliente, ao enviar o contrato para o backoffice, estes valores retidos serão respeitados na geração do plano de financiamento.

O processo de retenção de comissão ao enviar o contrato para o backoffice só irá ocorrer se a comissão for paga pelo cliente. Para a comissão paga pela empresa não há alteração ao enviar o contrato.

No exemplo abaixo, temos um componente definido com o seu percentual retido máximo de apenas 1%:

Além disso, quando a comissão é **paga pelo cliente**, o valor calculado da comissão será exibida por parcela, quando se visualiza o plano de pagamento na visão de proposta do Portal de Imóveis.

Estes valores também serão mostrados caso o corretor imprima o plano de pagamento.

Neste caso temos um Sinal, de R$ 10,000 onde 1% é o máximo retido da comissão. Veja que o Portal de Imóveis mostra em vermelho que os valores da comissão, neste caso equivalem a R$ 100,00 (1%):

Esta proposta foi salva e a comissão está sendo paga pelo cliente:

No menu de Comissão da proposta, o sistema irá exibir o valor da comissão de acordo com este percentual definido.

O valor desta comissão, com seu percentual máximo definido (1%) é enviado ao RM ao salvar a venda:

## **Incluindo um representante Legal em uma proposta.**

---

Um representante legal em uma proposta imobiliária é uma pessoa autorizada por um comprador ou vendedor de imóveis para agir em seu nome durante a negociação e a transação imobiliária.

Esse representante legal pode ser um advogado, um agente imobiliário ou outro profissional qualificado. Sua função é garantir que todas as transações sejam feitas de forma legal e transparente, garantindo assim que seus clientes estejam protegidos em todos os aspectos do processo.

O representante legal pode ajudar na elaboração e revisão de contratos, garantir que todas as cláusulas e requisitos legais sejam atendidos, facilitar a comunicação entre as partes envolvidas e assegurar que o processo de compra ou venda seja concluído de forma adequada e dentro do prazo estabelecido.

Ao realizar a simulação de um contrato, será apresnetado no cadastro a opção: Mostrar dados adcionais, ao clicar nesta opção (logo abaixo ainda na mesma página será apresentada uma opção para inclusão de um representante legal.  
OBS: esta opção **(representante legal)** será apresentada apenas quando for selecionado o tipo de proponente Pessoa Jurídica ***(conforme exemplo abaixo).***

Na opção novo (ao ser selecionada) basta preencher os dados do representante legal, de acordo com os campos disponibilizados no cadastro. Em seguida após validar a proposta (basta salvar a mesma para inclusão no sistema.

Observação sobre Visualizar o Empreendimento.

Obrigatório o preenchimento de Tipo de Imóvel - Topologia e Região.
