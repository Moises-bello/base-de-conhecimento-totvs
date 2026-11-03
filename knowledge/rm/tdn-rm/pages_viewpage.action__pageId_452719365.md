---
content_hash: 111424ecec77da91cb4bd0ad846627425c543ad303e1d48e687c63a2185d5a03
fetched_at: '2026-06-29T00:10:07.106159+00:00'
page_id: '452719365'
product: rm
source: tdn-rm
title: Processo Aviso Automático
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719365
version: 90
---

Este documento tem como objetivo orientar o usuário na parametrização do Aviso Automático, bem como explicar como é realizado o envio das mensagens.

falseAviso Automático1Configurações

### Arquitetura em Três Camadas – Requisito para Aviso Automático

Para o correto funcionamento da rotina de **Aviso Automático**, é necessário que o ambiente esteja configurado em **arquitetura de três camadas**. Nesse modelo, o processamento da rotina é realizado pelo **JobServer**, garantindo maior estabilidade, desempenho e confiabilidade na entrega das informações.

Importante:

Abaixo, seguem links com explicações sobre o conceito e configuração da arquitetura em três camadas na plataforma .NET:

* [Entenda a arquitetura em três camadas](http://tdn.totvs.com/pages/releaseview.action?pageId=64652114)
* [Configuração do ambiente em três camadas](http://tdn.totvs.com/pages/releaseview.action?pageId=181143177)
* [Configuração de Jobs em ambiente 3 camadas](http://tdn.totvs.com/pages/releaseview.action?pageId=75271283)

### Alternativa

Caso a empresa não utilize a arquitetura em três camadas de forma ampla, é possível **isolar uma estação** com essa configuração para execução da rotina. Nessa estação, os **Jobs devem estar devidamente agendados** para que os avisos sejam disparados corretamente.

### JobServer – Execução da Rotina de Avisos Automáticos

Para garantir maior controle, desempenho e confiabilidade na rotina de **Avisos Automáticos**, as execuções são realizadas pelo **JobServer**, mecanismo responsável pelo agendamento e execução de processos no sistema TOTVS. Essa estrutura permite uma gestão mais prática e detalhada das tarefas, além de aumentar a estabilidade das operações.

🔗 **Referência**:  
[Envio de e-mail – LINHA RM](http://tdn.totvs.com/display/public/rm/Envio+de+email+-+LINHA+RM)

⚠️ **Importante:**  
Mesmo ao marcar o checkbox de apenas **um aviso automático**, ao executar o processo via JobServer, **todos os avisos automáticos existentes serão processados**, e não apenas o selecionado.

### Configuração de E-mails do Sistema

Para que os **Avisos Automáticos** com tipo de envio “e-mail” funcionem corretamente, é essencial que o sistema esteja devidamente configurado para envio de mensagens eletrônicas.

🔗 Consulte aqui as orientações:  
[Envio de e-mail – LINHA RM](http://tdn.totvs.com/display/public/rm/Envio+de+email+-+LINHA+RM)

2Formas de Envio da MensagemBody

### As formas de envio da Mensagem disponíveis são:

#### **1. E-mail**

Os e-mails d**e avisos automáticos serão enviados conforme as parametrizações definidas nas programações de avisos, desde que as condições configuradas para o tipo de aviso sejam atendidas.**

#### **1.1 Botão "Enviar Mensagens"**

Este botão permite o envio manual do e-mail do tipo de aviso selecionado na tela, especialmente quando o ambiente **não está configurado em arquitetura N Camadas.**

#### Observações:

* + Até a versão 12.1.26, o campo Assunto do e-mail é preenchido com o tipo do aviso automático.
  + A partir da versão 12.1.27, o Assunto do e-mail passa a incluir também a descrição cadastrada do aviso automático, tornando a comunicação mais clara e personalizada.
  + Nas versões 12.1.24, 12.1.25 e 12.1.26, essa melhoria está disponível mediante ativação de um parâmetro específico.  
    Para mais informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=519716142).

Importante:

O processo de aviso automático não considera filtros por coligada para o envio dos e-mails. Isso significa que, caso existam múltiplas coligadas com o mesmo tipo de aviso automático configurado, o aviso será enviado para todas elas, independentemente da coligada ativa no momento da execução.

#### **2. Mensagem na Tela**

Serão exibidas mensagens em tela referentes aos avisos automáticos, direcionadas aos usuários ativos e autenticados no sistema.

O envio dessas mensagens ocorre de acordo com as parametrizações definidas nas programações de avisos, desde que as condições configuradas para o tipo de aviso sejam atendidas.

As mensagens enviadas podem ser visualizadas em "Mensagens de usuários" presente no item "Mensagens":

#### **3. Forma de Montagem – Gerador de Relatórios**

A exibição das informações dos **Avisos Automáticos** pode ser configurada utilizando o Gerador de Relatórios da TOTVS.

Por meio dessa funcionalidade, é possível personalizar o conteúdo das mensagens automáticas conforme a necessidade da empresa, ajustando campos, textos e dados apresentados.

Para detalhes sobre como configurar o relatório via Gerador de Relatórios, acesse a documentação no link: [Forma de Montagem – Gerador de Relatórios (MRH-3323)](http://tdn.totvs.com/display/LRM/MRH-3323_DT_AVISO_AUTOMATICO_RELATORIO_NET)

Importante:

O envio de e-mails para chefes ira respeitar sempre o tipo de gestão de hierarquia parametrizado no sistema buscando sempre chefe do funcionário de acordo com o tipo de gestão e as configurações do aviso

3Formas de Montagem da MensagemBody

### As formas de montagem de Mensagem disponíveis são:

**1. Padrão**

Quando selecionada a forma de montagem **Padrão**, o sistema utilizará uma mensagem interna pré-definida e o agrupamento será feito por **Funcionários**.

**2. Gerador**

Na forma de montagem **Gerador**, o sistema habilita uma aba para seleção do layout do relatório, que será usado para montar a mensagem a ser enviada.

**3. Fórmulas**

Quando a forma de montagem for **Fórmulas**, o sistema habilita campos para que o usuário informe as fórmulas do cabeçalho, detalhe e rodapé da mensagem.

4Tipos de AgrupamentoBody

### Os Tipos de Agrupamentos disponíveis são:

**1. Funcionários**

No agrupamento por **Funcionário**, o envio já está definido para o próprio funcionário, mas há a opção de enviar também para outros tipos, como supervisores, chefes e terceiros.

**2. Supervisor**

No agrupamento por **Supervisor**, os e-mails são enviados aos supervisores dos funcionários, conforme o cadastro na tabela de Chefes e Supervisores. Nesse agrupamento, também é possível enviar a mensagem para o chefe.

**3. Chefe**

No agrupamento por **Chefe**, os e-mails são enviados somente aos chefes dos funcionários, conforme cadastro na tabela de Chefes e Supervisores. É necessário definir a quebra por chefe.

Importante:

Para o envio a chefes, o campo **“Masc. Quebra Chefe”** é habilitado. Ele verifica se o chefe está na seção informada.

* Exemplo: se um chefe supervisor está na seção `0` e o campo contém `?`, o sistema encontra o chefe.
* Se for informado `??` e o chefe não estiver na seção subsequente (`01`, por exemplo), o sistema não o encontrará, mesmo que esteja em uma seção maior (`012.01`). Para encontrar o chefe nessa seção, deve-se usar a quantidade de interrogações correspondente ao tamanho da seção, como `??????`.

**4. Seção**

No agrupamento por **Seção**, os e-mails são enviados para o(s) chefe(s) da seção e/ou terceiros, sendo necessário definir a quebra de seção.

Importante:

Ao marcar a flag **“E-mail(s) de terceiro(s)”**, habilita-se um campo para informar os e-mails dos terceiros, separados por ponto e vírgula (;). Este é o único local do sistema para incluir terceiros no envio.

400basTipos e Avisos AutomáticosBody

### Os tipos de Avisos Automáticos disponíveis são:

**1. Escala de Férias**

Envia um aviso automático sempre que um ou mais funcionários estiverem próximos do início do período de férias. O objetivo é notificar os chefes para que possam se organizar e minimizar impactos. O número de dias de antecedência é controlado pelo campo **Nro. Dias Referência**.

Importante:

O campo **Nro. Dias Referência** considera a data atual e busca funcionários com o início do gozo das férias dentro do período informado. Ele não considera o status das férias, apenas a data de início.

**2. Término de Contrato de Trabalho**

Gera um aviso automático quando contratos de funcionários estiverem próximos do vencimento, para que os chefes possam se preparar para renovação ou desligamento. O prazo de antecedência também é controlado pelo **Nro. Dias Referência**.

**3. Férias em Dobro**

Gera aviso para funcionários que possuem férias vencidas há mais de um ano, alertando os chefes sobre a necessidade de pagamento em dobro caso as férias não sejam gozadas. O prazo de antecedência é controlado pelo **Nro. Dias Referência**.

**4. Alteração de Salário**

Gera aviso sempre que houver alteração salarial de um ou mais funcionários, notificando chefes e funcionários sobre a mudança.

**5. Alteração de Função**

Gera aviso para alterações na função do funcionário, mantendo os chefes informados sobre mudanças internas.

**6. Demissão**

Gera aviso automático quando um ou mais funcionários forem desligados.

**7. Solicitação de Alteração de Dados Bancários**

Gera aviso quando um funcionário solicita alteração de dados bancários via Portal ou pelo produto.

**8. Confirmação de Alteração de Dados Bancários**

Gera aviso quando o usuário aprova a alteração dos dados bancários pelas rotinas de aprovação ou libera a competência, dependendo do parâmetro **“Enviar direto para o cadastro de funcionários”** configurado no RM Portal.

**9. Outros**

Tipo criado para permitir customizações no envio de mensagens, dando flexibilidade para a equipe de desenvolvimento.

**10. Requisição de Alteração Salarial Aprovada**

Gera aviso sempre que uma requisição de alteração salarial é aprovada.

**11. Admissão de Candidatos**

Gera aviso sempre que um candidato é incluído em processo de admissão no Vitae.

**12. Anotação Pessoal**

Gera aviso quando é registrada uma anotação pessoal para um funcionário.

**13. Limite de Permanência na Categoria Profissional**

Gera aviso quando um funcionário atinge o limite de tempo para permanência em uma categoria profissional.

**14. Fórmula**

Gera aviso automático para funcionários que atendem a condição definida por uma fórmula. A fórmula deve retornar falso ou 0 quando a condição não é atendida, e uma mensagem (resultado da fórmula) quando atendida. A fórmula é executada para funcionários ativos (não demitidos e com usuário ativo).
