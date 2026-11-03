---
content_hash: fafdff2034063f7626ac281aca6c39c2ba7fd8e7b7c1ded5e3347051083d72f7
fetched_at: '2026-06-29T00:05:52.383166+00:00'
page_id: '1058204459'
product: rm
source: tdn-rm
title: eSocial - Adequação para atender Rubricas de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1058204459
version: 143
---

false

## **⚠️ATENÇÃO:**

* Para evitar impactos no fechamento da folha da competência **06/2026**, recomendamos a execução do Atualizador de Script e a realização das parametrizações necessárias em sua base de dados, sejam realizadas **após a liberação da competência 06/2026**.

**Webinar TOTVS | Rubricas de Férias e Abono Salarial (PIS)**

* Vídeo Apresentação  
  <https://www.youtube.com/watch?v=PLUFufomXqc>

* PPT Apresentação

250

Perguntas e Respostas

**001. Quando essa implementação estará disponível nos patches?**

**Resposta:** Atualmente, a implementação está em fase de validação com alguns clientes pilotos. Essa etapa é importante para garantir que a solução esteja validada em cenários reais de utilização, encontrados nas bases dos clientes.

Embora tenhamos realizado diversos testes internos com diferentes cenários, entendemos que a validação em ambientes reais proporciona maior segurança e qualidade antes da disponibilização geral.

A previsão é que a implementação seja liberada nos patches em **26/06/2026**.

**002. Será necessário retificar informações a partir do ano de 2024?**

**Resposta:** Não. Essa alteração passa a valer apenas para os eventos com competência a partir de **janeiro de 2026**, visando atender às novas regras de informação do PIS, cujos pagamentos ocorrerão a partir de 2028. Portanto, não será necessária a retificação de informações referentes aos anos anteriores.

**003. Qual o motivo dessa mudança no produto Folha de Pagamento RM?**

**Resposta:**Essa alteração foi necessária para adequar o produto às novas regras do eSocial, que passam a ser obrigatórias a partir de **01/01/2026**.

Com a inclusão da natureza **1015** e a alteração das naturezas **1016** e **1017**, o Manual de Orientação do eSocial (MOS) passou a definir uma nova forma de informar as verbas de férias. A partir dessa data, o **valor líquido das férias (código de cálculo 43)** não deverá mais ser enviado ao eSocial. Em vez disso, cada verba que compõe as férias deverá possuir sua respectiva verba de compensação, permitindo que o líquido seja representado corretamente no envio.

### Exemplo

Hoje, as verbas/eventos de férias são lançadas no envelope de pagamento da seguinte forma:

| Verba | Valor |
| --- | --- |
| Férias | R$ 3.000,00 |
| 1/3 Constitucional | R$ 1.000,00 |
| INSS | -R$ 400,00 |
| IRRF | -R$ 200,00 |
| **Líquido de Férias (CC 43)** | **R$ 3.400,00** |

Até então, esse valor líquido também era enviado ao eSocial.

Com a nova regra, o eSocial o correto é nãomais o envio do líquido de férias. Em vez disso, será necessário enviar apenas as verbas individualmente e suas respectivas verbas de compensação, conforme a parametrização exigida pelo MOS.

Poderíamos ter realizado uma implementação para alterar o envelope de pagamento para exibir todas essas verbas de compensação das férias. No entanto, isso faria com que o envelope do funcionário ficasse muito maior e mais complexo, além de poder impactar outros processos já existentes, como cálculos de diferenças retroativas.

Por esse motivo, optamos por **preservar o conceito atual do envelope de pagamento**, mantendo a experiência do usuário inalterada.

Assim, toda a adequação às novas exigências do eSocial será realizada **apenas no momento da geração das informações enviadas ao eSocial**, por meio do **De-Para de verbas/eventos**. Dessa forma, o usuário continua trabalhando normalmente no sistema, enquanto o produto gera automaticamente as informações no formato exigido pela legislação.

**Importante:** Nesta etapa inicial, será necessário que o usuário crie as novas verbas/eventos de compensação e realize a parametrização de cada uma delas em suas respectivas verbas/eventos de férias.

Essa configuração é necessária para que o sistema consiga gerar corretamente as informações exigidas pelo eSocial, de acordo com as novas regras vigentes a partir de 01/01/2026.

Todos os detalhes sobre esse processo, incluindo exemplos de configuração, estão descritos no tópico **"Como fica a parametrização após as alterações"**.

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

false

**A partir das Versões:**

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

## **01. ALTERAÇÕES**

## **01.1.** **Mudança das Rubricas no eSocial**

| RUBRICA | DESCRIÇÃO DA NATUREZA DA RUBRICA ATÉ 31-12-2025 | DESCRIÇÃO DA NATUREZA DA RUBRICA A PARTIR 01-01-2026 |
| --- | --- | --- |
| 1015 - Adiantamento de férias | Não existia | Valor correspondente ao pagamento do adiantamento da remuneração de férias, inclusive do terço constitucional. |
| 1016 - Férias | Valor correspondente à remuneração devida na época da concessão das férias, inclusive o adiantamento de férias.  Nessa natureza deve ser classifica do também o valor pago mensalmente ao trabalhador avulso e ao empregado com contrato de trabalho intermitente, a título de férias | Valor correspondente à remuneração devida na época da concessão das férias.    Nessa natureza deve ser classifica do também o valor pago mensalmente ao trabalhador avulso e ao empregado com contrato de trabalho intermitente, a título de férias |
| 1017 - Terço constitucional de férias | Valor correspondente ao terço constitucional de férias relativo à remuneração devida na época da concessão das férias, inclusive o adiantamento de férias.  Nessa natureza deve ser classificado também o valor pago mensalmente ao trabalhador avulso e ao empregado com contrato de trabalho intermitente, a título de terço constitucional de férias | Valor correspondente ao terço constitucional de férias relativo à remuneração devida na época da concessão das férias.  Nessa natureza deve ser classificado também o valor pago mensalmente ao trabalhador avulso e ao empregado com contrato de trabalho intermitente, a título de terço constitucional de férias |

**Atenção I:** As alterações estão destacadas em vermelho.

**Atenção II:** Veja mais detalhes sobre as mudanças e exemplos práticos no Manual de Orientação do eSocial (MOS), publicado em 07/2026, a partir da página 108.

* + [MOS S-1.3 | 07/2026](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-07-2026-com-marcacoes.pdf)

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

## **01.2.** **Mudança das Rubricas na Folha de Pagamento**

Clique no link abaixo para visualizar e comparar o comportamento **anterior** e **atual** das rubricas de férias no produto **TOTVS Folha de Pagamento**, entendendo as alterações realizadas na parametrização e na geração dos XMLs para atendimento às novas diretrizes do eSocial.

Mudança no processoO que mudouRecibo de Férias

## **Como era a parametrização no produto**

A partir do leiaute S-1.0 do eSocial, o detalhamento das verbas de férias passou a ser enviado diretamente noS-1200 (Remuneração), deixando de ser informado no S-1210.

Também foi definido que a **Antecipação de Férias** não possui incidência de **INSS** e **FGTS** no mês do pagamento, mantendo apenas a incidência de **IRRF**.

Para atender essa regra, foi realizada uma adequação na **TOTVS Folha de Pagamento**, onde as verbas originais do recibo de férias passaram a ser substituídas por verbas específicas para envio ao eSocial, contendo apenas a incidência de IRRF. Isso foi necessário para evitar a duplicidade de incidências, já que as verbas originais possuem incidência de IRRF, INSS e FGTS.

Essa parametrização era realizada por meio de um '**De-Para'**, disponível em Configurações | Parametrizador | eSocial | [Configurações Gerais 7/7](https://tdn.totvs.com/pages/viewpage.action?pageId=645896860).

A seguir, apresentamos um exemplo do cálculo de férias e o respectivo XML da Antecipação de Férias gerado pelo eSocial, considerando essa parametrização utilizada anteriormente, antes das alterações disponibilizadas nos patches mencionados.

* As férias foram calculadas no recibo, apresentando os seguintes códigos de cálculo:
  + **38 - Férias** : Provento - (Incide INSS; Incide IRRF Férias)
  + **40 - 1/3 Férias** : Provento (Incide INSS; Incide IRRF Férias)
  + **82 - INSS Férias** : Desconto
  + **30 - IRRF Férias** : Desconto
  + **90 - INSS Férias Alíquota Normal** : Base de Cálculo

* Nesse exemplo, foi configurado um **"De-Para"** que irá realizar a substituição de algumas verbas do **Recibo de Férias** no momento de gerar o XML. Entre elas, estão:
  + **311** - Provento (sem incidência em INSS; com incidência em IRRF Férias) : Substituindo o evento de férias (CC38)
  + **312** - Provento (sem incidência em INSS; com incidência em IRRF Férias) : Substituindo o evento de 1/3 de férias (CC40)
  + **313** - Desconto (sem incidências) : Substituindo o evento de INSS Férias (CC82)

* O XML é gerado realizando as substituições conforme o **De-Para** cadastrado. Nesse cenário, as verbas de **Férias** e **1/3 de Férias** são enviadas com incidência apenas de **IRRF Férias**.

  Já a verba de **INSS Férias** é enviada sem o **codIncCP = 31**, evitando que o valor seja considerado como desconto de INSS sobre férias na geração da Antecipação de Férias.

## **Como fica a parametrização após as alterações**

A regra do eSocial para envio da **Antecipação de Férias** com incidência exclusiva de **IRRF** permanece a mesma. Porém, com a atualização do MOS e a inclusão das novas naturezas de rubricas de férias, o eSocial passou a apresentar novos exemplos e orientações sobre a escrituração dessas verbas e suas incidências.

Para atender essas diretrizes e simplificar a configuração para os usuários, realizamos uma adequação no produto, centralizando as parametrizações do eSocial no próprio cadastro de verbas.

Com isso, o **De-Para** anteriormente configurado em Configurações | Parametrizador | eSocial | Configurações Gerais (7/7) foi descontinuado e substituído pela nova aba **eSocial**, disponível em Cadastros | Eventos, no grupo **Antecipação de Férias**, conforme print abaixo:

false⚠️ ATENÇÃO: 

Consulte neste documento Na seção **"O que o usuário deverá fazer? | Eventos"** para identificar quais verbas precisam ser configuradas e entender como será realizada a migração das informações anteriormente parametrizadas em Configurações | Parametrizador | eSocial | Configurações Gerais (7/7) para a nova configuração disponível em Cadastros | Eventos, no grupo **Antecipação de Férias**.

Envelope de Pagamento

## **Como era a parametrização no produto**

Com a alteração implementada pelo leiaute S-1.0 do eSocial, onde passou a enviar a **Antecipação de Férias** diretamente noS-1200 (Remuneração), considerando apenas a incidência de **IRRF,** as verbas de férias lançadas no **Envelope de Pagamento** também precisaram ser tratadas de forma diferenciada para evitar a duplicidade de incidência de IRRF, já que essa tributação já havia sido considerada na Antecipação de Férias. Assim, essas verbas passaram a considerar apenas as incidências de **INSS** e **FGTS**.

Para atender essa regra, a **TOTVS Folha de Pagamento** passou a enviar a verba do tipo "Base de Cálculo" com código de cálculo "**381-Base de IRRF Férias Envelope**" como dedutora, além de substituir algumas verbas originais de férias do Envelope de Pagamento por verbas específicas para envio ao eSocial, para não haver duplicidade de valores, uma vez que existem verbas que são as mesmas tanto no Recibo de Férias quanto no Envelope de Pagamento, a exemplo o INSS, IRRF dentre outras.

Essa parametrização era realizada por meio de um **De-Para**, disponível em Configurações | Parametrizador | eSocial | [Configurações Gerais 6/7](https://tdn.totvs.com/pages/viewpage.action?pageId=540899121).

A seguir, apresentamos um exemplo de lançamento de férias no Envelope de Pagamento e o respectivo XML gerado pelo eSocial, considerando essa parametrização utilizada anteriormente, antes das alterações disponibilizadas nos patches mencionados.

* As férias foram lançadas no envelope de pagamento, apresentando então os códigos de cálculo abaixo:
  + **41 - Férias no mês** : Provento (Incide INSS; Incide IRRF Férias)
  + **76 - 1/3 Férias no mês** : Provento (Incide INSS; Incide IRRF Férias)
  + **82 - INSS Férias** : Desconto
  + **30 - IRRF Férias** : Desconto
  + **43 - Adiantamento Conforme Recibo** : Desconto
  + **381 - Base de IRRF Férias Envelope** : Base de Cálculo (possui *codIncIRRF 13*, que estorna o IRRF Férias no governo)

**AJUSTAR O PRINT ABAIXO, POIS O 381 ESTA CONSIDERANDO APENAS 1/3**

* Nesse exemplo, foi configurado um **"De-Para"** que irá realizar a substituição de algumas verbas de Férias lançadas no **Envelope de Pagamento** no momento de gerar o XML. Entre elas, estão:

* + **304** - Desconto (sem incidência) : Substituindo o evento de IRRF Férias (CC30)
  + **306** - Base de Cálculo (sem incidência) : Substituindo o evento de INSS Férias Alíquota Normal (CC90)
  + **309** - Desconto (sem incidência) : Substituindo o evento de INSS Férias (CC82)

* Para evitar a duplicidade do IRRF Férias, considerando que o imposto de renda é caixa (ou seja, deverá ser considerado conforme data de pagamento), o sistema também lança o **Código de Cálculo 381**, que possui ***codIncIRRF 13 - IRRF Férias***, estornando então a base de IRRF do envelope no governo.

* Assim, na geração do XML, as verbas de Férias e 1/3 Férias são levadas normalmente sendo computadas para a base de INSS e FGTS, porém tendo a base de IRRF abatida pelo **CC 381**.

## **Como fica a parametrização após as alterações**

Para atender às diretrizes apresentadas no **Manual de Orientação do eSocial (MOS)**, que exemplifica as incidências corretas das verbas de férias lançadas no Envelope de Pagamento, e também para simplificar a configuração pelos usuários, realizamos uma adequação no produto, centralizando as parametrizações do eSocial no próprio cadastro de verbas.

Com isso, o **De-Para** anteriormente configurado em Configurações | Parametrizador | eSocial | Configurações Gerais (6/7) foi descontinuado e substituído pela nova aba **eSocial**, disponível em Cadastros | Eventos, nos grupos **Envelope de Pagamento (Provento)** e **Envelope de Pagamento (Desconto)**, conforme demonstrado abaixo:

### Por que agora existem dois eventos no De-Para?

Com as novas diretrizes apresentadas no MOS, o ideal é que cada verba lançada possua um **evento correspondente ("par")** com as rubricas e incidências necessárias para o correto fechamento das bases de **INSS, FGTS e IRRF**.

Dessa forma, quando uma verba do tipo Provento for lançada no Envelope de Pagamento, deverá ser configurado um evento do tipo Desconto para também ser enviado ao eSocial.

Da mesma forma, verbas do tipo Desconto poderão possuir um evento correspondente do tipo Provento.

**IMPORTANTE:**

Não haverá alteração no envelope de pagamento do funcionário. A mudança ocorre apenas na geração do XML enviado ao eSocial.

Com essa nova forma de configuração, os eventos abaixo passam a ser desconsiderados na geração do XML, pois cada verba passará a possuir seu respectivo "par", garantindo o correto fechamento das bases e dos valores líquidos:

* **43 - Adiantamento conforme Recibo**
* **381 - Base de IRRF Férias Envelope**
* **398 - Base de Abono Férias Envelope**

**Exemplos:**

* + **CC 41 - Férias no mês (Provento)** → Deve possuir um evento configurado em **Envelope de Pagamento (Desconto)**.
  + **CC 82 - INSS Férias (Desconto)** → Deve possuir um evento configurado em **Envelope de Pagamento (Provento)**.

false⚠️ ATENÇÃO: 

Consulte neste documento Na seção **"O que o usuário deverá fazer? | Eventos"** para identificar quais verbas precisam ser configuradas e entender como será realizada a migração das informações anteriormente parametrizadas em Configurações | Parametrizador | eSocial | Configurações Gerais (6/7) para a nova configuração disponível em Cadastros | Eventos, nos grupos **Envelope de Pagamento (Provento)** e **Envelope de Pagamento (Desconto)**.

Clique no link abaixo para visualizar os detalhes das alterações e as informações necessárias para compreender as mudanças implementadas em cada processo e cadastro do produto **Folha de Pagamento**.

Menus que tiveram alteração11Parametrizador

## **Menu Configurações | Parametrizador | eSocial**

Descontinuação do **'De-Para'** de eventos de férias eSocial. Foram desabilitados os campos/telas nos seguintes caminhos:

* Configurações Gerais 6/7
* Configurações Gerais 7/7

1 - As telas desabilitadas ficaram disponíveis somente para consulta das informações.

2 - Ao acessar as telas será exibida a mensagem abaixo:

3 - As parametrizações devem ser realizadas exclusivamente no menu Eventos | Eventosna nova aba "**eSocial**". Veja mais detalhes na aba "**Eventos/Verbas**" deste documento.

4 - Para transcrever essa parametrização para o **Cadastro de Eventos** é necessário executar o processo localizado no menu eSocial | Outros Processos | Conversor Parametrizador x Eventos. Veja mais detalhes na aba "**Conversor Parametrizador x Eventos**" deste documento.

false⚠️ ATENÇÃO: Mudança na Geração do XML

A geração do XML não realizará o '**De-Para**' nos eventos das tabelas **PFVERBASDIS** e **PFVERBASDISFER**. O processo de '**De-Para'** será executado apenas quando a verba for originada da tabela **PFFINANC**.

3Eventos/Verbas

## **Menu Administração de Pessoal | Eventos | Eventos**

### 1 - Aba "eSocial"

Essa aba tem como objetivo configurar o '**De-Para**' dos eventos relacionados às férias na geração dos XMLs do eSocial, garantindo que as informações sejam enviadas corretamente, conforme as regras exigidas pelo governo, além de proporcionar maior visibilidade ao usuário.

Adicionalmente, essa aba centraliza todas as informações relacionadas ao eSocial, permitindo a gestão em um único local, de forma mais organizada e eficiente.

**De-Para de Eventos**Para atender às recentes alterações normativas e atualizar as rubricas de férias, implementamos a funcionalidade '**De-Para**' diretamente no cadastro de eventos.

**Antecipação de Férias (Provento/Desconto)**

Mantendo a mesma lógica anteriormente utilizada em **Configurações Gerais (7/7)**, o sistema substitui as verbas originais apenas durante a geração do XML. Dessa forma, garante o envio correto da antecipação de férias ao eSocial, considerando as incidências exclusivas de **IRRF**, sem impactar os cálculos ou o envelope de pagamento do funcionário.

**Envelope de Pagamento (Provento) / Envelope de Pagamento (Desconto)**

Esses campos substituem a parametrização anteriormente realizada em **Configurações Gerais (6/7)**. Seu objetivo é garantir a correta apresentação das incidências de **INSS, FGTS e IRRF**, bem como o correto fechamento do líquido de férias no eSocial.

Após a atualização sistêmica, o sistema passará a utilizar os eventos configurados nesses campos para substituir ou complementar as verbas originais exclusivamente durante a geração do XML, sem alterar o envelope de pagamento do funcionário.

**Lógica de Substituição**

* + **Preenchimento Parcial:** Quando apenas um dos campos (Provento ou Desconto) estiver preenchido, o sistema mantém o evento original e gera também o evento correspondente configurado.
  + **Preenchimento Integral:** Quando os campos de Provento e Desconto estiverem preenchidos, o sistema desconsidera o evento original e envia ao eSocial apenas os dois eventos parametrizados.

**Incidências eSocial**

Neste campo são exibidas as incidências que serão geradas no XML do eSocial, proporcionando mais transparência e facilitando a conferência e manutenção das parametrizações no dia a dia.

> **Atenção:** Para os eventos/verbas já existentes, o grupo **Incidências eSocial** será preenchidos somente nas seguintes situações:
>
> * Ao salvar o cadastro do evento/verba; ou
> * Ao executar o processo eSocial | Outros Processos | Conversor do Parametrizador dos Eventos de Férias.
>
> A execução do **Conversor do Parametrizador dos Eventos de Férias** atualiza as Incidências eSocial de **todos os eventos/verbas** existentes na base.

**Novas Validações**

Ao salvar o cadastro do evento, o sistema realizará novas validações considerando informações como **Natureza de Rubrica** e **Incidências eSocial**. Dessa forma, para determinados **Códigos de Cálculo**, poderão ser apresentados alertas indicando a necessidade de ajuste na parametrização, conforme exemplo abaixo.

### 2 - Parâmetro "Forçar codIncCP eSocial" na aba "Inc. Descontos"

Foi criado o parâmetro **"Forçar codIncCP eSocial"** com o objetivo de definir manualmente o valor que será enviado na tag **<codIncCP>** do evento **S-1010**.

Atualmente, está disponível a seguinte opção:

* **31 – Mensal** (Contribuição descontada do segurado sobre salário de contribuição)

Ao utilizar esse parâmetro, o valor informado irá sobrescrever a regra padrão adotada pelo sistema no [Mapeamento do evento S-1010](https://tdn.totvs.com/display/LRM/Evento+S-1010).

**Importante:** O parâmetro somente ficará disponível para seleção quando o evento não possuir incidência de INSS configurada.

### 3 - Parâmetro "Forçar codIncIRRF eSocial" na aba "Inc. Proventos"

Foram disponibilizados novos códigos no parâmetro **"Forçar codIncIRRF eSocial"**, permitindo definir manualmente o valor que será enviado na tag **<codIncIRRF>** do evento **S-1010**.

Códigos disponíveis:

* **09** - Outras verbas não consideradas como base de cálculo ou rendimento
* **33** - Férias
* **43** - Previdência Social Oficial (PSO) - Férias
* **53** - Pensão alimentícia - Férias

**Importante:** O código **"00 - Rendimento não tributável"** foi descontinuado a partir da versão **S-1.0** do eSocial.

Ao utilizar esse parâmetro, o valor informado irá sobrescrever a regra padrão adotada pelo sistema no [Mapeamento do evento S-1010](https://tdn.totvs.com/display/LRM/Evento+S-1010).

**Observação:** O parâmetro somente ficará disponível para seleção quando o evento não possuir incidência de IRRF configurada.

Veja mais detalhes nos links: 

* [Cadastro de Eventos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719284)
* [S-1010](https://tdn.totvs.com/display/LRM/S-1010+-+Tabela+de+Rubricas)
* [Mapeamento S-1010](https://tdn.totvs.com/display/LRM/Evento+S-1010)

2Conversor Parametrizador x Eventos

## **Menu eSocial eSocial | Outros Processos**

false⚠️ ATENÇÃO:

**ANTES DE EXECUTAR O CONVERSOR DO PARAMETRIZADOR DOS EVENTOS DE FÉRIAS É NECESSÁRIO CRIAR/IMPORTAR OS EVENTOS/VERBAS CONFORME ORIENTADO NA ABA EVENTOS/VERBAS.**

Foi criado o processo **"Conversor do Parametrizador dos Eventos de Férias"**, com o objetivo de auxiliar na parametrização das verbas, realizando a vinculação das rubricas necessárias para a correta geração e envio dos XMLs ao eSocial.

Veja mais detalhes no link:

4Exportação e Importação de Eventos/Verbas

## **Menu Gestão | Gerador de Saída**

Adequação no leiaute de exportação “**FOPLAY0048 09.004.021 Exportação de Eventos.TotvsGen**” incluindo os novos campos no arquivo.

Veja mais detalhes nessa página na aba "**Eventos/Verbas**".

## **Menu Configurações | Importações | Importação de Dados da Folha de Pagamento | Aba Parâmetros I | Eventos**

Campos criados:

* CODEVENTODEPARARECIBOFERIAS
* CODEVENTODEPARAPROVENTOFERIAS
* CODEVENTODEPARADESCONTOFERIAS
* FORCARINCINSS
* INCINSSFORCADA

Veja mais detalhes no link:

5Recibo de Férias

## **Menu Administração de Pessoal | Funcionário | Férias**

Passa a apresentar na coluna "'**De-Para****Verbas**" com o código do evento parametrizado do campo "**Antecipação de Férias (Provento/Desconto)**" na aba "**eSocial**" do cadastro de evento.

Quando preenchido, o sistema passará a levar na geração do XML o código existente na coluna "'**De-Para****Verbas**" ao invés do código da coluna "**Evento**" presente no recibo.

No exemplo abaixo, o XML do evento de remuneração e/ou rescisão apresenta no período das férias os códigos da coluna "'**De-Para****Verbas**", em substituição aos eventos originais do recibo:

* **Z001** → substituindo o 0038
* **Z002** → substituindo o 0040
* **Z003** → substituindo o 0098

6Envelope de Pagamento

## **Menu Administração de Pessoal | Funcionário | Envelope**

Passa a apresentar as colunas "'**De-Para****Desconto**" e "'**De-Para** **Provento**" com os códigos dos eventos parametrizados nos campos "**Envelope de Pagamento (Desconto)**" e/ou "**Envelope de Pagamento (Provento)**", respectivamente, da aba "**eSocial**" do cadastro de evento.

Quando preenchidos, o sistema passará a levar na geração do XML os códigos existentes nas colunas "**Envelope de Pagamento (Desconto)**" e/ou "**Envelope de Pagamento (Provento)**" ao invés do código da coluna "**Código**" presente no envelope de pagamento.

No exemplo abaixo, o XML do evento de remuneração e/ou rescisão apresenta os códigos das colunas "**Envelope de Pagamento (Desconto)**" e/ou "**Envelope de Pagamento (Provento)**", em substituição aos eventos originais do envelope:

* **D076** → faz contrapartida com o 0076
* **D041** →  faz contrapartida com o 0041
* **P082** →  faz contrapartida com o 0098

7Fila de Eventos

## **Menu eSocial | Fila de Eventos | S-1010 | Processos | Atualizar competência da fila de eventos S-1010**

Foi disponibilizado um processo para atualização em lote do campo **Competência** (tag **<iniValid>**), facilitando a adequação das rubricas e a geração dos eventos **S-1010** no eSocial.

Para as naturezas de rubrica listadas abaixo, deverá ser informada a **Competência 01/2014**, garantindo que essas rubricas sejam consideradas pelo sistema na geração de retificações de períodos anteriores a 2026.

* 1016
* 1017

Para as naturezas de rubrica listadas abaixo, deverá ser informada a **Competência 01/2026**, garantindo que essas rubricas sejam consideradas pelo sistema na geração de retificações de períodos a partir de 2026.

* 1015

Veja mais detalhes em:

* [Fila de Eventos](https://tdn.totvs.com.br/display/public/LRM/Fila+de+Eventos)
8S-1010

## **Menu eSocial | Gerar XML | Evento S-1010**

O sistema passa a considerar as verbas também configuradas na aba **eSocial** do cadastro de eventos, nos campos **Antecipação de Férias (Provento/Desconto)**, **Envelope de Pagamento (Provento)** e **Envelope de Pagamento (Desconto)** durante a geração do XML.

Para mais informações acesse nessa página na aba "**Eventos/Verbas**".

Veja mais detalhes em:

* [Cadastro de Eventos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719284)
* [S-1010](https://tdn.totvs.com/display/LRM/S-1010+-+Tabela+de+Rubricas)
* [Mapeamento S-1010](https://tdn.totvs.com/display/LRM/Evento+S-1010)
9S-1200 | S-1202 | S-2299 | S-2399 

## **Menu eSocial | Gerar XML**

**Eventos S-1200, S-1202, S-1207, S-2299 e S-2399**

1 - Na geração do XML, o sistema passa a considerar as parametrizações configuradas na aba **eSocial** do cadastro de eventos para realizar as substituições das verbas, substituindo a configuração anteriormente realizada em Configurações | Parametrizador | eSocial | Configurações Gerais (6/7 e 7/7).

2 - O sistema passa a validar a existência dessas parametrizações durante a geração do XML, apresentando mensagem de erro quando houver eventos com códigos de cálculo que exigem configuração obrigatória e não possuam o respectivo **De-Para** informado.

3 - Os seguintes códigos de cálculo passam a ser desconsiderados na geração do XML:

* + **43 - Adiantamento conforme Recibo**
  + **90 - I.N.S.S. Férias com alíquota normal**
  + **137 - I.N.S.S. Fér. Próx. mês c/ alíq. normal**
  + **138 - I.N.S.S. Fér. desc. mês ant. alíq. normal**
  + **381 - Base de IRRF Férias Envelope**
  + **398 - Base de Abono Férias Envelope**

Veja mais detalhes em: 

+ [Gerar XML Periódicos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719232)

10Comparativo de Incidências de Rubricas

## **Menu eSocial | Outros processos | Comparativo de Incidências de Rubricas**

Em implementação

1 - Passa a considerar as parametrizações de '**De-Para**' da aba "eSocial" do cadastro de eventos ao invés do Configurações | Parametrizador | eSocial Configurações Gerais 6/7 e Configurações Gerais 7/7.

Veja mais detalhes nessa página na aba "**Eventos/Verbas**".

2 - Passa a desconsiderar os códigos de cálculos abaixo:

* **43 - Adiantamento conforme Recibo**
* **90 - I.N.S.S. Férias com alíquota normal**
* **137 - I.N.S.S. Fér. Próx. mês c/ alíq. normal**
* **138 - I.N.S.S. Fér. desc. mês ant. alíq. normal**
* **381 - Base de IRRF Férias Envelope**
* **398-  Base de Abono Férias Envelope**

Veja mais detalhes em:

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

## **02.** **O QUE O USUÁRIO DEVERÁ FAZER?**

Clique no link abaixo em entenda as ações necessárias e os procedimentos que deverão ser realizados pelos usuários para adequação às mudanças implementadas no produto **Folha de Pagamento**.

Alterações a serem realizadas pelo usuário11Atualizador

## **Atualização de Ambiente**

Após a liberação da versão será necessário executar os scripts de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

2Permissão de Acesso

## **Menu Serviços Globais | Segurança | Perfis**

Selecione o sistema **Folha de Pagamento**, edite o perfil desejado e conceda permissão ao processo abaixo:

**1) 09.03.02.11** - Atualizar competência de eventos S-1010

Essa permissão disponibilizará o processo: Folha de Pagamento | eSocial | Eventos Tabelas/Não Periódicos | Processos | Atualizar competência de eventos S-1010

**2) 09.05.16** - Conversor do Parametrizador dos Eventos de Férias

Essa permissão disponibilizará o processo: Folha de Pagamento | eSocial | Outros Processos | Conversor do Parametrizador dos Eventos de Férias

3Eventos/Verbas

## **Menu Administração de Pessoal | Eventos | Eventos**

### 1.1 - Criar os novos eventos/verbas MANUALMENTE

Deverão ser criados novos eventos/verbas conforme descrito abaixo, além de verificar as orientações de **Natureza de Rubrica** e **Incidências eSocial** indicadas para cada caso. Caso tenha mais de uma coligada, poderá criar os eventos/verbas em uma coligada e copiar para as demais.

Clique para ver a lista de eventos a serem criados

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **CÓDIGO EVENTOS / VERBAS****(APENAS SUGESTÕES)** | **CÓDIGO CÁLCULO** | **DESCRIÇÃO (APENAS SUGESTÕES)** | **TIPO** | **NATUREZA RUBRICA** | **CODINCCP** | **CODINCIRRF** | **CODINCFGTS** | **VINCULAR AO** **EVENTO / VERBA** |
| X001 | 0 | 1ª Parcela 13º - ENVELOPE DESC | Desconto | 5504 | 0 | 9 | 0 | 9 |
| X002 | 0 | IRRF Férias - ENVELOPE PROV | Provento | 9203 | 0 | 33 | 0 | 30107306 |
| X003 | 0 | Abono de Férias - ENVELOPE DESC | Desconto | 1023 | 0 | 75 | 0 | 3947311 |
| X004 | 0 | 1/3 Abono de Férias - ENVELOPE DESC | Desconto | 1023 | 0 | 13 | 0 | 56312 |
| X005 | 0 | INSS Férias - ENVELOPE PROV | Provento | 9221 | 0 | 43 | 0 | 82130141349 |
| X006 | 0 | Pensão Alimentícia Férias - ENVELOPE PROV | Provento | 9213 | 0 | 53 | 0 | 113320 |
| X007 | 0 | Arredondamento Férias - ENVELOPE DESC | Desconto | 2999 | 0 | 9 | 0 | 129 |
| X008 | 0 | INSS Férias Próx. Mês - ENVELOPE PROV | Provento | 9221 | 0 | 9 | 0 | 142 |
| X009 | 0 | Salário Família Férias - ENVELOPE DESC | Desconto | 1409 | 0 | 9 | 0 | 149 |
| X010 | 0 | Férias em Dobro - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | 309 |
| X011 | 0 | Adicional 1/3 Férias em Dobro - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | 310 |
| X012 | 0 | Férias Mês - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | 41 |
| X013 | 0 | Férias Próx. Mês - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | 42350 |
| X014 | 0 | Férias Pagas Mês Ant. - ENVELOPE PROV | Provento | 1016 | 11 | 13 | 11 | 44 |
| X015 | 0 | Férias Pagas Mês Ant. - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | 44 |
| X016 | 0 | 1/3 Férias Mês - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | 76 |
| X017 | 0 | 1/3 Férias Próx. Mês - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | 77351 |
| X018 | 0 | 1/3 Férias Pagas Mês Ant. - ENVELOPE PROV | Provento | 1017 | 11 | 13 | 11 | 78 |
| X019 | 0 | 1/3 Férias Pagas Mês Ant. - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | 78 |
| X020 | 0 | Estorno Pensão sobre Férias - ENVELOPE DESC | Desconto | 9213 | 0 | 53 | 0 | 201 |
| X021 | 0 | Adiantamento Provisão Empr. Consig. Férias (Desc) - ENVELOPE PROV | Provento | 1299 | 0 | 9 | 0 | 466 |
| X022 | 0 | Adiantamento Provisão Empr. Crédito Trab. - ENVELOPE PROV | Provento | 9299 | 0 | 9 | 0 | 489 |
| X023 | 0 | Previdência Privada Dedutível de IRRF Férias - ENVELOPE PROV | Provento | 922592249223 | 0 | 48 | 0 | 420 |
| X024 | 0 | Eventos adicionais sem CC com inc. IRRF - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | 0 |
| X025 | 0 | Eventos adicionais sem CC - ENVELOPE PROV | Provento | 9221 | 0 | 13 | 0 | 0 |
| X026 | 0 | Eventos adicionais sem CC sem Inc. IRRF - ENVELOPE DESC | Desconto | 9221 | 0 | 9 | 0 | 0 |
| X027 | 0 | Eventos adicionais sem CC sem Inc. IRRF - ENVELOPE PROV | Provento | 9221 | 0 | 9 | 0 | 0 |
| X028 | 0 | INSS Férias Desconto Mês Anterior - ENVELOPE PROV | Provento | 9221 | 0 | 9 | 0 | 131 |
| X029 | 0 | INSS Férias Desconto Mês Anterior- ENVELOPE DESC | Desconto | 9201 | 31 | 9 | 0 | 131 |

### 1.2 - Criar os novos eventos/verbas via IMPORTAÇÃO

Caso prefira, os novos eventos/verbas podem ser criados por meio da importação de eventos.

Para isso, utilize o arquivo disponibilizado abaixo, salvando-o com a extensão **.TXT**, e realize a importação conforme o procedimento padrão do sistema.

X001;1ª Parcela 13º - ENVELOPE DESC                                                  ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;5504;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;09;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X002;IRRF Férias - ENVELOPE PROV                                                     ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;  ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;9203;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;33;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X003;Abono de Férias - ENVELOPE DESC                                                 ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;1023;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;75;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X004;1/3 Abono de Férias - ENVELOPE DESC                                             ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;1 ;0 ;1023;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X005;INSS Férias - ENVELOPE PROV                                                     ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;  ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;43;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X006;Pensão Alimentícia Férias - ENVELOPE PROV                                       ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;  ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;9213;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;53;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X007;Arredondamento Férias - ENVELOPE DESC                                           ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;2999;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;09;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X008;INSS Férias Próx. Mês  - ENVELOPE PROV                                          ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;  ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;09;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X009;Salário Família Férias - ENVELOPE DESC                                          ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;1409;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;09;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X010;Férias em Dobro - ENVELOPE DESC                                                 ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;1 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X011;Adicional 1/3 Férias em Dobro - ENVELOPE DESC                                   ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;1 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X012;Férias Mês - ENVELOPE DESC                                                      ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;1 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X013;Férias Próx. Mês - ENVELOPE DESC                                                ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;1 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X014;Férias Pagas Mês Ant. - ENVELOPE PROV                                           ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;1 ;0 ;1 ;0 ;0 ;0 ;0 ;1 ;1 ;0 ;0 ;0 ;                                                                                                    ;  ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;1 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;1016;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;11;    ;    ;    ;0 ;  ;  
X015;Férias Pagas Mês Ant. - ENVELOPE DESC                                           ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;1 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X016;1/3 Férias Mês - ENVELOPE DESC                                                  ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;1 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X017;1/3 Férias Próx. Mês - ENVELOPE DESC                                            ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;1 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X018;1/3 Férias Pagas Mês Ant. - ENVELOPE PROV                                       ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;1 ;0 ;1 ;0 ;0 ;0 ;0 ;1 ;0 ;0 ;0 ;0 ;                                                                                                    ;  ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;1 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;1017;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;11;    ;    ;    ;0 ;  ;  
X019;1/3 Férias Pagas Mês Ant. - ENVELOPE DESC                                       ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;1 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X020;Estorno Pensão sobre Férias - ENVELOPE DESC                                     ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;9213;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;53;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X021;Adiantamento Provisão Empr. Consig. Férias (Desc) - ENVELOPE PROV               ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;  ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;1299;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;09;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X022;Adiantamento Provisão Empr. Crédito Trab. - ENVELOPE PROV                       ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;1299;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;09;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X023;Previdência Privada Dedutível de IRRF Férias - ENVELOPE PROV                    ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;  ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;9223;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;48;00;    ;    ;    ;0 ;  ;  
X024;Eventos adicionais sem CC com inc. IRRF - ENVELOPE DESC                         ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;1 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X025;Eventos adicionais sem CC - ENVELOPE PROV                                       ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;1 ;0 ;0 ;0 ;0 ;                                                                                                    ;  ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;0 ;  ;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X026;Eventos adicionais sem CC sem Inc. IRRF - ENVELOPE DESC                         ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;  ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;09;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X027;Eventos adicionais sem CC sem Inc. IRRF - ENVELOPE PROV                         ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;09;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X028;INSS Férias Desconto Mês Anterior - ENVELOPE PROV                               ;  ;0;0 ;P;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;9221;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;09;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;0 ;  ;  
X029;INSS Férias Desconto Mês Anterior- ENVELOPE DESC                                ;  ;0;0 ;D;V;     0,00;0  ;0 ;        ;        ;        ;        ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;                                                                                                    ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;                      ;                      ;          ;                                                            ;                      ;                      ;    ;        ;                ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;0 ;    ;0 ;0 ;0 ;0 ;        ;  ;0 ;0 ;0 ;0 ;0 ;0 ;                         ;   ;                ;0 ;0 ;0 ;    ;  ;                    ;        ; ;0   ;0 ;0 ;0 ;9201;0 ;0 ;0 ;                    ; ;  ;                    ; ;                    ; ;0 ;                    ; ;0 ;                    ; ;0 ;    ;    ; ;  ;0 ;0 ;0 ;  ;  ;0 ;0 ;  ;0 ;0 ;0 ;0 ;0 ;1 ;09;0 ;    ;  ;  ;    ;0 ;0 ;0 ;  ;    ;  ;  ;0 ;0 ;  ;  ;  ;00;    ;    ;    ;1 ;31;

### 2 - Realizar a conferência das parametrizações dos eventos/verbas originais da base

Revise as parametrizações dos eventos/verbas já existentes na base, validando as configurações de **Natureza de Rubrica**, **Incidências** e demais informações necessárias para garantir a correta geração dos eventos do eSocial.

Clique para ver a lista de eventos a serem parametrizados

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ITEM** | **SITUAÇÃO** | **CÓDIGO EVENTO / VERBA** | **CÓDIGO CÁLCULO** | **DESCRIÇÃO** | **TIPO** | **NATUREZA RUBRICA** | **CODINCCP** | **CODINCIRRF** | **CODINCFGTS** | **EXIBIDO** | **VINCULADO** **AO EVENTO** | **OBSERVAÇÃO** |
| 1 | Já existente | Verificar no cadastro de Evento | 9 | 1ª Parcela 13º | Provento | 5504 | 0 | 9 | 12 | * Recibo de Férias * Envelope | Nenhum |  |
| 2 | Já existente | Verificar no De-Para | 0 | 1ª Parcela 13º - ANTECIPAÇÃO | Provento | 5504 | 0 | 9 | 0 | * eSocial | 9 | Este evento substitui o evento informado no **Item 1** na geração do **S-1200** de antecipação de férias, pois apenas eventos com incidência de **IRRF** podem ser enviados ao eSocial.Atualmente configurado em Parametrizador eSocial | Configurações Gerais (7/7).Campo "Evento Antecipação da Primeira Parcela do 13º nas Férias (Provento)". |
| 3 | Novo | X001 | 0 | 1ª Parcela 13º - ENVELOPE DESC | Desconto | 5504 | 0 | 9 | 0 | * eSocial | 9 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 4 | Já existente | Verificar no cadastro de Evento | 30 | IRRF Férias | Desconto | 9203 | 0 | 33 | 0 | * Recibo de Férias * Envelope * eSocial | Nenhum |  |
| 5 | Novo | X002 | 0 | IRRF Férias - ENVELOPE PROV | Provento | 9203 | 0 | 33 | 0 | * eSocial | 30107306 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 6 | Já existente | Verificar no cadastro de Evento | 38 | Férias | Provento | 1015 | 11 | 13 | 11 | * Recibo de Férias | Nenhum |  |
| 7 | Já existe | De-Para | 0 | Férias - ANTECIPAÇÃO | Provento | 1015 | 0 | 13 | 0 | * eSocial | 38309 | Este evento substitui o evento informado no **Item 6** na geração do **S-1200** de antecipação de férias, pois apenas eventos com incidência de **IRRF** podem ser enviados ao eSocial.Código do evento / verba configurado em Parametrizador eSocial | Configurações Gerais (7/7).Campo "Evento Antecipação de Férias (Vencimento)". |
| 8 | Já existente | Verificar no cadastro de Evento | 39 | Abono de Férias | Provento | 1023 | 0 | 75 | 0 | * Recibo de Férias * Envelope * eSocial | Nenhum |  |
| 9 | Novo | X003 | 0 | Abono de Férias - ENVELOPE DESC | Desconto | 1023 | 0 | 9 | 0 | * eSocial | 3947311 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 10 | Já existente | Verificar no cadastro de Evento | 40 | 1/3 Férias | Provento | 1015 | 11 | 13 | 11 | * Recibo de Férias | Nenhum |  |
| 11 | Já existente | Verificar no De-Para | 0 | 1/3 Férias - ANTECIPAÇÃO | Provento | 1015 | 0 | 13 | 0 | * eSocial | 40310 | Este evento substitui o evento informado no **Item 10** na geração do **S-1200** de antecipação de férias, pois apenas eventos com incidência de **IRRF** podem ser enviados ao eSocial.Código do evento / verba configurado em Parametrizador eSocial | Configurações Gerais (7/7).Campo "Evento Antecipação Terço de Férias (Vencimento)". |
| 12 | Já existente | Verificar no cadastro de Evento | 41 | Férias no Mês | Provento | 1016 | 11 | 13 | 11 | * Envelope | Nenhum |  |
| 13 | Novo | X012 | 0 | Férias Mês - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | * eSocial | 41 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 14 | Já existente | Verificar no cadastro de Evento | 42 | Férias do Próximo Mês | Provento | 1015 | 0 | 13 | 0 | * Envelope | Nenhum |  |
| 15 | X013 | X013 | 0 | Férias Próx. Mês - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | * eSocial | 42350 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 16 | Já existente | Verificar no cadastro de Evento | 44 | Férias Pagas no Mês Anterior | Base de calculo | 1016 | 11 | 9 | 11 | * Envelope | Nenhum |  |
| 17 | Novo | X014 | 0 | Férias Pagas Mês Ant. - ENVELOPE PROV | Provento | 1016 | 11 | 13 | 11 | * eSocial | 44 | Este evento substitui o informado no **Item 16** na geração do **S-1200**, pois o eSocial espera um evento do tipo **provento**. |
| 18 | Novo | X015 | 0 | Férias Pagas Mês Ant. - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | * eSocial | 44 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 19 | Já existente | Verificar no cadastro de Evento | 47 | Média de Abono de Férias | Provento | 1023 | 0 | 75 | 0 | * Recibo de Férias * Envelope | Nenhum |  |
| 20 | Novo | X003 | 0 | Abono de Férias - ENVELOPE DESC | Desconto | 1023 | 00 | 75 | 00 | * eSocial | 3947311 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 21 | Já existente | Verificar no cadastro de Evento | 56 | 1/3 Abono de Férias | Provento | 1023 | 0 | 13 | 0 | * Recibo de Férias * Envelope | Nenhum |  |
| 22 | Novo | X004 | 0 | 1/3 Abono de Férias - ENVELOPE DESC | Desconto | 1023 | 0 | 13 | 0 | * eSocial | 56312 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 23 | Já existente | Verificar no cadastro de Evento | 76 | 1/3 Férias no Mês | Provento | 1017 | 11 | 13 | 11 | * Envelope | Nenhum |  |
| 24 | Novo | X016 | 0 | 1/3 Férias Mês - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | * eSocial | 76 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 25 | Já existente | Verificar no cadastro de Evento | 77 | 1/3 Férias no Próximo Mês | Provento | 1015 | 0 | 13 | 0 | * Envelope | Nenhum |  |
| 26 | Novo | X017 | 0 | 1/3 Férias Próx. Mês - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | * eSocial | 77351 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 27 | Já existente | Verificar no cadastro de Evento | 78 | 1/3 Férias Pagas no Mês Anterior | Base de calculo | 1017 | 11 | 9 | 11 | * Envelope | Nenhum |  |
| 28 | Novo | X018 | 0 | 1/3 Férias Pagas Mês Ant. - ENVELOPE PROV | Provento | 1017 | 11 | 13 | 11 | * eSocial | 78 | Este evento substitui o informado no **Item 27** na geração do **S-1200**, pois o eSocial espera um evento do tipo **provento**. |
| 29 | Novo | X019 | 0 | 1/3 Férias Pagas Mês Ant. - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | * eSocial | 78 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 30 | Já existente | Verificar no cadastro de Evento | 82 | INSS Férias | Desconto | 9201 | 31 | 43 | 0 | * Recibo de Férias * Envelope | Nenhum |  |
| 31 | Já existente | Verificar no De-Para | 0 | INSS Férias - ANTECIPAÇÃO | Desconto | 9205 | 0 | 43 | 0 | * eSocial | 82130141142349 | Este evento substitui o informado no **Item 30** na geração do **S-1200** de antecipação de férias, para evitar duplicidade, pois já consta no recibo de férias e no envelope.Código do evento / verba configurado em Parametrizador eSocial | Configurações Gerais (6/7).Campo "Evento INSS Antecipação de Férias (Desconto)". |
| 32 | Novo | X005 | 0 | INSS Férias - ENVELOPE PROV | Provento | 9221 | 0 | 43 | 0 | * eSocial | 82130141142349 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 33 | Já existente | Verificar no cadastro de Evento | 107 | IRRF de férias calculado pelo usuário | Desconto | 9203 | 0 | 33 | 0 | * Envelope | Nenhum |  |
| 34 | Novo | X002 | 0 | IRRF Férias - ENVELOPE PROV | Provento | 9203 | 00 | 33 | 00 | * eSocial | 30107306 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 35 | Já existente | Verificar no cadastro de Evento | 113 | Pensão Alimentícia Férias | Desconto | 9213 | 0 | 53 | 0 | * Recibo de Férias * Envelope | Nenhum |  |
| 36 | Novo | X006 | 0 | Pensão Alimentícia Férias - ENVELOPE PROV | Provento | 9213 | 0 | 53 | 0 | * eSocial | 113320 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 37 | Já existente | Verificar no cadastro de Evento | 129 | Arredondamento de Férias | Provento | 2999 | 0 | 9 | 0 | * Envelope | Nenhum |  |
| 38 | Novo | X007 | 0 | Arredondamento Férias - ENVELOPE DESC | Desconto | 2999 | 0 | 9 | 0 | * eSocial | 129 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 39 | Já existente | Verificar no cadastro de Evento | 130 | INSS Férias Próximo Mês | Desconto | 9205 | 0 | 43 | 0 | * Recibo de Férias * Envelope | Nenhum |  |
| 40 | Novo | X005 | 0 | INSS Férias - ENVELOPE PROV | Provento | 9221 | 0 | 43 | 0 | * eSocial | 82130141349 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 41 | Já existente | Verificar no cadastro de Evento | 131 | INSS Férias Desconto Mês Anterior | Base de calculo | 9201 | 31 | 9 | 0 | * Envelope | Nenhum |  |
| 42 | Novo | X029 | 0 | INSS Férias Desconto Mês Anterior- ENVELOPE DESC | Desconto | 9201 | 31 | 9 | 0 | * eSocial | 131 | Este evento substitui o informado no **Item 41** na geração do **S-1200**, pois o eSocial espera um evento do tipo **desconto**. |
| 43 | Novo | X028 | 0 | INSS Férias Desconto Mês Anterior - ENVELOPE PROV | Provento | 9221 | 0 | 9 | 0 | * eSocial | 131 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 44 | Já existente | Verificar no cadastro de Evento | 141 | INSS Férias no mês (informado) | Desconto | 9201 | 31 | 43 | 0 | * Envelope | Nenhum |  |
| 45 | Novo | X005 | 0 | INSS Férias - ENVELOPE PROV | Provento | 9221 | 0 | 43 | 0 | * eSocial | 82130141349 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 46 | Já existente | Verificar no cadastro de Evento | 142 | INSS Férias Próx. Mês (informado) | Desconto | 9205 | 0 | 9 | 0 | * Envelope | Nenhum |  |
| 47 | Novo | X008 | 0 | INSS Férias Próx. Mês - ENVELOPE PROV | Provento | 9221 | 0 | 9 | 0 | * eSocial | 142 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 48 | Já existente | Verificar no cadastro de Evento | 149 | Salário Família Férias | Provento | 1409 | 51 | 9 | 0 | * Recibo de Férias * Envelope * eSocial | Nenhum |  |
| 49 | Já existente | Verificar no De-Para | 0 | Salário Família Férias - ANTECIPAÇÃO | Provento | 1409 | 0 | 9 | 0 | * Envelope * eSocial | 149 | Este evento substitui o informado no **Item 48** na geração do **S-1200** de antecipação de férias, para evitar duplicidade, pois já consta no recibo de férias e no envelope.Código do evento / verba configurado em Parametrizador eSocial | Configurações Gerais (7/7).Campo "Evento Salário Família Antecipação de Férias (Provento)". |
| 50 | Novo | X009 | 0 | Salário Família Férias - ENVELOPE DESC | Desconto | 1409 | 0 | 9 | 0 | * eSocial | 149 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 51 | Já existente | Verificar no cadastro de Evento | 201 | Estorno Pensão Alimentícia sobre Férias | Provento | 9213 | 0 | 53 | 0 | * Envelope | Nenhum |  |
| 52 | Novo | X020 | 0 | Estorno Pensão sobre Férias - ENVELOPE DESC | Desconto | 9213 | 0 | 53 | 0 | * eSocial | 201 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 53 | Já existente | Verificar no cadastro de Evento | 309 | Férias em Dobro | Provento | 10161024 | 11 | 13 | 11 | * Recibo de Férias * Envelope * eSocial | Nenhum |  |
| 54 | Novo | X010 | 0 | Férias em Dobro - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | * eSocial | 309 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 55 | Já existente | Verificar no cadastro de Evento | 310 | Adicional 1/3 Férias em Dobro | Provento | 10171024 | 11 | 13 | 11 | * Envelope * eSocial | Nenhum |  |
| 56 | Novo | X011 | 0 | Adicional 1/3 Férias em Dobro - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | * eSocial | 310 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 57 | Já existente | Verificar no cadastro de Evento | 311 | Abono de Férias em Dobro | Provento | 1023 | 0 | 75 | 0 | * Recibo de Férias * Envelope * eSocial |  |  |
| 58 | Novo | X003 | 0 | Abono de Férias - ENVELOPE DESC | Desconto | 1023 | 0 | 75 | 0 | * eSocial | 3947311 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 59 | Já existente | Verificar no cadastro de Evento | 312 | 1/3 Abono de Férias em Dobro | Provento | 1023 | 0 | 13 | 0 | * Recibo de Férias * Envelope * eSocial |  |  |
| 60 | Novo | X004 | 0 | 1/3 Abono de Férias - ENVELOPE DESC | Desconto | 1023 | 0 | 13 | 0 | * eSocial | 56312 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 61 | Já existente | Verificar no cadastro de Evento | 320 | Pensão Alimentícia Férias Informada | Desconto | 9213 | 0 | 53 | 0 | * Recibo de Férias * Envelope * eSocial |  |  |
| 62 | Novo | X006 | 0 | Pensão Alimentícia Férias - ENVELOPE PROV | Provento | 9213 | 0 | 53 | 0 | * eSocial | 113320 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 63 | Já existente | Verificar no cadastro de Evento | 349 | INSS Férias no Terceiro Mês | Desconto | 9205 | 0 | 43 | 0 | * Recibo de Férias * Envelope * eSocial |  |  |
| 64 | Novo | X005 | 0 | INSS Férias - ENVELOPE PROV | Provento | 9221 | 0 | 43 | 0 | * eSocial | 82130141349 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 65 | Já existente | Verificar no cadastro de Evento | 350 | Férias no Terceiro Mês | Provento | 1015 | 0 | 13 | 0 | * Envelope * eSocial |  |  |
| 66 | Novo | X013 | 0 | Férias Próx. Mês - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | * eSocial | 42350 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 67 | Já existente | Verificar no cadastro de Evento | 351 | 1/3 Férias no Terceiro Mês | Provento | 1015 | 0 | 13 | 0 | * Envelope * eSocial |  |  |
| 68 | Novo | X017 | 0 | 1/3 Férias Próx. Mês - ENVELOPE DESC | Desconto | 9221 | 0 | 13 | 0 | * eSocial | 77351 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 69 | Já existente | Verificar no cadastro de Evento | 420 | Previdência Privada Dedutível de IRRF Férias | Desconto | 922592249223 | 0 | 48 | 0 | * Recibo de Férias * Envelope * eSocial |  |  |
| 70 | Novo | X023 | 0 | Previdência Privada Dedutível de IRRF Férias - ENVELOPE PROV | Provento | 922592249223 | 0 | 48 | 0 | * eSocial | 420 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 71 | Já existente | Verificar no cadastro de Evento | 466 | Adiantamento Provisão Empréstimo Consignado Férias (Desconto) | Desconto | 9299 | 0 | 9 | 0 | * Recibo de Férias * Envelope * eSocial |  |  |
| 72 | Novo | X021 | 0 | Adiantamento Provisão Empr. Consig. Férias (Desc) - ENVELOPE PROV | Provento | 1299 | 0 | 9 | 0 | * eSocial | 466 | Este evento será enviado ao eSocial para zerar o valor líquido. |
| 73 | Já existente | Verificar no cadastro de Evento | 489 | Adiantamento Provisão Empr. Crédito Trab. | Desconto | 9299 | 0 | 9 | 0 | * Envelope * eSocial |  |  |
| 74 | Novo | X022 | 0 | Adiantamento Provisão Empr. Crédito Trab. - ENVELOPE PROV | Provento | 9299 | 0 | 9 | 0 | * eSocial | 489 | Este evento será enviado ao eSocial para zerar o valor líquido. |

false⚠️ ATENÇÃO: 

* Antes da execução do Conversor do Parametrizador dos Eventos de Férias o cadastro de eventos não cobrará as vinculações do De/para para permitir as conferências e alterações necessarias nos eventos originais.
* Eventos/verbas com **incidências suspensas** vinculadas aos códigos de cálculo citados acima **não terão suas Incidências eSocial validadas**. Avalie a necessidade de revisar e ajustar os pares de incidências configurados.

### 3. Para evitar duplicidade de incidências

É necessário configurar as verbas do **Recibo de Férias** e do **Envelope de Pagamento** para os códigos de cálculo indicados abaixo, realizando o correto vínculo dos eventos conforme as novas regras do eSocial.

| CÓDIGO DE CÁLCULO |
| --- |
| [9 - 1ª Parcela 13º Salário](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718743) |
| [30 - I.R.R.F. Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718236) |
| [38 - Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718560) |
| [39 - Abono de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719764) |
| [40 - 1/3 de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719013) |
| [41 - Férias do mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452718570) |
| [42 - Férias do próximo mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452718562) |
| [44 - Férias pagas no mês anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=452718568) |
| [47 - Média de abono de férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718717) |
| [56 - 1/3 Abono de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719005) |
| [76 - 1/3 Férias no mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719012) |
| [77 - 1/3 Férias no próximo mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719010) |
| [78 - 1/3 férias pagas mês anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=452719011) |
| [82 - I.N.S.S. Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718205) |
| [107 - IRRF de férias calculado pelo usuário](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718237) |
| [113 - Pensão alimentícia sobre férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718804) |
| [129 - Arredondamento de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719802) |
| [130 - I.N.S.S. Férias próx. mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718229) |
| [131 - I.N.S.S. Férias desc. mês ant.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718225) |
| [141 - INSS Férias no mês (informado)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718223) |
| [142 - INSS Férias próx. mês (informado)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718227) |
| [149 - Salário Família nas Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719066) |
| [201 - ESTORNO DE PENSÃO ALIMENTÍCIA SOBRE FÉRIAS](https://tdn.totvs.com/pages/viewpage.action?pageId=452718669) |
| [309 - Férias em Dobro](https://tdn.totvs.com/pages/viewpage.action?pageId=452718557) |
| [310 - Adicional 1/3 de Férias em Dobro](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719770) |
| [311 - Abono de Férias em Dobro](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719762) |
| [312 - Adicional 1/3 Abono de Férias em Dobro](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719773) |
| [320 - Pensão Alimentícia Férias Informada](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718803) |
| [349 - INSS Férias no Terceiro Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719459) |
| [350 - Férias no Terceiro Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719949) |
| [351 - Adicional de 1/3 Férias no Terceiro Mês](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719883) |
| [420 - Previdência Privada Dedutível de IRRF Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=518477913) |
| [466 - Adiantamento Provisão Empréstimo Consignado Férias (Desconto)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=777277297) |
| [489 - Adiantamento Provisão Emprést. Crédito Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=944707701) |

Veja mais detalhes nos links:

* [Cadastro de Eventos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719284)
* [S-1010](https://tdn.totvs.com/display/LRM/S-1010+-+Tabela+de+Rubricas)
* [Mapeamento S-1010](https://tdn.totvs.com/display/LRM/Evento+S-1010)
2Conversor do Parametrizador dos Eventos de Férias

## **Menu eSocial eSocial | Outros Processos | Conversor do Parametrizador dos Eventos de Férias**

false⚠️ ATENÇÃO:

**ANTES DE EXECUTAR O CONVERSOR DO PARAMETRIZADOR DOS EVENTOS DE FÉRIAS É NECESSÁRIO CRIAR/IMPORTAR OS EVENTOS/VERBAS CONFORME ORIENTADO NA ABA EVENTOS/VERBAS.**

Execute o processo Conversor do Parametrizador dos Eventos de Férias para realizar a vinculação automática das novas rubricas criadas ou importadas aos respectivos eventos, conforme as parametrizações necessárias para geração dos XMLs do eSocial.

Clique para ver a lista de eventos a serem criados

| CÓDIGO DE CÁLCULO | DESCRIÇÃO CÓDIGO DE CÁLCULO | ANTECIPAÇÃO DE FÉRIAS (PROVENTO | DESCONTO) | ENVELOPE DE PAGAMENTO (PROVENTO) | ENVELOPE DE PAGAMENTO (DESCONTO) |
| --- | --- | --- | --- | --- |
| 0 | Evento adicional provento com incidencia IRRF |  |  | X024 |
| 0 | Evento adicional Desconto com incidencia IRRF |  | X025 |  |
| 0 | Evento adicional provento sem incidencia IRRF |  |  | X026 |
| 0 | Evento adicional Desconto sem incidencia IRRF |  | X027 |  |
| 9 | [1ª Parcela 13º Salário](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718743) | De-Para |  | X001 |
| 30 | [I.R.R.F. Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718236) |  | X002 |  |
| 38 | [Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718560) | De-Para |  |  |
| 39 | [Abono de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719764) |  |  | X003 |
| 40 | [1/3 de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719013) | De-Para |  |  |
| 41 | [Férias do mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452718570) |  |  | X012 |
| 42 | [Férias do próximo mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452718562) |  |  | X013 |
| 44 | [Férias pagas no mês anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=452718568) |  | X014 | X015 |
| 47 | [Média de abono de férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718717) |  |  | X003 |
| 56 | [1/3 Abono de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719005) |  |  | X004 |
| 76 | [1/3 Férias no mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719012) |  |  | X016 |
| 77 | [1/3 Férias no próximo mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719010) |  |  | X017 |
| 78 | [1/3 férias pagas mês anterior](https://tdn.totvs.com/pages/viewpage.action?pageId=452719011) |  | X018 | X019 |
| 82 | [I.N.S.S. Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718205) | De-Para | X005 |  |
| 107 | [IRRF de férias calculado pelo usuário](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718237) |  | X002 |  |
| 113 | [Pensão alimentícia sobre férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718804) |  | X006 |  |
| 129 | [Arredondamento de Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719802) |  |  | X007 |
| 130 | [I.N.S.S. Férias próx. mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718229) | De-Para | X005 |  |
| 131 | [I.N.S.S. Férias desc. mês ant.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718225) |  | X028 | X029 |
| 141 | [INSS Férias no mês (informado)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718223) | De-Para | X005 |  |
| 142 | [INSS Férias próx. mês (informado)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718227) | De-Para | X008 |  |
| 149 | [Salário Família nas Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719066) | De-Para |  | X009 |
| 201 | [ESTORNO DE PENSÃO ALIMENTÍCIA SOBRE FÉRIAS](https://tdn.totvs.com/pages/viewpage.action?pageId=452718669) |  |  | X020 |
| 309 | [Férias em Dobro](https://tdn.totvs.com/pages/viewpage.action?pageId=452718557) | De-Para |  | X010 |
| 310 | [Adicional 1/3 de Férias em Dobro](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719770) | De-Para |  | X011 |
| 311 | [Abono de Férias em Dobro](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719762) |  |  | X003 |
| 312 | [Adicional 1/3 Abono de Férias em Dobro](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719773) |  |  | X004 |
| 320 | [Pensão Alimentícia Férias Informada](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718803) |  | X006 |  |
| 349 | [INSS Férias no Terceiro Mês](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719459) | De-Para | X005 |  |
| 350 | [Férias no Terceiro Mês](https://tdn.totvs.com/pages/viewpage.action?pageId=452719949) |  |  | X013 |
| 351 | [Adicional de 1/3 Férias no Terceiro Mês](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452719883) |  |  | X017 |
| 420 | [Previdência Privada Dedutível de IRRF Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=518477913) |  | X023 |  |
| 466 | [Adiantamento Provisão Empréstimo Consignado Férias (Desconto)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=777277297) |  | X021 |  |
| 489 | [Adiantamento Provisão Emprést.Crédito Trabalhador](https://tdn.totvs.com.br/pages/releaseview.action?pageId=944707701) |  |  | X022 |

false⚠️ ATENÇÃO: 

* As configurações de **De-Para da Antecipação de Férias** serão preenchidas automaticamente pelo sistema com base nas informações cadastradas em Configurações | Parametrizador | eSocial | [Configurações Gerais 7/7](https://tdn.totvs.com/pages/viewpage.action?pageId=645896860).Assim, será necessário apenas realizar a vinculação nos eventos que não possuem código de cálculo.
* Eventos/verbas com **incidências suspensas** vinculadas aos códigos de cálculo citados acima **não terão suas Incidências eSocial validadas**. Avalie a necessidade de revisar e ajustar os pares de incidências configurados.
* A execução do **Conversor do Parametrizador dos Eventos de Férias** atualiza as Incidências eSocial de **todos os eventos/verbas** existentes na base.
* Serão visualizados inclusive os eventos/verbas "desativados", isso porque não tem como sabermos quando foi desativado

Veja mais detalhes no link:

10Comparativo de Incidências de Rubricas

## **Menu eSocial | Outros processos | Comparativo de Incidências de Rubricas**

Em implementação

Veja mais detalhes no link:

7Fila de Eventos

## **Menu eSocial | Fila de Eventos | S-1010 | Processos | Atualizar competência da fila de eventos S-1010**

Deverá executar a rotina "Atualizar competência da fila de eventos S-1010" para alterar o início de validade em lote para todas as novas verbas informando o início de validade desejado.

Veja mais detalhes no link:

* [Fila de Eventos](https://tdn.totvs.com.br/display/public/LRM/Fila+de+Eventos)
8S-1010

## **Menu eSocial | Gerar XML | Evento S-1010**

Deverá enviar as novas verbas criadas para o eSocial após a alteração da competência no passo da aba Fila de eventos.

9Retificação

## **Menu eSocial | Gerar XML**

1 - Deverá reabrir a folha de 01/2026

2 - Deverá excluir o S-1210

3 - Deverá retificar os eventos S-1200, S-2299 e S-2399 e S-1210.

Veja todos os detalhes sobre a retificação no link:

ATENÇÃO!

O processo acima deverá ser realizado mês a mês desde 01/2026 até a competência anterior a competência atual.

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

## **03.** **EXEMPLOS DO COMPORTAMENTO**

Clique nos links abaixo para visualizar exemplos práticos do comportamento do sistema, demonstrando como as informações serão processadas e enviadas após as alterações implementadas no produto **Folha de Pagamento**.

Exemplos de comportamento11Ferias no mêsFerias no mês

### **FÉRIAS NO MÊS**

Funcionário com gozo de férias dentro da competência **02/2026**.

1 - Foi realizado o cálculo do **Recibo de Férias**.

2 - Na geração do XML da **Antecipação de Férias**, o sistema considera os eventos configurados nos campos **Antecipação de Férias (Provento/Desconto)**. Os eventos vinculados podem ser visualizados na própria grid do recibo, por meio da coluna **"De-Para Verbas"**.

3 - As férias foram lançadas no **Envelope de Pagamento**. Como se trata de férias integrais no mês, foram gerados os eventos dos **Códigos de Cálculo 41 (Férias no Mês)** e **76 (1/3 de Férias no Mês)**.

4 - Na geração do XML do **Envelope de Pagamento**, o sistema considera os eventos configurados nos campos **Envelope de Pagamento (Provento)** e **Envelope de Pagamento (Desconto)**. Os eventos vinculados podem ser visualizados na grid do envelope por meio das colunas **"De-Para Provento"** e **"De-Para Desconto"**

false⚠️ ATENÇÃO: Mudança na Geração do XML

* **Lógica de Substituição:**

  + **Preenchimento Parcial:** Caso seja informado apenas o evento de provento (ou apenas o de desconto), o sistema gerará o evento original acompanhado de seu respectivo par correspondente.
  + **Preenchimento Integral:** Caso ambos os campos (provento e desconto) estejam preenchidos, o sistema desconsidera o evento original e reporta apenas os dois novos eventos parametrizados.
* A geração do XML não realizará o **'De-Para'** nos eventos das tabelas **PFVERBASDIS** e **PFVERBASDISFER.** O processo de **'De-Para'** será executado apenas quando a verba for originada da tabela **PFFINANC**.
1Ferias no mês e proximo mêsFerias no mêse proximo mês

### FÉRIAS PARTIDAS (MÊS E PRÓXIMO MÊS)

Funcionário com gozo de férias iniciando na competência **02/2026** e terminando na competência **03/2026**.

1 - Foi realizado o cálculo do **Recibo de Férias**.

2 - Na geração do XML da **Antecipação de Férias**, o sistema considera os eventos configurados nos campos **Antecipação de Férias (Provento/Desconto)**. Os eventos vinculados podem ser visualizados na própria grid do recibo, por meio da coluna **"De-Para Verbas"**.

3 - As férias foram lançadas no **Envelope de Pagamento**. Como o período de férias abrange duas competências, no mês de fevereiro foram gerados os eventos dos **Códigos de Cálculo 41, 76, 42 e 77**.

4 - Na geração do XML do **Envelope de Pagamento** referente ao mês 02/2026, o sistema considera os eventos configurados nos campos **Envelope de Pagamento (Provento)** e **Envelope de Pagamento (Desconto)**. Os eventos vinculados podem ser visualizados na grid do envelope por meio das colunas **"De-Para Provento"** e **"De-Para Desconto"**.

5 - Na finalização das férias no mês 03/2026, foram lançados no **Envelope de Pagamento** os eventos dos **Códigos de Cálculo 44 e 78**, referentes ao encerramento do período de férias.

6 - Observe que, para os eventos de **base de cálculo**, o preenchimento dos campos de Provento e Desconto ocorre de forma integral. Nessa situação, o evento original é desconsiderado na geração do XML, sendo substituído pelo par de eventos configurados (Provento e Desconto).

false⚠️ ATENÇÃO: Mudança na Geração do XML

* **Lógica de Substituição:**

  + **Preenchimento Parcial:** Caso seja informado apenas o evento de provento (ou apenas o de desconto), o sistema gerará o evento original acompanhado de seu respectivo par correspondente.
  + **Preenchimento Integral:** Caso ambos os campos (provento e desconto) estejam preenchidos, o sistema desconsidera o evento original e reporta apenas os dois novos eventos parametrizados.
* A geração do XML não realizará o **'De-Para'** nos eventos das tabelas **PFVERBASDIS** e **PFVERBASDISFER.** O processo de **'De-Para'** será executado apenas quando a verba for originada da tabela **PFFINANC**.

**\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**

## **04. DOCUMENTAÇÕES RELACIONADAS**

* [MOS S-1.3 | 07/2026](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-07-2026-com-marcacoes.pdf)
* [Nota Técnica S-1.3 04-2025 | Revisada 26-08-2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-04-2025-rev-26-08-2025.pdf)
* [Abono Salarial - Manual de Orientação - Atualizado 22-05-26](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/trabalhador/abono-salarial/manual-de-orientacao-para-o-empregador-atualizado-22-05.pdf)
