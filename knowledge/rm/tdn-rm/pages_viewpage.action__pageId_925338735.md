---
content_hash: 53703edd922175dbef675d3b965b07c67d64750b23a22f99487fc27876c3e879
fetched_at: '2026-06-29T00:12:07.377339+00:00'
page_id: '925338735'
product: rm
source: tdn-rm
title: Validação Inteligente de Documentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=925338735
version: 9
---

Disponível a partir da 12.1.2506.

# Descrição

Esse processo tem como objetivo realizar a **validação** dos documentos entregues por alunos e/ou responsáveis, verificando automaticamente se os documentos são válidos ou não. Antes de iniciar a execução, é necessário **ler e aceitar os termos** apresentados na tela inicial do processo.

Após o aceite dos termos e o avanço para a próxima etapa, o sistema permitirá a seleção dos documentos a serem validados, com base em um filtro previamente executado.

# Funcionamento

Após o cadastro dos , o vínculo com os **documentos da integração com a Inteligência Artificial**, a definição de um  e a existência de **documentos entregues com status "Entregue em Validação"**, o sistema dará início ao processo automático de validação.

Durante esse processo, cada documento será analisado pela inteligência artificial, que atribuirá um novo status conforme o resultado da validação:

* **Validado**: quando o documento for aceito;
* **Recusado**: quando o documento for rejeitado;
* **Validado pela IA com necessidade de revisão humana**: nesse caso, o campo **"Necessária revisão humana"** será automaticamente marcado.

Se o documento entregue estiver vinculado a um d[ocumento de IA](https://tdn.totvs.com/display/LRM/Documentos+IA), o campo **"Existe Doc. IA"** será preenchido automaticamente.

Um ponto importante é que, **caso o  esteja associado a mais de um modelo da IA**, **basta que um deles seja considerado válido** para que o documento do aluno seja aprovado e tenha seu status alterado para **Validado**.

Durante a execução do processo, **somente serão exibidos documentos com status "Entregue em Validação"** que não estão **em revisão humana**. É possível aplicar filtros para refinar os documentos exibidos e, ao final, selecionar individualmente os documentos de cada aluno. **Apenas os documentos marcados na grade serão processados**.

A validação por IA também verifica se o tipo de documento enviado corresponde ao esperado — por exemplo, se o arquivo enviado como RG é realmente um RG — e se o documento pertence ao aluno, por meio da comparação entre os dados extraídos do documento e os dados cadastrais do sistema.

Essa verificação de conteúdo é aplicada para os documentos **RG, CNH, CIN e CPF**, com base nas seguintes informações:

* **Nome completo + Data de nascimento + Naturalidade**, ou
* **CPF**, se estiver presente no documento.

Caso haja divergência entre os dados, o documento será automaticamente rejeitado, com uma **justificativa clara informando que ele não pertence ao aluno**. Para isso, foi adicionada uma nova categoria no cadastro de [motivo de rejeição de documento](https://tdn.totvs.com/x/C5IDJQ), intitulada **"Validação de Conteúdo"**.

Para os documentos **RG** e **CNH**, a análise exige a presença da **frente e verso no mesmo arquivo**. A ausência de uma das faces impedirá a validação.

Ao final da execução, será exibido um **log detalhado** com todas as ações realizadas durante o processo.

Para os documentos com status **Recusado**, mediante parametrização, será enviado automaticamente um e-mail, por meio da [Central de Notificações](https://tdn.totvs.com/pages/viewpage.action?pageId=425458864)e do [eduCONNET](https://tdn.totvs.com/display/LRM/03.5+-+Cadastro+de+Mensagens), para o Aluno/Responsáveis informando quais documentos foram recusados e o motivo da recusa. Funcionalidade disponível a partir da versão 12.1.2506.128.
