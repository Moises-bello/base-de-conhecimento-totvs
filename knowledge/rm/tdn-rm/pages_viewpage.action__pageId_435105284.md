---
content_hash: a832423f466604de5469d81ceb8207d62fcead27aab2377b280b2fb7ddbd9606
fetched_at: '2026-06-29T00:09:49.392992+00:00'
page_id: '435105284'
product: rm
source: tdn-rm
title: Eventos Contábeis - TOTVS Incorporação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105284
version: 23
---

**Eventos Contábeis**

---

Para a agilidade no processo de contabilização, pode ser cadastrado um evento contábil no menu Cadastro | Contabilidade | Eventos Contábeis, onde será informado as contas de débito e crédito com o valor de incidência referente ao que será contabilizado.

Evento Contábil

O parâmetro, Agrupa Partida Contábil, da tela de Evento Contábil somente será agrupado se o valor de incidência for o mesmo .

Por exemplo:

Vai agrupar:  Conta 001.001 - Valor Venda R$100,00 e  Conta 001.001 - Valor Venda R$150,00 => Agrupado  Conta 001.001 - Valor Venda R$250,00

Não vai agrupar:  Conta 001.001 - Valor Venda R$100,00 e  Conta 001.001 - Valor Juros Ambos R$300,00 => Não Agrupa.

Na Gestão Imobiliária a contabilização poderá incidir sobre os seguintes valores:

* Valor Contrato - Valor Juros Contrato Vincendo - Valor Juros Contrato Vencido - Valor Juros Contrato Ambos - Valor Monetário Vincendo - Valor Monetário Vencido - Valor Monetário Ambos - Valor Distrato - Valor Entrega Chave - Valor Seguro por Empreendimento - Valor Aditivo - Valor Receita 963 - Valor Receita Financeira 963 - Valor Adiantamento Cliente 963 - Valor Adiantamento Financeiro Cliente 963 - Valor Saldo Devedor - Valor Monetário do Principal - Valor de Juros Vincendos Antes da Entrega - Valor de Juros Vencidos Antes da Entrega - Valor de Juros Vincendos e Vencidos Antes da Entrega - Valor de Juros Vincendos Após a Entrega - Valor de Juros Vencidos Após a Entrega - Valor de Juros Vincendos e Vencidos Após a Entrega - Valor Monetário Vincendos Antes da Entrega - Valor Monetário Vencidos Antes da Entrega - Valor Monetário Vincendos e Vencidos Antes da Entrega - Valor Monetário Vincendos Após a Entrega - Valor Monetário Vencidos Após a Entrega - Valor Monetário Vincendos e Vencidos Após a Entrega  
  Estes valores de incidência podem ser utilizados tanto na contabilização da venda, de aditivos, de reajuste, de distrato, da apuração do POC. A contabilização também pode ser através de fórmulas e sentenças SQL, onde pode-se contabilizar qualquer campo do sistema. No cadastro do evento contábil será definida a utilização de fórmula ou percentual. E ao efetuar uma contabilização, a mesma calculará o valor contábil através da parametrização definida.  
     
  **Tipos de contabilizações do TIN**  
  **Contabilização da Venda:** A contabilização da venda ocorre quando é informado um evento contábil na pasta Contabilidade localizada na edição da Venda, e no momento da efetivação, o usuário poderá observar os lançamentos de débito e crédito que serão criados no lote da Gestão Contábil chamado "Contabilização da Inclusão da Venda".  
  **Observação:** Caso o usuário não queira contabilizar a Efetivação do contrato, basta clicar no botão de Cancelar da janela de Lançamentos Contábeis. Em seguida será mostrada uma tela possibilitando a efetivação do contrato.  
     
  **Contabilização do Distrato:** A contabilização do Distrato ocorre no momento da realização deste processo quando o Distrato é efetivado, desde que este já tenha cadastrado um evento contábil com o valor de incidência no Distrato. Será incluído um lote na Gestão Contábil com nome "Contabilização do Distrato da Venda".  
     
  **Contabilização do Aditivo:** A contabilização do Aditivo ocorre no momento da realização deste processo quando o Aditivo está sendo realizado, desde que este já tenha cadastrado um evento contábil com o valor de incidência no Aditivo. Neste processo é possível contabilizar o Aditivo pela Diferença entre saldo devedor negociado selecionado ou pelo Saldo devedor negociado. Será incluído um lote na Gestão Contábil com nome "Contabilização do Aditivo da Venda". É possível também contabilizar o aditivo de troca de subunidade (ou troca de Apto). O valor incidente é do valor do contrato.   
  **Observação:** Utilizamos itens de evento contábil do tipo Crédito e/ou Débito. Para atender as contabilizações do aditivo de troca de subunidade foram criadas duas tabelas default para que possam ser buscados os valores de contabilização de débito e crédito. Da mesma forma, essas tabelas default podem ser utilizadas nos itens gerenciais do evento contábil. São eles:

* **Subunidade Anterior:** Busca os valores incidentes da subunidade que estava relacionada à venda antes da efetivação do aditivo de troca de subunidade. Geralmente utilizada no item de débito do evento contábil.
* **Subunidade:** Refere-se a subunidade atual, que é associada à venda após a efetivação do aditivo. Geralmente utilizada no item de crédito.

**Contabilização do Reajuste:** A contabilização do Reajuste ocorre automaticamente quando é realizado o reajuste das parcelas, desde que esta venda a ser reajustada, já tenha cadastrado um evento contábil com o valor de incidência no reajuste. Será incluído um lote na Gestão Contábil com nome "Contabilização do Reajuste de Juros da Venda e/ou Contabilização do Reajuste Monetário da Venda". Na aba contabilidade da venda é possível associar dois eventos contábeis de reajuste, sendo um reajuste inflacionário (Para quando o valor de Juros e CM é positivo) e deflacionário (Quando há um reajuste em que o valor foi negativo).  
**Observação:** Os valores de reajuste calculados por parcelas serão somados em um único lançamento na Gestão Contábil para cada mês.  
Para que o histórico do reajuste seja gravado pelo sistema, o parâmetro "Desabilita Histórico Mensal" deve estar desabilitado. O parâmetro encontra-se em: **Ambiente| Parâmetros| 22.02 – Contrato| 22.02.07 – Reajuste Monetário| Parâmetros do Reajuste**.  
   
**Contabilização na Entrega das Chaves:** A contabilização da Entrega das Chaves só ocorre quando a venda já esteja efetivada e é solicitado a inclusão de Lote na Gestão Contábil, desde que esta venda já tenha cadastrado um evento contábil com o valor de incidência na Entrega das Chaves. Será incluído um lote na Gestão Contábil com nome "Contabilização da Entrega da Chave da Venda".  
   
**Contabilização do Seguro por Empreendimento:** A contabilização do Seguro por Empreendimento ocorre no momento da geração do Seguro por Empreendimento (Processo: ). Ao executar o processo é solicitado a inclusão de Lote na Gestão Contábil, desde que esta venda já tenha cadastrado um evento contábil na aba Seguro por Empreendimento. Será incluído um lote na Gestão Contábil com nome "Contabilização da Inclusão Seguro Prestamista".  
   
**Contabilização em Dot Net:** Nos processos de Efetivação, Aditivo e Distrato em Dot Net, o evento e os dados de lançamentos criados poderão ser alterados.  
**Data da contabilização:** Data que será feita a contabilização dos lançamentos contábeis para os seus respectivos lotes na Gestão Contábil.  
**Observação:** A data da contabilização deve respeitar o período contábil informado nos parâmetros da Gestão Contábil.  
   
**Evento contábil:** Campo utilizado para informar o evento que será utilizado no processo.  
**Carregar evento contábil:** Este botão deve ser utilizado, caso o usuário troque o evento contábil informado.  
**Pastas de Crédito e Débito:** Possui os botões de controle, utilizados para adicionar, editar, excluir e informar os rateios de contas gerenciais.  
   
**Contabilização do módulo de aluguel**  
Os eventos contábeis serão definidos com as seguintes opões:

* **Processo:** definição de qual processo o evento contábil será utilizado no Contratos de locação.
* **Buscar filial e departamento:** Serão buscadas as informações de Filial e Departamento a serem usados na contabilização nos seguintes pontos:
  + **Contrato de Locação:** busca a filial e o departamento do parâmetro de integração financeira associado ao contrato de locação que está sendo contabilizado.
  + **Default Contábil:** busca a filial e o departamento do default contábil da partida que está sendo processada
  + **Evento Contábil:** busca a filial e o departamento do evento contábil que está sendo processado.
* **Buscar Centro de custo:** Serão buscadas as informações de Centro de custo a serem usados na contabilização nos seguintes pontos:
  + **Contrato de Locação:** busca o centro de custo do parâmetro de integração financeira associado ao contrato de locação que está sendo contabilizado.
  + **Default Contábil:** busca o centro de custo do default contábil da partida que está sendo processada
  + **Evento Contábil:** busca o centro de custo do evento contábil que está sendo processado.
  + **Rateio:** busca o centro de custo conforme rateio de centros de custos informado no contrato de locação. Neste caso, deverá respeitar os percentuais de rateio, pois pode haver mais de um centro de custo definido no rateio.
* **Itens do evento:**
  + **Aplicar:** Define a "condição" em que os itens do evento serão considerados. As opções serão definidas conforme contexto:
    - Contrato de Locação (será aplicado também para os escalonamentos)
    - Item do contrato de locação
    - Lançamento Financeiro: esta opção não será apresentada para linearização
    - Rateio de Centro de Custo
    - Evento Financeiro
    - Rescisão
  + **Buscar Default (Conta contábil):** Define os cadastros que deverão conter a indicação da conta a ser utilizada. Esta definição irá ser variável, de acordo com a opção selecionada para o campo **"Aplicar"**.
  + **Valor:** Os valores possibilitam a correta contabilização e os devidos ajustes desejados. Tais opções estarão disponíveis na tela de cadastro do evento, mas também foram inseridas funções de fórmula que retornam os mesmos valores, possibilitando a flexibilidade dos cálculos utilizando fórmulas.
    - Os valores e funções de fórmula devem ser únicos e serem capazes de identificar qual o tratamento deve ser realizado, se usa linearização ou não.

* **Integração Protheus:**
  + **Buscar Item Contábil e Classe de Valor em:**Definição de onde será buscado o item contábil e/ou classe de valor que será utilizado na integração da contabilização com o Protheus.
    - Cliente\Fornecedor
    - Empreendimento

 A aba 'Integração Protheus' será apresentada no cadastro do evento contábil somente em bases que possuem a integração com Protheus EAI 2.0 ativa.

Principal1Processo: Aluguel – Contrato de locação

| **Aplicar** | **Valores Default** | **Origem/Cálculo** |
| --- | --- | --- |
| Contrato de locação | Receita linear | RL = (∑periodo (VO\* ia) ) /iT |
| Contrato de locação | Desconto linear | DL= (∑periodo (VO\* D)\* ia) /iT |
| Contrato de locação | Receita Liquida | Rec = ((VO+VR)\*(- D))+VO+VR |
| Contrato de locação | Provisão de Receita Linear | PRL=( Rec -(-DL) |
| Contrato de locação | Provisão de Linearização | PL= (RL+ (-DL) ) –Rec |
| Contrato de locação | Valor Total do Contrato | Campo do Contrato de Locação |
| Contrato de locação | Valor Final do Contrato | Campo do Contrato de Locação |
| Contrato de locação | Valor de Desconto | Campo do Contrato de Locação |
| Contrato de locação | Valor Final Anterior | Campo do Contrato de Locação |
| Contrato de locação | Valor de Resíduo | Campo do Contrato de Locação |
| Contrato de locação | Valor da Taxa de Administração | Campo do Contrato de Locação |
| Contrato de locação | Valor da Taxa de Intermediação | Campo do Contrato de Locação |

2Processo: Aluguel – Contrato de locação

| **Aplicar** | **Valores Default** | **Origem/Cálculo** |
| --- | --- | --- |
| Contrato de locação | Receita linear | RL = (∑periodo (VO\* ia) ) /iT |
| Contrato de locação | Desconto linear | DL= (∑periodo (VO\* D)\* ia) /iT |
| Contrato de locação | Receita Liquida | Rec = ((VO+VR)\*(- D))+VO+VR |
| Contrato de locação | Provisão de Receita Linear | PRL=( Rec -(-DL) |
| Contrato de locação | Provisão de Linearização | PL= (RL+ (-DL) ) –Rec |
| Contrato de locação | Valor Total do Contrato | Campo do Contrato de Locação |
| Contrato de locação | Valor Final do Contrato | Campo do Contrato de Locação |
| Contrato de locação | Valor de Desconto | Campo do Contrato de Locação |
| Contrato de locação | Valor Final Anterior | Campo do Contrato de Locação |
| Contrato de locação | Valor de Resíduo | Campo do Contrato de Locação |
| Contrato de locação | Valor da Taxa de Administração | Campo do Contrato de Locação |
| Contrato de locação | Valor da Taxa de Intermediação | Campo do Contrato de Locação |

3Processo: Aluguel – Contrato de locação

|  |  |  |
| --- | --- | --- |
| **Aplicar** | **Valores default** | **Origem/Cálculo** |
| Item do contrato de locação | Valor do Item | Campo do Contrato de Locação |
| Item do contrato de locação | Valor anterior do item | Campo do Contrato de Locação |

4Processo: Aluguel – Contrato de locação

|  |  |  |
| --- | --- | --- |
| **Aplicar** | **Valores default** | **Origem/Cálculo** |
| Item do contrato de locação | Valor do Item | Campo do Contrato de Locação |
| Item do contrato de locação | Valor anterior do item | Campo do Contrato de Locação |

5Processo: Aluguel – Contrato de locação

|  |  |  |
| --- | --- | --- |
| **Aplicar** | **Valores default** | **Origem/Cálculo** |
| Rateio de centro de custo | Receita Linear | RL = (∑periodo (VO\* ia) ) /iT |
| Rateio de centro de custo | Desconto linear | DL= (∑periodo (VO\* D)\* ia) /iT |
| Rateio de centro de custo | Receita Liquida | Rec = ((VO+VR)\*(- D))+VO+VR |
| Rateio de centro de custo | Provisão de Receita Linear | PRL=( Rec -(-DL) |
| Rateio de centro de custo | Provisão de Linearização | PL= (RL+ (-DL) ) –Rec |
| Rateio de centro de custo | Valor Total do Contrato | Campo do Contrato de Locação |
| Rateio de centro de custo | Valor Final do Contrato | Campo do Contrato de Locação |
| Rateio de centro de custo | Valor de Desconto | Campo do Contrato de Locação |
| Rateio de centro de custo | Valor Final Anterior | Campo do Contrato de Locação |
| Rateio de centro de custo | Valor de Resíduo | Campo do Contrato de Locação |
| Rateio de centro de custo | Valor da Taxa de Administração | Campo do Contrato de Locação |
| Rateio de centro de custo | Valor da Taxa de Intermediação | Campo do Contrato de Locação |
| Rateio de centro de custo | Valor total do evento financeiro | Campo do Contrato de Locação |

6Processo: Aluguel - Rescisão

|  |  |  |
| --- | --- | --- |
| **Aplicar** | **Valores default** | **Origem/Cálculo** |
| Rescisão | Valor da rescisão | Campo da rescisão |
| Rescisão | Valor do desconto | Campo da rescisão |
| Rescisão | Valor Final da rescisão | Campo da rescisão |
| Evento financeiro | Valor Total do Evento | Campo do Evento Financeiro |

7Processo: Venda Imobiliária - Curto e Longo Prazo

Para contabilização de curto e longo prazo, além da opção de trabalhar com cálculo por percentual, foi criado a função de fórmula **GETVALORINCIDENCIACONTABILVENDA**para dar mais opções no cálculo da contabilização. A função recebe como parâmetro o valor de incidência, na tabela abaixo podemos encontrar todos os parâmetros que podem ser utilizados.

* **Exemplo da função de fórmula:**GETVALORINCIDENCIACONTABILVENDA('parametro')

|  |  |  |
| --- | --- | --- |
| **Evento Contábil** | | **Processo** |
| Valor Incidência (percentual) | Fórmula (parâmetro) |
| Valor Venda | ValorVenda |  |
| Valor Venda Curto Prazo | ValorVendaCurtoPrazo |  |
| Valor Venda Longo Prazo | ValorVendaLongoPrazo |  |
| Valor Agregado Venda | ValorAgregadoVenda |  |
| Valor Agregado Venda Curto Prazo | ValorAgregadoVendaCurtoPrazo |  |
| Valor Agregado Venda Longo Prazo | ValorAgregadoVendaLongoPrazo |  |
| Valor Juros Vincenda | ValorJurosVincenda |  |
| Valor Juros Vincenda Curto Prazo | ValorJurosVincendaCurtoPrazo |  |
| Valor Juros Vincenda Longo Prazo | ValorJurosVincendaLongoPrazo |  |
| Valor Juros Vencida | ValorJurosVencida |  |
| Valor Juros Vencida Curto Prazo | ValorJurosVencidaCurtoPrazo |  |
| Valor Juros Vencida Longo Prazo | ValorJurosVencidaLongoPrazo |  |
| Valor Juros Ambos | ValorJurosAmbos |  |
| Valor Juros Ambos Curto Prazo | ValorJurosAmbosCurtoPrazo |  |
| Valor Juros Ambos Longo Prazo | ValorJurosAmbosLongoPrazo |  |
| Valor Juros Contrato Vincendo Antes Entrega | ValorJurosContratoVincendoAntesEntrega |  |
| Valor Juros Contrato Vincendo Antes Entrega Curto Prazo | ValorJurosContratoVincendoAntesEntregaCurtoPrazo |  |
| Valor Juros Contrato Vincendo Antes Entrega Longo Prazo | ValorJurosContratoVincendoAntesEntregaLongoPrazo |  |
| Valor Juros Contrato Vencido Antes Entrega | ValorJurosContratoVencidoAntesEntrega |  |
| Valor Juros Contrato Vencido Antes Entrega Curto Prazo | ValorJurosContratoVencidoAntesEntregaCurtoPrazo |  |
| Valor Juros Contrato Vencido Antes Entrega Longo Prazo | ValorJurosContratoVencidoAntesEntregaLongoPrazo |  |
| Valor Juros Contrato Ambos Antes Entrega | ValorJurosContratoAmbosAntesEntrega |  |
| Valor Juros Contrato Ambos Antes Entrega Curto Prazo | ValorJurosContratoAmbosAntesEntregaCurtoPrazo |  |
| Valor Juros Contrato Ambos Antes Entrega Longo Prazo | ValorJurosContratoAmbosAntesEntregaLongoPrazo |  |
| Valor Juros Contrato Vincendo Apos Entrega | ValorJurosContratoVincendoAposEntrega |  |
| Valor Juros Contrato Vincendo Apos Entrega Curto Prazo | ValorJurosContratoVincendoAposEntregaCurtoPrazo |  |
| Valor Juros Contrato Vincendo Apos Entrega Longo Prazo | ValorJurosContratoVincendoAposEntregaLongoPrazo |  |
| Valor Juros Contrato Vencido Apos Entrega | ValorJurosContratoVencidoAposEntrega |  |
| Valor Juros Contrato Vencido Apos Entrega Curto Prazo | ValorJurosContratoVencidoAposEntregaCurtoPrazo |  |
| Valor Juros Contrato Vencido Apos Entrega Longo Prazo | ValorJurosContratoVencidoAposEntregaLongoPrazo |  |
| Valor Juros Contrato Ambos Apos Entrega | ValorJurosContratoAmbosAposEntrega |  |
| Valor Juros Contrato Ambos Apos Entrega Curto Prazo | ValorJurosContratoAmbosAposEntregaCurtoPrazo |  |
| Valor Juros Contrato Ambos Apos Entrega Longo Prazo | ValorJurosContratoAmbosAposEntregaLongoPrazo |  |
| Valor Monetaria Vincenda | ValorMonetariaVincenda |  |
| Valor Monetaria Vincenda Curto Prazo | ValorMonetariaVincendaCurtoPrazo |  |
| Valor Monetaria Vincenda Longo Prazo | ValorMonetariaVincendaLongoPrazo |  |
| Valor Monetaria Vencida | ValorMonetariaVencida |  |
| Valor Monetaria Vencida Curto Prazo | ValorMonetariaVencidaCurtoPrazo |  |
| Valor Monetaria Vencida Longo Prazo | ValorMonetariaVencidaLongoPrazo |  |
| Valor Monetaria Ambos | ValorMonetariaAmbos |  |
| Valor Monetaria Ambos Curto Prazo | ValorMonetariaAmbosCurtoPrazo |  |
| Valor Monetaria Ambos Longo Prazo | ValorMonetariaAmbosLongoPrazo |  |
| Valor Monetario Vincendo Antes Entrega | ValorMonetarioVincendoAntesEntrega |  |
| Valor Monetario Vincendo Antes Entrega Curto Prazo | ValorMonetarioVincendoAntesEntregaCurtoPrazo |  |
| Valor Monetario Vincendo Antes Entrega Longo Prazo | ValorMonetarioVincendoAntesEntregaLongoPrazo |  |
| Valor Monetario Vencido Antes Entrega | ValorMonetarioVencidoAntesEntrega |  |
| Valor Monetario Vencido Antes Entrega Curto Prazo | ValorMonetarioVencidoAntesEntregaCurtoPrazo |  |
| Valor Monetario Vencido Antes Entrega Longo Prazo | ValorMonetarioVencidoAntesEntregaLongoPrazo |  |
| Valor Monetario Ambos Antes Entrega | ValorMonetarioAmbosAntesEntrega |  |
| Valor Monetario Ambos Antes Entrega Curto Prazo | ValorMonetarioAmbosAntesEntregaCurtoPrazo |  |
| Valor Monetario Ambos Antes Entrega Longo Prazo | ValorMonetarioAmbosAntesEntregaLongoPrazo |  |
| Valor Monetario Vincendo Apos Entrega | ValorMonetarioVincendoAposEntrega |  |
| Valor Monetario Vincendo Apos Entrega Curto Prazo | ValorMonetarioVincendoAposEntregaCurtoPrazo |  |
| Valor Monetario Vincendo Apos Entrega Longo Prazo | ValorMonetarioVincendoAposEntregaLongoPrazo |  |
| Valor Monetario Vencido Apos Entrega | ValorMonetarioVencidoAposEntrega |  |
| Valor Monetario Vencido Apos Entrega Curto Prazo | ValorMonetarioVencidoAposEntregaCurtoPrazo |  |
| Valor Monetario Vencido Apos Entrega Longo Prazo | ValorMonetarioVencidoAposEntregaLongoPrazo |  |
| Valor Monetario Ambos Apos Entrega | ValorMonetarioAmbosAposEntrega |  |
| Valor Monetario Ambos Apos Entrega Curto Prazo | ValorMonetarioAmbosAposEntregaCurtoPrazo |  |
| Valor Monetario Ambos Apos Entrega Longo Prazo | ValorMonetarioAmbosAposEntregaLongoPrazo |  |
| Valor Seguro Prestamista | ValorSeguroPrestamista |  |
| Valor Seguro Prestamista Curto Prazo | ValorSeguroPrestamistaCurtoPrazo |  |
| Valor Seguro Prestamista Longo Prazo | ValorSeguroPrestamistaLongoPrazo |  |
| Valor Aditivo Venda | ValorAditivoVenda |  |
| Valor Aditivo Venda Curto Prazo | ValorAditivoVendaCurtoPrazo |  |
| Valor Aditivo Venda Longo Prazo | ValorAditivoVendaLongoPrazo |  |
| Valor Aditivo Venda Subunidade Antes | ValorAditivoVendaSubunidadeAntes |  |
| Valor Aditivo Venda Subunidade Apos | ValorAditivoVendaSubunidadeApos |  |
| Valor Entrega Chave | ValorEntregaChave |  |
| Valor Distrato | ValorDistrato |  |
| Valor Saldo Devedor | ValorSaldoDevedor |  |
| Valor Saldo Devedor Curto Prazo | ValorSaldoDevedorCurtoPrazo |  |
| Valor Saldo Devedor Longo Prazo | ValorSaldoDevedorLongoPrazo |  |

Para testar essa fórmulas com sql o contexto deverá seguir o padrão abaixo e substituir os valores fixos quando utilizar

SELECT  
        'J' TIPO\_ORIGEM\_CONTABIL,  
        '2021-03-03'DATA\_CONTABIL,  
        0 NUM\_ADIT,   
        3 COD\_COMPN,   
         '2021-03-03' DAT\_REAJUSTE,    
        1 COD\_GRUPO  
  FROM XVENDA  
WHERE NUM\_VENDA=1

O tipo   tem esses códigos internos

| TIPO\_ORIGEM\_CONTABIL | DESCRICAO |
| --- | --- |
| A | Aditivo |
| B | Estorno POC |
| C | Apuração POC |
| D | Distrato |
| E | EntregaChaves |
| F | SeguroPrestamista |
| J | ReajusteJuros |
| M | ReajusteCM |
| N | EstornoVenda |
| O | EstornoAditivo |
| P | ContabApuracao963 |
| R | EstornoEntregaChaves |
| T | EstornoDistrato |
| V | Venda |
| X | EstornoReajuste |
| I | TrocaSubUnidade |
| G | TransferenciaContabil |
| H | EstornoTransferenciaContabil |
| K | Securitizacao |
| L | EstornoSecuritizacao |
| Q | EstornoSeguroPrestamista |

**Executar:** Finaliza o processo de contabilização.  
Para saber maiores informações sobre a contabilização no Novo Modelo de BackOffice .
