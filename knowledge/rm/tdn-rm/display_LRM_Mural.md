---
content_hash: 9d04084954e2de67d193bad3be9a9816872abd95b66571471dc109cdde6870c1
fetched_at: '2026-06-29T00:08:37.198340+00:00'
page_id: '284879154'
product: rm
source: tdn-rm
title: Mural
type: documentation
url: https://tdn.totvs.com/display/LRM/Mural
version: 45
---

O mural do portal tem como objetivo, realizar a apresentação da IE para os Alunos, Responsável Acadêmico e Responsável Financeiro. A IE pode parametrizar os avisos para que os mesmo fiquem em destaque, e através dela, o aluno poderá ser redirecionado para algum menu específico.

## **01. PARAMETRIZAÇÃO**

 Conceder permissão para o usuário que irá realizar a parametrização do banner a ser exibido no portal do aluno.**Serviços Globais | Acesso | Perfis | 'Sistema' Educacional | Acesso Menu| Educacional | Currículo e Oferta | Acadêmico | Auxiliares | Banner**

## **02. CONFIGURAÇÃO DO BANNER A SER EXIBIDO NO PORTAL**

Para realizar a configuração do banner a ser exibido no portal. **TOTVS Gestão Educacional | Currículo e Oferta | Acadêmico | Auxiliares | Banner**

* **Titulo**: O Título que aparecerá sob a imagem a ser configurada;
* **Link**: Caso deseja redirecionar o aluno para outra página, informar o link neste campo. O portal irá abrir em uma nova aba do navegador com o link informado;
* **Data Inicial**: A data inicial determina a data em que o Banner será apresentado no mural. A data inicial é preenchida automaticamente de acordo com a data corrente, mas é possível informar uma data anterior ou posterior a data atual;
* **Data Final**: A data final determina o dia em que o Banner será apresentado no mural;
* **Ordem**: O campo ordem tem como objetivo definir a ordem de apresentação do mural.

Exemplo: Existem 2 Banners com a ordem de apresentação = 1  
**---** A data do 1º Banner é do dia 01/12/2016 á 31/12/2016  
**---** A data do 2º Banner é do dia 15/12/2017 á 15/02/2017  
A ordem de apresentação será: a partir 1º Banner

* **Ativo**: Este parâmetro determina que o banner está ativo ou não, através deste parâmetro que o usuário determina se o Banner será apresentado no mural;
* **Portal do Aluno**: Este parâmetro determina que o banner será apresentado no mural do portal do aluno;
* **Portal do Professor**: Este parâmetro determina que o banner será apresentado no mural do portal do professor;
* **Imagem**: O campo imagem tem como objetivo determinar qual a imagem será exibida no mural, é possível cadastrar com as seguintes extensões: .JPG, .JPEG, .JPE

Dimensão da imagem

A dimensão da imagem do banner deve ter **350px** de altura. Já sua largura é variável, mas sugerimos a largura de mínima de 1440px, mas isto fica a critério da instituição.

## **03. PARAMETRIZAÇÃO DO TEXTO PARA O MURAL NO PORTAL**

Além da imagem, o usuário poderá efetuar a parametrização de um texto a ser exibido juntamento com Banner, o texto é um *Widgets* fixo, isso é, o usuário não poderá alterar o posicionamento a não ser que possui outros widgets classificado como padrão. Caso tenha algum *widgets* classificado como favorito, o *widgets* informações do mural, estará fixo ao lado esquerdo da página.

Para configurar o texto, acessar: **TOTVS Gestão Educacional | Configuração | Parâmetros | RM Portal - Gerais | Portal - Geral 12/18 | Informações Mural**

* Marcar o chekbox: Informações do Mural
* Informar o texto desejado e em seguida salvar.

Permissão necessária para a exibição do mural no portal do aluno

Para que o mural seja exibido no portal do aluno é necessário conceder a seguinte permissão no perfil do usuário: **Serviços Globais | Acesso | Perfis | 'Sistema' Educacional | Acesso Menu| Educacional | Educacional (Portal) | Acadêmico | Widget**

Permisão para alterar a configuração do Widget

Para que o usuário do portal possa alterar as configurações do widget **Serviços Globais | Acesso | Perfis | 'Sistema' Educacional | Acesso Menu| Educacional | Educacional (Portal) | Acadêmico | Widget | Permitir alterar configurações do Widget**

## **04. ALERTA DE PRÓXIMO VENCIMENTO**

A partir da versão 12.1.2310 foi disponibilizado a opção de exibir um alerta no Mural do Portal do Aluno

**TOTVS Gestão Educacional | Configuração | Parâmetros | RM Portal - Gerais | Portal - Geral 8/18 | Exibir alerta de próximo vencimento**

**Exibir alerta de próximo vencimento:** Essa opção marcada e a quantidade de dias informada for maior que '0', permite que a instituição parametrize a exibição de um alerta no portal do aluno informando que existe um boleto para vencer em **X** dias. (quantidade de dias é limitado a 30)

Exemplo:

* Boleto com vencimento daqui a 5 dias
* Parâmetro **Exibir alerta de próximo vencimento** marcado e definido **10**

O alerta já começa a ser exibido e fica durante 5 dias até o boleto vencer ou ser quitado.

No portal será apresentado boleto que estiver nas condições do Alerta de Próximo vencimento.

Ao clicar no botão Pagar Agora, será apresentado uma tela com as opções de pagamento do boleto que está próximo a vencer. 

## **05. ALERTA PARA ATIVIDADES ACADÊMICAS**

A partir da versão 12.1.2502 foi disponibilizado a opção de exibir um alerta para atividades acadêmicas no Mural do Portal do Aluno

**TOTVS Gestão Educacional | Configuração | Parâmetros | RM Portal - Gerais | Portal - Geral 2/18 | Alerta para atividades acadêmicas**

**Exibir alerta com X dias de antecedência:** Com essa opção marcada, permite que a instituição parametrize a exibição de um alerta no portal do aluno informando as próximas atividades ofertadas e avaliações com **X** dias de antecedência.

Configuração das atividades para exibição

O portal irá exibir o **alerta das atividades acadêmicas do contexto do aluno selecionado**. As opções disponíveis são:

Atividades ofertadas

Para exibir as atividades ofertadas no alerta, será considerado o campo **Data da inicial** para realizar o cálculo do intervalo de tempo.

O aluno deve estar com a **Inscrição confirmada** para que seja exibido o alerta da atividade ofertada.

Avaliações

Para exibir as avaliações no alerta, será considerado o campo **Data da avaliação** para realizar o cálculo do intervalo de tempo.

Caso o campo **Data da avaliação** não esteja preenchido, será considerado o campo **Data prevista**.

Para que a avaliação seja exibida no alerta, a etapa precisa estar com o parâmetro "Exibe no portal e na central do aluno" marcado.

No portal será apresentado o seguinte modal contendo as próximas atividades acadêmicas do aluno:

Opção de "Não mostrar mais hoje"

Ao clicar fechar o alerta com a opção "Não mostrar mais hoje", o alerta **não será mais exibido** para o dia atual do contexto selecionado, no próximo dia de acesso a tela de mural, o alerta será exibido novamente, caso tenha alguma informação a ser exibida.
