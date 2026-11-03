---
article_id: 28116821508759
category: Financeiro - Conciliador Backoffice
content_hash: dd7453300d56274f9c19366f948eab0d9983c703eb41e4b2f318ec9ed6a88f99
fetched_at: '2026-06-28T22:37:47.085857+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Conciliação Automática
  no novo Conciliador Backoffice
type: support-article
updated_at: '2025-09-18T13:35:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28116821508759-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-Concilia%C3%A7%C3%A3o-Autom%C3%A1tica-no-novo-Conciliador-Backoffice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28116821478551) Tempo aproximado para leitura: **00****:15:00 min**

**Dúvida**  
Como realizar a Conciliação Automática no novo Conciliador Backoffice?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - 12.1.2210

**Solução**

**1.** Para garantir a configuração adequada do arquivo, recomenda-se validar o relatório de **Extração CNAB (FINR680)**, a fim de verificar se o layout destinado à extração do arquivo de importação está conforme o esperado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28116821480087)

**Importante**

Caso seja identificada alguma divergência, será necessário revisar o arquivo de configuração para verificar a disposição e realizar os ajustes pertinentes.

**2.** Depois que o relatório for validado, acesse a rotina de **Manutenção de Extratos** para importar o extrato bancário.

![Gravar_2024_11_27_15_44_48_120.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28116821483159)

**3.** Para iniciar a conciliação o usuário deve escolher o menu de configuração **0023 - Conciliação Automática no Conciliador Backoffice** para realizar a conciliação automática dos movimentos bancários no sistema.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28116815477783)

**4.** Em seguida, clique em **"Ver Filtros"**, o que abrirá os campos para preenchimento do filtro.

O campo Exibir pode ser preenchido com as seguintes opções: **Ambos, Conciliados ou Não conciliados.** Nessa tela, é **obrigatório** preencher todos os campos **"Data Mov. Ex de"** e **"Data Dispon. de"**. Após o preenchimento, clique em **Aplicar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28116821484823)

**5.** A rotina será aberta em **Dados da Conciliação**, porém, clique em **Dados Não Encontrados**. Nessa tela, será possível validar os movimentos bancários e realizar o processo de **match**.

A seção **Dados Não Encontrados** mostra todos os dados encontrados pelo filtro de conciliação, mas que ainda não tiveram seus matches efetuados.

Para fazer um match entre as tabelas de origem e destino, é necessário escolher os registros correspondentes em cada uma delas.

Ao selecionar **'Aplicar match'**, uma mensagem de confirmação é apresentada para realizar o match manualmente. Depois da confirmação, as informações são atualizadas e aparecem na seção 'Dados da Conciliação'.

![Gravar_2024_11_27_16_17_10_809.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28116815482519)

**6.** Por fim, pressione o botão **"Aplicar Conciliação".**

![Gravar_2024_11_27_16_24_33_888.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28116815483799)

**7. O botão "Ações" possui algumas funcionalidades, tais como:**

* **Ignorar Registros:**

Marca o(s) registro(s) selecionados com o status de ignorado(s).  
Desta forma o registro é movido para a pasta de Dados da Conciliação ficando com o tipo de match igual a Ignorado ()

Ação aplicável apenas a pasta Movimentos Extrato (SIG).

* **Efetivação**

A efetivação é o procedimento de incluir um movimento bancário que está presente no extrato, mas que não está registrado no sistema bancário.   
Normalmente utilizado em **tarifas, imposto sobre transações financeiras (IOF) e outros.**

Clicar em **Ações → Efetivação**, uma janela será aberta com as informações de natureza, histórico e informações contábeis do movimento que está sendo criado.

Após validar o procedimento de Efetivação, teremos:

Registro das transações bancárias nas tabelas do sistema **(FK5/SE5)**;  
Transferência dos dados para a pasta Dados da Conciliação, utilizando o tipo de correspondência Manual.

```
Atenção  
Este processo permite que vários registros sejam selecionados e efetivados com apenas uma   
ação. Caso tenha selecionado 2 registros na tabela de extratos (SIG) e confirmar a   
efetivação, serão gerados 2 registros nas tabelas Movimentos Bancários (FK5).  
  
Neste momento, os registros estão preparados para a conciliação, ou seja, existe um   
registro na Tabela de Extratos (SIG) e um registro nas tabelas de Movimentação Bancária   
(FK5) com match. Apenas ao clicar no botão Aplicar Conciliação (canto superior direito  
 da tela) é que o processo de conciliação será gravado efetivamente.  
  
 
```

* **Cancelar efetivação**

O processo de Cancelar Efetivação é o processo de excluir os movimentos bancários efetivados através do processo de Efetivação.  
Ao selecionar um ou mais registros e clicar no botão Ações → Cancelar Efetivação, o processo cancelará os movimentos efetivados nas tabelas de Movimentação Bancária do sistema (FK5/SE5).

```
Atenção  
  
Esse processo não permite que registros que já estavam no sistema anteriormente e   
realizados por outros processos (movimento bancário manual, baixas, etc.) sejam excluídos.
```

Caso o registro se encontre na aba Dados da Conciliação, basta:

* Posicionar sobre o registro desejado, clicar em (à esquerda na aba dados da Conciliação)
* Ao se abrir uma caixa de opções, clicar em Cancelar Match.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29119053576087)

Após esta ação, os registros terão seus matches cancelados e retornarão para a aba Dados não encontrados, permitindo a aplicação do processo de Cancelar Efetivação

**Importante**

**Ação aplicável apenas a pasta Movimentos Extrato (SIG).**

* **Disponibilidade**

**Disponibilidade** é o processo que permite ajustar as datas de disponibilidade para cada transação bancária no Protheus **(tabelas FK5/SE5)**, visando harmonizar a data da transação no sistema com a registrada no extrato bancário.

* **Ao clicar em Ações → Disponibilidade,** uma tela será exibida com a nova data de disponibilidade e a maneira de aplicá-la:
* **Disponibilidade da Data**  
  Indique a nova data que deseja ter disponível.
* **Quais registros serão afetados por esta data?**

Apenas nos registros da tabela Movimentos Bancários (FK5) na seção Dados não localizados, as datas de disponibilidade foram aplicadas.

* **Registros escolhidos →** A data indicada será aplicada apenas aos registros escolhidos na tela.

**Por Exemplos:**  
Escolhi três registros na tela e as datas correspondentes aos movimentos são 10/11/2023.

Todas as entradas com essa data, sejam elas marcadas ou não, terão como data de disponibilidade a data indicada no respectivo campo.  
Escolhi três registros na tela e as datas correspondentes aos movimentos são 08/11/2023, 09/11/2023 e 10/11/2023.  
Todos os registros, marcados ou não, que apresentem uma das datas mencionadas acima, serão atualizados com a nova data definida.

* **Todas as entradas →** Todas as entradas do processo, marcadas ou não, presentes na tabela Movimentos Bancários (FK5) na seção Dados não localizados.

**Importante**

**Ação aplicável apenas a pasta Movimentos Bancários (FK5).**

**8.** Para cancelar a conciliação, basta clicar nos **três ponto**s e selecionar a opção **Cancelar Match**.

![Gravar_2024_11_27_16_52_06_140.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28116815485207)

**Saiba mais**

[Conciliador BackOffice - Conciliação Bancária Automática](https://tdn.totvs.com.br/pages/releaseview.action?pageId=753654798)
