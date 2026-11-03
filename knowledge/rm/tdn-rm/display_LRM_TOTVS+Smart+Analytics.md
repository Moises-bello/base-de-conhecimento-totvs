---
content_hash: 9c51ebb73d3d7653b288de843dd028de94ce62614972fc44d344c6ac3a962584
fetched_at: '2026-06-29T00:08:14.434756+00:00'
page_id: '244711617'
product: rm
source: tdn-rm
title: TOTVS Smart Analytics
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Smart+Analytics
version: 136
---

O TOTVS Smart Analytics é solução dos produtos TOTVS para extrair dados da base RM, transforma-los e transporta-los para a ferramenta de Business Analytics Gooddata.  
Abaixo, apresentamos a documentação particionada em "Passos" para que seja possível implantar as funcionalidades e localizar informações para "Help".

ImplantacaoExtratoresRM1 - Configurar Ambiente

# 1.1 – Criar uma Base Vazia no Banco de Dados

Sugerimos como nome STAGE. Esse nome será usado em demais passos, e caso definir outro nome, deverá alterar a referencia dessa base nos passos seguintes.  
Conceda permissão de acesso a base criada, para o Administrador do Banco de Dados do RM.

# 1.2 – Ativar Integração

Acesse no módulo Integração: Ferramentas / Configurar  
Informe o usuário e senha do Administrador do Banco de dados.  
Clique em Testar Conexão. Se for bem sucedida, o Botão avançar etapa será habilitado. 

Avance para próxima Etapa.  

# 1.3 – Ativar a Integração e Criar Base Stage

Selecione a integração TOTVS Business Analytics.  
Avance a Etapa.

No campo Diretório Conceitos, informe: C:\totvs\CorporeRM\ObjetosGerenciais\Conceito\Gooddata.  
Os conceitos são recursos de integrações do RM com fontes externas. Para o funcionamento da extração de dados do RM, esses recursos foram utilizados e é primordial realizar a importação de todos os Conceitos atualizados, que estão disponibilizados na pasta de instalação do RM: C:\totvs\CorporeRM\ObjetosGerenciais\Conceito\Gooddata.

Obs.: Os seguintes conceitos relacionados ao segmento Educacional estão obsoletos e devem ser removidos do sistemas (uma vez que a extração de dimensões e fatos do Educacional é feita utilizando arquivos .csv):

* Dimensão - Aluno
* Dimensão - Bolsa de Estudo
* Dimensão - Campus
* Dimensão - Curso Educacional
* Dimensão - Disciplinas
* Dimensão - Grade Curricular
* Dimensão - Habilitação
* Dimensão - Instituição de Ensino
* Dimensão - Nível de Ensino
* Dimensão - Período Letivo
* Dimensão - Professor
* Dimensão - Situação de Matricula
* Dimensão - Turno Aula
* Fato - Educacional - Inadimplência
* Fato - Educacional - Matricula
* Fato - Educacional - Turmas e Professores

Nas opções Banco de Dados BI (destino), informe os dados da base de dados criada (STAGE) e o usuário e senha do banco dados. Clique em Testar conexão.

Ao Avançar a etapa, a estrutura física de tabelas da base será criada na base de dados (STAGE).  
A estrutura da base segue o modelo de informações que serão transportadas para o Gooddata, com tabelas representando Dimensões e Fatos.  
Atenção! Essa estrutura não pode ser alterada via banco de dados. 

2 - Parametrizações para Extração

No Parametrizador, existe o recurso "Salvar Processo Como", que cria o arquivo XML com as parametrizações. O arquivo exportado, poderá ser carregado em qualquer coligada, por meio do recurso "Carregar Processo", localizado também no Parametrizador da integração.  
Atenção: Deverá utilizar a funcionalidade quando os dados das parametrizações da coligada origem forem idênticos na coligada de destino.  
Para localizar os parâmetros abaixo, acesse no módulo Integração: Ferramentas / Parâmetros / 50.08 - TOTVS Business Analytics

ParametrosExtratoresParâmetros Globais

# Totvs Smart Analytics Agent

Para utilização do processo de envio dos dados para o Totvs Smart Analytics é necessário informar os parâmetros para o envio dos dados.

Para isto acesse *menu Integração->Ferramentas-> Parâmetros -> TOTVS Business Analytics*e informe os parâmetros:

* Instância: Campo utilizado para diferencias os dados extraídos de duas ou mais bases RM para uma única Fluig Smart Data. Esse campo é de preenchimento obrigatório, mesmo quando a extração for feita utilizando apenas uma base, e deve conter 2 caracteres (Ex.: 01, 02, 03, 12, 36, etc). Realizar a extração das bases sempre considerando o mesmo período no plano de extração. Ex.: Extraído dados de Janeiro de 2017 da base RM1 então deve ser extraído os dados de Janeiro de 2017 da base RM2. Após realizar a extração das bases os dados podem ser enviados para o GoodData.
* Caminho do Java.exe
* Caminho do Agent
* Caminho do my.properties
* E-mail para envio do log de conclusão do processo de envio dos dados.

Caso seja necessário habilite e informe os parâmetro de *proxy* para o envio dos dados para o Totvs Smart Analytics.

* Url do proxy
* Usuário do proxy
* Senha do proxy
* Porta do proxy

Estes parâmetros serão compartilhados entre todas as coligadas.

* **RH – Faixa Etária**

**Descrição:** Define faixas agrupadoras que serão exibidas no GoodData de acordo com a idade do colaborador na data de extração.

**Fatos em que o parâmetro é utilizado:** Banco de Horas, Folha de Pagamento, Treinamentos Colaboradores, Treinamentos por Tipo de Custo, Vida Profissional

* **RH – Tempo de Casa**

**Descrição:** Define faixas agrupadoras de acordo com a diferença de datas entre a data da extração e a data de admissão do Colaborador.

**Fatos em que o parâmetro é utilizado:** Banco de Horas, Folha de Pagamento, Treinamentos Colaboradores, Treinamentos por Tipo de Custo, Vida Profissional

* **RH – Tempo de Cargo**

**Descrição:** Define faixas agrupadoras de acordo com a diferença de datas entre a data da extração e a data de em que o colaborador assumiu o cargo que ocupa atualmente.

**Fatos em que o parâmetro é utilizado:** Banco de Horas, Folha de Pagamento, Treinamentos Colaboradores, Treinamentos por Tipo de Custo, Vida Profissional

Parâmetros por EmpresaParametrosExtratoresAreasRecursos Humanos

Estes parâmetros deverão ser configurados individualmente para cada coligada.

# 1.1 Parâmetro – Eventos de Proventos do Custo da Folha

**Descrição:** Na coluna da esquerda estarão todos os eventos de Proventos do módulo de Folha de Pagamento, e deverá ser feita a seleção, enviando para o campo da direita “Eventos Selecionados” os eventos que deverão ser considerados na métrica correspondente aos Proventos de Custo da Folha no GoodData.

**Fato em que o parâmetro é utilizado:** Folha de Pagamento

# 1.2 Parâmetro – Eventos de Desconto do Custo da Folha

**Descrição:** Na coluna da esquerda estarão todos os eventos de Desconto do módulo de Folha de Pagamento, e deverá ser feita a seleção, enviando para o campo da direita “Eventos Selecionados” os eventos que deverão ser considerados na métrica correspondente aos Descontos de Custo da Folha no GoodData.

**Fato em que o parâmetro é utilizado:** Folha de Pagamento

# 1.3 Parâmetro – Eventos de Base de Cálculo do Custo da Folha

**Descrição:** Na coluna da esquerda estarão todos os eventos de Base de Cálculo do módulo de Folha de Pagamento, e deverá ser feita a seleção, enviando para o campo da direita “Eventos Selecionados” os eventos que deverão ser considerados na métrica correspondente aos Base de Cálculo de Custo da Folha no GoodData.

**Fato em que o parâmetro é utilizado:** Folha de Pagamento

# 1.4 Parâmetro – Eventos de Hora Trabalhada do Custo da Folha

**Descrição:** Na coluna da esquerda estarão todos os eventos de Provento do módulo de Folha de Pagamento, e deverá ser feita a seleção, enviando para o campo da direita “Eventos Selecionados” os eventos que deverão ser considerados na métrica correspondente à soma de Horas Trabalhadas no Custo da Folha no GoodData.

**Fato em que o parâmetro é utilizado:** Folha de Pagamento

# 1.5 Parâmetro – Eventos de Hora Extra do Custo da Folha

**Descrição:** Na coluna da esquerda estarão todos os eventos de Provento do módulo de Folha de Pagamento, e deverá ser feita a seleção, enviando para o campo da direita “Eventos Selecionados” os eventos que deverão ser considerados na métrica correspondente à soma de Horas Extras no Custo da Folha no GoodData.

**Fato em que o parâmetro é utilizado:** Folha de Pagamento

# 1.6 Parâmetro – Eventos Especiais do Custo da Folha

**Descrição:** Na coluna da esquerda estarão todos os eventos do módulo de Folha de Pagamento, e deverá ser feita a seleção, enviando para o campo da direita “Eventos Selecionados” os eventos que não são recorrentes no pagamento da folha e que pode ser parametrizado de forma personalizada a critério do cliente com o que for considerado custo especial. Exemplos: PLR, Bonificação, Gratificação, etc.

**Fato em que o parâmetro é utilizado:** Folha de Pagamento

# 1.7 Parâmetro – Encargos Pagos pelo Colaborador

**Descrição:** Na coluna da esquerda estarão todos os encargos do módulo de Folha de Pagamento, e deverá ser feita a seleção, enviando para o campo da direita “Encargos Selecionados” os encargos que deverão ser considerados na métrica correspondente aos Encargos da Folha do Colaborador, Pagos pelo Colaborador, no GoodData.

**Fato em que o parâmetro é utilizado:** Folha de Pagamento

# 1.8 Parâmetro – Encargos Pagos pela Empresa

**Descrição:** Na coluna da esquerda estarão todos os encargos do módulo de Folha de Pagamento, e deverá ser feita a seleção, enviando para o campo da direita “Encargos Selecionados” os encargos que deverão ser considerados na métrica correspondente aos Encargos da Folha do Colaborador, Pagos pela Empresa, no GoodData.

**Fato em que o parâmetro é utilizado:** Folha de Pagamento

# 1.9 Parâmetro – Benefícios Pagos pelo Colaborador

**Descrição:** Na coluna da esquerda estarão todos os eventos do módulo de Folha de Pagamento, e deverá ser feita a seleção, enviando para o campo da direita “Eventos Selecionados” os eventos que deverão ser considerados na métrica correspondente aos Valores de Benefícios do Colaborador, Pagos pelo Colaborador, no GoodData.

**Fato em que o parâmetro é utilizado:** Folha de Pagamento

# 1.10 Parâmetro – Benefícios Pagos pela Empresa

**Descrição:** Na coluna da esquerda estarão todos os eventos do módulo de Folha de Pagamento, e deverá ser feita a seleção, enviando para o campo da direita “Eventos Selecionados” os eventos que deverão ser considerados na métrica correspondente aos Valores de Benefícios do Colaborador, Pagos pela Empresa, no GoodData.

**Fato em que o parâmetro é utilizado:** Folha de Pagamento

# 1.11 Parâmetro – Tipo Benefício Bolsa - Colaborador

**Descrição:** Na coluna da esquerda estarão todos os tipos de benefício do módulo de Folha de Pagamento, e deverá ser feita a seleção, enviando para o campo da direita “Tipo de Benefício Selecionados” os tipos de benefício que deverão ser considerados na(s) métrica(s) do GoodData que correspondem ou existência de benefício.

**Fatos em que o parâmetro é utilizado:** Treinamentos Colaboradores, Treinamentos por Tipo de Custo

Ao finalizar, clicando em Concluir, todas as configurações feitas serão salvas e estarão prontas para utilização dos conceitos (Fatos) do modulo de Recursos Humanos.

Controladoria

Estes parâmetros deverão ser configurados individualmente para cada coligada.

# 1.1 Indicadores Gerenciais

 Para cada indicador gerencial é dever do usuário informar quais são as contas contábeis correspondentes. Os indicadores são:

1 – Ativo Total  
2 – Ativo Circulantes  
3 – Clientes  
4 – Duplicatas Descontadas  
5 – Estoques  
6 – Realizável Longo Prazo  
7 – Ativo Permanente  
8 – Passivo Circulantes  
9 – Fornecedores  
10 – Empréstimos e Financiamentos Curto Prazo  
11 – Empréstimos e Financiamentos Longo Prazo  
12 – Exigível Longo Prazo  
13 – Patrimônio Líquido  
14 – Receita de Vendas  
15 – Receita Operacional de Vendas  
16 – Custo  
17 – Devoluções  
18 – Resultado Operacional  
19 – Lucro Líquido/Lucros e Perdas  
20 – Compras  
21 – Imposto Sobre Vendas  
22 – Despesas Operacionais  
23 – Receitas Financeiras  
24 – Despesas Financeiras

Disponível em  **Menu Integração-> Ferramentas-> Parâmetros**> TOTVS Business Analytics->* Indicadores Gerenciais*

Na coluna do lado esquerdo o sistema apresentará todas as contas contábeis existentes na sua base de dados da coligada em uso.  
Leve para a coluna da direita as contas contábeis que você deseja selecionar. Para isso basta marcar a conta contábil na coluna da esquerda e clicar o botão Adicionar.

****Histórico de fechamento****

Na extração dos indicadores gerenciais, serão desconsiderados os lançamentos contábeis que pertencerem aos históricos de fechamento parametrizados.  
Disponível em  **Menu Integração-> Ferramentas-> Parâmetros**> TOTVS Business Analytics->Histórico de fechamento.**

Na coluna do lado esquerdo o sistema apresentará todos os histórico de fechamento existentes na sua base de dados.  
Leve para a coluna da direita os histórico de fechamento que você deseja selecionar. Para isso basta marcar o histórico de fechamento na coluna da esquerda e clicar em >, ou então clicar em >> caso deseje que todos  os histórico de fechamento sejam parametrizados.

Materiais

# 1.1 Parâmetro – Carteira de Compra

É dever do usuário informar quais são os tipos de movimento que serão considerados na extração dos dados para este indicador.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Materiais >> Mov – Carteira de Compra*” você deverá selecionar quais são os tipos de movimento cujos dados devem ser levados em consideração na fato ‘Carteira de Compras’ que irá espelhar os dados das suas Ordens de Compra que ainda estão em aberto ou parcialmente recebidas. Na coluna do lado esquerdo o sistema apresentará todos os tipos de movimento de Ordens de Compras (1.1.XX) existentes na sua base de dados. Leve para a coluna da direita os tipos de movimento que você deseja selecionar. Para isso basta marcar o tipo de movimento na coluna da esquerda e clicar em >, ou então clicar em >> caso deseje que os dados de todos os movimentos do tipo 1.1 sejam considerados na consulta.

**Fato em que o parâmetro é utilizado:** Carteira de Compras

# 1.2 Parâmetro – Ordem de Compra

É dever do usuário informar quais são os tipos de movimento que serão considerados na extração dos dados para este indicador.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Materiais >> Mov – Ordem de Compra*” você deverá selecionar quais são os tipos de movimento cujos dados devem ser levados em consideração na fato ‘Gestão de Compras’ que irá espelhar os dados das suas Ordens de Compra. Na coluna do lado esquerdo o sistema apresentará todos os tipos de movimento de Ordens de Compras (1.1.XX) existentes na sua base de dados. Leve para a coluna da direita os tipos de movimento que você deseja selecionar. Para isso basta marcar o tipo de movimento na coluna da esquerda e clicar em >, ou então clicar em >> caso deseje que os dados de todos os movimentos do tipo 1.1 sejam considerados na consulta.

**Fato em que o parâmetro é utilizado:** Gestão de Compras

# 1.3 Parâmetro – Devolução de Compra

É dever do usuário informar quais são os tipos de movimento que serão considerados na extração dos dados para este indicador.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Comercial >> Mov – Devolução Compra*” você deverá selecionar quais são os tipos de movimento cujos dados devem ser levados em consideração na fato ‘Devolução de Compras’ que irá espelhar os dados relativos a todas as devoluções de compra efetuadas por sua empresa. Na coluna do lado esquerdo o sistema apresentará todos os tipos de movimento de Devolução de Compra existentes na sua base de dados. Para determinar os tipos de movimento que são de Devolução de Venda o sistema irá verificar a parametrização dos tipos de movimento 1.2 e mostrará na tela apenas aqueles cujo campo ‘Usar Cópia de Movimentos por referência’ estiver marcado e cujo motivo de referência seja o 4 (Devolução de Compra de Mercadorias).

Para verificar essa parametrização nos tipos de movimento da sua empresa vá em “Backoffice > Gestão de Estoque, Compras e Faturamento > Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > 04.09 – Outras Movimentações > Tipo de Movimento > Mov – Outros Dados”.

**Fato em que o parâmetro é utilizado:** Devolução de Compras

# 1.4 Parâmetro – Nota Fiscal Compra

É dever do usuário informar quais são os tipos de movimento que serão considerados na extração dos dados para este indicador.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Comercial >> Mov – Nota Fiscal Compra*” você deverá selecionar quais são os tipos de movimento cujos dados devem ser levados em consideração na fato ‘Nota Fiscal Compra’ que irá espelhar os dados das compras da sua empresa. Na coluna do lado esquerdo o sistema apresentará todos os tipos de movimento de saída (1.2.XX) existentes na sua base de dados. Leve para a coluna da direita os tipos de movimento que você deseja selecionar. Para isso basta marcar o tipo de movimento na coluna da esquerda e clicar em >, ou então clicar em >> caso deseje que os dados de todos os movimentos do tipo 1.2 sejam considerados na consulta.

**Fato em que o parâmetro é utilizado:** Nota Fiscal Compra

# 1.5 Parâmetro – Solicitação de Compras

É dever do usuário informar quais são os tipos de movimento de Solicitação de Compras.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Comercial >> Mov – Solicitação Compra*” você deverá selecionar quais são os tipos de movimento cujos dados devem ser levados em consideração nas fatos que utilizam informações de Solicitação de Compras. Na coluna do lado esquerdo o sistema apresentará todos os tipos de movimento de Solicitação de Compras (1.1.XX) existentes na sua base de dados. Leve para a coluna da direita os tipos de movimento que você deseja selecionar. Para isso basta marcar o tipo de movimento na coluna da esquerda e clicar em >, ou então clicar em >> caso deseje que os dados de todos os movimentos do tipo 1.1 sejam considerados na consulta.

**Fatos em que o parâmetro é utilizado:** Os que utilizam informações de Solicitação de Compras

# 1.6 Parâmetro – Aprovação Ordem de Compra

Durante a extração das Fatos Gestão de Compras e Carteira de Compras, o sistema verificará a parametrização referente a Aprovação da Ordem de compra, é dever do usuário definir quais tipos de movimentos utilizarão tal filtro.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Comercial >> Mov –  Aprovação Ordem Compra*”, serão exibidos os tipos de movimento e, caso parametrizado, seu tipo de Aprovação (Fórmula e Aprovação por WorkFlow), basta selecionar o registro e marcar a opção "Enviar somente aprovadas". Parâmetro - Aprovação Ordem de Compra

**Fato em que o parâmetro é utilizado:** Aprovação Ordem de Compra

Comercial

# 1.1 Parâmetro – Carteira de Vendas

É dever do usuário informar quais são os tipos de movimento que serão considerados na extração dos dados para este indicador.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Comercial >> Mov – Carteira Vendas*” você deverá selecionar quais são os tipos de movimento cujos dados devem ser levados em consideração na fato ‘Carteira de Vendas’ que irá espelhar os dados dos seus Pedidos de Venda que ainda estão em aberto ou parcialmente faturados. Na coluna do lado esquerdo o sistema apresentará todos os tipos de movimento de Pedido de Vendas (2.1.XX) existentes na sua base de dados. Leve para a coluna da direita os tipos de movimento que você deseja selecionar. Para isso basta marcar o tipo de movimento na coluna da esquerda e clicar em >, ou então clicar em >> caso deseje que os dados de todos os movimentos do tipo 2.1 sejam considerados na consulta.

**Fato em que o parâmetro é utilizado:** Carteira de Vendas

# 1.2 Parâmetro – Vendas

É dever do usuário informar quais são os tipos de movimento que serão considerados na extração dos dados para este indicador.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Comercial >> Mov –Vendas*” você deverá selecionar quais são os tipos de movimento cujos dados devem ser levados em consideração na fato ‘Vendas’ que irá espelhar os dados dos seus Pedidos de Venda independente do status dos mesmos, ou seja, nesta consulta serão considerados tanto os pedidos de venda que ainda estão em aberto, como os pedidos de venda que já foram faturados. Na coluna do lado esquerdo o sistema apresentará todos os tipos de movimento de Pedido de Vendas (2.1.XX) existentes na sua base de dados. Leve para a coluna da direita os tipos de movimento que você deseja selecionar. Para isso basta marcar o tipo de movimento na coluna da esquerda e clicar em >, ou então clicar em >> caso deseje que os dados de todos os movimentos do tipo 2.1 sejam considerados na consulta.

**Fato em que o parâmetro é utilizado:** Vendas

# 1.3 Parâmetro – Faturamento

É dever do usuário informar quais são os tipos de movimento que serão considerados na extração dos dados para este indicador.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Comercial >> Mov – Faturamento*” você deverá selecionar quais são os tipos de movimento cujos dados devem ser levados em consideração na fato ‘Faturamento’ que irá espelhar os dados do faturamento da sua empresa. Na coluna do lado esquerdo o sistema apresentará todos os tipos de movimento de saída (2.2.XX) existentes na sua base de dados. Leve para a coluna da direita os tipos de movimento que você deseja selecionar. Para isso basta marcar o tipo de movimento na coluna da esquerda e clicar em >, ou então clicar em >> caso deseje que os dados de todos os movimentos do tipo 2.2 sejam considerados na consulta.

**Fato em que o parâmetro é utilizado:** Faturamento

# 1.4 Parâmetro – Devolução de Vendas

É dever do usuário informar quais são os tipos de movimento que serão considerados na extração dos dados para este indicador.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Comercial >> Mov – Devolução Venda*” você deverá selecionar quais são os tipos de movimento cujos dados devem ser levados em consideração na consulta Devolução de Vendas que irá espelhar os dados relativos a todas as devoluções de venda recebidas por sua empresa. Na coluna do lado esquerdo o sistema apresentará todos os tipos de movimento de Devolução de Venda existentes na sua base de dados. Para determinar os tipos de movimento que são de Devolução de Venda o sistema irá verificar a parametrização dos tipos de movimento 2.2 e mostrará na tela apenas aqueles cujo campo ‘Usar Cópia de Movimentos por referência’ estiver marcado e cujo motivo de referência seja o 5 (Devolução de Venda de Mercadorias).

Para verificar essa parametrização nos tipos de movimento da sua empresa vá em “Backoffice > Gestão de Estoque, Compras e Faturamento > Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > 04.09 – Outras Movimentações > Tipo de Movimento > Mov – Outros Dados”.

**Fato em que o parâmetro é utilizado:** Devolução de Vendas

Financeiro

Estes parâmetros deverão ser configurados individualmente para cada coligada.

# 1.1 Parâmetro – Tipo de Documento a Pagar

É dever do usuário informar quais são os tipos de documentos que serão considerados na extração dos dados dos lançamentos financeiros.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Financeiro >> Tipos de Documento a Pagar*” você deverá selecionar quais são os tipos de documentos a pagar, pois serão considerados apenas os lançamentos financeiros a pagar que estão compreendidos para os tipos de documento parametrizado. Na coluna do lado esquerdo o sistema apresentará todos os tipos de documento a pagar existentes na sua base de dados. Leve para a coluna da direita os tipos de documento a pagar que você deseja selecionar. Para isso basta marcar o tipo de documento a pagar na coluna da esquerda e clicar em >, ou então clicar em >> caso deseje que todos os tipo de documento sejam parametrizados.

**Fato em que o parâmetro é utilizado:** Tipos de Documento a Pagar

# 1.2 Parâmetro – Tipo de Documento a Receber

É dever do usuário informar quais são os tipos de documentos que serão considerados na extração dos dados dos lançamentos financeiros.

**Descrição:** Em “*Integração >> Parâmetros >> TOTVS Business Analytics >> Parâmetros por Empresa >> Financeiro >> Tipos de Documento a Receber* ” você deverá selecionar quais são os tipos de documentos a receber, pois serão considerados apenas os lançamentos financeiros a receber que estão compreendidos para os tipos de documento parametrizado. Na coluna do lado esquerdo o sistema apresentará todos os tipos de documento a receber existentes na sua base de dados. Leve para a coluna da direita os tipos de documento a receber que você deseja selecionar. Para isso basta marcar o tipo de documento a receber na coluna da esquerda e clicar em >, ou então clicar em >> caso deseje que todos os tipo de documento sejam parametrizados.

**Fato em que o parâmetro é utilizado:** Tipos de Documento a Receber

Educacional

Estes parâmetros deverão ser configurados individualmente para cada coligada. Os dados apresentados na coluna da esquerda poderão ser filtrados por nível de ensino e/ou por descrição para facilitar a sua localização.

# 1.1 Parâmetro – Situação de Matrícula de Evasão

**Descrição:** Na coluna da esquerda, "Situação de Matrícula", estarão todas as situações de matrículas cadastradas no TOTVS Educacional que possui o campo "No Curso" ou "No Período" marcado. Deverão ser selecionadas e enviadas para a coluna da direita, "Indicar Perda de Aluno - Evasão", as situações que equivalem a evasão de alunos pois serão consideradas nas métricas de evasão no TOTVS Smart Analytics.

**Fato em que o parâmetro é utilizado:** Alunos

# 1.2 Parâmetro – Situação de Matrícula de Egresso - Ensino Superior

**Descrição:** Na coluna da esquerda, "Selecionar Situação de Matrícula", estarão todas as situações de matrícula cadastradas no TOTVS Educacional que possuem os campos "No Curso" e "Indica Conclusão do Curso" marcados. Deverão ser selecionadas e enviadas para a coluna da direita, "Indicar Egresso do Aluno", as situações que equivalem ao egresso de alunos pois serão consideradas nas métricas sobre formandos no TOTVS Smart Analytics. Essa parametrização é válida para Ensino Superior.

**Fato em que o parâmetro é utilizado:** Alunos

# 1.3 Parâmetro – Situação de Matrícula de Alunos Ativos

**Descrição:** Na coluna da esquerda, "Situação de Matrícula", estarão todas as situações de matrículas cadastradas no TOTVS Educacional que possui o campo "No Período" marcado. Deverão ser selecionadas e enviadas para a coluna da direita, "Indicar Alunos Ativos", as situações que definem que o aluno está ativo na instituição pois serão consideradas nas métricas sobre total de alunos ativos no TOTVS Smart Analytics.

**Fato em que o parâmetro é utilizado:** Alunos

# 1.4 Parâmetro – Situação de Matrícula de Transferência Interna

**Descrição:** Na coluna da esquerda, "Situação de Matrícula", estarão todas as situações de matrículas cadastradas no TOTVS Educacional que possui os campos "No Curso" e "Indica Transferência" marcados. Deverão ser selecionadas e enviadas para a coluna da direita, "Indica Transferência Interna", as situações que definem que o aluno sofreu transferêncai interna de curso na instituição pois serão consideradas nas métricas sobre transferência interna de alunos no TOTVS Smart Analytics.

**Fato em que o parâmetro é utilizado:** Alunos

# 1.5 Parâmetro – Curso Educacional

 **Descrição:** Na coluna da esquerda, "Curso Educacional", estarão todos os cursos educacionais cadastrados no TOTVS Educacional. Deverão ser selecionados e enviados para a coluna da direita, "Curso(s) Educacional(is) Selecionado(s)", os cursos educacionais da instituição que serão enviados para o TOTVS Smart Analytics.

Obs.: Os campos "Modalidade", "Área" (apenas Ensino Superior) e "Presencial/Distância" (apenas Ensino Superior), presentes no cadastro do curso do TOTVS Educacional, são essenciais para correta extração das informações do curso para a quebra dos valores na fato Alunos, por isso, seu preenchimento passa a ser obrigatório para clientes que utilizam o TOTVS Smart Analytics do Educacional.

 **Fato em que o parâmetro é utilizado:** Alunos

# 1.6 Parâmetro – Período Letivo

**Descrição:** Na coluna da esquerda, "Período Letivo", estarão todos os períodos letivos cadastrados com os campos "Data de Início" e "Data de Término" ou "Previsão de Término" preenchidos no TOTVS Educacional. Deverão ser selecionados e enviados para a coluna da direita, "Período(s) Letivo(s) Selecionado(s)", os períodos letivos da instituição que serão enviados para o TOTVS Smart Analytics. 

Obs.: Os campos "Data de Início" e "Data de Término" ou "Previsão de Término", presentes no cadastro do período letivo do TOTVS Educacional, são essenciais para correta extração das informações dos alunos dentro do período letivo, por isso, seu preenchimento passa a ser obrigatório para clientes que utilizam o TOTVS Smart Analytics do Educacional.

**Fato em que o parâmetro é utilizado:** Alunos

# 1.7 Parâmetro – Situação de Matrícula de Egresso - Ensino Básico

**Descrição:** Na coluna da esquerda, "Selecionar Situação de Matrícula", estarão todas as situações de matrícula cadastradas no TOTVS Educacional que possuem o campo "No Período " marcado. Deverão ser selecionadas e enviadas para a coluna da direita, "Indicar Egresso do Aluno", as situações que equivalem ao egresso de alunos pois serão consideradas nas métricas sobre formandos no TOTVS Smart Analytics. Essa parametrização é válida para Ensino Básico em conjunto com a última série egresso no ensino básico informada no parâmetro "Última Série Egresso - Ensino Básico"

**Fato em que o parâmetro é utilizado:** Alunos

# 1.8 Parâmetro – Última Série Egresso - Ensino Básico

**Descrição:** Na coluna da esquerda, "Selecionar Última Série Egresso - Ensino Básico", estarão todas as séries, vinculadas aos cursos do ensino básico parametrizados no parâmetro "Curso Educacional", cadastradas no TOTVS Educacional. Deverão ser selecionadas e enviadas para a coluna da direita, "Última(s) Série(s) Egresso(s) Selecionada(s)", as séries que equivalem a última série do ensino básico para formação do aluno; Essa parametrização é válida somente para o Ensino Básico em conjunto com as situações de matrículas informadas no parâmetro "Situação de Matrícula de Egresso - Ensino Básico".

**Fato em que o parâmetro é utilizado:** Alunos

Construção & Projetos

Estes parâmetros deverão ser configurados individualmente para cada coligada. Os dados apresentados na coluna da esquerda poderão ser filtrados por nível de ensino e/ou por descrição para facilitar a sua localização.

3 - Plano de Extração dos Dados

O cadastro do plano de extração é uma definição de um plano de trabalho para a extração dos dados do Totvs-RM. Ele permite que a extração dos dados seja realizada de forma seletiva, onde é possível extrair somente as áreas, fatos e dimensões relevantes para o tipo de análise que se deseja realizar.

Para cadastrar os planos de extração, acesse *RM >> Integração >> Integração >> TOTVS Business Analytics >> Plano de Extração.*

ProcessoPlanoExtraçaoCadastro do Plano de Extração

Para cadastrar um plano de extração é necessário definir algumas informações como descrição do plano, tipo de período, tipo do extrator.

* **Tipo de Período**  
    
  Os períodos de extração são filtros de data que serão considerados na extração das informações do ERP-RM. Ao realizar o cadastro do plano de extração é necessário informar qual será o tipo de período de extração. O tipo de período de extração pode ser:  
   **Sem período**: É utilizado quando o tipo de extração for definido apenas com dimensões, onde não é necessário ser informado filtro por período.  
  **Período Fixo**: É muito comum a utilização do período fixo quando o plano de extração dos dados for de carga inicial, ou seja ao implantar o Totvs Smart Analytics comTotvs-RM.  
  **Período Variável**: Utilizando o período de extração variável, será considerado, o intervalo de data de extração variável conforme os valores informados, levando em consideração sempre a data atual menos um dia. Esta opção é comumente utilizada em cargas incrementais.

* **Tipo de seleção do Extrator**  
  Para proceder com a extração dos dados do ERP Totvs-RM de forma segmentada é necessário informar qual será o tipo de extração para o plano, podendo ser por:  
  Dimensões  
  Controladoria  
  Financeiro  
  Comercial  
  Materiais  
  Recursos Humanos  
  Educacional  
  Personalizado: Permite ao usuário realizar a extração apenas dos fatos que julgar necessário.  
    
  Observação: É obrigatório o cadastro de um plano de extração de Dimensões.
Processo do Plano de Extração

Após a definição dos parâmetros e do cadastro do plano de extração, basta executar o plano de extração. Para executá-lo acesse o*menu *RM >> Integração >> Integração >> TOTVS Business Analytics >> *Processo do Plano de Extração.*** Ao executar o processo de extração, o processo identifica os planos em comum ao plano selecionado. Dessa forma, será emitido ao usuário um alerta informando sobre a ocorrência em outro momento da extração dos dados em comum ao plano selecionado, cabendo ao usuário decidir se conclui ou não o processo.

Quando o processo entra em execução é inicializado a limpeza das tabelas da Fluig Smart Data envolvidas (dimensões e fatos) conforme o tipo de extrator definido no cadastro do plano. Para realizar a limpeza das tabelas o processo leva em consideração a instância parametrizada no sistema, dessa maneira é possível trabalhar com a extração de informações de mais de uma base RM para a Fluig Smart Data pois cada extração limpará os dados relacionados apenas a instância configurada para a base.

Ao concluir a execução do processo do plano de extração, os dados foram extraídos, tratados, padronizados e então carregados no Fluig Smart Data (apenas os dados relacionados a coligadas ativas). A partir deste ponto, os dados deverão ser transportados até a nuvem ( através do processo de Envio dos Dados para o GoodData), para o Data Warehouse do TOTVS Smart Analytics.

**Importante:**

* Extração de Fatos/Dimensões do Educacional:
  + A fato de alunos considera períodos mensais para consolidação das informações, por isso, mesmo que no plano criado o usuário insira como periodo de extração um mês incompleto, a extração será feita considerando todo o mês do período definido. Ex.: Plano de Extração - 10/08/2017 a 20/08/2017 → a execução desse plano para a fato de alunos levará em consideração as informações de todo o mês de Agosto/2017.
  + Na extração de dimensões e fatos do Educacional, as informações processadas serão inseridas em um arquivo .csv que será salvos em diretório a ser definido no arquivo “my.properties” (arquivo de configuração utilizado pelo Agent para enviar as informações para o TOTVS Smart Analytics). Toda vez que for feito a extração da mesma fato, mesmo configurando períodos diferentes, ou dimensões, o arquivo .csv gerado será sobreposto pelos novos arquivos gerados pela extração.
* Caso seu ambiente esteja configurado em três camadas é possível realizar o agendamento da execução do plano de extração conforme sua necessidade.
* Quando o processo de extração gerar as informações para arquivos ".csv" e o ambiente for 3 camadas, é importante que as parametrizações apresentadas no link abaixo sejam aplicadas.

Histórico de Execução do Plano de Extração

O histórico de execução do plano de extração, nos permite visualizar informações de todos os planos de extração executados em sua base, permitindo que seja efetuado analises sobre a cada item de extração do plano.

Poderão ser consultadas informações tais como o período de extração, quantidade de registros extraído de cada item do plano, usuário que executou o processo, o tempo de extração por item e o status de execução do item do plano. O status do item do plano de extração representa a ação que está ou foi executado, São eles:

* Plano em Execução
* Plano Executado
* Erro na Extração
* Enviando para GoodData
* Enviado para GoodData
4 - Envio dos Dados para o Gooddata

O processo de envio (Processo de Envio dos Dados para o TOTVS Smart Analytics) identifica os dados que foram extraídos, através da conclusão do processo do plano de extração, e executa em background o **Agent**, que é quem envia os dados presentes na Stage Area e nos arquivos .csv (existentes no diretório configurado no my.properties) para o Totvs Smart Analytics.

Antes de executar o processo de envio dos dados é necessário informar alguns parâmetros. Para isto acesse *menu Integração->Ferramentas-> Parâmetros -> TOTVS Business Analytics*e informe os parâmetros:

* Caminho do Java.exe
* Caminho do Agent
* Caminho do my.properties

**Importante:**Antes de executar o processo de envio, certifique-se que o my.properties (arquivo de configuração do **Agent**) já esteja devidamente configurado para o envio.

Para mais detalhes de como configura-lo consulte: [Onde encontro o download do Agent](http://tdn.totvs.com/pages/viewpage.action?pageId=235312097)

# Configuração do arquivo my.properties do Agent

| **Produto:** **Totvs RM** |
| --- |
| Como configurar o arquivo **my.properties** para a execução do **Agent** linha RM? |
| A seguir, a relação dos parâmetros existentes no **Agent** e como preenchê-los no arquivo do **my.properties**: Parâmetros obrigatórios: **E-mail completo do usuário:**  **Parâmetro:** gdc.username  **Exemplo:** gdc.username = [email@totvs.com.br](mailto:email@totvs.com.br)  **Observação:** Este usuário deve ser Administrador no **GoodData**.  **Senha do GoodData:**  **Parâmetro:** gdc.password  **Exemplo:** gdc.password = senha    **URL de envio do arquivo compactado para o GoodData:**  **Parâmetro:** gdc.upload\_url  **Exemplo:** gdc.upload\_url = https://[analytics.totvs.com.br](http://analytics.totvs.com.br)/project-uploads/<Project\_ID>/today/  **Observação:** Saiba como obter o valor do Project\_ID em: [“Como obtenho o valor do Project\_ID e do Process\_ID”](http://tdn.totvs.com/pages/viewpage.action?pageId=165283537#_Como_obter_o) false **URL de execução do ETL do TOTVS Smart Analytics:**  **Parâmetro:** gdc.etl.process\_url  **Exemplo:** gdc.etl.process\_url = https://[analytics.totvs.com.br](http://analytics.totvs.com.br/)/gdc/projects/<Project\_ID>/dataload/processes/<Process\_ID>/  **Observação:** Saiba como obter o valor do Project\_ID e/ou do Process\_ID em [“Como obtenho o valor do Project\_ID e do Process\_ID”](http://tdn.totvs.com/pages/viewpage.action?pageId=165283537#_Como_obter_o)  **Parâmetro referente à execução do *graph* que inicia o ETL do Smart Analytics:**  **Parâmetro:** gdc.etl.graph  **Exemplo:** gdc.etl.graph = Totvs Smart Analytics v11/graph/MAIN\_JOB.grf  **Observação:** Geralmente, este parâmetro não deve ser alterado. Para checar a necessidade de mudá-lo, acesse  o seguinte documento: [erro 404 Not Found](http://tdn.totvs.com/pages/viewpage.action?pageId=165283537#_Quando_executo_o).    **Parâmetro que Indica Caminho dos Arquivos .csv (obrigatório apenas para extração do Educacional):**  Configurar o agent para buscar informações de arquivos .csv para serem enviadas para o Gooddata.  **Parâmetros:** filesystem.input\_dir e filesystem.wildcard  **Exemplo:**   * filesystem.input\_dir=C:/Gooddata/ * filesystem.wildcard=\*.csv    2. Os parâmetros abaixo se referem ao **Java Database Connectivity (JDBC)**. Cada Banco de Dados possui sua própria configuração, aqui  seguem os mais utilizados. Para mais exemplos de **JDBC** consulte o item: [erros de JDBC.](http://tdn.totvs.com/pages/viewpage.action?pageId=165283537#_Erros_referente_ao)    **Diretório e .JAR do Banco de Dados utilizado:**  **Parâmetro:** jdbc.driver\_path  **Exemplo:** jdbc.driver\_path = C:/jdbc/sqljdbc4.jar  **Observação:** Este .jar não é o arquivo do **Agent** e sim o arquivo do Banco de Dados. Cada banco de dados possui seu próprio .jar.  Se necessário consulte o fabricante do *software* para a solicitação deste.  ***Driver* de conexão do JDBC:**  **Parâmetro:** jdbc.driver  **Exemplo:** jdbc.driver= com.microsoft.sqlserver.jdbc.SQLServerDriver  **Observação:** Cada banco de dados possui a sua própria conexão de *driver*. Segue abaixo as possíveis conexões nos principais bancos de dados:   * **IBM DB2:**   jdbc.driver = com.ibm.db2.jdbc.app.DB2Driver   * **Oracle Thin:**   jdbc.driver=oracle.jdbc.driver.OracleDriver   * **PostgreSQL (a partir da v7.0):**   jdbc.driver=org.postgresql.Driver   * **Microsoft SQL Server 2000 (Microsoft Driver):**   jdbc.driver=com.microsoft.sqlserver.jdbc.SQLServerDriver   * **Progress (OpenEdge):**   jdbc.driver=com.ddtek.jdbc.openedge.OpenEdgeDriver    Para maiores informações e solicitação do *driver* do banco de dados, consulte o fabricante do *software*.  **URL de conexão do JDBC com o Banco de Dados:**  **Paramentro:** jdbc.url  **Exemplos:** jdbc.url= jdbc:sqlserver://nomedamaquina\\sqlexpress¹;DatabaseName=BISTAGE ou  jdbc.url= jdbc:sqlserver://nomedamaquina;DatabaseName=BISTAGE  ¹ - Representa a instância do SGBD  **Observação:** Cada Banco de Dados possui a sua própria **URL** de conexão. Segue abaixo as possíveis **URLs** dos principais Bancos de Dados:   * **IBM DB2**   jdbc.url=jdbc:db2://<HOST>:<PORT>/<DB>   * **Oracle Thin**   jdbc.url=jdbc:oracle:thin:@<HOST>:<PORT>:<SID>   * **PostgreSQL (v7.0 and later)**   jdbc.url=jdbc:postgresql://<HOST>:<PORT>/<DB>   * **Microsoft SQL Server 2000 (Microsoft Driver)**   jdbc.url=jdbc:microsoft:sqlserver://<HOST>;DatabaseName=<DB>   * **Progress (OpenEdge)**   jdbc.url=jdbc:datadirect:openedge://<HOST>;databaseName=<DB>  **Usuário do Banco de Dados:**  **Parâmetro:** jdbc.username  **Exemplo:** jdbc.username = usuário  **Senha do Banco de Dados:**  **Parâmetro:** jdbc.password  **Exemplo:** jdbc.password = senha  **Observação**: Os demais itens **NÃO** devem sofrer alterações, exceto se ocorrer uma atualização do **Agent** ou solicitação pela área de inovação de **B.A.**  **Parâmetro de Usuário e Senha para acessar o ETL do Smart Analytics:**  **Parâmetro:** gdc.etl.param.USER\_PWD\_SECURE\_DI  **Exemplo:** gdc.etl.param.USER\_PWD\_SECURE\_DI = email%[40totvs.com.br](http://40totvs.com.br/):senha  **Observação:** Certos símbolos devem ser substituídos pelo seu código em hexadecimal, por exemplo o **@** deve ser alterado por **%40**.  **Conversão de campos do tipo data para *string*. Isso é possível por meio dos parâmetros a seguir:**  **Parâmetro:** gdc.jbdc.file\_date  **Exemplo:** C:\<Caminho\_arquivo>\DATE\_FIELD.txt, onde **<Caminho\_arquivo>** é o local do diretório onde encontra-se o arquivo **DATE\_FIELD.txt**.    **Parâmetro:** gdc.jdbc.format\_date  **Exemplo:** gdc.jdbc.format\_date = <CONVERSAO>, onde **<CONVERSAO>** representa a função utilizada para conversão, que deve  ser escolhida entre as duas opções abaixo. Esta função depende do Banco de Dados utilizado, por exemplo, se o Banco de Dados  for o Oracle, deve-se utilizar a **Opção 1**, no caso do SQL Server, use a **Opção 2**.   * **Opção 1:** To\_Char(FIELD\_DATE, 'yyyyMMdd') * **Opção 2:** Convert(VARCHAR(08), FIELD\_DATE, 112)     **Observação**: Os parâmetros citados acima devem ser utilizados de forma conjunta.    **Atenção:**  Após efetuar todas as configurações acima, deverá fazer download do arquivo  e substituir este arquivo na pasta do Agent. |

5 - Fatos e Indicadores

Apresentamos abaixo, conforme o modelo de áreas do projeto padrão TOTVS Smart Analytics/Gooddata as respectivas Fatos e Indicadores.

FatosIndicadoresComercial

# 1.1 Carteira de Vendas (HL3)

Extrai os itens das movimentações de Pedido de Vendas nas seguintes condições: - Pedidos com status em aberto ou parcialmente faturado; - A data do movimento (conforme parâmetro do tipo de movimento) é menor ou igual à data final do período de extração; - O código do tipo de movimento está parametrizado como “Carteira de Vendas”; - A quantidade do item de movimento é maior do que 0 (zero).

***Filtro – Período de extração***

O período de extração são filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

***Processamento***

Tabela de Destino: **HL3**

***Indicadores Diretos:***

* **Vl Carteira (HL3\_VCARTE):** indica o valor da carteira de vendas, ou seja, o valor das vendas que ainda não foram faturadas. Este valor diz respeito às movimentações dos pedidos.
* **Qtde Entregas Carteira sem Atraso:** indica a quantidade de itens cujas entregas em carteira que estão em dia, ou seja, a previsão de entrega não foi ultrapassada.
* **Qtde Entregas Carteira em Atraso:** indica a quantidade de itens cujas entregas em carteira que estão em atraso.
* **Qtde Entregas Carteira (Qtde Entregas Carteira sem Atraso + Qtde Entregas Carteira em Atraso):** indica a quantidade total de entregas de itens em carteira.
* **Dias sem Atraso Carteira:** indica o número de dias que restam para efetuar a entrega em dia, ou seja, os dias decorridos entre a data de programada para entrega do item no pedido e a data da extração.
* **Dias Atraso Carteira:** indica o número de dias em atraso, ou seja, o número de dias decorridos entre a data de extração e a data programada para entrega do item no pedido.
* **Média de Atrasos Carteira (Dias Atraso Carteira / Qtde Entregas Carteira em Atraso):** indica a média de atrasos, em dias, das entregas em carteira. Para uma boa performance, esta média deve tender a zero.

# 1.2 Vendas (HL4)

Extrai os itens das movimentações de Pedido de Vendas nas seguintes condições: - Pedidos com status em aberto, parcialmente faturado ou faturado; - A data do movimento (conforme parâmetro do tipo de movimento) está inserida entre as datas inicial e final do período de extração; - O código do tipo de movimento está parametrizado como “Vendas”.

***Filtro – Período de extração***

O período de extração são os filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

***Processamento***

Tabela de Destino: **HL4**

***Indicadores Diretos:***

* **Qtde Vendida (HL4\_QVENDA)**: indica a quantidade vendida na unidade de medida do item.
* **Qtde Vendida Família Comercial (HL4\_QVENFC)**: indica a quantidade vendida na unidade de medida da família comercial, no caso da linha RM é a mesma quantidade vendida do item visto que não existe o conceito de unidade específica por família comercial que é uma tabela de classificação.
* **Qtde Vendida Família Material (HL4\_QVENFM)**: indica a quantidade vendida na unidade de medida da família material, no caso da linha RM é a mesma quantidade vendida do item visto que não existe o conceito de unidade específica por família material que é uma tabela de classificação.
* **Vl Desconto Venda (HL4\_VLDESV)**: indica o valor total do desconto que está sendo concedido para a venda.
* **Vl Impostos Venda (HL4\_VIMPVD)**: indica o valor referente a impostos vinculados ao pedido de venda.
* **Vl Venda Líquida (HL4\_VVNDLQ)**: indica o valor líquido da venda, relacionada às movimentações dos pedidos, sem os impostos IPI, PIS, COFINS, IRRF, ISS, INSS e descontos. O valor do ICMS pode estar descontado dependendo da origem da informação. **Vl Venda Mercadoria (HL4\_VVMERC)**: indica o valor líquido da mercadoria vendida, relacionado as movimentações dos pedidos.
* **Vl Venda Total (HL4\_VVENDA)**: indica o valor bruto da venda, relacionado às movimentações dos pedidos. Esse valor corresponde ao valor de venda da mercadoria acrescido de todos os impostos e das despesas da venda.
* **% Variação Previsão Vendas ((Qtde Vendida / Qtde Prevista) - 1)**: Não se aplica.
* **% Desconto Venda (Vl Desconto Venda / Vl Venda Mercadoria)**: indica o percentual de desconto sobre a venda.

# 1.3 Faturamento (HL2)

Extrai os itens dos movimentos de Venda nas seguintes condições: - Movimentos com status diferente de Cancelado; - A data do movimento (conforme parâmetro do tipo de movimento) está inserida entre as datas inicial e final do período de extração; - O código do tipo de movimento está parametrizado como “Faturamento”.

***Filtro – Período de extração***

O período de extração são os filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

***Processamento***

Tabela de Destino: **HL2**

***Indicadores Diretos:***

* **Qtde Faturada Item (HL2\_QFATIT)**: Indica a quantidade inserida na nota fiscal na unidade de medida do item.
* **Qtde Faturada Família Comercial (HL2\_QVENFC)**: Indica a quantidade inserida na nota fiscal na unidade de medida da família comercial, no caso da linha RM é a mesma quantidade do item no movimento, visto que não existe o conceito de unidade específica por família comercial que é uma tabela de classificação.
* **Qtde Faturada Família Material (HL2\_QVENFM):** Indica a quantidade inserida na nota fiscal na unidade de medida da família material, no caso da linha RM é a mesma quantidade do item no movimento, visto que não existe o conceito de unidade específica por família material que é uma tabela de classificação.
* **Qtde Prazo Duplicata (HL2\_QPRZDP):** Não se aplica.
* **Vl COFINS Faturamento (HL2\_VCOFIN):** Indica o valor do COFINS calculado para o faturamento.
* **Vl Comissão Faturamento (HL2\_VCMFAT):** Indica o valor da comissão do representante baseado nos valores faturados.
* **Vl Custo Faturamento (HL2\_VLCSFT):** Indica o valor do custo de faturamento do item de acordo com a definição do tipo de custo que a empresa trabalha.
* **Vl Desconto Faturamento (HL2\_VLDESF):** Indica o valor de desconto concedido na nota fiscal de saída.
* **Vl Despesas (HL2\_VDESPE):** Indica o valor de despesas da nota fiscal. Somente considera o valor do seguro e das embalagens. Não considera frete.
* **Vl Faturamento Líquido (HL2\_VFATLQ):** Indica o valor faturado sem o valor do imposto ICMS.
* **Vl Faturamento Mercadoria (HL2\_VFATME):** Indica o valor líquido da nota fiscal acrescido do valor do ICMS.
* **Vl Faturamento Total (HL2\_VFATOT):** Indica o valor faturado bruto.
* **Vl Frete NF (HL2\_VFRTNF):** Indica o valor do frete para a nota fiscal.
* **Vl ICMS Subst. Faturamento (HL2\_VICMSS):** Indica o valor do ICMS Substituto calculado para a nota fiscal.
* **Vl IRF Faturamento (HL2\_VLIRFF):** Indica o valor do IRF calculado na nota fiscal de saída.
* **Vl INSS Faturamento (HL2\_VINSSF):** Indica o valor do INSS calculado na nota fiscal de saída.
* **Peso Líquido (HL2\_QTPESL):** Não se aplica.
* **Peso Bruto (HL2\_QTPESB):** Não se aplica.
* **Vl ICMS Faturamento (HL2\_VICMSF):** Indica o valor do ICMS calculado para a nota fiscal.
* **Vl IPI Faturamento (HL2\_VIPIFT):** Indica o valor do IPI calculado para a nota fiscal.
* **Vl ISS Faturamento (HL2\_VISSFT):** Indica o valor do ISS calculado para a nota fiscal.
* **Vl PIS Faturamento (HL2\_VPISFT):** Indica o valor do imposto PIS incidente sobre o valor faturado.
* **Vl Receita Financeira (HL2\_VRECFI):** Não se aplica.
* **Quantidade (HL2\_QTDVEN):** Não se aplica.
* **Valor Unitário (HL2\_VLUNIT):** Indica o valor da unidade do item vendido.
* **Vl Custo de Mercadoria Vendida (HL2\_VLCMEV):** Não se aplica.
* **% Margem (Vl Margem / Vl Faturamento Líquido):** Indica o valor, em percentual, da relação entre a margem de contribuição e o faturamento líquido.
* **% Desconto Faturamento (Vl Desconto Faturamento / Vl Faturamento Mercadoria):** Indica o percentual de desconto praticado na nota fiscal de saída.
* **Vl Faturamento Líquido Sem Devoluções (Vl Faturamento Líquido - Vl Devolução Líquida):** Indica o valor faturado líquido de impostos e descontos, exceto devoluções.
* **Vl Margem (Vl Faturamento Líquido - Vl Custo Faturamento - Vl Receita Financeira - Vl Comissão Faturamento):** Indica o valor da margem de contribuição que corresponde ao lucro líquido. O valor de faturamento líquido está isento de impostos e descontos.
* **Vl Preço Médio Faturado (Vl Faturamento Mercadoria / Qtde Faturada Item):** Indica o valor do preço médio. A análise desse valor deve ser feita por item ou por família comercial quando a família for composta de itens com a mesma unidade de medida. **Vl Variação Entre Vendas x Faturamento (Vl Venda Total - Vl Faturamento Total):** Indica a diferença entre o valor da venda bruto e o valor faturado bruto.

# 1.4 Análise de Crédito (HL0)

Extrai os dados dos Clientes/Fornecedores que estejam cadastrados como Cliente ou Ambos.

***F**iltro – Período de extração***

Não é utilizado neste fato.

***Processamento***

Tabela de Destino: **HL0**

***Indicadores Diretos:***

* **Vl Limite Crédito (HL0\_VLMCDT):** Indica o valor total do limite de crédito cedido ao cliente.
* **Vl Limite Crédito Disponível (HL0\_VLMCDD):** Indica o saldo do crédito disponível para o cliente considerando o valor total do limite cedido menos o valor do crédito em uso.

# 1.5 Devolução de Vendas (HL6)

Extrai os itens dos movimentos de devolução de venda nas seguintes condições: - Movimentos com status diferente de Cancelado; - A data do movimento (conforme parâmetro do tipo de movimento) está inserida entre as datas inicial e final do período de extração; - O código do tipo de movimento está parametrizado como “Devolução Venda”.

***Filtro – Período de extração***

O período de extração são os filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

***Processamento***

Tabela de Destino: **HL6**

***Indicadores Diretos:***

* **Qtde Devolvida Item (HL6\_QDEVIT):** indica a quantidade de itens devolvidos.
* **Qtde Devolvida Família Comercial (HL6\_QDEVFC):** Quantidade do Item no movimento na unidade de medida da família comercial. Como a linha RM Não trabalha com unidade de medida nas tabelas de classificação, utiliza-se a própria unidade de medida do item.
* **Qtde Devolvida Família Material (HL6\_QDEVFM):** Quantidade do Item no movimento na unidade de medida da família material. Como a linha RM Não trabalha com unidade de medida nas tabelas de classificação, utiliza-se a própria unidade de medida do item.
* **Vl COFINS Devolução (HL6\_VCOFID):** indica o valor referente ao imposto COFINS calculado para a devolução.
* **Vl Custo Devolução (HL6\_VCSTDV):** indica o valor do custo do item na devolução. IMPORTANTE: Para que essa informação possa ser utilizada, o tipo de movimento deve estar parametrizado para afetar estoque, caso contrário não é possível buscar o custo do produto.
* **Vl Devolução Líquida (HL6\_VDEVLQ):** indica o valor líquido da devolução. Valor líquido do item de movimento considerando descontos e despesas e subtraindo o tributo ICMS.
* **Vl Devolução Mercadoria (HL6\_VDEVME):** indica o valor líquido da devolução considerando descontos e despesas.
* **Vl Devolução Total (HL6\_VDEVTO):** indica o valor total dos itens que foram devolvidos.
* **Vl ICMS Subst. Devolução (HL6\_VICMSS):** indica o valor do ICMS de substituição calculado para a devolução.
* **Vl Desconto Devolução (HL6\_VDESDV):** indica o valor do desconto concedido no faturamento que está em devolução. É composto pela somatória dos campos TITMMOV.VALORDESC + TITMMOV.RATEIODESC, onde TITMMOV.RATEIODESC representa o rateio do desconto do movimento nos itens.
* **Vl INSS Devolução (HL6\_VINSSD):** indica o valor do INSS calculado para a devolução.
* **Vl ICMS Devolução (HL6\_VICMSD):** indica o valor do ICMS calculado para a devolução.
* **Vl IPI Devolução (HL6\_VIPIDV):** indica o valor do IPI calculado para a devolução.
* **Vl PIS Devolução (HL6\_VPISDV):** indica o valor do PIS calculado para o faturamento.
* **% Desconto Devolução (Vl Desconto Devolução / Vl Devolução Mercadoria):** indica o percentual de desconto concedido na venda, estornado na devolução.

# 1.6 Entrega de Vendas (HL7)

Extrai os itens dos movimentos de venda nas seguintes condições: - Movimentos com status diferente de Cancelado; - A data do movimento (conforme parâmetro do tipo de movimento) está inserida entre as datas inicial e final do período de extração; - O código do tipo de movimento está parametrizado como “Vendas”; - A “Data de Entrega” do item de movimento ou do movimento estão preenchidas.

***Filtro – Período de extração***

O período de extração são os filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

***Processamento***

Tabela de Destino: **HL7**

***Indicadores Diretos:***

* **Dias Antecipação (HL7\_QDSANT):** indica o número de dias ocorridos entre a data de saída da mercadoria e a data de entrega programada no pedido. Pode ser utilizada como base para o cálculo da média de dias de antecipação.
* **Dias Atraso (HL7\_QDSATR):** indica o número de dias ocorridos entre a data de entrega programada no pedido e a data de saída da mercadoria. Pode ser utilizada como base para o cálculo da média de dias de atraso.
* **Nr Entregas (HL7\_QNRENT):** Não se aplica.
* **Lead Time Entrega (HL7\_QLEADT):** indica o número de dias entre a data de implantação do pedido e a data da última nota fiscal. Pode ser utilizada como base para o cálculo do lead time médio de entrega.
* **Lead Time Emissão Implantação (HL7\_QDEMIP):** Não se aplica.
* **Lead Time Interno (Dias Antecipação - Dias Atraso):** indica o número de dias entre data de entrega programada no pedido e a data de saída da mercadoria. Um valor negativo indica atraso e um valor positivo antecipação. Zero significa entrega na data prevista.
* **Qtde Entregas Únicas:** indica a quantidade de entregas únicas realizadas. Entrega única é quando ocorre a entrega total do item de uma só vez, sem haver entregas parciais.
* **Qtde Entregas Ocorridas:** indica a quantidade de entregas ocorridas independentemente do número total das entregas do item. Por exemplo, quando o número de entregas do item for 3, a quantidade de entregas ocorridas será 1.
* **Qtde Entregas Atrasadas:** indica a quantidade de entregas ocorridas com atraso.
* **Qtde Entregas Antecipadas:** indica a quantidade de entregas ocorridas de forma antecipada.
* **% Entregas sem Atraso ((Qtde Entregas Ocorridas - Qtde Entregas Atrasadas) / Qtde Entregas Ocorridas):** indica o percentual de entregas na data programada, sem atraso.
* **% Entregas Únicas ((Qtde Entregas Únicas / Qtde Entregas Ocorridas)):** indica o percentual de entregas únicas. Mostra o percentual de vezes que a entrega ocorreu de forma única e não em partes. Quanto maior o percentual, menor os custos de transporte. É interessante analisar esta medida juntamente com o "% Entregas Sem Atraso", pois apesar da empresa estar entregando os pedidos de uma só vez, poderá estar fazendo com atraso.
* **Média de Antecipações ((Dias Antecipação / Qtde Entregas Antecipadas)):** indica a média de antecipação das entregas em número de dias. Se esse indicador for alto, indica que os prazos poderiam ser mais curtos, tornando a empresa mais competitiva.
* **Qtde Entregas na Data (Qtde Entregas Ocorridas - Qtde Entregas Atrasadas - Qtde Entregas Antecipadas):** indica a quantidade de entregas realizadas na data programada.
* **Média de Atrasos (Dias Atraso / Qtde Entregas Atrasadas):** indica a média de atraso das entregas em número de dias.
* **Lead Time Médio de Implantação (Lead Time Emissão Implantação / Nr Entregas):** Não se aplica.

Controladoria

# 1.1 Indicadores Gerenciais (HLA)

Extrai o saldo e movimentações das contas contábeis agrupadas conforme a parametrização realizada para cada indicador gerencial, conforme o período definido no plano de extração, exceto os lançamentos que pertencem aos históricos de fechamento definido nos parâmetros **Menu Integração-> Ferramentas-> Parâmetros**> TOTVS Business Analytics->Histórico de fechamento.** Os valores dos lançamentos contábeis, são quebrados mensalmente por empresa, filial e indicador, dentro do período de extração.

É dever do usuário informar quais serão as contas contábeis que correspondente a cada indicador gerencial. Os indicadores são:

1 – Ativo Total  
2 – Ativo Circulantes  
3 – Clientes  
4 – Duplicatas Descontadas  
5 – Estoques  
6 – Realizável Longo Prazo  
7 – Ativo Permanente  
8 – Passivo Circulantes  
9 – Fornecedores  
10 – Empréstimos e Financiamentos Curto Prazo  
11 – Empréstimos e Financiamentos Longo Prazo  
12 – Exigível Longo Prazo  
13 – Patrimônio Líquido  
14 – Receita de Vendas  
15 – Receita Operacional de Vendas  
16 – Custo  
17 – Devoluções  
18 – Resultado Operacional  
19 – Lucro Líquido/Lucros e Perdas  
20 – Compras  
21 – Imposto Sobre Vendas  
22 – Despesas Operacionais  
23 – Receitas Financeiras  
24 – Despesas Financeiras

***Processamento***

Tabela de Destino: **HLA**

***Indicadores Diretos:***

* **Valor do mês** (HLA\_VLRMES) – Trata-se do valor que foi realizado no período, ou seja, o valor do movimento contábil.
* **Valor do mês acumulado** (HLA\_VLRMSA) – Valor de Saldo atual até o mês.
* **Mês Referência** (HLA\_VLRMSA) – Indica o mês de referência para os indicadores que está sendo analisados.
* **Indicador** (HLA\_INDICA) define a qual indicador ele pertence.

# 1.2 Contabilidade (HL9)

Extrai o saldo e as movimentações (totais de débitos e créditos) das contas contábeis conforme o período definido no plano de extração. Os valores são quebrados mensalmente, por empresa, filial, centro de custo e conta contábil, dentro do período de extração.

***Processamento***

Tabela de Destino:**HL9**

***Indicadores Diretos:***

* **Vl Saldo Inicial Real**(HL9\_VSDINI): indica o saldo inicial contábil do período.
* **Vl Débito Real** (HL9\_VDREAL): indica o valor do movimento a debito no período.
* **Vl Crédito Real**(HL9\_VCREAL): indica o valor do movimento a crédito no período.
* **Vl Saldo Final Real** (HL9\_VSDFIN): indica o saldo final contábil do período.
* **Vl Movimento Contábil Real (**HL9\_VCTBRL): indica o valor que foi realizado no período;
* **Vl Apuração Resultado**(HL9\_VAPURA): indica o valor contábil referente à apuração de resultado. (Histórico de fechamento)

# 1.3 Orçamento (HLC)

Extrai os valores orçados x realizados das contas contábeis conforme o período definido no plano de extração. Os valores são quebrados mensalmente, por empresa, filial, centro de custo e conta contábil, dentro do período de extração.

***Processamento***

Tabela de Destino:**HLC**

*****Indicadores Diretos:*****

* **Vl Orçado**(HLC\_VORCAD) - Indica o valor contábil que foi orçado para o período.
* **Vl Contábil Real** (HLC\_VCTBRL) - Indica o valor que foi realizado no período, ou seja, o valor do movimento contábil.

Financeiro

# 1.1 Contas a Pagar – Carteira (HLK)

O processo de extração de contas a pagar Carteira, leva em consideração apenas os lançamentos financeiros que estão compreendidos para os tipos de documento parametrizados e o saldo a pagar maior que zero.   
Caso existam faturas, serão considerados apenas os vencimentos de fatura e não os lançamentos faturados.  
Para informar os tipos de documentos a pagar que serão considerados no momento da extração, acesse os parâmetros:  
**Menu Integração-> Ferramentas-> Parâmetros**> TOTVS Business Analytics->Tipos de documentos a pagar.**

*****Processamento*****

Tabela de Destino: **HLK**

***Indicadores Diretos:***

* **Vl a Pagar** (HLK\_VPAGAR): indica o valor do saldo atual disponível para o lançamento a pagar
* **Prazo Vencimento Carteira**(HLK\_PRZVCT): essa medida indica a diferença em dias entre a data de vencimento e a data de emissão do lançamento em carteira.
* **Prazo Vencimento Carteira**(HLK\_PRZVCT): Não se aplica.

# 1.2 Contas a Pagar – Pagamento (HLI)

O processo de extração do contas a pagar pagamento, leva em consideração apenas os lançamentos financeiros a pagar que tiveram baixas parciais ou total que estão compreendidos para os tipos de documento parametrizado e conforme o período definido no plano de extração, utilizando como filtro, a data de baixa.   
Caso existam faturas, serão considerados apenas os vencimentos de fatura e não os lançamentos faturados.  
Para informar os tipos de documentos a pagar que serão considerados no momento da extração, acesse os parâmetros:  
***Menu Integração-> Ferramentas-> Parâmetros**> TOTVS Business Analytics->Tipos de documentos a pagar.***

******Processamento******

Tabela de Destino:**HLI**

***Indicadores Diretos:***

* **Vl Pago**(HLI\_VPAGO): indica o total dos valores vencidos. Este valor representa o quanto à empresa ficou inadimplente com seus fornecedores.
* **Vl Juros Pagos**(HLI\_VJUPAG): indica o valor total dos juros pagos, inclusive multa.
* **Vl Desconto Recebido**(HLI\_VDESCR): indica o valor total de todos os descontos obtidos.
* **Prazo Pagamento** (HLI\_PRZPAG): essa medida indica a diferença em dias entre a data de pagamento e a data de emissão do título.
* **Vl Substituição Pagamento**(HLI\_VSUBPG): Não se aplica

# 1.3 Contas a Pagar – Vencimento (HLD)

O processo de extração para o contas a pagar vencimento, leva em consideração apenas os lançamentos financeiros com saldo a pagar que estão compreendidos para os tipos de documento parametrizado e dentro do período definido no plano de extração, utilizando como filtro, a data de vencimento dos lançamentos.   
Caso existam faturas, serão considerados apenas os vencimentos de fatura e não os lançamentos faturados.  
Para informar os tipos de documentos a pagar que serão considerados no momento da extração, acesse os parâmetros:  
***Menu Integração-> Ferramentas-> Parâmetros**> TOTVS Business Analytics->Tipos de documentos a pagar.***

******Processamento******

Tabela de Destino: **HLD**

***Indicadores Diretos:***

* **Vl Vencimento**(HLD\_VVECTO): indica o valor a pagar ou o saldo que a empresa tem a pagar junto aos seus fornecedores.
* **Vl Comprado** (HLD\_VCOMPR): essa medida indica o valor dos títulos implantados.
* **Prazo Vencimento**(HLD\_PRZVCT): essa medida indica a diferença em dias entre a data de vencimento e a data de emissão do título.
* **Vl Substituição Vencimento** (HLD\_VSUBVC): Não se aplica

# 1.4 Contas a Receber – Carteira (HLL)

O processo de extração para o contas a receber, leva em consideração apenas os lançamentos financeiros que estão compreendidos para os tipos de documento parametrizados cujo o saldo a receber seja maior que zero.   
Caso existam faturas, serão considerados apenas os vencimentos de fatura e não os lançamentos faturados.  
Para informar os tipos de documentos a receber que serão considerados no momento da extração, acesse os parâmetros:  
***Menu Integração-> Ferramentas-> Parâmetros**> TOTVS Business Analytics->Tipos de documentos a receber.***

******Processamento******

Tabela de Destino: **HLL**

***Indicadores Diretos:***

* **Vl a Receber Carteira**(HLL\_VRECEB): indica o valor do saldo atual disponível para o título a receber.
* **Prazo Vencimento Carteira**(HLL\_ PRZREC): essa medida indica a diferença em dias entre a data de vencimento e a data de emissão do título em carteira.
* **Vl Substituição Carteira** (HLL\_VSUBCT): Não se aplica

# 1.5 Contas a Receber – Recebimento (HLJ)

O processo de extração de contas a receber - recebimento, leva em consideração apenas os lançamentos financeiros a receber que tiveram baixas parciais ou totais que estão compreendidos para os tipos de documento a receber parametrizado e conforme o período definido no plano de extração sendo filtrado pela data de baixa.  
Caso existam faturas, serão considerados apenas os vencimentos de fatura e não os lançamentos faturados.  
Para informar os tipos de documentos a receber que serão considerados no momento da extração, acesse os parâmetros:  
***Menu Integração-> Ferramentas-> Parâmetros**> TOTVS Business Analytics->Tipos de documentos a receber.***

******Processamento******

Tabela de Destino: **HLJ**

***Indicadores Diretos:***

* **Vl Recebido**(HLJ\_VRCBDO): indica o valor recebido pelas cobranças feitas junto aos clientes.
* **Vl Desconto Concedido** (HLJ\_VDESCC): indica o valor total de desconto concedido.
* **Vl Juros Recebidos**(HLJ\_VJUREC): indica o valor total dos juros cobrados.
* **Prazo Recebimento** (HLJ\_PRZREC): essa medida indica a diferença em dias entre a data de recebimento e a data de emissão do título.
* **Vl Substituição Recebimento**(HLJ\_VSUBRC): Não se aplica

# 1.6 Contas a Receber – Vencimento (HLE)

O processo de extração do contas a receber - Vencimento, leva em consideração apenas os lançamentos financeiros com saldo a receber que estão compreendidos para os tipos de documento parametrizado  e conforme o período definido no plano de extração filtrando a data de vencimento dos lançamentos.  
Caso existam faturas, serão considerados apenas os vencimentos de fatura e não os lançamentos faturados.  
Para informar os tipos de documentos a receber que serão considerados no momento da extração, acesse os parâmetros:  
***Menu Integração-> Ferramentas-> Parâmetros**> TOTVS Business Analytics->Tipos de documentos a receber.***

******Processamento******

Tabela de Destino: **HLE**

***Indicadores Diretos:***

* **Vl Vencimento**(HLE\_VVECTO): indica o valor a receber ou o saldo que a empresa tem a receber junto aos seus clientes.
* **Vl Substituição Vencimento** (HLE\_VSUBVC): Não se aplica
* **Vl Faturado** (HLE\_VFATUR): essa medida indica o valor dos títulos implantados.
* **Prazo Vencimento** (HLE\_PRZVCT): essa medida indica a diferença em dias entre a data de vencimento e a data de emissão do título.
Materiais

# 1.1 Carteira de Compras (HKQ)

Extrai os itens das Ordens de Compra nas seguintes condições:  
- Ordens de Compra com status em aberto ou parcialmente faturada;  
- A data do movimento (conforme parâmetro do tipo de movimento) é menor ou igual à data final do período de extração;  
- O código do tipo de movimento está parametrizado como “Carteira de Compras”;  
- A quantidade do item de movimento é maior do que 0 (zero).

***Filtro – Período de extração***

O período de extração são filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

***Processamento***

Tabela de Destino: **HKQ**

***Indicadores Diretos:***

* **Qtde Carteira (HKQ\_QCARTE):** Indica a quantidade do item que está em carteira, ou seja, que ainda não foi entregue pelos fornecedores.
* **Vl Carteira (HKQ\_VCARTE):** Indica o valor total dos itens que estão em carteira, ou seja, que ainda não foi entregue pelos fornecedores.
* **Dias Atrasados Carteira (HKQ\_QDSATR):** Indica a quantidade de dias de atraso relacionada à data prevista para entrega da compra.
* **Qtde Entregas Carteira em Atraso (HKQ\_QENTAT):** Indica o número de entregas em carteira atrasadas.
* **Qtde Entregas Carteira sem Atraso (HKQ\_QENTAN):** Indica o número de entregas em carteira que estão sem atraso.
* **Dias sem Atraso Carteira (HKQ\_QDSANT):** Indica a quantidade de dias sem atraso relacionado à data prevista para entrega da compra.
* **Qtde Entregas Carteira:** Qtde Entregas Carteira sem Atraso + Qtde Entregas Carteira em Atraso.

# 1.2 Gestão de Compras (HKO)

Extrai os itens das Ordens de Compra nas seguintes condições:  
- Ordens de Compra com status em aberto, parcialmente faturada ou faturada;  
- A data do movimento (conforme parâmetro do tipo de movimento) está compreendida entre as datas inicial e final do período de extração;  
- O código do tipo de movimento está parametrizado como “Ordem de Compra”.

***Filtro – Período de extração***

O período de extração são filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

***Processamento***

Tabela de Destino: **HKO**

***Indicadores Diretos:***

* **Qtde Ordens Compra (HKO\_QORDCP):** Indica a quantidade total de itens em ordens emitidas no período selecionado.
* **Qtde Comprada (HKO\_QCOMPR):** Indica a quantidade dos itens que foram comprados em um determinado período em análise.
* **Qtde Comprada Família Material (HKO\_QCPMAT):** Indica a quantidade comprada, convertida para a família de material em um determinado período em análise.
* **Vl Comprado (HKO\_VCOMPR):** Indica o valor dos itens que foram comprados em um determinado período em análise.
* **Vl IPI Comprado (HKO\_VIPICP):** Indica o valor do IPI dos itens que foram comprados.
* **Vl ICMS Comprado (HKO\_VICMCP):** Indica o valor do ICM dos itens que foram comprados.
* **Preço Médio Compra (Valor Comprado / Qtde Comprada):** Indica o preço médio dos itens comprados, que se obtém pela seguinte fórmula: Vl Comprado /Qtde Comprada.
* **Tempo Ressuprimento Interno (Data Emissão Pedido - Data Emissão Ordem):** Não se aplica.
* **Tempo Ressuprimento Previsto (Data Entrega - Data Emissão Ordem):** Indica a quantidade de dias de ressuprimento previsto (data de entrega da ordem de compra - data da ordem de compra).
* **Média Ressuprimento Interno ((Data Emissão Pedido - Data Emissão Ordem) / Qtde Ordens Compra):** Não se aplica.
* **Média Ressuprimento Previsto ((Data Entrega - Data Emissão Ordem) / Qtde Ordens Compra):** Indica a média de dias de ressuprimento previsto por ordem de compra.

# 1.3 Devolução de Compras (HKL)

Extrai os itens das NF de Devolução Compra nas seguintes condições:

- Status do movimento diferente de Cancelado;  
- A data do movimento (conforme parâmetro do tipo de movimento) está compreendida entre as datas inicial e final do período de extração;  
- O código do tipo de movimento está parametrizado como “Devolução de Compra”.

***Filtro – Período de extração***

O período de extração são filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

***Processamento***

Tabela de Destino: **HKL**

***Indicadores Diretos:***

* **Qtde Devolvida (HKL\_QDEVOL):** Indica a quantidade dos itens que foram devolvidas.
* **Qtde Devolvida Família Material (HKL\_QDVFMT):** Indica a quantidade devolvida, convertida para a unidade da família de material.
* **Vl Devolvido (HKL\_VDEVOL):** Indica o valor dos itens que foram devolvidos.
* **Qtde Ordens Devolvidas (HKL\_QORDDV):** Indica a quantidade total de itens de ordens de compras devolvidas.
* **% Qtde Devolvida:** Fórmula Qtde Devolvida / Qtde Recebida.

# 1.4 Recebimento de Compras (HKM)

Extrai os itens das NF de Devolução Compra nas seguintes condições:  
- Status do movimento diferente de Cancelado;  
- A data do movimento (conforme parâmetro do tipo de movimento) está compreendida entre as datas inicial e final do período de extração;  
- O código do tipo de movimento está parametrizado como “Nota Fiscal Compra”.

***Filtro – Período de extração***

O período de extração são filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

***Processamento***

Tabela de Destino: **HKM**

***Indicadores Diretos:***

* **Dias Antecipação (HKM\_QDIAAN):** Indica o número de dias ocorridos entre a data real de entrega (saída da mercadoria) e a data programada no pedido.
* **Dias Atrasado (HKM\_QDIAAT):** Indica o número de dias ocorridos entre a data programada no pedido e a data real de entrega (saída da mercadoria).
* **Qtde Recebida (HKM\_QRECEB):** Indica a quantidade dos itens que foram recebidos.
* **Qtde Recebida Família Material (HKM\_QRECFM):** Indica a quantidade recebida, convertida para família de material.
* **Vl Recebido (HKM\_VRECEB):** Indica o valor líquido dos itens que foram recebidos.
* **Qtde Recebimentos Antecipados (HKM\_QRECAN):** Indica o número de recebimentos realizados antecipadamente, ou seja, antes da data programada.
* **Qtde Recebimentos em Atraso (HKM\_QRECAT):** Indica o número de recebimentos realizados em atraso, ou seja, depois da data programada.
* **Qtde Recebimentos em Dia (HKM\_QRECDT):** Indica o número de recebimentos realizados em dia, ou seja, na data programada.
* **Qtde Recebimentos Únicos (HKM\_QRECUN):** Indica o número de recebimentos realizados onde todo o pedido foi entregue de uma só vez, sem recebimentos parciais.
* **Lead Time Entrega (Dias Antecipação - Dias Atrasado):** Indica o número de dias ocorridos entre a data real de entrega (entrega da mercadoria) e a data programada no pedido.
* **Tempo Ressuprimento Real (Data do Recebimento do Pedido de Compra – Data da Emissão da Ordem de Compra):** Indica o tempo total gasto para completar o ciclo desde o momento em que uma ordem de compra é gerada até a entrega total dos produtos comprados. (Data Recebimento – Data Ordem Compra).
* **Tempo Ressuprimento Previsto (Data da Previsão da Entrega do Pedido de Compra – Data da Emissão da Ordem de Compra):** Não se aplica.
* **% Recebimentos Antecipados (Qtde Recebimentos Antecipados / Qtde Recebimentos):** Indica o percentual de recebimentos antecipados em relação a todos os recebimentos.
* **% Recebimentos Atrasados (Qtde Recebimentos Atrasados / Qtde Recebimentos):** Indica o percentual de recebimentos atrasados em relação a todos os recebimentos.
* **% Recebimentos em Dia (Qtde Recebimentos em Dia / Qtde Recebimentos):** Indica o percentual de recebimentos na data prevista em relação a todos os recebimentos.
* **% Recebimentos sem Atraso (Qtde Recebimentos Antecipados + Qtde Recebimentos em Dia / Qtde Recebimentos):** Indica o percentual de recebimentos sem atraso em relação a todos os recebimentos.
* **% Recebimentos Únicos (Qtde Recebimentos Únicos / Qtde Recebimentos):** Indica o percentual de recebimentos únicos em relação a todos os recebimentos.
* **Média de Antecipações (Dias Antecipação / Qtde Recebimentos Antecipados):** Indica a média de dias de antecipação das compras recebidas de forma antecipada.
* **Média de Atrasos (Dias Atrasados / Qtde Recebimentos em Atraso):** Indica a média de dias de atraso das compras recebidas com atraso.
* **Qtde Recebimentos (Qtde Recebimentos Antecipados + Qtde Recebimentos em Atraso + Qtde Recebimentos em Dia):** Indica o número total de recebimentos, considerando atrasados, antecipados e em dia.
* **Lead Time Interno (Data Emissão do Pedido - Datas Emissão da Ordem):** Indica o número de dias entre a data de abertura de uma solicitação de compras e o dia em que o pedido de compras originado da mesma foi aprovado. Avalia o tempo de trâmites internos, e o processo de cotação e desenvolvimento de novos fornecedores.

# 1.5 Estoque Diário (HKS)

Extrai os dados das movimentações de estoque (movimentos parametrizados para afetar o saldo 2) no período de extração determinado, utilizando como base para extração a data do movimento (conforme parâmetro do tipo de movimento).

***Filtro – Período de extração***

O período de extração são filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

***Processamento***

Tabela de Destino: **HKS**

***Indicadores Diretos:***

* **Qtde Entrada (HKS\_QENTRA):** Indica a quantidade total de entrada para o item no estoque.
* **Qtde Saída (HKS\_QSAIDA):** Indica a quantidade total de saída para o item no estoque.
* **Vl Entradas (HKS\_VENTRA):** Indica o valor total de entrada para o item no estoque.
* **Vl Saídas (HKS\_VSAIDA):** Indica o valor total de saída para o item no estoque.
* **Qtde Saldo Médio (HKS\_QSDMED):** Não se aplica.
* **Qtde Saída Acumulada (HKS\_QSAIAC):** Não se aplica.
* **Vl Saldo Médio (HKS\_VSDMED):** Indica o saldo médio relativo aos valores de entrada e saída, movimentadas no período de análise.
* **Dias de Giro (HKS\_QGIRO):** Não se aplica.
* **Vl Material no Estoque (HKS\_VMATES):** Não se aplica.
* **Vl Mão de Obra no Estoque (HKS\_VMOBES):** Não se aplica.
* **Vl GGF no Estoque (HKS\_VGGFES):** Não se aplica.
* **% Giro (Qtde Saída/Qtde Saldo Médio):** Não se aplica.
* **Qtde Movimentos (Count(Qtde Saldo Médio)):** Não se aplica.

# 1.6 Estoque Mensal (HKR)

Extrai os dados das movimentações de estoque (movimentos parametrizados para afetar o saldo 2) no período de extração determinado, utilizando como base para extração a data do movimento (conforme parâmetro do tipo de movimento).

***Filtro – Período de extração***

O período de extração são filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

***Processamento***

Tabela de Destino: **HKR**

***Indicadores Diretos:***

* **Qtde Saldo Inicial (HKR\_QINISD):** Indica o saldo de quantidades antes da movimentação no estoque.
* **Qtde Saldo Final (HKR\_QFINSD):** Indica o saldo de quantidades após a movimentação no estoque.
* **Vl Saldo Inicial (HKR\_VINISD):** Indica o saldo de valores antes da movimentação no estoque.
* **Vl Saldo Final (HKR\_VFINSD):** Indica o saldo de valores após a movimentação no estoque.
* **Qtde Saldo Médio (HKR\_QSDMED):** Não se aplica.
* **Vl Saldo Médio (HKR\_VSDMED):** Não se aplica.
* **Qtde Consumo Real (HKR\_QEREAL):** Indica a quantidade de consumo real do item.
* **Vl Consumo Previsto (HKR\_VEPREV):** Não se aplica.
* **Vl Consumo Real (HKR\_VEREAL):** Indica o valor de consumo real do item.
* **Vl Estoque de Segurança (HKR\_VESEGU):** Não se aplica.
* **Qtde Consumo Previsto (HKR\_QEPREV):** Não se aplica.
* **% Variação Vl Consumo ((Vl Consumo Real/Vl Consumo Previsto) – 1):** Não se aplica.
* **Qtde Movimentos (Count(Qtde Saldo Médio)):** Não se aplica.
* **Vl Preço Unitário (Vl Final do Saldo / Qtde Final do Saldo):** Indica o valor do preço unitário do item baseado no saldo do estoque. (Vl Final do Saldo / Qtde Final do Saldo).

# 1.7 Saldo de Estoque Diário (HKT)

Extrai os dados das movimentações de estoque (movimentos parametrizados para afetar o saldo 2) no período de extração determinado, utilizando como base para extração a data do movimento (conforme parâmetro do tipo de movimento).

***Filtro – Período de extração***

O período de extração são filtros de data que serão considerados na extração das informações do ERP. Para este fato é necessário informar qual será o período de extração. O período de extração pode ser parametrizado por fato, período fixo ou variável.

******Processamento******

Tabela de Destino: **HKT**  
***Indicadores Diretos:***

* **Qtde Saldo Inicial (HKT\_QINISD):** Indica o saldo de quantidades antes da movimentação no estoque.
* **Qtde Saldo Final (HKT\_QFINSD):** Indica o saldo de quantidades após a movimentação no estoque.
* **Vl Saldo Inicial (HKT\_VINISD):** Indica o saldo de valores antes da movimentação no estoque.
* **Vl Saldo Final (HKT\_VFINSD):** Indica o saldo de valores após a movimentação no estoque.
* **Vl Preço Unitário (Vl Final do Saldo / Qtde Final do Saldo):** Indica o valor do preço unitário do item baseado no saldo do estoque.
RH

# 1.1 Fato Folha de Pagamento (HLP)

 As regras de extração, os campos atributos da fato folha de pagamento e os campos que geram dados para métricas diretas, estão descritas abaixo:

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Empresa (HLP\_EMPRES) | Código de Coligada. |
| Estabelecimento (HLP\_ESTABL) | Código de Filial. |
| Unidade de Negócio (HLP\_UNDNEG) | Ausente |
| Moeda (HLP\_MOEDA) | "R$" |
| Sindicato (HLP\_SINDIC) | Código de Sindicato vinculado ao funcionário. |
| Turno (HLP\_TURNO) | Código de horário de trabalho do funcionário. |
| Evento (HLP\_EVENTO) | Código do Evento da Ficha Financeira. |
| Mão de Obra (HLP\_TIPMOB) | Ausente |
| Plano Centro Custo (HLP\_PLCCST) | Ausente |
| Centro de Custo (HLP\_CCUSTO) | Centro de Custo da Seção do funcionário. |
| Colaborador (HLP\_COLABR) | Código de Pessoa. |
| Cargo(HLP\_CARGO) | Código de Função. |
| Nível Hierárquico (HLP\_NIVHIE) | Código do Cargo do funcionário. |
| Faixa Salarial (HLP\_FXASAL) | Tabela Salarial do funcionário. |
| Categoria Salarial (HLP\_CATSAL) | Código de recebimento |
| Região (HLP\_REGIAO) | Código de Município + Código de UF |
| Estado Civil (HLP\_ESTCIV) | Estado Civil do funcionário |
| Faixa Etária (HLP\_FXAETA) | Faixa Etária do Colaborador de acordo com faixas determinadas em parâmetro. |
| Grau de Instrução (HLP\_GRAINS) | Código do grau de Instrução da Pessoa. |
| Tempo Casa (HLP\_TPCASA) | Tempo total desde que o funcionário foi admitido, até a data atual. |
| Tempo Cargo (HLP\_TPCARG) | Tempo total em que o funcionário ocupa o cargo atual. |
| Relação Trabalho (HLP\_RELTRB) | Tipo do Cadastro do funcionário. |
| Situação Colaborador (HLP\_SITCLB) | Código de situação do funcionário. |
| Localidade (HLP\_LOCALI) | Ausente |
| Prestador Serviço (HLP\_PRESRV) | Ausente |
| Plano Lotação (HLP\_PLOTAC) | Ausente |
| Unidade Lotação (HLP\_ULOTAC) | Ausente |
| Seção (HLP\_SECAO) | Código de seção a qual o funcionário pertence. |

### ***Processamento***

Tabela de Destino: **HLP**

***Indicadores Diretos:***

****•** Qtde Dependentes (HLP\_QDEPEN)** - Indica a quantidade de dependentes relacionada a cada colaborador. O valor inclui os colaboradores demitidos no mesmo período.

 Regra: A extração considera a quantidade de dependentes de IR.

**• Qtde Horas Extras (HLP\_QHREXT)** - Indica a quantidade total de horas extras realizadas pelos colaboradores e pagas na folha de pagamento.

Regra: No Parametrizador de Integrações, os eventos parametrizados como eventos de Horas Extras, serão recuperados na ficha financeira dos funcionários e serão somadas as Referências dos respectivos eventos a fim de compor o valor da **Qtde de Horas Extras**

**• Qtde Horas Previstas (HLP\_QHRPRV)** - Indica a quantidade de horas de trabalho previstas para os colaboradores de acordo com o turno.

Regra: Na extração será recuperada a Jornada de trabalho da época.

**• Qtde Colaboradores Calculados (HLP\_QCBCAL)** - Indica o total de colaboradores que tiveram a folha de pagamento calculada.

Regra: A extração é realizada a partir da existência de eventos na Ficha Financeira (folha de pagamento calculada), para os colaboradores.

**• Qtde Colaboradores Não Calculados (HLP\_QCBNCA)** – Ausente no RM.

**• Qtde Horas Trabalhadas (HLP\_QHRTRB)** - Indica a quantidade total de horas trabalhadas pelos colaboradores.

Regra: No Parametrizador de Integrações, os eventos parametrizados como eventos de Salário, serão recuperados na ficha financeira dos funcionários e serão somadas as Referências dos respectivos eventos a fim de compor a **Qtde de Horas Pagas**. Caso o evento seja do tipo Dia, o valor encontrado de Referência será dividido por 30 e multiplicado pela Jornada Mensal da época.

**• Vl Benefícios Colaborador (HLP\_VBENCB)** - Indica o valor total de benefícios pagos pelos colaboradores.

Regra: No Parametrizador de Integrações, os eventos parametrizados como eventos de Benefícios, serão recuperados na ficha financeira dos funcionários e serão somados os Valores dos respectivos eventos a fim de compor o **Vl Benefícios Colaborador**.

**• Vl Benefícios Empresa (HLP\_VBENEM)** - Indica o valor total de benefícios pagos pela empresa aos colaboradores.

Regra: No Parametrizador de Integrações, os eventos parametrizados como eventos de Benefícios da Empresa, serão recuperados na ficha financeira dos funcionários e serão somados os Valores dos respectivos eventos a fim de compor o **Vl Benefícios Empresa**.

**• Vl Desconto Folha Pagamento (HLP\_VDESFP)** - Indica o valor dos descontos na folha de pagamento dos colaboradores.

Regra: Na extração serão recuperados os eventos do tipo desconto para somar os valores de descontos. Com exceção dos eventos Código de Cálculo 43 - Líquido de Férias e do evento de Líquido de rescisão do tipo Desconto, que tiver associado ao Parametrizador do Sistema, em Rescisão | Líquido de Rescisão - campo Evento Desconto Líquido Rescisão.

**• Vl Encargos Colaborador (HLP\_VENCCB)** - Indica o valor total de encargos sociais pagos pelo colaborador.

Regra: No Parametrizador de Integrações, os encargos parametrizados como encargos do Colaborador, serão recuperados em encargos calculados e serão somados os respectivos valores por funcionário a fim de compor o **Vl Encargos Colaborador**.

**• Vl Encargos Empresa (HLP\_VENCEM)** - Indica o valor total de encargos sociais pagos pela empresa.

Regra: No Parametrizador de Integrações, os encargos parametrizados como encargos da Empresa, serão recuperados e somados os respectivos valores por funcionário a fim de compor o **Vl Encargos Empresa**.

**• Vl Eventos Especiais (HLP\_VEVESP)** - Indica o valor dos eventos especiais da folha de pagamento.

Regra: No Parametrizador de Integrações, os encargos parametrizados como encargos da Empresa, serão recuperados e somados os respectivos valores por funcionário a fim de compor o **Vl Eventos Especiais**.

**• Vl Folha Pagamento (HLP\_VFLHPG)** - Indica o valor dos eventos da folha de pagamento dos colaboradores. Quando totalizado por colaborador, possui o valor recebido por este.

Regra: O total de proventos menos o total de descontos compõe o valor dessa métrica. Os eventos de Proventos e Descontos devem estar parametrizados no Parametrizador da Integração.

**• Vl Horas Extras (HLP\_VHREXT)** - Indica o valor total de horas extras realizadas pelos colaboradores e pagas na folha de pagamento.

Regra: No Parametrizador de Integrações, os eventos parametrizados como eventos de Horas Extras, serão recuperados na ficha financeira dos funcionários e serão somados os Valores dos respectivos eventos a fim de compor o valor de Horas Extras

**• Vl Horas Trabalhadas (HLP\_VHRTRB)** - Indica o valor total de horas trabalhadas pelos colaboradores.

Regra: No Parametrizador de Integrações, os eventos parametrizados como eventos de Horas Trabalhadas, serão recuperados na ficha financeira dos funcionários e serão somados os Valores dos respectivos eventos a fim de compor o valor de **Vl Horas Trabalhadas.**

# 1.2 Fato Vida Profissional (HLQ)

As regras de extração, os campos atributos da vida profissional e os campos que geram dados para métricas diretas, estão descritas abaixo:

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Empresa (HLQ\_EMPRES) | Código de Coligada. |
| Estabelecimento (HLQ\_ESTABL) | Código de Filial. |
| Unidade de Negócio (HLQ\_UNDNEG) | Ausente |
| Moeda (HLQ\_MOEDA) | "R$" |
| Mão de Obra (HLQ\_TIPMOB) | Ausente |
| Motivo Movimentação (HLQ\_MOTMOV) | Ausente |
| Tipo Motivo (HLQ\_TIPMOT) | Ausente |
| Categoria Salarial (HLQ\_CATSAL) | Código de recebimento |
| Plano Centro Custo (HLQ\_PLCCST) | Ausente |
| Centro de Custo (HLQ\_CCUSTO) | Código de Centro de Custo da Seção do Funcionário. |
| Turno (HLQ\_TURNO) | Código de horário de trabalho do funcionário. |
| Faixa Salarial (HLQ\_FXASAL) | Tabela Salarial do funcionário. |
| Sindicato (HLQ\_SINDIC) | Código de Sindicato vinculado ao funcionário. |
| Situação Colaborador (HLQ\_SITCLB) | Código de situação do funcionário. |
| Colaborador (HLQ\_COLABR) | Código de Pessoa. |
| Região (HLQ\_REGIAO) | Código de Município + Código de UF |
| Cargo (HLQ\_CARGO) | Código de Função do Funcionário. |
| Nível Hierárquico (HLQ\_NIVHIE) | Código do Cargo do funcionário. |
| Estado Civil (HLQ\_ESTCIV) | Estado Civil do funcionário |
| Faixa Etária (HLQ\_FXAETA) | Faixa Etária do Colaborador de acordo com faixas determinadas em parâmetro. |
| Grau de Instrução (HLQ\_GRAINS) | Código do grau de Instrução da Pessoa. |
| Tempo Casa (HLQ\_TPCASA) | Tempo total desde que o funcionário foi admitido, até a data atual. |
| Tempo Cargo (HLQ\_TPCARG) | Tempo total em que o funcionário ocupa o cargo atual. |
| Relação Trabalho (HLQ\_RELTRB) | Tipo do Cadastro do funcionário. |
| Prestador Serviço (HLQ\_PRESRV) | Ausente |
| Plano Lotação (HLQ\_PLOTAC) | Ausente |
| Unidade Lotação (HLP\_ULOTAC) | Ausente |
| Localidade (HLQ\_LOCALI) | Ausente |
| Seção (HLQ\_SECAO) | Código de seção do funcionário. |

### ***Processamento***

Tabela de Destino: **HLQ**

***Indicadores Diretos:***

**• Qtde Aumento Salarial (HLQ\_QAMSAL)** - Indica a quantidade de colaboradores que receberam aumento salarial.

Regra: A extração irá atribuir valor 1 neste campo, no mês que o funcionário tiver aumento salarial e na mesma tiver alteração de função.

**• Qtde Colaboradores (HLQ\_QCOLAB)** - Indica a quantidade de colaboradores que trabalharam considerando admitidos e demitidos no mesmo período.

Regra: Na extração, para todos os funcionários será atribuído 1 no campo **Qtde Colaboradores**, exceto: No mês que o funcionário for transferido de Localidade (transferência de filial ou coligada)

**• Qtde Colaboradores Admitidos (HLQ\_QCBADM)** - Indica a quantidade de colaboradores que ingressaram na empresa.

Regra: Na extração, para no mês que o funcionário for admitido, receberá valor 1 neste campo.

**• Qtde Colaboradores Demitidos (HLQ\_QCBDEM)** - Indica a quantidade de colaboradores que foram desligados da empresa.

Regra: Na extração, no mês que o funcionário for demitido, receberá valor 1 neste campo.

**• Qtde Dependentes (HLQ\_QDEPEN)** - Indica a quantidade de dependentes relacionada a cada colaborador. O valor inclui os colaboradores demitidos no mesmo período.

Regra: A extração considera a quantidade de dependentes de IR.

**• Qtde Dias Férias (HLQ\_QDFERI)** - Indica o saldo de dias de férias dos colaboradores.

Regra: Quantidade de dias de férias gozadas no mês.

**• Qtde Dias Férias a Vencer (HLQ\_QDFAVC)** - Indica a quantidade de dias de férias, a vencer, que os colaboradores terão direito.

Regra: A extração soma os avos do mês atual até o mês de fim do período aquisitivo.

**• Qtde Dias Férias Vencidas (HLQ\_QDFVCD)** - Indica a quantidade de dias de férias, já vencidos, que os colaboradores têm direito.

Regra: A extração soma os avos vencidos que ainda não foram gozados.

**• Qtde Horas Afastamento (HLQ\_QHRAFT)** - Indica a quantidade de horas que os colaboradores ficaram afastados da empresa.

Regra: De acordo com o histórico de afastamento do funcionário, o sistema irá multiplicar a quantidade de dias de afastamento pela jornada diária do funcionário.

**• Qtde Horas Previstas (HLQ\_QHRPRV)** - Indica a quantidade de horas de trabalho previstas para os colaboradores de acordo com o turno.

Regra: A extração considera a jornada mensal do funcionário e realiza o cálculo de horas de jornada relativas a quantidade de dias do mês.

**• Qtde Promovidos (HLQ\_QPROMO)** - Indica a quantidade de colaboradores que foram promovidos, ou seja, mudaram de cargo com aumento salarial.

Regra: A extração atribuirá valor 1 nesse campo quando houver alteração de Função e Alteração salarial com mesma data.

**• Qtde Realocação (HLQ\_QRELOQ)** - Indica a quantidade de colaboradores que mudaram de cargo.

Regra: A extração atribuirá valor 1 nesse campo quando houver alteração de Função sem que tenha havido alteração salarial.

**• Qtde Transferência Setor (HLQ\_QTRANS)** – Indica a quantidade de colaboradores que foram transferidos de setor.

Regra: Na extração será atribuído valor 1 nesse campo, caso no mês, o funcionário tenha sido alterado de seção pertencente a mesma filial da seção origem.

**• Qtde Transferência Localidade (HLQ\_QTRANL)** – Indica a quantidade de colaboradores que foram transferidos de localidade geográfica.

Regra: será atribuído valor 1 nesse campo, caso no mês, o funcionário tenha sido transferido para outra filial ou coligada pelos tipos: 5 – Transferência sem ônus para cedente ou; 6 – transferência com ônus para cedente.

**• Vl Aumento Salarial (HLQ\_VAMSAL)** - Indica o valor de aumento salarial recebido pelos colaboradores.

Regra: No mês do aumento salarial, a extração irá calcular a diferença do novo salarial pelo salário anterior e irá atribuir o valor a este campo.

**• Vl Custo Bruto Demissão (HLQ\_VCBDEM)** – Indica o valor do custo bruto relacionado à demissão de colaboradores.

Regra: A extração irá somar o valor dos proventos constantes na Rescisão do funcionário e somará o valor da Multa do FGTS, se existir.

**• Vl Custo Líquido Demissão (HLQ\_VCLDEM)** – Indica o valor do custo líquido relacionado à demissão de colaboradores.

Regra: A extração irá fazer a diferença do total de proventos pelo total de descontos calculados na rescisão e irá atribuir a este campo.

**• Absenteísmo (HLQ\_ABSENT)** - Indica em horas, a relação do grau de ausência ao trabalho por horas trabalhadas.

Regra: A extração irá considerar o total de atrasos e faltas dos eventos CC8 descontados no mês.

**• Vl Calculado Absenteísmo (HLQ\_VLABST)** - Indica a valorização do absenteísmo pelo salário/hora.

Regra: A extração irá calcular neste campo o valor da hora trabalhada do funcionário. O cálculo do valor do absenteísmo é calculado pela métrica.

# 1.3 Fato Banco de Horas (HLO)

As regras de extração, os campos atributos de banco de horas e os campos que geram dados para métricas diretas, estão descritas abaixo:

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Empresa (HLO\_EMPRES) | Código de Coligada |
| Estabelecimento (HLO\_ESTABL) | Código de Filial |
| Unidade de Negócio (HLO\_UNDNEG) | Ausente |
| Moeda (HLO\_MOEDA) | R$ |
| Sindicato (HLO\_SINDIC) | Sindicato do funcionário |
| Turno (HLO\_TURNO) | Horário do Funcionário |
| Mão de Obra (HLO\_TIPMOB) | Ausente |
| Plano Centro Custo (HLO\_PLCCST) | Ausente |
| Centro de Custo (HLO\_CCUSTO) | Centro de custo do cadastro da seção do funcionário |
| Colaborador (HLO\_COLABR) | Código de Pessoa |
| Faixa Salarial (HLO\_FXASAL) | Tabela salarial do funcionário |
| Tipo Horas (HLO\_TIPHRS) | Ausente |
| Região (HLO\_REGIAO) | Estado natal do trabalhador |
| Categoria Salarial (HLO\_CATSAL) | Código de Recebimento do cadastro de funcionário. |
| Cargo (HLO\_CARGO) | Função do Funcionário. |
| Nível Hierárquico (HLO\_NIVHIE) | Ausente |
| Estado Civil (HLO\_ESTCIV) | Estado civil do cadastro do funcionário. |
| Faixa Etária (HLO\_FXAETA) | Idade do funcionário enquadrada nas faixas parametrizadas na integração BA. |
| Grau de Instrução (HLO\_GRAINS) | Grau de Instrução definida no cadastro do funcionário. |
| Tempo Casa (HLO\_TPCASA) | Tempo de admissão do funcionário enquadrada na parametrização da integração BA. |
| Tempo Cargo (HLO\_TPCARG) | Tempo no cargo atual enquadrado na parametrização da integração BA. |
| Relação Trabalho (HLO\_RELTRB) | Tipo de Funcionário do cadastro do funcionário. |
| Localidade (HLO\_LOCALI) | Ausente |
| Prestador Serviço (HLO\_PRESRV) | Ausente |
| Plano Lotação (HLO\_PLOTAC) | Ausente |
| Unidade Lotação (HLO\_ULOTAC) | Ausente |
| Seção (HLO\_SECAO) | Código da Seção do Funcionário |

### ***Processamento***

Tabela de Destino: **HLO**

***Indicadores Diretos:***

**• Qtde Horas Banco Horas (HLO\_QBCOHR)** - Indica a quantidade de horas alocadas no banco de horas dos colaboradores.

Regra: No RM, a extração irá considerar os valores da tabela ABANCOHOR, sendo que a extração é mensal (por período), e para essa métrica é calculado o valor do saldo do mês do banco de horas: **TOTAL de extras** (menos) **TOTAL de atrasos** (menos) **TOTAL faltas**.

• **Vl Horas Banco Horas (HLO\_VBCOHR)** - Indica o valor das horas alocadas no banco de horas dos colaboradores.

Regra Condicional: A compensação do banco de horas, depende de cálculos de aplicação de percentual de acréscimo incidentes sobre o valor hora normal.  
 Dessa forma, o extrator do RM irá enviar o valor hora do funcionário para o Gooddata, apenas se o TOTVS Automação de Ponto estiver com o banco de horas parametrizado para considerar o percentual de acréscimo e armazenar essas horas no banco já acrescidas.

O percentual de acréscimo em Banco de Horas é aplicado no TOTVS Automação de Ponto em 2 situações:

(1)     Quando estiver parametrizado nos sindicatos para calcular o acréscimo na hora efetivada: **Somente nessa situação, o Extrator do RM enviará para o Gooddata o valor Hora do Banco.**

(2) Quando não estiver parametrizado serão aplicados os acréscimos na compensação e pagamento do banco na folha: Não situação, o Extrator do RM não enviará para o Gooddata o valor Hora do Banco, pois se o saldo do banco for multiplicado pelo valor/hora do salário do funcionário sem acréscimos, não representaria o valor real devido daquele banco de horas.

**Saldo do Banco acumulado (\_livre0) Saldo do banco anterior + atual**: Métrica Customizada: A extração do saldo de horas do banco de cada mês é guardada no campo \_livre0 da Stage. A métrica irá considerar sempre o último valor relativo ao filtro que for passado no relatório do Gooddata, por exemplo: Se o filtro for janeiro, será apresentado o saldo do banco de janeiro. Se o filtro de janeiro a dezembro, o saldo será relativo a dezembro.

# 1.4 Fato Recrutamento (HLG)

As regras de extração, os campos atributos de recrutamento e os campos que geram dados para métricas diretas, estão descritas abaixo:

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Empresa (HLG\_EMPRES) | Código de Coligada. |
| Estabelecimento (HLG\_ESTABL) | Código de Filial. |
| Colaborador (HLG\_COLABR) | Código de Pessoa. |
| Grau de Instrução (HLG\_GRAINS) | Código do grau de Instrução da Pessoa. |
| Nível Hierárquico (HLG\_NIVHIE) | Código do Cargo do funcionário. |
| Sindicato (HLG\_SINDIC) | Código de Sindicato vinculado ao funcionário. |
| Moeda (HLG\_MOEDA) | "R$" |
| Seção (HLG\_SECAO) | Código de seção a qual o funcionário pertence. |
| Status Requisição (HLG\_STAREQ) | Código do Status da Requisição. |
| Tipo Requisição (HLG\_TIPREQ) | "1" |

### ***Processamento***

Tabela de Destino: **HLG**

***Indicadores Diretos:***

**• Qtde de Dias para Contratação (HLG\_QTDIAC)** - Indica a quantidade de dias entre a data de abertura da requisição e a data de Admissão.

Regra: A extração totalizará a quantidade de dias entre o início do processo seletivo e a data de admissão dos funcionários participantes do processo.

**• Potencial Desenvolvimento (HLG\_QPOTDV)** - Indica o potencial de desenvolvimento que é calculado pela média ponderada da graduação exigida para a função e a graduação obtida pelo colaborador.

Regra: A extração calculará a média da avaliação de desempenho do funcionário considerado a graduação exigida e a obtida.

**• Valor Salário (HLG\_VLSAL)** - Indica o valor do salário do colaborador.

Regra: A extração considerará o valor do salário no cadastro do funcionário.

# 1.5 Fato Treinamento por Colaborador (HLM)

As regras de extração, os campos atributos de treinamento por colaborador e os campos que geram dados para métricas diretas, estão descritas abaixo:

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Empresa (HLM\_EMPRES) | Código de Coligada. |
| Estabelecimento (HLM\_ESTABL) | Código de Filial. |
| Unidade de Negócio (HLM\_UNDNEG) | Ausente |
| Moeda (HLM\_MOEDA) | "R$" |
| Faixa Salarial (HLM\_FXASAL) | Tabela Salarial do funcionário. |
| Categoria Salarial (HLM\_CATSAL) | Código de recebimento |
| Sindicato (HLM\_SINDIC) | Código de Sindicato vinculado ao funcionário. |
| Turno (HLM\_TURNO) | Código de horário de trabalho do funcionário. |
| Mão de Obra (HLM\_TIPMOB) | Ausente |
| Colaborador (HLM\_COLABR) | Código de Pessoa. |
| Plano Centro Custo (HLM\_PLCCST) | Ausente |
| Centro de Custo (HLM\_CCUSTO) | Centro de Custo da Seção do funcionário. |
| Instituição (HLM\_INSTIT) | Código da Entidade da Turma. |
| Instrutor(HLM\_INSTRU) | Código do Instrutor da Turma. |
| Curso (HLM\_CURSO) | Código de Curso da Turma. |
| Tipo de Curso (HLM\_TIPCUR) | Código de Grupo de Curso |
| Região (HLM\_REGIAO) | Código de Município + Código de UF |
| Estado Civil (HLM\_ESTCIV) | Estado Civil do funcionário |
| Faixa Etária (HLM\_FXAETA) | Faixa Etária do Colaborador de acordo com faixas determinadas em parâmetro. |
| Grau de Instrução (HLM\_GRAINS) | Código do grau de Instrução da Pessoa. |
| Nível Hierárquico (HLM\_NIVHIE) | Código do Cargo do funcionário. |
| Relação Trabalho (HLM\_RELTRB) | Tipo do Cadastro do funcionário. |
| Tempo Casa (HLM\_TPCASA) | Tempo total desde que o funcionário foi admitido, até a data atual. |
| Tempo Cargo (HLM\_TPCARG) | Tempo total em que o funcionário ocupa o cargo atual. |
| Cargo (HLM\_CARGO) | Código de função. |
| Localidade (HLM\_LOCALI) | Ausente |
| Plano Lotação (HLM\_PLOTAC) | Ausente |
| Unidade Lotação (HLM\_ULOTAC) | Ausente |
| Seção (HLM\_SECAO) | Código de seção a qual o funcionário pertence. |
| Bolsa de Estudo (HLM\_BOLSA) | Código de Benefício dentro os Benefícios do Funcionário. |
| Motivo Treinamento (HLM\_MOTTRE) | Ausente |

### ***Processamento***

Tabela de Destino: **HLM**

***Indicadores Diretos:***

**• Qtde Colaboradores Treinados (HLM\_QCTREI)** - Indica a quantidade de colaboradores que participaram de treinamentos já concluídos. Para a apresentação da informação correta desta medida é necessário que sua análise seja realizada em conjunto com a dimensão Curso.

Regra: A extração irá atribuir a quantidade de colaboradores inscritos nos treinamentos cuja a vigência corresponda ao mês.

**• Qtde Horas Treinamento (HLM\_QHTREI)** - Indica a quantidade de horas registradas referente aos treinamentos.

Regra: A extração irá totalizar a carga horária definida nas turmas que tiverem vigente no mês.

**• Vl Investimento Empresa (HLM\_VINVEP)** - Indica o valor do investimento pago pela empresa quando o treinamento se tratar de bolsa de estudo.

Regra: A extração irá totalizar os benefícios definidos com bolsa na parametrização da Integração.

**• Vl Investimento Colaborador (HLM\_VINVCL)** - Indica o valor do investimento pago pelo colaborador bolsista quando o treinamento se tratar de bolsa de estudo.

Regra: A extração irá totalizar o valor do evento de desconto/provento do funcionário referente ao evento parametrizado como bolsa de estudo.

**• Qtde Dias Bolsa Estudo (HLM\_DBOLSA)** - Indica a quantidade total de dias de bolsa de estudos.

Regra: Não se aplica.

**• Qtde Colaboradores Bolsistas (HLM\_QBOLSA)** - Indica a quantidade de colaboradores com bolsa de estudo.

Regra: A extração irá totalizar a quantidade de colabores que possuírem desconto/provento de bolsa na folha de pagamento.

**• Vl Treinamento (HLM\_VTREIN)** - Indica o valor do custo dos treinamentos.

Regra: A extração irá totalizar o valor do treinamento definido no cadastro de turmas.

# 1.6 Fato Treinamento por Custo (HQV)

As regras de extração, os campos atributos de treinamento por custo e os campos que geram dados para métricas diretas, estão descritas abaixo:

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Empresa (HQV\_EMPRES) | Código de Coligada. |
| Estabelecimento (HQV\_ESTABL) | Código de Filial. |
| Unidade de Negócio (HQV\_UNDNEG) | Ausente |
| Moeda (HQV\_MOEDA) | "R$" |
| Faixa Salarial (HQV\_FXASAL) | Tabela Salarial do funcionário. |
| Categoria Salarial (HQV\_CATSAL) | Código de recebimento |
| Sindicato (HQV\_SINDIC) | Código de Sindicato vinculado ao funcionário. |
| Turno (HQV\_TURNO) | Código de horário de trabalho do funcionário. |
| Mão de Obra (HQV\_TIPMOB) | Ausente |
| Colaborador (HQV\_COLABR) | Código de Pessoa. |
| Plano Centro Custo (HQV\_PLCCST) | Ausente |
| Centro de Custo (HQV\_CCUSTO) | Centro de Custo da Seção do funcionário. |
| Instituição (HQV\_INSTIT) | Código da Entidade da Turma. |
| Instrutor(HQV\_INSTRU) | Código do Instrutor da Turma. |
| Curso (HQV\_CURSO) | Código de Curso da Turma. |
| Tipo de Curso (HQV\_TIPCUR) | Código de Grupo de Curso |
| Região (HQV\_REGIAO) | Código de Município + Código de UF |
| Estado Civil (HQV\_ESTCIV) | Estado Civil do funcionário |
| Faixa Etária (HQV\_FXAETA) | Faixa Etária do Colaborador de acordo com faixas determinadas em parâmetro. |
| Grau de Instrução (HQV\_GRAINS) | Código do grau de Instrução da Pessoa. |
| Nível Hierárquico (HQV\_NIVHIE) | Código do Cargo do funcionário. |
| Relação Trabalho (HQV\_RELTRB) | Tipo do Cadastro do funcionário. |
| Tempo Casa (HQV\_TPCASA) | Tempo total desde que o funcionário foi admitido, até a data atual. |
| Tempo Cargo (HQV\_TPCARG) | Tempo total em que o funcionário ocupa o cargo atual. |
| Cargo (HQV\_CARGO) | Código de função. |
| Localidade (HQV\_LOCALI) | Ausente |
| Plano Lotação (HQV\_PLOTAC) | Ausente |
| Unidade Lotação (HQV\_ULOTAC) | Ausente |
| Seção (HQV\_SECAO) | Código de seção a qual o funcionário pertence. |
| Bolsa de Estudo (HQV\_BOLSA) | Código de Benefício dentro os Benefícios do Funcionário. |
| Motivo Treinamento (HQV\_MOTTRE) | Ausente |

### ***Processamento***

Tabela de Destino: **HQV**

# 1.7 Reclamações Trabalhistas (HLF)

As regras de extração, os campos atributos de reclamações trabalhistas e os campos que geram dados para métricas diretas, estão descritas abaixo:

|  |  |
| --- | --- |
| **Campo** | **Descrição** |
| Empresa (HLF\_EMPRES) | Código de Coligada. |
| Estabelecimento (HLF\_ESTABL) | Código de Filial. |
| Reclamante (HLF\_COLREC) | Código da Pessoa. |
| Grau de Instrução (HLF\_GRAINS) | Código do grau de Instrução da Pessoa |
| Nível Hierárquico (HLF\_NIVHIE) | Código do Cargo do funcionário. |
| Sindicato(HLF\_SINDIC) | Código de Sindicato vinculado ao funcionário. |
| Situação Colaborador (HLF\_SITCLB) | Código de situação do funcionário. |
| Tempo Casa (HLF\_TPCASA) | Tempo total desde que o funcionário foi admitido, até a data atual. |
| Tempo Cargo (HLF\_TPCARG) | Tempo total em que o funcionário ocupa o cargo atual. |
| Seção (HLF\_SECAO) | Código de seção a qual o funcionário pertence. |

***Processamento***

Tabela de Destino: **HLF**

***Indicadores Diretos:***

**• Qtde Reclamações (HLF\_QTRECL)** - Indica o número de reclamações trabalhistas.

Regra: A extração totalizará no mês a quantidade de reclamações trabalhista incluídas.

**Atenção**

|  |
| --- |
| Além das métricas descritas, há as métricas indiretas que são compostas por cálculos utilizando as métricas diretas. |

Educacional

# 1.1 Fato de Alunos (HHF)

Extrai informações sobre os alunos matriculados na instituição de ensino conforme o período definido no plano de extração. Os valores são quebrados mensalmente por empresa, filial, nível de ensino, curso, habilitação, período letivo, turno, modalidade, área de conhecimento e tipo do curso. Para correta visualização das informações no TOTVS Smart Analytics, fica obrigatório o preenchimento dos campos "Data de Início" e "Data de Término" ou "Previsão de Término" no cadastro do período letivo, e dos campos "Modalidade", "Área" (apenas Ensino Superior), "Presencial/Distância" (apenas Ensino Superior) no cadastro de curso. Além disso, é importante que no projeto do TOTVS Smart Analytics o filtro de "Período (Datas)" equivalha ao período letivo selecionado no filtro "Período Letivo"

|  |  |
| --- | --- |
| Campo | Descrição |
| Empresa (HHF\_EMPRES) | Código da coligada |
| Estabelecimento (HHF\_ESTABL) | Código da filial |
| Nível de Ensino (HHF\_NIVENS) | Nível de ensino (Básico ou Superior) |
| Curso (HHF\_CURSOE) | Curso da instituição de ensino |
| Habilitação (HHF\_HABILI) | Habilitação do curso |
| Período Letivo (HHF\_PERLET) | Período letivo |
| Turno (HHF\_TURENS) | Turno do curso |
| Modalidade (HHF\_MODCUR) | Modalidade do curso (Presencial ou EAD) |
| Área de Conhecimento (HHF\_ARECON) | Área de conhecimento do curso |
| Tipo do Curso (HHF\_TIPCUR) | Tipo do curso |

**Processamento:**

Tabela de Destino: HHF

**Indicadores Diretos:**

* **Quantidade de Alunos Base (HHF\_QTDBAS)** – Indica a quantidade de alunos ativos no mês anterior ao período de datas selecionado.   
  Regra: A extração considera:
  + Parametrização de alunos ativos, curso educacional, período letivo.
  + Data da matrícula deve ser menor que a data final de extração (alterada mês a mês até a data final escolhida na extração).
  + Data da matrícula deve estar dentro das datas início e término ou início e previsão de término do período letivo ou anterior a data de início do período letivo.
  + Data da matricula deve ser menor que a data do inicio do periodo selecionado.
  + Data final de extração deve estar dentro das datas início e término ou início e previsão de término do período letivo.

* **Quantidade de Alunos Evadidos (HHF\_QTDEVA)** – Indica a quantidade de alunos que evadiram da instituição de ensino no mês.   
  Regra: A extração considera:
  + Parametrização de alunos evadidos, curso educacional, período letivo.
  + Data de alteração do status no período letivo deve estar dentro do período de extração (alterada mês a mês até a data final escolhida na extração).
  + Data inicial e final do período de extração deverão estar dentro das datas início e término ou início e previsão de término do período letivo.

* **Quantidade de Alunos Bolsistas (HHF\_QTDBOL)** – Indica a quantidade de alunos ativos na instituição que possui algum tipo de bolsa ativa (inclusive FIES).  
  Regra: A extração considera:
  + Parametrização de alunos ativos, curso educacional, período letivo.
  + Data da matrícula deve ser menor que a data final de extração (alterada mês a mês até a data final escolhida na extração).
  + Data da matrícula deve estar dentro das datas início e término ou início e previsão de término do período letivo.
  + Data final de extração deve estar dentro das datas início e término ou início e previsão de término do período letivo.

* **Quantidade de Alunos com FIES (HHF\_QTDFIE)** – Indica a quantidade de alunos ativos na instituição que possui financiamento do curso através do FIES.  
  Regra: A extração considera:   
  + Parametrização de alunos ativos, curso educacional, período letivo.
  + Marcação da flag “FIES” no cadastro de bolsa no TOTVS Educacional.
  + Data da matrícula deve ser menor que a data final de extração (alterada mês a mês até a data final escolhida na extração).
  + Data da matrícula deve estar dentro das datas início e término ou início e previsão de término do período letivo.
  + Data final de extração deve estar dentro das datas início e término ou início e previsão de término do período letivo.

* **Quantidade de Alunos Formados (HHF\_QTDFOR)** – Indica a quantidade de alunos formados no mês.  
  Regra: A extração considera:   
  + **Ensino Superior**  
    - Parametrização de egresso de alunos, curso educacional, período letivo.
    - Data de conclusão de curso deve estar dentro do período de extração quando o parâmetro "Considerar a Data de Conclusão de Curso" para indicar Egresso do Aluno ao invés da Situação de Matrícula (apenas Ensino Superior)" estiver marcado.
    - Data de alteração deve estar dentro do período de extração (alterada mês a mês até a data final escolhida na extração).
    - Data inicial e final do período de extração deverão estar dentro das datas início e término ou início e previsão de término do período letivo.
  + **Ensino Básico**
    - Parametrização de egresso de alunos, última série egresso, curso educacional, período letivo.
    - Data de alteração deve estar dentro do período de extração (alterada mês a mês até a data final escolhida na extração).
    - Data inicial e final do período de extração deverão estar dentro das datas início e término ou início e previsão de término do período letivo.

* **Quantidade de Novos Alunos (HHF\_QTDNOV)** – Indica a quantidade de novos alunos no mês.  
  Regra: A extração considera:
  + Parametrização de alunos ativos, curso educacional, período letivo.
  + Data de matrícula deve estar dentro do período de extração (alterada mês a mês até a data final escolhida na extração).
  + Data da matrícula deve estar dentro das datas início e término ou início e previsão de término do período letivo
  + Data inicial e final do período de extração deverão estar dentro das datas início e término ou início e previsão de término do período letivo.
  + Não deve existir matrícula em outro período letivo para o aluno.
  + Aluno não pode ter sido transferido de outro curso.
  + Último status do aluno no mês de entrada no curso deve ser um dos status parametrizado para os indicadores de aluno ativo, evadido ou transferido internamente para outro curso da instituição de ensino.

* **Quantidade de Alunos Ativos (HHF\_QTDTOT)** – Indica a quantidade de alunos ativos no mês.  
  Regra: A extração considera:
  + Parametrização de alunos ativos, curso educacional, período letivo.
  + Data da matrícula deve ser menor que a data final de extração (alterada mês a mês até a data final escolhida na extração).
  + Data da matrícula deve estar dentro das datas início e término ou início e previsão de término do período letivo, ou anterior à data de início do período letivo.
  + Data final de extração deve estar dentro das datas início e término ou início e previsão de término do período letivo.
* **Quantidade de Transferência Interna Entrada (HHF\_LIVRE0)** – Indica a quantidade de transferências intena de entrada no curso.  
  Regra: A extração considera:
  + Parametrização de curso educacional, período letivo, transferência interna.
  + Data da matrícula deve ser menor que a data final de extração (alterada mês a mês até a data final escolhida na extração).
  + Data da matrícula deve estar dentro das datas início e término ou início e previsão de término do período letivo, ou anterior à data de início do período letivo.
  + Data final de extração deve estar dentro das datas início e término ou início e previsão de término do período letivo.
* **Quantidade de Transferência Interna Saída (HHF\_LIVRE1)** – Indica a quantidade de transferências intena de saída do curso.  
  Regra: A extração considera:
  + Parametrização de curso educacional, período letivo, transferência interna.
  + Data da matrícula deve ser menor que a data final de extração (alterada mês a mês até a data final escolhida na extração).
  + Data da matrícula deve estar dentro das datas início e término ou início e previsão de término do período letivo, ou anterior à data de início do período letivo.
  + Data final de extração deve estar dentro das datas início e término ou início e previsão de término do período letivo.

**Métricas:**

Métricas são indicadores que são utilizados para construção dos relatórios no TOTVS Smart Analytics. A fato de alunos possui várias metrícas no projeto padrão do Educacional, elas estão detalhadas na documentação sobre métricas e variáveis: [saiba mais](http://tdn.totvs.com/display/PROT/TOTVS+Smart+Analytics+-+P12#TOTVSSmartAnalytics-P12-Educacional).

**Variáveis:**

As variáveis são utilizadas com agrupadores de registro de uma dimensão, dessa forma podemos exibir informações nos relatórios de forma agrupada. As variáveis relacionadas a fato de alunos estão detalhadas na documentação sobre métricas e variáveis: [saiba mais](http://tdn.totvs.com/display/PROT/TOTVS+Smart+Analytics+-+P12#TOTVSSmartAnalytics-P12-variaveiseducacionalturnos).

**Observações:**

* Os dados a cima são gerados pelo extrator a partir da base RM considerando o tratamento dos registros presentes na tabela SLOGPLETIVO. Por isso, a data inicial do período de extração da fato ALUNO deve ser maior ou igual que a menor data registrada no campo SLOGPLETIVO.DTALTERACAO e essa tabela nunca deve ter seus registros apagados.
* As consultas de conferência, analítica ou sintética, para validação de cada indicador da fato de ALUNO estão disponíveis no processo de "Consulta de Conferência de Indicadores" presente no menu "Educacional -> Integrações -> Smart Analytics". As consultas de conferência podem ser exportadas para arquivo texto ou para o cadastro de "Visões de Dados" presente no menu "Educacional -> Gestão -> Ferramentas de Análise". No cadastro de "Visões de Dados" as consultas de conferência são exportadas para ficarem visíveis a todas as coligadas. Na exportação das consultas de conferência para arquivo texto, se o ambiente for 3 camadas. É importante que as parametrizações apresentadas no link  sejam aplicadas.

# 1.2 Fato de Contabilidade do Educacional (HL9)

Extração do saldo e movimentações das contas contábeis conforme o período definido no plano de extração. Os valores são quebrados mensalmente por empresa, filial, centro de custo e conta contábil dentro do período de extração.

**Processamento:**

Tabela de Destino: HL9

**Indicadores Diretos:**

* **Vl Saldo Inicial Real (HL9\_VSDINI)** – Indica o saldo inicial contábil do período.

* **Vl Débito Real (HL9\_VDREAL)** – Indica o valor do movimento a debito no período.

* **Vl Crédito Real (HL9\_VCREAL)** – Indica o valor do movimento a crédito no período.

* **Vl Saldo Final Real (HL9\_VSDFIN)** – Indica o saldo final contábil do período.

* **Vl Movimento Contábil Real (HL9\_VCTBRL)** – Indica o valor que foi realizado no período.

* **Vl Apuração Resultado (HL9\_VAPURA)** – Indica o valor contábil referente à apuração de resultado (histórico de fechamento).

**Relação Indicadores Contábil x Indicadores Diretos:**

| Indicador Contábil | Indicadores Diretos (tabela HL9) |
| --- | --- |
| Despesas Antecipadas com Bolsas e Gratuidades | Vl Movimento Contábil Real (HL9\_VCTBRL) |
| Contas a Pagar | Vl Apuração Resultado (HL9\_VAPURA) |
| Despesas com Pessoal - Administrativo | Vl Movimento Contábil Real (HL9\_VCTBRL) |
| Despesas com Pessoal - Docente | Vl Movimento Contábil Real (HL9\_VCTBRL) |
| Despesas Operacionais | Vl Movimento Contábil Real (HL9\_VCTBRL) |
| Lucro ou Prejuízo do Exercício | Vl Movimento Contábil Real (HL9\_VCTBRL) |
| Outras Receitas Operacionais | Vl Movimento Contábil Real (HL9\_VCTBRL) |
| Perdas Estimadas em Créditos de Liquidação Duvidosa | Vl Saldo Final Real (HL9\_VSDFIN) |
| Receita Bruta de Vendas e Serviços | Vl Movimento Contábil Real (HL9\_VCTBRL) |
| Receita Líquido de Vendas e Serviços | Vl Movimento Contábil Real (HL9\_VCTBRL) |

**Métricas:**

Métricas são indicadores que são utilizados para construção dos relatórios no TOTVS Smart Analytics. A fato de contabilidade do educacional possui várias metrícas no projeto padrão do Educacional, elas estão detalhadas na documentação sobre métricas e variáveis: [saiba mais](http://tdn.totvs.com/display/PROT/TOTVS+Smart+Analytics+-+P12#TOTVSSmartAnalytics-P12-Educacional).

**Variáveis:**

As variáveis são utilizadas com agrupadores de registro de uma dimensão, dessa forma podemos exibir informações nos relatórios de forma agrupada. As variáveis relacionadas a fato de contabilidade do educacional estão detalhadas na documentação sobre métricas e variáveis: [saiba mais](http://tdn.totvs.com/display/PROT/TOTVS+Smart+Analytics+-+P12#TOTVSSmartAnalytics-P12-variaveiseducacionalturnos).

**Observações:**

* É necessário configurar variáveis no TOTVS Smart Analytics para representar indicadores na montagem de DRE (Demonstração do Resultado do Exercício) das instituições de ensino. Essas variáveis funcionam como agrupadores de contas contábeis.
* A conferência dos valores contábeis podem ser utilizados os relatórios listados abaixo informando o lote zero e/ou as contas contábeis configuradas nas variáveis no TOTVS Smart Analytics:
  + Relatório Balancete presente no menu "BackOffice -> Gestão Contábil -> Relatórios"
  + Relatório Razão presente no menu "BackOffice -> Gestão Contábil -> Relatórios"
  + Consulta de Saldo da Conta presente no menu "BackOffice -> Gestão Contábil -> Escrituração Contábil"
  + Demonstração Contábil presente no menu "BackOffice -> Gestão Contábil -> Escrituração Contábil"
Construção & Projetos

# 1.1 Fato de Custo Previsto(HZA)

Extrai informações sobre o Custo Previsto do cronograma planejado conforme o período definido no plano de extração. Os valores são quebrados mensalmente por empresa, filial, moeda, projeto de construção e período. Para correta visualização das informações no TOTVS Smart Analytics, fica obrigatório o preenchimento dos campos "Empresa", "Estabelecimento" ou "Filial", estabelecimento é o campo filial no Construção & Projetos, e dos campos "Moeda" e "Projeto de Construção" . Além disso, é importante que no projeto do TOTVS Smart Analytics o filtro de "Período (Datas)" equivalha ao período do projeto selecionado no filtro "Período"

|  |  |
| --- | --- |
| Campo | Descrição |
| Empresa (HZA\_EMPRES) | Código da coligada |
| Estabelecimento (HZA\_ESTABL) | Código da filial |
| Moeda (HZA\_MOEDA) | Moeda do Projeto |
| Data (HZA\_DATA) | Data do custo previsto |
| Projeto (HZA\_PROJCO) | Projeto de construção |
| Tarefa (HZA\_TAREPC) | Tarefa |
| Valor (HZA\_VLPREV) | Valor do custo previsto da tarefa |

**Processamento:**

Tabela de Destino: HZA

***Indicadores Diretos:***

**• Valor do Custo Previsto (HZA\_VLPREV)** - Indicativo do custo previsto da tarefa é o valor do cronograma planejado da mesma. Esse valor é calculado para cada período parametrizado para o projeto.

# 1.2 Fato de Avanço Físico (HZB)

Extrai informações sobre o Custo Previsto do cronograma planejado conforme o período definido no plano de extração. Os valores são quebrados mensalmente por empresa, filial, moeda, projeto de construção e período. Para correta visualização das informações no TOTVS Smart Analytics, fica obrigatório o preenchimento dos campos "Empresa", "Estabelecimento" ou "Filial", estabelecimento é o campo filial no Construção & Projetos, e dos campos "Moeda", "Projeto de Construção" . Além disso, é importante que no projeto do TOTVS Smart Analytics o filtro de "Período (Datas)" equivalha ao período do projeto selecionado no filtro "Período"

|  |  |
| --- | --- |
| Campo | Descrição |
| Empresa (HZB\_EMPRES) | Código da coligada |
| Estabelecimento (HZB\_ESTABL) | Código da filial |
| Data (HZB\_DATA) | Data do avanço físico |
| Projeto (HZB\_PROJCO) | Projeto de construção |
| Tarefa (HZB\_TAREPC) | Tarefa |
| Percentual Realizado (HZB\_REALIZ) | Percentual realizado da tarefa |

**Processamento:**

Tabela de Destino: HZB

***Indicadores Diretos:***

**• Percentual Realizado da Tarefa (HZB\_REALIZ)** - Indica o percentual realizado da tarefa em relação a obra. O valor deste campo em percentual é obtido da seguinte forma: (Percentual da tarefa do cronograma realizado \* Percentual da tarefa na Planilha) / 100. Esse valor é calculado para cada período parametrizado para o projeto.

consulte: [Onde encontro o download do Agent?](http://tdn.totvs.com/pages/viewpage.action?pageId=235312097) [Como preencho o arquivo my.properties do Agent ?](http://tdn.totvs.com/pages/viewpage.action?pageId=228590015)

|  |
| --- |
| R |
