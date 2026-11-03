---
content_hash: 8009ea4e3c9b6b41d79f88bcfb5f4d56180309e616a91fe2a7d754580efd8cee
fetched_at: '2026-06-29T00:11:25.387299+00:00'
page_id: '708105303'
product: rm
source: tdn-rm
title: 08.3 Integração com TOTVS Assinatura Eletrônica (TAE)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=708105303
version: 23
---

O processo de Integração TOTVS Assinatura Eletrônica permite que seja enviado para ser assinado eletronicamente um documento que represente o contrato do aluno no TOTVS Educacional.

Com as parametrizações feitas para a integração é possível habilitar a utilização do TAE na matrícula on-line, para isso, acesse o caminho abaixo e marque a opção conforme o comportamento que queira no portal.

Menu: Configurações | Parâmetros | RM Portal | Matrícula | Portal - Assinatura contrato

Não é possível habilitar a utilização do **TAE** junto com o **Token/chave de segurança**, somente será possível utilizar uma forma de assinatura.

Marcando somente o parâmetro Utilizar assinatura com TOTVS Assinatura Eletrônica

Parâmetro para **Utilizar assinatura com TOTVS Assinatura Eletrônica**marcado:

No processo de matricula on-line ao finalizar:

No contrato do aluno não irá ser marcado o campo que indica que ele está assinado e não será preenchido a data de assinatura, mesmo após o aceite do aluno. Com isso, não teremos um registro na visão de assinatura associado ao contrato do aluno.

Vale lembrar que, este comportamento somete será respeitado, se o [contrato](https://tdn.totvs.com/display/LRM/Contratos+-+Educacional) (do tipo plano) do aluno for criado no momento da matrícula on-line ou se o mesmo já tenha sido criado anteriormente, caso contrário isso não irá acontecer, ou seja, esta integração não efetua nenhuma criação de [contrato](https://tdn.totvs.com/display/LRM/Contratos+-+Educacional).

Caso opte por utilizar o **token/chave de segurança**, ao finalizar a matrícula e o contrato for criado, o mesmo irá ter seu campo assinado marcado e a data de assinatura preenchida.

Após a criação do contrato é necessário enviá-lo para o **TAE**, para isso acesse na visão de contrato o processo: **Integração TOTVS Assinatura Eletrônica**.

Vale ressaltar que caso seja necessário enviar o contrato para o fiador, o aluno deverá possuir um fiador **ativo** e **aprovado** com nome, CPF (quando a nacionalidade for Brasileira) e e-mail preenchidos no cadastro do **cliente/fornecedor**, caso não possua o documento não será enviado para o TAE.

Para saber mais sobre o processo [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=578823895).

Marcar também o parâmetro para Assinatura do contrato obrigatória na rematrícula

Parâmetro para **Utilizar assinatura com TOTVS Assinatura Eletrônica** e **Assinatura do contrato obrigatória na rematrícula** marcado:

Por padrão, a assinatura da entidade **Responsável financeiro/contrato** é obrigatória, portanto, não é possível desmarcá-lo.

No processo de matrícula on-line se estiver somente com a entidade **Responsável financeiro/contrato** marcado, se oAluno e Responsável Financeiro são a mesma pessoa e tem os mesmos dados, ao clicar **Assinar contrato** o processo seguirá sem impedimentos. 

**Após os patchs 12.1.2502.256, 12.1.2506.214 e 12.1.2510.142**, o assinante que executa a rematrícula receberá em seu e-mail **apenas o token** para concluir a matrícula, já demais assinantes receberão normalmente o e-mail de notificação com link de acesso ao TAE. Nessas versões, será exibida a seguinte mensagem:

A finalização da matrícula do aluno só será confirmada quando o processo for concluído por meio do portal do Aluno, inserindo o Token enviado pelo e-mail. O e-mail de "Assinatura pendente" deve ser ignorado.

Clique em **Ciente** e **Continuar**

Chegará no e-mail do usuário logado o código de acesso para assinatura do contrato

Será possível **Reenviar e-mail** com código para validação

E-mail com código de acesso para assinatura.

Inclui o código que chegou no e-mail e clicar em OK.

Contrato assinado no TAE

Na matricula pelo portal, ao logar com mesmo usuário que assinou no TAE será apresentado a mensagem abaixo, sendo necessarío apenas clicar em **Finalizar matrícula**.

Matrícula confirmada com sucesso e documento assinado no TAE.

Após finalizar a matricula será marcado no contrato o campo que indica que ele está assinado e será preenchido a data de assinatura.

Em**Anexo/Integração TOTVS Assinatura Eletrônica**o documento terá o status de Finalizado, quando ele for enviado somente para um Assinante, caso seja enviado para mais de um o status estará pendente aguardando a Assinatura eletrônica dos demais. 

Caso os assinantes selecionados possuam o mesmo e-mail e sejam pessoas diferentes, ao tentar enviar o e-mail para assinatura no TOTVS Assinatura Eletrônica o sistema irá emitir mensagem de erro, informando que não é possível enviar pois existem destinatários com e-mail repetido e solicitando que entre em contato com a instituição para fazer o ajuste.

O usuário que estiver logando no portal deverá ter:

* E-mail informado no cadastro
* Usuário marcado como Assinante nos paramêtros Educacional | RM Portal | Matricula | Portal - Assinatura Contrato

Caso não se enquadre será apresentado a mensagem abaixo.

O usuário de nacionalidade Brasileira que estiver logando no portal deverá ter o CPF informado no cadastro, caso não esteja será apresentado a mensagem abaixo.

Após clicar em **Reenviar e-mail,** se a tela se fechar por algum motivo, poderá ser enviado novo token após 5min.

O usuário logado que é responsável financeiro, independe se ele tenha outro papel no sistema, é indicado que ele esteja com o campo "Usuário de acesso" preenchido. Deste modo, possibilita ao sistema identificar corretamente os dados de e-mail e CPF associados ao cadastro de Cliente/Fornecedor que serão utilizados para envio ao TAE.

Situações que será enviado novo documento no TAE

* Documento cancelado no TAE e reenvio de novo documento na matricula pelo portal.
* Após finalização da matricula e documento no TAE e refazer o processo de matricula no portal.
* Envio de documento para e-mail incorreto, correção do e-mail e envio novamente pela matricula no portal.  
  **Mãe, Pai e Responsável Acadêmico:** Correção do e-mail deve ser realizado no cadastro da pessoa  
  **Aluno:** Correção do e-mail deve ser realizado no cadastro do aluno  
  **Responsável Financeiro:** Correção do e-mail deve ser realizado no cadastro do cliente fornecedor
