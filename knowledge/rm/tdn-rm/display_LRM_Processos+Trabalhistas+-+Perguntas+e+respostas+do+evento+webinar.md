---
content_hash: 1b65d191d66925e527af95e78f2e15828c757f56154514ba3c71d3ac28d542a8
fetched_at: '2026-06-29T00:11:43.067764+00:00'
page_id: '801334020'
product: rm
source: tdn-rm
title: Processos Trabalhistas - Perguntas e respostas do evento webinar
type: documentation
url: https://tdn.totvs.com/display/LRM/Processos+Trabalhistas+-+Perguntas+e+respostas+do+evento+webinar
version: 3
---

**Última atualização:** 31/10/2023

Listamos abaixo as perguntas e respostas realizadas no último evento Webinar Tira Dúvidas, referente ao Processo Trabalhista (S-1.1)

Clique para expandir a lista de perguntas

#### **001 - O cadastro de processos trabalhistas buscará dados já cadastrados no sistema? Será possível realizar a exportação/importação de arquivos provenientes de sistemas jurídicos?**

Nenhum dado já cadastrado no RM será reutilizado no cadastro dos processos trabalhistas. Sendo necessário preencher as informações de forma manual, salvo apenas os campos que apresentam valores pré-definidos no layout do eSocial, os quais já irão apresentar informações para seleção. Dessa forma será necessário o preenchimento manual das informações.

O cadastro em questão é totalmente desvinculado do produto, ou seja, não serão exibidas informações cadastradas no produto. Foram criadas novas tabelas para atender o Processo Trabalhista, sendo assim:

* Não haverá validação com outros eventos do eSocial, por exemplo: Folha e SST.
* Não possui regra de negócio específica.
* Não possui integração com Folha, SST e Financeiro.
* Foi disponibilizado no TAF o cadastro desses eventos também, disponível para clientes TAF FULL.

Atualmente não há funcionalidade ou processo que permita a importação/exportação dos dados. Contudo, você poderá incluir uma sugestão em nossa Central Colaborativa. Tal sugestão será avaliada pelo time de desenvolvimento do produto e, se aprovada, será incluída em Road Map para implementações futuras. 

Central Colaborativa: <https://centraldeatendimento.totvs.com/hc/pt-br/community/topics> 

Road Map - TOTVS RH - Linha RM: <https://produtos.totvs.com/produto/totvs-rh/totvs-rh-linha-rm/> 

#### **002 - Quem deverá declarar o processo e pagar o valor da condenação?**

Quase sempre será o próprio empregador. Uma vez que ele é vencido em alguma parte no julgamento, ele deverá declarar estes dados. Lembrando que quando a empresa não é condenada, não há necessidade de envio do evento.

Em casos de terceirização do trabalho, o processo trabalhista envolve tanto o empregador quanto a empresa que contratou o serviço. Neste caso, supondo que a empregadora por algum motivo não cumpre sua obrigação conforme a decisão do juiz , a subsidiária será a empresa a transmitir o processo ao eSocial, mesmo ela não sendo a empregadora. 

#### **003 - O envio dos processos trabalhistas há escalonamento (faseamento de grupos do eSocial)?**

Apesar de existirem 4 grupos distintos para este evento não haverá faseamento, não havendo distinção entre os grupos, estando todos obrigados a efetuar o envio mediante entrada em produção.

#### **004 - As informações enviadas nos eventos de processos trabalhistas são totalmente novas?**

Não são. Os dados que passarão a ser enviados nestes eventos as empresas já prestavam contas ao governo, por exemplo,  por meio da GFIP, mas com a entrada dos processos trabalhistas as informações passarão a serem enviadas de forma estruturada. 

#### **005 - Quais as formas as empresas possuem para envio desses eventos?**

A forma de envio se dará da mesma forma que os demais eventos do eSocial. O empregador poderá utilizar o próprio portal do eSocial através do módulo específico para inclusão de processos trabalhistas ou utilizando sistemas próprios, como o da TOTVS.

#### **006 - Os cálculos de código de receita de contribuição previdenciária e imposto de renda dos processos serão calculados pelo eSocial?**

Cabe ao empregador declarar as bases e os valores específicos a recolher. Tanto o eSocial quanto o módulo de Gestão de Pessoas são passivos, apenas receberão os dados preenchidos pelo empregador.

Tanto no evento S-2500 quanto no S-2501 valores originários de cada competência, a própria empresa deverá solicitar ao calculista que sinalize os valores originais e os valores corrigidos (atualizações, juros) evitando o transporte de valores corrigidos, impedindo a incidência de atualizações.  

#### **007 - Quais são os prazos de envio?**

S-2500: até o dia 15 (quinze) do mês subsequente à data: a) do trânsito em julgado da decisão líquida proferida no processo trabalhista; b) da homologação de acordo judicial; c) do trânsito em julgado da decisão homologatória dos cálculos de liquidação da sentença; d) da celebração do acordo celebrado perante CCP ou Ninter; ou e) da determinação judicial para cumprimento antecipado da decisão, ainda que parcial.

 S-2501: até o dia 15 (quinze) do mês subsequente ao do pagamento referido na decisão/acordo proferida no processo trabalhista ou no acordo celebrado perante a CCP ou Ninter. 

Mas esses prazos podem ser antecipados para fins de cumprimento de obrigações decorrentes da decisão judicial.

#### **008 - Para envio dos processos trabalhistas é necessário que a folha de pagamento esteja aberta?**

Não é necessário visto que eles são tratados de forma isolada dos demais eventos do eSocial. 

#### **009 - Estes eventos impactam a folha de pagamento?**

Os eventos S-2500 e S-2501 não impactam na folha,  exceto em situações excepcionais, por exemplo, em reintegrações, onde faço o envio do S-2500 e o funcionário em algum momento retorna para a folha da empresa.  

#### **010 - Há penalidades para as empresas que não cumprirem com as obrigações?**

Sim, há penalidades no âmbito trabalhista e tributário. Para maiores informações sugerimos que avaliem os cenários em questão junto a equipe jurídica da empresa. 

#### **011 - Qualquer tipo de processo poderá ser enviado ao eSocial?**

Não, pois apenas os processos cujas ações foram julgadas da justiça do trabalho deverão ser declarados ao eSocial por meio do evento S-2500. Processos julgados na justiça comum ou federal não deverão ser enviados através deste evento. 

#### **012 - Posso enviar eventos de trânsito sem valores ainda definidos ou que ainda estão em andamento e foram iniciados antes da data de obrigatoriedade (01/10/2023)?**

Não será possível, pois o eSocial prevê que devem ser enviados processos trabalhistas cujas decisões sejam líquidas, ou seja, aqueles já possuem valores de pagamento definidos. Ele deverá ser informado ao eSocial somente quando a decisão possui valores líquidos (homologação dos cálculos). 

O envio será enviado desde que o trânsito julgado seja com data igual ou posterior à entrada em produção. Neste caso as datas de pagamento são indiferentes. 

A data que será considerada será a data do acordo, sentença, homologação ou trânsito julgado. Dito isto, se o mesmo for julgado após esta data de início 01/10, será necessário encaminhar o evento sim conforme Manual de Orientação do eSocial:

Devem ser prestadas nesse evento, independentemente do período abrangido pelas decisões/acordos, as informações relativas a: a) processos trabalhistas cujas decisões transitaram em julgado do dia 1º de outubro de 2023 em diante; b) acordos judiciais homologados a partir desta mesma data; c) processos com trânsito em julgado da decisão homologatória dos cálculos de liquidação a partir dessa mesma data, mesmo que o trânsito em julgado da sentença condenatória tenha ocorrido em data anterior; d) acordos no âmbito de CCP ou Ninter celebrados também dessa data em diante; ou e) determinações judiciais para cumprimento antecipado de decisão, ainda que parcial, proferidas a partir dessa mesma data

#### **013 - A partir de qual versão do RM será possível enviar os eventos para o eSocial?**

A rotina está liberada a partir das versões 12.1.34.263, 12.1.2205.211, 12.1.2209.155 e superiores. Mas ressaltamos a importância de manter o ambiente atualizado com os pacotes mais recentes da release para garantir que ajustes já realizados sejam aplicados.

#### **014 - Para cadastro e envio do S-2501 é necessário já ter enviado um S-2500?**

Sim, para envio dos tributos é necessário já haver no eSocial os dados de qual processo trabalhista este S-2501 corresponde. Todo tributo será decorrente de um processo trabalhista. 

#### **015 - Quando se tratar de citação para pagamento de condenação em 48 horas que tenha verba do INSS, o prazo não será observado pois preciso enviar as informações para que seja possível emitir a guia de INSS?**

No Manual de Orientações do eSocial (MOS), referente ao prazo de envio, consta a seguinte observação: "Esse prazo pode ser antecipado para fins de cumprimento de obrigações decorrentes da decisão judicial". Ou seja, no caso de pagamento de condenação em 48h será necessário antecipar o envio. 

Para mais detalhes acesse: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-07-2023.pdf> 

#### **016 - É necessário inserir informações quando os cálculos forem homologados e novamente quando houver a condenação no processo?**

O envio dos eventos de processo trabalhista do eSocial só são realizados após passadas todas as fases, até a execução do trânsito em julgado e cobrança dos valores definidos pelo Juiz do Direito do Trabalho. 

Para mais detalhes acesse: [https://espacolegislacao.totvs.com/esocial-processo-trabalhista**/**](https://espacolegislacao.totvs.com/esocial-processo-trabalhista/)

#### **017 - Referente as atualizações de patch que ocorrerão em 01/11/2023 e 20/11/2023 com liberação do layout S-1.2, no caso de possuirmos processos trabalhistas já no mês de obrigatoriedade (outubro/2023), podemos encaminhá-los ao eSocial normalmente?**

Processos que foram a julgamento e concluídos antes da data de início do período de convivência, deverão ser encaminhados no leiaute S-1.1, o leiaute atual do RM. Após esta data 20/11 será possível encaminhar os eventos no leiaute S-1.1 ou S-1.2, não sendo obrigatório ainda o envio do evento no leiaute atualizado, até o dia 21/01/2024.

No caso do evento S-2501 este deverá ser enviado exclusivamente no layout S-1.2 a partir de 01/2024.

#### **018 - Para processos trabalhistas onde não há recolhimento de INSS e FGTS, apenas pagamento de dano moral e cálculo de juros e honorários é aplicável a geração do evento S 2500?**

Conforme o MOS o evento S-2500 deve ser enviado mesmo quando não houver Contribuição Previdenciária, FGTS ou Imposto de Renda a recolher. 

Para mais detalhes acesse: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-07-2023.pdf> 

#### **019 - No campo período, o que devo informar como competência inicial e final? Este período compreende todo o tempo laboral do colaborador na empresa, sendo necessário discriminar mês a mês?**

Nesses campos deverão ser informadas a competência inicial e final a que se refere o processo ou conciliação, o usuário deverá informar, respectivamente, os meses inicial e final abrangidos pelo pedido no processo trabalhista, mesmo que não haja valores devidos em todos eles. Dessa forma deverão incluir mês a mês os valores das bases de cálculo.

Para mais detalhes acesse: <https://tdn.totvs.com/display/LRM/S-2500+-+Mapeamento+de+Dados> 

#### **020 - Quando na sentença, houver a correção de remuneração e/ou data de demissão (ou similar). Além do envio do S-2500, S-2501 terei que corrigir algum evento não periódico do trabalhador? (S-2200, S-2205, S-2206, S-2299)?**

No caso do colaborador possuir algum vínculo, será necessário encaminhar o S-2206 com a alteração. Segue informação citada no Manual de orientação: 1.6 D) Eventual informação de alteração contratual ocorrida durante o período do vínculo deve ser prestada por meio do envio do evento S-2206.

Para mais detalhes acesse: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-07-2023.pdf> 

#### **021 - Ao preencher os campos de cadastros dos Processos Trabalhistas, quando a opção de "Salvar" não estiver disponível, falta alguma habilitação para o usuário?**

O botão "Salvar" ficará desabilitado quando alguma informação obrigatória ainda não foi preenchida no cadastro. Fique atento se existe algum cadastro expansível obrigatório que não foi incluído.

Quando um campo for obrigatório ele não exibirá a palavra (opcional). Porém, pelo leiaute do eSocial alguns campos são definidos como opcionais, e passam a ser obrigatórios dependendo das informações digitadas em outros campos. Esta regra pode ser visualizada através da documentação técnica disponibilizada pelo eSocial.

#### **022 - Processos extrajudiciais também devem ser informados?**

Conforme o MOS deverão enviar o evento S-2500 quando o declarante que em processos trabalhistas ou em demandas submetidas à CCP ou Ninter for obrigado a reconhecer ou alterar informações relativas a vínculo trabalhista, pagar verbas de natureza remuneratória ou indenizatória ou recolher FGTS, contribuição previdenciária ou Imposto de Renda correspondentes.

#### **023 - Ao cadastrar o S-2500 é possível que através do campo contrato de trabalho o sistema faça o preenchimento automático do cadastro do trabalhador já realizado na Folha de Pagamento?**

O cadastro em questão não possui integração com a Folha de Pagamento, SST e Financeiro, dessa forma será necessário preenchimento manual dos dados do Contrato de Trabalho. 

Contudo, você poderá incluir uma sugestão em nossa Central Colaborativa. Tal sugestão será avaliada pelo time de desenvolvimento do produto e, se aprovada, será incluída em Road Map para implementações futuras. 

Central Colaborativa: <https://centraldeatendimento.totvs.com/hc/pt-br/community/topics> 

Road Map - TOTVS RH - Linha RM: <https://produtos.totvs.com/produto/totvs-rh/totvs-rh-linha-rm/> 

#### **024 - Ao efetuar a exclusão do Processo Trabalhista e evento S-2500 correspondente, caso exista necessidade de retransmissão será possível aproveitar o cadastro do processo excluído?**

Uma vez excluído não será possível aproveitar os dados para um novo cadastro. Contudo, você poderá incluir uma sugestão em nossa Central Colaborativa. Tal sugestão será avaliada pelo time de desenvolvimento do produto e, se aprovada, será incluída em Road Map para implementações futuras. 

Central Colaborativa: <https://centraldeatendimento.totvs.com/hc/pt-br/community/topics> 

Road Map - TOTVS RH - Linha RM: <https://produtos.totvs.com/produto/totvs-rh/totvs-rh-linha-rm/> 

#### **025 - Na inserção de um processo trabalhista ao incluir o contrato de trabalho, no campo Tipo devemos informar o Tipo de contrato original em que o funcionário foi contratado ou a forma como a determinação judicial reconheceu na decisão final?**

Segundo o leiaute do eSocial, no campo "Tipo de contrato" deverá ser informado o tipo de contrato a que se refere o processo judicial ou a demanda submetida à CCP ou ao NINTER. 

"No campo {tpContr} do grupo [infoContr] deve ser declarada a condição do processo judicial ou da demanda submetida à CCP ou ao Ninter, considerando a situação do vínculo antes e após o processo trabalhista: ..."

Para mais detalhes acesse: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-07-2023.pdf/> 

#### **026 - As inclusões dos dados para geração do S-2500 e S-2501 servirão como guia para pagamentos?**

O retorno com sucesso do evento S-2501 importa o envio dos créditos tributários apurados para o Portal da DCTFWeb no ambiente da RFB. 

Para mais detalhes acesse: <https://espacolegislacao.totvs.com/esocial-processo-trabalhista/> 

#### **027 - Ao finalizar o cadastro do S-2500 e/ou S-2501 o sistema gerará gatilho dos eventos em questão?**

Sim, após o cadastro o sistema irá disparar de forma automática os eventos S-2500 e S-2501 a medida que forem incluídos. Assim como ocorre com os demais eventos de Folha de Pagamento, como, S-2200 e os eventos de SST, estes terão ser gatilhos gerados na Fila de Eventos do eSocial no módulo de Folha de Pagamento, onde poderão gerar os XMLs, consultas inconsistências durante as gerações e também realizar as transmissões. 

#### **028 - A funcionalidade de processos trabalhistas é um módulo à parte no RM?**

Apesar do cadastro em questão ser totalmente desvinculado do produto, ou seja, não serão exibidas informações cadastradas no sistema, o mesmo está disponível no módulo de Gestão de Pessoas da linha RM.

Da mesma forma foi disponibilizado no TAF o cadastro desses eventos também, disponível para clientes TAF FULL.

#### **029 - A guia DCTFWeb deverá ser emitida para fins de recolhimento previdenciário ou o pagamento poderá ser feito integralmente via guia judicial no processo?**

Os dados referentes a recolhimentos serão enviados através do evento S-2501. O retorno com sucesso deste evento importa o envio dos créditos tributários apurados para o Portal da DCTFWeb no ambiente da RFB. 

Para mais detalhes acesse: <https://espacolegislacao.totvs.com/esocial-processo-trabalhista/>

#### **030 - Em caso de processos com sentença ou acordo que possuem mais de uma parcela para pagamento, o evento S-2500 deverá ser cadastrado uma única vez ou mensalmente de acordo com a quantidade de parcelas? Já o S-2501 deverá ser mensalmente se houver contribuições relativas às parcelas?**

O processo trabalhista seria cadastrado novamente somente em casos de haver mais de um processo em julgamento. No caso do pagamento para casos onde este será parcelado, deverão enviar um S-2501 correspondente a cada parcela conforme o mês correspondente a cada pagamento.

Dados referentes a informações de Remuneração e Periodicidade de pagamento (remuneracao) deverão ser preenchidos?

As informações em questão deverão obrigatoriamente serem preenchidas quando Tipo de contrato a que se refere o processo judicial ou a demanda submetida à CCP ou ao NINTER (tpContr) for diferente de 6 - Trabalhador sem vínculo de emprego/estatutário (TSVE), sem reconhecimento de vínculo empregatício e Tipo de regime trabalhista (tp RegTrab) for igual a 1 - CLT - Consolidação das Leis de Trabalho e legislações trabalhistas específicas ou se a Categoria do trabalhador for igual a 721, 722 ou 771.

Para mais detalhes acesse: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1.1-nt-01-2023/index.html#evtProcTrab>

#### **031 - As informações de Dependentes (dependente) deverão obrigatoriamente serem enviadas quando existir um contrato onde o campo Indicativo se o contrato possui informação no evento S-2190, S-2200 ou S-2300 no declarante (indContr) for igual a Não (N).**

Para mais detalhes acesse: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1.1-nt-01-2023/index.html#evtProcTrab>

#### **032 - Referente a casos de pagamento por precatórios, como proceder nestes casos?**

Caso refira-se a requisição de pagamento de quantias ao ente público (União, Estado, município, suas autarquias ou fundações), em virtude de decisão judicial definitiva e condenatória, que possibilita à pessoa vitoriosa receber o crédito da condenação, subentende-se que os evento S-2500 e S-2501 não contemplam tais pagamentos, visto que nestes eventos não devem ser utilizado para prestação de informação relativa a processos de trabalhadores vinculados ao RGPS ou ao RPPS, que sejam da competência da Justiça Comum ou Justiça Federal. As informações relativas a esses processos devem ser prestadas mediante o envio/retificação dos eventos não periódicos e periódicos do eSocial.

Para mais detalhes acesse: <https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-1-consolidada-ate-a-no-s-1-1-07-2023.pdf/>
