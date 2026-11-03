---
content_hash: 3ef8a94f948d8ab7fe1e90261f474f57daf242bb417e1d80e156bb3d9f840e81
fetched_at: '2026-06-29T00:11:50.442199+00:00'
page_id: '841167644'
product: rm
source: tdn-rm
title: Central de Autorizações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=841167644
version: 29
---

## 

## **CONTEÚDO**

CONTEÚDO

## **01. VISÃO GERAL**

A **Central de Autorizações** é o módulo responsável pelo gerenciamento e controle das solicitações de autorização de procedimentos, exames, internações e demais serviços médicos junto às operadoras de convênios e planos de saúde.

Ela centraliza o fluxo de requisições enviadas pelos setores assistenciais, garantindo que todas as solicitações passem pelos processos de validação, autorização e retorno das operadoras de forma padronizada e rastreável.

O módulo permite o acompanhamento em tempo real do status das autorizações (pendente, em análise, autorizada, negada, etc.), o registro de protocolos, a anexação de documentos complementares e a comunicação com os sistemas de operadoras via integração (TISS).

Com isso, a Central de Autorizações otimiza o processo de atendimento ao paciente, reduzindo retrabalho, agilizando o retorno das operadoras e assegurando a conformidade com as normas da ANS e do padrão TISS.

## **02. TELA CENTRAL DE AUTORIZAÇÕES**

Faturamento / Particular e Convênios / Central de Autorizações

Esta visão exibirá os procedimentos que possuem uma solicitação de autorização.

A visão principal exibe (a esquerda) exibe as guias com seus itens, caso a guia possua itens, senão somente a guia, já a visão anexada (da direita) exibe todos os itens da guia selecionada na visão principal.

Atenção

Ao selecionar na visão principal um item de uma guia que possui mais de um item, no anexo o item selecionado será o primeiro da lista!

As autorizações também podem ser visualizadas em Faturamento / Particular e Convênios / Elaboração de Contas / aba Guias / Autorizações

## **03. CADASTRO DA AUTORIZAÇÃO**

Neste módulo, podemos visualizar uma autorização gerada (guia), e editar algumas das informações da mesma, como o número, senha e data da guia, a validade da senha, o status da autorização e a observação,

Ao abrir a visão, temos a área principal que é a aba "Autorização", exibindo dados do atendimento, parcial, paciente, os dados da guia, e algumas funcionalidades como verificar elegibilidade e anexos da guia.

Ao adicionar, é exibido o botão "Selecionar Atendimento" para que seja informado o atendimento e parcial vinculados a nova guia a ser lançada.

Em seguida temos a aba "Complemento", com campos de adicionais, como observações, e o histórico de autorização.

Por fim, temos a aba "Itens da Autorização", exibindo os itens lançados na guia.

Caso o status da guia seja "Autorizado" e possua as configurações de comunicação com o Serviço da TISS online, bloqueará a edição de todos os campos.

Atenção

Ao alterar o status da guia para Autorizado, Negado ou Cancelado, o status de todos os itens serão alterados de acordo.

Ao alterar o status de um item, o status da guia será afetado, por exemplo, se a guia está autorizada com 2 itens autorizados, e alterar o status de um deles para outro status, como pendente ou em análise, a guia ficará parcialmente autorizada.

Só é possível alterar o status da guia ou do item manualmente, se não possuir configurações de comunicação com o Serviço da TISS online nas condições contratuais!  
Se for possuir as configurações necessárias para efetuar a comunicação online, os status serão alterados apenas com a utilização dos processos (como solicitar autorização ou cancelar guia).

## **04. VERIFICAR ELEGIBILIDADE**

Na parte superior da tela, há um botão "Verificar Elegibilidade".

Para utilizar o processo, deve-se acessar Cadastros > Faturamento > Condições Contratuais > Aba Eletrônicos 3 > Aba WebService e configurar o campo "Solicitação de Elegibilidade" com a URL do webservice da operadora, e os campos "Usuário" e "Senha".

Ao clicar neste botão, a elegibilidade do paciente será verificada no convênio do mesmo, onde ao lado do botão, será exibido o resultado. onde:

* Se o paciente estiver elegível, o texto será "Elegível" na cor verde.
* Se o paciente não estiver elegível, o texto será "Não Elegível" na cor vermelha.
* Em qualquer outra situação, como falha de processamento, falta de internet, etc... o texto ficará "Não Verificado" na cor preta.

Em caso de problemas de processamento, é gerado um registro no log, podendo ser visualizado no Histórico de Autorização.

## **05. REALIZAR AUTORIZAÇÃO**

Este processo atualizará o item com o status da guia.

Esta atualização pode ser efetuada de modo online, efetuando a solicitação de autorização para o webservice da operadora, ou de modo offline.

#### Modo Online

Para utilizar o processo de modo online, deve-se acessar Cadastros > Faturamento > Condições Contratuais > Aba Eletrônicos 3 > Aba WebService e configurar o campo "Solicitação de Autorização" com a URL do webservice da operadora.

Com a URL do webservide da operadora configurado, e executar o processo de Realizar Autorização, o processo será executado diretamente, sem a interação do usuário, apenas exibindo o log do resultado do processamento.  
Ao fim do processo, o status é alterado de acordo com o retorno da operadora, e é gerado no log todo o processamento.

Se nas condições contratuais, o campo "Usa Código Validação" estiver marcado...

Ao executar o processo no modo online, será exibida uma etapa onde o usuário deve informar o código do token do usuário, ou o motivo de ausência do mesmo.  
É obrigatório informar um dos dois campos, e se não for informado, ao executar, será exibida uma mensagem, obrigando o usuário a informar.

Ao informar um dos dois, o outro será desabilitado.

#### Modo Offline

Se a URL da operadora não for informada, o sistema entenderá que não há um webservice para se comunicar com a operadora.  
Com isso o processo será executado de modo offline (manual).

Ao executar o processo no modo offline/manual, será exibida uma etapa onde o usuário deve informar o status do item da guia.  
Este campo é obrigatório, e se não informado, será exibida uma mensagem obrigando o preenchimento do mesmo.  
As opções disponíveis são:

* Autorizado
* Em análise
* Não Autorizado
* Pendente

Atenção

Também existe a opção "Cancelado", mas assim como destacado na tela do processo, para efetuar o cancelamento, deve-se utilizar o processo "Cancelar Guia".

Ao fim do processo, o status do item será atualizado, e adicionado no log a manipulação do registro pelo usuário.

Com duplo clique no registro do log, pode-se visualizar a mensagem completa, informando o número da guia que foi atualizada, junto do novo status e o usuário responsável pela alteração.  
Em caso de falha no processamento, também exibe o status atual.

## **06. CONSULTAR STATUS GUIA**

Este processo efetuará a consulta da guia no webservice da operadora, atualizando o status da guia de acordo com o retorno da operadora.

Para isso, a URL de consulta de status da guia deve estar informada.

Em caso de falha de comunicação dom o webservice, seja por falta de internet, serviço fora do ar, etc... exibirá uma mensagem informando o fato, e adicionando esta mensagem no log.

## **07. ENVIAR DOCUMENTOS**

Este processo enviará o documentos da guia no webservice da operadora.

Para isso, a URL da autorização e envio de documentos deve estar informada.

O processo de enviar documentos só poderá ser utilizado quando:

* Webservice de autorização e envio de documento estiverem preenchidos.
* Existir  uma autorização
* O status do item de autorização estiver autorizado ou analise.

Para adicionar um documento clique nos 3 pontos e selecione o arquivo. Depois clique em adicionar.

Após adicionar todos os arquivos execute o processo.

Em caso de falta de configuração ou não atender aos requisitos acima, exibirá uma mensagem informativa.

Após o envio do documento, o mesmo pode ser visualizado através do botão "Anexos da Guia"

Esta tela permite visualizar o documento, ou excluiro mesmo, caso ainda não tenha sido enviado para a operadora.

## **08. IMPRIMIR GUIAS**

Este processo efetuará a impressão da guia selecionada.

## **09. CANCELAR GUIA**

Este processo efetuará o cancelamento da guia, enviando a solicitação de cancelamento para o webservice da operadora caso a URL de cancelamento esteja configurada.

Em caso da URL não estar configurada, executará um cancelamento manual (offline).

Em caso de erro ao efetuar o processo online, informará o erro, e questionará se deseja efetuar o processo offline.

O motivo da falha também é adicionado no log.

## **10. VINCULAR ITEM DE ALTO CUSTO**

Este processo determinará que o item autorizado seja de alto custo.

O item em questão deve ser um material ou medicamento

Caso o processo já tenha sido executado anteriormente, exibirá este fato ao usuário.

Se o valor do item for inferior ao valor mínimo configurado como sendo de alto custo, exibirá uma mensagem informando este fato prousuário, e permitindo prosseguir.

A configuração do valor de alto custo, é efetuada em Cadastros > Faturamento > Condições Contratuais > Parâmetros 3 > MatMed, campo "Considerar Alto Custo a partir de R$".

Também é necessário marcar a opção "Incluir na Central de Autorizações".

Mais informações sobre itens de alto custo na documentação:

## **11. VALIDAÇÕES DA CENTRAL DE AUTORIZAÇÕES**

* Validação dos dados da guia e da solicitação
  + Campo “Número Guia Operadora” obrigatório, Caso esteja parametrizado
  + Data da guia obrigatório depende de parametrização do contrato com o convênio
  + Senha:
    - Pode ter o mesmo valor do número da guia operadora, caso esteja parametrizado para copiar o valor
    - Pode ser obrigatório caso esteja parametrizado. Este parâmetro só é habilitado para convênios que não possuem webservice
  + Campos sempre obrigatórios:
    - Tipo de paciente
    - Tipo de guia
    - Unidade de atendimento
    - Paciente
    - Convênio
    - Plano
* Validação dos itens da guia
  + Quantidade deve ser maior que zero
  + O procedimento deve ser informado

## **12.****Central de Autorizações**

A funcionalidade possibilita que a instituição junto com o controle de Autorizações e a Equipe da Central de Guias, acompanhe e realize o processo de Autorização de Guias de todos os procedimentos, diárias, taxas e serviços pendentes de autorização.

1. Acesse Cadastro/Faturamento/Condições Contratuais com o Convênio, anexo Restrições de Contrato.
2. Inclua restrições do tipo “Exige liberação do Convênio”.
3. Nas Condições Contratuais, aba Parâmetros 1, marque a opção “Diárias OBRIGATORIAMENTE incluídas nas Guias/ Autorizações de Internação”.
4. Essa configuração fará com que, caso a quantidade de diárias lançadas na conta do paciente exceda a quantidade autorizada (Autorizada + Pendente), seja lançada automaticamente uma nova guia de Solicitação de Prorrogação na Central de Autorizações.
5. Registre um atendimento para um paciente através de Atendimento/Internação/Registro de Internação ou Atendimento/Pronto Atendimento/ Registro de Atendimento Externo.
6. Através da Elaboração de Contas, inclua o item configurado como Restrito (Exigindo liberação do Convênio).
7. Será apresentada uma mensagem informando a condição do item, clique em Sim para confirmar.
8. O item será lançado na conta do paciente com um indicador laranja, informando a necessidade de liberação do Convênio.
9. Na guia Diárias, caso seja feito um novo lançamento que ultrapasse a quantidade autorizada (Guia/Autorização) e a quantidade pendente na Central de Autorização, será apresentada a mensagem abaixo.
10. Acesse Opções/Parâmetros/Parâmetros Gerais, aba Registro de Controle.
11. Marque a opção Procedimentos em 'Registro de Informações Cirúrgicas' iguais ao informado em 'Registro de Internações'.
12. Acesse a Cuidados com o Paciente/Centro Cirúrgico/Registro de Informação Cirúrgica.
13. Inclua um novo registro, selecionando o paciente que teve o atendimento registrado.
14. Na aba Procedimentos, inclua um novo item (que não conste na aba Guia/Autorização do Registro de Atendimento)
15. Ao confirmar o registro, sistema emitirá a mensagem abaixo.
16. Clique em Sim, o procedimento incluído será lançado na Central de Autorizações e o registro será exibido para preenchimento dos dados.
17. Após salvar as informações preenchidas, acesse o Processo “Realizar Autorização dos Lançamentos”.
18. Caso a autorização do lançamento seja posterior, acesse Faturamento/Central de Autorizações e selecione o registro desejado.
19. O registro autorizado ficará disponível no Registro de Atendimento, aba Guia/Autorização.
20. A configuração feita no passo 3 permitirá que, caso a quantidade de diárias lançadas na conta do paciente exceda a quantidade autorizada (Guias/Autorização), seja lançada uma nova guia de Solicitação de Prorrogação.

O lançamento da central poderá ser classificado de acordo com seu status e com o auxílio da classificação de autorização, presente em Cadastros/Faturamento/Classificação de Autorização.IMPORTANTE!

## **13. TABELAS UTILIZADAS**

Coloque o link das tabelas relacionadas
