---
content_hash: a86ad226c6a208997a201ac91adcadef8714c78ec0725714c95ba5cfe78e9ab8
fetched_at: '2026-06-29T00:09:34.032434+00:00'
page_id: '425459120'
product: rm
source: tdn-rm
title: Contabilidade -  Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459120
version: 7
---

---

Nos parâmetros do sistema *Ambiente | Parâmetros | TOTVS Educacional | Integração | Contabilidade 1/2:*

- Indique qual dos dois modelos o sistema deverá adotar para a realização da contabilização por competência.

* **Primeiro** modelo de contabilização por competência do contrato educacional, marque **somente** a primeira opção 'Utiliza contabilização por competência'.
* **Segundo** modelo de contabilização por competência do contrato educacional, marque a opção 'Utiliza contabilização por competência' **e também** a opção 'Registra separadamente contabilizações de cancelamento e aumento'.

A diferença básica entre os dois modelos de contabilização por competência previstos no sistema, é a forma como as alterações ocorridas no valor do contrato, sejam elas devido a aumento ou redução nos valores dos serviços, bolsas ou descontos serão contabilizadas.  
Para obter mais informações sobre os dois modelos de contabilização por competência .

- **'Eventos contábeis*'*** criados previamente para mapear e determinar as regras da contabilização devem ser indicados.

* Se o **Primeiro** modelo de escrituração for o escolhido, somente os eventos para a contabilização do valor do 'Contrato' e também para a contabilização da apropriação 'Mensal' devem ser respectivamente indicados.
* Se o **Segundo** modelo de escrituração for o escolhido, será necessário que todos os eventos contábeis solicitados nesta tela sejam indicados, cada um para sua específica utilização.

Para maiores detalhes quanto à criação de eventos contábeis .

- *'***Lotes Contábeis***'* contábil que receberá os lançamentos que serão criados a cada execução do processo para gerar a contabilização por competência dos contratos deve ser informado, assim como o '*Número do lote para estorno'* que receberá os lançamentos de estorno que porventura forem necessários. Os números dos lotes aqui indicados ficarão fixos. Ao indica-los aqui, estes lotes serão criados automaticamente e exclusivamente para tal finalidade dentro do sistema TOTVS Gestão Contábil, onde poderão ser visualizados e consultados.

- **Contabiliza parcela do tipo Extra**: Marque essa opção para contabilizar parcelas do tipo Extra

- **Contabiliza parcela do tipo Adicional**: Marque essa opção para contabilizar parcelas do tipo Adicional.

Parâmetros do sistema *Ambiente | Parâmetros | TOTVS Educacional | Integração | Contabilidade 2/2:*

- '**Data contábil***'* deve ser indicado o local onde o sistema deverá verificar o período de competência contábil para a inclusão dos lançamentos referentes à contabilização por competência do contrato educacional. Este local pode ser no cadastro do 'Período Letivo', na 'Parametrização por Curso' ou no 'Contrato e Plano de Pagamento'. Dentro do cadastro do respectivo local aqui escolhido, será habilitada uma aba chamada Contabilização, onde deve ser informado o período de competência contábil, preenchendo-se o mês/ano da competência inicial e o mês/ano da competência final.   
Para obter mais informações sobre competência contábil .  
  
- '**Considera a data de cancelamento do contrato para a data do estorno contábil no processo de cancelamento de contrato**' somente ficará habilitado para quem estiver utilizando o **primeiro** modelo de contabilização por competência do contrato educacional, onde somente a primeira opção 'Utiliza contabilização por competência' é marcada. Com este parâmetro habilitado os estornos da contabilização receberão a mesma data informada no processo de "Cancelar contrato". Com o parâmetro desabilitado a data dos lançamentos de estorno continuará igual à data de execução do processo.   
  
- '**Utiliza fracionamento de processos'**: Habilitando o fracionamento de job terá uma quebra de processos em 'N' processos de acordo com o número de contratos por fracionamento

* "Utiliza fracionamento de processos: Indica se o fracionamento de processos (jobs) está habilitado.
* "N° de contratos por fracionamento: Indica o número limite de contratos que o sistema considerará por fracionamento.
* Nº máximo de processos por contexto: Número limite de processos a serem gerados pelo fracionamento, ou seja, o sistema somente criará processos até o número máximo especificado por esse parâmetro.

- '**Considera apenas a provisão de contratos**': Habilitando essa opção será feita a provisão de contratos, apropriações mensais não serão contabilizadas, exceto, para que tenham sidos contabilizados antes de marcar esse parâmetro. 

- '**Considera a data contábil para a data de contabilização da provisão**': Caso a apropriação de contrato seja feita junto com a apropriação mensal, será utilizada a data do contrato como a data de contabilização da provisão.
