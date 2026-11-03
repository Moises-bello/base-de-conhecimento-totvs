---
content_hash: f82c419b27b5ac9c3cb0c1dc217f1c0566c05288e6ab9cf58f8014d05fda6ee7
fetched_at: '2026-06-29T00:09:32.563340+00:00'
page_id: '425458875'
product: rm
source: tdn-rm
title: Geração de Lançamentos Agrupados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458875
version: 21
---

Todo lançamento financeiro gerado pelo TOTVS Educacional já é gerado com o seu respectivo boleto.

O sistema permite, no entanto, gerar vários lançamentos financeiros agrupados em um único boleto, desde que as parcelas referentes à estes lançamentos obedeçam algumas regras:

**Regras para geração de lançamento agrupados na mesma Filial**

* As parcelas não podem ser do tipo extra
* As parcelas devem ter a mesma data de vencimento
* As parcelas devem ter o mesmo responsável financeiro
* Se o lançamento já estiver gerado, o status tem que ser igual a “Aberto”, e o boleto não pode esta remetido ao banco
* Se o lançamento já estiver gerado, não será permitido realizar o agrupamento quando pelo menos um deles estiver em processo de cobrança terceirizada nas **versões 12.1.2302 e superiores**

**Regras para geração de lançamento agrupados entre filiais**

* As parcelas não podem ser do tipo extra
* As parcelas devem ter a mesma data de vencimento
* As parcelas devem ter o mesmo responsável financeiro
* Se o lançamento já estiver gerado, o status tem que ser igual a “Aberto”, e o boleto não pode esta remetido ao banco
* Se o lançamento já estiver gerado, não será permitido realizar o agrupamento quando pelo menos um deles estiver em processo de cobrança terceirizada nas **versões 12.1.2302 e superiores**

Neste caso, o campo "Nosso Número" para estes lançamentos financeiros gerados agrupados em um único boleto, receberá o mesmo valor.

A geração dos lançamentos financeiros pode ser feita por dentro do **contrato** do aluno ou pelo processo financeiro de **geração em lote**, através do **Assistente de Geração de Lançamentos Financeiros (menu Financeiro/Contábil | Geração | Financeiro***).*

Se a geração for feita por dentro do **Contrato** do aluno:

* O sistema obedecerá o que estiver previamente definido nos parâmetros do sistema referente à forma de agrupamento (Ambientes | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Agrupamento)
* As parcelas cujo os lançamentos desejam gerar boletos agrupados dentro da mesma filial, os lançamentos precisam ser gerados simultaneamente.
* As parcelas cujo os lançamentos desejam gerar boletos agrupados entre filiais, na geração de lançamento o TOTVS Educacional realizará uma análise nos lançamentos de **todas as outras Filiais da coligada**, identificando se existem parcelas que poderão ter os lançamentos agrupados ao mesmo boleto do lançamento correspondente ao contexto corrente de processamento.

Se a geração for feita pelo processo financeiro de **Geração em lote**

* A parametrização definida previamente servirá como *default*, podendo ser alterada alguns parâmetros no momento da execução do processo.

**Parâmetros do sistema para Agr****upamento de lançamentos**

(Ambientes | Parâmetros | Educacional | Integração | Financeiro | Educacional | Fin – Agrupamento), indique a forma como o sistema deverá agrupar os lançamentos no momento da sua geração

**- Responsável financeiro:** Esta opção pode ser utilizada para os casos em que mais de um aluno, por exemplo irmãos, possuem o mesmo responsável financeiro.**- Contrato:**O sistema tentará gerar em um único boleto as parcelas do mesmo contrato.**- Aluno:**O sistema tentará gerar em um único boleto as parcelas do mesmo aluno.**- Não agrupado:**O sistema não irá agrupar mais de um lançamento em um mesmo boleto.

O agrupamento de lançamento de outras filiais será aplicado somente para a forma de agrupamento por “**Aluno**” ou “**Responsável financeiro**”

**- Não agrupar serviços diferentes**  
Se as parcelas possuírem a mesma data de vencimento e o mesmo responsável financeiro o sistema poderá agrupar os seus lançamentos em um único boleto, mesmo que as parcelas sejam referentes à serviços distintos, por exemplo, uma parcela para o serviço **Mensalidade**e outra para o serviço **Apostila**. Se desejar que parcelas referentes à serviços distintos **não** sejam geradas agrupadas em um único boleto, esta opção nos parâmetros do sistema tem que estar **marcada**.

***-*****Agrupar no mesmo boleto lançamentos de outras Filiais**Se as parcelas da mesma coligada possuírem as mesmas regras para agrupamento de lançamentos em um único boleto, ao gerar uma parcela em uma filial o TOTVS Educacional realizará uma análise nos lançamentos de **todas as outras Filiais da coligada**, e se identificar que existem parcelas serão agrupadas no mesmo boleto, para mais informações 

**- Agrupar lançamentos de parcelas a serem geradas com lançamentos previamente gerados**Agrupa um lançamento que está sendo gerado agora a um boleto já existente, desde que as parcelas dos lançamentos a serem agrupados sejam processadas ao mesmo tempo e que sigam além das regras de agrupamento também as regras abaixo:   
- Não ser um lançamento de bolsa de crédito  
- Lançamento já gerado não pode ter sido faturado  
- O status do lançamento já gerado deve ser "Em aberto"  
- A opção *'Não agrupar serviços diferentes'* também influencia no agrupamento podendo fazer com que somente lançamentos de parcelas com mesmo serviço sejam agrupados em um mesmo boleto.  
- Para os casos em que o status do boleto dos lançamentos já gerados for igual a '*Remetido'* ou '*Registrado'*, o agrupamento de novo lançamento a este boleto somente será permitida se o parâmetro do sistema **'Cancelar remessa automaticamente ao regerar o lançamento financeiro quando boleto estiver com status Remetido ou Registrado'** estiver marcado, pois como haverá mudança de valores, a remessa do boleto original precisará ser cancelada. Para maiores informações consulte o link com as regras para .

**Atenção:**  
Conforme já mencionado, para conseguirmos incluir um novo lançamento a um boleto já gerado, todos os lançamentos envolvidos neste agrupamento devem ser processados ao mesmo tempo, isto significa que os lançamentos originais serão regerados e sendo assim, seguirão as regras para . Se por algum motivo o boleto referente aos lançamentos originais tiver sido excluído ou cancelado, como regra também o sistema sempre irá criar um novo boleto, mas neste caso específico, as regras de agrupamento de lançamentos não serão aplicadas em lançamentos já agrupados e será incluído um boleto para cada lançamento  gerado. Se desejar que as regras de agrupamento de lançamentos sejam aplicadas, os lançamentos envolvidos deverão ser cancelados e incluídos novamente.

-  **Identificação** **automática****das parcelas que podem ser agrupadas no mesmo boleto independente do filtro selecionado no processo de geração de lançamento**Agrupa quando possível lançamento em um único boleto, ao gerar o lançamento de uma parcela o TOTVS Educacional irá verifica para cada parcela processada, se existe outra parcela ou lançamento que pode ser agrupado, levando em consideração as regras de agrupamento e parâmetros marcados, por exemplo: Ao gerar uma parcela que possui outras parcelas com as mesmas regras para agrupamento o sistema fara automático a geração das demais parcelas agrupamento o lançamento no mesmo boleto. 

# Geração de lançamentos agrupados do Educacional ao Movimento (TOTVS Gestão de Faturamento)

O lançamento financeiro originado da venda do produto será agrupado ao boleto da parcela do educacional durante a geração do lançamento, neste momento o processo realizará uma análise na filial parametrizada identificando se existem lançamentos gerados para o tipo de movimento parametrizado que podem ser agrupados ao boleto da parcela que está sendo gerada, para mais informações [clique aqui.](https://tdn.totvs.com/pages/releaseview.action?pageId=515290296)

**Regras para que o lançamento seja agrupado:**

* Deve ter o mesmo responsável financeiro
* Mesma dada de vencimento
* As parcelas não podem ser do tipo extra
* A conta caixa parametrizada deve ser a mesma para o lançamento Educacional e do movimento
* No cadastro da conta caixa a filial não pode ser informada
* O lançamento originado da venda do produto não pode ter boleto gerado
* Se o lançamento já estiver gerado, o status tem que ser igual a “Aberto”, e o boleto não pode esta remetido ao banco
* Se o lançamento já estiver gerado, não será permitido realizar o agrupamento quando pelo menos um deles estiver em processo de cobrança terceirizada nas **versões 12.1.2302 e superiores**

Para que o agrupamento de boleto da parcela na filial, agrupamento de boleto da parcelas entre filiais e agrupamento de boleto da parcela educacional com lançamentos do movimento ocorra, os parâmetros de data de vencimento tanto do **TOTVS Educacional em Integração | Financeiro | Educacional | Fin - Geral 4/4** quando do **TOTVS Gestão Financeira em Contas a Receber | Manutenção de Lançamento| Lançamento | Inclusão a Receber e Calendário Oficial** devem ser configurados igualmente.   
Exemplo:   
- Sábado é dia útil   
- Buscar próximo dia útil para vencimento em dia não útil

**Regeração de Lançamentos**Em casos que mais de uma parcela Educacional tiver lançamentos gerados que seu boleto foi agrupado e no **TOTVS Gestão Financeira** foi desvinculado o boleto, nesse caso na regeração dos lançamentos Educacionais o boleto não será agrupado. Somente será agrupado uma das parcelas Educacional ao lançamento do movimento que não possui boleto e respeitar as regras do agrupamento.

 Veja Também

---
