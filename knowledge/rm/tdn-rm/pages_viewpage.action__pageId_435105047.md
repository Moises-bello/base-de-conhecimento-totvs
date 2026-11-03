---
content_hash: 8107e1e27dd5564e9b29868a4e4aa5f62f3800924aa5ecdb42839d9a62bf1fe7
fetched_at: '2026-06-29T00:09:47.689460+00:00'
page_id: '435105047'
product: rm
source: tdn-rm
title: Totvs Incorporação - Parâmetros - Portal do Cliente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105047
version: 26
---

# **A) Relatórios**

---

Nesta opção temos os parâmetros do TOTVS Portal Incorporação. Para a utilização da Segunda Via e Impressão do Boleto no TOTVS Portal Incorporação, deve ser preenchido os seguintes parâmetros no sistema. São eles:

* **Relatório para impressão de Ficha Financeira:**Neste campo é definido qual relatório do sistema será usado para impressão das Fichas Financeiras no Portal.
* **Relatório para impressão de Informe de Pagamentos - IR:**Neste campo é definido qual relatório do sistema será usado para impressão do Informe de Pagamentos - IR no Portal.
* **Exibir todo o plano de financiamento:** Se a opção estiver desmarcada o Portal do Cliente irá exibir as parcelas vencidas e a parcela que vence no mês atual. Se a opção estiver marcada serão exibidas todas as parcelas, incluindo as vincendas.
* **Permite antecipação de pagamento:**Este parâmetro permite a incorporadora indicar se o Portal TIN deve ou não disponibilizar parcelas financeiras com vencimento futuro para antecipação do pagamento. Para o correto funcionamento do recurso de Antecipação de Pagamento, o recurso de reajuste online do financeiro deve estar ativado para cálculo de valores contratuais(Juros e CM), caso contrário não haverá atualização dos valores contratuais.
  + **Pode antecipar, mesmo com parcela atrasada:** Marque esta opção para permitir que o cliente possa antecipar o pagamento das parcelas vincenda (a vencer), mesmo que ele tenha parcelas vencidas, em aberto.
  + **Ordem de antecipação de pagamento:** Utilize essa opção para definir em qual ordem o cliente pode selecionar as parcelas para a antecipação, sendo:
    - *Qualquer parcela*: o cliente pode selecionar qualquer parcela da lista para antecipar.
    - *Da primeira para a última*: o cliente só pode antecipar as parcelas em ordem crescente de vencimento, em relação à data de acesso ao PDC.
    - *Da última para a primeira:* o cliente só pode antecipar as parcelas em ordem decrescente de vencimento, em relação à data de acesso ao PDC.
* **Limitar vencimento do boleto até o último dia do mês atual:** Utilize esse opção para limitar o vencimento do boleto para até o último dia do mês de acesso ao PDC.
* **Número máximo de dias para vencimento do boleto:** Defina o número máximo de dias, em relação à data de acesso ao PDC, para que o cliente possa definir a data de vencimento do boleto. Este parâmetro respeita a parametrização  acima, sendo que o sistema não aceita números  negativos.
* **Permite gerar novo boleto parcela vencida e do mês:** Nem todas as empresas permitem que sejam gerados novos títulos para parcelas já vencidas sendo necessário a parametrização para que cada cliente estabeleça seus próprios critérios.
* **Opções de pagamento para as parcelas:** Este parâmetro define se novos boletos ou a antecipação de boleto será feita pelo processo de registro online ou pelo processo de gerar boletos não registrados. Abaixo temos uma explicação de cada item:
  + **Registro Online**: A geração do boleto é feita pela entidade bancária.
  + **Pix TPD:** O Pix para pagamento desse boleto é gerado diretamente na entidade bancária cadastrada para o cliente, sem a intermediação de nenhuma outra entidade bancária.
  + **Registro Online / Pix TPD**: São geradas as duas opções de pagamento acima, cabendo ao cliente escolher a que melhor lhe atende.
  + **Boleto Híbrido**: Geração do boleto com código de barras e o QrCode do Pix, ou seja as duas modalidades de pagamento em um único documento. Para mais informações e instruções de configuração, acesse [Boleto Híbrido](https://tdn.totvs.com/pages/releaseview.action?pageId=908344227#0-1).

Importante!

Quando configurado a opção de pagamento pelo Boleto Híbrido, é importante que o relatório associado a esta opção esteja preparado para a tratar tanto a impressão do Código de Barras e como a impressão do QR Code do PIX.

* **Exibir Valores Sumarizados do Contrato:** Permite exibir ou não os campos de "Valor Total Financiado Atualizado", "Saldo Devedor" e "Valor Total Pago" da visão de Situação Financeira
* **Limitar o acesso do Comprador Principal desativado:** Essa opção permite limitar o acesso do antigo Comprador Principal, para que ele veja somente as parcelas e os boletos que estão atribuídos a ele e não mais os de todo o contrato.

# **B) Termo de Aceite**

---

Parametrizações do relatório de Termo de Aceite, de acordo com a LGPD.

* **Relatório para exibição do Termo de Aceite**: Neste parâmetro deverá ser definido o relatório de Termo de Aceite que será exibido no login do usuário do PdC.
* **Versão**: Versão do Relatório de termo de aceite. Esse campo deverá ser um número inteiro e sempre incremental.

# **C) Renegociação de Contrato**

---

Estes parâmetros do sistema, possibilitam configurar como os recursos de Renegociação de Contrato serão utilizados Portal do Cliente. Veja abaixo maiores detalhes destes recursos:

* **Permite efetivação automática da renegociação de contrato:**Este parâmetro determina se a efetivação da renegociação de contrato será automática ou não. Quando o parâmetro é marcado os parâmetros Valor máximo para renegociação e Número máximo de parcelas são habilitados.
  + **Valor máximo para renegociação:**Neste parâmetro é informado qual o valor máximo para renegociação.
  + **Número máximo de parcelas:**Neste parâmetro é informado o número máximo de parcelas para a renegociação.
* **Dias corridos para o primeiro vencimento:**Neste campo é preciso informar a quantidade de dias corridos para o primeiro vencimento.
* **Limite de parcelas:** Disponível a partir da versão 12.1.35. Neste parâmetro será informado o limite de parcelas para gerar o valor da renegociação.

No Portal do Cliente haverá uma limitação para inclusão do número de parcelas que serão renegociadas.   
Observe neste exemplo abaixo que a quantidade encontra-se limitada a 10 parcelas.

* **E-mail do(s) responsáveis pela aprovação (separado por ponto e vírgula):**Neste campo são informados os e-mails dos responsáveis pela aprovação das Renegociações de Contrato feitas pelo Portal do Cliente. Os e-mails informados irão ser notificados quando for necessária a aprovação de alguma Renegociação.
* **Termo da Renegociação**: Disponível a partir da versão 12.1.28, neste campo deveremos preencher o relatório que possui os termos da renegociação, que será apresentado na visão de renegociação ao realizar uma proposta no Meu Imóvel e no PDC. A TOTVS [disponibiliza](https://tdn.totvs.com/pages/viewpage.action?pageId=544188979) um relatório, que poderá ser utilizado como modelo.

# **D) Parâmetros de Aplicativo**

---

Nesta etapa o sistema apresenta os seguintes parâmetros:

* **Usar Multiportal:** Ao marcar esta opção as incorporadoras poderão trabalhar com mais de um Portal do Cliente - PDC, possibilitando separar portais por diferentes segmentos de atuação da empresa ou até por diferentes coligadas dentro da sua estrutura. Dessa forma, será possível direcionar seus clientes à portais que tratam especificamente seu contexto. Após marcá-lo, consulte .
* **URL de Acesso externo ao Host:** Informe a url com acesso externo para que o app Meu Imóvel se conecte ao RM para enviar e receber as requisições de dados realizadas diretamente no Meu Imóvel;
* **Título do Texto que será Exibido na Tela de Informações do Aplicativo:** Insira o Título que será exibido ao usuário do Meu Imóvel, quando ele acessar a tela de Informações neste app. Exemplo: Bem vindo ao Meu Imóvel da TOTVS;
* **Texto que será Exibido na Tela de Informações do Aplicativo:** Insira o Texto descritivo que será exibido ao usuário do Meu Imóvel, quando ele acessar a tela de Informações neste app;
