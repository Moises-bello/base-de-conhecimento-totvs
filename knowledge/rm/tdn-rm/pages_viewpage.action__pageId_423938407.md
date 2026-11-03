---
content_hash: c5b05d5f4d1dd0be96599cf5651f282f80de5026e6cf6dda18fbe9a2913d1c97
fetched_at: '2026-06-29T00:09:26.754017+00:00'
page_id: '423938407'
product: rm
source: tdn-rm
title: Plano de Manutenção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938407
version: 5
---

A função do Plano de Manutenção é cadastrar peças e serviços relacionados a uma determinada manutenção periódica.   
**Exemplo 1**: A revisão de 10.000 km do Uno 1.6R, caso o objeto do sistema seja um automóvel.  
Todas as vezes que for necessário criar uma ordem de serviço para a revisão citada, poderíamos apenas selecionar o veículo e clicar no processo "Cria OS do Plano de Manutenção" e uma ordem de serviço com todos os seus itens (peças e/ou serviços) será gerada automaticamente. Esta função diminui consideravelmente o tempo gasto para montar uma OS. Existem dois tipos de Plano de Manutenção:

1. Plano de Manutenção por Cíclico é executado quando o Objeto de Manutenção ultrapassar o valor da freqüência informada no Plano de Manutenção.
2. Plano de Manutenção por Marco é executado quando o Objeto de Manutenção alcançar ou ultrapassar o valor exato da freqüência informada no Plano de Manutenção.

Faixa de Ano Modelo É possível definir um intervalo de "Faixa de Ano Modelo" para um plano de manutenção. Quando definido a Faixa de Ano Modelo o plano será executado apenas para aqueles objetos de manutenção com ano do modelo dentro da faixa. O ano do modelo é informado na tela de cadastro de objeto de manutenção pasta identificação. Informe o ano do modelo inicial e final para que o plano filtre os objetos que tenha o ano do modelo dentro desse intervalo.

**Exemplo 2**: Um plano por Cíclico 10000 km irá vencer quando ultrapassar o valor de 10000 km definido no plano de manutenção.   
Se o primeiro indicador de uso inserido quando o plano foi inicializado foi 2000 km então o plano irá vencer quando os indicadores de uso do objeto de manutenção atingir 12000 km.   
Já um plano de manutenção por marco 10000 km irá vencer quando o objeto de manutenção atingir 10000 km. S  
e o primeiro indicador de uso inserido quando o plano foi inicializado foi 2000 km, então quando for inserido mais 8000 km que é o restante que falta para o plano atingir os 10000 km o plano irá vencer.  
***Observação***: Os modelos apresentados na lista serão filtrados de acordo com o tipo de objeto selecionado.

**Dica** **1**: Na descrição do plano de manutenção é interessante preenchermos detalhadamente qual Tipo de Objeto o plano atinge e qual sua finalidade.   
Isso facilita a criação da OS para o Objeto de Manutenção.

**Exemplo 3**: Revisão Preventiva do Marea Turbo 2.0 MPI 20V – 10.000 Km.

**Dica** **2**: Caso um plano de manutenção seja comum a todos os sub-modelos de um determinado modelo (tenha produtos/serviços iguais ou semelhantes para a manutenção), ao copiá-lo, basta preencher ou não o campo sub-modelo.

**Exemplo 4**: Manutenção Preventiva de 25.000 Km do Vectra Manutenção Preventiva de 25.000 Km do Vectra 2.0 Manutenção Preventiva de 25.000 Km do Vectra 2.2. A caixa Tipo de Freqüência permite selecionar qual será o valor utilizado como referência de periodicidade para o plano de manutenção.

**Exemplo 5**:

1. Para um plano de manutenção bimestral do "Escort Station" deve ser escolhido o tipo de freqüência igual a "dias" e a freqüência igual a 60.
2. Selecionando a opção indicador de uso para o objeto de manutenção aeronave, no caso do plano "revisão do motor do Caravan I", realizado a cada 300 horas de vôo, o campo freqüência deve ser preenchido com o numeral 300.

A aba Parâmetro(s) só estará disponível quando parametrizada a opção "Gera Ordem de serviço automática", em "Opções | Parâmetros | Sistema".  
Na opção "Geração automática de Ordem(ns) de Serviço(s)", informe no campo "Tipo Movimento." qual será o tipo de movimento que será gerado pelo Plano de Manutenção.  
Quando o tipo de movimento não estiver preenchido significa que não deseja gerar Ordens de Serviço automáticas para o respectivo Plano de Manutenção.  
Quando o Plano de Manutenção estiver vencido ou vencendo no dia consultado, o sistema efetuará a geração da(s) respectiva(s) Ordem(ns) de Serviço, desde que sejam feitas as seguintes configurações:

No cadastro de tipo de movimento "Cadastros | Tipo de Movimento" devem estar informados

* a filial;
* o local de estoque e o funcionário responsável;
* o objeto de manutenção deverá ter preenchido seu cliente / fornecedor;

Assim, a geração automática de Ordens de Serviço poderá ser verificada quando entrar no aplicativo ou quando trocar de coligada.   
Nestes casos, será gerada uma solicitação de geração automática de Ordem de Serviço.   
Então, é só iniciar a geração das OS que possivelmente estejam armazenadas no banco de dados para ser geradas, através do menu "Sistema | Server | Executar Processos, Iniciar".  
Se uma das condições necessárias não se confirmar ou se houver algum problema na geração da Ordem de Serviço, será emitido um arquivo de log onde será informado qual o problema ocorrido para a não geração da ordem de serviço.

---
