---
content_hash: 7bf8473afd143916a7db98b1b5dc48acb2ec47374f892c4ba2b066d15dd57dd7
fetched_at: '2026-06-29T00:10:25.894871+00:00'
page_id: '506387467'
product: rm
source: tdn-rm
title: Gerar Eventos Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506387467
version: 71
---

falseGeração dos Eventos

Foi criado o processo para geração dos eventos, o processo será executado a partir do evento periódico R-5011/R9011 e\ou R-9015.  
  
O processo EFD-Reinf - Gerar Eventos será exibido em **RM -> Gestão Fiscal -> Obrigações Acessórias -> SPED -> REINF -> Eventos Periódicos.**

**Comportamento do processo:** Quando selecionado um ou muitos Eventos R-5011/R-9011 e\ou R-9015 na visão de Eventos Periódicos, o processo de geração será executado considerando o período de cada evento.  
Se não for selecionado nenhum evento R-5011/R-9011 e\ou R-9015 na visão de Eventos Periódicos, serão considerados todos os Eventos R-5011/R-9011 e\ou R-9015 com Status em Aberto para geração dos demais registros de evento.  
  
Foi disponibilizado no processo a possibilidade de execução via agendamento de Serviço (Aplicado quando o ambiente for 3 camadas).

falseConsistências 

Ao disparar o processo serão feitas as seguintes consistências para geração dos Eventos:  
  
**Períodos de apuração:** No Processo EFD-Reinf - Gerar Eventos → o xml dos eventos 2010, 2020, 2030, 2040, 2050 e 2060 serão gerados somente se os períodos de apurações correspondentes estiverem encerrados.

Na geração dos eventos periódicos se houver período de apuração com status **Aberto** pertinentes aos eventos. O processo ira emitir uma mensagem sinalizando quais períodos devem ser encerrados e sua respectiva filial. 

**Cadastro Parâmetros de Processos**: No Processo EFD-Reinf - Gerar Eventos → o xml dos eventos 4010, 4020 e 4080 serão gerados somente se tiver cadastro no Parâmetros de Processos - EDF REINF.

**Agrupamento por CNPJ:**A geração dos eventos periódicos será realizada na filial Matriz, agrupando os dados de filiais com o mesmo CNPJ, caso o CNPJ possua a mesma raiz mas possua diferença no número *estabelecimento\dígito de verificação (numeração após a barra)* os eventos não vão ser agrupados.

falseRegra válida para os eventos periódicos: R-2010, R-2020, R-2040, R-2050 e R-2060

EXEMPLO:   
  
**Situação 01:**  
Filial 1 com CNPJ xx.xxx.xxx/xxxx-xx possui dados para geração de um evento R-2010   
Filial 2 com CNPJ xx.xxx.xxx/xxxx-xx possui dados para geração de um evento R-2010

**Resultado:** Será gerado um Evento R-2010 com os valores agregados uma vez que os CNPJs são iguais.  
(Salvo regra da chave de geração, o R-2010 por exemplo é gerado por Cliente\Fornecedor nesse caso será agrupado por CNPJ e Cli\for).

**Situação 02:**  
Filial 1 com CNPJ xx.xxx.xxx/xxxx-xx possui dados para geração de um evento R-2010   
Filial 2 com CNPJ xx.xxx.xxx/xxxy-yy possui dados para geração de um evento R-2010

**Resultado:** Serão gerados dois Eventos R-2010 com seus valores pertinentes uma vez que os CNPJs são diferentes.

**Observação:**

Até a versão 12.1.28, se tratando de Filiais SCP não são feitos agrupamentos entre filiais uma vez que esse tipo de Filial possui a geração separada de eventos da Filial Matriz.

A partir da versão 12.1.29, se tratando de Filiais SCP a geração dos eventos depende da flag "Filial SCP transmite REINF através da Filial Matriz" localizada no cadastro da Filial SCP em Anexos | Dados Fiscais, aba "Dados Adicionais".

Comportamento:

* Flag marcada: O sistema gera os eventos da Filial SCP na Filial Matriz.
* Flag desmarcada: Os eventos da Filial SCP são gerados separadamente.

Documento de referência dos [Dados Fiscais](https://tdn.totvs.com/pages/viewpage.action?pageId=422545725#1-1761235669) da Filial

Imagem

**Regra válida para os eventos periódicos: R-4010, R-4020, R-4080**

É necessário parametrizar as Filiais que terão os dados gerados nos Eventos da REINF - no cadastro de Parâmetros de Processos opções ‘**[Filtro de Filiais](https://tdn.totvs.com/display/LRM/Filtro+de+Filiais)**’ e o Campo ‘**[Centralizado](https://tdn.totvs.com/pages/viewpage.action?pageId=490650588)**’ no mesmo cadastro porem na Pasta Parâmetros da REINF.

EXEMPLO:   
  
**Situação 01:**  
Filial 1 com CNPJ xx.xxx.xxx/xxxx-xx possui dados para geração de um evento R-4020   
Filial 2 com CNPJ xx.xxx.xxx/xxxy-yy possui dados para geração de um evento R-4020

**Resultado:**

* Flag marcada ‘Centralizado’: Será gerado um Evento R-4020 na **Filial Matriz**, com informações das duas Filiais.
* Flag desmarcada ‘Centralizado’: Serão gerados dois Eventos R-4020, um para cada Filial.
* O Agrupamento dos Eventos R-4010 e R-4020 será realizado pelo nome do beneficiário, sempre que ele estiver domiciliado no exterior. Para eventos onde o beneficiário é nacional o agrupamento continua sendo por CNPJ.

**Observação:**

Quando tiver configurado alguma Filial SPC para gerar REINF através da Matriz e a mesma tiver um CNPJ diferente do CNPJ da Matriz, o tipo de Geração configurado nos Parametros de Processos deve ser Obrigatóriamente marrcado como "**Centralizado**".
