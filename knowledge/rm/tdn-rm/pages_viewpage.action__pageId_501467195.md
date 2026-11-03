---
content_hash: 07c7db464c483d453e9b33d3e18f442f33e45c024430588e4e4ade73698adbc8
fetched_at: '2026-06-29T00:10:25.113656+00:00'
page_id: '501467195'
product: rm
source: tdn-rm
title: Log de contabilizações por competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=501467195
version: 3
---

---

Na geração da contabilização/estorno por competência do TOTVS Educacional com o objetivo de mostrar um Log de contabilização mais detalhado para o usuário, foi desenvolvida funcionalidade que é possível identificar os períodos de competência de cada contrato contabilizados/estonar com sucesso, erro ou advertência durante o processo. 

Após o processo de contabilização/estorno do contrato será gravado o Log e esse poderá ser visualizado em Log de contabilização por competência.

Nessa nova funcionalidade é possível identificar os períodos de competência de cada contrato contabilizado ou estornado com Status, Origem, Tipo, Operação, Data Contábil, Valores e Memória de Cálculo.

Duas formas de visualizar o Log de contabilização por competência:

* Acesse *Financeiro/Contábil | Contratos *| Anexos *|  Log de contabilizações***
* Acesse *Financeiro/Contábil | Geração | Contabilidade *| ***Log de contabilizações*****

Para que seja possível a utilização do log de contabilizações, é necessário que o sistema esteja parametrizado para utilizar o modelo de contabilização que registra separadamente as contabilizações de cancelamento e aumento.

Esse parâmetro pode ser encontrado em:

Menu: ***Educacional | Configurações | Parâmetros***

Caminho: ***Integração | Contabilidade | Contabilidade 1/2 | "Registra separadamente contabilizações de cancelamento e aumento"***

Após a execução do processo de contabilização, será possível ver a tela de log com os seguintes itens:  
**- Status**  
Sucesso: Contabilização do Contrato e Mensal gerados corretamente  
Erro: Contabilização de contrato não gerada por algum erro no processo de contabilização.  
Advertência: Contabilização de contrato não gerada por alguma advertência no processo de contabilização.  
**- Origem**  
Serviço: Contabilização dos valores de contrato e apropriação mensal  
Aumento: Contabilização de aumento no valores do contrato e  apropriação mensal  
Cancelamento: Contabilização de redução no valor do contrato e  apropriação mensal  
**- Tipo**  
Contrato: Contabilização total do contrato  
Parcela Contábil: Contabilização das apropriações mensais  
**- Operação**Contabilização: Contratos contabilizados  
Estorno: Contratos Estornados**- RA,****Código do contrato,****ID Período Letivo, Período Letivo:** Informações do contrato   
**- Mês/Ano:** Data de contabilização do período de competência  
**- Data Contábil:** Data de inclusão da partida contábil  
**- Mensagem:** Quando o processo é executado com erro é informado no campo mensagem descriminando o erro  
**- ID do Job,****Id. da contabilização de contrato,****Id. da parcela do contrato, Id.oeração:** Chave de identificação do Job, da Contabilização de contrato e mensal e da Operação  
**- Valor de serviço:** Valor total do contrato e valor das apropriações mensais de contrato  
**- Valor de bolsa:** Valor total da bolsa incondicional e valor das apropriações mensais de bolsa  
**- Valor de desconto:** Valor total do desconto e valor das apropriações mensais de desconto  
**- Memória de Cálculo:** Texto detalhando os valores do contrato e a memória de calculo das apropriações mensais.   
**- Criado por e Alterado por:** Usuário responsável por criar ou alterar o processo de contabilização ou estorno  
**- Data de Criação e Data Alteração:**Data de contabilização ou estorno do processo

Nessa tela também será possível:

* Filtrar registros de acordo com os grupos: Operação, Status Contabilização, Status Diagnostico, Tipo de Contabilização, Origem da Contabilização
* Com o duplo clique no Log de contabilização com sucesso, abrirá a visão do lançamento no TOTVS Gestão Contábil para avaliar as partidas contábeis.
* Visualizar valores totais contabilizados de serviços, bolsas e descontos

**Contabilização**No Log da contabilização do contrato será possível avaliar o valor contabilizado da provisão contrato e das apropriações mensais, com valores de bolsas e descontos, na coluna memória de cálculo terá será apresentado de forma textual, a memória de cálculo dos valores contabilizados.   
Contratos não contabilizados por erro durante o processo será gravado o Log e mensagem informando o motivo pelo qual não foi contabilizado, caso seja executado o processo novamente corrigindo o erro e gerando contabilizações para o contrato o Log será substituído pelo novo Log de sucesso.

**Estorno**No processo de estorno o log só será gravado para contratos que apresentarem erros os advertência durante a execução do processo, os contratos que o estorno for executado com sucesso o mesmo limpará o Log de contabilização gravado do contrato junto as partidas contabilizadas.  
Será possível excluir manualmente, através da tela de Log de contabilizações, apenas informações de Log cuja a origem seja referente a erros ou advertência.

Informação sobre os campos "Status" e "Mensagem"

Os campos "Status" e "Mensagem" estão disponíveis para mostrar ao usuário as mensagens de Log de Erro ou Advertência ao final do processo de contabilização.

Ao passar o mouse sobre o ícone "Status" ou o campo "Mensagem" será apresentado a descrição do Erro ou Advertência e será possível copiar a mensagem clicando com o botão direito do mouse.

Abaixo listamos as possíveis mensagens de erro no LOG de contabilização:

Mensagem de erro que o sistema identificar no processo de contabilização:

* Não foi possível gerar a contabilização/estorno para o contrato XXX. O período informado para contabilização/estorno não é válido, o período deve: \* Ser igual ou superior a data do contrato do aluno (xx/xxxx).
* Não foi possível gerar a contabilização/estorno para o contrato XXX. O período informado para contabilização/estorno não é válido, o período deve: \* Estar entre o período inicial xx/xxxx e final xx/xxxx de competência contábil do contrato.
* Não foi possível gerar a contabilização/estorno para o contrato XXX. Não foi possível carregar as partidas contábeis do evento de apropriação mensal de cancelamento (Código do evento:xx).  
  O cancelamento pode estar relacionado com alterações nos valores de serviço, bolsa ou de desconto nas parcelas do contrato.  
  Para que a contabilização possa ser executada com sucesso é recomendado que o evento contábil possua itens a débito e a crédito carregando valores de serviço, bolsa ou desconto. Como podem ocorrer reduções nos valores de serviço, bolsa ou desconto de forma independente, recomenda-se que exista um item de evento para cada um deles.  
  Neste caso sugerimos revisar o evento contábil avaliando se o mesmo contempla todos itens parametrizados corretamente e verificar também se, em caso de uso de default de conta, se não existe alguma classificação de conta que possa estar limitando o item de evento.

Mensagem de advertência que o sistema identificar no processo de contabilização:

* Identificamos uma modificação nos valores (bolsa ou serviço) do contrato 10639, porém o evento contábil 82 não retornou nenhuma informação contábil, portando esta informação não foi enviada para o TOTVS Gestão Contábil. Caso seja necessário contabilizar a informação recomendamos que o evento contábil seja revisado e as contabilizações do contrato sejam estornadas e contrato seja contabilizado novamente.

  Informações Complementares

---
