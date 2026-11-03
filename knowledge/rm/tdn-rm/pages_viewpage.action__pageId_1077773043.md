---
content_hash: a8a5fa43e0a4dba76b5bcd63d2f9cc000efb047b5d85cf935c86fcf57f5b1122
fetched_at: '2026-06-29T00:05:54.277266+00:00'
page_id: '1077773043'
product: rm
source: tdn-rm
title: PI - Integração - RD Station - Time Line/Dados Externos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077773043
version: 2
---

Para que a Time Line possa ser apresentada e atualizada na edição de um Lead, estes dados são originados a partir do momento em que as informações são preenchidas na TIMELINE na edição do Lead.

Já os dados externos são originados a partir das informações inseridas neste registro através da Integração com o RD Station.

Acompanhamento de Engajamento e Negociações na Tela de Pessoas (Versão 12.1.2606+)

Para que o corretor entenda todo o contexto do Lead antes de uma venda, a visão de "Pessoas" no Portal de Imóveis foi evoluída para exibir dados em tempo real do RD Marketing e CRM.

**Como visualizar:** Ao abrir o cadastro de um Prospect, desde que as integrações estejam ativas, duas novas caixas aparecerão na lateral direita:

* **RDStation Marketing (Botão Lead):** Exibe informações de captação, origem da oportunidade, etapa do funil e campos customizados respondidos pelo cliente.
* **RDStation CRM (Botão Negociações):** Mostra as negociações em andamento, status, previsão de fechamento e as anotações do corretor feitas diretamente no RD, centralizando o histórico.

**Simulação de Proposta Direto da Negociação (A partir da versão 12.1.2606)**

Para tornar o processo de vendas ainda mais ágil, o corretor pode iniciar a simulação de uma proposta diretamente do modal de "Negociações (RD Station CRM)".

Ao abrir as negociações de um cliente na tela de Pessoas, um botão **"Simular"** estará disponível dentro de cada card de negociação.

**Como realizar a simulação:**

1. No Portal de Imóveis, acesse o menu de **Pessoas** e abra o cadastro do cliente desejado.
2. No menu lateral direito, localize o quadro "RDStation CRM" e clique no botão **Negociações**.
3. O sistema abrirá uma janela com os *cards* de todas as negociações ativas desse cliente. Localize a negociação que deseja evoluir para uma venda e clique no botão **Simular**.
4. **Redirecionamento Inteligente:** O sistema utilizará a informação de "Empreendimento Procurado" daquela negociação e abrirá automaticamente o **Mapa de Disponibilidade** do empreendimento correto.
5. No mapa, selecione a unidade e o bloco desejados e clique novamente no botão **Simular**.

**O que acontece a seguir:**

* **Preenchimento Automático:** Você será redirecionado para a tela de "Preencher Proposta". O cliente (comprador) já virá preenchido e a negociação do RD CRM já estará vinculada, a mesma selecionada por você na tela de pessoas.
* **Cálculo Automático (Plano Padrão):** Se o empreendimento selecionado possuir um plano de financiamento padrão (default), a proposta será aberta **já salva e com o plano de pagamento totalmente calculado**, eliminando a necessidade de montar as parcelas manualmente.

  *(Nota: caso o empreendimento não possua um plano padrão, a aba de condições de pagamento abrirá em branco para preenchimento manual).*

  **Como configurar o Plano Padrão (Modalidade) no TOTVS RM:**

  **Passo a passo no RM:**

  1. Acesse o módulo Gestão de Imóveis e vá até a aba **Venda**.
  2. Clique no ícone **Empreendimento.**
  3. Na lista, selecione o empreendimento desejado e clique em **Editar** (ícone de lápis).
  4. Na tela de edição, olhe o menu lateral esquerdo. Dentro do grupo **Dados Gerais**, clique na opção **Informações**.
  5. Localize o campo **Modalidade** e clique no botão de busca (`...`) ao lado dele.
  6. A janela de "Modalidade de Venda" será aberta. Selecione qual será a modalidade padrão e clique em OK.
  7. Salve o cadastro do empreendimento.

  ---
* **Sincronização de Campos:** Ao salvar a proposta, os campos personalizados configurados para o RD Station (como Bloco, Unidade, Valor e Situação) são preenchidos e sincronizados com o CRM de forma automática.
