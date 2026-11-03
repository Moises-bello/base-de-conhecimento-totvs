---
content_hash: 54f97c873df56d64fc617287ab7afb4a03d9358e0e3781ecab34db0c1b4c3701
fetched_at: '2026-06-29T00:10:30.028194+00:00'
page_id: '518482641'
product: rm
source: tdn-rm
title: Meu Imóvel - Situação Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=518482641
version: 87
---

**Índice**

Venda

# **1) Visão Geral**

---

A funcionalidade **Situação Financeira** estará disponível a partir da versão 12.1.28 da Biblioteca RM. Esta funcionalidade apresentará de forma resumida as parcelas em aberto/parcialmente baixadas de um determinado contrato e seus valores atualizados. Será possível também, a partir da versão 12.1.29, realizar renegociações financeiras para contratos de aluguel.

* **Seleção de Empreendimento / Unidade / Contrato de locação**Esta tela permite ao usuário selecionar o empreendimento ou o contrato de aluguel, no carrossel superior e ver os detalhes dos valores financiados, pagos e valores restantes.  
  Ao selecionar o empreendimento, o Meu Imóvel irá listar, em formato de cards, a(s) sua(s) subunidade(s) compradas, com os detalhes financeiros pertinentes a cada uma.

Ao selecionar a opção Aluguel no carrossel, o Meu Imóvel irá listar, em formato de cards, o(s) seu(s) contratos de aluguel, com os seus respectivos detalhes financeiros. Para estes contratos de aluguel, serão listadas apenas informações sobre as parcelas pagas e o menu para renegociação de dívidas, bem como o número de parcelas em atraso.

Novidade

### Implementação do Boleto Híbrido no App Meu Imóvel

Foi implementado o **boleto híbrido** no **App Meu Imóvel**.

Com essa implementação, ao configurar nos parâmetros do portal do cliente no **TCGI** para utilizar o boleto híbrido, o **App Meu Imóvel** passará a gerar o boleto híbrido no processo da **Situação Financeira.**

Na tela de visualização de boletos, estarão disponíveis, em um único registro de boleto, as seguintes opções:

* **Copiar código de barras**, permitindo pagamento via boleto bancário tradicional.
* **Copiar QR code PIX**, possibilitando pagamento instantâneo via PIX.
* **Enviar boleto por...**, oferecendo praticidade para envio rápido do documento.

Dessa forma, o cliente terá ainda mais flexibilidade para escolher a forma de pagamento mais adequada às suas necessidades, seja pela agilidade do PIX ou pela praticidade e maior prazo do boleto tradicional, sempre com segurança e facilidade na utilização.

* Para configurar o uso do boleto híbrido no portal, acesse: [Totvs Incorporação - Parâmetros - Portal do Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047).
* Para saber mais sobre o funcionamento e vantagens do boleto híbrido, acesse: [Boleto Híbrido](https://tdn.totvs.com/pages/releaseview.action?pageId=908344227#0-1).

**É importante que o relatório associado à impressão deste tipo de boleto esteja parametrizado para apresentar tanto a imagem do código de barras, quanto a imagem do qr code pix.**

No card principal da subunidade, o Meu imóvel apresentará algumas informações como o valor financiado total, o valor restante e o valor já pago, bastando deslizar o dedo onde se lê os valores em reais do financiamento.  
Alem destas informações, consta, como mostra a figura, a porcentagem do valor já pago.

O Meu Imóvel irá informar ao usuário quantas parcelas estão em atraso no momento, (caso existam) no card da subunidade em questão.

Para cada contrato há a possibilidade de **pagar as parcelas atrasadas ou antecipá-las**. Há também a possibilidade de **renegociar as dívidas**, permitindo o comprador realizar ou sugerir uma renegociação de parcelas vencidas de sua venda, gerando um novo plano com novas parcelas.

---

# **2) Pagar parcelas atrasadas ou antecipar**

---

Ao tocar no menu "**Pagar parcelas atrasadas ou antecipar**" O Meu Imóvel irá mostrar todas as parcelas em aberto e vencidas para a subunidade, conforme as configurações aplicadas nos [Parâmetros de Relatórios do Portal do Cliente](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047). Possibilitando a geração de boleto para uma ou mais parcelas, neste caso, agrupando-as num só boleto. Caso não existam parcelas atrasadas, o Meu Imóvel irá mostrar o menu **"Antecipar parcelas".**

Ao dar um clique em  de uma determinada parcela selecionada, a mesma será expandida, mostrando alguns **detalhes da parcela**, como juros e multa no dia corrente.

* **Resumo do plano de financiamento:**Ao tocar na seta dupla à direita das informações da Subunidade, será exibido um **resumo** do **plano de financiamento**, com o percentual do que já foi pago, além dos Valores Financiados, Valor Total Pago e o Valor Restante do financiamento, ampliando o leque de informações pertinentes a subunidade na data atual.

Caso o percentual pago seja menor que 80%, as informações exibidas estarão na cor laranja, caso contrário, as informações serão exibidas na cor verde.

**Passo a passo para gerar boleto das parcelas exibidas na Situação Financeira:**

* **Seleção de parcelas para renegociar:**Ao tocar sobre a parcela a mesma será selecionada, exibindo uma caixa de diálogo informando o número de parcelas já selecionadas para o filtro atual.

É possível filtrar os tipos de parcelas exibidas na tela. Para isto, existe o ícone de filtro que, ao ser pressionado exibe a tela de filtro com os tipos de parcela existentes. Após selecionar o(s) tipo(s) desejado, basta pressionar fora do filtro, em qualquer área da tela.

* Ao seguir , cliente pode selecionar opção (Boleto ou Pix).

* **Seleção da Data de Vencimento:**Ao tocar em continuar será aberto uma tela para seleção da data de vencimento para as parcelas selecionadas:
  + **Importante: Para que o Meu Imóvel apresente as datas de vencimento para seleção, devemos primeiro definir o parâmetro "Nro máximo de Dias para Vencimento do Boleto" Em *Ambiente / Parâmetros / Portal do Cliente / Relatórios.***

* **Parcelas Recalculadas:**Após selecionar a nova data de vencimento para as parcelas selecionadas, o Meu Imóvel irá apresentar a visão das parcelas recalculadas, com os seus respectivos valores atualizados.

* **Gerar boleto:**Ao pressionar em Continuar, o app Meu Imóvel irá gerar um boleto com o valor total unificando as parcelas e com a data de vencimento definida anteriormente. A partir desta tela é possível visualizar o boleto em formato PDF, compartilhar o arquivo através de outros aplicativos e também, copiar o código de barras deste boleto para pagamento em outros aplicativos.

Depois do boleto ter sido gerado, ele passará a ser exibido no menu **Boletos:**

* **Gerando PIX.**

Selecionando as parcelas que serão pagas por PIX.

Verificando o Valor e em seguida : Confirmar

Em Boletos ele fica com PIX em seu registro.

No TOTVS Gestão Financeira fica o registro do PIX inserido via APP meu Imóvel.

**Dentro do Portal do Cliente o PIX fica registrado :**

Atenção

* Os novos boletos serão gerados somente através de Registro Online;
* Para que seja possível gerar novos boletos para parcelas vencidas é necessário habilitar a opção através dos parâmetros abaixo. Caso contrário serão exibidas apenas parcelas futuras para antecipação.
  + ***Ambiente / Parâmetros / Portal do Cliente / Relatórios -*** "Permite gerar novo boleto parcela vencida e do mês".
  + ***Ambiente / Parâmetros / Portal do Cliente / Relatórios -***  **"**Nro máximo de Dias para Vencimento do Boleto**"**
* O convênio utilizado para gerar os boletos deve ser associado no anexo Dados Bancários no cadastro de Empreendimento.

---

# **3) Renegociar Dívida**

---

Será possível também, no Meu Imóvel, realizar uma renegociação de parcelas vencidas de sua venda ou aluguel, gerando um novo plano com novas parcelas, tocando no menu "**Renegociar Dívida**". São parcelas passíveis de renegociação para **contratos de venda:**

* Parcelas em aberto e vencidas
* Parcelas com o componente do tipo Entrada ou Principal
* Parcelas do tipo a Receber

As parcelas que poderão ser negociadas para **contratos de aluguel** são as seguintes: 

* Parcelas em aberto e vencidas;
* Baixadas parcialmente;
* Parcelas do tipo a Receber;
* Parcelas do evento financeiro integrado ou parcialmente integrado;
* Parcelas do evento financeiro do mesmo tipo de evento financeiro configurado no contrato de locação.

Os valores das parcelas exibidas já são apresentados com reajuste atualizado. Portanto para o uso adequado desta ferramenta é necessário que o RM esteja configurado para utilizar o Reajuste Online.  
Ao tocar no menu **"Renegociar dívida"**, o Meu Imóvel exibirá um resumo das parcelas em atraso, seus valores atualizados e ao tocar no botão "Continuar" o usuário poderá renegociar uma ou mais parcelas.

* **Tempo da Renegociação**: Ao tocar em continuar, teremos a apresentação da tela de tempo da renegociação. Neste momento o usuário selecionará a quantidade de parcelas do novo plano, que deverá ser entre 1 a 60 parcelas. Além disso, o Meu Imóvel irá mostrar o valor atualizado das novas parcelas que serão geradas. Ao tocar no botão "Continuar", iremos para a próxima tela, de revisão da renegociação.

Para as renegociações de aluguel, o sistema irá respeitar o parâmetro "Número máximo de parcelas", que deverá ser definido em   
No caso de parcelas de Vendas, o "Limite de Parcelas" poderá ser definida em: [Parâmetros / Portal do Cliente / Renegociação de Contrato](https://tdn.totvs.com/pages/viewpage.action?pageId=435105047)

Após a definição do número de parcelas e verificar os valores correspondentes, o Meu Imóvel nesta etapa irá exibir a tela de revisão, onde será possível visualizar o número de parcelas geradas e o valor destas novas parcelas.  
Serão exibidos também as datas do primeiro vencimento e o último vencimento dos valores renegociados, além do valor renegociado e os valores totais a serem pagos na renegociação.

Para as **renegociações de aluguel**, o sistema irá respeitar o parâmetro "Utiliza regra de vencimento do contrato de locação" e "Número de dias corridos para o primeiro vencimento", que deverão ser definidos em  obedecendo a seguinte lógica para calcular a data do primeiro vencimento:

* Com o parâmetro "Utiliza regra de vencimento do contrato de locação" marcado, se o vencimento de um determinado contrato de aluguel é no dia 8 e a renegociação está sendo realizada num dia anterior, então o vencimento será no dia 8 deste mesmo mês. Se a renegociação ocorrer no dia 8 ou após este dia, então o vencimento da primeira parcela mudará para o dia 8 do mês seguinte.
* Com o parâmetro "Número de dias corridos para o primeiro vencimento" marcado, o Meu Imóvel não usará a regra de vencimento do contrato e passará a valer-se deste parâmetro para definir a data da primeira parcela a partir da data da renegociação.
Importante

* Para contratos de venda, quando o usuário chegar nessa tela, o sistema criará um aditivo para a venda correspondente com o Status '**Em Análise**' e caso o usuário desista da operação ou feche o aplicativo esse aditivo será excluído, caso ele prossiga e finalize o processo de renegociação o aditivo será alterado para o Status '**Em Preparação**' para que o operador do sistema dê sequencia no processo.
* Para renegociações de aluguel, quando o usuário chegar nessa tela, o sistema criará um , com o status **"Em Análise",**e caso o usuário desista da operação ou feche o aplicativo esse aditivo será excluído. Caso ele prossiga e finalize o processo de renegociação, o aditivo será alterado para o status "**Em Preparação",**para que o operador do sistema dê sequencia no processo.
* Caso não exista termo configurado nos [parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=435105240) o sistema irá incluir o aditivo já no status **"Em Preparação".**

Após revisar os novos valores, o usuário deverá tocar no botão "Termos da Renegociação".   
O termo da renegociação é um relatório, que será mostrado ao usuário, listando os valores atualizados e a quantidade de parcelas selecionadas. A TOTVS disponibiliza, a partir da versão 12.1.28 um [modelo simples do relatório](https://tdn.totvs.com/pages/viewpage.action?pageId=544188979) que poderá ser utilizado somente para renegociações de contratos de vendas.

Para renegociações de aluguel, o Meu Imóvel irá valer-se do Termo de Renegociação parametrizado em:  . Além disso, deve-se também parametrizar nesta mesma área uma classificação de documento, que fará com que o termo seja associado ao contrato de aluguel no momento em que a renegociação é gerada.  
Será possível então, salvar este relatório no aparelho, visualizá-lo ou enviar / compartilhar através de outros aplicativos, O relatório será salvo e compartilhado sempre no formato .pdf, da mesma forma que é feito com os boletos gerados no aplicativo.

Assim que fizer download ou visualizar em seu celular o relatório da renegociação, basta tocar na caixa "**Confirmo que li e concordo com os termos da renegociação financeira**", para que a renegociação possa ser concluída com sucesso. Assim que o usuário tocar em "Confirmar", o Meu Imóvel irá exibir a seguinte tela:

Com isso, o usuário poderá acompanhar sua renegociação como mostrado no tópico abaixo, bem como consultar o documento do Termo de Renegociação, que ficará disponível no menu de Documentos.

Aditivo é criado no TCGI no valor da Renegociação para ser ou não aprovado.

---

# **4) Ver detalhes da renegociação**

---

Após a renegociação solicitada com sucesso, o  usuário poderá acessar o status desta negociação, através do menu **"Ver detalhes da Renegociação"**, no menu principal da situação financeira. Este menu, irá listar todas as renegociações deste contrato, suas datas, valores e status da negociação, como mostram a imagem abaixo:

Neste caso, temos uma renegociação ainda em preparação, com seus valores, número de parcelas e datas listadas no card. Assim que o aditivo de renegociação for efetivado, seu status passará para **efetivado,** e a renegociação estará completa. Nesta tela também poderá ser consultado o termo de renegociação, que listará em formato de um relatório todos os valores, parcelas e outros detalhes da negociação.

O termo da renegociação é um relatório, que deverá ser definido nos parâmetros em

Para renegociações de contratos de aluguel, o termo de renegociação deverá ser definido em:  [Parâmetros / Aluguel / Renegociação de Contrato](https://tdn.totvs.com/pages/viewpage.action?pageId=435105240#TotvsIncorpora%C3%A7%C3%A3o-Par%C3%A2metros-Aluguel-Renegocia%C3%A7%C3%A3odeContrato)

---

# **5) Ver parcelas pagas**

---

Será possível também, no Meu Imóvel, visualizar as parcelas já pagas de sua venda ou do seu contrato de aluguel, bastando tocar no menu "Ver Parcelas Pagas" na visão de contratos.

Para as parcelas pagas de um contrato de aluguel, o sistema irá ordenar estas parcelas da competência mais nova para a mais antiga, facilitando ver as últimas parcelas pagas em primeiro lugar.

**Importante**: As solicitações de renegociação podem ser efetivadas de forma automática ou não, dependendo dos parâmetros. Caso a solicitação necessite de uma aprovação do setor responsável, então um alerta será exibido para o usuário.

Caso não exista relatório de renegociação parametrizado como informado acima, o Meu Imóvel não irá apresentar o botão "Termos da renegociação". Entretanto, permitirá a solicitação da renegociação, que deverá ser analisada posteriormente pelo setor responsável.
