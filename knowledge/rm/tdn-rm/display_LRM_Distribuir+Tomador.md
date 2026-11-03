---
content_hash: 595c71467fa055dbdd1f4c682cc9191a2c63c0240f4ae33a09792e609f937f24
fetched_at: '2026-06-29T00:10:07.297656+00:00'
page_id: '452719395'
product: rm
source: tdn-rm
title: Distribuir Tomador
type: documentation
url: https://tdn.totvs.com/display/LRM/Distribuir+Tomador
version: 10
---

falseATENÇÃO:

A partir da release **12.1.2606**, este menu teve sua descrição alterada de **Distribui SEFIP** para **Distribuir Tomador**, refletindo que as informações anteriormente relacionadas à SEFIP passaram a ser atendidas pelo **eSocial**.

No anexo "Rateio Tomadores" do cadastro de funcionários serão cadastradas as informações das empresas Tomadoras de Serviço. As informações dos Tomadores de Serviço serão prestadas nos arquivos com Códigos de Recolhimento 150, 155 e outros. Para os funcionários que trabalharam em Tomadores de serviço a movimentação do funcionário deverá ser informada proporcionalmente aos dias trabalhados em cada Tomador de Serviço.

De acordo com o cadastro acima deverá ser feita a distribuição por tomador de serviços dos valores pagos no mês atual aos funcionários.  
   
O procedimento de distribuição deverá ser efetuado após o fechamento da folha de pagamento. Apenas os eventos que seguem rateio de tomadores e o INSS (Código de Cálculo 3) serão distribuídos, os demais terão os seus valores lançados integralmente na empresa.   
   
Os períodos podem ser selecionados para a distribuição de acordo com a necessidade do usuário.

Na competência atual, quando selecionado o período 10000 não serão habilitados os campos:  “Distribuição Somente de Retificação” e “Rateio tomador por”.

A opção: “Distribuição Somente de Retificação” será habilitada apenas para competências anteriores à atual devendo ser informado o período de retificação para distribuição da movimentação por tomador.

 As opções disponíveis no campo "Rateio tomador por" definirão como será realizada a distribuição por tomador em caso de retificação e/ou distribuição retroativa, de acordo com a opção selecionada pelo usuário:   
   
**Tomadores da Competência Atual:** O rateio de tomador será realizado observando o "Rateio Tomador" cadastrado em: Funcionários | Anexos: Folha de Pagamento | Rateio Tomadores.

**Histórico de Tomador**: O rateio de tomador será realizado observando o cadastro de “Histórico de Rateio por Tomador”, cadastrado em:  Funcionários | Anexos: Históricos | Histórico de Rateio Por Tomador.

**Observação:** Para as duas opções acima é possível optar por **“Sobrepor dados existentes”**. Com o flag marcado, o sistema substituirá o rateio existente, no mês selecionado, pelo novo rateio que está sendo realizado. Com o flag desmarcado, o sistema fará o rateio apenas para os eventos que não possuem distribuição no mês selecionado.

**Rateio de Eventos:** O rateio de tomador será realizado observando o rateio informado em tela. O mesmo deve ser previamente cadastrado em: Administração de Pessoal | Eventos | Rateio de Eventos, informando quais os eventos serão utilizados como base para a distribuição.

**Observação:**

1. Quando não houver tomador cadastrado para realizar a distribuição será considerado o tomador empresa cadastrado em: Configurações | Parametrizador | Folha Normal | Tomador de Serviços.
2. O tomador empresa não deve ser utilizado no anexo "Rateio Tomadores" do cadastro de funcionários. Caso algum evento não esteja configurado para seguir o rateio por tomador, ele será automaticamente atribuído ao tomador empresa, o que pode gerar erros na distribuição.

|  |  |
| --- | --- |
|  | Veja Também |

---

[Como processar a distribuição para tomadores de serviços de retificação da rescisão?](http://tdn.totvs.com/pages/viewpage.action?pageId=435110514)
