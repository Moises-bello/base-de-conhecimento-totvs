---
content_hash: 7530cc88648c566a321e6ea836a7f00a5ced9740f3606908e8a91bec015da6af
fetched_at: '2026-06-29T00:08:57.083956+00:00'
page_id: '353272952'
product: rm
source: tdn-rm
title: Controle de Tributos e Despesas de consumo
type: documentation
url: https://tdn.totvs.com/display/LRM/Controle+de+Tributos+e+Despesas+de+consumo
version: 7
---

# **Objetivo**

O objetivo deste recurso é administrar todas as despesas de um imóvel ou subunidade, sejam elas taxas, tarifas, tributos, despesas de consumo ou manutenção, condomínio, etc. As despesas em sua maioria são recorrentes, mensalmente ou anualmente, tendo variação de valores, mas também serão tratadas despesas esporádicas.

O recurso deve permitir identificar despesa, Gerar a Cobrança no Backoffice, ou seja, gerar movimento a pagar (ex: Pedido de Compra)  centralizando assim a digitação, já que o volume é um dos fatores críticos desta rotina, além de gerar o repasse destes pagamentos aos inquilinos, para as despesas que forem reembolsáveis. É importante que no reembolso o sistema tenha a inteligencia de gerar mes a mes este repasse verificando quais imóveis estão locados e se necessário faça o rateio daqueles que tiverem locação fracionada. Assim o usuário não terá que fazer controles a parte (planilhas excel) para saber se o imóvel está vago ou  não e se pode ou não repassar a despesa.

Este recurso posteriormente será utilizado nos módulos de Venda e Condomínio, portanto sua nomenclatura deve ter características genéricas.

# **Menu de Acesso**

No módulo de aluguel o recurso terá as seguintes opções de acesso:

* No menu Geral: onde serão apresentados todas as despesas;
* Anexo ao Imóvel: onde serão apresentados todas as despesas.

## Regra de Negócios

O controle de despesas terá as seguintes informações:

Capa da Despesa

* Tipo: (Tabela)
  + Código
  + Descrição: (IPTU / foro / taxa de lixo)
  + Tributo: campo que informa sim ou não, haverá tratamento especifico. Taxa de Incêndio, taxa de lixo, foro, ITR não permitem parcelamento. Uma vez marcada esta opção o sistema não deve deixar informar a quantidade de cotas diferente de 1. *(gerar cotas conforme número de inscrições municipais)*
  + Natureza Orçamentária Financeira
  + Parâmetro para gerar Movimento (Pedido de Compra)
* Gerar Cota para cada inscrição municipal.(s/n)
* Freqüência : Anual, Mensal e Único
* Entidade: Órgão  ou empresa responsável pela cobrança;
* Imóvel (1 ou vários): Um imóvel poderá ter um ou vários índices cadastrais, que é o caso de Edifícios Garagem, onde cada vaga tem um IPTU distinto, podendo totalizar volumes como 600 vagas, com o mesmo número de guias para pagamento. Como o cadastro é aberto, eventualmente podem ser cadastrados vários imóveis mas tendo apenas um registro municipal e e um único IPTU ou vice versa;  
    
  **Anexo****Competência**  
  Como a mesma despesa pode ser recorrente ano após ano será gerado um controle das cobranças com os seguintes dados:
* A competência: mês / Ano;
* Exercício: Ano;
* Status ou situação: em preparação, integrado;
* Nº de controle: este número pode ser o número do documento ou da inscrição;
* Área do terreno: dado informado quando se tratar do tipo Tributo. Avaliar Default como competência anterior, ou dado do empreendimento. Como este dado pode sofrer alteração por aquisição ou venda parcial a informação será por competência. **(Monica passou para o cadastro do Imóvel)**
* Área Construída: dado informado quando se tratar do tipo Tributo. Avaliar Default como competência anterior, ou dado do empreendimento. Como este dado pode sofrer alteração por novas construções ou ampliação a informação será por competência.(**Monica passou para o cadastro do Imóvel)**
* Data do vencimento: informado pelo usuário;
* **Valor Venal:** valor venal avaliado pelo órgão. Campo aplicado quando o Tipo for Tributo. (ex: IPTU) este valor tb pode ser informado no cadastro do imóvel;
* **Valor Total da Cota**: valor total de despesa, taxa ou do tributo;
* Valor com Desconto para Cota Única: corresponde ao valor para pagamento a vista;
* Número de Cotas de Cobrança;
* Valor das Cotas: campo calculado pela fórmula (valor Total da cota/ Número de Cotas) se o Número de Cotas for 1, considerar Valor com Desconto para Cota Única;
* Atualiza Valor Venal do Imóvel (sim ou não): este campo será utilizado pelo processo de atualização de valor
* Reembolso: locador ou locatário ou Nenhum. Permitir indicar a ordem de prioridade.
  + locatário: se o imóvel estiver locado o sistema deve gerar o repasse da cobrança contra o locatário, conforme vigência do contrato de locação, e proporção por metro quadrado locado.
  + Locador: se o imóvel for de terceiro o sistema deve gerar o repasse da cobrança contra o locador, mesmo que o imóvel não esteja locado e não esteja gerando cobranças. Não deve ser verificada a vigência do contrato de administração. Esta opção só deve ser disponibilizada se o imóvel não for próprio.
  + Nenhum: neste caso não há repasse da cobrança.
* Número de Cotas de Repasse: o repasse pode ser feito pelo mesmo número de cotas da cobrança ou por uma quantidade definida, ou seja, a administradora do imóvel pode pagar o IPTU a vista mas repassar em 8 cotas.
* Vencimento
* Permitir associar documento digitalizado e levá-lo (a referencia fluig) até o movimento do backoffice.
* Anexo a este registro devem constar todas as cotas geradas controlando o status se já foi integrado para o backoffice ou não.  
    
  *Exemplo de tela com capa e competência.*  
    
    
    
  **Processos**

* **Gerar Cotas de cobrança**  
  O processo de Gerar Cotas verifica o número de cotas definidas por competência e se deve *"Gerar Cota para cada inscrição municipal"*desta forma se um imóvel tiver 600 inscrições serão gerados 600 movimentos, em caso de pagamento a vista, ou se parcelado deve multiplicar o número de cotas de  cobrança pelo número de inscrições municipais. Este é um processo que visa facilitar principalmente a cobrança de IPTU mas servirá para qualquer outra despesa. Se não estiver marcada a opção *"Gerar Cota para cada inscrição municipal"* o sistema deve gerar apenas o número de cotas da Cobrança.  
  **Unificou com a regra de cobrança.**
* **Gerar Cobrança**  
  Este processo integra  o numero de  movimentos definido para a competência conforme quantidade de cotas de cobrança.  
  Este é um processo é dependente do processo anterior e da indicação dos dados de competência.

* **Gerar Repasse ou Reembolso**  
  Este processo deve ser gerado periodicamente permitindo agendamento e provisão. Executando todos os meses o sistema poderá identificar os imóveis locados e suas frações se locado por metro quadrado, bem como vigência dos contratos.  
  Não podem ser cobradas cotas para contratos de locação encerrados ou rescindidos.  
  Não podem ser cobradas cotas para contratos de locação que ainda não teve inicio.   
  Para imóveis controlados por área seu valor deve ser rateado proporcionalizando vigência e área.
* **Atualizar Valores do Imóvel**  
  Este processo deve atualizar os valores Venal e de IPTU no cadastro do Imóvel conforme valor indicado na competência.
* **Copiar Despesa**  
  Este processo permitirá que uma despesa gere uma cópia na mesma coligada ou em outra para otimizar o cadastro de despesas semelhantes, ou para atender a casos onde um imóvel foi vendido de uma coligada para outra.

**Considerações Gerais**

* Quando um imóvel for inativado a despesa também deve ser inativada.
* Quando um contrato de locação for encerrado ou rescindido e seu repasse for para o locatário, os lançamentos financeiros futuros devem ser atualizados retirando a cobrança. Não deve ser desfeito o movimento de cobrança da despesa pois este independe da locação do imóvel.
* Se um locatário pagou uma despesa a vista mas rescindiu o contrato de locação. A diferença da despesa deve ser devolvida.
* Anexo ao cadastro das despesas devem ser apresentadas todas as Cobranças Geradas (movimentos) bem como todos os repasses gerados.
* Vários que estejam associados a um único contrato podem gerar um reembolso agrupado.
* O sistema deve permitir alterar o vencimento e o valor das cotas, pois ocorre por exemplo a emissão do IPTU por atraso da prefeitura, assim vários meses serão cobrados na primeira parcela.
* Permitir Alterar valor e vencimento das cotas em Lote. ex: tem 600 inscrições municipais iguais para vagas de garagem e precisa alterar o vencimento ou mesmo o valor de cada IPTU na competência,
* Criar objeto gerencial que lista a situação das despesas permitindo filtro por um ou mais tributos, situação e multi coligadas. O layout do objeto será definido em tempo de projeto. Preferencialmente CUBO.

**Ilustração da Estrutura**

## Fluxo de Processo Macro
