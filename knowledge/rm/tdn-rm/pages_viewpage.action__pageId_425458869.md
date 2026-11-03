---
content_hash: b28b7d5a53bf59905a0aa4d6914b52cade2b8b1c0c98cf42508caf3e3dc7824f
fetched_at: '2026-06-29T00:09:32.538135+00:00'
page_id: '425458869'
product: rm
source: tdn-rm
title: Prévia dos Valores do Lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458869
version: 4
---

---

**1 - Gerar / Excluir Prévia dos Valores do Lançamento**

Este processo é responsável por gerar uma *Prévia* dos valores correspondentes aos lançamentos financeiros facilitando assim a conferência antes da geração oficial dos lançamentos financeiros e consequente integração entre os sistemas. Com a execução deste processo é possível obter rapidamente uma Prévia da receita assim como dos valores de bolsas e descontos facilitando, assim, a conferência dos valores que irão compor o lançamento sendo utilizadas para a geração da Prévia, as mesmas regras aplicadas na geração de lançamentos.

Para utilizar os recursos referentes à geração da Prévia é importante conceder no Perfil do usuário as devidas permissões.

O processo para geração da Prévia é semelhante ao processo de geração de lançamentos, porem a saída final será uma prévia dos valores que irão compor o lançamento financeiro futuramente.

Para gerar a Prévia dos valores financeiros, acesse o menu *Financeiro/Contábil | Geração | Financeiro | Gerar / Excluir Prévia de Valores do Lançamento* e selecione a opção **'Gerar prévia'**.  Utilizando esta opção, o processo será executado no modo de *geração da prévia*, ou seja, o sistema vai realizar a simulação da geração de lançamentos e gravar os valores simulados na base de dados conforme as informações atribuídas para o processo.

No cálculo do *Valor líquido* para a parcela o sistema sempre considera o maior desconto por antecipação que porventura esteja parametrizado, mas se desejar que na geração da Prévia o sistema *não* considere os valores dos descontos por antecipação, *desmarque* a opção '**Considerar nos cálculos da prévia o desconto por antecipação'.**  Na visão será apresentada uma coluna para identificar se os valores foram processados levando em consideração o desconto por antecipação ou não.

Nas próximas etapas do processo, preencha as opções para seleção dos registros para a geração da Prévia conforme desejar.

**Observação:**

Na tela inicial do processo tem a a opção "*Não apresentar as opções de filtro por serviços, planos de pagamento e matrizes aplicada, pois as informações deverão ser identificadas automaticamente durante a execução do processo no servidor*". O uso desta opção é recomendado quando a execução do processo é agendada, pois desta forma os dados referentes aos serviços, planos de pagamento e matrizes aplicada serão carregados no momento da execução do processo garantindo assim que estas informações estejam atualizadas. Mantenha a opção desmarcada caso seja necessário utilizar alguns destes filtros.

**2 - Visualização dos Valores da Prévia**

As Prévias geradas ficarão armazenadas na base de dados e estarão disponíveis para consulta através do menu Visualização dos Valores da Prévia e também através de cubos criados para importação no módulo TOTVS Inteligência de Negócios.

Para visualizar as Prévias geradas dos valores financeiros, acesse o menu *Financeiro/Contábil | Geração | Financeiro | **Visualização dos Valores da Prévia***.

Todos os valores encontrados através do processo de geração da prévia serão apresentados para consulta, tais como valor líquido do lançamento, valor dos descontos, valor de bolsas, além de várias outras informações que poderão auxiliar nos filtros e análises dos dados, tais como período letivo, curso, turno, matriz aplicada, habilitação, serviço, usuário que processou, entre outras.

Para facilitar mais ainda a consulta e conferência, o Anexo **'Prévia dos Valores de Bolsa'**, presente nesta visão, permite consultar analiticamente os dados e valores calculados para cada bolsa.

 **3 - Exclusão dos Valores da Prévia**

A exclusão da Prévia somente poderá ser executada por usuários que tiverem permissão habilitada em seu *Perfil*. A exclusão poderá ser executada de duas formas:

1- Através da própria visão da Prévia, selecione os registros desejados e execute o Processo **'Excluir Prévia dos Valores do Lançamento'**.

2- Através do menu *Financeiro/Contábil | Geração | Financeiro | Gerar / Excluir Prévia de Valores do Lançamento* utilizando a **'Excluir prévia':** Utilizando esta opção, o processo será executado no modo de *exclusão*, ou seja, o sistema vai excluir as Prévias já processadas conforme as informações atribuídas para o processo.

**Observações:**- Sempre que houver alteração de valores de parcelas, bolsas e/ou descontos ou para os casos em que a parcela for calculada por crédito e houver alteração na matriz curricular, a Prévia ficará *desatualizada*, sendo necessário executar o processo de geração da Prévia novamente.

 Veja Também

---

[Visualização da Prévia via Cubo](http://tdn.totvs.com/pages/viewpage.action?pageId=340362303)
