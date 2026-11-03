---
article_id: 4436320923799
category: Materiais - Compras (SIGACOM)
content_hash: 2e0bafbe981990309eb652b543fe794bbd113ae3586e522adc0fdc2bcc290279
fetched_at: '2026-06-28T22:41:22.058762+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Parâmetros (F12) Documento
  de Entrada
type: support-article
updated_at: '2024-12-03T17:47:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4436320923799-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Par%C3%A2metros-F12-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28245340084759) Tempo aproximado para leitura: **00:30:00 min** **Dúvida**Qual a funcionalidade dos parâmetros (F12) no Documento de Entrada?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

**Ao teclar será exibida a tela de perguntas padrão da rotina de Documento de Entrada (Grupo de Perguntas **MTA103** da Tabela **SX1**). O grupo de perguntas **MTA103** tem a finalidade de alterar o comportamento de determinados processos na rotina. A seguir detalharemos a funcionalidade de cada pergunta.**

**1. Mostra Lançamentos Contábeis?**

Considera a visualização dos itens com lançamentos contábeis. Opção utilizada para exibir a tela de contabilização ao confirmar a inclusão do Documento de Entrada.

Obs.: Opção válida apenas para contabilização on-line.

**2. Aglutina Lançamentos?**

Indica se deve ou não aglutinar os lançamentos contábeis.

Obs.: Opção válida apenas para contabilização on-line.

**3. Verifica Cotação?**

Pergunta temporariamente desabilitada no sistema. Não utilizar.

**4. Aplicar Reajuste?**

Indica se deve aplicar o reajuste dos Pedidos na Entrada das Notas Fiscais, baseado na fórmula do Pedido **(C7\_REAJUST).** Opção utilizada para aplicar a fórmula informada no campo **C7\_REAJUST**, no cálculo dos valores unitário **(D1\_VUNIT**) e total **(D1\_TOTAL)** no momento da importação de itens do Pedido de Compras para o Documento de entrada.

**5. Incluir Amarração?**

Considera a amarração do produto ao fornecedor. Opção utilizada para atualizar os registros das tabelas **SA5** (Amarração Produto x Fornecedor) e **SAD** (Amarração Grupo x Fornecedor). Ao incluir um Documento de Entrada, do tipo Normal com produtos que não possuem amarração os registros serão criados.

Obs.: A pergunta só será considerada em inclusão de documentos com o tipo normal.

Dica: Utilize essa opção em conjunto com as perguntas 12 e 15.

**6. Lançamento Contábil On-Line?**

Informa se deve gerar os lançamentos contábeis on-line.

Dica: Utilize essa opção em conjunto com as perguntas 1 e 2.

**7. Quanto ao PC?**

Indica se na busca do Pedido de Compras, através dos botões ou teclas de atalho, deve ser considerado somente o código do fornecedor ou o código e a loja. Opção utilizada para vincular ao Documento de Entrada um ou mais Pedido(s) de Compras do mesmo fornecedor, mas de uma loja diferente da loja informada no Documento de Entrada.

**8. Operação Triangular?**

Considera as operações triangulares para notas de beneficiamento: Cliente > Forn1 > Forn2 > Cliente.

Opção utilizada para permitir a alteração do fornecedor na devolução de documento de poder de terceiros. Por padrão o fornecedor do documento de devolução deve ser o mesmo do documento de origem. Apenas em operações triangulares deve-se permitir a alteração o fornecedor.

**9. Quebra do rodapé?**

Considera a quebra do rodapé por alíquota ou imposto. Opção utilizada no folder de impostos no rodapé do Documento de Entrada.

**10. Ultimo preço com desconto?**

Atualiza o último preço de compra deduzindo o desconto ou não. Opção utilizada para considerar o valor de desconto na atualização dos campos **B1\_UPRC/BZ\_UPRC** (Último preço de compra), no momento da gravação do Documento de Entrada.

Obs.: Os campos serão atualizados somente se o Documento de Entrada for do tipo Normal ou Complemento de Preço/Frete e o campo **F4\_UPRC** (Atualiza Preço de Compra) estiver configurado para permitir a atualização.

Dica: Utilize o ponto de Entrada **MT103UPC** para customizar a gravação dos campos **B1\_UPRC/BZ\_UPRC.**

Dica 2: Utilize essa opção em conjunto com a pergunta 11.

**11. Atualiza ultimo preço por?**

Ao atualizar o último preço de compra considerar o preço por data de recebimento ou por data de emissão. Opção utilizada na gravação dos campos **B1\_UCOM/BZ\_UCOM** (Data da última compra). Caso o usuário opte por considerar a data de recebimento, será gravado o conteúdo do campo D1\_DTDIGIT (Data de Digitação), caso o usuário opte por considerar a data de emissão, será gravado o conteúdo do campo 1\_Emissão (Data de Emissão).

Obs.: Os campos serão atualizados somente se o Documento de Entrada for do tipo Normal ou Complemento de Preço/Frete e o campo F4\_UPRC (Atualiza Preço de Compra) estiver configurado para permitir a atualização.

Dica: Utilize essa opção em conjunto com a pergunta 10.

**12. Atualiza amarração?**

Informe se ao incluir o Documento de Entrada os dados da amarração Produto x Fornecedor devem ser atualizados. Opção utilizada para atualização dos dados de compra na tabela SA5. Serão atualizados os seguintes campos: **A5\_DTCOMXX** (Data da compra XX), **A5\_PRECOXX** (Preço da compra XX), A5\_QUANTXX (Quantidade da compra XX), A5\_CONDXX (Condição de pagamento da compra XX).

Dica: Utilize essa opção em conjunto com as perguntas 5 e 15.

**13. Rateia Valor?**

Indica o valor a ser utilizado no rateio de múltiplas naturezas: Bruto (Valor do título somado aos impostos) ou Líquido (Valor do título sem os impostos). Opção utilizada para gravação do campo **EV\_VALOR** (Valor da Movimentação). Caso utilizada a opção “Bruto”, serão considerados os valores dos seguintes impostos: **PIS (E2\_PIS), COFINS (E2\_COFINS), CSLL (E2\_CSLL).**

Dica: Utilize essa opção em conjunto com a pergunta 14.

**14. Gera Rateio?**

Se utilizada opção de Múltiplas Naturezas, indica se gera o rateio por naturezas também para os títulos dos impostos.

Obs.: Pergunta só será valida se utilizada a opção “Bruto” na pergunta 13 “Rateio Valor?”

Dica: Utilize essa opção em conjunto com a pergunta 13.

**15. Amarração Produto x Fornecedor?**

Fornecedor por código completo do produto ou pelo código da família, referência de grade, na consulta de pedido de compras (Opção utilizada apenas para clientes que utilizam o template de Drogaria).

Obs.: No padrão a pergunta será utilizada da seguinte forma: Caso a pergunta 5 “Incluir Amarração?” esteja configurada com a opção “sim”, também será gravado o campo **A5\_DESREF** (Descrição referência de Grade) na atualização da tabela **SA5**.

Dica: Utilize essa opção em conjunto com as perguntas 5 e 12.

**16. NF de Bonificação?**

Indica que o Documento de Entrada poderá ser carregado de um Pedido de Compras do fornecedor e dos fabricantes associados pela amarração Produto x Fornecedor.

Obs.: Opção utilizada apenas para clientes que utilizam o template de Drogaria.

Dica: Utilize essa opção em conjunto com a pergunta 15.

**17. Bloqueia Movimento?**

Pergunta utilizada para bloquear as movimentações de integração com outros módulos. Caso a resposta seja configurada como “Sim” não serão geradas as movimentações de Estoque, Financeiro e Fiscal.

Obs. 1: Opção válida apenas para documentos que utilizam formulário próprio.

Obs. 2: É possível realizar a transmissão da nota com bloqueio de movimentos e emissão do DANFE.

Obs. 3: Para o desbloqueio da nota e geração dos registros nos Livros Fiscais, Estoque e Financeiro é necessário realizar a classificação da nota.

Obs. 4: No momento da classificação, para as notas transmitidas, não será possível realizar alterações no item e no cabeçalho, assim como nas abas Impostos, Descontos/Fretes/Despesas e Livros Fiscais.

Obs. 5: Esta implementação foi realizada com exclusividade no processo em que o Documento de Entrada tem origem pelo módulo de Compras. Em documentos manuais de entrada (Livros Fiscais), este tratamento não está disponível.

**18. Gera Título de ICMS por Antecipação Tributária?**

Informe se deverá ser gerado o título a pagar do **ICMS** por Antecipação Tributária.

Dica: Utilize essa opção em conjunto com a pergunta 19.

**19. Guia de Recolhimento de ICMS por Antecipação?**

Informe se deverá ser gerada uma guia de recolhimento do **ICMS** por Antecipação Tributária. O Sistema irá apresentar uma tela para que as informações necessárias a geração da guia sejam preenchidas.

Dica: Utilize essa opção em conjunto com a pergunta 18.

**20. Gera Título de ICMS ST por Transporte?**

Informe se deverá ser gerado o título a pagar do ICMS-ST por transporte.

Dica.: Utilize essa opção em conjunto com a pergunta 21.

**21. Guia de ICMS ST por Transporte?**

Informe se deverá ser gerada a guia a pagar do ICMS-ST por transporte.

Dica.: Utilize essa opção em conjunto com a pergunta 20.

**22. Replica Tipos de Operação?**

Habilita o preenchimento automático de tipos de operação no processo de entrada. Opção utilizada para preenchimento automático do campo **D1\_OPER** (Tipo de Operação) na classificação de uma prenota. Se a resposta da pergunta for configurada com o conteúdo “Sim”, ao informar o tipo de operação de um item, no momento da classificação de um documento, a informação será replicada para os itens seguintes.

Obs.: Opção disponível apenas para operação de Classificação.

Dica: Para validar e alterar as respostas do usuário utilize o ponto de entrada **MT103SX1**. O ponto será executado ao sair da tela de perguntas.

23. Gera Título PIS/COFINS Importação?

24. Gera Título ISS Importação?

25. Antecipação Parcial – BA ?

26. Gera ICMS Antecipação Separado?

27. Gera Título FASE-MT?

***Saiba Mais:***

[SIGACOM - Alçada de Solicitação de Compras por Entidade Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Al%C3%A7ada-de-Solicita%C3%A7%C3%A3o-de-Compras-por-Entidade-Cont%C3%A1bil)  
[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)  
[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
