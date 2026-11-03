---
content_hash: a7842d781e4340737e93cf3a1909f7bb5bea9ce89cc047f67bbdf08511025d04
fetched_at: '2026-06-29T00:09:18.712608+00:00'
page_id: '421388759'
product: rm
source: tdn-rm
title: Associação do Layout do Registro Online
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388759
version: 6
---

Possibilita configurar a fórmula ou valor fixo que será associado a cada cadastro definido no layout de registro online do banco. Essa configuração deve ser associada ao convênio, para que seja possível utilizar fórmula ou valor fixo diferentes para convênios diferentes do mesmo banco.

Na visão de banco no menu anexo | Layout Registro Online realize o cadastro de um novo campo.

É necessário liberar permissão no perfil para o acesso a inclusão, edição e exclusão da Associação dos campos do Registro Online.

Acesse o cadastro de convênio, menu anexos | Associação do Layout do Registro Online inclua um novo Registro, em *Campo do Registro Online* selecione o registro já cadastrado para o banco, após informe a *Fórmula* ou o *Valor fixo*que será utilizado.

O Item 'Campo do registro online' quando salvo, não poderá ser editado*.*

O item 'Fórmula' e 'Valor fixo' pode ser alterado conforme necessidade.

Integração com Processo Seletivo

Ao utilizar 'Fórmula' que contenha chamada para 'Consulta SQL' e o Registro Online seja gerado pela integração com o Novo Portal do Processo Seletivo, o usuário padrão "RMProcessoSeletivo" deve possuir acesso à coligada na qual será registrada a inscrição do candidato, caso contrário ao ser aplicada a segurança padrão do Corpore RM os dados esperados não serão retornados.

No convênio para cada campo do registro online cadastrado no banco é possível incluir uma fórmula ou um valor fixo, sendo que ao incluir uma fórmula o campo valor fixo ficará inativo, e ou ao incluir um valor fixo o campo fórmula ficará inativo, não sendo possível incluir os dois para o mesmo registro.

Veja também

* [Documentação técnica complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=307835775)
