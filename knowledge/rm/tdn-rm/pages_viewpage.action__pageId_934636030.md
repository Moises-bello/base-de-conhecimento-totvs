---
content_hash: d5585567a4ee5b918cc6cd384a1e29be423389903ca2692ae6cde56ed560a3f6
fetched_at: '2026-06-29T00:12:08.460405+00:00'
page_id: '934636030'
product: rm
source: tdn-rm
title: Comece por aqui!
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=934636030
version: 8
---

Conteúdo:

1Conteúdo:

# 1. Sobre

O objetivo dessa documentação é guiá-lo durante a configuração do sistema para acessar o TOTVS Inteligência Tributária. Consulte sempre que tiver dúvidas!

Basta seguir essas orientações para ter acesso ao TOTVS Inteligência Tributária. É bem simples! 

Lembrando que a nova ferramenta está disponível a partir dos seguintes patches e superiores:

* 12.1.2402.**291**
* 12.1.2406.**263**
* 12.1.2410.**212**
* 12.1.2502.**131**

# 2. Passo a passo

CardsPré-requisitos técnicosPermissão de acesso

Na MDI, acesse o [cadastro de perfis](https://tdn.totvs.com/display/LRM/Perfil) e selecione o sistema '**Gestão Fiscal**'.

Edite o cadastro do perfil associado ao usuário que deseja liberar o acesso ao TOTVS Inteligência Tributária e clique na aba 'Acesso a Menus'. Por fim, permita o acesso a etapa [04.04], conforme demonstrado na imagem abaixo:  

Imagem

# 

Processamento dos dados

Com o intuito de tornar o acesso aos dados do TOTVS Inteligência Tributária o mais transparente e disponível possível, foi disponibilizado um processo para calcular e armazenar, de forma criptografada, as informações exibidas nas diversas abas do painel TOTVS  Inteligência Tributária.

O processo consiste em identificar os períodos que devem ser processados para, em seguida, recuperar os dados, realizar o processamento e armazená-los em uma tabela específica e criptografada para cada período.

Observação

Os tributos considerados pelo TOTVS Inteligência Tributária, e neste processo, são: **ICMS, ICMS-ST, ISS, IPI, PIS e COFINS**.

Esse processo pode ser executado manualmente ou de forma agendada através da opção **TOTVS Inteligência Tributária | Processamento.**

Imagem

Basta selecionar o período para o qual deseja processar os dados e a(s) Coligada(s) na qual deseja que o processamento ocorra:

Imagem

Será então iniciado um processamento ou agendamento do JOB (ambiente 3 camadas) para as coligadas e período selecionados.

Os dados necessários serão selecionados, processados e armazenados para posterior exibição nas diversas visões do TOTVS Inteligência Tributária.

Os registros na tabela do TOTVS Inteligência Tributária possuem um status que indica a situação do registro, podendo ser: **Consistente**, **Inconsistente** ou **Parcial/Aberto**. Esse status é determinado conforme a situação do período de apuração no TOTVS Gestão Fiscal no momento do processamento dos dados para o TOTVS Inteligência Tributária (ver mais abaixo). Os status podem ser:

* + **Consistente**: Todos os períodos de apuração - coligada, filial e tributos - estão encerrados;
  + **Parcial/Aberto**: Quando algum dos período de apuração - coligada, filial e tributos - está aberto;
  + **Inconsistente**: Este status possui um tratamento diferenciado pois ele é aplicado aos registros quando o respectivo período de apuração no TOTVS Gestão Fiscal for reaberto. Mesmo que o período no TOTVS Gestão Fiscal seja reaberto para um tributo e filial específicos este status será aplicado a todos os registros de tal coligada/período no TOTVS Inteligência Tributária independente de filial e tributo.

O processamento para a geração de dados no TOTVS Inteligência Tributária considera apenas os cenários (coligadas e períodos selecionados) que:

1. 1. **Não existem** nas tabelas do TOTVS Inteligência Tributária.
   2. **Possuem status Inconsistente ou Parcial/Aberto**.

Nesses casos, os registros são excluídos, os dados das movimentações da coligada e do período são recuperados, processados e, então, novos registros são inseridos na tabela do TOTVS Inteligência Tributária com o status adequado:

* + **Consistente**: Se **todos** os períodos de apuração da coligada e do período (independentemente da filial e do tributo) estiverem encerrados;
  + **Parcial/Aberto**: Se **pelo menos um** dos períodos de apuração da coligada e do período estiver aberto.
0solid

**Quer contribuir com a evolução da nossa documentação? [Clique aqui e dê um feedback sobre esta página!](https://forms.gle/RZXc3eYwhuq9TNtD6)**
