---
content_hash: 0ee8359c6a17853b74ab86f8ea8b200ef639162954cb8b275acd72612168ce09
fetched_at: '2026-06-29T00:09:49.152540+00:00'
page_id: '435105244'
product: rm
source: tdn-rm
title: Novidades 12.1.21 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105244
version: 3
---

**Novidades 12.1.21**   
**Vendas**  
**Contabilização de Lançamento Padrão pela FRU - Protheus e Aglutinação**  
Processo de contabilização dos lançamentos acessórios e Aglutinação Protheus [Clique aqui e veja com utilizar o processo.](http://tdn.totvs.com/pages/viewpage.action?pageId=379305796)  
**Listagem Plano de Financiamento controlando compôs da visão**  
Foi criado um parâmetro nas configurações do Portal PDC no TIN para que os dados financeiros da venda na tela do Plano financeiro fiquem ocultos. ( Valor Financeiro Atualizado , Saldo Devedor e Valor Total Pago.  
**Ferramenta de diagnóstico da Integração Protheus**  
Foi criado uma ferramenta no RM com o objetivo de verificar divergências entre a integração Protheus e RM TIN, por exemplo, quando houver títulos baixados no Protheus e o seu lançamento correspondente no RM estiver em aberto ou parcialmente baixado, é possível realizar a correção dessa inconsistência pela ferramenta de diagnóstico.  
Foi criado no Menu Utilitários um botão para utilizar o cockpit do TIN. Para mais informações, acesse: Cockpit TIN  
**Permitir escolher o tipo de Documento do Componente**  
Será possível a partir desta versão escolher qual o tipo de documento cada componente gerador de parcela terá. Os dados serão buscados automaticamente do empreendimento ou dos parâmetros do Tipo de Parcela, porém na geração do plano de financiamento da venda, será possível alterar esse tipo de documento, tanto a pagar quanto a receber.  
**Criar uma venda a partir de outra**  
Foi implementado um novo processo para gerar uma nova venda a partir de uma venda já existente. Este processo irá copiar toda a regra, datas e parametrizações para uma nova venda com uma nova subunidade e tabela de preço.   
**Contabilizar o aditivo de troca de subunidade**  
Desenvolvemos a funcionalidade de contabilizar o aditivo de troca de subunidade, com o objetivo de facilitar toda a operação da apuração pelo POC. Para essa funcionalidade foi criada a tabela default "Subunidade Anterior" e " Subunidade" nos itens do evento contábil, de onde pode ser buscado os valores da contabilização.  
**Log dos cálculos do SPED EFD**  
A geração do SPED EFD do TIN agora possui um log para consulta dos valores gerados. Este log possui os valores calculados de cada parcela de acordo com as parametrizações do Empreendimento e a participação do parceiro. Após a execução do processo, o log será salvo automaticamente na pasta RM.Net\Log\_SPED. Essa melhoria ficará disponível a partir da versão 12.1.18.  
**Bloqueio de alteração das contas gerenciais das subunidades**  
Após a realização do POC, ou de gerar uma venda para uma subunidade, não será mais possível realizar a troca de uma conta gerencial da subunidade. Esta evolução foi realizada para garantir que os cálculos e contabilizações da apurações sejam realizadas corretamente.  
   
   
**Aluguel**   
**Cadastro de Registro do Imóvel**  
No cadastro de Imóveis na aba Identificação, foi incluído o campo de Cartório para identificar o cartório onde o registro do imóvel foi realizado  
**Tratar a deflação no reajuste do aluguel**  
O sistema agora possibilita o reajuste com ou sem a deflação para os Contratos de Locação no Módulo de Aluguéis.  
**Anexo de Matrículas no Cadastro de Imóveis**  
No Cadastro de Imóveis, foi criado o anexo de Matrículas do Imóvel para realização do cadastro de uma ou mais matrículas vinculadas ao imóvel.  
**Histórico de Áreas dos Imóveis**  
Foi criado o Histórico de Áreas dos Imóveis. Esse histórico será preenchido quando houver alteração nos campos do cadastro da área do imóvel.   
**Anexo de Inscrição Municipal**  
No cadastro de Imóveis, foi criado um anexo para a inclusão de Inscrição Municipal.  
**Cadastro de Prefeitura no Imóvel**  
Foi incluído no Cadastro de Imóveis na aba Identificação (Módulo de Aluguéis), um campo para informar a Prefeitura que é cadastrado em Gestão Financeira/ Cliente/Fornecedor.  
**Aluguel em Dobro**  
Foi implementado o processo de geração de Aluguel em Dobro para determinados meses. Para a execução desse processo é necessário inserir os parâmetros através do cadastro Aluguel em Dobro, anexo do Contrato de Locação. Assim como determinar o Valor de Integração a ser utilizado nos Parâmetros do TOTVS Incorporação. O Aluguel em Dobro será gerado juntamente com o processo de Geração de Lançamentos do Contrato de Locação.   
**Campo Cap Rate (Parâmetros de Aluguel)**  
Foi criado o campo Cap Rate nos parâmetros de Aluguel. Este campo será utilizado para calcular o valor mensal de aluguel baseado no valor de venda do imóvel.  
**Geração de Imóveis a partir de Subunidades 1**  
Foi criado o processo para geração de Imóveis a partir de Subunidades. Este processo estará presente nos cadastros de Empreendimento, Unidades e Subunidades.  
**Geração de Imóveis a partir de Subunidades 2**  
O processo de **Gerar imóve(is) para aluguel** foi aprimorado, e agora envia também as características da subunidade para o imóvel gerado.  
**Geração de Imóveis a partir de Subunidades 3**  
O processo de **Gerar imóve(is) para aluguel** foi aprimorado, e agora caso o endereço da subunidade não esteja preenchido, o sistema irá criar o imóvel com o endereço do empreendimento.  
**Aditivo de Alteração de Aluguel em Dobro**  
Foi criado o Aditivo de Alteração de Aluguel em Dobro, que provem os recursos necessários para executar tais alterações em contratos que possuem Aluguel em Dobro.  
**Anexo de Lançamentos Financeiros no Contrato de Locação**  
Foi criado o anexo de Lançamentos Financeiros para o Contrato de Locação, possibilitando aos usuários realizar todos os processos importantes para a Gestão Financeira, através da própria tela de Contrato de Locação.  
**Memória de Cálculo na Geração do Aluguel Complementar**  
Foi criada a Memória de Cálculo na Geração do Aluguel Complementar, que mostra todo o detalhamento do cálculo realizado.  
**Melhoria no Aluguel Complementar**  
Feita melhoria no processo de Efetivação de Escalonamento, quando existe Aluguel Complementar no mesmo período.   
**Campo Taxa de Participação no Faturamento**  
Na tela de Contrato de Locação aba Parâmetros de Aluguel Complementar, foi criado o campo **% Taxa de Participação no Faturamento**, que possibilita o usuário informar um percentual que o imóvel representa em relação ao todo da loja alugada.  
**Campo Modelo de Cálculo no Contrato de Locação**  
Na aba Identificação do Contrato de Locação foi criado o campo **Modelo de Cálculo**, onde o usuário pode definir se utilizará o Pro Rata para Aditivos e Escalonamentos nas operações realizadas dentro do contrato.  
**Parâmetro Usar a opção "Utiliza Cálculo Pro Rata" como default no campo "Modelo de cálculo" do Contrato**  
Foi criado o parâmetro de aluguel **Usar a opção "Utiliza Cálculo Pro Rata" como default no campo "Modelo de cálculo" do Contrato**, que será um default para o campo **Modelo de Cálculo** localizado na aba identificação do Contrato de Locação.  
**Campo Classificação de Condomínios (Administradoras)**  
No cadastro de Condomínios (Administradoras) foi criado o campo de Classificação.  
**Rateio de Valor Fixo**  
Foi aprimorado o Rateio de Valor Fixo para imóveis que possuem o Tipo de Locação "Áreas Unificadas". O sistema agora irá permitir que seja feito o cálculo do fechamento por Valor Fixo para imóveis com esse Tipo de Locação.  
**Importações via Conceito (Módulo de Integração)**  
Foi disponibilizado o recurso de Importação via Conceito dos cadastros do TIN. As importações disponíveis no momento são:

* Importação de Locatários - Importação de Locadores - Importação de Beneficiários - Importação de Fiadores - Importação de Administradores de Condomínio - Importação de Procuradores - Importação de Imóveis - Importação de Contratos de Administração - Importação de Eventos Financeiros Avulsos - Importação de Contratos de Locação  
  **Dois lançamentos para o mesmo período**  
  Foi disponibilizado a opção de gerar dois lançamentos financeiros em um período de Locação. Para realizar essa parametrização é necessário alterar a regra de vencimento, para maiores informações clique aqui    
  **Novas Funções de Fórmula criadas para o TIN:**  
  **Função ALGCAMPOCOMPLCONTRATOLOC**  
  Foi criada a função de fórmula ALGCAMPOCOMPLCONTRATOLOC que retorna os valores dos campos complementares do contrato de locação.  
  **Função COMPETENCIAALGCOMPLEMENTAR**  
  Retorna a competência que está sendo processada na geração de aluguel complementar. Se for processado fora do contexto, irá retornar a data atual.  
  **Função VALORBASEALUGUEL**  
  Retorna o valor Base da Competência informada como parâmetro.  
  **Função FATURAMENTOALGCOMPLEMENTARVALOR**  
  Retorna o valor do Faturamento da Competência informada como parâmetro.  
  **Função PERCENTUALFATURAMENTOALGCOMPLEMENTAR**  
  Retorna o percentual (Conforme faturamento) da Competência informada como parâmetro.  
  **Medições - Aluguel Complementar**  
  O rótulo do campo "Valor do aluguel na competência" foi modificado para "Valor do aluguel utilizado no cálculo" e passa a ser preenchido (automaticamente) somente no momento do cálculo do aluguel complementar (ao executar o processo "Gerar Aluguel Complementar" selecionando a medição em questão). Esta alteração se faz necessária porque atualmente existem vários processos que podem alterar o valor do aluguel na competência (escalonamento, aluguel em dobro, reajuste, aditivos...) e os mesmos podem ocorrer entre o cadastro da medição e a geração do aluguel complementar, sendo assim este processo precisará obter o valor correto mais atualizado para realizar este cálculo. Para mais informações sobre medições clique aqui  
  **Condomínio**   
  **Considerar despesas anteriores no fechamento**  
  A partir da versão 12.1.21, o processo de Calcular Fechamento agora passa a considerar as despesas de períodos anteriores que não tenham sido calculadas ou integradas no fechamento de sua competência. Todas as despesas em aberto anteriores à competência do fechamento devem ser consideradas.  
  **Processo Associar Tarifa**  
  A partir da versão 12.1.21, foi implementado o processo de Associar Tarifa. Este processo tem o objetivo de facilitar a associação de tarifa a um ou mais medidores. Para maiores informações sobre o processo clique aqui
